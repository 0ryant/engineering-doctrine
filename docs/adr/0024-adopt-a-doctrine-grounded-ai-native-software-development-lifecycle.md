# 0024. Adopt A Doctrine-Grounded AI-Native Software Development Lifecycle

Status: Accepted
Decision date: 2026-07-17
Recorded date: 2026-07-17
Retrospective: No

## Context

A non-binding lifecycle proposal recast AI-native delivery as a governed state-transition system. Its core separation of intended state, executable change, authority, verification evidence, and observed production reality is compatible with this library, but the proposal could not be adopted unchanged:

- it leaves open whether every agent action needs a run contract, while [run-contracts.md](../../doctrine/patterns/run-contracts.md) already requires one for every agent execution;
- it risks treating verifier packs as broad correctness proof, while [verifier-packs.md](../../doctrine/patterns/verifier-packs.md) makes them a bounded mirror of execution obligations;
- it needs explicit alignment with repository authority, protected merge paths, immutable artefact promotion, human-gated high-risk change, secure development, materiality, and runtime accountability;
- its market sources are useful observations but do not independently establish an effective or portable control model; and
- it proposes a universal transition schema before an adopting estate has tested the minimum record and blocked paths on a representative brownfield change.

The accompanying [research note](../../doctrine/evolution/research-ai-native-sdlc-2026-07.md) triangulates the proposal against NIST SSDF and SP 800-218A, NIST AI RMF, NCSC secure AI guidance, ISO/IEC 5338, SLSA, the EU AI Act, COBIT's goals cascade, GQM/GQM+Strategies, DORA measurement guidance, and current vendor lifecycle material. External sources support lifecycle-wide security, governance, provenance, oversight, monitoring, goal lineage, and contextual measurement; the objective-to-outcome contract, eleven-state lifecycle, and transition-record synthesis remain this library's design choices.

## Decision

1. Adopt [AI-Native Software Development Lifecycle](../../doctrine/patterns/ai-native-software-development-lifecycle.md) as the canonical pattern for software delivery in which AI agents or model-mediated automation participate.
2. Model delivery as evidence-backed transitions across S0 observed need through S10 reconciled. These are control points, not a mandatory waterfall or a requirement for a new orchestration product.
3. Require a reconstructable transition record: source/destination, intent and claims, affected scope, risk, immutable candidate identity, authority, verification, enactment/rollback, outcome, and bounded exception data.
4. Preserve existing doctrine as the control spine:
   - repository, CI, artefact store, deployment system, and observability records remain authoritative;
   - every agent execution has a run contract and applicable verifier packs;
   - verifier packs are execution-local evidence combined with domain, security, supply-chain, human/policy, and runtime evidence;
   - protected-branch and release policy authorise; agents only propose or recommend;
   - build, policy, promotion, rollback, and receipts are deterministic and address immutable artefacts; and
   - capability and materiality are separate axes, with accountable human approval for high-risk change.
5. Add [AI-Native SDLC Readiness Checklist](../../doctrine/checklists/ai-native-sdlc-readiness.md) and an illustrative tooling map, then route the pattern from principles and library navigation.
6. Adopt brownfield stages P0–P5. Each adopting estate pilots a representative bounded change, including at least one failed or inconclusive path, before standardising an estate-wide transition schema.
7. Change class: **normative tightening** for consumers using AI across the software delivery lifecycle. Treat the change as a **0.x minor** compatibility increment: pinned consumers must review the migration before upgrading. Non-agentic paths retain existing obligations. Consumer migration begins with traceability and agent run contracts before authority is expanded.
8. For multi-agent or long-running work, require separate run contracts plus explicit parent/child lineage, delegated scope, dependency and workspace ownership, checkpoints, expiry, escalation, cancellation, and safe resume. Duration and agent count do not grant authority.
9. Treat agent-produced executable content as untrusted until independently challenged in an isolated preview/test environment without standing production credentials. Record observable actions and tool receipts; private chain-of-thought is neither required nor accepted as evidence.
10. Permit operational agents to originate S0 observations and proposed remediations, but never to detect, implement, approve, and deploy one change as a closed authority loop.
11. Put a governed objective-to-outcome chain upstream of lifecycle execution: stakeholder need → objective or standing obligation → outcome measures and guardrails → intervention hypothesis → tasks/run contracts → outputs → observed outcomes → portfolio decision. AI may propose each translation, but accountable business/product governance owns objectives, measure validity, priority/capacity, and continue/change/stop decisions. Output completion never proves objective achievement.

## Alternatives Considered

### Keep Conventional SDLC Phases And Add Agents To Each Phase

Rejected as the governing model. It is easy to explain, but it hides authority changes and evidence invalidation inside phase completion. Conventional labels remain usable as views over the state-transition record.

### Adopt The Initial Proposal Unchanged

Rejected. Its core model is valuable, but open decisions conflict with already adopted run-contract doctrine, the evidence model is underspecified, and vendor material is not sufficient authority for normative controls.

### Require One New Central Lifecycle Platform And Schema Now

Rejected for initial adoption. It risks automating an untested abstraction and duplicating issue, repository, CI/CD, artefact, and observability systems. Adopters establish which fields need a portable schema through representative changes.

### Keep Existing Doctrine Without A Lifecycle Pattern

Rejected. The individual controls exist, but teams lack one end-to-end model showing how intent, agent work, evidence, authority, enactment, and runtime feedback compose.

### Compile KPIs Directly Into Tasks And Treat Outputs As Success

Rejected. It erases the causal intervention hypothesis, encourages metric gaming and backlog inflation, and allows an agent to maximise activity without proving stakeholder or business value. Measures diagnose progress and guardrails; they do not authorise work or substitute for observed outcomes.

## Consequences

- Teams gain a single traceable model without changing the authority of existing principles and control systems.
- AI-assisted work receives explicit pre-execution bounds, independent challenge, and post-deployment reconciliation.
- Tooling may implement the record as linked artefacts; central orchestration is optional.
- Consumers using lifecycle-wide agents have migration work: classification, run contracts, binding evidence, protected authorisation, deterministic enactment, and runtime links.
- Parallel and long-running work adds coordination, checkpoint, workspace-isolation, cancellation, and review-attention costs that must be measured rather than hidden by output volume.
- Strategy, portfolio, product, engineering, risk, finance, and operations records need durable objective/measure/intervention/task/output/outcome lineage; this adds governance work but makes AI-generated activity challengeable and stoppable.
- No universal transition-record schema, retention profile, or empirical autonomy threshold is claimed without representative evidence; adopting estates may standardise narrower local contracts after testing them.

## Library Acceptance And Adopter Validation

- The pattern, checklist, principle/tooling anchors, research basis, glossary, navigation, ADR index, and sitemap are present and cross-linked.
- The Markdown pattern, checklist, ADR, research note, and integration anchors express the adopted model and source limitations.
- Before claiming end-to-end adoption, an estate demonstrates parent/child run lineage, non-overlapping workspaces, safe stop/resume, an isolated executable preview, and an operations-originated S0 observation that follows the normal authority path.
- The adopter's representative change links one objective or standing obligation to a measurement contract, guardrails, intervention hypothesis, tasks, outputs, runtime outcome evidence, and an explicit continue/change/stop portfolio decision.
- Doctrine preflight and relevant repository checks pass.
- No live agent-runtime or orchestration root is modified by doctrine adoption.

## Measures

An adopter's pilot records objective/guardrail movement and attribution limits alongside lead time by materiality, evidence completeness, stale/unbound evidence rejection, human correction and inconclusive rates, change failure/rollback outcomes, waiver age, release-to-runtime reconciliation coverage, coordination conflicts/orphaned runs, resume failures, human attention per accepted outcome, generated-to-accepted ratio, abandoned artefacts, and induced backlog. Autonomy expands only when these measures and sampled review show acceptable outcomes.

## Residual Risks

- The eleven-state decomposition is not independently validated as the optimal granularity.
- Evidence retention and privacy boundaries require estate policy.
- Existing systems may not expose durable links or invalidate approvals automatically after candidate change.
- A transition schema created without representative evidence could freeze local assumptions; no universal schema is adopted by this ADR.
- Objective/KPI cascades can create false precision, Goodhart-style gaming, conflicting local targets, and spurious attribution unless measures, guardrails, causal assumptions, and portfolio decisions are independently reviewed.
