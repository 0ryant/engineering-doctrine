# Canonical References Index

This index lists **authoritative external sources** used across the doctrine. Each principle and tooling file also contains **context-specific references** and **rationale tables**. Use this page for **navigation and audits**; use per-doc sections for **why** a decision applies to that topic.

---

## Standards And Specifications

| Topic | Reference |
| --- | --- |
| Semantic Versioning | https://semver.org/ |
| CloudEvents | https://github.com/cloudevents/spec |
| OpenTelemetry | https://opentelemetry.io/ |
| W3C Trace Context | https://www.w3.org/TR/trace-context/ |
| HTTP Problem Details | https://www.rfc-editor.org/rfc/rfc9457.html |
| SPDX (SBOM) | https://spdx.dev/ |
| WCAG 2.2 | https://www.w3.org/TR/WCAG22/ |
| CloudEvents — NATS protocol binding | https://github.com/cloudevents/spec/blob/main/cloudevents/bindings/nats-protocol-binding.md |
| CloudEvents — Kafka protocol binding | https://github.com/cloudevents/spec/blob/main/cloudevents/bindings/kafka-protocol-binding.md |

---

## Messaging, Events, And NATS (Depth)

Used by `principles/event-contracts.md`, `patterns/message-channel-operations.md`, `patterns/example-order-jetstream-workflow.md`, `tooling/nats-jetstream.md`, and `principles/state-machines-and-workflows.md`—not mandatory product choices.

| Topic | Reference |
| --- | --- |
| NATS documentation | https://docs.nats.io/ |
| JetStream concepts | https://docs.nats.io/nats-concepts/jetstream |
| JetStream consumers (ack, MaxDeliver, backoff, NAK) | https://docs.nats.io/nats-concepts/jetstream/consumers |
| Enterprise Integration Patterns (messaging catalogue) | https://www.enterpriseintegrationpatterns.com/patterns/messaging/ |
| Martin Fowler — Event Sourcing (projections, history, concurrency) | https://martinfowler.com/eaaDev/EventSourcing.html |

---

## Security

| Topic | Reference |
| --- | --- |
| CIS Benchmarks (hardening guides index) | https://www.cisecurity.org/cis-benchmarks |
| OWASP API Security Top 10 (2023) | https://owasp.org/API-Security/editions/2023/en/0x11-t10/ |
| OWASP API2 Broken Authentication | https://owasp.org/API-Security/editions/2023/en/0xa2-broken-authentication/ |
| OWASP API4 Unrestricted Resource Consumption | https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/ |
| OWASP Dependency-Check (SCA concept) | https://owasp.org/www-project-dependency-check/ |
| STRIDE threat categories (overview) | https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats |

---

## Platform Engineering (Reference Framing)

Used by `patterns/platform-as-product-and-golden-paths.md` as **optional** external maturity framing—not a mandate to adopt any CNCF project.

| Topic | Reference |
| --- | --- |
| CNCF TAG App Delivery — Platform Engineering Maturity Model (whitepaper) | https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/ |

---

## Site Reliability Engineering

| Topic | Reference |
| --- | --- |
| Google SRE Book (TOC) | https://sre.google/sre-book/table-of-contents/ |
| Implementing SLOs (workbook) | https://sre.google/workbook/implementing-slos/ |
| Error Budget Policy (workbook) | https://sre.google/workbook/error-budget-policy/ |
| Handling Overload (SRE book) | https://sre.google/sre-book/handling-overload/ |
| DORA — software delivery performance | https://dora.dev/ |
| DORA — 2024 State of DevOps report (DevEx, documentation, platform engineering) | https://dora.dev/research/2024/dora-report |
| ACM Queue — SPACE of Developer Productivity | https://queue.acm.org/detail.cfm?id=3454124 |
| Communications of the ACM — SPACE of Developer Productivity | https://cacm.acm.org/practice/the-space-of-developer-productivity/ |
| Principles of Chaos Engineering | https://principlesofchaos.org/ |
| NIST SSDF (secure SDLC) | https://csrc.nist.gov/Projects/SSDF |
| NIST SP 800-218 (SSDF publication) | https://csrc.nist.gov/publications/detail/sp/800-218/final |
| SLSA (supply-chain levels) | https://slsa.dev/ |
| OWASP ASVS (application verification) | https://owasp.org/www-project-application-security-verification-standard/ |

---

## Testing

| Topic | Reference |
| --- | --- |
| Software Engineering at Google, Ch. 11 (Testing) | https://abseil.io/resources/swe-book/html/ch11.html |
| Fixing a Test Hourglass | https://testing.googleblog.com/2020/11/fixing-a-test-hourglass.html |
| Just Say No to More E2E Tests | https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html |
| Mutation testing (concept) | https://mutationtesting.org/ |
| Hypothesis (property-based testing) | https://hypothesis.readthedocs.io/ |

---

## Data And Migrations

| Topic | Reference |
| --- | --- |
| Parallel Change (Martin Fowler) | https://martinfowler.com/bliki/ParallelChange.html |
| Zero-downtime migrations (example guide) | https://www.jamesrossjr.com/blog/database-migrations-guide |

---

## Observability Tooling

| Topic | Reference |
| --- | --- |
| Deploy the OpenTelemetry Collector | https://opentelemetry.io/docs/collector/deployment/ |
| Scaling the Collector | https://opentelemetry.io/docs/collector/scaling/ |
| OTel log correlation (.NET example) | https://opentelemetry.io/docs/languages/dotnet/logs/correlation/ |
| Azure Monitor + OpenTelemetry (example backend) | https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable |

---

## Estate example: Azure (optional supplement)

Used by `tooling/estates/azure-container-runtimes.md` only—not a global requirement.

| Topic | Reference |
| --- | --- |
| Azure Container Apps overview | https://learn.microsoft.com/en-us/azure/container-apps/overview |
| AKS introduction | https://learn.microsoft.com/en-us/azure/aks/intro-kubernetes |
| Container Apps logging / monitoring | https://learn.microsoft.com/en-us/azure/container-apps/log-monitoring |

---

## Kubernetes security (when clusters are in scope)

| Topic | Reference |
| --- | --- |
| Kubernetes Pod Security Admission | https://kubernetes.io/docs/concepts/security/pod-security-admission/ |
| Kubernetes network policies | https://kubernetes.io/docs/concepts/services-networking/network-policies/ |
| Your distribution’s security baseline | EKS, GKE, AKS, or vendor hardening guide — use current provider docs |

---

## CI/CD And Dependencies

| Topic | Reference |
| --- | --- |
| GitHub Actions docs | https://docs.github.com/en/actions |
| GitLab CI/CD | https://docs.gitlab.com/ee/ci/ |
| Azure Pipelines | https://learn.microsoft.com/en-us/azure/devops/pipelines/ |
| Renovate bot comparison | https://docs.renovatebot.com/bot-comparison/ |
| GitHub Dependabot | https://docs.github.com/en/code-security/dependabot |
| OSV — Open Source Vulnerabilities | https://osv.dev/ |

---

## Privacy And Governance

| Topic | Reference |
| --- | --- |
| ICO — data minimisation (UK GDPR principle) | https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/principles/data-minimisation/ |
| NIST Privacy Framework | https://www.nist.gov/privacy-framework |
| NTIA SBOM minimum elements | https://www.ntia.gov/SBOM |

---

## Architecture Decisions

| Topic | Reference |
| --- | --- |
| ADR GitHub community | https://adr.github.io/ |

---

## Internal Doctrine Map

### Umbrella and meta

| File | Focus |
| --- | --- |
| [../ENGINEERING.md](../ENGINEERING.md) | Headline principles index (repo root) |
| [principles/timeless-principles-and-tooling.md](principles/timeless-principles-and-tooling.md) | Principles vs tooling vs estates |
| [evolution/moscow-review.md](evolution/moscow-review.md) | Audit trail, MoSCoW, thin-area notes |
| [evolution/honest-review-synthesis.md](evolution/honest-review-synthesis.md) | Condensed external review signal |
| [evolution/deep-research-section-gaps.md](evolution/deep-research-section-gaps.md) | Section-by-section gap research |
| [evolution/public-doctrine-benchmark-gap-analysis-2026-04.md](evolution/public-doctrine-benchmark-gap-analysis-2026-04.md) | Public doctrine benchmark, scorecard, and residual gap analysis |
| [evolution/anti-patterns-and-failure-modes-gap-analysis-2026-04.md](evolution/anti-patterns-and-failure-modes-gap-analysis-2026-04.md) | Public anti-patterns / failure modes benchmark, taxonomy, and gap analysis |
| [evolution/research-ai-ml-ops-landscape-2026-04.md](evolution/research-ai-ml-ops-landscape-2026-04.md) | AI/ML ops, governance, RAG, Azure AI Landing Zone — external sources + doctrine map |
| [evolution/research-internal-ai-knowledge-factory-governance-2026-04.md](evolution/research-internal-ai-knowledge-factory-governance-2026-04.md) | Internal AI knowledge layer, handoffs, councils, agentic workflows — enterprise governance + doctrine map (no build specs) |
| [evolution/research-enterprise-rag-agents-indexing-2026-04.md](evolution/research-enterprise-rag-agents-indexing-2026-04.md) | Enterprise RAG, ANN/indexing, hybrid search, MCP/agents — synthesis + doctrine gap map |
| [SITEMAP.md](SITEMAP.md) | Auto-generated list of all Markdown under doctrine/ |
| [README.md](README.md) | Doctrine folder entry |
| [tldr-principles-and-mvp.md](tldr-principles-and-mvp.md) | TL;DR spine + MVP synthesis |
| [glossary.md](glossary.md) | Terms and acronyms (in-repo usage) |

### Governance & Assurance

| File | Focus |
| --- | --- |
| [principles/merge-path-evidence-and-pipeline-integrity.md](principles/merge-path-evidence-and-pipeline-integrity.md) | Merge path as controlled channel; pipeline definitions in scope; binding gates; evidence/SBOM/provenance; **externally cited** |
| [patterns/engineering-controls-governance-program.md](patterns/engineering-controls-governance-program.md) | Org-level **governance programme** for engineering controls (CSF Govern / GV.SC, ownership, waivers, audit packs) |
| [tooling/merge-path-and-pipeline-control-suite.md](tooling/merge-path-and-pipeline-control-suite.md) | Illustrative **control suite** mapping (scanner categories, OIDC, pipeline static analysis) |
| [checklists/governance-program-readiness.md](checklists/governance-program-readiness.md) | Org readiness checklist for merge-path / supply-chain **governance programme** |

### Core principles

| File | Focus |
| --- | --- |
| [principles/build.md](principles/build.md) | Build surfaces, release metadata |
| [principles/collaboration.md](principles/collaboration.md) | Trunk, PRs, SRE collaboration |
| [principles/event-contracts.md](principles/event-contracts.md) | CloudEvents, payloads, ops pointer |
| [principles/semantic-versioning.md](principles/semantic-versioning.md) | SemVer, deprecation |
| [principles/interoperability-and-standards.md](principles/interoperability-and-standards.md) | Specs vs stacks |
| [principles/container-runtime-choice.md](principles/container-runtime-choice.md) | Managed vs K8s |
| [principles/kubernetes-platform-security.md](principles/kubernetes-platform-security.md) | Cluster baseline |
| [principles/single-source-of-truth.md](principles/single-source-of-truth.md) | DRY vs wrong abstraction |
| [principles/configuration-and-secrets.md](principles/configuration-and-secrets.md) | Config vs secrets |
| [principles/audit-logging.md](principles/audit-logging.md) | Audit fields and retention |
| [principles/errors-and-failure-modes.md](principles/errors-and-failure-modes.md) | Errors at boundaries |
| [principles/naming-and-repo-layout.md](principles/naming-and-repo-layout.md) | Repo layout |
| [principles/modularity-and-ports-adapters.md](principles/modularity-and-ports-adapters.md) | Hexagonal / ports |
| [principles/zero-trust-and-workload-identity.md](principles/zero-trust-and-workload-identity.md) | Zero trust, workload ID |
| [principles/secure-development-lifecycle.md](principles/secure-development-lifecycle.md) | SDL / SSDF alignment |

### Patterns

| File | Focus |
| --- | --- |
| [patterns/how-to-read-this-doctrine.md](patterns/how-to-read-this-doctrine.md) | Navigation |
| [patterns/doctrine-versioning-and-consumer-compatibility.md](patterns/doctrine-versioning-and-consumer-compatibility.md) | Doctrine release labels, change classes, and downstream compatibility impact |
| [patterns/build-surface-model.md](patterns/build-surface-model.md) | Layer model |
| [patterns/trunk-workflow.md](patterns/trunk-workflow.md) | Trunk + delivery |
| [patterns/message-channel-operations.md](patterns/message-channel-operations.md) | DLQ, replay, backlog |
| [patterns/adoption-playbook.md](patterns/adoption-playbook.md) | Team migration toward doctrine |
| [patterns/platform-as-product-and-golden-paths.md](patterns/platform-as-product-and-golden-paths.md) | Platform-as-product, golden paths, self-service guardrails, service catalog (portable) |
| [patterns/example-order-jetstream-workflow.md](patterns/example-order-jetstream-workflow.md) | Fictional order FSM + JetStream sketch |
| [patterns/example-saga-payment-workflow.md](patterns/example-saga-payment-workflow.md) | Fictional saga + compensation sketch |
| [patterns/chaos-engineering-and-game-days.md](patterns/chaos-engineering-and-game-days.md) | Chaos experiments and game days |
| [patterns/incident-lifecycle-and-on-call-operations.md](patterns/incident-lifecycle-and-on-call-operations.md) | Incident lifecycle, IC, comms, state doc, escalation, handoff, on-call sustainability, post-incident actions |
| [patterns/webhook-ingress-security.md](patterns/webhook-ingress-security.md) | Webhook ingress hardening |
| [patterns/idempotency-across-boundaries.md](patterns/idempotency-across-boundaries.md) | Idempotency patterns |
| [patterns/rag-retrieval-baseline.md](patterns/rag-retrieval-baseline.md) | RAG retrieval: hybrid search, eval, privacy/security baseline |
| [patterns/engineering-controls-governance-program.md](patterns/engineering-controls-governance-program.md) | Org-level governance programme for merge-path / supply-chain controls (CSF 2.0 Govern / GV.SC) |

### Extended principles

| File | Focus |
| --- | --- |
| [principles/ai-ml-systems.md](principles/ai-ml-systems.md) | GenAI, RAG, agents; governance tiers; merge path |
| [principles/data-and-migrations.md](principles/data-and-migrations.md) | Schema evolution, backups |
| [principles/observability.md](principles/observability.md) | Logs, metrics, traces |
| [principles/testing-strategy.md](principles/testing-strategy.md) | Pyramid, contracts, flakiness |
| [principles/state-machines-and-workflows.md](principles/state-machines-and-workflows.md) | FSM, transitions, event-type mapping |
| [principles/api-boundaries-and-security.md](principles/api-boundaries-and-security.md) | HTTP limits, OWASP API |
| [principles/threat-modeling-stride-lite.md](principles/threat-modeling-stride-lite.md) | STRIDE-lite trust-boundary review |
| [principles/privacy-and-data-governance.md](principles/privacy-and-data-governance.md) | PII, retention |
| [principles/reliability-slo-incidents.md](principles/reliability-slo-incidents.md) | SLOs, incidents; [patterns/incident-lifecycle-and-on-call-operations.md](patterns/incident-lifecycle-and-on-call-operations.md) for full incident lifecycle / on-call |
| [principles/performance-and-cost.md](principles/performance-and-cost.md) | Load, FinOps |
| [principles/documentation-knowledge.md](principles/documentation-knowledge.md) | ADRs, runbooks |
| [principles/dependencies-supply-chain.md](principles/dependencies-supply-chain.md) | SBOM, licences |
| [principles/merge-path-evidence-and-pipeline-integrity.md](principles/merge-path-evidence-and-pipeline-integrity.md) | Merge path, pipeline definitions, binding gates, evidence (NIST / CSF / CISA / SLSA–cited) |
| [principles/developer-experience.md](principles/developer-experience.md) | DevEx, time-to-first-change, local loop, docs findability, cognitive load, review flow |
| [principles/user-facing-quality.md](principles/user-facing-quality.md) | A11y, i18n |
| [principles/measurement-and-dora.md](principles/measurement-and-dora.md) | Delivery metrics, Four Keys |

### Illustrative tooling

| File | Focus |
| --- | --- |
| [tooling/build.md](tooling/build.md) | Example stack |
| [tooling/ai-assisted-development.md](tooling/ai-assisted-development.md) | Categories of AI dev tools (illustrative) |
| [tooling/vector-retrieval-and-embedding-illustration.md](tooling/vector-retrieval-and-embedding-illustration.md) | RAG pipeline layers: ingest, lexical, vector, rerank (illustrative) |
| [tooling/cloudevents.md](tooling/cloudevents.md) | CloudEvents baseline |
| [tooling/nats-jetstream.md](tooling/nats-jetstream.md) | Illustrative NATS / JetStream |
| [tooling/kafka-and-cloudevents.md](tooling/kafka-and-cloudevents.md) | Illustrative Kafka + CloudEvents |
| [tooling/collaboration.md](tooling/collaboration.md) | Git host examples |
| [tooling/observability.md](tooling/observability.md) | OTel examples |
| [tooling/ci-platform-mapping.md](tooling/ci-platform-mapping.md) | CI mapping |
| [tooling/merge-path-and-pipeline-control-suite.md](tooling/merge-path-and-pipeline-control-suite.md) | Merge-path control categories, OIDC, pipeline static analysis (illustrative) |
| [tooling/dependency-automation.md](tooling/dependency-automation.md) | Bots |

### Checklists

| File | Focus |
| --- | --- |
| [checklists/build-readiness.md](checklists/build-readiness.md) | New repo build |
| [checklists/collaboration-readiness.md](checklists/collaboration-readiness.md) | Trunk + branch |
| [checklists/platform-readiness.md](checklists/platform-readiness.md) | SRE / platform |
| [checklists/release-readiness.md](checklists/release-readiness.md) | Versioned release |
| [checklists/doctrine-change-checklist.md](checklists/doctrine-change-checklist.md) | Editing doctrine |
| [checklists/governance-program-readiness.md](checklists/governance-program-readiness.md) | Org governance programme for engineering controls |
| [checklists/developer-experience-scorecard.md](checklists/developer-experience-scorecard.md) | DevEx scorecard for local loop, docs findability, review flow, cognitive load |

### Estates

| File | Focus |
| --- | --- |
| [tooling/estates/README.md](tooling/estates/README.md) | Estate supplements |
| [tooling/estates/TEMPLATE.md](tooling/estates/TEMPLATE.md) | Scaffold |
| [tooling/estates/minimum-viable-doctrine.template.md](tooling/estates/minimum-viable-doctrine.template.md) | One-page team pitch |
| [tooling/estates/azure-container-runtimes.md](tooling/estates/azure-container-runtimes.md) | Example Azure |
| [tooling/estates/aws-container-runtimes.md](tooling/estates/aws-container-runtimes.md) | AWS stub (fill from TEMPLATE) |
| [tooling/estates/gcp-container-runtimes.md](tooling/estates/gcp-container-runtimes.md) | GCP stub (fill from TEMPLATE) |
