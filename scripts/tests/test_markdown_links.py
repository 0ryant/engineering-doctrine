from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


CHECKER = Path(__file__).resolve().parents[1] / "check_markdown_links.py"


class MarkdownLinkCheckerCliTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        subprocess.run(
            ["git", "init", "--quiet", str(self.root)],
            check=True,
            text=True,
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
                text=True,
            )
        return path

    def run_checker(
        self,
        *args: str,
        cwd: Path | None = None,
        environment: dict[str, str] | None = None,
    ) -> subprocess.CompletedProcess[str]:
        child_environment = {**os.environ, "PYTHONIOENCODING": "utf-8"}
        child_environment.update(environment or {})
        return subprocess.run(
            [sys.executable, str(CHECKER), "--root", str(self.root), *args],
            cwd=cwd,
            env=child_environment,
            capture_output=True,
            encoding="utf-8",
            text=True,
            check=False,
        )

    def test_reports_missing_local_link_with_line_and_summary(self) -> None:
        self.write("README.md", "[missing](docs/missing.md)\n")

        check_process = self.run_checker()

        self.assertEqual(check_process.returncode, 1, check_process.stdout + check_process.stderr)
        self.assertIn(
            "README.md:1: missing local target: docs/missing.md",
            check_process.stdout,
        )
        self.assertTrue(
            check_process.stdout.endswith(
                "checked 1 Markdown file(s), 1 local target(s): 1 error(s)\n"
            ),
            check_process.stdout,
        )
        self.assertEqual(check_process.stderr, "")

    def test_accepts_encoded_paths_directories_images_and_reference_links(self) -> None:
        self.write("docs/space name.md", "# Space\n")
        self.write("docs/guide.md", "# Guide\n")
        self.write("assets/logo one.png", "not really an image\n")
        self.write(
            "README.md",
            "\n".join(
                [
                    "[space](docs/space%20name.md)",
                    "[directory](docs/)",
                    "![logo](assets/logo%20one.png)",
                    "[guide][guide-ref]",
                    "",
                    "[guide-ref]: docs/guide.md",
                    "",
                ]
            ),
        )

        check_process = self.run_checker()

        self.assertEqual(check_process.returncode, 0, check_process.stdout + check_process.stderr)
        self.assertTrue(
            check_process.stdout.endswith(
                "checked 3 Markdown file(s), 4 local target(s): 0 error(s)\n"
            ),
            check_process.stdout,
        )

    def test_ignores_links_in_code_and_html_comments(self) -> None:
        self.write(
            "README.md",
            "\n".join(
                [
                    "`[inline](missing-inline.md)`",
                    "",
                    "```md",
                    "[fenced](missing-fenced.md)",
                    "```",
                    "",
                    "<!-- [comment](missing-comment.md) -->",
                    "",
                ]
            ),
        )

        check_process = self.run_checker()

        self.assertEqual(check_process.returncode, 0, check_process.stdout + check_process.stderr)
        self.assertIn("0 local target(s): 0 error(s)", check_process.stdout)

    def test_ignores_external_and_scheme_targets(self) -> None:
        self.write(
            "README.md",
            " ".join(
                [
                    "[https](https://example.com)",
                    "[mail](mailto:test@example.com)",
                    "[protocol-relative](//example.com/path)",
                    "![data](data:image/png;base64,AA)",
                ]
            )
            + "\n",
        )

        check_process = self.run_checker()

        self.assertEqual(check_process.returncode, 0, check_process.stdout + check_process.stderr)
        self.assertIn("0 local target(s): 0 error(s)", check_process.stdout)

    def test_rejects_target_that_escapes_repository_even_when_it_exists(self) -> None:
        outside = self.root.parent / f"{self.root.name}-outside.md"
        outside.write_text("# Outside\n", encoding="utf-8")
        self.addCleanup(outside.unlink, missing_ok=True)
        self.write("README.md", f"[outside](../{outside.name})\n")

        check_process = self.run_checker()

        self.assertEqual(check_process.returncode, 1, check_process.stdout + check_process.stderr)
        self.assertIn(
            f"README.md:1: local target escapes repository: ../{outside.name}",
            check_process.stdout,
        )

    def test_checks_only_git_tracked_markdown_by_default(self) -> None:
        self.write(".gitignore", "ignored.md\n")
        self.write("README.md", "# Tracked\n")
        self.write("ignored.md", "[broken](missing.md)\n", tracked=False)

        check_process = self.run_checker()

        self.assertEqual(check_process.returncode, 0, check_process.stdout + check_process.stderr)
        self.assertIn(
            "checked 1 Markdown file(s), 0 local target(s): 0 error(s)",
            check_process.stdout,
        )

    def test_tracked_non_ascii_filename_is_decoded_as_utf8(self) -> None:
        self.write("docs/café.md", "# Café\n")

        check_process = self.run_checker(
            environment=(
                {
                    "LC_ALL": "C",
                    "PYTHONCOERCECLOCALE": "0",
                    "PYTHONUTF8": "0",
                }
                if os.name == "nt"
                else None
            )
        )

        self.assertEqual(check_process.returncode, 0, check_process.stdout + check_process.stderr)
        self.assertIn(
            "checked 1 Markdown file(s), 0 local target(s): 0 error(s)",
            check_process.stdout,
        )

    def test_explicit_path_checks_an_untracked_fixture(self) -> None:
        self.write("fixture.md", "[broken](missing.md)\n", tracked=False)

        check_process = self.run_checker("fixture.md")

        self.assertEqual(check_process.returncode, 1, check_process.stdout + check_process.stderr)
        self.assertIn("fixture.md:1: missing local target: missing.md", check_process.stdout)

    def test_default_root_is_independent_of_current_working_directory(self) -> None:
        copied_checker = self.root / "scripts" / "check_markdown_links.py"
        copied_checker.parent.mkdir(parents=True)
        copied_checker.write_text(CHECKER.read_text(encoding="utf-8"), encoding="utf-8")
        self.write("README.md", "# Tracked\n")

        check_process = subprocess.run(
            [sys.executable, str(copied_checker)],
            cwd=self.root.parent,
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
            capture_output=True,
            encoding="utf-8",
            text=True,
            check=False,
        )

        self.assertEqual(check_process.returncode, 0, check_process.stdout + check_process.stderr)
        self.assertIn("checked 1 Markdown file(s)", check_process.stdout)

    def test_rejects_missing_engineering_anchor(self) -> None:
        self.write("ENGINEERING.md", "# Engineering Doctrine\n")
        self.write("README.md", "[bad](ENGINEERING.md#not-a-real-heading)\n")

        check_process = self.run_checker()

        self.assertEqual(check_process.returncode, 1, check_process.stdout + check_process.stderr)
        self.assertIn(
            "README.md:1: missing ENGINEERING.md anchor: not-a-real-heading",
            check_process.stdout,
        )

    def test_accepts_current_engineering_heading_anchor(self) -> None:
        self.write(
            "ENGINEERING.md",
            "# Engineering Doctrine\n\n## Core Propositions\n",
        )
        self.write("README.md", "[core](ENGINEERING.md#core-propositions)\n")

        check_process = self.run_checker()

        self.assertEqual(check_process.returncode, 0, check_process.stdout + check_process.stderr)

    def test_engineering_slugs_match_github_punctuation_and_duplicates(self) -> None:
        self.write(
            "ENGINEERING.md",
            "\n".join(
                [
                    "# Engineering Doctrine",
                    "",
                    "## API: Ready?",
                    "",
                    "## Repeat!",
                    "",
                    "## Repeat!",
                    "",
                    '<a id="manual-anchor"></a>',
                    "",
                ]
            ),
        )
        self.write(
            "README.md",
            " ".join(
                [
                    "[punctuation](ENGINEERING.md#api-ready)",
                    "[duplicate](ENGINEERING.md#repeat-1)",
                    "[explicit](ENGINEERING.md#manual-anchor)",
                ]
            )
            + "\n",
        )

        check_process = self.run_checker()

        self.assertEqual(check_process.returncode, 0, check_process.stdout + check_process.stderr)

    def test_same_document_engineering_anchor_is_checked(self) -> None:
        self.write(
            "ENGINEERING.md",
            "# Engineering Doctrine\n\n[bad](#missing-local-anchor)\n",
        )

        check_process = self.run_checker()

        self.assertEqual(check_process.returncode, 1, check_process.stdout + check_process.stderr)
        self.assertIn(
            "ENGINEERING.md:3: missing ENGINEERING.md anchor: missing-local-anchor",
            check_process.stdout,
        )

    def test_anchor_markup_in_inline_code_is_not_an_explicit_anchor(self) -> None:
        self.write(
            "ENGINEERING.md",
            '# Engineering Doctrine\n\n`<a id="inline-ghost"></a>`\n',
        )
        self.write("README.md", "[ghost](ENGINEERING.md#inline-ghost)\n")

        check_process = self.run_checker()

        self.assertEqual(check_process.returncode, 1, check_process.stdout + check_process.stderr)
        self.assertIn(
            "README.md:1: missing ENGINEERING.md anchor: inline-ghost",
            check_process.stdout,
        )

    def test_anchor_markup_in_fenced_code_is_not_an_explicit_anchor(self) -> None:
        self.write(
            "ENGINEERING.md",
            "\n".join(
                [
                    "# Engineering Doctrine",
                    "",
                    "```html",
                    '<a id="fenced-ghost"></a>',
                    "```",
                    "",
                ]
            ),
        )
        self.write("README.md", "[ghost](ENGINEERING.md#fenced-ghost)\n")

        check_process = self.run_checker()

        self.assertEqual(check_process.returncode, 1, check_process.stdout + check_process.stderr)
        self.assertIn(
            "README.md:1: missing ENGINEERING.md anchor: fenced-ghost",
            check_process.stdout,
        )

    def test_engineering_slug_strips_copyright_symbol(self) -> None:
        self.write("ENGINEERING.md", "# Engineering Doctrine\n\n## A©B\n")
        self.write("README.md", "[symbol](ENGINEERING.md#ab)\n")

        check_process = self.run_checker()

        self.assertEqual(check_process.returncode, 0, check_process.stdout + check_process.stderr)

    def test_engineering_slug_preserves_unicode_letters_but_strips_symbols(self) -> None:
        self.write(
            "ENGINEERING.md",
            "# Engineering Doctrine\n\n## Привет ♥ 東京 — Café\n",
        )
        self.write(
            "README.md",
            "[unicode](ENGINEERING.md#привет--東京--café)\n",
        )

        check_process = self.run_checker()

        self.assertEqual(check_process.returncode, 0, check_process.stdout + check_process.stderr)


if __name__ == "__main__":
    unittest.main()
