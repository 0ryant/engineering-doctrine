#!/usr/bin/env bash
# Preflight for doctrine library edits: regenerate sitemap and print harness reminders.
# Run from repo root: ./scripts/doctrine-change-preflight.sh
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "== doctrine-change-preflight =="
if [[ ! -f "doctrine/patterns/doctrine-library-change-harness.md" ]]; then
  echo "error: expected doctrine/patterns/doctrine-library-change-harness.md" >&2
  exit 1
fi

./scripts/generate-doctrine-sitemap.sh

echo ""
echo "Manual checks (see doctrine/patterns/doctrine-library-change-harness.md):"
echo "  [ ] ADR created/updated in docs/adr/ + index, or editorial-only skip documented"
echo "  [ ] Research note or external refs in doc + REFERENCES.md as needed"
echo "  [ ] glossary.md, doctrine/README.md, ENGINEERING.md / tldr — if discoverability changes"
echo "  [ ] doctrine/checklists/doctrine-change-checklist.md"
echo "OK: sitemap regenerated."
