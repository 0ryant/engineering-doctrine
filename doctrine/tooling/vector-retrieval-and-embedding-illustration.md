# Illustrative Vector, Embedding, And Search Stack

**Illustrative only** — names **layers** a **Tier B/C** RAG system typically implements. **Products** (vector DB, search engine, embedding API, reranker) are **estate** choices recorded in ADRs—see [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) and [../patterns/rag-retrieval-baseline.md](../patterns/rag-retrieval-baseline.md).

---

## 1. Pipeline Layers (Ingestion → Query)

| Layer | Typical responsibility | Notes |
| --- | --- | --- |
| **Connectors** | Read sources (git, wiki, ticket export, object storage) | **ACL** at source flows to index metadata |
| **Parser / normaliser** | HTML/PDF/office → clean text; preserve headings/tables where possible | Bad parsing dominates failed RAG |
| **Chunker** | Split into **retrieval units** (often hundreds of tokens); attach metadata (doc id, section, tenant) | See [glossary.md](../glossary.md) **Chunking** |
| **Embedder** | Batch or stream **embedding** API or local model | **Version** model id with index |
| **Lexical writer** | Inverted index / BM25 fielded index | Optional separate product or same platform |
| **Vector writer** | Upsert vectors + metadata into **ANN** index | **Rebuild** when dims or model change |
| **Orchestrator / API** | Query → hybrid retrieve → fuse → rerank → assemble context | **Tenant** filter **before** wide vector scan when possible |

---

## 2. Operations And Migrations

- **Freshness** — define **SLA** (event-driven vs batch); stale index = wrong answers + compliance risk.
- **Re-embed migration** — new **embedding model** ⇒ new index (or backfill job) + **golden-set** regression ([rag-retrieval-baseline.md](../patterns/rag-retrieval-baseline.md) §4).
- **ANN tuning** — recall@K vs latency; load tests on **production-sized** shards ([performance-and-cost.md](../principles/performance-and-cost.md)).
- **Secrets** — embedding and reranker API keys via [configuration-and-secrets.md](../principles/configuration-and-secrets.md); never in logged prompts.

---

## 3. Agent And Tool Surfaces

- **MCP servers** (or equivalent) exposing search/query tools sit at the **same** trust boundary as internal APIs—[api-boundaries-and-security.md](../principles/api-boundaries-and-security.md), [zero-trust-and-workload-identity.md](../principles/zero-trust-and-workload-identity.md).
- **Short-term** conversation or tool scratchpad ≠ **durable** policy corpus; governed text stays **versioned** per [ai-ml-systems.md](../principles/ai-ml-systems.md) §1.

---

## References

- Research synthesis: [../evolution/research-enterprise-rag-agents-indexing-2026-04.md](../evolution/research-enterprise-rag-agents-indexing-2026-04.md)  
- MCP docs: https://modelcontextprotocol.io  
