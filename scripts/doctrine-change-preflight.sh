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
./scripts/check-principles-glance.sh

if [[ -d doctrine/skills ]]; then
  if [[ -n "${PYTHON_BIN:-}" ]]; then
    PYTHON=("$PYTHON_BIN")
  elif command -v python3 >/dev/null 2>&1; then
    PYTHON=(python3)
  elif command -v python >/dev/null 2>&1; then
    PYTHON=(python)
  elif command -v py >/dev/null 2>&1; then
    PYTHON=(py -3)
  else
    echo "error: Python 3 is required to validate doctrine skills" >&2
    echo "hint: install Python 3 or set PYTHON_BIN to its executable" >&2
    exit 1
  fi

  "${PYTHON[@]}" scripts/validate-skills.py
fi

echo ""
echo "Manual checks (see doctrine/patterns/doctrine-library-change-harness.md):"
echo "  [ ] ADR created/updated in docs/adr/ + index, or editorial-only skip documented"
echo "  [ ] Research note or external refs in doc + REFERENCES.md as needed"
echo "  [ ] glossary.md, doctrine/README.md, ENGINEERING.md / tldr — if discoverability changes"
echo "  [ ] doctrine/checklists/doctrine-change-checklist.md"
echo "OK: sitemap current."
