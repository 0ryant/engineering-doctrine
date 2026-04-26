# 0003. Split Doctrine Into Principles, Patterns, Tooling, Checklists, And Evolution

Status: Accepted (retrospective)  
Decision date: 2026-04-07  
Recorded date: 2026-04-26  
Retrospective: Yes

## Context

The library expanded from a small build doctrine into a broader engineering reference. That expansion introduced many topic files plus navigation, references, generated sitemap, change checklist, estate tooling, and evolution notes.

Evidence:

- Commit `6d4fb83` — "Expand doctrine: principles, patterns, tooling, adoption, and governance" (`2026-04-07`)
- Files introduced included `doctrine/principles/timeless-principles-and-tooling.md`, `doctrine/patterns/how-to-read-this-doctrine.md`, `doctrine/REFERENCES.md`, `doctrine/SITEMAP.md`, `doctrine/checklists/doctrine-change-checklist.md`, `doctrine/evolution/moscow-review.md`, and `scripts/generate-doctrine-sitemap.sh`

## Decision

Organise the library by **layer**, not by programme or vendor:

- `principles/` for durable, platform-agnostic intent.
- `patterns/` for compositional guidance.
- `tooling/` for illustrative implementations.
- `tooling/estates/` for optional estate-specific supplements.
- `checklists/` for reviewable execution.
- `evolution/` for research, audits, and change rationale.

## Consequences

- New cross-cutting topics should normally be added as files inside existing layers, not as new top-level doctrine layers.
- Navigation pages may group related files by theme, but grouping does not override the layer taxonomy.
- Tool and vendor selections stay out of timeless principles unless the operating model itself changes.

## Honesty Note

This ADR was written after the commit landed. It reconstructs the decision from repository evidence and should not be read as proof that an ADR existed on 2026-04-07.
