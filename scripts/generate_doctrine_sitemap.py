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
"""

from __future__ import annotations

import datetime as _dt
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCTRINE = ROOT / "doctrine"
OUT = DOCTRINE / "SITEMAP.md"


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


def main() -> int:
    if not DOCTRINE.is_dir():
        print(f"error: missing {DOCTRINE}", file=sys.stderr)
        return 1
    generated = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    content = render(collect_markdown(DOCTRINE), generated)
    OUT.write_text(content, encoding="utf-8", newline="\n")
    print(f"Wrote {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
