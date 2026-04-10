# External Honest Review — Synthesis (Maintenance Note)

**Date:** 2026-04-07.  
**Purpose:** Capture **durable signal** from a multi-perspective review of this library (strengths, gaps, positioning) without preserving chat-only context. Update when a major external review completes.

---

## Strengths Noted

- **Principles / tooling / estates** split is the main **architectural** differentiator—keeps vendor detail from masquerading as universal law.
- **Conditional scoping** (“only when Kubernetes,” “if the repo uses events”) reduces false universality.
- **Operational specificity** (cardinality discipline, expand/contract migrations, error-budget **policy**, message DLQ/replay) goes beyond generic “best practice” lists.
- **Meta-governance**: change checklist, MoSCoW audit, `SITEMAP.md` generation, `REFERENCES.md`, how-to-read navigation.
- **Checklists** tie principles to **verifiable** execution.

---

## Gaps Acknowledged

- **Team validation** — doctrine is stress-tested by **individual** depth; multi-team disagreement, legacy coexistence, and onboarding friction are **explicit risks**—see [../patterns/adoption-playbook.md](../patterns/adoption-playbook.md).
- **Size** — full tree is a **reference library**; onboarding needs a **one-pager** ([../tooling/estates/minimum-viable-doctrine.template.md](../tooling/estates/minimum-viable-doctrine.template.md)).
- **Preference vs principle** — language tables, container engine on workstation, and strong interop choices (e.g. CloudEvents) should stay clearly labelled **illustrative** or **interop** where relevant; see [../principles/timeless-principles-and-tooling.md](../principles/timeless-principles-and-tooling.md).
- **User-facing quality** — expand or scope-bound when desktop/OS/legal surfaces dominate [../principles/user-facing-quality.md](../principles/user-facing-quality.md).
- **Measurement** — practices need **outcome** metrics; addressed in [../principles/measurement-and-dora.md](../principles/measurement-and-dora.md).

---

## Positioning (High Level)

Forkable, modular doctrine starter kits are **rare** relative to company handbooks or narrow manifestos; this repo aims at **portable principles** plus **replaceable** tooling. Competitive claims belong in talks and posts—here we only **document** structure and adoption aids.

---

## Ongoing Gap Research

- Section-by-section industry comparison: [deep-research-section-gaps.md](deep-research-section-gaps.md)

---

## Artefacts Added From This Review Cycle

| Item | Location |
| --- | --- |
| Adoption / migration path | [../patterns/adoption-playbook.md](../patterns/adoption-playbook.md) |
| DORA / Four Keys layer | [../principles/measurement-and-dora.md](../principles/measurement-and-dora.md) |
| One-page team pitch template | [../tooling/estates/minimum-viable-doctrine.template.md](../tooling/estates/minimum-viable-doctrine.template.md) |
| Convictions vs standards | [../principles/timeless-principles-and-tooling.md](../principles/timeless-principles-and-tooling.md) §5 |
| A11y / i18n scope and depth | [../principles/user-facing-quality.md](../principles/user-facing-quality.md) |

---

## Not Tracked Here

- Open-source **publishing** decision, market validation, or org-specific estate fills—those live in programme / sponsor context, not this synthesis file.
