#!/usr/bin/env bash
# Guards the two per-file inventories of doctrine/principles/:
#   1. the "Every Principle At A Glance" section of doctrine/tldr-principles-and-mvp.md
#      lists every active principle file exactly once, links to nothing that does
#      not exist, and uses each file's own H1 (minus any trailing parenthetical)
#      as the link text, so a retitled file fails loudly;
#   2. doctrine/README.md links every active principle file at least once.
# "Active" means the file's first ten lines carry no deprecation or supersession
# banner. principles/README.md, if one is ever added, is not a principle.
# Run from repo root: ./scripts/check-principles-glance.sh
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

GLANCE="doctrine/tldr-principles-and-mvp.md"
README="doctrine/README.md"
PRINCIPLES="doctrine/principles"
HEADING="## Every Principle At A Glance"

for f in "$GLANCE" "$README"; do
  [[ -f "$f" ]] || { echo "error: missing $f" >&2; exit 1; }
done

# Active principle files (basename), sorted.
actual=""
for path in "$PRINCIPLES"/*.md; do
  name="$(basename "$path")"
  [[ "$name" == "README.md" ]] && continue
  if head -n 10 "$path" | grep -qiE 'scheduled for deprecation|superseded by|^> \*\*deprecated'; then
    continue
  fi
  actual+="$name"$'\n'
done
actual="$(printf '%s' "$actual" | sort)"

# Section body: from the glance heading to the next H2 (or end of file).
section="$(awk -v h="$HEADING" '
  $0 == h { on = 1; next }
  on && /^## / { exit }
  on { print }
' "$GLANCE")"
[[ -n "$section" ]] || { echo "error: section '$HEADING' not found in $GLANCE" >&2; exit 1; }

# Links inside the section: "[text](principles/<name>.md)".
links="$(printf '%s\n' "$section" | grep -oE '\[[^]]+\]\(principles/[^)]+\.md\)' || true)"
linked="$(printf '%s\n' "$links" | sed -E 's|.*\]\(principles/([^)]+)\)|\1|' | grep . | sort || true)"

rc=0

missing="$(comm -23 <(printf '%s\n' "$actual") <(printf '%s\n' "$linked" | sort -u))"
if [[ -n "$missing" ]]; then
  echo "error: active principle files with no glance row:" >&2
  printf '  %s\n' $missing >&2
  rc=1
fi

unknown="$(comm -13 <(printf '%s\n' "$actual") <(printf '%s\n' "$linked" | sort -u))"
if [[ -n "$unknown" ]]; then
  echo "error: glance rows linking to files that are missing or carry a deprecation banner:" >&2
  printf '  %s\n' $unknown >&2
  rc=1
fi

dupes="$(printf '%s\n' "$linked" | uniq -d)"
if [[ -n "$dupes" ]]; then
  echo "error: principle files listed more than once in the glance:" >&2
  printf '  %s\n' $dupes >&2
  rc=1
fi

# Link text must equal the file's H1 with any trailing " (...)" removed.
while IFS= read -r link; do
  [[ -n "$link" ]] || continue
  text="$(printf '%s' "$link" | sed -E 's|^\[([^]]+)\]\(.*|\1|')"
  name="$(printf '%s' "$link" | sed -E 's|.*\]\(principles/([^)]+)\)|\1|')"
  path="$PRINCIPLES/$name"
  [[ -f "$path" ]] || continue
  h1="$(grep -m1 -E '^# ' "$path" | sed -E 's|^# ||; s| \([^)]*\)$||')"
  if [[ "$text" != "$h1" ]]; then
    echo "error: glance link text does not match the file title:" >&2
    echo "  $name" >&2
    echo "    row:   $text" >&2
    echo "    title: $h1" >&2
    rc=1
  fi
done <<< "$links"

# README must link every active principle file.
readme_linked="$(grep -oE '\(principles/[^)]+\.md\)' "$README" | tr -d '()' | sed 's|^principles/||' | sort -u || true)"
readme_missing="$(comm -23 <(printf '%s\n' "$actual") <(printf '%s\n' "$readme_linked"))"
if [[ -n "$readme_missing" ]]; then
  echo "error: active principle files not linked from $README:" >&2
  printf '  %s\n' $readme_missing >&2
  rc=1
fi

if [[ $rc -eq 0 ]]; then
  count="$(printf '%s\n' "$actual" | grep -c . || true)"
  echo "OK: glance lists all $count active principle files exactly once with matching titles; README links them all."
fi
exit $rc
