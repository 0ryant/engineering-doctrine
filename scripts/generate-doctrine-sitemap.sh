#!/usr/bin/env bash
# Regenerates doctrine/SITEMAP.md from all Markdown paths under doctrine/.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DOCTRINE="$ROOT/doctrine"
OUT="$DOCTRINE/SITEMAP.md"

if [[ ! -d "$DOCTRINE" ]]; then
  echo "error: missing $DOCTRINE" >&2
  exit 1
fi

tmp="$(mktemp)"
trap 'rm -f "$tmp"' EXIT

{
  printf '%s\n' "# Doctrine sitemap (generated)"
  printf '%s\n' ""
  printf '%s\n' "**Do not edit the file list by hand.** Regenerate after adding, renaming, or removing Markdown under \`doctrine/\`:"
  printf '%s\n' ""
  printf '%s\n' '```bash'
  printf '%s\n' "./scripts/generate-doctrine-sitemap.sh   # POSIX"
  printf '%s\n' "python scripts/generate_doctrine_sitemap.py   # any platform"
  printf '%s\n' '```'
  printf '%s\n' ""
  printf '%s\n' "Generated: $(date -u +"%Y-%m-%d %H:%M UTC")"
  printf '%s\n' ""
  printf '%s\n' "## All Markdown files"
  printf '%s\n' ""

  (cd "$DOCTRINE" && find . -name '*.md' -type f | sed 's|^\./||' | LC_ALL=C sort) | while IFS= read -r rel; do
    printf '%s\n' "- [${rel}](${rel})"
  done
} >"$tmp"

mv "$tmp" "$OUT"
trap - EXIT
echo "Wrote $OUT"
