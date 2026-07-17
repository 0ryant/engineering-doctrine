# External Honest Review — Synthesis (Maintenance Note)

**Date:** 2026-04-07; updated 2026-07-17.

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

- **Adoption evidence** — a portable control cannot prove its effectiveness in every consuming environment. Adopters validate applicable controls against representative changes, failure paths, legacy constraints, and onboarding needs; see [../patterns/adoption-playbook.md](../patterns/adoption-playbook.md).
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
- Public doctrine benchmark and portability-focused scorecard: [public-doctrine-benchmark-gap-analysis-2026-04.md](public-doctrine-benchmark-gap-analysis-2026-04.md)
- Taxonomy, **which to choose when**, and refreshed **honest** scorecard (2026-04-27): [public-doctrine-taxonomy-scorecard-and-choice-2026-04-27.md](public-doctrine-taxonomy-scorecard-and-choice-2026-04-27.md)
- Anti-patterns and failure modes benchmark: [anti-patterns-and-failure-modes-gap-analysis-2026-04.md](anti-patterns-and-failure-modes-gap-analysis-2026-04.md)

## Portability Boundary Review — 2026-07-17

A public-readiness review found organisation-private implementation names,
local programme evidence links, and repository-specific rollout statements in
publishable doctrine surfaces. Those details weakened the declared
principles/tooling/estate split. [ADR 0027](../../docs/adr/0027-keep-public-doctrine-implementation-neutral.md)
therefore requires capability-class wording in the public library and keeps
concrete private implementations in consumer-owned estate documentation.

## Normative Precision And AI-Native Delivery Review — 2026-07-17

Two substantive external reviews agreed that the repository's primary problem was no longer missing coverage. The general review found overbroad universal language, duplicated authority between the umbrella and topic principles, weak applicability/exception semantics, and insufficient control-retirement mechanics. The AI-native review found a strong evidence/authority kernel obscured by mandatory product-portfolio logic, eleven operational states, universal run-contract wording, and an underspecified claim/coordination model.

The release decision is recorded in [the `v0.3.0` plan](v0.3.0-release-plan.md):

| Proposal | Decision | Reason |
| --- | --- | --- |
| Claim-level normative language, composable applicability, portable exceptions | **Take** | Makes obligations precise without replacing the established directory taxonomy. |
| Compact, non-duplicative umbrella | **Take** | Detailed canonical ownership remains in principles and patterns. |
| Control effectiveness, cost, simplification, and retirement | **Take** | Prevents process accumulation from becoming the product. |
| Full directory restructure, hard line quota, one strength label per document | **Reject** | These create migration or false precision without improving authority. |
| Corpus-wide metadata | **Defer** | Validate the need and schema before touching every document. |
| Seven AI delivery gates and five record families | **Take** | Keeps challenge and authorisation separate while reducing operational vocabulary. |
| S0-S10 as required workflow statuses | **Replace** | Retain it as a diagnostic crosswalk rather than an externally validated lifecycle claim. |
| Run contracts for governed execution | **Take** | Tool use, mutation, sensitive data, delegation, controlled-path output, or material reliance require bounds; incidental fully inspected assistance does not automatically activate the envelope. |
| Objective/KPI/intervention chain for every change | **Reject** | Every change needs a mandate. Only strategic interventions or explicit external authorities activate the full outcome overlay. |
| Verification independence by actor/model count | **Replace** | Evidence diversity follows failure modes and materiality; first-party deterministic tests remain valid evidence. |
| Federated systems of record, typed claims, three closure modes, multi-agent invariants | **Take** | These close contradictions and make the model usable for routine and high-impact work. |

Primary-source support and the boundary between external guidance and library synthesis are maintained in [research-doctrine-authority-applicability-2026-07.md](research-doctrine-authority-applicability-2026-07.md) and [research-ai-native-sdlc-2026-07.md](research-ai-native-sdlc-2026-07.md). ADRs 0028-0030 record the adopted decisions.

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
