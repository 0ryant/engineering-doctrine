from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


CHECKER = Path(__file__).resolve().parents[1] / "check_doctrine_examples.py"


class DoctrineExampleCheckerCliTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        subprocess.run(["git", "init", "--quiet", str(self.root)], check=True)
        self.write(
            "contracts/example.schema.json",
            """{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": false,
  "required": ["name"],
  "properties": {"name": {"type": "string", "minLength": 1}}
}
""",
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def write(self, relative_path: str, content: str, *, tracked: bool = True) -> Path:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        if tracked:
            subprocess.run(
                ["git", "-C", str(self.root), "add", "--", relative_path],
                check=True,
            )
        return path

    def run_checker(
        self, *args: str, cwd: Path | None = None
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(CHECKER), "--root", str(self.root), *args],
            cwd=cwd,
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
            capture_output=True,
            encoding="utf-8",
            text=True,
            check=False,
        )

    def test_accepts_schema_partial_external_and_both_yaml_labels(self) -> None:
        self.write(
            "doctrine/examples.md",
            """<!-- doctrine-example: {"schema":"contracts/example.schema.json","wrapper":"example"} -->
```yaml
example:
  name: complete
```

<!-- doctrine-example: {"partial":"Excerpt omits the enclosing contract."} -->
```yml
name: syntax-only
```

<!-- doctrine-example: {"external":"Prometheus owns runtime semantics; syntax only."} -->
```yaml
- record: example:ratio
  expr: sum(rate(example_total[5m]))
```
""",
        )

        result = self.run_checker()

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(
            "checked 3 YAML example(s) in 1 Markdown file(s): "
            "1 schema, 1 partial, 1 external, 0 error(s)",
            result.stdout,
        )
        self.assertEqual(result.stderr, "")

    def test_rejects_malformed_yaml(self) -> None:
        path = self.write(
            "fixture.md",
            """<!-- doctrine-example: {"partial":"A deliberately small excerpt."} -->
```yaml
name: [unterminated
```
""",
            tracked=False,
        )

        result = self.run_checker(str(path))

        self.assertEqual(result.returncode, 1)
        self.assertIn("fixture.md:2: malformed YAML", result.stdout)

    def test_rejects_invalid_typed_scalar_without_traceback(self) -> None:
        cases = {
            "invalid date": "date: 2026-02-30",
            "invalid integer": "value: !!int invalid",
            "invalid boolean": "value: !!bool invalid",
            "invalid timestamp": "value: !!timestamp invalid",
            "invalid float": "value: !!float invalid",
        }
        for label, yaml_line in cases.items():
            with self.subTest(label=label):
                path = self.write(
                    "invalid-scalar.md",
                    f"""<!-- doctrine-example: {{"partial":"A deliberately small excerpt."}} -->
```yaml
{yaml_line}
```
""",
                    tracked=False,
                )

                check_process = self.run_checker(str(path))

                self.assertEqual(
                    check_process.returncode,
                    1,
                    check_process.stdout + check_process.stderr,
                )
                self.assertIn(
                    "invalid-scalar.md:2: malformed YAML",
                    check_process.stdout,
                )
                self.assertIn(
                    "checked 1 YAML example(s) in 1 Markdown file(s): "
                    "0 schema, 1 partial, 0 external, 1 error(s)",
                    check_process.stdout,
                )
                self.assertEqual(check_process.stderr, "")

    def test_rejects_duplicate_mapping_keys(self) -> None:
        self.write(
            "doctrine/duplicate.md",
            """<!-- doctrine-example: {"partial":"A deliberately small excerpt."} -->
```yaml
name: first
name: second
```
""",
        )

        result = self.run_checker()

        self.assertEqual(result.returncode, 1)
        self.assertIn("duplicate mapping key 'name'", result.stdout)

    def test_rejects_unknown_yaml_tags(self) -> None:
        self.write(
            "doctrine/tag.md",
            """<!-- doctrine-example: {"partial":"A deliberately small excerpt."} -->
```yaml
name: !execute echo-no
```
""",
        )

        result = self.run_checker()

        self.assertEqual(result.returncode, 1)
        self.assertIn("unknown YAML tag", result.stdout)

    def test_rejects_schema_invalid_instance(self) -> None:
        self.write(
            "doctrine/invalid.md",
            """<!-- doctrine-example: {"schema":"contracts/example.schema.json"} -->
```yaml
unexpected: true
```
""",
        )

        result = self.run_checker()

        self.assertEqual(result.returncode, 1)
        self.assertIn("schema validation failed", result.stdout)

    def test_rejects_missing_and_unknown_classification(self) -> None:
        self.write(
            "missing.md",
            """```yaml
name: missing
```
""",
            tracked=False,
        )
        self.write(
            "unknown.md",
            """<!-- doctrine-example: {"mystery":"not a supported class"} -->
```yaml
name: unknown
```
""",
            tracked=False,
        )

        missing = self.run_checker("missing.md")
        unknown = self.run_checker("unknown.md")

        self.assertEqual(missing.returncode, 1)
        self.assertIn("missing doctrine-example metadata", missing.stdout)
        self.assertEqual(unknown.returncode, 1)
        self.assertIn("unknown doctrine-example metadata", unknown.stdout)

    def test_rejects_missing_or_outside_root_schema(self) -> None:
        outside = self.root.parent / f"{self.root.name}-outside.schema.json"
        outside.write_text('{"type":"object"}\n', encoding="utf-8")
        self.addCleanup(outside.unlink, missing_ok=True)
        missing_path = self.write(
            "missing-schema.md",
            """<!-- doctrine-example: {"schema":"contracts/missing.schema.json"} -->
```yaml
name: example
```
""",
            tracked=False,
        )
        outside_path = self.write(
            "outside-schema.md",
            f"""<!-- doctrine-example: {{"schema":"../{outside.name}"}} -->
```yaml
name: example
```
""",
            tracked=False,
        )

        missing = self.run_checker(str(missing_path))
        escaped = self.run_checker(str(outside_path))

        self.assertEqual(missing.returncode, 1)
        self.assertIn("schema does not exist", missing.stdout)
        self.assertEqual(escaped.returncode, 1)
        self.assertIn("schema path escapes repository", escaped.stdout)

    def test_wrapper_must_be_the_only_top_level_key(self) -> None:
        missing_wrapper = self.write(
            "missing-wrapper.md",
            """<!-- doctrine-example: {"schema":"contracts/example.schema.json","wrapper":"example"} -->
```yaml
name: hidden-by-wrapper
```
""",
            tracked=False,
        )
        extra_key = self.write(
            "extra-wrapper-key.md",
            """<!-- doctrine-example: {"schema":"contracts/example.schema.json","wrapper":"example"} -->
```yaml
example:
  name: visible
hidden:
  name: must-not-be-ignored
```
""",
            tracked=False,
        )

        missing = self.run_checker(str(missing_wrapper))
        extra = self.run_checker(str(extra_key))

        self.assertEqual(missing.returncode, 1)
        self.assertIn("wrapper 'example' is missing", missing.stdout)
        self.assertEqual(extra.returncode, 1)
        self.assertIn("wrapper must be the only top-level key", extra.stdout)

    def test_rejects_external_schema_ref_without_network_access(self) -> None:
        self.write(
            "contracts/remote.schema.json",
            '{"$ref":"https://example.invalid/must-not-fetch.json"}\n',
        )
        self.write(
            "doctrine/remote.md",
            """<!-- doctrine-example: {"schema":"contracts/remote.schema.json"} -->
```yaml
name: example
```
""",
        )

        result = self.run_checker()

        self.assertEqual(result.returncode, 1)
        self.assertIn("external $ref is forbidden", result.stdout)

    def test_rejects_external_dynamic_ref_without_network_access(self) -> None:
        self.write(
            "contracts/remote-dynamic.schema.json",
            """{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$dynamicRef": "https://example.invalid/must-not-fetch.json#node"
}
""",
        )
        self.write(
            "doctrine/remote-dynamic.md",
            """<!-- doctrine-example: {"schema":"contracts/remote-dynamic.schema.json"} -->
```yaml
name: example
```
""",
        )

        result = self.run_checker()

        self.assertEqual(result.returncode, 1)
        self.assertIn("external $dynamicRef is forbidden", result.stdout)

    def test_rejects_duplicate_metadata_keys(self) -> None:
        self.write(
            "doctrine/duplicate-metadata.md",
            """<!-- doctrine-example: {"partial":"first reason","partial":"hidden replacement"} -->
```yaml
name: example
```
""",
        )

        result = self.run_checker()

        self.assertEqual(result.returncode, 1)
        self.assertIn("duplicate metadata key 'partial'", result.stdout)

    def test_default_scan_uses_only_tracked_doctrine_markdown(self) -> None:
        self.write(
            "doctrine/classified.md",
            """<!-- doctrine-example: {"partial":"A deliberately small excerpt."} -->
```yaml
name: tracked
```
""",
        )
        self.write(
            "doctrine/new.md",
            """```yaml
name: newly-added
```
""",
            tracked=False,
        )

        before_add = self.run_checker()
        subprocess.run(
            ["git", "-C", str(self.root), "add", "--", "doctrine/new.md"],
            check=True,
        )
        after_add = self.run_checker()

        self.assertEqual(before_add.returncode, 0, before_add.stdout)
        self.assertEqual(after_add.returncode, 1)
        self.assertIn("doctrine/new.md:1: missing doctrine-example metadata", after_add.stdout)

    def test_default_root_is_independent_of_current_working_directory(self) -> None:
        copied_checker = self.root / "scripts" / "check_doctrine_examples.py"
        copied_checker.parent.mkdir(parents=True, exist_ok=True)
        copied_checker.write_text(CHECKER.read_text(encoding="utf-8"), encoding="utf-8")
        self.write(
            "doctrine/example.md",
            """<!-- doctrine-example: {"schema":"contracts/example.schema.json"} -->
```yaml
name: from-any-cwd
```
""",
        )

        result = subprocess.run(
            [sys.executable, str(copied_checker)],
            cwd=self.root.parent,
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
            capture_output=True,
            encoding="utf-8",
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("checked 1 YAML example(s)", result.stdout)

    def test_metadata_must_be_immediate_and_has_no_unknown_fields(self) -> None:
        separated = self.write(
            "separated.md",
            """<!-- doctrine-example: {"partial":"Too far from the fence."} -->

```yaml
name: example
```
""",
            tracked=False,
        )
        unknown_field = self.write(
            "unknown-field.md",
            """<!-- doctrine-example: {"schema":"contracts/example.schema.json","typo":true} -->
```yaml
name: example
```
""",
            tracked=False,
        )

        gap = self.run_checker(str(separated))
        extra = self.run_checker(str(unknown_field))

        self.assertEqual(gap.returncode, 1)
        self.assertIn("missing doctrine-example metadata", gap.stdout)
        self.assertEqual(extra.returncode, 1)
        self.assertIn("unknown doctrine-example metadata field", extra.stdout)


if __name__ == "__main__":
    unittest.main()
