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
| OpenGitOps (principles, community) | https://opengitops.dev/ |
| OpenGitOps — GitOps Principles v1.0.0 (source) | https://raw.githubusercontent.com/open-gitops/documents/v1.0.0/PRINCIPLES.md |
| OWASP — Top 10 CI/CD Security Risks | https://owasp.org/www-project-top-10-ci-cd-security-risks/ |
| NIST — SSDF (SP 800-218) | https://csrc.nist.gov/publications/detail/sp/800-218/final |
| Twelve-Factor App — Config | https://12factor.net/config |

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
| OWASP — Secure by Design Framework | https://owasp.org/www-project-secure-by-design-framework/ |
| CSA Lab — “AI Vulnerability Storm” / Mythos-ready security program (strategy briefing) | https://labs.cloudsecurityalliance.org/research/ai-vulnerability-storm-mythos-ready-security-program/ |
| CSA — Mythos CISO briefing hub | https://labs.cloudsecurityalliance.org/mythos-ciso/ |
| Anthropic — Project Glasswing (industry defensive coordination initiative) | https://www.anthropic.com/project/glasswing |
| Anthropic — Frontier Red Team, Claude Mythos Preview | https://red.anthropic.com/2026/mythos-preview/ |
| CISA & NSA — Defending CI/CD environments | https://www.cisa.gov/news-events/alerts/2023/06/28/cisa-and-nsa-release-joint-guidance-defending-continuous-integrationcontinuous-delivery-cicd |
| NIST — Strategies for the integration of software supply chain security in DevSecOps CI/CD pipelines | https://www.nist.gov/publications/strategies-integration-software-supply-chain-security-devsecops-cicd-pipelines |
| ISO/IEC 27002:2022 — information security controls (incl. technical vulnerability management) | https://www.iso.org/standard/75652.html |

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

Used by `principles/ai-ml-systems.md`, `patterns/rag-retrieval-baseline.md`, `patterns/agentic-loop-design.md`, `patterns/ai-native-software-development-lifecycle.md`, and the `tooling/` AI supplement.

| Topic | Reference |
| --- | --- |
| NIST AI Risk Management Framework (AI RMF 1.0) | https://www.nist.gov/itl/ai-risk-management-framework |
| NIST AI 100-1 (AI RMF PDF) | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf |
| NIST AI 600-1 — Generative AI Profile | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf |
| NIST SP 800-218A (GenAI / foundation models, SSDF profile) | https://csrc.nist.gov/pubs/sp/800/218/a/final |
| NIST AI RMF Core — mission/goals, business value, tasks, benefits/costs, measures | https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ |
| ISACA — COBIT 2019 Goals Cascade | https://www.isaca.org/resources/news-and-trends/industry-news/2019/employing-cobit-2019-for-enterprise-governance-strategy |
| Basili et al. — GQM+Strategies | https://arxiv.org/abs/1402.0292 |
| University of Maryland — Goal/Question/Metric technical report | https://drum.lib.umd.edu/items/8119803a-362b-42ec-b6ce-2311713e7236 |
| DORA — software delivery performance metrics and pitfalls | https://dora.dev/guides/dora-metrics/ |
| Google — OKR playbook (practitioner guidance, reprinted with permission) | https://www.whatmatters.com/resources/google-okr-playbook |
| NCSC/CISA et al. — Guidelines for Secure AI System Development | https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development/guidelines |
| ISO/IEC 5338:2023 — AI system life cycle processes | https://www.iso.org/standard/81118.html |
| SLSA Specification v1.2 | https://slsa.dev/spec/v1.2/ |
| EU AI Act — Regulation (EU) 2024/1689 | https://eur-lex.europa.eu/eli/reg/2024/1689/oj |
| AWS — AI-Driven Development Life Cycle (vendor observation) | https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/ |
| Microsoft — AI-led SDLC (vendor observation) | https://techcommunity.microsoft.com/blog/appsonazureblog/an-ai-led-sdlc-building-an-end-to-end-agentic-software-development-lifecycle-wit/4491896 |
| GitHub Spec Kit — Evolving specifications (vendor observation) | https://github.github.com/spec-kit/guides/evolving-specs.html |
| Anthropic — 2026 Agentic Coding Trends Report (vendor research; landing page links the report) | https://resources.anthropic.com/2026-agentic-coding-trends-report |
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

## AI Governance And Regulation

Used by `principles/ai-ml-systems.md`, `patterns/ai-adoption-controls.md`, `principles/threat-modeling-stride-lite.md` §3.1, and `checklists/ai-adoption-readiness.md`. Regulators are cited as **rationale and vocabulary**, not as obligations this doctrine imposes.

| Topic | Reference |
| --- | --- |
| NIST AI RMF 1.0 (GOVERN 1.6 inventory; Map/Measure/Manage) | https://www.nist.gov/itl/ai-risk-management-framework |
| NIST AI RMF Playbook — GOVERN | https://airc.nist.gov/airmf-resources/playbook/govern/ |
| NIST AI 600-1 — Generative AI Profile | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf |
| Federal Reserve SR 11-7 — model risk management, effective challenge | https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm |
| PRA SS1/23 — model risk management principles (inventory + tiering, independent validation) | https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss |
| EU AI Act — Art 4 literacy, Art 12 logging, Art 14 human oversight, Art 15 lifecycle accuracy, Art 26 deployers | https://artificialintelligenceact.eu/ |
| EU DORA — Art 28 register + exit strategies, Art 29 concentration risk | https://www.digital-operational-resilience-act.com/Article_28.html |
| EBA outsourcing guidelines (EBA/GL/2019/02) | https://www.eba.europa.eu/activities/single-rulebook/regulatory-activities/internal-governance/guidelines-outsourcing-arrangements |
| FCA PS21/3 — operational resilience (important business services, impact tolerances) | https://www.fca.org.uk/publications/policy-statements/ps21-3-building-operational-resilience |
| BoE/FCA — AI in UK financial services 2024 (adoption survey) | https://www.bankofengland.co.uk/report/2024/artificial-intelligence-in-uk-financial-services-2024 |
| FSB — Financial stability implications of AI (2024) | https://www.fsb.org/2024/11/the-financial-stability-implications-of-artificial-intelligence/ |
| IAIS — Application paper on supervision of AI (2025) | https://www.iais.org/uploads/2025/07/Application-Paper-on-the-supervision-of-artificial-intelligence.pdf |
| ISO/IEC 42001:2023 — AI management systems | https://www.iso.org/standard/42001 |
| ISO/IEC 23894:2023 — AI risk management guidance | https://www.iso.org/standard/77304.html |
| MITRE ATLAS — adversary tactics against AI | https://atlas.mitre.org/ |
| UK AISI Inspect — evaluation harness | https://inspect.aisi.org.uk/ |
| NCSC — impact of AI on the cyber threat | https://www.ncsc.gov.uk/report/impact-of-ai-on-cyber-threat |
| FinCEN FIN-2024-Alert004 — deepfake fraud targeting financial institutions | https://www.fincen.gov/system/files/shared/FinCEN-Alert-DeepFakes-Alert508FINAL.pdf |
| Europol — deepfakes and law enforcement | https://www.europol.europa.eu/publications-events/publications/facing-reality-law-enforcement-and-challenge-of-deepfakes |

---

## Architecture Decisions

| Topic | Reference |
| --- | --- |
| ADR GitHub community | https://adr.github.io/ |

---

## Internal Doctrine Map

### Machine-readable contracts

| File | Focus |
| --- | --- |
| [../contracts/run-contract.v1.schema.json](../contracts/run-contract.v1.schema.json) | Run-contract v1 JSON Schema 2020-12; consumed by `patterns/run-contracts.md` |
| [../contracts/verifier-pack.v1.schema.json](../contracts/verifier-pack.v1.schema.json) | Verifier-pack v1 JSON Schema 2020-12; consumed by `patterns/verifier-packs.md` |
| [../contracts/router-policy.v1.schema.json](../contracts/router-policy.v1.schema.json) | Router-policy v1 JSON Schema 2020-12; consumed by ADR-0012; structural 3-tier shape (`tiers: { premium, default, narrow_scope }`) + escalation + refusal rules + two-tier cost ceilings |
| [../contracts/examples/default-production.router-policy.yaml](../contracts/examples/default-production.router-policy.yaml) | v3 production-default router policy (3-tier: premium/default/narrow_scope; FALSIFIED-escalates default → premium; haiku narrow-scope with mandatory external review) |
| [../contracts/examples/enterprise-strict.router-policy.yaml](../contracts/examples/enterprise-strict.router-policy.yaml) | Strict-estate variant: immediate premium escalation on first FALSIFIED, haiku denied beyond scaffolded subtasks, lower per-session kill |
| [../contracts/examples/experimental-haiku-narrow-scope.router-policy.yaml](../contracts/examples/experimental-haiku-narrow-scope.router-policy.yaml) | Narrow_scope haiku tier exercised in production with mandatory external review (sample rate 1.0); permitted only for scaffolded_typed_authority cells |
| [../scripts/validate-contracts-v1.py](../scripts/validate-contracts-v1.py) | Reference Python validator (uses `jsonschema`) for all three v1 schemas; positive in-memory + on-disk YAML cases + 12 router-policy negative cases |

### Umbrella and meta

| File | Focus |
| --- | --- |
| [../ENGINEERING.md](../ENGINEERING.md) | Headline principles index (repo root) |
| [../CHANGELOG.md](../CHANGELOG.md) | Version history for **SemVer-shaped** doctrine tags |
| [../AGENTS.md](../AGENTS.md) | Short agent instructions; points at **harness** for library edits |
| [SEMANTIC_INDEX.md](SEMANTIC_INDEX.md) | Semantic route map for humans and agents: ingestion set, task routes, evidence paths |
| [patterns/doctrine-library-change-harness.md](patterns/doctrine-library-change-harness.md) | **Library change** workflow: research, ADR, cross-links, sitemap, glossary, refs |
| [principles/timeless-principles-and-tooling.md](principles/timeless-principles-and-tooling.md) | Principles vs tooling vs estates |
| [evolution/moscow-review.md](evolution/moscow-review.md) | Audit trail, MoSCoW, thin-area notes |
| [evolution/scorecard-vs-mainstream-frameworks.md](evolution/scorecard-vs-mainstream-frameworks.md) | Domain-by-domain scorecard vs 11 mainstream frameworks (Google SRE, DORA, AWS WAF, NIST, etc.) |
| [evolution/honest-review-synthesis.md](evolution/honest-review-synthesis.md) | Condensed external review signal |
| [evolution/deep-research-section-gaps.md](evolution/deep-research-section-gaps.md) | Section-by-section gap research |
| [evolution/public-doctrine-benchmark-gap-analysis-2026-04.md](evolution/public-doctrine-benchmark-gap-analysis-2026-04.md) | Public doctrine benchmark, scorecard, and residual gap analysis |
| [evolution/public-doctrine-taxonomy-scorecard-and-choice-2026-04-27.md](evolution/public-doctrine-taxonomy-scorecard-and-choice-2026-04-27.md) | Taxonomy of public *kinds* of doctrine, honest scorecard refresh, **which to choose when** |
| [evolution/anti-patterns-and-failure-modes-gap-analysis-2026-04.md](evolution/anti-patterns-and-failure-modes-gap-analysis-2026-04.md) | Public anti-patterns / failure modes benchmark, taxonomy, and gap analysis |
| [evolution/research-ai-ml-ops-landscape-2026-04.md](evolution/research-ai-ml-ops-landscape-2026-04.md) | AI/ML ops, governance, RAG, Azure AI Landing Zone — external sources + doctrine map |
| [evolution/research-internal-ai-knowledge-factory-governance-2026-04.md](evolution/research-internal-ai-knowledge-factory-governance-2026-04.md) | Internal AI knowledge layer, handoffs, councils, agentic workflows — enterprise governance + doctrine map (no build specs) |
| [evolution/research-enterprise-rag-agents-indexing-2026-04.md](evolution/research-enterprise-rag-agents-indexing-2026-04.md) | Enterprise RAG, ANN/indexing, hybrid search, MCP/agents — synthesis + doctrine gap map |
| [evolution/mythos-era-engineering-principles-research-2026-04-28.md](evolution/mythos-era-engineering-principles-research-2026-04-28.md) | AI-accelerated vuln discovery, VulnOps, principle clusters — **research**; [ADR 0010](../docs/adr/0010-record-mythos-era-vulnerability-storm-research-and-doctrine-gaps.md) maps **G1–G6** to closed corpus sections |
| [evolution/research-ai-adoption-control-gaps-2026-07.md](evolution/research-ai-adoption-control-gaps-2026-07.md) | AI adoption-control gap audit (inventory/materiality, effective challenge, fairness/drift, provider continuity, literacy) — coverage map + verified authorities; [ADR 0023](../docs/adr/0023-add-ai-adoption-control-coverage-inventory-challenge-testing-continuity-literacy.md) maps **A1–A8** to closed corpus sections |
| [evolution/research-ai-native-sdlc-2026-07.md](evolution/research-ai-native-sdlc-2026-07.md) | Council-proposal audit and primary-source grounding for the AI-native SDLC, including objective/measure lineage; separates external support from the library's objective-to-outcome and eleven-state synthesis; [ADR 0024](../docs/adr/0024-adopt-a-doctrine-grounded-ai-native-software-development-lifecycle.md) records adoption |
| [../docs/adr/0012-model-routing-policy.md](../docs/adr/0012-model-routing-policy.md) | ADR (Proposed): model routing policy v1 contract; structural 3-tier shape (premium/default/narrow_scope) + escalation + non-empty evidence-backed refusal rules + two-tier cost ceilings; encodes the v3 9-cell scoreboard, the council-D4 3-tier resolution, and the CC-2 interpreter-wrapper refusal |
| [../docs/adr/0010-record-mythos-era-vulnerability-storm-research-and-doctrine-gaps.md](../docs/adr/0010-record-mythos-era-vulnerability-storm-research-and-doctrine-gaps.md) | ADR: research adoption + **G1–G6** closure traceability |
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
| [patterns/code-review-and-change-approval.md](patterns/code-review-and-change-approval.md) | PR/MR **duties**, blockers vs nits, review latency, high-risk classes, **LLM**/**agent**-authored diffs, escalation when review disagrees |
| [patterns/gitops-and-declarative-operations.md](patterns/gitops-and-declarative-operations.md) | **GitOps** (cites **OpenGitOps** v1.0, **OWASP** CI/CD top 10, **NIST** SSDF pointer, **12factor**); portable invariants; then **in-repo** **alignment** to build / **SSOT** / **merge** path |
| [patterns/platform-as-product-and-golden-paths.md](patterns/platform-as-product-and-golden-paths.md) | Platform-as-product, golden paths, self-service guardrails, service catalog (portable) |
| [patterns/example-order-jetstream-workflow.md](patterns/example-order-jetstream-workflow.md) | Fictional order FSM + JetStream sketch |
| [patterns/example-saga-payment-workflow.md](patterns/example-saga-payment-workflow.md) | Fictional saga + compensation sketch |
| [patterns/chaos-engineering-and-game-days.md](patterns/chaos-engineering-and-game-days.md) | Chaos experiments and game days |
| [patterns/incident-lifecycle-and-on-call-operations.md](patterns/incident-lifecycle-and-on-call-operations.md) | Incident lifecycle, IC, comms, state doc, escalation, handoff, on-call sustainability, post-incident actions |
| [patterns/webhook-ingress-security.md](patterns/webhook-ingress-security.md) | Webhook ingress hardening |
| [patterns/idempotency-across-boundaries.md](patterns/idempotency-across-boundaries.md) | Idempotency patterns |
| [patterns/rag-retrieval-baseline.md](patterns/rag-retrieval-baseline.md) | RAG retrieval: hybrid search, eval, privacy/security baseline |
| [patterns/engineering-controls-governance-program.md](patterns/engineering-controls-governance-program.md) | Org-level governance programme for merge-path / supply-chain controls (CSF 2.0 Govern / GV.SC) |
| [patterns/ai-adoption-controls.md](patterns/ai-adoption-controls.md) | AI adoption operating model: inventory + materiality, ownership + effective challenge, harm-surface test matrix, provider continuity, role-based literacy (NIST AI RMF / SR 11-7 / SS1/23 / DORA / AI Act–cited) |
| [patterns/ai-native-software-development-lifecycle.md](patterns/ai-native-software-development-lifecycle.md) | AI-native SDLC: objective-to-outcome chain, S0–S10 evidence-backed transitions, transition records, authority separation, layered evidence, deterministic enactment, runtime reconciliation |
| [patterns/feature-flag-lifecycle.md](patterns/feature-flag-lifecycle.md) | Feature flag taxonomy, lifecycle FSM, progressive delivery, flag debt |
| [patterns/agentic-loop-design.md](patterns/agentic-loop-design.md) | Agent harness patterns: nested loop, verifiability gate, ISC, autonomy slider, dual-path injection defence, context engineering, verbal RL |
| [patterns/run-contracts.md](patterns/run-contracts.md) | Run contracts as the first-class typed envelope of agent execution; lifecycle, schema surface, validation tooling; §3.5 auto-bundled skills |
| [patterns/verifier-packs.md](patterns/verifier-packs.md) | Verifier packs as the mandatory mirror of every skill; 11 canonical kinds plus `custom`, fail-loud verdicts, discovery convention |
| [patterns/anti-confabulation-priming.md](patterns/anti-confabulation-priming.md) | Anti-confabulation priming pattern for build-class agents; canonical ~200-token block lifts Sonnet 4.6 canonical 78→85; hash-anchored doctrine artefact |
| [skills/anti-confabulation.skill.md](skills/anti-confabulation.skill.md) | Skill pack containing the verbatim canonical priming block (SHA-256 `c138dd96…`); auto-bundled into build-class run contracts |

### Extended principles

| File | Focus |
| --- | --- |
| [principles/ai-ml-systems.md](principles/ai-ml-systems.md) | GenAI, RAG, agents; governance tiers; merge path |
| [principles/data-and-migrations.md](principles/data-and-migrations.md) | Schema evolution, backups |
| [principles/observability.md](principles/observability.md) | Logs, metrics, traces |
| [principles/testing-strategy.md](principles/testing-strategy.md) | Pyramid, contracts, flakiness, adversarial CI / abuse-case testing (§5) |
| [principles/state-machines-and-workflows.md](principles/state-machines-and-workflows.md) | FSM, transitions, event-type mapping |
| [principles/api-boundaries-and-security.md](principles/api-boundaries-and-security.md) | HTTP limits, OWASP API |
| [principles/threat-modeling-stride-lite.md](principles/threat-modeling-stride-lite.md) | STRIDE-lite trust-boundary review |
| [principles/privacy-and-data-governance.md](principles/privacy-and-data-governance.md) | PII, retention |
| [principles/reliability-slo-incidents.md](principles/reliability-slo-incidents.md) | SLOs, incidents; [patterns/incident-lifecycle-and-on-call-operations.md](patterns/incident-lifecycle-and-on-call-operations.md) for full incident lifecycle / on-call |
| [principles/performance-and-cost.md](principles/performance-and-cost.md) | Load, FinOps |
| [principles/cost-and-finops.md](principles/cost-and-finops.md) | FinOps operating model, unit economics, anomaly detection, AI inference cost |
| [principles/platform-engineering.md](principles/platform-engineering.md) | Team topologies, TVP, golden paths, cognitive load |
| [principles/documentation-knowledge.md](principles/documentation-knowledge.md) | ADRs, runbooks |
| [principles/dependencies-supply-chain.md](principles/dependencies-supply-chain.md) | SBOM, licences |
| [principles/merge-path-evidence-and-pipeline-integrity.md](principles/merge-path-evidence-and-pipeline-integrity.md) | Merge path, pipeline definitions, binding gates, evidence (NIST / CSF / CISA / SLSA–cited) |
| [principles/developer-experience.md](principles/developer-experience.md) | DevEx, time-to-first-change, local loop, docs findability, cognitive load, review flow |
| [principles/user-facing-quality.md](principles/user-facing-quality.md) | A11y, i18n |
| [principles/measurement-and-dora.md](principles/measurement-and-dora.md) | Current DORA delivery metrics, metric pitfalls, and delivery-signal/company-objective boundary |

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
| [checklists/ai-adoption-readiness.md](checklists/ai-adoption-readiness.md) | AI adoption: inventory/materiality, challenge, harm-surface tests, provider continuity, uplift |
| [checklists/ai-native-sdlc-readiness.md](checklists/ai-native-sdlc-readiness.md) | AI-native delivery readiness: objective/outcome lineage, design, agent bounds, evidence, authority, enactment, runtime reconciliation |

### Estates

| File | Focus |
| --- | --- |
| [tooling/estates/README.md](tooling/estates/README.md) | Estate supplements |
| [tooling/estates/TEMPLATE.md](tooling/estates/TEMPLATE.md) | Scaffold |
| [tooling/estates/minimum-viable-doctrine.template.md](tooling/estates/minimum-viable-doctrine.template.md) | One-page team pitch |
| [tooling/estates/azure-container-runtimes.md](tooling/estates/azure-container-runtimes.md) | Example Azure |
| [tooling/estates/aws-container-runtimes.md](tooling/estates/aws-container-runtimes.md) | AWS stub (fill from TEMPLATE) |
| [tooling/estates/gcp-container-runtimes.md](tooling/estates/gcp-container-runtimes.md) | GCP stub (fill from TEMPLATE) |
