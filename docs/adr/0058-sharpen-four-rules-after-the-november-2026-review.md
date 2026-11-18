# ADR 0058: Sharpen Four Rules After The November 2026 Review

- **Status:** Accepted
- **Decision date:** 2026-11-18
- **Recorded date:** 2026-11-18
- **Retrospective:** No
- **Deciders:** Repository operator
- **Review provenance:** Operator-selected (four of thirteen disputed rules chosen for redrafting) and operator-accepted on 2026-11-18; drafted and reviewed by a model, no independent human or domain review recorded
- **Research:** [Full doctrine review, November 2026](../../doctrine/evolution/review-full-doctrine-2026-11.md#sources-for-the-four-redrafted-rules)
- **Canonical owners:** [Reliability](../../doctrine/principles/reliability-slo-incidents.md) §8 (D1); [Data And Migrations](../../doctrine/principles/data-and-migrations.md) §1 (D2); [Dependencies And Supply Chain](../../doctrine/principles/dependencies-supply-chain.md) §4 (D3); [Measurement And DORA](../../doctrine/principles/measurement-and-dora.md) (D4)
- **Derived landings:** [Database Migration](../../doctrine/impl/database-migration.md) invariant 2; [glossary](../../doctrine/glossary.md) (expand and contract)
- **Relationship to earlier decisions:** D1 rewords one sentence that [ADR 0057](0057-close-owner-gaps-from-implementation-batch-3.md) D1 introduced. D3 completes [ADR 0053](0053-correct-slsa-attribution-and-settle-supply-chain-evidence.md) D1.

## Context

The November 2026 review listed thirteen rules that a reviewer disputed. The rules are the maintainer's, so none was changed by the review. He chose four to redraft. In each, the wording did not deliver what the rule intends, and the objection was confirmed on a primary source. The other nine stay as written.

## Decision

### D1. Graceful stop keeps serving until routing stops

Owner: reliability §8. Strength unchanged (SHOULD).

- Before: on a termination signal a workload stops taking new work.
- After: on a termination signal a workload reports itself not ready and keeps serving until the platform has stopped routing to it, or for a short configured delay where the platform gives no such signal. It then finishes or returns in-flight work and exits within the grace period.

The intent, that a deploy drops no requests, is unchanged. On the most widely used orchestrator, routing is withdrawn at the same time as the signal is sent, so a workload that refuses work at once rejects requests still on their way to it.

### D2. Expand and contract backfills before readers switch

Owner: data and migrations §1.

- Before: add new structure first; move writers and readers; backfill; then remove old paths.
- After: add new structure first; deploy application code that is valid for the old and new shape; backfill; verify; switch readers and writers; then remove old paths in a later release.

This is the order the Database Migration reference already shows. Its invariant 2 and the glossary entry now say the same.

### D3. Provenance comes from the build platform

Owner: dependencies §4.

- Before: emit a signed provenance document and attach it with a named signing tool or generator.
- After: use the build platform's own provenance mechanism and confirm which Build level the platform documents for it. A statement assembled and signed by a user-defined build step does not by itself meet Build L2.

Tool names leave the principle; the tooling page already carries them.

### D4. Delivery metrics describe one service and its team

Owner: measurement and DORA.

- Before: the metrics describe how the organisation delivers change; deployment frequency is how often you ship safely.
- After: the metrics describe how one application or service, and the team that owns it, delivers change; deployment frequency is how often you deploy to production. One sentence records that the publisher applies them to one application or service at a time.

## Control Cost And Lifecycle

| Decision | Failure addressed | Evidence | Operating cost | Review trigger |
| --- | --- | --- | --- | --- |
| D1 | Requests dropped on every deploy by a workload that follows the rule as it was worded | Shutdown handling that waits for routing to stop; no error spike across a rollout | A readiness change and a short delay in shutdown code | A platform that guarantees routing stops before the signal |
| D2 | Readers switched to a structure that is not yet backfilled | Migration notes showing backfill and verification before the switch | None beyond the existing sequence | A migration incident traced to step order |
| D3 | A Build level claimed on provenance the platform did not generate | The platform's documented level, recorded with the provenance | Possibly a change of attestation mechanism | A new version of the specification |
| D4 | Delivery metrics rolled up or compared across unlike services | Metric definitions scoped to a service | None | The publisher changes its guidance |

## Alternatives Considered

- **Leave all thirteen as written.** Open to the maintainer; he chose to redraft these four.
- **Redraft all thirteen.** Rejected; nine are his judgement on thresholds, defaults, and emphasis, and the review does not outrank it.
- **D1: also make tolerance of abrupt stop a MUST for stateful workloads.** Not taken; it changes strength, which was not asked for.
- **D2: require dual writes by name.** Not taken; the reference describes a compatible deployment, and the rename variation covers dual writes.
- **D4: add the publisher's statement that speed and stability are not trade-offs.** Not taken; it adds content beyond the framing.

## Consumer Impact And Migration

Change class: **normative correction** for D1 and D2 (the rule asks for something different in one step), **normative clarification** for D3, **editorial** for D4. Compatibility: pre-1.0 minor.

Migration: check shutdown handling against D1, particularly services that close their listener on the first signal; check migration runbooks for the D2 order; confirm how provenance is generated before stating a Build level.

## Acceptance Criteria

- Each owner carries the redrafted sentence, with strength unchanged where one was stated.
- Database Migration invariant 2 and the glossary entry match data and migrations §1.
- The review note marks the four rules as redrafted and the other nine as kept.
- The ADR index lists this decision, and doctrine preflight passes.

## Residual Risk

Each change rests on one primary source and was drafted and checked by a model. D1 describes one orchestrator's behaviour; other platforms differ, which the "short configured delay" clause allows for. D2's source is one practitioner account.
