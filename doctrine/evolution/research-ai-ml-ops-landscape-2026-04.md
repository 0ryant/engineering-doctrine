# Research: AI / ML Ops, Governance, RAG, And Azure AI Landing Zone (April 2026)

**Purpose:** Capture **current** public guidance on generative-AI delivery, **map** it to this repo’s **principles / patterns / tooling / estates** split, and record **where a future `principles/ai-ml-systems.md` (or Azure estate supplement)** would attach—without turning portable principles into a cloud catalogue.

**Not:** Product recommendations, benchmark winners, or a substitute for legal review.

**See also:** internal **knowledge layer**, **handoffs**, **councils**, **agentic workflows**, and **governance-first** factory framing (still **no build specs**) → [research-internal-ai-knowledge-factory-governance-2026-04.md](research-internal-ai-knowledge-factory-governance-2026-04.md). **Enterprise RAG**, **indexing**, **MCP** → [research-enterprise-rag-agents-indexing-2026-04.md](research-enterprise-rag-agents-indexing-2026-04.md).

---

## 1. Executive Summary

- **Governance** for AI systems is converging on **layered** controls: classic app/API security **plus** GenAI-specific threat models (**OWASP Top 10 for LLM Applications**, now under the broader **OWASP GenAI Security Project**), **NIST SSDF** with the **SP 800-218A** community profile for **model development** lifecycle tasks, and cloud **landing zones** + **policy-as-code** where you run workloads (e.g. **Azure AI Landing Zone**).
- **RAG** is the default pattern for grounding; **production** retrieval usually means **hybrid search** (lexical + dense), **fusion** (often **RRF**), **reranking**, and **continuous eval**—not “embeddings only.”
- **Minimal AI ops** scales with **risk**: call a managed API with quotas and logging → add RAG + eval gates → only then custom training/fine-tuning with data lineage and supply-chain rigor.
- **NIST SP 800-218A** explicitly focuses on **AI model development** (data through integration); it does **not** replace **deployment/operations** guidance—those stay in your existing **reliability**, **observability**, **performance/cost**, and **API security** principles.

---

## 2. Azure “AILZ” / AI Landing Zone (What It Is)

**Names in the wild:** “Azure AI Landing Zone,” “AI Landing Zones,” “AI ALZ” (blog shorthand).

**What Microsoft publishes:**

- **Open reference implementation** (Bicep, Terraform, Portal) for secure, scalable **AI apps and agents** on Azure, aligned with **Cloud Adoption Framework** AI scenario and **Azure Well-Architected** AI workload guidance. Two composable tracks: **Foundry**-oriented landing zone and **API Management as AI Gateway**—deploy together or separately.
- **Status:** Project documentation states the offering is **in preview** and may use **preview** services given the pace of AI change—treat as **living** reference, not frozen “certified architecture.”
- **Governance angle:** Community content describes **Azure Policy**, initiatives, and **policy-as-code** (e.g. **EPAC**) as the **governance backbone** for consistent guardrails across subscriptions.

**Primary sources (verify before citing in contracts):**

- [Azure AI Landing Zones — documentation site](https://azure.github.io/AI-Landing-Zones/)
- [Azure/AI-Landing-Zones — GitHub](https://github.com/Azure/AI-Landing-Zones)
- [Azure Well-Architected — AI workloads (get started)](https://learn.microsoft.com/en-us/azure/well-architected/ai/get-started)
- [Azure Well-Architected — application design for AI workloads](https://learn.microsoft.com/en-us/azure/well-architected/ai/application-design)
- [AI workload hub (aka.ms)](https://aka.ms/wafAI)
- [Microsoft Tech Community — secure/compliant AI Landing Zone / policy framework](https://techcommunity.microsoft.com/blog/azurearchitectureblog/building-a-secure-and-compliant-azure-ai-landing-zone-policy-framework--best-pra/4457165) (EPAC, policy categories—**editorial**, still useful for vocabulary)

**Doctrine placement:** **`tooling/estates/`** supplement (e.g. extend `azure-container-runtimes.md` or add `azure-ai-landing-zone.md` **only** when an estate adopts Azure AI platform patterns). **Not** a global principle—other clouds and on-prem need parallel **abstract** guidance.

---

## 3. Governance And Secure Development (Non-Azure)

### 3.1 NIST SSDF and SP 800-218A

- **[NIST SP 800-218](https://csrc.nist.gov/publications/detail/sp/800-218/final)** — Secure Software Development Framework (SSDF) v1.1; already mapped in [secure-development-lifecycle.md](../principles/secure-development-lifecycle.md).
- **[NIST SP 800-218A](https://csrc.nist.gov/pubs/sp/800/218/a/final)** (July 2024) — **SSDF Community Profile** for **generative AI** and **dual-use foundation models**: extra practices/tasks for **data sourcing, training, fine-tuning, evaluation, integration** of models. **Audience:** model producers, system producers, acquirers.
- **Important scope note (from NIST):** practices for **deployment and operation** of AI systems are **out of scope** for 800-218A; use **other** NIST and organisational guidance for runtime ops (maps cleanly to this repo’s **reliability**, **observability**, **api-boundaries**, **configuration-and-secrets**, etc.).

### 3.2 OWASP GenAI / LLM Top 10 (2025)

- The **OWASP Top 10 for LLM Applications** is maintained as part of the **[OWASP GenAI Security Project](https://owasp.org/www-project-top-10-for-large-language-model-applications)**; canonical current list: **[genai.owasp.org — LLM Top 10](https://genai.owasp.org/llm-top-10/)** (v2.0 / 2025 framing in community materials).
- **RAG-relevant** items called out in community analysis include **prompt injection** (indirect injection via retrieved content), **vector and embedding weaknesses** (poisoning, cross-tenant leakage, retrieval manipulation), **data/model poisoning**, **misinformation** / overreliance on outputs, **unbounded consumption** / resource exhaustion, and **excessive agency** for agentic flows.
- **Evaluation:** Community guidance references concepts like **context relevance**, **groundedness**, and **answer relevance** (“RAG triad” style evaluation)—i.e. **quality and safety** are measurable, not vibe-only.

**Doctrine placement:**

- **STRIDE + OWASP API** already live in [threat-modeling-stride-lite.md](../principles/threat-modeling-stride-lite.md) and [api-boundaries-and-security.md](../principles/api-boundaries-and-security.md). **Related** already links **LLM / RAG** → [rag-retrieval-baseline.md](../patterns/rag-retrieval-baseline.md) + OWASP LLM Top 10. **Could (future):** add a compact **LLM/GenAI ↔ STRIDE** table (prompt injection → Tampering/Spoofing of instruction channel; vector store → Information disclosure; tool use → Elevation; unbounded tokens → DoS)—optional, not required for baseline coverage.
- **SDL:** extend [secure-development-lifecycle.md](../principles/secure-development-lifecycle.md) with one subsection “**GenAI / model integration**” pointing to SP 800-218A + OWASP GenAI when an ADR adopts AI doctrine.

### 3.3 MITRE ATLAS

- OWASP LLM materials reference **MITRE ATLAS** techniques for ML attack tactics. Useful for **red team / tabletop** vocabulary; same **doctrine slot** as threat modeling and security testing—not a separate pillar.

---

## 4. RAG, Search, And “Latest” Retrieval Practice

### 4.1 When RAG vs search vs both

| Pattern | Good fit | Weak fit |
| --- | --- | --- |
| **Lexical / BM25 / traditional search** | SKUs, statutes, error codes, exact tokens | Paraphrases, “concept” questions without shared vocabulary |
| **Dense vector retrieval** | Semantic similarity, FAQs, paraphrased docs | Rare tokens, IDs, precise legal clause text unless chunking is perfect |
| **Hybrid (lexical + dense)** | Enterprise docs, mixed query styles | Tiny corpora where tuning cost exceeds benefit |
| **RAG (retrieve → generate)** | Open-ended answers with citations to **your** corpus | Strict structured lookup where search UI + API is enough |

**Consensus from 2024–2025 practitioner write-ups:** hybrid retrieval + **fusion** (e.g. **reciprocal rank fusion**) + optional **cross-encoder reranking** is **common** for production RAG; **measure** on **your** queries—bad fusion weights can **underperform** dense-only.

**Illustrative secondary sources (not normative for this repo):**

- [Hybrid search + reranking playbook (OptyxStack)](https://optyxstack.com/rag-reliability/hybrid-search-reranking-playbook)
- [Premai — BM25, SPLADE, vector combined](https://blog.premai.io/hybrid-search-for-rag-bm25-splade-and-vector-search-combined/)
- [Thread Transfer — hybrid search production](https://thread-transfer.com/blog/2025-03-22-hybrid-search-production/)

### 4.2 Operations implications

- **Dual indexes** → **data-and-migrations** discipline, **idempotent** index rebuilds, **version** corpus snapshots for reproducible eval.
- **Caching** (query → retrieved chunks) → intersects [api-boundaries-and-security.md](../principles/api-boundaries-and-security.md) (cache poisoning / stale sensitive data) and [privacy-and-data-governance.md](../principles/privacy-and-data-governance.md) (PII in context).
- **Observability:** trace **retrieval** (which chunks, scores), **model** (latency, tokens), and **downstream** actions (agent tools)—maps to [observability.md](../principles/observability.md) and OpenTelemetry GenAI conventions where adopted.

---

## 5. “Minimal AI Ops” — Tiered Model

Use this to decide **how much** process to borrow before writing `principles/ai-ml-systems.md`.

| Tier | What you ship | Minimum ops / governance |
| --- | --- | --- |
| **A — Managed API only** | No custom index; prompt templates in app | API keys via [configuration-and-secrets.md](../principles/configuration-and-secrets.md); quotas + spend alerts ([performance-and-cost.md](../principles/performance-and-cost.md)); no PII in logs; OWASP API + basic abuse controls |
| **B — RAG** | Chunking, embeddings, vector store, optional hybrid | **Eval** set + regression on retrieval; access control on **vector store** (tenant isolation); threat model for **indirect prompt injection** via documents; DPIA if personal data in corpus ([privacy-and-data-governance.md](../principles/privacy-and-data-governance.md) §5) |
| **C — Fine-tuning / custom training** | Data pipelines, GPUs, model artifacts | **SP 800-218A**-style rigor for data lineage, pipeline integrity, model verification; supply chain for weights ([dependencies-supply-chain.md](../principles/dependencies-supply-chain.md)); stronger release and rollback story |
| **D — Agentic / tool use** | LLM invokes APIs, runs workflows | **Least privilege** per tool, human-in-the-loop for irreversible acts, STRIDE on **new** trust boundaries; aligns with OWASP **excessive agency** and API **SSRF**-class issues |

---

## 6. Platforms (High-Level, Estate-Agnostic)

**Portable doctrine** should name **categories**, not pick winners:

- **Managed model APIs** (hosted LLM inference with enterprise terms)
- **Model + agent hosting** (orchestration, guardrails, tracing hooks)
- **Vector / search** (managed search + vector, or self-managed)
- **Gateways** (policy, routing, rate limits, logging, content safety)—analogous to “AI gateway” in Azure WAF application-design guidance
- **Training / ML platforms** (notebooks, pipelines, experiment tracking)—only when Tier C applies

**Hyperscaler families (for navigation only):**

- **Azure:** AI Foundry / OpenAI Service patterns, **APIM** as gateway—see §2 and [WAF AI application design](https://learn.microsoft.com/en-us/azure/well-architected/ai/application-design).
- **AWS / GCP:** Equivalent patterns exist (managed foundation models, private connectivity, KMS-style encryption, VPC/service perimeter); map in **`tooling/estates/`** when those stubs are filled—**not** in `principles/`.

---

## 7. Where This Research Maps In **This** Doctrine

| Topic | Best home in **this** repo | Notes |
| --- | --- | --- |
| Azure AI Landing Zone, Foundry, APIM AI gateway | `tooling/estates/azure-*.md` (new or extend) | Preview/reference IaC; pair with CAF + WAF links |
| SSDF / SP 800-218A | [secure-development-lifecycle.md](../principles/secure-development-lifecycle.md); [privacy §5.3](../principles/privacy-and-data-governance.md) already cites 218A | Add GenAI subsection when adopted |
| OWASP LLM / GenAI | [threat-modeling-stride-lite.md](../principles/threat-modeling-stride-lite.md); [api-boundaries-and-security.md](../principles/api-boundaries-and-security.md) **Related** (LLM/RAG) + [rag-retrieval-baseline.md](../patterns/rag-retrieval-baseline.md) | Complements OWASP **API** Top 10 |
| RAG retrieval, hybrid search, rerank | [`patterns/rag-retrieval-baseline.md`](../patterns/rag-retrieval-baseline.md) | Portable defaults + eval + privacy; estate docs add product-specific indexes |
| Eval / regression / “model decay” | [testing-strategy.md](../principles/testing-strategy.md); [reliability-slo-incidents.md](../principles/reliability-slo-incidents.md) | Non-deterministic SLOs need careful definition |
| Token cost, third-party model spend | [performance-and-cost.md](../principles/performance-and-cost.md) §3 | Already API-cost aware |
| PII in prompts, training data | [privacy-and-data-governance.md](../principles/privacy-and-data-governance.md) §5 | DPIA / minimisation |
| Agent tools, SSRF, excessive privilege | [api-boundaries-and-security.md](../principles/api-boundaries-and-security.md); [zero-trust-and-workload-identity.md](../principles/zero-trust-and-workload-identity.md) | Same as “dangerous API from a new client” |
| Audit trail for AI-assisted decisions | [audit-logging.md](../principles/audit-logging.md) | Model version + prompt hash + retrieval IDs |
| Chaos / resilience for model dependencies | [chaos-engineering-and-game-days.md](../patterns/chaos-engineering-and-game-days.md); [reliability-slo-incidents.md](../principles/reliability-slo-incidents.md) | Degrade gracefully when model API impaired |
| SBOM / model provenance | [dependencies-supply-chain.md](../principles/dependencies-supply-chain.md) | Models as **dependencies** |

---

## 8. Gaps This Research Does **Not** Close

- **Legal** basis, **copyright**, **licensing** of training data and model outputs—need **legal** sign-off, not engineering doctrine alone.
- **SOC 2 / ISO** control mapping to AI—explicitly out of current doctrine scope per [deep-research-section-gaps.md](deep-research-section-gaps.md) §8 **Won’t**.
- **Vendor-specific** “best GPU / best model” comparisons—expire quarterly; keep in estate ADRs.

---

## 9. Suggested Next Repo Actions (ADR-Gated)

1. **`principles/ai-ml-systems.md`** — **done** — tiers A–D, governance, merge path, pointers to OWASP LLM / NIST; illustrative tooling: [`tooling/ai-assisted-development.md`](../tooling/ai-assisted-development.md).
2. **`patterns/rag-retrieval-baseline.md`** — **done** (hybrid + fusion + rerank defaults; eval; privacy + API security pointers).
3. **`tooling/estates/azure-ai-landing-zone.md`** — link AILZ + WAF + EPAC blog; “preview” warning.
4. **Glossary** — expanded in [glossary.md](../glossary.md) (incl. ANN, BM25, chunking, context window, cross-encoder, **GenAIOps**, grounding, HNSW, hybrid search, ingestion pipeline, IVF, lexical search, MCP, reranking—plus prior AI entries).

---

## References (URLs)

| Resource | URL |
| --- | --- |
| Azure AI Landing Zones (docs) | https://azure.github.io/AI-Landing-Zones/ |
| Azure AI Landing Zones (GitHub) | https://github.com/Azure/AI-Landing-Zones |
| Azure WAF — AI get started | https://learn.microsoft.com/en-us/azure/well-architected/ai/get-started |
| Azure WAF — AI application design | https://learn.microsoft.com/en-us/azure/well-architected/ai/application-design |
| Azure WAF — AI hub | https://aka.ms/wafAI |
| NIST SP 800-218 (SSDF) | https://csrc.nist.gov/publications/detail/sp/800-218/final |
| NIST SP 800-218A (GenAI / foundation models profile) | https://csrc.nist.gov/pubs/sp/800/218/a/final |
| NIST AI 600-1 — AI RMF Generative AI Profile (PDF) | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf |
| OWASP GenAI / LLM Top 10 project | https://owasp.org/www-project-top-10-for-large-language-model-applications |
| OWASP LLM Top 10 (GenAI site) | https://genai.owasp.org/llm-top-10/ |

---

*Research captured: 2026-04-06. Revisit yearly or when adding a dedicated AI principle ADR.*
