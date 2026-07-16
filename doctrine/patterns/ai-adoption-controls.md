# AI adoption controls (inventory, challenge, testing, continuity, uplift)

**The risk is not using AI; it is using AI without an operating model.** This pattern is the **around-the-system** layer that [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) assumes: a register of what exists, named owners with independent challenge, tests matched to the harm surface, continuity for external providers, and people who know what they may and may not do. Adoption without these defaults to **incident-driven** governance.

**Scope:** portable defaults for any team shipping or embedding AI (products, copilots, RAG services, agents, third-party AI features). Regulatory sources (NIST AI RMF, PRA SS1/23, Fed SR 11-7, EU DORA, EU AI Act) are cited as **rationale and shared vocabulary** — this pattern does not make regulatory claims for adopters. Sector-specific mappings belong in [../tooling/estates/](../tooling/estates/) or ADRs. Decision record: [ADR 0023](../../docs/adr/0023-add-ai-adoption-control-coverage-inventory-challenge-testing-continuity-literacy.md); research basis: [../evolution/research-ai-adoption-control-gaps-2026-07.md](../evolution/research-ai-adoption-control-gaps-2026-07.md).

**Related:** [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) (capability tiers, change path, retrieval lifecycle), [engineering-controls-governance-program.md](engineering-controls-governance-program.md) (the generic controls programme this specializes), [../principles/reliability-slo-incidents.md](../principles/reliability-slo-incidents.md) §7 (dependency continuity), [../checklists/ai-adoption-readiness.md](../checklists/ai-adoption-readiness.md) (reviewable execution).

---

## 1. Inventory And Materiality (You Cannot Govern What You Cannot List)

Maintain an **AI system inventory**: one entry per AI system in production or handling real data — including **embedded** and **vendor** AI (copilots, SaaS features with model backends, RAG services, agents, low-code automations), not only systems a team built.

| Inventory field | Content |
| --- | --- |
| **System + purpose** | What it does, for whom; link to the system's repo/ADR. |
| **Owner** | Named **first-line owner** (§2) with an escalation path — a role, not a team alias that resolves to nobody. |
| **Capability tier** | A–D per [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) §2. |
| **Materiality** | Business-impact tier (§1.1) and the **business services** the system supports. |
| **Data classes** | Allowed inputs; personal-data flags → [../principles/privacy-and-data-governance.md](../principles/privacy-and-data-governance.md) §5. |
| **Third-party dependencies** | External model APIs, hosting, subprocessors; links to continuity artifacts (§4). |
| **Human oversight mode** | In-the-loop / on-the-loop / none, and the fallback path (§2). |
| **Test evidence** | Where the §3 harm-surface results live. |

Reconcile the inventory **on material change and at least quarterly**, like the branch-protection register in [engineering-controls-governance-program.md](engineering-controls-governance-program.md) §2. An AI system in production above minimal materiality but absent from the inventory is a **finding**, not paperwork debt.

**Shadow AI:** wrappers, copilots, and low-code automations spread faster than documentation. Treat discovery **no-blame** with a cheap **sanctioned path** (lightweight registration + an approved-tools list per §5) — teams route around expensive registration, and the register goes dark (NCSC shadow-IT posture). Unregistered AI use is closed by making registration easy, not by making detection punitive.

### 1.1 Materiality Is An Axis, Not A Synonym For Capability

Capability tiers say what a system **can do**; materiality says what its failure **costs**. A Tier-A "just calls a model API" system that drafts customer-facing decisions is **high-materiality**; a Tier-D agent refactoring test fixtures is not. Tier by **business impact**: person-affected decisions, money movement, regulatory reporting, irreversibility, and blast radius ([../principles/threat-modeling-stride-lite.md](../principles/threat-modeling-stride-lite.md) §4). Controls in §§2–5 scale with the **max** of capability tier and materiality. Where the estate runs an operational-resilience regime (**important business services**, **impact tolerances** — UK PS21/3 / SS1/21 vocabulary), an AI system inside an important business service inherits that service's tolerance regardless of who supplies the model.

**Why:** NIST AI RMF GOVERN 1.6 makes inventory a precondition of risk management ("mechanisms are in place to inventory AI systems… resourced according to organizational risk priorities"); PRA SS1/23 Principle 1 is a firm-wide model inventory with **risk-based tiering**; EU AI Act deployers cannot discharge duties without knowing which systems are high-risk. The 2024 BoE/FCA survey found a **third** of AI use cases are third-party implementations — an inventory that only lists in-house systems misses the fastest-growing class.

---

## 2. Ownership And Independent Challenge

- **First line owns the system.** The **first-line owner** (§1) is accountable for **purpose**, **data inputs**, **acceptable use**, and **human oversight mode** — not the model vendor, not a central AI team. Ownership follows the *decision the system makes*, not the infrastructure it runs on.
- **Second line challenges independently.** Someone **not invested in shipping** — security, privacy, risk, or a peer team where no second-line function exists — reviews high-materiality systems before launch and on material change. Borrow the **effective challenge** test (Fed SR 11-7): the challenger needs **incentives** (independent of delivery), **competence** (can identify limitations and assumptions), and **influence** (authority to force change). Review that cannot block launch is decoration.
- **Self-assessment is not challenge.** A team grading its own AI system repeats the anti-pattern [ADR 0012](../../docs/adr/0012-model-routing-policy.md) closes for agent runs ("the cell cannot grade its own work") at the organisational level. Merge-time code review ([code-review-and-change-approval.md](code-review-and-change-approval.md)) reviews the **change**; second-line challenge reviews the **system** — purpose, data, oversight, harm surface. Both are required for high-materiality systems; neither substitutes for the other.
- **Human oversight is a runtime property, not a launch checkbox.** For **person-affected** or otherwise high-materiality decisions: define the **fallback path** when the system is unavailable, low-confidence, or contested (degrade to human handling, not silent failure); give overseers the authority and the UI affordance to **disregard, override, or halt** output (EU AI Act Art 14 vocabulary — including awareness of **automation bias**); and provide affected people a **contest/complaint path** that reaches a human with authority to reverse the decision. Log enough per decision (input summary, model/version, confidence signals, override events — [../principles/audit-logging.md](../principles/audit-logging.md)) that an explanation and a complaint investigation are *possible*.

**Why:** the change-path gates in [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) §4 protect the **repo**; this section protects the **people the system decides about**. "High-stakes automation without effective human fallback" is a repeatable failure pathway — the fallback must be designed, staffed, and tested, not assumed.

---

## 3. Testing Matched To The Harm Surface

Test what the system can **break**, not what is easy to measure. Minimum classes by system type; depth scales with materiality (§1.1). Record evidence where the inventory points (§1).

| Class | Applies to | What it means |
| --- | --- | --- |
| **Performance / accuracy** | All models | Task-level quality against a held-out or golden set; declared operating range; regression on change ([rag-retrieval-baseline.md](rag-retrieval-baseline.md) §4, [../principles/testing-strategy.md](../principles/testing-strategy.md)). |
| **Fairness / bias** | Person-affected outputs | Outcome comparison across relevant cohorts **before launch and on retrain/model swap**. The **obligation to test and record** is doctrine; metric choice (demographic parity, equalised odds, …) is estate- and domain-specific — pick per system, record in the system's ADR, and justify. "We didn't look" is not a neutral state; it is an untested harm surface. |
| **Drift** | All production models | **Continuous** monitoring of input distribution and output quality against the launch baseline — not only change-triggered eval. Alert thresholds and a retrain/rollback decision path; lifetime event logging (EU AI Act Art 12 vocabulary) is the precondition ([../principles/observability.md](../principles/observability.md)). |
| **Robustness** | All models | Behaviour under malformed, boundary, and adversarial input perturbation; graceful degradation rather than confident garbage ([../principles/errors-and-failure-modes.md](../principles/errors-and-failure-modes.md)). |
| **Prompt injection** | GenAI | Direct and **indirect** (retrieved/ingested content) — already normative: [rag-retrieval-baseline.md](rag-retrieval-baseline.md) §3, OWASP **LLM01**. |
| **Jailbreak / guardrail bypass** | GenAI with safety or policy constraints | Distinct from injection: adversarial attempts to defeat the system's **own** refusal/policy layer. Red-team pre-deployment and on model swap; MITRE **ATLAS** and OWASP LLM give the taxonomy; UK AISI **Inspect**-style harnesses make it repeatable. |
| **Output validation** | GenAI feeding downstream systems or users | Model output is **untrusted input** to whatever consumes it: schema/type validation for structured output, sanitisation before render or execution (OWASP **LLM05** Improper Output Handling), groundedness checks for user-visible claims. |
| **Data-leakage probing** | GenAI over non-public data | Actively probe for system-prompt leakage (**LLM07**), training/context-data disclosure (**LLM02**), and cross-tenant retrieval ([rag-retrieval-baseline.md](rag-retrieval-baseline.md) §3) — as **tests with evidence**, not only design-time ACLs. |
| **Decision logging** | Person-affected automation | Verify the §2 audit trail actually reconstructs a contested decision end-to-end — test the log, not the logging intention. |

Where the system (or a control it replaces) performs **identity verification or fraud detection**, re-test it against **synthetic-media** attack scenarios (deepfake voice/video, GenAI phishing, synthetic identities) on a cadence, not once — threat framing: [../principles/threat-modeling-stride-lite.md](../principles/threat-modeling-stride-lite.md) §3.1.

**Why:** the corpus already tested what GenAI **retrieves and merges** (injection, RAG eval) but not what models **decide** (fairness), how they **age** (drift), or how they **fail their own policy** (jailbreak). NIST AI 600-1 names pre- and post-deployment red-teaming for the GenAI classes; EU AI Act Art 15 expects accuracy "consistent throughout the lifecycle" — a lifecycle claim requires drift monitoring, not a launch benchmark.

---

## 4. Third-Party AI Continuity (The Provider Is A Dependency You Cannot Patch)

For each external model API, AI platform, or AI-embedding vendor in the inventory (§1):

- **Due diligence before adoption** — proportionate to materiality: model/data-handling posture, subprocessor chain, retention and training-on-your-data terms, security attestations, and **audit rights where feasible** (for high-materiality use, prefer providers that grant them; record the residual risk where they don't).
- **Resilience expectations in the contract** — availability SLAs, deprecation/notice windows for model retirement or behaviour change, and incident-notification duties. A silent model upgrade is a **change to your system** (§3 regression triggers).
- **Concentration risk, assessed not assumed** — before contracting, ask the DORA Art 29 question: is this provider **easily substitutable**, and how many of our systems already sit on it? Estate-level view lives in the inventory's dependency column.
- **Exit and substitution plan, tested** — for high-materiality systems: a named substitute (alternate provider, alternate model family, or degraded human process), the data/prompt/eval assets needed to move (portable eval sets make substitution *provable*), and a **provider-impairment game day** ([chaos-engineering-and-game-days.md](chaos-engineering-and-game-days.md)) exercising it. Runtime mechanics (timeouts, fallbacks, circuit breaking): [../principles/reliability-slo-incidents.md](../principles/reliability-slo-incidents.md) §7. Intra-catalog model substitution in agent runs: [run-contracts.md](run-contracts.md) `model_policy.fallback`.
- **Continuity for loss of provider** — decide **in advance** whether the answer is failover, queue-and-degrade, or stop-the-service; wire it to the incident process ([incident-lifecycle-and-on-call-operations.md](incident-lifecycle-and-on-call-operations.md)).

**Why:** DORA Arts 28–29 (register of information; **documented, tested exit strategies**; concentration risk) and EBA outsourcing guidelines encode hard-won lessons: the time to discover a provider is irreplaceable is not during its outage. The FSB names AI vendor concentration a **systemic** vulnerability; a third of surveyed firms' AI use cases are already third-party implementations.

---

## 5. Capability Uplift (Approved Use, Prohibited Use, And Who Needs To Know What)

- Publish an **acceptable-use artifact** (e.g. `docs/ai-usage.md` or an ADR — [../tooling/ai-assisted-development.md](../tooling/ai-assisted-development.md) shows a shape): **approved** tools and use cases, **prohibited** ones (with the why: data classes, IP, person-affected decisions), and the sanctioned path (§1) for proposing new ones. Keep it short enough that people actually read it; version it like any other governed doc.
- **Literacy is role-based, not one-size** (EU AI Act Art 4 posture: "sufficient" literacy is contextual): **builders** need the harm-surface classes (§3) and injection/leakage failure modes; **operators/reviewers** need the limits of the system they oversee — especially **automation bias** and when to override (§2); **approvers/executives** need enough to challenge (§2), not to implement; **everyday users** need the acceptable-use boundaries and what never to paste into a prompt.
- **Uplift is evidence, not vibes** — track who has been trained for which role, refresh on material system change, and fold AI-specific onboarding into the existing paths ([../principles/documentation-knowledge.md](../principles/documentation-knowledge.md) §5, [../principles/secure-development-lifecycle.md](../principles/secure-development-lifecycle.md) §4).

**Why:** most "AI incidents" in low-maturity orgs are **use** incidents (wrong data pasted, output trusted blind, unapproved tool wired to production), not model failures. Boundaries plus role-appropriate literacy are the cheapest control in this pattern and a precondition for the shadow-AI posture in §1.

---

## 6. Anti-Patterns

- **Ethics statement as operating model** — principles poster, no inventory, no owner, no tests.
- **Capability-only tiering** — a "low-tier" API call quietly deciding claims, credit, or hiring.
- **Registration so heavy teams route around it** — the inventory dies; shadow AI wins.
- **Challenge by the invested** — the building team, or a reviewer who cannot block launch.
- **Human-in-the-loop as label** — an approver with no time, no authority, no override affordance, rubber-stamping at volume (automation bias, unmitigated).
- **Fairness and drift as launch-only checks** — tested once, never monitored; retrain silently shifts outcomes.
- **Provider trust by longevity** — "they're a big lab" as the continuity plan; no exit assets, no game day.
- **Training as compliance theatre** — annual generic module; builders never taught injection, reviewers never taught override.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Inventory is the root control | Every other layer (owner, tests, continuity, use boundaries) attaches to an inventory entry; NIST GOVERN 1.6 / SS1/23 P1 both sequence it first. |
| Materiality orthogonal to capability | Capability tiers under-control low-tech/high-stakes systems and over-control high-tech/low-stakes ones; two axes fix both errors. |
| Effective-challenge test imported | "Incentives, competence, influence" (SR 11-7) is a portable, checkable definition of independence — better than "get a second opinion." |
| Test matrix names classes, not metrics | The obligation to test fairness/drift is durable; metric choice is contested and domain-specific — forcing one would be false precision. |
| Continuity artifacts per provider | Exit plans that exist only as intentions fail exactly when needed; DORA's "documented **and tested**" is the memorable bar. |
| Regulators as rationale, not law | Keeps the pattern portable across sectors while giving regulated estates the citation trail they need. |
| Pattern layer (not principle) | This is how surfaces fit together across org roles and vendors; the durable anchors live in [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md). |

---

## References

- NIST **AI RMF 1.0** (GOVERN 1.6 inventory; MAP per-system context): https://www.nist.gov/itl/ai-risk-management-framework — Playbook: https://airc.nist.gov/airmf-resources/playbook/govern/
- NIST **AI 600-1** — Generative AI Profile: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- Federal Reserve **SR 11-7** / OCC 2011-12 — Supervisory Guidance on Model Risk Management (effective challenge): https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm
- PRA **SS1/23** — Model risk management principles for banks: https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss
- **EU AI Act** — Art 4 (literacy): https://artificialintelligenceact.eu/article/4/ · Art 12 (record-keeping): https://artificialintelligenceact.eu/article/12/ · Art 14 (human oversight): https://artificialintelligenceact.eu/article/14/ · Art 15 (accuracy, robustness): https://artificialintelligenceact.eu/article/15/ · Art 26 (deployer obligations): https://artificialintelligenceact.eu/article/26/
- **DORA** (EU 2022/2554) — Art 28 (register, exit strategies): https://www.digital-operational-resilience-act.com/Article_28.html · Art 29 (concentration risk): https://www.digital-operational-resilience-act.com/Article_29.html
- **EBA** Guidelines on outsourcing (EBA/GL/2019/02): https://www.eba.europa.eu/activities/single-rulebook/regulatory-activities/internal-governance/guidelines-outsourcing-arrangements
- FCA **PS21/3** — Building operational resilience: https://www.fca.org.uk/publications/policy-statements/ps21-3-building-operational-resilience · PRA **SS1/21** (impact tolerances): https://www.bankofengland.co.uk/prudential-regulation/publication/2021/march/operational-resilience-impact-tolerances-for-important-business-services-ss
- Bank of England / FCA — **AI in UK financial services 2024**: https://www.bankofengland.co.uk/report/2024/artificial-intelligence-in-uk-financial-services-2024
- **FSB** — Financial Stability Implications of AI (Nov 2024): https://www.fsb.org/2024/11/the-financial-stability-implications-of-artificial-intelligence/
- **IAIS** — Application Paper on the supervision of AI (Jul 2025): https://www.iais.org/uploads/2025/07/Application-Paper-on-the-supervision-of-artificial-intelligence.pdf
- OWASP **Top 10 for LLM Applications 2025**: https://genai.owasp.org/llm-top-10/
- **MITRE ATLAS**: https://atlas.mitre.org/ · UK AISI **Inspect**: https://inspect.aisi.org.uk/
- **ISO/IEC 42001:2023** (AI management systems): https://www.iso.org/standard/42001 · **ISO/IEC 23894:2023** (AI risk management): https://www.iso.org/standard/77304.html
- **NCSC** — Impact of AI on the cyber threat: https://www.ncsc.gov.uk/report/impact-of-ai-on-cyber-threat · Shadow IT guidance: https://www.ncsc.gov.uk/guidance/shadow-it
