# Doctrine Change Checklist

Use when **adding or substantially editing** files under `doctrine/` or the umbrella `ENGINEERING.md`.

```text
[ ] Change belongs in principles (timeless) vs tooling (illustrative) vs estates (vendor-specific) — see principles/timeless-principles-and-tooling.md
[ ] If principle changed: rationale and references updated; not just opinion
[ ] If umbrella ENGINEERING.md changed: principle file exists or is intentionally summary-only; no new prescriptive vendor picks in principles
[ ] Cross-links added from related principles/patterns (avoid orphan pages)
[ ] REFERENCES.md internal map updated if new first-class doc
[ ] doctrine/SITEMAP.md regenerated: ./scripts/generate-doctrine-sitemap.sh
[ ] doctrine/README.md Start Here or section lists updated when files are added/removed
[ ] Checklists updated if new obligation for adopting teams
[ ] Change class labelled for consumer impact: editorial / navigation / additive guidance / normative tightening / normative replacement / estate-only / deprecation
[ ] Migration notes added for normative tightening, replacement, deprecation, or removal
[ ] evolution/moscow-review.md or decision note updated for large shifts (optional but encouraged)
[ ] evolution/honest-review-synthesis.md updated when absorbing a substantive external review of the library
[ ] For material doctrine releases: update [CHANGELOG.md](../../CHANGELOG.md) at the tag; note version or date in evolution/moscow-review.md or a short decision log entry (optional but encouraged); classify release kind using patterns/doctrine-versioning-and-consumer-compatibility.md
```
