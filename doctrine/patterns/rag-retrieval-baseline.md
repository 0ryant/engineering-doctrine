# RAG Retrieval Baseline

**Retrieval-augmented generation (RAG)** pattern: **retrieve** grounded passages, then **generate** an answer. This doc is a **portable baseline** for **retrieval** design, security, and evaluation—**not** model choice, hosting, or legal basis for training data.

**Relates to:** [ai-ml-systems.md](../principles/ai-ml-systems.md) (tier **B**, §§6–7 index lifecycle and ANN), [privacy-and-data-governance.md](../principles/privacy-and-data-governance.md) §5 (PII, DPIA), [api-boundaries-and-security.md](../principles/api-boundaries-and-security.md) (injection, SSRF-class tool use if agents follow), [observability.md](../principles/observability.md), [performance-and-cost.md](../principles/performance-and-cost.md) §3, [testing-strategy.md](../principles/testing-strategy.md), [threat-modeling-stride-lite.md](../principles/threat-modeling-stride-lite.md), [collaboration.md](../principles/collaboration.md) §3 (handoff shape for human ↔ agent PR flow). Pipeline **layers** (illustrative): [../tooling/vector-retrieval-and-embedding-illustration.md](../tooling/vector-retrieval-and-embedding-illustration.md). Landscape research: [../evolution/research-ai-ml-ops-landscape-2026-04.md](../evolution/research-ai-ml-ops-landscape-2026-04.md); enterprise RAG / indexing / agents: [../evolution/research-enterprise-rag-agents-indexing-2026-04.md](../evolution/research-enterprise-rag-agents-indexing-2026-04.md). Internal **factory / councils / agentic** governance framing: [../evolution/research-internal-ai-knowledge-factory-governance-2026-04.md](../evolution/research-internal-ai-knowledge-factory-governance-2026-04.md).

---

## 1. Default Retrieval Stack

1. **Candidate generation (wide recall)** — run **lexical** (e.g. BM25 / inverted index) and **dense** (embedding similarity) **in parallel**; take top-N from each (typical planning range **50–200** per channel—tune to latency budget).
2. **Fusion** — merge rankings with **reciprocal rank fusion (RRF)** (common constant **k = 60**) or a **weighted** blend only when you have **labeled** query–doc pairs to justify weights.
3. **Reranking (precision)** — optional but high leverage: cross-encoder or managed reranker over the fused **top M** (**~100–150**), keep **top K** passages for the LLM (**~8–20**).

**Why:** Dense-only misses exact tokens (SKUs, statutes, error codes); lexical-only misses paraphrases. **Measure** on your traffic—**misfused** hybrid can underperform a good dense-only baseline.

---

## 2. Chunking And Index Hygiene

- Chunks **heading-aware**; typical doc chunks **~300–800 tokens** (domain-dependent); keep **tables, code blocks, and structured fields** as first-class chunks where layout matters.
- **Field boosts** for lexical indexes (title > headings > body) when the platform supports them.
- **Corpus versioning** — record **snapshot id** or content hash with the index so **eval** and **incident replay** are reproducible; align with [data-and-migrations.md](../principles/data-and-migrations.md) for pipeline idempotency.

---

## 3. Security And Privacy

- **Tenant isolation** on the **vector store and search index** — same rigor as row-level security for a multi-tenant DB; cross-tenant retrieval is an **information disclosure** incident.
- **Indirect prompt injection** — untrusted documents are **untrusted input**; retrieved text can instruct the model to exfiltrate or misbehave. Mitigations: **instruction** hardening, **output** policy, **tool** least privilege, **human** review for high-risk actions—not “RAG alone.”
- **PII** in the corpus or in **logged** queries/responses: [privacy-and-data-governance.md](../principles/privacy-and-data-governance.md) §5; minimise what is embedded and what is logged.
- **Caching** retrieval results: treat cache keys and TTL like any **sensitive** cache—stale or cross-user leakage is a **Tampering / Information disclosure** risk (see [api-boundaries-and-security.md](../principles/api-boundaries-and-security.md) cache discussion where applicable).

---

## 4. Evaluation (Non-Negotiable For Production RAG)

- Maintain a **golden set** (queries + expected relevant chunk ids or rubric-scored answers); run **regression** on **retrieval** when changing chunking, embeddings, fusion, or corpus.
- Track at least: **hit rate @K** (any relevant chunk in top-K), **MRR** or **nDCG@K** where feasible, and **groundedness** checks on answers (human or automated) when answers are user-visible.
- **OWASP LLM** framing for RAG includes **vector/embedding weaknesses** and **poisoning** — include **adversarial** and **dirty** documents in **red-team** scenarios where the threat model warrants it. Reference: [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) (GenAI project).

---

## 5. Observability And Cost

- Trace **retrieval**: query id, corpus version, **ids** of chunks sent to the LLM (not necessarily full text in logs), fusion/rerank scores if useful for debug.
- Meter **tokens** and **third-party** search/embed/rerank API calls — [performance-and-cost.md](../principles/performance-and-cost.md) §3; alert on **spend** and **latency** anomalies like any high-cost dependency.

---

## 6. When Not To Use Full RAG

- **Pure lookup** (stable IDs, structured filters) — **search API + UI** or deterministic query may be simpler and easier to test.
- **Tiny corpus** where a single well-tuned index suffices — still **eval**, but skip dual-index complexity until data proves it.

---

## References

- OWASP — **Top 10 for LLM Applications** (GenAI): https://genai.owasp.org/llm-top-10/  
- OWASP — project home: https://owasp.org/www-project-top-10-for-large-language-model-applications  
- NIST — **SP 800-218A** (secure practices for GenAI / foundation model **development**; use with SP 800-218): https://csrc.nist.gov/pubs/sp/800/218/a/final  
