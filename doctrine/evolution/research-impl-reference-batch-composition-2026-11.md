# Implementation Reference Batch: Service API, Secretless Workload Identity, Database Migration

Recorded: 2026-11-15. Repository basis: `54fd5f39383c081fc62b3ccbae44735069e31201` and the companion change.

## Question

Can the first three candidates in the [screened backlog](research-implementation-reference-layer-2026-09.md#screened-backlog) become concise activity references without strengthening, relocating, or inventing doctrine?

The additions are [Service API](../impl/service-api.md), [Secretless Workload Identity](../impl/secretless-workload-identity.md), and [Database Migration](../impl/database-migration.md). They are governed by [ADR 0048](../../docs/adr/0048-add-implementation-reference-layer.md); no new decision is needed because the layer, its contract, and the backlog already exist. The backlog ordering favoured narrow, frequently used flows before broad ones such as `new-service.md`, and these three are its first three rows.

## Evidence Boundary

This is a composition audit, not a source admission. Every material invariant in the three references traces to an existing canonical principle or owning pattern, and those owners keep their own external citations in [REFERENCES.md](../REFERENCES.md). No new external source is admitted here, and no claim is graded. The separate [latest-developments research](research-latest-developments-2026-11.md) is source-maintenance evidence and does not feed these references.

## Owner Audit: Service API

| Reference material | Existing authority | Scope preserved |
| --- | --- | --- |
| Contract first, live inventory | [Core Proposition 4](../../ENGINEERING.md#4-define-and-verify-material-boundaries); [API boundaries](../principles/api-boundaries-and-security.md) §9 and API9 row; [Semantic versioning](../principles/semantic-versioning.md) §§6.2, 7 | OpenAPI "or equivalent"; gRPC protobuf contracts remain first-class per [Interoperability](../principles/interoperability-and-standards.md) §4. |
| Verified caller identity | API boundaries §§2, 7; [Zero trust](../principles/zero-trust-and-workload-identity.md) §1 | Documented exception for shared static service passwords preserved. mTLS remains one pattern, not a mandate. |
| Object, function, and property authorisation | API boundaries §2 and API1/API3/API5 rows | Gateway authentication does not substitute; resolver-level checks for GraphQL from §5. |
| Bounded requests and rate limits | API boundaries §§1, 3 and API4/API6 rows | Numeric GraphQL ranges stay in the owner. |
| Declared retry semantics | API boundaries §4; [Errors](../principles/errors-and-failure-modes.md) §3; [Idempotency](../patterns/idempotency-across-boundaries.md) §§1–2 | Enforcement only where duplicates could cause material harm; mechanisms remain a bounded choice. |
| Machine-readable errors | Errors §1; API boundaries §1 | RFC 9457 remains "for example"; documented debug mode retained. |
| Correlated telemetry, SLIs | [Observability](../principles/observability.md) §§2–3, 5.1; [Reliability](../principles/reliability-slo-incidents.md) §1 | SLIs only where SLOs exist. |
| Audit where material | [Audit logging](../principles/audit-logging.md) §§1–2 | Purpose and materiality select events; not every mutation. |
| Untrusted outbound calls, SSRF | API boundaries §§8–9 | Unchanged. |
| Review and adversarial gates | [Code review](../patterns/code-review-and-change-approval.md) §5; [Merge path](../principles/merge-path-evidence-and-pipeline-integrity.md) invariant 8 | Binding gate only "where policy requires"; risk tiering stays estate-defined. |
| Versioning, deprecation, private boundary | Semantic versioning §§6.1–6.3, 9 | One primary mechanism for external consumers; shorter notice only with a documented private boundary or contractual notice. |
| Agent tool servers | [AI and ML-assisted systems](../principles/ai-ml-systems.md) §7; API boundaries Related section | Routed only; the MCP baseline is not restated. |

Two draft phrasings were removed during the audit because no owner states them: a preference for events over calls, and an "only when" restriction on private-API deprecation that omitted the contractual-notice path.

## Owner Audit: Secretless Workload Identity

| Reference material | Existing authority | Scope preserved |
| --- | --- | --- |
| Identity, not location; no shared static service passwords | Zero trust §1 | Documented exception preserved. |
| Short-lived, audience-scoped workload credentials; no ambient credentials | Zero trust §2 | SPIFFE "where adopted"; federation mechanisms are examples. |
| Configuration versus secrets | [Configuration and secrets](../principles/configuration-and-secrets.md) §1 | Secret store, managed identity, or short-lived token remain alternatives. |
| Nothing committed; example file; secret scanning | Configuration and secrets §4; [Build](../principles/build.md) §10 | Unchanged. |
| CI federation and privileged pipelines | Configuration and secrets §4; Merge path §§1–2 and invariant 4 | Evidence fields quoted from invariant 4; applies to automation with write or deploy authority. |
| Rotation, overlap, blast radius | Configuration and secrets §2; [Webhook ingress](../patterns/webhook-ingress-security.md) §1 | Automation "where the platform supports it". |
| Secret values out of logs and audit | Audit logging §§1, 3 | Unchanged. |
| Human access and break-glass | Zero trust §3 | Unchanged. |
| Container platforms | [Kubernetes platform security](../principles/kubernetes-platform-security.md) | Applies only when clusters are in scope. |
| Agents holding their own identity | Zero trust §2.1 | Routed with its applicability test; tiered principal floor not restated. |
| External baselines and exceptions | [Revision-pinned profiles](../patterns/revision-pinned-control-profiles.md); [exception contract](../patterns/normative-language-applicability-and-exceptions.md#5-exception-contract) | Profiles bind only where activated. |

Secretless framing: at the maintainer's request the reference leads with the secretless path and was renamed from the backlog's `workload-identity-and-secrets.md`. The owners already prefer it: zero trust §2 prefers short-lived, audience-scoped workload credentials, and configuration and secrets §§2 and 4 prefer managed identity, dynamic credentials, and CI federation where the platform allows. [ADR 0051](../../docs/adr/0051-make-secretless-workload-identity-the-default.md), accepted the same day, then makes secretless the default in zero trust §2 for estate-governed and production workloads where the target supports federation, with registered fallbacks for targets that cannot. The reference follows that owner text and its scope. The "Revisit" step applies the owner rule when a target gains federation support; it adds no new trigger.

Removed during the audit: "each workload gets its own principal" and "developers never use shared production secrets" were sharper than any owner. The reference now says permissions match the workload's purpose, which is the least-privilege form in Core Proposition 7 and zero trust §2. Per-agent principal rules remain only in §2.1.

## Owner Audit: Database Migration

| Reference material | Existing authority | Scope preserved |
| --- | --- | --- |
| Compatible overlap, expand/migrate/contract, split dangerous operations | [Data and migrations](../principles/data-and-migrations.md) §1 | Sequence follows the owner and the existing [CI/CD Delivery](../impl/cicd-delivery.md) sketch. |
| Forward-only, no data-dropping down migrations | Data and migrations §§1, 3 | Application rollback remains a valid recovery. |
| Bounded backfills and recorded limits | Data and migrations §1 | Numeric starting defaults stay in the owner. |
| Snapshot or PITR, lag and lock review | Data and migrations §3 | "Where the platform supports it". |
| Re-run or defined recovery | Idempotency §4 | A runner that can be invoked again is not thereby idempotent. |
| Reconciliation and risk-proportionate evidence | [Core Proposition 6](../../ENGINEERING.md#6-design-failure-retry-recovery-and-reconciliation); [Testing strategy](../principles/testing-strategy.md) §4 | No specific test type is required. |
| Review class | Code review §5 | The owner's table is illustrative; the reference says "states … so informed reviewers can challenge it" rather than adding a reviewer count. |
| Migration notes and data promotion | Build §§4, 7; [GitOps](../patterns/gitops-and-declarative-operations.md) §5 | Not all state belongs in Git. |
| Flag-controlled switches | [Feature flag governance](../patterns/feature-flag-governance.md) §7 | Flag lifecycle unchanged. |
| External shapes | Semantic versioning §§6–9; [Event contracts](../principles/event-contracts.md) | Unchanged. |
| Index and embedding migrations | [RAG retrieval baseline](../patterns/rag-retrieval-baseline.md); AI and ML-assisted systems §7 | Routed only. |

Removed during the audit: a read-then-write switch order, backfill progress telemetry, usage evidence before the contract step, and a rule that data corrections must never be console sessions. None has a canonical owner. They may be sound practice, but adding them belongs in the owning principle with consumer-impact review.

### Owner Gap Recorded, Not Resolved

[Platform Readiness](../checklists/platform-readiness.md) accepts "expand/contract or documented maintenance window", but the owning principle names only expand/contract. The reference lists the maintenance window as a variation and routes it to the checklist. This is a derived prompt with no stated canonical owner. The [doctrine-change checklist](../checklists/doctrine-change-checklist.md) and [ADR 0049](../../docs/adr/0049-add-doctrine-integrity-gates-and-obligation-routing.md) expect obligations to have an owner, so a future editorial change should either add the alternative to `data-and-migrations.md` §1 or remove it from the checklist. This note does not choose.

## Compression Test

| Reference | Owners composed | Why one owner is not enough |
| --- | --- | --- |
| Service API | 15 (principles, patterns, umbrella) | The API principle owns security controls but routes errors, retries, versioning, identity, telemetry, and audit elsewhere. |
| Secretless workload identity | 12 | Zero trust owns identity shape; configuration owns secret handling; merge-path owns pipeline privilege; none gives the acquisition flow. |
| Database migration | 12 | The data principle owns sequencing rules; review class, evidence, idempotent recovery, flag validation, and artefact placement live in six other owners. |

Each reference deletes cleanly: removing it removes no obligation, because every invariant restates an owner's rule at the same or weaker strength and links that owner. Each lands between roughly 1,300 and 1,500 words, at or inside the layer's 500–1,500 target; the secretless reference is the longest because it carries both the default and its fallback.

## Variation And Review Cases

Applicability was checked against materially different consumers: an internal east-west API under a mesh; a public partner API with unknown integrators; a gRPC service behind a transcoding gateway; a payment-initiating endpoint; a serverless job calling a cloud API through managed identity; a CI pipeline deploying through federation; a third-party SaaS key with no federation; an unattended agent holding its own credentials; an additive nullable column; a hot-table index build; a rename; and an estate using maintenance windows. In each case the reference names the owner that decides, and no profile becomes universal.

## Consumer Impact

Change class: **additive guidance / navigation**. No consumer obligation, exception path, migration, or enforcement setting changes. The owner pointer lines added to four principles are navigation only; their opening paragraphs are unchanged.

## Residual Risk

The main risks remain summary drift and accidental strengthening. The removals above show the audit catching both, but the audit is model review of the same author's drafts, not independent review. Links and the sitemap prove reachability only. Lifecycle sweeps should compare these references with their owners whenever an owner changes. The backlog's remaining eight candidates are still proposals.
