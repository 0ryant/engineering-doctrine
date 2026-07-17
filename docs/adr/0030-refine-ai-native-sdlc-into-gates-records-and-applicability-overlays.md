# 0030. Refine The AI-Native SDLC Into Gates, Records, And Applicability Overlays

Status: Accepted
Decision date: 2026-07-17
Recorded date: 2026-07-17
Retrospective: No
Amends: [ADR 0024](0024-adopt-a-doctrine-grounded-ai-native-software-development-lifecycle.md)
Depends on: [ADR 0028](0028-adopt-claim-level-authority-applicability-and-exceptions.md)

## Context

[ADR 0024](0024-adopt-a-doctrine-grounded-ai-native-software-development-lifecycle.md) established a strong kernel for AI-assisted change: intent, executable change, evidence, authority, enactment, and observed outcome remain distinct; evidence and approvals bind to an immutable candidate; agents propose while policy and accountable people authorise; uncertainty does not silently become success; and runtime observation closes the delivery loop.

Its first operational form also made S0-S10 the primary state vocabulary, required an objective/measure/intervention chain for every change, required a run contract for every broadly described agent execution, described several control surfaces as deterministic, and placed generic multi-agent coordination inside the software-change lifecycle. A substantive external review identified the resulting ceremony and category errors. The [refreshed research ledger](../../doctrine/evolution/research-ai-native-sdlc-2026-07.md) rechecked the adjacent primary sources and found that:

- NIST SSDF, SP 800-218A, NCSC secure-AI guidance, NIST AI RMF, and SLSA support lifecycle-wide risk practices, traceable evidence, provenance, oversight, and runtime monitoring;
- COBIT, GQM+Strategies, NIST AI RMF, and DORA support contextual goal and measurement linkage when strategic outcomes are being pursued;
- none of those sources mandates eleven states, seven gates, five record families, one run-contract threshold, one claim taxonomy, or one closure model; and
- vendor lifecycle publications are useful observations, not portable authority or comparative effectiveness evidence.

The revision must reduce operational burden without weakening the evidence/authority separation that made ADR 0024 valuable.

## Decision

### 1. Preserve The Kernel

The lifecycle continues to enforce:

> Intent is not implementation. Implementation is not evidence. Evidence is not authority. Authority is not enactment. Enactment is not outcome.

Candidate-bound evidence, separate challenge and authority, promotion of the authorised artefact, explicit uncertainty verdicts, bounded exceptions, and runtime observation remain non-negotiable.

### 2. Use Seven Operational Gates

The primary operational vocabulary is:

1. **Admit mandate** — establish mandate class, owner, materiality, scope, and non-goals.
2. **Specify claims** — state what must be true and what evidence could discriminate it.
3. **Bound governed execution** — constrain model/agent authority when the activation conditions apply.
4. **Produce candidate** — create an addressable change and disclose limitations.
5. **Challenge candidate** — gather claim-appropriate evidence with sufficiently different failure modes.
6. **Authorise transition** — policy and accountable people decide for the exact candidate.
7. **Enact, observe, and close** — promote the authorised candidate, emit receipts, evaluate runtime claims, and select a closure mode.

Challenge and authorisation remain separate because evidence is not authority. S0-S10 remains a diagnostic and migration crosswalk over these gates; consumers are not required to encode eleven workflow statuses.

### 3. Use Five Record Families

Lifecycle evidence composes through:

1. **Mandate** — mandate class, owner, materiality, scope, non-goals, and optional strategic linkage.
2. **Governed execution** — authority envelope, inputs, permitted tools/data, outputs, limits, delegation, stop/escalation conditions, and receipts.
3. **Candidate claim set** — immutable candidate identity, typed claims, limitations, affected surfaces, and required evidence.
4. **Challenge and decision** — separately addressable evidence, findings, policy verdict, authority, approvals, and waivers.
5. **Enactment and observation** — separately addressable deployment receipt, technical verdict, operational observation, rollback/containment state, and optional outcome-review link.

These families may be distributed across existing issue, repository, CI/CD, artefact, policy, deployment, and observability systems. They do not require a central lifecycle database or allow evidence, authority, and enactment to collapse into a single status.

### 4. Activate Run Contracts For Governed Execution

A run contract is required when model-mediated work can invoke tools, mutate persistent artefacts, access sensitive data, operate asynchronously, delegate, consume material budget, cross controlled systems, enter a controlled delivery path without full inspection, or materially influence a decision whose basis will not be fully inspected.

Incidental, ephemeral, low-risk assistance does not become governed execution merely because a model was used. The host product's data/use controls still apply, and any output a human adopts into software follows the normal candidate, review, and CI path. The existing run-contract v1 schema is not changed by this decision.

### 5. Type Claims And Diversify Failure Modes

Material claims identify their type, subject, scope, property or threshold, validity window, evidence obligation, and falsifier where practicable. The portable claim classes are structural, functional, quantitative, compatibility, safety/security, operational, and causal/outcome.

First-party deterministic tests are valid evidence. Required challenge depends on whether evidence surfaces can fail for the same material reason as the producer and on the change's materiality. A second agent, model, or person is not independent merely by being a separate actor.

### 6. Use Federated Authoritative Records

Executable intent lives in an identified, versioned system of record. Repository state is preferred where the delivery surface can be represented as code. External state must have explicit ownership, controlled mutation, version or equivalent identity, durable linkage, and reconciliation. Chat, prompt, model memory, and private reasoning remain non-authoritative.

### 7. Bound Final Authority And Enactment

Final authority and enactment use explicitly configured, bounded, inspectable, reconstructable non-model controls. Their inputs, policy/configuration version, identity, target, candidate, and outputs remain addressable. Candidate identity and promotion remain deterministic and immutable where required; statistical telemetry, incomplete context, and human judgement do not justify open-ended model discretion at the authority boundary.

### 8. Use Three Closure Modes

- **Technical closure** — the authorised candidate was enacted and immediate technical claims were evaluated.
- **Operational closure** — runtime behaviour remained within declared guardrails for the relevant observation window.
- **Outcome review** — aggregated evidence informs a strategic/product continue, change, stop, or reverse decision.

A change may close technically while linking to a continuing operational observation or outcome review. Enactment alone does not satisfy any unsupported claim.

### 9. Make Strategic Outcome Linkage Conditional

Every change requires a mandate. The full objective → measures/guardrails → intervention hypothesis → outputs → observed outcomes → portfolio decision chain activates for strategic/product interventions or an applicable external obligation.

External obligation, vulnerability/incident response, compatibility/lifecycle, risk-reduction, maintenance, and enabling work may instead state the relevant invariant, obligation, exposure, or capability they preserve. They do not invent business KPIs or causal product hypotheses.

### 10. Keep Coordination With Governed Execution

Multi-agent and long-running governed execution requires owned workspaces or an explicit merge protocol, immutable input snapshots, child authority no broader than parent authority, bounded depth/fan-out/time/cost, typed handoffs treated as claims until checked, cancellation and revocation propagation, resume revalidation, and transactional or explicit reconciliation of shared mutable state. The agent-execution patterns own the detailed mechanism; the software-change lifecycle consumes their receipts.

### 11. Source And Compatibility Classification

The seven gates, five record families, activation rule, claim taxonomy, evidence-diversity rule, federated-record composition, and closure modes are this library's synthesis. External sources ground the adjacent lifecycle, security, provenance, risk, measurement, and oversight requirements but do not validate this exact design.

This is a **normative replacement and clarification** for AI-assisted delivery consumers. It is proposed for `v0.3.0`, a pre-1.0 minor release whose pinned consumers must review the migration.

## Relationship To ADR 0024

This ADR amends rather than erases ADR 0024:

- ADR 0024's evidence-backed kernel and candidate-bound controls remain accepted.
- Its S0-S10 primary vocabulary becomes a reference crosswalk.
- Its universal objective/measure/intervention chain becomes a conditional overlay.
- Its universal run-contract wording becomes the governed-execution activation rule.
- Its strict deterministic-control wording becomes bounded, configured, inspectable, reconstructable non-model control execution while preserving immutable candidate addressing and promotion.
- Its independent-actor slogan becomes evidence diversity based on failure modes and materiality.
- Its single runtime/portfolio reconciliation concept becomes technical closure, operational closure, and optional outcome review.
- Its multi-agent requirements remain but move to the canonical execution/coordination surface.

Where the original ADR text conflicts with this amendment, this ADR governs.

## Alternatives Considered

### Keep S0-S10 As Mandatory Operational States

Rejected. The states remain useful diagnostic detail, but several boundaries do not correspond to distinct operational decisions for routine changes and can induce ceremonial fields or a new orchestration product.

### Adopt Six Gates By Combining Challenge And Authorisation

Rejected. Combining them obscures the central rule that evidence is not authority.

### Create Three Independent Lifecycles

Rejected. Run contracts and agent-loop patterns already own execution governance; software change control consumes those records; outcome linkage is a conditional overlay. Three mandatory lifecycles would create a parallel ontology.

### Require Strategic KPI Lineage For Every Change

Rejected. It misclassifies maintenance, obligation, remediation, compatibility, migration, risk-reduction, and enabling work and encourages false causal precision.

### Exempt Low-Materiality Agent Mutation From A Run Contract

Rejected. Incidental assistance is outside governed execution, but persistent or uninspected agent authority remains bounded even when the immediate change is low materiality.

### Make A Second Model Or Human Review Universally Mandatory

Rejected. Actor count is a weak proxy for independent challenge. Evidence diversity and accountable approval scale with claim type and materiality.

### Require A Central Lifecycle Platform And Universal Schema

Rejected as a prerequisite. Existing linked systems can carry the five record families. A portable machine contract would require separate compatibility evidence and a versioned decision.

## Consequences

- Routine changes gain a smaller operational vocabulary and avoid fictional strategy records.
- Strategic interventions retain strong objective, measurement, guardrail, hypothesis, and outcome governance.
- Challenge remains distinct from approval, and first-party tests become explicitly useful without becoming sufficient for every material claim.
- Consumers must define the governed-execution boundary and identify federated systems of record.
- Long-term observation can continue without keeping every implementation issue open.
- S0-S10 links remain interpretable through the crosswalk, reducing migration breakage.
- Some organisations will need platform work for durable cross-system linkage, candidate invalidation, cancellation propagation, and resume revalidation.

## Consumer Migration

Before adopting the replacement, consumers should:

1. map existing S0-S10 states or fields to the seven gates rather than deleting evidence;
2. group existing records into the five families while preserving separate evidence, decisions, receipts, and observations;
3. classify representative model interactions against the governed-execution activation rule;
4. type material claims and assess challenge diversity by failure mode;
5. identify the authoritative system and version identity for each controlled surface;
6. select technical, operational, and outcome closure explicitly; and
7. retain the strategic outcome overlay only where the mandate class activates it.

## Acceptance Evidence

The normative pattern and checklist must demonstrate at least these fixtures:

- an incidental advisory interaction that does not require a run contract;
- a governed tool-using change that does;
- a dependency or compatibility update with no invented KPI;
- a vulnerability or incident response justified by exposure and obligation;
- a strategic product intervention with measures, guardrails, a causal hypothesis, and an outcome review;
- a candidate change that invalidates earlier evidence and approval;
- challenge and authorisation as distinct records; and
- technical closure linked to a longer operational or outcome observation.

Doctrine preflight, Markdown links, run-contract v1 validation, negative control cases, and consumer migration wording must pass before release. Source-local checks prove repository consistency; they do not prove that the synthesis is optimal across adopting organisations.

## Measures

Adopters should measure gate lead time and rework, evidence completeness, stale/unbound evidence rejection, verifier false-result and inconclusive samples, shared-failure-mode findings, human correction/review cost, coordination and resume failures, candidate approval invalidations, change failure and rollback outcomes, generated-to-accepted ratio, induced maintenance load, and technical/operational closure coverage. Outcome-review measures apply only where the strategic overlay is active.

## Residual Risks

- Seven gates and five record families remain a library synthesis without cross-organisation comparative validation.
- Governed-execution classification can drift or be gamed without policy ownership and representative fixtures.
- Federated systems of record can weaken traceability if links, identities, or retention are unreliable.
- Bounded controls can still make wrong decisions from incomplete or noisy inputs; reconstructability is not correctness.
- Evidence diversity can become ceremonial unless correlated failures are sampled.
- Moving outcome review out of routine closure can hide long-term harm if mandate classification is weak.
- No universal autonomy threshold or portable record schema is established by this decision.

## Evidence

- [Research: A Doctrine-Grounded AI-Native Software Development Lifecycle](../../doctrine/evolution/research-ai-native-sdlc-2026-07.md)
- [v0.3.0 Release Plan](../../doctrine/evolution/v0.3.0-release-plan.md) T08-T13
- NIST, [SSDF 1.1](https://csrc.nist.gov/pubs/sp/800/218/final) and [SP 800-218A](https://csrc.nist.gov/pubs/sp/800/218/a/final)
- NIST, [AI RMF 1.0 Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)
- NCSC and international partners, [Guidelines for Secure AI System Development](https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development/guidelines)
- SLSA, [Provenance v1.2](https://slsa.dev/spec/v1.2/provenance)
- ISACA, [COBIT 2019 Goals Cascade](https://www.isaca.org/resources/news-and-trends/industry-news/2019/employing-cobit-2019-for-enterprise-governance-strategy)
- Basili et al., [GQM+Strategies](https://arxiv.org/abs/1402.0292)
- DORA, [Software delivery performance metrics](https://dora.dev/guides/dora-metrics/)
