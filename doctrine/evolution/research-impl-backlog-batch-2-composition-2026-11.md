# Implementation Reference Batch 2: Observability, Release, Event Consumers, Dependencies

Recorded: 2026-11-17. Repository basis: `69908f8` and the companion change.

## Question

Can backlog rows 4, 7, 8, and 9 of the [screened backlog](research-implementation-reference-layer-2026-09.md#screened-backlog) become concise activity references without strengthening, relocating, or inventing doctrine?

The additions are [Service Observability](../impl/service-observability.md), [Release And Rollback](../impl/release-and-rollback.md), [Event Consumer](../impl/event-consumer.md), and [Dependency Adoption](../impl/dependency-adoption.md). They are governed by [ADR 0048](../../docs/adr/0048-add-implementation-reference-layer.md). Rows 5 (application deployment) and 6 (infrastructure delivery) were deferred because CI/CD Delivery and Testing And Verification already carry most of their shape; row 10 (new service) stays last because of its breadth; row 11 (privileged automation) remains open.

## Method And Evidence Boundary

Each page was drafted by a separate model agent under the layer contract, with instructions to restate owners at the same or weaker strength, use no normative keywords, name no products, and return an owner-audit table with a verbatim owner phrase for every invariant and variation. The lead author then re-checked those phrases against the owner files (62 of 62 located, several only after allowing for bold markup), read every page against its owners, and corrected one scope slip. No external source is admitted; the owners keep their own citations. This is model drafting and model review, with no independent human review.

## Owner Audit Summary

The full per-claim tables were returned by the drafting agents and checked by the lead author. They are summarised here by page.

| Page | Main owners composed | Scope kept explicit |
| --- | --- | --- |
| Service Observability | [Observability](../principles/observability.md) §§1–7; [Reliability](../principles/reliability-slo-incidents.md) §§1, 5; [Audit logging](../principles/audit-logging.md) §§1–4; [Privacy](../principles/privacy-and-data-governance.md) §§1–2, 4, 5.3; [Collaboration](../principles/collaboration.md) §8; [Build](../principles/build.md) §5; [Incident lifecycle](../patterns/incident-lifecycle-and-on-call-operations.md); [Chaos engineering](../patterns/chaos-engineering-and-game-days.md); Core Proposition 8 | SLIs and burn rate only where SLOs exist; GenAI per-call signals only on model-mediated paths; audit records only for selected actions; profiling and kernel probes optional |
| Release And Rollback | [Feature flag governance](../patterns/feature-flag-governance.md) §§1–7; Collaboration §§1, 4, 8; Build §§5–7, 12; [Semantic versioning](../principles/semantic-versioning.md); Reliability §§2–3; [Data and migrations](../principles/data-and-migrations.md) §§1, 3; [GitOps](../patterns/gitops-and-declarative-operations.md); [Code review](../patterns/code-review-and-change-approval.md) §3; Core Propositions 3 and 6 | Metric gates and automated reversion apply to flag-controlled rollouts; automated reversion is baseline for ops flags and context-dependent for release and experiment flags; error-budget policy only where SLOs exist |
| Event Consumer | [Event contracts](../principles/event-contracts.md) §§1–4, 6–7; [Message channel operations](../patterns/message-channel-operations.md); [Idempotency](../patterns/idempotency-across-boundaries.md) §§1, 3; [State machines](../principles/state-machines-and-workflows.md) §§1–5; [Errors](../principles/errors-and-failure-modes.md) §1; [Webhook ingress](../patterns/webhook-ingress-security.md); Core Propositions 4, 6, 8 | CloudEvents as the portable default with documented equivalents; deduplication before non-idempotent effects where at-least-once applies; SLO on lag only where latency matters to users |
| Dependency Adoption | [Dependencies and supply chain](../principles/dependencies-supply-chain.md) §§1–8; [AI and ML-assisted systems](../principles/ai-ml-systems.md) §§4, 6–7; [Merge path](../principles/merge-path-evidence-and-pipeline-integrity.md) §§1–2; Code review §§1, 3, 5, 6; Build §§7, 10, 12, 14; [Secure development](../principles/secure-development-lifecycle.md) §§2–3 | Pre-install lookup required on estate-governed and production paths, recommended locally; model and dataset digests for production or estate-governed use; signature checks where the publisher signs; admission control where adopted |

Correction during lead review: Release And Rollback's metric-gate invariant now says it applies to flag-controlled rollouts, matching its owner.

## Dropped For Lack Of An Owner

Practices the drafts considered and removed because no principle or pattern states them:

- **Observability:** verifying that telemetry arrives bound to the candidate identity (only a sibling reference says it), a sampling strategy, a telemetry cost budget, a general rule to redact personal data in logs and traces, one dashboard per SLO, and runbook links in every alert.
- **Release:** automated deployment rollback on health or burn-rate signals, bake or soak periods and gates for deployment-level canaries, a fixed rollback time, snapshot restore as a rollback method, dark launch and shadow traffic, and stakeholder notice before release.
- **Event consumers:** when to acknowledge relative to committing the effect, retry counts and backoff values, a tolerant-reader rule, consumer-group rebalance handling, and dead-letter alert thresholds.
- **Dependencies:** a registry lookup for human-proposed packages, blanket signature verification for third-party packages and images, review of every dependency diff regardless of author, and maintainer-health or unused-dependency checks.

Each may be sound practice. Adding one belongs in its owning principle or pattern with consumer-impact review, not in a reference.

## Owner Gaps And Contradictions Found

Recorded, not resolved. Each is a candidate for a later editorial or normative change.

| # | Finding | Where |
| ---: | --- | --- |
| 1 | Deduplication identity is inconsistent: event contracts and idempotency use `source` + `id`, not `id` alone, but the webhook pattern stores `ce_id`, a state-machines rationale line says "dedup via `id`", and the order fiction persists `ce_id` | [Webhook ingress](../patterns/webhook-ingress-security.md) §2, [State machines](../principles/state-machines-and-workflows.md) §2, [order fiction](../patterns/example-order-jetstream-workflow.md) |
| 2 | No owner says when a consumer acknowledges relative to committing its effect | Event contracts, message channel operations |
| 3 | Deduplication strength varies: lowercase "should", plain imperative, and MUST for material harm describe overlapping cases | Message channel operations, idempotency §§1, 3 |
| 4 | Errors §3 scopes retry and idempotency to the HTTP boundary; message retry documentation exists only through §1 and the patterns | [Errors](../principles/errors-and-failure-modes.md) §3 |
| 5 | Post-deployment telemetry verification has no general owner; only GenAI telemetry names its evidence | Build §5, observability §7.1 |
| 6 | SLO strength differs: unconditional in collaboration §8, "where appropriate" in Core Proposition 8 | Collaboration §8, ENGINEERING.md |
| 7 | Business identifiers on spans and logs are encouraged without a general minimisation rule for operational telemetry | Observability §2, privacy |
| 8 | Deployment-level canaries, automated deployment rollback, and who decides a non-flag rollback have no owner; only flags and agent responders are covered | Collaboration §8, feature flag governance §§4.3–4.4, incident lifecycle §10 |
| 9 | Code review §5 says safety flags default off; feature flag governance gives ops flags a safe default that can be on | Code review §5, feature flag governance §2 |
| 10 | Release readiness routes flag ownership to collaboration rather than feature flag governance, and its "revert release" option has no owner | [Release readiness](../checklists/release-readiness.md) |
| 11 | Image pinning: Kubernetes security says "digests or tags"; dependencies says digest, not mutable tag | [Kubernetes platform security](../principles/kubernetes-platform-security.md) §3, dependencies §4 |
| 12 | Bot updates: dependencies says human review; collaboration and code review allow documented bot-only paths and auto-merge | Dependencies §2, collaboration §2, code review §6 |
| 13 | SBOM and provenance triggers differ: "every shipped artefact" and an SLSA L2 baseline in dependencies versus "where policy or regulators expect" in build, merge path, and release readiness | Dependencies §§3–4, build §14, merge path invariant 6 |
| 14 | Merge path sends third-party skills and tool servers to dependency admission, but the dependencies principle has no section defining that admission | Merge path invariant 2, dependencies |

## Resolution In This Change

Editorial fixes applied in the same change, at the maintainer's request. Each aligns wording or routing with the canonical owner and changes no obligation's strength or scope.

| # | Resolution |
| ---: | --- |
| 1 | Fixed. The [webhook pattern](../patterns/webhook-ingress-security.md) §2 now stores the CloudEvents `source` + `id` pair, or the provider's documented delivery id and its scope; the state-machines rationale and the order fiction now name the pair. |
| 3 | No change needed. Message channel operations already routes to idempotency, and the stronger duty there is conditional on material harm, so the wordings describe nested cases rather than conflicting ones. |
| 4 | Fixed by routing. [Errors](../principles/errors-and-failure-modes.md) §3 now points message and event duplicate handling to idempotency §3 and message channel operations. |
| 6 | No conflict on re-read. Collaboration §8 scopes SLOs to user-facing paths ("where users care"), which Core Proposition 8's "where appropriate" summarises. |
| 9 | Fixed. The illustrative code-review row now says a typed flag carries the safe default its type fixes, and routes to feature flag governance instead of collaboration. |
| 10 | Fixed. [Release readiness](../checklists/release-readiness.md) routes flag prompts to feature flag governance, asks for expiry only on release and experiment flags, and names the recovery options its owners define. |
| 11 | Fixed as a misattribution. [Kubernetes platform security](../principles/kubernetes-platform-security.md) §3 now cites dependencies §4 for base-image digests and merge-path invariant 9 for referencing the exact promoted artefact by digest or version. No pinning duty changed. |
| 14 | Fixed by routing. [Merge path](../principles/merge-path-evidence-and-pipeline-integrity.md) invariant 2 now names where skill and tool-server admission is defined: code review §5, dependencies §§1–2, and AI and ML-assisted systems §7. |

Decisions for the remaining findings, made by the maintainer and recorded in [ADR 0052](../../docs/adr/0052-close-owner-gaps-from-implementation-batch-2.md) (accepted 2026-11-18), with sources in the [owner gap rules note](research-owner-gap-rules-2026-11.md):

| # | Route |
| ---: | --- |
| 2 | ADR 0052 D2: consumers acknowledge after the effect is durable; [message channel operations](../patterns/message-channel-operations.md) owns the rule. |
| 5 | ADR 0052 D4: post-deployment verification covers telemetry; [observability](../principles/observability.md) §8 owns it. |
| 7 | ADR 0052 D5: identifiers in telemetry are minimised; observability §2 owns it, grounded in privacy §§1–2. |
| 8 | ADR 0052 D3: deployment canaries record their signals and tolerance, automated rollback is bounded, and a decider is named; [collaboration](../principles/collaboration.md) §8.1 owns it. |
| 12 | ADR 0052 D1: low-risk updates may merge on a documented bot-only path once required checks pass; [dependencies](../principles/dependencies-supply-chain.md) §2 owns it. |
| 13 | Folded into the open M16 SLSA decision and the provenance-limits candidate in the [latest-developments note](research-latest-developments-2026-11.md); not decided here. |

Some practices listed under "Dropped For Lack Of An Owner" now have owners through ADR 0052: acknowledgement order, deployment canary gates, and bounded automated deployment rollback. The references were updated to match.

The dependencies principle's §4 rationale, which says provenance makes tampering detectable, also stays as written; rewording it belongs to the provenance-limits candidate, not an editorial pass.

## Compression Test

All four pages compose at least eight owners each, and none of those owners alone describes the activity end to end. Removing any page removes no obligation. Each lands between 1,370 and 1,400 words, inside the layer's target.

## Consumer Impact

Change class: **additive guidance / navigation**, plus **editorial** alignment for the fixes above. No obligation, exception path, or enforcement setting changes. Owner pointer lines added to existing files are navigation only.

## Residual Risk

The drafts were written by agents and reviewed by the lead author against owners, which is model self-review. Owner phrases were located but not every surrounding paragraph was re-read for nuance. The gaps above are where summaries are most likely to drift when an owner changes; lifecycle sweeps should check these pages whenever those owners move.
