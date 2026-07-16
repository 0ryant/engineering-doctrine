# 0023. Add AI Adoption-Control Coverage: Inventory, Independent Challenge, Harm-Surface Testing, Provider Continuity, Literacy

Status: Accepted  
Decision date: 2026-07-16  
Recorded date: 2026-07-16  
Retrospective: No

## Context

An operator-supplied summary of a regulated-sector (financial services / insurance) AI-risk paper — "the issue is not adoption, it is control" — was audited against this corpus. The paper's provenance could not be confirmed (see honesty note in the research file), but its five-layer control model matches verifiable primary sources: **NIST AI RMF** GOVERN 1.6 (AI system inventory), **PRA SS1/23** / **Fed SR 11-7** (model inventory with risk-based tiering; independent validation and *effective challenge*), **EU DORA** Arts 28–29 (register of information; tested exit strategies; concentration risk), **EU AI Act** Arts 4/12/14/15 (literacy; lifetime logging; human oversight; lifecycle-consistent accuracy), **NIST AI 600-1** and **OWASP LLM Top 10 (2025)** (GenAI test surface), and **NCSC / FinCEN / Europol** (GenAI-accelerated social engineering and deepfake fraud).

Three independent full-corpus surveys (2026-07-16) confirmed the library asserts strong **capability**-tier governance (ADR 0005, `ai-ml-systems.md` tiers A–D) and change-path human gates, but had **zero-match** gaps on: AI system inventory and **materiality** tiering, shadow AI, three-lines-style **independent challenge**, runtime **human fallback and contestability** for person-affected automated decisions, **fairness/bias** and **drift** testing, **jailbreak**/output-validation/leakage-probing as named test classes, AI **provider continuity** (exit/substitution, concentration risk, due diligence, audit rights), GenAI **fraud acceleration** (deepfake/phishing/synthetic identity), and role-based **AI literacy** / acceptable-use. One asserted control was a **dangling pointer**: `ai-ml-systems.md` §6 promised "timeouts, fallbacks, error budgets" via `reliability-slo-incidents.md`, which contained none of it.

Evidence:

- Committed research note: [doctrine/evolution/research-ai-adoption-control-gaps-2026-07.md](../../doctrine/evolution/research-ai-adoption-control-gaps-2026-07.md) (coverage map with zero-match claims; verified external authorities; landing decisions).
- Existing gap registers (`anti-patterns-and-failure-modes-gap-analysis-2026-04.md`, `deep-research-section-gaps.md`) did **not** list these gaps — they were unrecognized, not deferred.

## Decision

1. **Adopt** the research note as the library's basis for AI **adoption-control** coverage, complementing ADR 0005 (AI systems as governed systems) with the *operating-model* layer: what must exist **around** each AI system for adoption to be controlled.
2. **Add one pattern** — [doctrine/patterns/ai-adoption-controls.md](../../doctrine/patterns/ai-adoption-controls.md) — carrying the five layers (inventory & materiality; ownership & independent challenge; harm-surface test matrix; third-party continuity; capability uplift). Regulators are cited as **rationale and vocabulary**, never as obligations the doctrine imposes on adopters; sector-specific mappings stay in estates/ADRs.
3. **Anchor principles**: extend `ai-ml-systems.md` (materiality axis orthogonal to capability tiers; inventory and literacy in governance-first ordering; runtime human fallback and contestability; named test classes; shadow-AI anti-pattern), fix the continuity dangling pointer in `reliability-slo-incidents.md`, and add the GenAI attacker-uplift note to `threat-modeling-stride-lite.md`.
4. **Add one checklist** — [doctrine/checklists/ai-adoption-readiness.md](../../doctrine/checklists/ai-adoption-readiness.md) — making the five layers reviewable.
5. **Change class:** additive guidance (new pattern, checklist, principle sections) with **one normative tightening**: production AI systems above minimal materiality must appear in an owned inventory (see pattern §1). Consumer impact labelled in the PR.

## Gap → Closure Table

**Verification 2026-07-16 (closed):** an independent adversarial audit at commit `632228c` attempted to refute each row and returned **CLOSED on all eight** — cited sections exist at the cited numbers with normative, reviewable content; the pre-change dangling pointer was re-confirmed against `632228c^` (zero fallback/failover/provider/exit hits in `reliability-slo-incidents.md`); every relative link in all touched files resolves; all 22 checklist obligations trace to pattern/principle statements; no contradiction with the capability-tier table. Audit findings fixed in the follow-up commit: REFERENCES.md internal-map row for the research note; "every AI system" vs "above minimal materiality" reconciled as aspiration vs **enforcement bar** (`ai-ml-systems.md` §3); §2.1 max-of-two shorthand scoped to the pattern's §§2–5 controls; synthetic-media re-test note added under the pattern §3 matrix so `threat-modeling-stride-lite.md` §3.1's citation lands.

| ID | Gap (2026-07-16 audit) | Closed in (section) |
| --- | --- | --- |
| A1 | AI system inventory, materiality tiering, business-service mapping, shadow AI | [ai-adoption-controls.md](../../doctrine/patterns/ai-adoption-controls.md) §1; [ai-ml-systems.md](../../doctrine/principles/ai-ml-systems.md) §2.1, §3, §8 |
| A2 | First-line ownership, second-line independent (effective) challenge | [ai-adoption-controls.md](../../doctrine/patterns/ai-adoption-controls.md) §2; [ai-ml-systems.md](../../doctrine/principles/ai-ml-systems.md) §3 |
| A3 | Runtime human fallback, override, contestability for person-affected decisions | [ai-ml-systems.md](../../doctrine/principles/ai-ml-systems.md) §4; [ai-adoption-controls.md](../../doctrine/patterns/ai-adoption-controls.md) §2 |
| A4 | Fairness/bias testing, production drift monitoring, jailbreak / output validation / leakage probing as named classes | [ai-adoption-controls.md](../../doctrine/patterns/ai-adoption-controls.md) §3; [ai-ml-systems.md](../../doctrine/principles/ai-ml-systems.md) §6 |
| A5 | Provider continuity: due diligence, audit rights, resilience SLAs, exit/substitution, concentration risk; dangling §6 pointer | [reliability-slo-incidents.md](../../doctrine/principles/reliability-slo-incidents.md) §7; [ai-adoption-controls.md](../../doctrine/patterns/ai-adoption-controls.md) §4 |
| A6 | GenAI fraud acceleration (deepfake, phishing, synthetic identity) in threat modeling | [threat-modeling-stride-lite.md](../../doctrine/principles/threat-modeling-stride-lite.md) §3.1 |
| A7 | Role-based AI literacy, acceptable/prohibited-use artifact | [ai-adoption-controls.md](../../doctrine/patterns/ai-adoption-controls.md) §5; [ai-ml-systems.md](../../doctrine/principles/ai-ml-systems.md) §3 |
| A8 | Reviewable execution of the above | [checklists/ai-adoption-readiness.md](../../doctrine/checklists/ai-adoption-readiness.md) |

## Consequences

- **Two axes, one system**: capability tiers (A–D) say what a system *can do*; materiality says what its failure *costs*. Both now travel together in the inventory entry; controls key off the max of the two. This resolves the previously unstated assumption that capability implies impact.
- **Portable, not sectoral**: teams outside regulated sectors get the same five layers as defaults; regulated estates map them to SS1/23 / DORA / AI Act in estate supplements.
- Discoverability: research note under **Start Here**; pattern and checklist in `doctrine/README.md`, `SEMANTIC_INDEX.md` routes, `REFERENCES.md` (new AI governance & regulation section), glossary terms (materiality, shadow AI, effective challenge, model drift, AI literacy).
- Residual risk: fairness-metric choice and impact-tolerance methodology are intentionally **not** standardized here (estate-specific); the five-layer arrangement is our synthesis of primary sources, not a copied framework.
