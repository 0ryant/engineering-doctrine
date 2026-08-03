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
- **Dual-path injection defence (agentic RAG)**: when a RAG pipeline feeds an agent that also has access to **private data** and **write/communication tools** simultaneously — the **lethal trifecta** — instruction hardening alone is insufficient. Apply an architectural defence: the **planning LLM** sees only the user request; a separate **quarantined processor** handles raw external/retrieved content and outputs typed structured values only (no free-text forwarding); a **controller layer** enforces capability policies in deterministic code. This is the mechanism independently described by the Willison Dual LLM pattern (2023) and formalised with taint tracking in the CaMeL paper (Google DeepMind, 2025). Full pattern: [agentic-loop-design.md](agentic-loop-design.md) §9; defence-effectiveness claims are evidenced by **adaptive evaluation**, not static replay — §9.4 there and [testing-strategy.md](../principles/testing-strategy.md) §5.
- **PII** in the corpus or in **logged** queries/responses: [privacy-and-data-governance.md](../principles/privacy-and-data-governance.md) §5; minimise what is embedded and what is logged.
- **Caching** retrieval results: treat cache keys and TTL like any **sensitive** cache—stale or cross-user leakage is a **Tampering / Information disclosure** risk (see [api-boundaries-and-security.md](../principles/api-boundaries-and-security.md) cache discussion where applicable).

---

## 4. Evaluation (Non-Negotiable For Production RAG)

- Maintain a **golden set** (queries + expected relevant chunk ids or rubric-scored answers); run **regression** on **retrieval** when changing chunking, embeddings, fusion, or corpus.
- Track at least: **hit rate @K** (any relevant chunk in top-K), **MRR** or **nDCG@K** where feasible, and **groundedness** checks on answers (human or automated) when answers are user-visible.
- **OWASP LLM** framing for RAG includes **vector/embedding weaknesses** and **poisoning** — include **adversarial** and **dirty** documents in **red-team** scenarios where the threat model warrants it. Reference: [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) (GenAI project).

---

## 5. Observability And Cost

- Trace **retrieval**: query id, corpus version, **ids** of chunks sent to the LLM (not necessarily full text in logs), fusion/rerank scores if useful for debug. The **generation call** itself carries the **per-call minimum signal set** of [../principles/observability.md](../principles/observability.md) §7; the chunk/corpus ids here are that set's **retrieval-linkage** leg — same restraint on content (ids, not full text).
- Meter **tokens** and **third-party** search/embed/rerank API calls — [performance-and-cost.md](../principles/performance-and-cost.md) §3; alert on **spend** and **latency** anomalies like any high-cost dependency.

---

## 6. When Not To Use Full RAG

- **Pure lookup** (stable IDs, structured filters) — **search API + UI** or deterministic query may be simpler and easier to test.
- **Tiny corpus** where a single well-tuned index suffices — still **eval**, but skip dual-index complexity until data proves it.

---

## 7. When Retrieval Is Relational (Graph-Augmented Retrieval / GraphRAG)

The §1 stack retrieves **passages** and answers questions whose evidence sits inside the top-K chunks. Some question classes need **structure** instead:

| Question class | Example | Why passage retrieval struggles |
| --- | --- | --- |
| **Multi-hop** | “Which suppliers behind the delayed release also appear in open incident post-mortems?” | Evidence spans documents connected only by **shared entities**; no single chunk matches the query. Microsoft frames this as answers that require “traversing disparate pieces of information through their shared attributes.” |
| **Corpus-global / sensemaking** | “What are the main themes across this quarter’s customer calls?” | The answer is a **synthesis over the whole corpus** (query-focused summarization), not top-K passages. |
| **Entity-centric** | “Everything we hold on vendor X and its dependencies.” | The **relationships** are the payload; similarity search returns scattered mentions, not the neighbourhood. |

**GraphRAG** (Edge et al., Microsoft Research 2024) is the reference approach: extract an **entity knowledge graph** from the corpus, detect **communities** of related entities and pre-summarize them, then answer **global** questions by map-reducing over community summaries and **local** questions by fanning out from matched entities to neighbours (project query modes: **Global**, **Local**, **DRIFT**, and vector-only **Basic**). On corpora in the ~1M-token range it substantially outperformed vector RAG on **comprehensiveness** and **diversity** of answers to global questions. The survey formalisation (Peng et al. 2024) splits any such pipeline into **graph-based indexing → graph-guided retrieval → graph-enhanced generation** — useful vocabulary when comparing products.

### 7.1 Decision Rule And Cost Ladder

- **Default remains §1.** Lookup and paraphrase workloads — most workloads — are served by hybrid retrieval; a graph adds an **extraction pipeline you must own**. Treat “graph **vs** RAG” framing in vendor content as marketing: production systems that benefit usually run **both** and merge contexts (HybridRAG-style union, evaluated per stage — Sarmah et al. 2024).
- **Adopt a graph on evidence, not on demo:** extend the §4 golden set with multi-hop and corpus-global questions first; reach for a graph only when the §1 stack **measurably fails** that slice.
- **Climb the cost ladder, don’t jump:** (1) metadata filters + hybrid (§1); (2) **lazy** variants — **LazyGraphRAG** builds a lightweight noun-phrase co-occurrence graph at index time and defers LLM work to query time (vendor-measured: indexing cost ≈ vector RAG, ~0.1% of full GraphRAG’s; global-answer quality comparable to GraphRAG global search at a small fraction of its query cost); (3) **full LLM-extracted** graph with pre-built community summaries only where those summaries earn their keep beyond QA (repeated global queries, shareable reports). **LLM extraction is the expensive step and re-runs as the corpus changes** — budget it like any high-cost pipeline (§5).
- Out-of-box extraction prompts underperform on domain corpora — Microsoft’s own guidance is that default use “may not yield the best possible results”; plan **prompt/schema tuning** for your entity and relation types.

### 7.2 Security And Tenancy Additions

- **Text-to-query generation** (Cypher / SPARQL / Gremlin from natural language) is an **injection surface of SQL class**: execute generated queries under **read-only, least-privilege** credentials; prefer allowlisted query shapes or parameterised templates over free generation; expose no more schema than the retriever needs. Same boundary discipline as [api-boundaries-and-security.md](../principles/api-boundaries-and-security.md); LLM-side framing per OWASP LLM Top 10 (§3 references).
- **Tenancy is harder on a graph:** one cross-tenant **edge** bridges two tenants’ subgraphs, and traversal then **amplifies** the leak. §3 isolation applies at **node, edge, and traversal** level — filter at query time *and* keep tenant corpora in separate graphs where materiality warrants.
- **Extraction poisoning:** adversarial or dirty documents (§4 red-team) now mint **false entities and edges** that persist in the index and steer future answers; include extraction-level scenarios in red-team coverage, not just passage-level injection.

### 7.3 Evaluation And Freshness Additions

- **Sample extraction quality** (entity/relation precision on a labeled slice) — extraction quality dominates graph answer quality the way chunking (§2) dominates passage retrieval.
- **Freshness:** corpus change ⇒ incremental extraction or rebuild; treat graph rebuilds and **extraction-prompt changes** as index **migrations** with golden-set regression, exactly like embedding-model changes ([ai-ml-systems.md](../principles/ai-ml-systems.md) §7, §2 corpus versioning here).
- Keep §4 metrics for the passage channel; add **multi-hop answer correctness** and (for global questions) rubric-scored **comprehensiveness/groundedness** — global answers rarely have single gold chunks to score against.

---

## References

- OWASP — **Top 10 for LLM Applications** (GenAI): https://genai.owasp.org/llm-top-10/  
- OWASP — project home: https://owasp.org/www-project-top-10-for-large-language-model-applications  
- NIST — **SP 800-218A** (secure practices for GenAI / foundation model **development**; use with SP 800-218): https://csrc.nist.gov/pubs/sp/800/218/a/final  
- Willison — **Dual LLM Pattern** (architectural injection defence, Apr 2023): https://simonwillison.net/2023/Apr/25/dual-llm-pattern/  
- Willison — **The Lethal Trifecta** (external content + private data + write tools, 2025): https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/  
- CaMeL — Debenedetti et al. (taint tracking, Google DeepMind / ETH Zurich, 2025): https://arxiv.org/abs/2503.18813  
- Edge et al. — **From Local to Global: A Graph RAG Approach to Query-Focused Summarization** (Microsoft Research, 2024): https://arxiv.org/abs/2404.16130  
- Microsoft — **GraphRAG** project docs (Global / Local / DRIFT / Basic search): https://microsoft.github.io/graphrag/  
- Microsoft Research — **LazyGraphRAG** (deferred-extraction variant; vendor-measured cost claims, Nov 2024): https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/  
- Peng et al. — **Graph Retrieval-Augmented Generation: A Survey** (2024): https://arxiv.org/abs/2408.08921  
- Sarmah et al. — **HybridRAG** (vector + knowledge-graph union, finance domain, 2024): https://arxiv.org/abs/2408.04948  
