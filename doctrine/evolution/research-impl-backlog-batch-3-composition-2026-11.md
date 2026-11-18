# Implementation Reference Batch 3: Deployment, Infrastructure, New Service, Privileged Automation

Recorded: 2026-11-18. Repository basis: `8b518c9` and the companion change.

## Question

Can the last four rows of the [screened backlog](research-implementation-reference-layer-2026-09.md#screened-backlog) (5, 6, 10, and 11) become concise activity references without strengthening, relocating, or inventing doctrine?

The additions are [Application Deployment](../impl/application-deployment.md), [Infrastructure Delivery](../impl/infrastructure-delivery.md), [New Service](../impl/new-service.md), and [Privileged Automation](../impl/privileged-automation.md). They are governed by [ADR 0048](../../docs/adr/0048-add-implementation-reference-layer.md). The backlog is now empty.

## Method And Evidence Boundary

Each page was drafted by a separate model agent under the layer contract, with instructions to restate owners at the same or weaker strength, use no normative keywords, name no products, and return an owner-audit table with a verbatim owner phrase for every invariant, variation, and implementation step. Each agent checked its phrases by script as exact substrings of the owner files. The lead author read all four pages in full, re-checked seven of the cited owner sentences that carry the strongest claims, and found them as quoted. No external source is admitted by the pages; the owners keep their own citations. This is model drafting and model review, with no independent human review.

Two pages were then revised by the lead author. Application Deployment and Infrastructure Delivery had each reported that the centre of their subject had no owner. After the owner text in [ADR 0057](../../docs/adr/0057-close-owner-gaps-from-implementation-batch-3.md) was drafted, those pages were updated to compose it, at weaker strength than the owner states.

## Owner Audit Summary

| Page | Main owners composed | Scope kept explicit |
| --- | --- | --- |
| Application Deployment | [Build](../principles/build.md) §§5, 12; [Configuration and secrets](../principles/configuration-and-secrets.md) §§1, 3; [Zero trust](../principles/zero-trust-and-workload-identity.md) §§1–2; [Container runtime choice](../principles/container-runtime-choice.md) §§1–3, 5; [Kubernetes platform security](../principles/kubernetes-platform-security.md) §§1–3; [GitOps](../patterns/gitops-and-declarative-operations.md) §4; [Performance and cost](../principles/performance-and-cost.md) §§1–3; [Cost and FinOps](../principles/cost-and-finops.md) §§2, 5, 7; [Reliability](../principles/reliability-slo-incidents.md) §§7–8; [Data and migrations](../principles/data-and-migrations.md) §§1, 2, 4; [Collaboration](../principles/collaboration.md) §§6, 8–9; [Observability](../principles/observability.md) §8 | Same-artefact promotion where the platform allows; cluster baseline only where the estate runs an orchestrator; redundancy where an availability objective exists; managed platforms confirm and configure |
| Infrastructure Delivery | GitOps §§1, 3–6; [Idempotency](../patterns/idempotency-across-boundaries.md) §4; [Code review](../patterns/code-review-and-change-approval.md) §§1, 3, 5; [Single source of truth](../principles/single-source-of-truth.md) §1; Collaboration §§6–10; Build §§4, 5, 10, 12; [Merge path](../principles/merge-path-evidence-and-pipeline-integrity.md) §2; Zero trust §§2–3; Data and migrations §§2, 4; [Platform engineering](../principles/platform-engineering.md) §7 | A plan is not a promotable artefact; either enactment model passes; cluster access only where clusters are in scope; continuity objectives only where promised |
| New Service | Core Propositions 2, 4, 6, 8; Collaboration §§2, 7–10; [Documentation](../principles/documentation-knowledge.md) §§1–3; [Naming and layout](../principles/naming-and-repo-layout.md) §§1, 3; [Secure development](../principles/secure-development-lifecycle.md) §1; [Threat modelling](../principles/threat-modeling-stride-lite.md) §§1–2; Build §§1, 3–5, 10; Zero trust §2; [Platform as product](../patterns/platform-as-product-and-golden-paths.md) §§2, 4, 6–7; [Adoption playbook](../patterns/adoption-playbook.md) §6 | The order is a reading order, not a rule; on-call where applicable; objectives for user-facing paths; data and model duties only when those profiles apply |
| Privileged Automation | Merge path §§1–2; Zero trust §§2, 2.1; [Run contracts](../patterns/run-contracts.md) §§1.1, 3, 6, 8, 9; [Agentic loop design](../patterns/agentic-loop-design.md) §§6, 6.1, 8.3; [AI and ML-assisted systems](../principles/ai-ml-systems.md) §§2, 4; [AI-native lifecycle](../patterns/ai-native-software-development-lifecycle.md) §§3, 13; [Audit logging](../principles/audit-logging.md) §§1–3; Collaboration §§2, 8, 8.1, 9; [Incident lifecycle](../patterns/incident-lifecycle-and-on-call-operations.md) §10 | Three separate applicability tests; agent principal tiers kept as the owner states them; agent responder rules only where agents are rostered; run contracts for model-driven runs only |

## Dropped For Lack Of An Owner

Practices the drafts considered and removed because no principle or pattern states them:

- **Deployment:** probe design, start-up ordering and warm-up, rollout mechanics, environment isolation by account, read-only filesystems outside the cluster baseline, and batch-job concurrency and retry policy.
- **Infrastructure:** plan expiry, a separate approver per environment, drift detection cadence and alerting, who may invoke break-glass and how soon declared state returns, version pinning for infrastructure modules and providers, protection of the state backend, preview environments, soak time between environments, and cost estimates in plan review.
- **New service:** anything "before creation", a production-readiness gate or sign-off authority, data classification as a step, a recovery rehearsal before first release, dashboards and alert routing for a new service, universal catalogue registration, a rule for new repository versus shared repository, and decommissioning.
- **Privileged automation:** stop or pause for non-agent automation, limits for deterministic jobs and controllers, a rule that automation cannot edit its own gates, a dedicated identity per pipeline or bot, a register of non-AI automation identities, the general condition under which an agent may enact production change outside incident response, dry-run before apply, and periodic permission recertification.

Each may be sound practice. Adding one belongs in its owning principle or pattern with consumer-impact review, not in a reference.

## Owner Gaps And Contradictions Found

| # | Finding | Where |
| ---: | --- | --- |
| 1 | No owner says how a workload signals health, stops, stays available across failure domains, or declares resources. Resource limits appear only as a cluster admission check | Build §5, reliability, Kubernetes platform security §3 |
| 2 | Configuration supplied outside the artefact is implied by same-artefact promotion but never stated | Configuration and secrets §1, build §5 |
| 3 | No owner says a plan belongs to one environment, that the applied plan is the reviewed one, or that applies run from a pipeline; only sibling references say it | Idempotency §4, GitOps §§4–5 |
| 4 | Destroying or replacing a data-bearing resource through an infrastructure change has no owner; the snapshot rule is scoped to migrations | Data and migrations §3 |
| 5 | Drift is "measured and triaged" with no ending; the only rule pairing a live fix with a source change is scoped to agent responders | GitOps §4, incident lifecycle §10 |
| 6 | Rollback "without further approval" meets "reviewed changes to desired state" in a declared-state estate with no stated order | Collaboration §8.1, GitOps §4 |
| 7 | "Automation does not widen exposure or roll forward" has no stated subject and reads as a ban on automated promotion | Collaboration §8.1 |
| 8 | A maintenance window is allowed by collaboration §8 and Platform Readiness but absent from the migration owner | Data and migrations §1 |
| 9 | Minimum tag sets differ between two principles | Cost and FinOps §2, performance and cost §3 |
| 10 | "The deployment checklist" is cited for model cost controls without naming a checklist | Cost and FinOps §7 |
| 11 | Zero trust requires the delegation chain in audit records and points to audit logging, whose field list has no such field | Zero trust §2.1, audit logging §2 |
| 12 | Deploy-time signature verification is unconditional in one owner and "where adopted" in another | Dependencies §5, Kubernetes platform security §3 |
| 13 | Three applicability tests for agents do not coincide: governed run, own principal, and privileged definition | Run contracts §1.1, zero trust §2.1, merge path §1 |
| 14 | "Agents propose" sits beside rules for agents that write to production, with no general condition for agent enactment outside incident response | AI and ML-assisted systems §4, zero trust §2.1, agentic loop design §6 |
| 15 | The high tier for agent principals includes "Tier D", which another owner defines broadly enough to empty the lower tier | Zero trust §2.1, AI and ML-assisted systems §2 |
| 16 | Whether a bot-only path may merge a pipeline-definition update is unstated | Dependencies §2, merge path invariant 2 |
| 17 | Five overlapping lists say which changes need human approval when AI takes part | AI and ML-assisted systems §4, AI-native lifecycle §3, agentic loop design §6, code review §6 |
| 18 | Stop authority is stated only for agent responders; nobody is named to stop a standing agent, and non-agent automation has no stop rule | Incident lifecycle §10, zero trust §2.1 |
| 19 | Ownership granularity varies: team, team or channel, alias, and a role with a named holder | Collaboration §§8, 11, documentation §3, zero trust §2.1 |
| 20 | Threat-model scope is stated three ways | Secure development §1, threat modelling §1, Platform Readiness |
| 21 | Two checklist prompts have no principle text behind them: a personal-data inventory, and recording concrete runtime products | Platform Readiness |
| 22 | First exercise of recovery, service retirement, and any sequence for creating a service have no owner | Documentation §2, Core Proposition 8 |
| 23 | Immutable references read "digest or equivalent" in one place and "digest or version" in another | GitOps §4, merge path invariant 9 |
| 24 | Pinning is owned for application payloads and lockfiles, not for infrastructure modules and providers | GitOps §4, dependencies §1 |
| 25 | Failure posture (timeouts, circuit breaking, degraded mode) is scoped to third-party dependencies | Reliability §7 |

## Resolution In This Change

| # | Resolution |
| ---: | --- |
| 1 | Decided in [ADR 0057](../../docs/adr/0057-close-owner-gaps-from-implementation-batch-3.md) D1 (accepted 2026-11-18): reliability §8, workload runtime shape. |
| 2 | ADR 0057 D2: configuration and secrets §1. |
| 3, 4, 5 | ADR 0057 D3: GitOps pattern §4, invariants 7 to 10. |
| 6, 7 | ADR 0057 D5: collaboration §8.1. |
| 8 | ADR 0057 D4: data and migrations §1. |
| 9 | Fixed editorially. Performance and cost §3 now defers to the minimum tag set in cost and FinOps §2. |
| 10 | Fixed editorially. Cost and FinOps §7 links AI Adoption Readiness. |
| 11 | Fixed editorially. Audit logging §2 lists the delegation chain that zero trust §2.1 already requires. |
| 12 | Settled by [ADR 0053](../../docs/adr/0053-correct-slsa-attribution-and-settle-supply-chain-evidence.md) D3, which types signing and verification as SHOULD. |
| 13–25 | Open. Each is a candidate for a later decision. Findings 13 to 18 concern agent and automation authority and are best taken together. |

Sources and strengths for the ADR 0057 rules are in the [batch 3 owner gap rules note](research-owner-gap-rules-batch-3-2026-11.md).

## Layer Check

All four pages pass the activity, traceability, and variation tests. Two points are recorded against the compression test:

- **New Service** is a router. Its value is the reading order and the links; deleting it removes no obligation. It stays under 1,200 words to keep it from becoming a checklist.
- **Application Deployment** composed sixteen owners but lacked its centre until reliability §8 was drafted. If that section is later narrowed or withdrawn, the page loses its runtime-shape invariant and should be reconsidered.

## Consumer Impact

Change class for the four pages: **additive guidance and navigation**. They create no obligation. The owner changes they rely on are classed in ADR 0057.

## Residual Risk

The lead author re-checked a sample of owner sentences, not all of them. Thirteen findings stay open. The pages restate owner text that this same change edits, so a later owner revision must be followed into the pages. No independent review is recorded.
