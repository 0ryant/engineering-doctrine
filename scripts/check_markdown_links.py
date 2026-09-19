#!/usr/bin/env python3
"""Check local targets referenced by repository Markdown files."""

from __future__ import annotations

import argparse
import subprocess
import unicodedata
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from markdown_it import MarkdownIt


MARKDOWN = MarkdownIt("commonmark", {"html": True})


class ExplicitAnchorParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.anchors: set[str] = set()

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        if tag.lower() != "a":
            return
        values = dict(attrs)
        for attribute in ("id", "name"):
            if values.get(attribute):
                self.anchors.add(values[attribute] or "")


def tracked_markdown(root: Path) -> list[Path]:
    result = subprocess.run(
        ["git", "-C", str(root), "ls-files", "-z", "--", "*.md"],
        check=True,
        capture_output=True,
        encoding="utf-8",
        text=True,
    )
    return [root / name for name in result.stdout.split("\0") if name]


def iter_local_targets(path: Path) -> list[tuple[int, str]]:
    tokens = MARKDOWN.parse(path.read_text(encoding="utf-8"))
    targets: list[tuple[int, str]] = []
    for token in tokens:
        if token.type != "inline" or token.map is None:
            continue
        for child in token.children or []:
            if child.type == "link_open":
                target = child.attrGet("href")
            elif child.type == "image":
                target = child.attrGet("src")
            else:
                continue
            if target is None:
                continue
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            targets.append((token.map[0] + 1, target))
    return targets


def github_slug(value: str) -> str:
    retained: list[str] = []
    for character in value.lower():
        category = unicodedata.category(character)
        if (
            character in {" ", "-"}
            or category[0] in {"L", "M", "N"}
            or category == "Pc"
        ):
            retained.append(character)
    return "".join(retained).replace(" ", "-")


def engineering_anchors(path: Path) -> set[str]:
    source = path.read_text(encoding="utf-8")
    tokens = MARKDOWN.parse(source)
    anchors: set[str] = set()
    for index, token in enumerate(tokens[:-1]):
        if token.type != "heading_open" or tokens[index + 1].type != "inline":
            continue
        visible = "".join(
            child.content
            for child in tokens[index + 1].children or []
            if child.type in {"text", "code_inline", "image"}
        )
        base = github_slug(visible)
        candidate = base
        suffix = 1
        while candidate in anchors:
            candidate = f"{base}-{suffix}"
            suffix += 1
        anchors.add(candidate)

    explicit = ExplicitAnchorParser()
    for token in tokens:
        if token.type == "html_block":
            explicit.feed(token.content)
        elif token.type == "inline":
            for child in token.children or []:
                if child.type == "html_inline":
                    explicit.feed(child.content)
    explicit.close()
    return anchors | explicit.anchors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="Markdown files to check")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root (defaults to the script's repository)",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    files = (
        [Path(item) if Path(item).is_absolute() else root / item for item in args.paths]
        if args.paths
        else tracked_markdown(root)
    )

    diagnostics: list[str] = []
    target_count = 0
    engineering_path = (root / "ENGINEERING.md").resolve()
    anchors = (
        engineering_anchors(engineering_path) if engineering_path.is_file() else set()
    )
    for path in sorted(files):
        for line, raw_target in iter_local_targets(path):
            target_count += 1
            parsed = urlsplit(raw_target)
            target_path = (
                path.parent / unquote(parsed.path) if parsed.path else path
            ).resolve()
            display_path = path.resolve().relative_to(root).as_posix()
            if not target_path.is_relative_to(root):
                diagnostics.append(
                    f"{display_path}:{line}: local target escapes repository: {raw_target}"
                )
            elif not target_path.exists():
                diagnostics.append(
                    f"{display_path}:{line}: missing local target: {raw_target}"
                )
            elif (
                target_path == engineering_path
                and parsed.fragment
                and unquote(parsed.fragment) not in anchors
            ):
                diagnostics.append(
                    f"{display_path}:{line}: missing ENGINEERING.md anchor: "
                    f"{unquote(parsed.fragment)}"
                )

    for diagnostic in diagnostics:
        print(diagnostic)
    print(
        f"checked {len(files)} Markdown file(s), {target_count} local target(s): "
        f"{len(diagnostics)} error(s)"
    )
    return 1 if diagnostics else 0


if __name__ == "__main__":
    raise SystemExit(main())
