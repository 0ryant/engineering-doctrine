#!/usr/bin/env python3
"""Validate classified YAML examples embedded in doctrine Markdown.

Every ``yaml`` or ``yml`` fence must have one metadata comment on the line
immediately before it. The comment body is strict JSON in one of these forms::

    <!-- doctrine-example: {"schema":"contracts/example.schema.json"} -->
    <!-- doctrine-example: {"schema":"contracts/example.schema.json","wrapper":"example"} -->
    <!-- doctrine-example: {"partial":"Why this excerpt is syntax-only."} -->
    <!-- doctrine-example: {"external":"Why another system owns semantics."} -->

``schema`` paths are repository-relative local JSON Schema files. A ``wrapper``
means the YAML root must contain exactly that key and its mapping value is the
schema instance. ``partial`` and ``external`` examples are syntax-checked only;
their non-empty reason prevents a syntax check being mistaken for conformance.

The checker never executes example content or retrieves schema references.
External ``$ref``, ``$dynamicRef``, and ``$recursiveRef`` values fail closed.
With no file arguments it checks only Git-tracked Markdown under ``doctrine/``.
The default repository root is derived from this script, so invocation is
independent of the current working directory.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml
from jsonschema import exceptions as jsonschema_exceptions
from jsonschema import validators
from markdown_it import MarkdownIt
from referencing import Registry


COMMENT_PREFIX = "<!-- doctrine-example: "
COMMENT_SUFFIX = " -->"
YAML_TAG = "tag:yaml.org,2002:map"


class DuplicateKeyError(yaml.YAMLError):
    """Raised when YAML contains a duplicate mapping key."""


class DuplicateMetadataKeyError(ValueError):
    """Raised when metadata JSON contains a duplicate object key."""


class StrictSafeLoader(yaml.SafeLoader):
    """SafeLoader variant that rejects duplicate mapping keys."""


def _construct_unique_mapping(
    loader: StrictSafeLoader, node: yaml.nodes.MappingNode, deep: bool = False
) -> dict[Any, Any]:
    loader.flatten_mapping(node)
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            duplicate = key in mapping
        except TypeError as error:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                "found an unhashable mapping key",
                key_node.start_mark,
            ) from error
        if duplicate:
            raise DuplicateKeyError(f"duplicate mapping key {key!r}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictSafeLoader.add_constructor(YAML_TAG, _construct_unique_mapping)


@dataclass
class Totals:
    files: int = 0
    examples: int = 0
    schema: int = 0
    partial: int = 0
    external: int = 0
    errors: list[str] = field(default_factory=list)


def _display_path(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path.resolve())


def _tracked_doctrine_markdown(root: Path) -> list[Path]:
    result = subprocess.run(
        ["git", "-C", str(root), "ls-files", "-z", "--", "doctrine"],
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        message = result.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"git ls-files failed: {message or 'unknown error'}")
    names = result.stdout.decode("utf-8").split("\0")
    return sorted(
        (root / name for name in names if name and Path(name).suffix.lower() == ".md"),
        key=lambda path: path.as_posix(),
    )


def _explicit_paths(root: Path, arguments: list[str]) -> list[Path]:
    paths: list[Path] = []
    for argument in arguments:
        path = Path(argument)
        paths.append(path.resolve() if path.is_absolute() else (root / path).resolve())
    return paths


def _parse_metadata(line: str) -> tuple[str | None, dict[str, Any] | None]:
    if not (line.startswith(COMMENT_PREFIX) and line.endswith(COMMENT_SUFFIX)):
        return "missing doctrine-example metadata", None
    raw = line[len(COMMENT_PREFIX) : -len(COMMENT_SUFFIX)]
    try:
        def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
            result: dict[str, Any] = {}
            for key, value in pairs:
                if key in result:
                    raise DuplicateMetadataKeyError(f"duplicate metadata key {key!r}")
                result[key] = value
            return result

        metadata = json.loads(raw, object_pairs_hook=unique_object)
    except DuplicateMetadataKeyError as error:
        return str(error), None
    except json.JSONDecodeError as error:
        return f"invalid doctrine-example metadata JSON: {error.msg}", None
    if not isinstance(metadata, dict):
        return "doctrine-example metadata must be a JSON object", None

    classes = [name for name in ("schema", "partial", "external") if name in metadata]
    if len(classes) != 1:
        return "unknown doctrine-example metadata: choose exactly one of schema, partial, external", None
    classification = classes[0]
    allowed = {"schema", "wrapper"} if classification == "schema" else {classification}
    unknown = sorted(set(metadata) - allowed)
    if unknown:
        return f"unknown doctrine-example metadata field: {unknown[0]}", None

    value = metadata[classification]
    if not isinstance(value, str) or not value.strip():
        noun = "path" if classification == "schema" else "reason"
        return f"{classification} {noun} must be a non-empty string", None
    if "wrapper" in metadata and (
        not isinstance(metadata["wrapper"], str) or not metadata["wrapper"].strip()
    ):
        return "wrapper must be a non-empty string", None
    return None, metadata


def _load_yaml(content: str) -> tuple[str | None, Any]:
    try:
        return None, yaml.load(content, Loader=StrictSafeLoader)
    except DuplicateKeyError as error:
        return str(error), None
    except yaml.constructor.ConstructorError as error:
        if "could not determine a constructor for the tag" in str(error):
            return f"unknown YAML tag: {error.problem}", None
        return f"malformed YAML: {error.problem or str(error)}", None
    except yaml.YAMLError as error:
        problem = getattr(error, "problem", None)
        return f"malformed YAML: {problem or str(error).splitlines()[0]}", None
    except (ValueError, KeyError, AttributeError) as error:
        return f"malformed YAML: {error}", None


def _external_reference(
    schema: Any, location: str = "$"
) -> tuple[str, str] | None:
    if isinstance(schema, dict):
        for key, value in schema.items():
            child_location = f"{location}.{key}"
            if key in {"$ref", "$dynamicRef", "$recursiveRef"} and (
                not isinstance(value, str) or not value.startswith("#")
            ):
                return key, child_location
            found = _external_reference(value, child_location)
            if found:
                return found
    elif isinstance(schema, list):
        for index, value in enumerate(schema):
            found = _external_reference(value, f"{location}[{index}]")
            if found:
                return found
    return None


def _schema_instance(
    data: Any, metadata: dict[str, Any]
) -> tuple[str | None, Any]:
    wrapper = metadata.get("wrapper")
    if wrapper is None:
        return None, data
    if not isinstance(data, dict) or wrapper not in data:
        return f"wrapper {wrapper!r} is missing", None
    if set(data) != {wrapper}:
        return "wrapper must be the only top-level key", None
    child = data[wrapper]
    if not isinstance(child, dict):
        return f"wrapper {wrapper!r} value must be a mapping", None
    return None, child


def _validate_schema(
    data: Any, metadata: dict[str, Any], root: Path
) -> str | None:
    schema_name = metadata["schema"]
    schema_relative = Path(schema_name)
    if schema_relative.is_absolute() or schema_relative.suffix.lower() != ".json":
        return "schema must be a repository-relative JSON file"
    schema_path = (root / schema_relative).resolve()
    try:
        schema_path.relative_to(root)
    except ValueError:
        return "schema path escapes repository"
    if not schema_path.is_file():
        return f"schema does not exist: {schema_name}"

    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return f"cannot load schema {schema_name}: {error}"
    external_reference = _external_reference(schema)
    if external_reference:
        keyword, ref_location = external_reference
        return f"external {keyword} is forbidden ({schema_name} at {ref_location})"

    instance_error, instance = _schema_instance(data, metadata)
    if instance_error:
        return instance_error
    try:
        validator_class = validators.validator_for(schema)
        validator_class.check_schema(schema)
        errors = sorted(
            validator_class(schema, registry=Registry()).iter_errors(instance),
            key=lambda error: [str(part) for part in error.absolute_path],
        )
    except jsonschema_exceptions.SchemaError as error:
        return f"invalid JSON schema {schema_name}: {error.message}"
    except Exception as error:  # fail closed for unresolved/internal reference faults
        return f"schema validation could not complete: {error}"
    if errors:
        first = errors[0]
        location = ".".join(str(part) for part in first.absolute_path) or "$"
        return f"schema validation failed at {location}: {first.message}"
    return None


def _check_file(path: Path, root: Path, totals: Totals) -> None:
    display = _display_path(path, root)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as error:
        totals.errors.append(f"{display}: cannot read Markdown: {error}")
        return
    lines = text.splitlines()
    for token in MarkdownIt("commonmark").parse(text):
        if token.type != "fence":
            continue
        language = token.info.strip().split(maxsplit=1)[0].lower() if token.info.strip() else ""
        if language not in {"yaml", "yml"}:
            continue
        totals.examples += 1
        fence_line = token.map[0] + 1 if token.map else 1
        previous = lines[fence_line - 2] if fence_line >= 2 else ""
        metadata_error, metadata = _parse_metadata(previous)
        yaml_error, data = _load_yaml(token.content)
        if metadata_error:
            totals.errors.append(f"{display}:{fence_line}: {metadata_error}")
        if yaml_error:
            totals.errors.append(f"{display}:{fence_line}: {yaml_error}")
        if metadata is None:
            continue

        classification = next(key for key in ("schema", "partial", "external") if key in metadata)
        setattr(totals, classification, getattr(totals, classification) + 1)
        if yaml_error or classification != "schema":
            continue
        schema_error = _validate_schema(data, metadata, root)
        if schema_error:
            totals.errors.append(f"{display}:{fence_line}: {schema_error}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Check classified YAML examples in doctrine Markdown.",
        epilog=(
            'Metadata syntax: <!-- doctrine-example: {"schema":"contracts/x.schema.json",'
            '"wrapper":"optional"} -->, or one non-empty partial/external reason.'
        ),
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="repository root (default: parent of this script's directory)",
    )
    parser.add_argument(
        "files",
        nargs="*",
        help="Markdown files to check; default: Git-tracked doctrine/**/*.md",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.root.resolve()
    try:
        paths = _explicit_paths(root, args.files) if args.files else _tracked_doctrine_markdown(root)
    except RuntimeError as error:
        print(error)
        return 1

    totals = Totals(files=len(paths))
    for path in paths:
        _check_file(path, root, totals)
    for error in totals.errors:
        print(error)
    print(
        f"checked {totals.examples} YAML example(s) in {totals.files} Markdown file(s): "
        f"{totals.schema} schema, {totals.partial} partial, {totals.external} external, "
        f"{len(totals.errors)} error(s)"
    )
    return 1 if totals.errors else 0


if __name__ == "__main__":
    sys.exit(main())
