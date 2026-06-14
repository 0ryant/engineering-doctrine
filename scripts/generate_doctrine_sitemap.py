#!/usr/bin/env python3
"""Regenerate doctrine/SITEMAP.md from all Markdown paths under doctrine/.

Cross-platform port of scripts/generate-doctrine-sitemap.sh so the mandatory
preflight runs on Windows (PowerShell) as well as POSIX shells without WSL or
Git-Bash. Python is already a repo dependency (see requirements.txt), so this
adds no new toolchain.

Output is byte-for-byte equivalent to the bash generator:
  - forward-slash relative paths under doctrine/
  - C-locale (bytewise) sort
  - UTC timestamp "YYYY-MM-DD HH:MM UTC"
  - LF line endings

Usage (from anywhere):
    python scripts/generate_doctrine_sitemap.py
    python scripts/generate_doctrine_sitemap.py --check
"""

from __future__ import annotations

import argparse
import datetime as _dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCTRINE = ROOT / "doctrine"
OUT = DOCTRINE / "SITEMAP.md"
GENERATED_RE = re.compile(r"^Generated: (.+)$", re.MULTILINE)


def collect_markdown(doctrine: Path) -> list[str]:
    rels = [
        p.relative_to(doctrine).as_posix()
        for p in doctrine.rglob("*.md")
        if p.is_file()
    ]
    # C-locale (bytewise) sort to match `LC_ALL=C sort` in the bash version.
    return sorted(rels, key=lambda s: s.encode("utf-8"))


def render(files: list[str], generated: str) -> str:
    lines = [
        "# Doctrine sitemap (generated)",
        "",
        "**Do not edit the file list by hand.** Regenerate after adding, "
        "renaming, or removing Markdown under `doctrine/`:",
        "",
        "```bash",
        "./scripts/generate-doctrine-sitemap.sh   # POSIX",
        "python scripts/generate_doctrine_sitemap.py   # any platform",
        "```",
        "",
        f"Generated: {generated}",
        "",
        "## All Markdown files",
        "",
    ]
    lines += [f"- [{rel}]({rel})" for rel in files]
    return "\n".join(lines) + "\n"


def existing_generated_timestamp() -> str | None:
    if not OUT.exists():
        return None
    match = GENERATED_RE.search(OUT.read_text(encoding="utf-8"))
    if match is None:
        return None
    return match.group(1)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify doctrine/SITEMAP.md without rewriting its generated timestamp",
    )
    args = parser.parse_args(argv)

    if not DOCTRINE.is_dir():
        print(f"error: missing {DOCTRINE}", file=sys.stderr)
        return 1
    if args.check:
        generated = existing_generated_timestamp()
        if generated is None:
            print(f"error: missing generated timestamp in {OUT}", file=sys.stderr)
            return 1
        expected = render(collect_markdown(DOCTRINE), generated)
        actual = OUT.read_text(encoding="utf-8").replace("\r\n", "\n")
        if actual != expected:
            print(f"error: {OUT} is not up to date", file=sys.stderr)
            return 1
        print(f"{OUT} is up to date")
        return 0

    generated = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    content = render(collect_markdown(DOCTRINE), generated)
    OUT.write_text(content, encoding="utf-8", newline="\n")
    print(f"Wrote {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
