# AI-Native SDLC Readiness Checklist

Use with [AI-Native Software Development Lifecycle](../patterns/ai-native-software-development-lifecycle.md). Record `Yes`, `No`, or `N/A` with rationale, owner, evidence link, and due date. `N/A` is not a verifier verdict: justify it from the activation profile.

Start by recording:

- mandate class: product/strategic, external obligation, vulnerability/incident, compatibility/lifecycle, risk reduction/invariant, or enabling work;
- AI capability tier and change materiality as separate axes;
- whether governed-execution triggers apply;
- whether multi-agent/long-running, high-materiality, externally controlled data, or strategic-outcome overlays apply; and
- the controlled systems of record that own mandate, candidate, evidence/authority, enactment, and observation.

## Baseline AI-Assisted Change

Apply whenever model-produced content enters a software candidate or AI materially assists a controlled transition.

### Admit Mandate And Specify Claims

- [ ] An addressable need, obligation, exposure, incident, compatibility condition, invariant, or authorised opportunity justifies the change.
- [ ] Purpose, owner, scope, non-goals, affected consumers/systems, and materiality are explicit.
- [ ] Strategic objectives/KPIs are required only when the strategic-outcome overlay or an external authority activates them.
- [ ] Claims state subject, scope, property/threshold, evidence obligation, owner, validity/observation window, limitations, and candidate binding where material.
- [ ] Security, privacy, data, compatibility, operational, and person-impact claims are included where applicable.
- [ ] Rollout, containment, rollback, or forward recovery is proportionate to impact and reversibility.

### Produce And Challenge The Candidate

- [ ] The candidate is reviewable and immutable build artefacts are addressable by digest or equivalent identity.
- [ ] AI involvement, generated surfaces, material limitations, and affected dependencies are declared.
- [ ] Required structural, functional, quantitative, compatibility, security/safety, operational, and causal/outcome evidence is selected by claim rather than by habit.
- [ ] First-party tests are retained as evidence; additional challenge uses sufficiently different failure modes for the claim and materiality.
- [ ] Evidence is authenticatable, current, scoped to candidate/claim/target/time, retrievable, and reproducible where feasible.
- [ ] Binding CI and protected-branch policy reject missing, stale, untrusted, inconclusive, or unbound required evidence.
- [ ] A changed candidate invalidates evidence and approvals bound to the earlier identity.

### Authorise, Enact, Observe, And Close

- [ ] Request, production, challenge, authorisation, and enactment duties have explicit identities and separation appropriate to materiality.
- [ ] AI recommendations, confidence, self-scores, or model votes are not treated as merge/release authority.
- [ ] Any waiver has an authority, owner, rationale, exact scope, expiry, compensating control, evidence/detection, and remediation link; it does not rewrite a failed or inconclusive result.
- [ ] Promotion uses the exact authorised artefact and a least-privilege workload identity through configured, bounded, inspectable control execution.
- [ ] The target, actor, time, policy/candidate identity, result, and rollback state are emitted in a durable receipt.
- [ ] Runtime evidence maps to declared claims and supports technical, operational, or outcome closure as applicable.
- [ ] Divergence reopens the earliest falsified assumption or triggers containment/rollback and an accountable follow-up.

## Governed-Execution Overlay

Apply when the model/agent invokes tools, mutates persistent state, receives sensitive data, runs asynchronously or delegates, consumes material budget, crosses systems, can enter a controlled path without full inspection, or will otherwise be relied on without full inspection.

- [ ] Every governed execution has a validated [run contract](../patterns/run-contracts.md); incidental fully inspected assistance is not misclassified merely to create paperwork.
- [ ] Input snapshot, tools, data, filesystem, network, subprocess, target, permissions, required outputs, and verifier packs are bounded.
- [ ] Time/token/compute/cost limits are enforced by the contract where represented or by a versioned host/workflow policy; prompt wording alone is not enforcement.
- [ ] Stop, expiry, escalation, cancellation, and receipt behaviour are explicit.
- [ ] Agent work occurs away from protected branches and production authority.
- [ ] Agent-produced executable content runs in an isolated preview/test environment without standing production credentials.
- [ ] Verifier-pack results remain bounded execution evidence, not whole-system correctness or approval.

## Multi-Agent And Long-Running Overlay

Apply when governed executions delegate, run concurrently, or can stop and resume.

- [ ] Parent/child contract identities, delegated scope, dependencies, integration owner, and authority attenuation are recorded.
- [ ] Each mutable workspace has one writer or an explicit merge protocol; parallel work uses isolated input snapshots.
- [ ] Fan-out, depth, retries, time, token/compute/cost, and total budget are externally bounded.
- [ ] Typed handoffs carry provenance, claims, limitations, evidence, and unresolved findings and are checked before integration.
- [ ] Parent cancellation or authority narrowing propagates to affected children and revokes cached authority.
- [ ] Resume revalidates input snapshot, policy, identity, authority, lease/expiry, and target rather than trusting an old checkpoint.
- [ ] Shared mutable state uses transaction/version checks or an explicit reconciliation owner; non-atomic effects have compensation or containment.

## High-Materiality Overlay

Apply to estate-defined high-impact change, including authentication/authorisation, cryptography, tenant isolation, data/schema migration, pipeline/policy, irreversible operations, or person-affecting decisions.

- [ ] Accountable human approval is explicit and bound to the candidate.
- [ ] Challenge includes domain/security expertise with enough independence and influence to force change.
- [ ] Progressive exposure, guardrails, rollback/containment authority, and observation windows are declared.
- [ ] Person-affecting decisions include fallback, contest, override/halt, automation-bias controls, and reconstructable decision evidence where applicable.
- [ ] External control profiles identify governing authority, exact revision, boundary, tailoring/parameters, assessment basis, exceptions, and migration state.

## Strategic Outcome Overlay

Apply only to product/strategic interventions or when an external authority requires objective-to-outcome lineage; see [Outcome And Portfolio Linkage](../patterns/outcome-and-portfolio-linkage.md).

- [ ] Objective, owner, scope, time horizon, and non-goals describe a stakeholder/customer/mission/business/risk outcome rather than an activity.
- [ ] Measures and guardrails declare baseline, target/range, population/unit, source/query, owner, cadence, observation window, uncertainty, and countermetrics.
- [ ] Intervention hypothesis states the expected mechanism, assumptions, alternatives, dependencies, materiality, capacity/cost, and review/kill date.
- [ ] Bounded work and outputs trace to the accepted intervention without being treated as outcome proof.
- [ ] Outcome evidence records guardrails, costs, unintended effects, confounders, and attribution limits.
- [ ] Accountable governance can continue, scale, change, stop, or reverse the intervention; a missed KPI does not automatically generate more work.
- [ ] Technical or operational change records may close while a linked aggregate outcome review continues.

## Adoption And Measurement

- [ ] Existing issue, repository, CI/CD, artefact, policy, deployment, and observability records are reused before adding a workflow database.
- [ ] Representative routine, governed-agent, high-materiality, and strategic cases select the intended overlays consistently.
- [ ] At least one negative case confirms stale evidence, unbound approval, inconclusive challenge, unauthorised enactment, or expired authority is blocked.
- [ ] Measures cover flow, evidence quality, safety/quality, authority health, agent effectiveness, coordination, demand amplification, and runtime reconciliation as applicable.
- [ ] Autonomy expands only from observed success, discriminating verification, rollback performance, incident data, and sampled review—not confidence, duration, or agent count.
- [ ] Controls identify operating cost and effectiveness and can be simplified or retired without losing the evidence obligation.

## Decision

- [ ] **Ready:** every applicable blocking item is satisfied and evidenced.
- [ ] **Conditionally ready:** every bounded exception has accountable authority, owner, compensating control, and expiry.
- [ ] **Not ready:** missing mandate, binding evidence, authority, candidate-bound enactment, or rollback/observation blocks adoption.
