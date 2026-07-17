# Glossary

Short definitions for terms used across this doctrine. **Normative detail** lives in linked principles, patterns, and external specs—this page is for **orientation** only.

See also: **[tldr-principles-and-mvp.md](tldr-principles-and-mvp.md)** (spine + MVP), **[REFERENCES.md](REFERENCES.md)** (external authorities).

---

## A

**Acceptance (of messages)** — Consumer tells the broker it finished processing; behaviour (single vs cumulative ack, redelivery) is **broker-specific**. See [message-channel-operations.md](patterns/message-channel-operations.md).

**ADR (Architecture Decision Record)** — In-repo note: context, decision, consequences; superseded decisions stay linked. See [documentation-knowledge.md](principles/documentation-knowledge.md).

**Agentic workflow** — An LLM **plans** and invokes **tools** (HTTP, CLI, browser, etc.) in **iterative** steps; treat like a new **client** at trust boundaries (SSRF, cost, audit). See [ai-ml-systems.md](principles/ai-ml-systems.md) §§2–4, §7, [api-boundaries-and-security.md](principles/api-boundaries-and-security.md), [research-internal-ai-knowledge-factory-governance-2026-04.md](evolution/research-internal-ai-knowledge-factory-governance-2026-04.md) §7.

**AI RMF (NIST)** — *Artificial Intelligence Risk Management Framework* (NIST AI 100-1): **Govern, Map, Measure, Manage**—**Govern** is cross-cutting. **Generative AI** companion: **NIST AI 600-1**. See [research-internal-ai-knowledge-factory-governance-2026-04.md](evolution/research-internal-ai-knowledge-factory-governance-2026-04.md) §2.

**AI literacy** — **Role-based** capability to use, oversee, or challenge AI systems: builders ≠ reviewers ≠ approvers ≠ everyday users (EU AI Act **Art 4** vocabulary: "sufficient" literacy is contextual). See [ai-adoption-controls.md](patterns/ai-adoption-controls.md) §5.

**AI-native SDLC** — Software delivery in which AI participates across lifecycle work while stakeholder need, objective, guardrailed outcome measures, intervention hypothesis, bounded work, executable change, authority, verification evidence, enactment, and observed outcome remain separate, addressable records advanced through governed transitions. Tasks and outputs are not outcomes; AI participation does not imply autonomous merge or deploy. See [ai-native-software-development-lifecycle.md](patterns/ai-native-software-development-lifecycle.md).

**AI system inventory** — Owned, **materiality**-tiered register of every AI system in production or on real data — including **embedded**, **vendor**, and **copilot**-class AI. Root control of AI adoption (NIST AI RMF **GOVERN 1.6**); each entry carries owner, capability tier, materiality, data classes, dependencies, oversight mode, test evidence. See [ai-adoption-controls.md](patterns/ai-adoption-controls.md) §1, [ai-ml-systems.md](principles/ai-ml-systems.md) §3.

**AILZ / Azure AI Landing Zone** — Microsoft’s **reference application landing zone** for AI workloads on Azure (e.g. **Foundry** and/or **APIM** as AI gateway); **preview**-style, **estate**-level mapping—not portable law. See [research-ai-ml-ops-landscape-2026-04.md](evolution/research-ai-ml-ops-landscape-2026-04.md) §2.

**ANN** — *Approximate nearest neighbour*: index structures (e.g. **HNSW**, **IVF** families) that trade **recall** vs **latency** vs **memory** for embedding search. See [ai-ml-systems.md](principles/ai-ml-systems.md) §7, [research-enterprise-rag-agents-indexing-2026-04.md](evolution/research-enterprise-rag-agents-indexing-2026-04.md) §3.

**Artefact / artifact** — Versioned output of a build (binary, image, package, chart). This library often uses **artefact** (British spelling); tools and US docs may say **artifact**. See [build.md](principles/build.md).

**At-least-once delivery** — A message or request may arrive **more than once**; handlers must be **idempotent** or **dedupe** explicitly. See [event-contracts.md](principles/event-contracts.md), [idempotency-across-boundaries.md](patterns/idempotency-across-boundaries.md).

**Audit log** — Append-oriented record of **who** did **what** to **which** resource, for security and compliance—not the same as product analytics. See [audit-logging.md](principles/audit-logging.md).

---

## B

**Blameless postmortem** — Incident review focused on **system** and **process** fixes, not individual fault; actions tracked to completion. See [reliability-slo-incidents.md](principles/reliability-slo-incidents.md), [collaboration.md](principles/collaboration.md).

**Blocker (review comment)** — Feedback that must be resolved (or a time-bounded waiver recorded) before merge: correctness, security, contract, or regulatory gap—not mere preference unless policy says otherwise. See [code-review-and-change-approval.md](patterns/code-review-and-change-approval.md) §3.

**BOLA / BOPLA** — *Broken object (and property) level authorisation*: access control bugs where callers reach others’ objects or fields. Top theme in OWASP API Top 10. See [api-boundaries-and-security.md](principles/api-boundaries-and-security.md).

**BM25** — *Best Matching 25*: classic **lexical** relevance ranking (sparse retrieval); pairs with **dense** vector search in **hybrid** RAG. See [rag-retrieval-baseline.md](patterns/rag-retrieval-baseline.md) §1.

**Build surface** — Named entrypoint in the delivery model (quality gate, build/publish, deploy, verify, etc.). See [build.md](principles/build.md), [build-surface-model.md](patterns/build-surface-model.md).

---

## C

**Canary / gradual rollout** — Release to a **small** slice first, expand if healthy; limits blast radius. See [collaboration.md](principles/collaboration.md).

**Chaos engineering** — **Controlled** fault injection and game days to validate resilience **before** production surprises. See [reliability-slo-incidents.md](principles/reliability-slo-incidents.md).

**Chunking** — Splitting documents into **retrieval-sized** segments (often hundreds of tokens) with metadata (source, heading, tenant); quality dominates RAG outcomes. See [rag-retrieval-baseline.md](patterns/rag-retrieval-baseline.md) §2, [tooling/vector-retrieval-and-embedding-illustration.md](tooling/vector-retrieval-and-embedding-illustration.md).

**CloudEvents** — Vendor-neutral **envelope** for events (`id`, `source`, `type`, `time`, …) over HTTP, Kafka, NATS, etc.; **payload** still needs its own schema. See [event-contracts.md](principles/event-contracts.md), [tooling/cloudevents.md](tooling/cloudevents.md).

**CODEOWNERS** — Git host file mapping **paths** to **required reviewers** (teams or individuals). See [collaboration.md](principles/collaboration.md), [naming-and-repo-layout.md](principles/naming-and-repo-layout.md).

**Contract** — Explicit, versioned **shape** and rules at a boundary (schema, OpenAPI, proto, migration contract). Violations are **build or runtime failures** per policy—not informal JSON. See [ENGINEERING.md](../ENGINEERING.md) §1.

**Context window** — Maximum **tokens** a model can take as input per call; large windows do **not** remove need for **RAG** on big or **governed** corpora. See [performance-and-cost.md](principles/performance-and-cost.md) §3, [ai-ml-systems.md](principles/ai-ml-systems.md).

**Council (multi-agent)** — Several LLM **roles** (or agents) **critique** one proposal before a human decision—useful for **diversity of critique**, weak against **agreement bias** and **false confidence**; **not** a substitute for **CI** or review. See [research-internal-ai-knowledge-factory-governance-2026-04.md](evolution/research-internal-ai-knowledge-factory-governance-2026-04.md) §6.

**CUI** — *Controlled Unclassified Information*: information the U.S. Government creates or possesses, or that an entity creates or possesses for or on its behalf, that a law, regulation, or government-wide policy requires or permits an agency to handle using safeguarding or dissemination controls. Establish the governing authority, category/marking, exact baseline revision, and bounded system/data scope; do not infer CUI solely from content sensitivity. See [Revision-Pinned External Control Profiles](patterns/revision-pinned-control-profiles.md) and the [NARA CUI programme](https://www.archives.gov/cui).

**CORS / CSP** — *Cross-Origin Resource Sharing* and *Content Security Policy*: browser-facing controls for APIs and pages. See [api-boundaries-and-security.md](principles/api-boundaries-and-security.md).

**Cross-encoder (reranking)** — Model that scores **query–passage** pairs for **precision** after cheap candidate retrieval; common **second stage** in RAG. See [rag-retrieval-baseline.md](patterns/rag-retrieval-baseline.md) §1.

---

## D

**Dead letter queue (DLQ)** — Destination for messages that **failed** processing after policy limits; avoids infinite retry loops. See [message-channel-operations.md](patterns/message-channel-operations.md).

**Deployable unit** — Thing you **ship or operate** with its own lifecycle (app, infra module, automation package, etc.); often maps to **separate** deploy surfaces. See [build.md](principles/build.md).

**DORA delivery metrics** — Current delivery-system signals across throughput and instability: *change lead time*, *deployment frequency*, *failed deployment recovery time*, *change fail rate*, and *deployment rework rate*. They are not universal company objectives or individual targets. See [measurement-and-dora.md](principles/measurement-and-dora.md).

**DPIA / PIA** — *Data protection* or *privacy* **impact assessment** for high-risk processing. See [privacy-and-data-governance.md](principles/privacy-and-data-governance.md).

---

## E

**Effective challenge** — Independent review with **incentives** (not invested in delivery), **competence** (can identify limitations and assumptions), and **influence** (authority to force change) — the SR 11-7 test for whether "second opinion" review is real. See [ai-adoption-controls.md](patterns/ai-adoption-controls.md) §2.

**Error budget** — Allowed **unreliability** derived from an SLO; spending it signals **slow down or invest** in reliability. See [reliability-slo-incidents.md](principles/reliability-slo-incidents.md).

**Estate** — In this repo: a **specific** organisation, cloud, or region whose **named** product choices live under `tooling/estates/`—not global law. See [timeless-principles-and-tooling.md](principles/timeless-principles-and-tooling.md).

**Exactly-once (illusion)** — True end-to-end **exactly-once side effects** are rare; most systems are **at-least-once** plus **idempotent** design. See [message-channel-operations.md](patterns/message-channel-operations.md).

**Embedding** — Numeric **vector** representing text (or other content) for **similarity** search; used in **dense** retrieval alongside **lexical** search in typical RAG. Changing **model** or **dimensions** forces **re-embed** and index **migration** ([ai-ml-systems.md](principles/ai-ml-systems.md) §7). See [rag-retrieval-baseline.md](patterns/rag-retrieval-baseline.md).

---

## F

**Feature flag** — Toggle for **incomplete** or **risky** behaviour; safe defaults and **removal** discipline required. See [collaboration.md](principles/collaboration.md).

**FinOps** — Cost **visibility**, allocation, and governance for cloud spend. See [performance-and-cost.md](principles/performance-and-cost.md).

---

## G

**GenAI** — *Generative artificial intelligence*: models that **synthesize** content (text, code, media). Portable rules: [ai-ml-systems.md](principles/ai-ml-systems.md); security framing: **OWASP LLM Top 10**, **NIST AI 600-1**, **NIST SP 800-218A**. Research: [evolution/research-ai-ml-ops-landscape-2026-04.md](evolution/research-ai-ml-ops-landscape-2026-04.md), [evolution/research-enterprise-rag-agents-indexing-2026-04.md](evolution/research-enterprise-rag-agents-indexing-2026-04.md).

**GenAIOps** — Operating **GenAI** systems in production: **eval** and regression on outputs/retrieval, **index** freshness and **embedding** migrations, **cost** and quota governance, **provider** resilience, and **observability** (trace to chunk/tool ids)—same **SRE** habits as other critical dependencies. See [ai-ml-systems.md](principles/ai-ml-systems.md) §§6–7, [rag-retrieval-baseline.md](patterns/rag-retrieval-baseline.md) §4, [reliability-slo-incidents.md](principles/reliability-slo-incidents.md).

**Golden path** — Org’s **blessed** default way to build/run a service (scaffold → gates → promote → operate). See [platform-as-product-and-golden-paths.md](patterns/platform-as-product-and-golden-paths.md).

**GitOps** — In this library: **anchored** to **OpenGitOps** v1.0.0 [PRINCIPLES.md](https://raw.githubusercontent.com/open-gitops/documents/v1.0.0/PRINCIPLES.md) (declarative, versioned, pull, reconcile) plus [OWASP Top 10 CI/CD Security Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/) and [NIST SSDF](https://csrc.nist.gov/publications/detail/sp/800-218/final) *pointers* in [gitops-and-declarative-operations.md](patterns/gitops-and-declarative-operations.md), then mapped to in-repo build/collab/merge-path doctrine. Community hub: [OpenGitOps](https://opengitops.dev/).

**Grounding** — Supplying the model with **retrieved** or **tool-fetched** facts so answers cite **organisation** truth; still vulnerable to **injection** in retrieved text. See [rag-retrieval-baseline.md](patterns/rag-retrieval-baseline.md), OWASP [LLM Top 10](https://genai.owasp.org/llm-top-10/).

---

## H

**Handoff (structured)** — Passing **goal**, **constraints**, **verified state**, and **next actions** between people and/or **agents**—same shape as a strong **PR** description, not a raw chat log. See [research-internal-ai-knowledge-factory-governance-2026-04.md](evolution/research-internal-ai-knowledge-factory-governance-2026-04.md) §5, [collaboration.md](principles/collaboration.md) §3.

**HNSW** — *Hierarchical Navigable Small World*: popular **ANN** graph index for embedding search; tune for recall/latency as corpus grows. See [ai-ml-systems.md](principles/ai-ml-systems.md) §7, [research-enterprise-rag-agents-indexing-2026-04.md](evolution/research-enterprise-rag-agents-indexing-2026-04.md) §3.

**Hermetic build** — Build with **declared** inputs only (pinned toolchains, lockfiles) so outputs are **reproducible** and auditable. See [build.md](principles/build.md) §14.

**Hexagonal / ports and adapters** — Core domain isolated from I/O via **interfaces**; adapters implement DB, HTTP, queues. See [modularity-and-ports-adapters.md](principles/modularity-and-ports-adapters.md).

**Hybrid search** — **Parallel** (or fused) **lexical** (e.g. BM25) and **dense** (embedding) retrieval, then **fusion** (e.g. **RRF**) and often **reranking**. See [rag-retrieval-baseline.md](patterns/rag-retrieval-baseline.md) §1.

---

## I

**Idempotency** — Repeating an operation with the **same intent** does not **compound** harm (safe retries, dedupe keys). See [ENGINEERING.md](../ENGINEERING.md) §4, [idempotency-across-boundaries.md](patterns/idempotency-across-boundaries.md).

**Incident command / incident lifecycle** — Coordinated **response** to a production-impacting event: **incident commander**, **comms** cadence, **state doc** (single source of truth), **escalation**, **handoff**, **sustainable** on-call, **post-incident** **actions**. See [incident-lifecycle-and-on-call-operations.md](patterns/incident-lifecycle-and-on-call-operations.md), [reliability-slo-incidents.md](principles/reliability-slo-incidents.md).

**IDOR** — *Insecure direct object reference*—often overlaps **BOLA**. See [api-boundaries-and-security.md](principles/api-boundaries-and-security.md).

**Ingestion pipeline (RAG)** — Jobs that **extract**, **chunk**, **embed**, and **write** lexical/vector indexes—**separate** from online **query** path; needs **freshness** SLAs and **idempotent** rebuilds. See [ai-ml-systems.md](principles/ai-ml-systems.md) §7, [tooling/vector-retrieval-and-embedding-illustration.md](tooling/vector-retrieval-and-embedding-illustration.md).

**IVF** — *Inverted file* (clustering-based) **ANN** structure; common at **large** scale; may need **training** on representative vectors and **re-tuning** when the corpus distribution shifts. See [research-enterprise-rag-agents-indexing-2026-04.md](evolution/research-enterprise-rag-agents-indexing-2026-04.md) §3.

---

## L

**LLM** — *Large language model*: often backs **chat** or **agent** UIs; treat **output** and **retrieved context** as **untrusted** at system boundaries until validated. See [api-boundaries-and-security.md](principles/api-boundaries-and-security.md) Related, [rag-retrieval-baseline.md](patterns/rag-retrieval-baseline.md); OWASP [LLM Top 10](https://genai.owasp.org/llm-top-10/).

**Lexical search** — Keyword / **inverted-index** retrieval (e.g. **BM25**); complements **semantic** vector search in **hybrid** RAG. See [rag-retrieval-baseline.md](patterns/rag-retrieval-baseline.md) §1.

**LTS (long-term support) branch** — Exceptional **parallel** line for extended patch support; document EOL. See [trunk-workflow.md](patterns/trunk-workflow.md).

---

## M

**Materiality (AI)** — Business-impact tier of an AI system (person-affected decisions, money movement, irreversibility, blast radius) — **orthogonal** to capability tiers A–D; controls scale with the **max** of the two. See [ai-ml-systems.md](principles/ai-ml-systems.md) §2.1, [ai-adoption-controls.md](patterns/ai-adoption-controls.md) §1.1.

**MCP (Model Context Protocol)** — Open **client–server** protocol for AI **hosts** to discover **tools** and **resources** (often JSON-RPC); treat servers as **production** integrations (authz, audit, supply chain). Docs: https://modelcontextprotocol.io — see [ai-ml-systems.md](principles/ai-ml-systems.md) §7, [research-enterprise-rag-agents-indexing-2026-04.md](evolution/research-enterprise-rag-agents-indexing-2026-04.md) §4.

**Merge queue** — Serialises merges to `main` by testing the **merged** result; reduces “green branch, red main.” See [collaboration.md](principles/collaboration.md), [trunk-workflow.md](patterns/trunk-workflow.md).

**Minimum viable doctrine (MVP)** — Smallest practice set that makes **further** adoption safe; team-specific one-pager in [minimum-viable-doctrine.template.md](tooling/estates/minimum-viable-doctrine.template.md). See [tldr-principles-and-mvp.md](tldr-principles-and-mvp.md).

**Model drift** — Degradation of a deployed model as **input distribution** or the world shifts from the launch baseline; requires **continuous** monitoring with alert thresholds and a retrain/rollback path — not only change-triggered eval. Distinct from **config/GitOps drift**. See [ai-adoption-controls.md](patterns/ai-adoption-controls.md) §3.

**mTLS** — *Mutual TLS*: both parties present certificates; common for **service-to-service** identity. See [api-boundaries-and-security.md](principles/api-boundaries-and-security.md), [zero-trust-and-workload-identity.md](principles/zero-trust-and-workload-identity.md).

**Mutation testing** — Changes code under test to see if tests **fail**; surviving mutants imply weak assertions. See [testing-strategy.md](principles/testing-strategy.md).

---

## N

**NIST AI 600-1** — *AI Risk Management Framework: Generative Artificial Intelligence Profile* (July 2024): GenAI-specific risks and suggested actions aligned with **AI RMF** functions. See [research-internal-ai-knowledge-factory-governance-2026-04.md](evolution/research-internal-ai-knowledge-factory-governance-2026-04.md) §2, [research-ai-ml-ops-landscape-2026-04.md](evolution/research-ai-ml-ops-landscape-2026-04.md) references.

**Nit (non-blocking review)** — Style, naming, or **optional** improvement that **need not** block merge; often lands as a follow-up **issue**. See [code-review-and-change-approval.md](patterns/code-review-and-change-approval.md) §3.

---

## O

**Observability** — Logs, metrics, traces (and **correlation**) sufficient to debug **unknown-unknown** failures. See [observability.md](principles/observability.md).

**Objective-to-outcome chain** — Traceable operating logic from stakeholder need to an owned objective or standing obligation, guardrailed outcome measures, an explicit intervention hypothesis, bounded tasks/run contracts, outputs, observed outcomes, and a continue/change/stop portfolio decision. It prevents task completion or artefact production from being reported as business value. See [ai-native-software-development-lifecycle.md](patterns/ai-native-software-development-lifecycle.md) §2.1.

**ODP** — *Organisation-defined parameter*: a value an organisation must choose where a control baseline deliberately leaves a parameter open. Record the value, scope, owner, source/approval, effective date, and evidence with the exact profile revision; never let an AI or implementation silently invent it. See [Revision-Pinned External Control Profiles](patterns/revision-pinned-control-profiles.md).

**OIDC** — *OpenID Connect*: identity layer on OAuth 2.0; common for **human** and sometimes **workload** flows. See [zero-trust-and-workload-identity.md](principles/zero-trust-and-workload-identity.md).

**OpenTelemetry (OTel)** — Vendor-neutral telemetry APIs and **OTLP** export. See [interoperability-and-standards.md](principles/interoperability-and-standards.md), [tooling/observability.md](tooling/observability.md).

**Outbox** — Pattern to **atomically** persist business state and an **outbound** message descriptor so publishers don’t double-send under crash. Related to idempotency; see [idempotency-across-boundaries.md](patterns/idempotency-across-boundaries.md).

---

## P

**PII** — *Personally identifiable information*; minimise, segregate from analytics, define retention. See [privacy-and-data-governance.md](principles/privacy-and-data-governance.md).

**PITR** — *Point-in-time recovery*: restore a database (or object store with equivalent semantics) to a **specific timestamp** using **continuous** backups / WAL / logs—not only a **snapshot** from last night. See [data-and-migrations.md](principles/data-and-migrations.md).

**Platform as product** — Internal **platform** work treated as a **product**: clear offerings, customer (team) feedback, prioritised **adoption** and **toil** reduction—not only infra tickets. See [platform-as-product-and-golden-paths.md](patterns/platform-as-product-and-golden-paths.md).

**Principle** — In this repo: **durable intent** under `principles/`—**not** tied to one vendor SKU. See [timeless-principles-and-tooling.md](principles/timeless-principles-and-tooling.md).

**Problem Details** — `application/problem+json` (RFC 9457) for **machine-readable** HTTP errors. See [errors-and-failure-modes.md](principles/errors-and-failure-modes.md), [api-boundaries-and-security.md](principles/api-boundaries-and-security.md).

**Promotion** — Moving a **built** artefact through environments **without** rebuilding for each hop (where the platform allows). See [build.md](principles/build.md).

**Publishable unit** — Thing consumers pin versions on (package, image, API product, CLI); gets its **own** SemVer line. See [semantic-versioning.md](principles/semantic-versioning.md).

**Prompt injection** — Crafted input causes the model to **ignore** policy, **exfiltrate** data, or **mis-route** tools; **indirect** injection uses **retrieved** text (RAG) or hidden content. See [rag-retrieval-baseline.md](patterns/rag-retrieval-baseline.md) §3, OWASP [LLM Top 10](https://genai.owasp.org/llm-top-10/).

---

## Q

**Quality gate** — Mandatory checks (fmt, lint, test, contracts, scans) before merge or tag. See [build.md](principles/build.md).

---

## R

**RAG** — *Retrieval-augmented generation*: **retrieve** relevant chunks from a corpus, then **generate** an answer (often via an LLM). Baseline: [rag-retrieval-baseline.md](patterns/rag-retrieval-baseline.md); principle: [ai-ml-systems.md](principles/ai-ml-systems.md); stack layers: [tooling/vector-retrieval-and-embedding-illustration.md](tooling/vector-retrieval-and-embedding-illustration.md). Research: [evolution/research-ai-ml-ops-landscape-2026-04.md](evolution/research-ai-ml-ops-landscape-2026-04.md), [evolution/research-enterprise-rag-agents-indexing-2026-04.md](evolution/research-enterprise-rag-agents-indexing-2026-04.md); internal factory: [evolution/research-internal-ai-knowledge-factory-governance-2026-04.md](evolution/research-internal-ai-knowledge-factory-governance-2026-04.md).

**Reranking** — Second-stage **ordering** of retrieval candidates (often **cross-encoder** or managed API) to improve **precision** before LLM context assembly. See [rag-retrieval-baseline.md](patterns/rag-retrieval-baseline.md) §1.

**Replay** — Re-deliver or re-process messages from history or DLQ **deliberately**; needs **idempotency** and scope. See [message-channel-operations.md](patterns/message-channel-operations.md).

**RFC (design)** — *Request for comments*: **pre-decision** exploration; outcomes land in ADRs when decided. See [documentation-knowledge.md](principles/documentation-knowledge.md).

**RPO / RTO** — *Recovery point* / *time* **objectives**: how much data loss and downtime are acceptable in DR. See [data-and-migrations.md](principles/data-and-migrations.md).

**RRF** — *Reciprocal rank fusion*: merge **ranked** lists (e.g. lexical + dense retrieval) using rank positions, often with constant **k = 60**—common default in **hybrid** RAG. See [rag-retrieval-baseline.md](patterns/rag-retrieval-baseline.md) §1.

**Runbook** — Step-by-step **operator** procedure (deploy, rollback, common failures). See [documentation-knowledge.md](principles/documentation-knowledge.md).

---

## S

**Saga** — Multi-step **distributed** workflow with **forward** recovery or **compensating** actions; not one ACID transaction across services. See [state-machines-and-workflows.md](principles/state-machines-and-workflows.md).

**SBOM** — *Software bill of materials*: inventory of components in a build (often SPDX/CycloneDX). See [dependencies-supply-chain.md](principles/dependencies-supply-chain.md).

**SCA** — *Software composition analysis*: dependency + vuln + sometimes **licence** scanning. See [dependencies-supply-chain.md](principles/dependencies-supply-chain.md).

**SDL** — *Secure development lifecycle*: design review, implementation norms, **vulnerability response**. See [secure-development-lifecycle.md](principles/secure-development-lifecycle.md).

**SemVer** — *Semantic versioning* `MAJOR.MINOR.PATCH` per **publishable unit**. See [semantic-versioning.md](principles/semantic-versioning.md).

**Semantic index** — Curated route map from task intent to the doctrine files an agent or reader should ingest. It is navigation, not a replacement for source principles, patterns, tooling pages, checklists, ADRs, or evolution notes. See [SEMANTIC_INDEX.md](SEMANTIC_INDEX.md).

**Separation of duties (SoD)** — Different roles for **authoring**, **approving**, and **operating** high-risk change (including **who runs agents** vs **who merges** to protected branches); **estate** policy detail complements portable collaboration rules. See [research-internal-ai-knowledge-factory-governance-2026-04.md](evolution/research-internal-ai-knowledge-factory-governance-2026-04.md) §1, [collaboration.md](principles/collaboration.md).

**Shadow AI** — Copilots, wrappers, vendor AI features, or low-code automations in production **outside the AI inventory** — spreading faster than documentation, lifecycle control, and auditability. Closed with a **cheap sanctioned path** (no-blame registration + approved-tools list), not punitive detection. See [ai-adoption-controls.md](patterns/ai-adoption-controls.md) §1.

**Service catalog** — **Index of systems** the org runs: identity, **ownership**, interfaces (APIs/events), runtime, dependencies, ops links (SLOs, runbooks)—**tool-agnostic**; may be a portal, Git index, or dedicated product. See [platform-as-product-and-golden-paths.md](patterns/platform-as-product-and-golden-paths.md).

**Shift left** — Move security, quality, and validation **earlier** in the lifecycle (design, CI), not only pre-release. See [ENGINEERING.md](../ENGINEERING.md) §5.

**SLA** — *Service level **agreement***: **contractual** promise to a customer (often stricter or broader than internal SLOs).

**SLI** — *Service level **indicator***: measured metric backing an SLO (e.g. successful requests ÷ total).

**SLO** — *Service level **objective***: internal target for reliability/latency derived from user needs; pairs with **error budget**. See [reliability-slo-incidents.md](principles/reliability-slo-incidents.md).

**SLSA** — *Supply-chain levels for software artifacts*: framework for **build integrity** and **provenance**. See [build.md](principles/build.md) §14, [dependencies-supply-chain.md](principles/dependencies-supply-chain.md).

**Software factory (agent-assisted)** — In this repo’s research usage: **scaled** automation of engineering work **with** agents while **git + CI + human merge** stay the **system of record**—not autonomous **direct** production mutation. See [research-internal-ai-knowledge-factory-governance-2026-04.md](evolution/research-internal-ai-knowledge-factory-governance-2026-04.md) §8.

**SP 800-218A** — NIST **SSDF community profile** for **generative AI** and dual-use **foundation model development** (training/integration—not a full substitute for **runtime** ops guidance). See [research-ai-ml-ops-landscape-2026-04.md](evolution/research-ai-ml-ops-landscape-2026-04.md), [privacy-and-data-governance.md](principles/privacy-and-data-governance.md) §5.3.

**SPACE** — Framework for **developer experience** (satisfaction, performance, activity, collaboration, flow)—complements DORA. See [measurement-and-dora.md](principles/measurement-and-dora.md).

**SPIFFE / SPIRE** — *Secure production identity framework for everyone* and common implementation: **workload identities** and SVIDs. See [zero-trust-and-workload-identity.md](principles/zero-trust-and-workload-identity.md).

**SSDF** — NIST *Secure Software Development Framework* (SP 800-218): practices grouped **Prepare, Protect, Produce, Respond**. See [timeless-principles-and-tooling.md](principles/timeless-principles-and-tooling.md) §6.

**STRIDE** — *Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege*—threat-model **prompts**. See [threat-modeling-stride-lite.md](principles/threat-modeling-stride-lite.md).

---

## T

**Telemetry (three pillars)** — **Metrics**, **logs**, **traces**—each answers different questions under failure. See [observability.md](principles/observability.md).

**Threat modeling** — Structured identification of threats at **trust boundaries** (often STRIDE). See [threat-modeling-stride-lite.md](principles/threat-modeling-stride-lite.md).

**Toil** — Manual, repetitive operational work that does not **improve** the system long-term; budget its reduction. See [reliability-slo-incidents.md](principles/reliability-slo-incidents.md).

**Tooling** — In this repo: **illustrative** stacks under `tooling/` and `tooling/estates/`—swappable if **surface contracts** stay stable. See [timeless-principles-and-tooling.md](principles/timeless-principles-and-tooling.md).

**Transition record** — Reconstructable, addressable evidence for a controlled lifecycle step: source/destination, strategy lineage, objective and claims, scope/risk, candidate identity, authority, verification, enactment/rollback, outcome, and any bounded exception. It may be distributed across linked planning, issue, repository, CI/CD, artefact, policy, and observability systems. See [ai-native-software-development-lifecycle.md](patterns/ai-native-software-development-lifecycle.md) §4.

**Trunk-based development** — Integrate frequently to a **single** default branch (`main`); short-lived topic branches. See [collaboration.md](principles/collaboration.md).

---

## V

**Vector store** — Index or database for **embeddings** (similarity search); in multi-tenant RAG, isolation failures are **information disclosure** incidents. See [rag-retrieval-baseline.md](patterns/rag-retrieval-baseline.md) §3, [ai-ml-systems.md](principles/ai-ml-systems.md) §7, [tooling/vector-retrieval-and-embedding-illustration.md](tooling/vector-retrieval-and-embedding-illustration.md).

**VulnOps** — *Vulnerability operations*: **continuous** discovery, triage, remediation, and feedback into engineering backlogs—treated as a **standing** capability (people + automation), not only periodic audits or a security-owned spreadsheet. Industry briefings use the term in an AI-accelerated **offense** context; this library’s research note and [ADR 0010](../docs/adr/0010-record-mythos-era-vulnerability-storm-research-and-doctrine-gaps.md) cite it as **input** until normative doctrine is extended. See [evolution/mythos-era-engineering-principles-research-2026-04-28.md](evolution/mythos-era-engineering-principles-research-2026-04-28.md), [secure-development-lifecycle.md](principles/secure-development-lifecycle.md).

---

## W

**Warm standby** — DR site (or region) where **infrastructure** and often **replicated data** are **ready** for a **short** failover (lower **RTO** than cold; **higher** ongoing cost). See [data-and-migrations.md](principles/data-and-migrations.md) §4.

**Cold standby** — DR capacity **exists** but is **not** continuously running serving traffic—**longer RTO**, **lower** ongoing cost until failover work completes. See [data-and-migrations.md](principles/data-and-migrations.md) §4.

**Webhook** — HTTP **callback** from a provider; verify signatures, bound replay windows, **idempotent** handlers. See [webhook-ingress-security.md](patterns/webhook-ingress-security.md).

**Workload identity** — Runtime identity for **services** (tokens, certs, SPIFFE) distinct from **human** logins. See [zero-trust-and-workload-identity.md](principles/zero-trust-and-workload-identity.md).

---

## Z

**Zero Trust** — No implicit trust from **network location** alone; verify **per request** with least privilege. See [ENGINEERING.md](../ENGINEERING.md) §8, [zero-trust-and-workload-identity.md](principles/zero-trust-and-workload-identity.md).

---

## Maintenance

Add or tighten entries when a term appears in **multiple** principle files without a single definition. Prefer **links** over long prose here.
