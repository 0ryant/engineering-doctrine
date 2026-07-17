# AI-Native SDLC Readiness Checklist

Use with [AI-Native Software Development Lifecycle](../patterns/ai-native-software-development-lifecycle.md). Record `Yes`, `No`, `N/A` with rationale, owner, evidence link, and due date. `N/A` is not a verifier verdict and must be justified by scope.

## Objective And Outcome Lineage

- [ ] The change links to an authorised objective, standing obligation, or risk/incident response with an accountable owner and decision horizon.
- [ ] Outcome measures/key results/KPIs declare baseline, target or range, window, population/unit, data source/query, owner, cadence, leading/lagging role, guardrail/countermetric, and known data-quality limits.
- [ ] Key results describe outcomes or credible outcome evidence—not tasks completed, artefacts produced, code volume, deployments, or generic activity.
- [ ] An explicit intervention hypothesis states the expected causal mechanism, assumptions, alternatives, dependencies, capacity/cost, materiality, and review/kill date.
- [ ] AI may propose objectives, measures, initiatives, and decomposition; accountable business/product governance accepts their value, validity, priority, capacity, and trade-offs.
- [ ] Every task/run contract and output traces upward to the intervention and objective/measure version; orphan AI-generated work is rejected or deliberately classified.
- [ ] The outcome review can continue, change, stop, or reverse the intervention; completing the output alone cannot close the objective.

## Intent And Scope

- [ ] A real observation, consumer need, defect, risk, or opportunity is linked to the change.
- [ ] The intended outcome, non-goals, owner, affected consumers/services, and source-of-truth records are explicit.
- [ ] The issue/spec and acceptance claims are versioned; material clarifications invalidate and rebind derived plans, contracts, evidence, and approvals.
- [ ] AI capability tier and change materiality are recorded as separate classifications.
- [ ] Acceptance claims include security, privacy, data, operational, and person-impact obligations where relevant.
- [ ] The affected artefact and dependency graph is known well enough to bound review and rollout.

## Transition Design

- [ ] Design or ADR depth is proportional to reversibility, novelty, blast radius, and consumer impact.
- [ ] Rollout, containment, and rollback/forward-recovery are defined and testable.
- [ ] High-risk classes and required accountable approvers are identified before implementation.
- [ ] Competing designs have shared constraints, explicit alternatives, a decision owner, and recorded rationale.

## Agent Work

- [ ] Every agent execution has a validated [run contract](../patterns/run-contracts.md).
- [ ] Inputs, tools, data access, permissions, budgets, required outputs, and handoff rules are bounded.
- [ ] Multi-agent work records parent/child run identifiers, delegated scope, dependencies, non-overlapping workspace ownership, and integration responsibility.
- [ ] Long-running work has durable checkpoints, expiry, escalation, cancellation, and safe stop/resume rules; a stale run cannot silently continue.
- [ ] Every invoked skill has its required [verifier pack](../patterns/verifier-packs.md).
- [ ] Agent work occurs away from protected branches and production authority.
- [ ] Agent-produced executable content runs in an isolated preview/test environment without standing production credentials.
- [ ] The producing agent is not the sole verifier or approver of its candidate.

## Candidate And Evidence

- [ ] The candidate is a reviewable repository change and immutable build artefacts are addressable by digest or equivalent identity.
- [ ] Required structural, behavioural, semantic/harm, security, supply-chain, human/policy, and runtime evidence classes are declared.
- [ ] Evidence is authenticatable, scoped to the candidate, retrievable, current, and reproducible where feasible.
- [ ] Audit evidence records observable actions, tool receipts, outputs, and decisions without requiring private chain-of-thought or unnecessary prompt/secret retention.
- [ ] Binding CI and protected-branch policy reject missing, stale, untrusted, inconclusive, or unbound evidence.
- [ ] A changed candidate invalidates evidence and approvals bound to the earlier version.
- [ ] Verifier-pack results are treated as bounded execution evidence, not whole-system correctness.

## Authority And Enactment

- [ ] Request, production, challenge, authorisation, and enactment duties have explicit identities and separation appropriate to materiality.
- [ ] High-risk changes receive accountable human approval under estate policy.
- [ ] Any waiver has an owner, rationale, exact scope, expiry, compensating control, and removal issue; it does not rewrite a failed or inconclusive result.
- [ ] Deployment/promotion uses deterministic least-privilege tooling and the exact authorised artefact.
- [ ] The target, actor, time, candidate/resulting digest, and decision are emitted in a durable enactment receipt.

## Runtime And Reconciliation

- [ ] Progressive delivery or bounded exposure is used where blast radius warrants it.
- [ ] Runtime checks map back to specified claims and include SLO/security/AI harm or drift signals where relevant.
- [ ] Runtime evidence evaluates objective/KPI movement, guardrails, costs, unintended effects, and attribution limits—not only technical health.
- [ ] Rollback or containment authority is usable without model discretion at the control boundary.
- [ ] Runtime divergence reopens the earliest falsified assumption and links incidents or follow-up work.
- [ ] An operational agent may originate a traceable S0 observation, but cannot implement, approve, and deploy its own remediation as one authority loop.
- [ ] Intent, repository state, deployed state, evidence, and operational knowledge are reconciled before closure.

## Adoption And Measurement

- [ ] One representative brownfield change has been reconstructed end to end before platform-wide automation.
- [ ] The pilot exercises at least one blocked, failed, or inconclusive path.
- [ ] Measures cover flow, evidence quality, safety/quality, authority health, agent effectiveness, and runtime reconciliation.
- [ ] Measures include coordination failures, human attention per accepted outcome, generated-to-accepted ratio, abandoned artefacts, and induced maintenance/backlog load.
- [ ] Delivery-health metrics remain diagnostic rather than universal targets; objective measures are contextual and use countermetrics to surface gaming or local optimisation.
- [ ] Measures are segmented by materiality/change class and reviewed for gaming or hidden manual control debt.
- [ ] Autonomy widens only from observed success, discriminating verification, rollback performance, and sampled human review.

## Decision

- [ ] **Ready:** all applicable blocking items are satisfied and evidenced.
- [ ] **Conditionally ready:** named owner and expiry exist for every bounded exception.
- [ ] **Not ready:** missing authority, binding evidence, deterministic enactment, or rollback/reconciliation blocks adoption.
