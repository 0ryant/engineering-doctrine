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
| CycloneDX (SBOM + VEX) | https://cyclonedx.org/ |
| OpenFeature (feature flags) | https://openfeature.dev/ |
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

## Site Reliability Engineering

| Topic | Reference |
| --- | --- |
| Google SRE Book (TOC) | https://sre.google/sre-book/table-of-contents/ |
| Implementing SLOs (workbook) | https://sre.google/workbook/implementing-slos/ |
| Error Budget Policy (workbook) | https://sre.google/workbook/error-budget-policy/ |
| Handling Overload (SRE book) | https://sre.google/sre-book/handling-overload/ |
| DORA — software delivery performance | https://dora.dev/ |
| ACM Queue — SPACE of Developer Productivity | https://queue.acm.org/detail.cfm?id=3454124 |
| Principles of Chaos Engineering | https://principlesofchaos.org/ |
| NIST SSDF (secure SDLC) | https://csrc.nist.gov/Projects/SSDF |
| NIST SP 800-218 (SSDF publication) | https://csrc.nist.gov/publications/detail/sp/800-218/final |
| SLSA (supply-chain levels) | https://slsa.dev/ |
| SLSA Getting Started | https://slsa.dev/get-started |
| Sigstore — keyless signing | https://www.sigstore.dev/ |
| EU Cyber Resilience Act (SBOM / vuln disclosure) | https://www.european-parliament.europa.eu/doceo/document/TA-9-2024-0130_EN.pdf |
| OWASP ASVS (application verification) | https://owasp.org/www-project-application-security-verification-standard/ |

- Google SRE Workbook, **Alerting on SLOs** (multi-burn-rate model): https://sre.google/workbook/alerting-on-slos/

---

## FinOps And Cloud Cost

| Topic | Reference |
| --- | --- |
| FinOps Foundation framework | https://www.finops.org/framework/ |
| FOCUS spec (cloud billing normalisation) | https://focus.finops.org/ |
| OpenCost (open-source Kubernetes cost monitoring) | https://www.opencost.io/ |
| Green Software Foundation — Software Carbon Intensity (SCI) | https://greensoftware.foundation/ |

---

## Platform Engineering And Team Topologies

| Topic | Reference |
| --- | --- |
| Team Topologies (Skelton & Pais, 2019) | https://teamtopologies.com/book |
| CNCF Platforms Whitepaper | https://tag-app-delivery.cncf.io/whitepapers/platforms/ |
| Platform engineering community | https://platformengineering.org/ |
| Backstage — open-source developer portal | https://backstage.io/ |
| Gartner — Platform Engineering | https://www.gartner.com/en/articles/what-is-platform-engineering |

---

## Feature Flags And Progressive Delivery

| Topic | Reference |
| --- | --- |
| Martin Fowler — Feature Toggles | https://martinfowler.com/articles/feature-toggles.html |
| OpenFeature — vendor-neutral flag standard | https://openfeature.dev/ |
| Trunk-based development — feature flags | https://trunkbaseddevelopment.com/feature-flags/ |
| LaunchDarkly — Feature Flag Best Practices | https://launchdarkly.com/blog/feature-flag-best-practices/ |

---

## AI, Agents, And GenAI

Used by `principles/ai-ml-systems.md`, `patterns/rag-retrieval-baseline.md`, `patterns/agentic-loop-design.md`, and the `tooling/` AI supplement.

| Topic | Reference |
| --- | --- |
| NIST AI Risk Management Framework (AI RMF 1.0) | https://www.nist.gov/itl/ai-risk-management-framework |
| NIST AI 100-1 (AI RMF PDF) | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf |
| NIST AI 600-1 — Generative AI Profile | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf |
| NIST SP 800-218A (GenAI / foundation models, SSDF profile) | https://csrc.nist.gov/pubs/sp/800/218/a/final |
| OWASP Top 10 for LLM Applications | https://genai.owasp.org/llm-top-10/ |
| Model Context Protocol documentation hub | https://modelcontextprotocol.io |
| Anthropic — Building Effective Agents (Dec 2024) | https://www.anthropic.com/engineering/building-effective-agents |
| Anthropic — Multi-Agent Research System (Jun 2025) | https://www.anthropic.com/engineering/built-multi-agent-research-system |
| ReAct — Yao et al., ICLR 2023 (reason + act loop) | https://arxiv.org/abs/2210.03629 |
| Reflexion — Shinn et al., NeurIPS 2023 (verbal RL / critique-retry) | https://arxiv.org/abs/2303.11366 |
| CaMeL — Debenedetti et al., Google DeepMind 2025 (taint tracking, injection defence) | https://arxiv.org/abs/2503.18813 |
| Willison — Dual LLM Pattern (architectural injection defence, Apr 2023) | https://simonwillison.net/2023/Apr/25/dual-llm-pattern/ |
| Willison — The Lethal Trifecta (external content + private data + write tools, 2025) | https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ |
| Karpathy — Verifiability (automation gate, Nov 2025) | https://karpathy.bearblog.dev/verifiability/ |
| Karpathy — 2025 Year in Review (autonomy slider, context engineering) | https://karpathy.bearblog.dev/year-in-review-2025/ |
| Karpathy — Animals vs. Ghosts (limits of current LLMs, Oct 2025) | https://karpathy.bearblog.dev/animals-vs-ghosts/ |
| Miessler — PAI Algorithm v4.0 (ISC, 7-phase loop, scaffolding thesis) | https://github.com/danielmiessler/Personal_AI_Infrastructure |
| LangChain — Context Engineering (Chase, Jun 2025) | https://blog.langchain.com/the-rise-of-context-engineering/ |
| 12 Factor Agents (Horthy — "own your context window") | https://github.com/humanlayer/12-factor-agents |
| LangGraph (cyclic graphs / state machines for agentic loops) | https://github.com/langchain-ai/langgraph |

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
| [evolution/research-ai-ml-ops-landscape-2026-04.md](evolution/research-ai-ml-ops-landscape-2026-04.md) | AI/ML ops, governance, RAG, Azure AI Landing Zone — external sources + doctrine map |
| [evolution/research-internal-ai-knowledge-factory-governance-2026-04.md](evolution/research-internal-ai-knowledge-factory-governance-2026-04.md) | Internal AI knowledge layer, handoffs, councils, agentic workflows — enterprise governance + doctrine map (no build specs) |
| [evolution/research-enterprise-rag-agents-indexing-2026-04.md](evolution/research-enterprise-rag-agents-indexing-2026-04.md) | Enterprise RAG, ANN/indexing, hybrid search, MCP/agents — synthesis + doctrine gap map |
| [SITEMAP.md](SITEMAP.md) | Auto-generated list of all Markdown under doctrine/ |
| [README.md](README.md) | Doctrine folder entry |
| [tldr-principles-and-mvp.md](tldr-principles-and-mvp.md) | TL;DR spine + MVP synthesis |
| [glossary.md](glossary.md) | Terms and acronyms (in-repo usage) |

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
| [patterns/build-surface-model.md](patterns/build-surface-model.md) | Layer model |
| [patterns/trunk-workflow.md](patterns/trunk-workflow.md) | Trunk + delivery |
| [patterns/message-channel-operations.md](patterns/message-channel-operations.md) | DLQ, replay, backlog |
| [patterns/adoption-playbook.md](patterns/adoption-playbook.md) | Team migration toward doctrine |
| [patterns/example-order-jetstream-workflow.md](patterns/example-order-jetstream-workflow.md) | Fictional order FSM + JetStream sketch |
| [patterns/example-saga-payment-workflow.md](patterns/example-saga-payment-workflow.md) | Fictional saga + compensation sketch |
| [patterns/chaos-engineering-and-game-days.md](patterns/chaos-engineering-and-game-days.md) | Chaos experiments and game days |
| [patterns/webhook-ingress-security.md](patterns/webhook-ingress-security.md) | Webhook ingress hardening |
| [patterns/idempotency-across-boundaries.md](patterns/idempotency-across-boundaries.md) | Idempotency patterns |
| [patterns/rag-retrieval-baseline.md](patterns/rag-retrieval-baseline.md) | RAG retrieval: hybrid search, eval, privacy/security baseline |
| [patterns/feature-flag-lifecycle.md](patterns/feature-flag-lifecycle.md) | Feature flag taxonomy, lifecycle FSM, progressive delivery, flag debt |
| [patterns/agentic-loop-design.md](patterns/agentic-loop-design.md) | Agent harness patterns: nested loop, verifiability gate, ISC, autonomy slider, dual-path injection defence, context engineering, verbal RL |

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
| [principles/reliability-slo-incidents.md](principles/reliability-slo-incidents.md) | SLOs, incidents |
| [principles/performance-and-cost.md](principles/performance-and-cost.md) | Load, FinOps |
| [principles/cost-and-finops.md](principles/cost-and-finops.md) | FinOps operating model, unit economics, anomaly detection, AI inference cost |
| [principles/platform-engineering.md](principles/platform-engineering.md) | Team topologies, TVP, golden paths, cognitive load |
| [principles/documentation-knowledge.md](principles/documentation-knowledge.md) | ADRs, runbooks |
| [principles/dependencies-supply-chain.md](principles/dependencies-supply-chain.md) | SBOM, licences |
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
| [tooling/dependency-automation.md](tooling/dependency-automation.md) | Bots |

### Checklists

| File | Focus |
| --- | --- |
| [checklists/build-readiness.md](checklists/build-readiness.md) | New repo build |
| [checklists/collaboration-readiness.md](checklists/collaboration-readiness.md) | Trunk + branch |
| [checklists/platform-readiness.md](checklists/platform-readiness.md) | SRE / platform |
| [checklists/release-readiness.md](checklists/release-readiness.md) | Versioned release |
| [checklists/doctrine-change-checklist.md](checklists/doctrine-change-checklist.md) | Editing doctrine |

### Estates

| File | Focus |
| --- | --- |
| [tooling/estates/README.md](tooling/estates/README.md) | Estate supplements |
| [tooling/estates/TEMPLATE.md](tooling/estates/TEMPLATE.md) | Scaffold |
| [tooling/estates/minimum-viable-doctrine.template.md](tooling/estates/minimum-viable-doctrine.template.md) | One-page team pitch |
| [tooling/estates/azure-container-runtimes.md](tooling/estates/azure-container-runtimes.md) | Example Azure |
| [tooling/estates/aws-container-runtimes.md](tooling/estates/aws-container-runtimes.md) | AWS stub (fill from TEMPLATE) |
| [tooling/estates/gcp-container-runtimes.md](tooling/estates/gcp-container-runtimes.md) | GCP stub (fill from TEMPLATE) |
