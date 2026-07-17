# 0021. Verification Discipline Applies To The Runner Itself

Status: Proposed
Decision date: 2026-05-20
Recorded date: 2026-05-20
Retrospective: No

## Context

A measurement or evaluation runner can declare dependencies, tools, policies,
or verifier surfaces without proving that they were available and active. If it
continues after a declared dependency fails to initialise, its output measures a
different condition from the one it reports. A successful process exit does not
repair that evidence break.

This is a recursive control problem: a system that evaluates evidence-backed
work must apply the same evidence discipline to its own preconditions.

## Proposed Decision

When a runner declares an expected execution substrate:

1. The declaration is a versioned, machine-readable precondition contract.
2. Before paid or material work begins, the runner observes the actual registered
   substrate and computes the missing, unexpected, and unhealthy sets.
3. A missing required dependency fails closed. Optional dependencies must be
   labelled optional before the run, not downgraded after failure.
4. The runner emits a durable preflight receipt containing the declared set,
   observed set, verdict, policy version, and timestamps.
5. Downstream scoring rejects results whose preflight receipt is missing,
   invalid, or bound to a different run.
6. A changed declaration invalidates evidence produced under the earlier
   declaration.

## Consequences

- Evaluation conditions become reconstructable and comparable.
- Invalid runs stop before consuming unnecessary budget or producing misleading
  scores.
- Runner maintenance includes dependency-health probes and receipt validation.
- This does not prove that a registered tool behaved correctly; behavioural
  verification remains a separate evidence layer.

## Consumer Impact

**Change class:** normative replacement of one-estate incident prose with a
portable measurement-integrity rule. Consumers that already verify runner
preconditions have no migration. Others should add preflight contracts before
using evaluation output for release, procurement, or policy decisions.

## Verification

- A fixture with one missing required dependency is rejected before task work.
- A fixture with an explicitly optional missing dependency records the degraded
  condition without mislabelling the substrate.
- A clean fixture emits a receipt bound to the run identity.
- Scoring rejects absent, stale, or mismatched preflight receipts.

## Related

- [Run Contracts](../../doctrine/patterns/run-contracts.md)
- [Verifier Packs](../../doctrine/patterns/verifier-packs.md)
- [Audit Logging](../../doctrine/principles/audit-logging.md)
- [ADR 0027](0027-keep-public-doctrine-implementation-neutral.md)
