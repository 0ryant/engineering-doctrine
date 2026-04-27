---
name: DoctrineLibraryChange
description: >-
  Edit the canonical engineering-doctrine *library* repo: research grounding, ADR,
  principle/pattern/tooling layering, cross-links, sitemap/glossary/references/README,
  checklist, preflight. USE WHEN adding or changing doctrine/, docs/adr/, ENGINEERING.md
  in the engineering-doctrine repository; doctrine harness; library contribution workflow; ADR task
  for doctrine; navigation updates for new principle.
---

# Doctrine library change (canonical repo)

Use when the user (or task) **changes this repository** — the versioned doctrine **library** — not when they only *consume* doctrine in another product repo.

## Canonical path

This skill applies when the open workspace (or path the user provides) is the **engineering-doctrine** git checkout.

## Execution order

1. **Read** `doctrine/patterns/doctrine-library-change-harness.md` — full procedure, tables, and **§7 agent prompt** (copy-paste block).
2. **Research** — additions need references and/or a note under `doctrine/evolution/`; link from ADR **Context** / **Evidence** when non-trivial.
3. **ADR** — new `docs/adr/NNNN-*.md` + index update, or reference existing ADR; editorial-only may skip (document in PR).
4. **Author** — place text in the right **layer**; cross-link **principle ↔ pattern ↔ tooling**; update checklists if new adopter obligations.
5. **Navigation** — run `./scripts/doctrine-change-preflight.sh` from repo root; update **glossary**, **REFERENCES**, **doctrine/README** (and **ENGINEERING** / **tldr** / **how-to-read** when the spine changes).
6. **Verify** — `doctrine/checklists/doctrine-change-checklist.md`; PR: change class, consumer impact, ADR link.
7. **Releases** — **CHANGELOG** only for **material** releases (see `GOVERNANCE.md` and `doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md`).

## Optional Cursor rule

Install from repo: `docs/cursor/doctrine-library-change.mdc` → `.cursor/rules/` (see `docs/cursor/README.md`).

## Related skills

- **EngineeringDoctrine** — align *any* work with shared doctrine; this skill is **only** for **editing the library repo** itself.

## Output

Summarize: files touched, **ADR** number, **change class**; do not claim “done” without preflight and checklist alignment.
