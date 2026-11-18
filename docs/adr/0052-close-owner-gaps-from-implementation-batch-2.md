# ADR 0052: Close Owner Gaps Found By Implementation Batch 2

- **Status:** Accepted
- **Decision date:** 2026-11-18
- **Recorded date:** 2026-11-18
- **Retrospective:** No
- **Deciders:** Repository operator
- **Review provenance:** Operator-directed (D1 option selected by the operator; D2–D5 drafted on request) and operator-accepted on 2026-11-18; drafted and reviewed by a model, no independent human or domain review recorded
- **Research:** [Owner gap rules from implementation batch 2](../../doctrine/evolution/research-owner-gap-rules-2026-11.md); findings in the [batch 2 owner audit](../../doctrine/evolution/research-impl-backlog-batch-2-composition-2026-11.md#resolution-in-this-change)
- **Canonical owners:** [Dependencies And Supply Chain](../../doctrine/principles/dependencies-supply-chain.md) §2 (D1); [Message Channel Operations](../../doctrine/patterns/message-channel-operations.md) (D2); [Collaboration](../../doctrine/principles/collaboration.md) §8.1 (D3); [Observability](../../doctrine/principles/observability.md) §§2, 8 (D4, D5)
- **Derived landings:** [Platform Readiness](../../doctrine/checklists/platform-readiness.md); [Release Readiness](../../doctrine/checklists/release-readiness.md); [Event Consumer](../../doctrine/impl/event-consumer.md); [Release And Rollback](../../doctrine/impl/release-and-rollback.md); [Service Observability](../../doctrine/impl/service-observability.md); [Dependency Adoption](../../doctrine/impl/dependency-adoption.md)

## Context

Composing four implementation references exposed places where owners disagreed or where a reference needed a rule no owner states. Eight were fixed editorially. Six needed decisions. The SBOM and provenance trigger (finding 13) is folded into the open M16 SLSA decision and is not decided here. This ADR settles the other five.

## Decision

### D1. Bot-opened dependency updates may use a documented bot-only path

Owner: [Dependencies And Supply Chain](../../doctrine/principles/dependencies-supply-chain.md) §2.

- Update pull requests are automated. Updates that estate policy classifies as low risk MAY merge through a documented bot-only path, as [collaboration](../../doctrine/principles/collaboration.md) §2 allows, once required checks pass. Other updates get human review.
- Agent-authored dependency and lockfile diffs keep the explicit human review in [code review](../../doctrine/patterns/code-review-and-change-approval.md) §6; an update bot is not an agent for that rule.

This resolves the conflict between dependencies §2 ("with human review") and collaboration §2, code review §6, and the dependencies principle's own low-severity cadence row.

### D2. Consumers acknowledge after the effect is durable

Owner: [Message Channel Operations](../../doctrine/patterns/message-channel-operations.md), new section "Acknowledgement And Commit Order".

- **SHOULD (consumers of at-least-once channels):** acknowledge a message, or commit the consumer position, only after its effect is durably committed, scheduled, or written to an outbox, so a crash leads to redelivery rather than loss.
- **MUST (where losing the effect would cause material harm):** do not acknowledge before the effect is durable.
- **Exception path:** acknowledging first gives at-most-once delivery for that consumer. Where that is acceptable, the consumer's documentation states the choice and the loss it accepts.

### D3. Deployment canaries are judged on recorded signals, and rollback has a decider

Owner: [Collaboration](../../doctrine/principles/collaboration.md), new §8.1 "Deployment Canaries And Rollback".

- **SHOULD (deployments using a canary or gradual rollout):** before the rollout starts, record the signals it is judged on and their tolerance, and do not widen exposure while a signal degrades beyond it.
- **MAY:** automation rolls back to the previously verified candidate when the trigger, target, and alert are recorded and the rollback path has been exercised. Automation does not widen exposure or roll forward.
- **Decider:** the service owner, the on-call engineer following the documented runbook, or the incident commander during an incident can roll back to the previously verified candidate without further approval. A forward fix follows the controlled change path or the documented emergency path.
- Feature flags keep their own gates and reversion rules in [feature flag governance](../../doctrine/patterns/feature-flag-governance.md) §§4.3–4.4.

### D4. Post-deployment verification covers telemetry

Owner: [Observability](../../doctrine/principles/observability.md), new §8 "Telemetry Verification".

- **SHOULD (production services on material paths):** post-deployment verification checks that the expected logs, metrics, and traces arrive, that trace context joins across the service's boundaries, and, where SLOs exist, that the SLI data alerts depend on is present.
- **SHOULD:** alerting rules and monitoring configuration are reviewed and tested like code. Alerts that rarely fire are validated with a known signal or an exercise.

### D5. Identifiers in telemetry are minimised

Owner: [Observability](../../doctrine/principles/observability.md) §2, grounded in [privacy](../../doctrine/principles/privacy-and-data-governance.md) §§1–2.

- **SHOULD:** business identifiers added to logs and spans are limited to what support and investigation need. Prefer stable internal or pseudonymous references over direct personal data.
- **SHOULD:** session identifiers, access tokens, credentials, keys, and payment data are kept out of telemetry, or masked or hashed where a reference is needed. Personal data that does enter telemetry follows its data category's retention.

## Control Cost And Lifecycle

| Decision | Failure addressed | Evidence | Operating cost | Review trigger |
| --- | --- | --- | --- | --- |
| D1 | Update backlog from reviewing every trivial bump, or unreviewed auto-merge with no policy | Documented low-risk classes and bot-only path; required checks on bot PRs | Writing and maintaining the class list | A bot-merged update causes an incident |
| D2 | Messages acknowledged before their effect, then lost on crash | Consumer documentation of acknowledgement order or the accepted at-most-once choice | Small; mostly channel configuration | Duplicate or loss incidents traced to acknowledgement order |
| D3 | Canaries promoted on schedule while degrading; on-call waiting for permission to roll back | Recorded canary signals and tolerance; rollback runbook naming the decider | Canary analysis setup | A canary promoted past a degrading signal; a delayed rollback |
| D4 | Deployments that pass while the telemetry needed to detect failure is broken | Post-deploy verification output covering telemetry; tested alert rules | Additional verification checks | An incident detected late because telemetry was missing |
| D5 | Personal data and secrets accumulating in logs and traces | Logging review; masking in telemetry pipelines | Review and masking configuration | A data-exposure finding in telemetry |

Each rule can be simplified or retired if its review trigger shows it adds cost without reducing the failure.

## Alternatives Considered

- **D1: always require human review.** Rejected by the operator; it would contradict two owners and produce update backlogs.
- **D2: leave acknowledgement to tooling.** Rejected; the delivery semantics follow from the order, whatever the channel.
- **D3: make deployment canary gates a MUST, as for flags.** Deferred; a SHOULD fits evidence drawn from one provider's practice, and estates differ in canary tooling.
- **D4 and D5: stay silent.** Rejected; the batch 2 references could not describe a complete operating shape without them.
- **D5: put the rule in privacy.** Rejected; the rule bounds telemetry content, which observability owns, and privacy remains the grounding.

## Consumer Impact And Migration

Change class: **normative loosening** for D1 (scoped to estate-defined low-risk updates) and **normative additions** for D2–D5, mostly SHOULD, with one MUST in D2 scoped to material harm. Compatibility: pre-1.0 minor.

Migration: define the low-risk update classes and bot-only path, if used; document each consumer's acknowledgement order; record canary signals and the rollback decider in runbooks; add telemetry checks to post-deploy verification; review logging for identifiers, tokens, and personal data.

## Acceptance Criteria

- Each owner section states its rule with strength and scope.
- Derived prompts land in Platform Readiness and Release Readiness and link their owners.
- The Event Consumer, Release And Rollback, Service Observability, and Dependency Adoption references reflect the rules without restating more than the owners say.
- The batch 2 owner audit marks findings 2, 5, 7, 8, and 12 resolved, and finding 13 routed to M16.
- The ADR index lists this decision, and doctrine preflight passes.

## Residual Risk

The rules rest on a small set of sources, mostly one provider's practice book and product-scoped documentation. "Low risk" and "material harm" remain estate judgements. Acknowledgement mechanics differ per channel and need tooling mappings. Model review only.
