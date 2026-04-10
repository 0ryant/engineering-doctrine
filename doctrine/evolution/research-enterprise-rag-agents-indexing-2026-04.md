# Research: Enterprise RAG, Vector Indexing, Search, And Agent Tooling (April 2026)

**Purpose:** Synthesize **public** guidance on **first-class** enterprise knowledge systems (vectors, indexing, hybrid search, RAG, agent connectors) and map **gaps** filled by [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) §7, [../tooling/vector-retrieval-and-embedding-illustration.md](../tooling/vector-retrieval-and-embedding-illustration.md), and [../glossary.md](../glossary.md). **Not** a product bake-off or implementation runbook.

**Companion:** [research-ai-ml-ops-landscape-2026-04.md](research-ai-ml-ops-landscape-2026-04.md), [research-internal-ai-knowledge-factory-governance-2026-04.md](research-internal-ai-knowledge-factory-governance-2026-04.md).

---

## 1. Executive Summary

- **Naive RAG** (single embedding index, no eval) underperforms in enterprise settings; practitioner literature converges on **multi-stage** retrieval: **hybrid** lexical + dense, **metadata/tenant** pre-filters, **widen** candidate retrieval then **rerank** for precision.
- **Vector indexes** (typically **ANN** algorithms such as **HNSW** or **IVF** families) trade **recall**, **latency**, and **memory**; parameters and **rebuild** strategy must **change** as corpus grows—**monitor** Recall@K and tail latency, not only “it worked in POC.”
- **Ingestion** (parse, chunk, embed, index) and **query** paths should be **separately** operable: freshness SLAs, **idempotent** rebuilds, and **versioned** corpus snapshots for **reproducible** eval.
- **Embedding model** or **dimension** changes are **migrations**: full **re-embed** + regression on a **golden** set before promoting.
- **Agents** need **governed** tool boundaries; **Model Context Protocol (MCP)** is a **rising standard** for client/server tool and data access—treat MCP servers as **production** integrations (authz, audit, supply chain), not “helper scripts.”

---

## 2. RAG And Search Stack (Conceptual Layers)

| Layer | Role | Failure mode if skipped |
| --- | --- | --- |
| **Source systems** | CMS, git, tickets, APIs | Stale or illegal content in index |
| **Ingestion** | Parse, normalize, **chunk**, extract metadata | Garbage chunks, lost structure |
| **Lexical index** | BM25-style (or search engine) | Missed SKUs, codes, exact titles |
| **Dense index** | Embeddings + **ANN** | Wrong neighbours at scale, drift |
| **Fusion** | RRF or weighted merge | Misfused worse than single channel |
| **Rerank** | Cross-encoder or managed reranker | Low precision in top-K |
| **LLM** | Grounded generation | Hallucination, injection from context |
| **Observability** | Trace ids, chunk ids, scores | Un-debuggable quality regressions |

Portable pattern detail: [../patterns/rag-retrieval-baseline.md](../patterns/rag-retrieval-baseline.md). Illustrative tooling layers: [../tooling/vector-retrieval-and-embedding-illustration.md](../tooling/vector-retrieval-and-embedding-illustration.md).

---

## 3. Vector Indexing (ANN) — Research Themes

- **HNSW** (hierarchical navigable small world) is widely used for **low-latency** ANN; **tuning** parameters (graph connectivity, construction vs search breadth) affects **recall** as **N** grows. Practitioner guides recommend **measuring** recall@K vs latency rather than defaulting vendor knobs.
- **IVF** (inverted file / clustering) variants often suit **very large** corpora or **memory** pressure; may require **training** on a representative sample and **periodic** retraining when the distribution shifts.
- **Quantization** (e.g. product quantization) reduces memory at some **accuracy** cost—decision belongs in **estate** capacity planning, not portable law.

**Illustrative practitioner overview (not normative):** [Enterprise RAG Architecture: A Practitioner’s Guide (Applied AI)](https://www.applied-ai.com/briefings/enterprise-rag-architecture/).

---

## 4. Agents And MCP

- **MCP** standardises how **hosts** (IDEs, assistants) connect to **servers** that expose **tools** and **resources**; reduces bespoke N×M connectors but introduces **new** trust boundaries (see [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) §7).
- **Ecosystem** documentation: https://modelcontextprotocol.io  
- **Origin / research note:** [Anthropic — Introducing the Model Context Protocol](https://www.anthropic.com/research/model-context-protocol) (Nov 2024). Governance context: protocol has moved toward **foundation-hosted** stewardship (industry reporting describes **Agentic AI Foundation** / Linux Foundation alignment—verify current charter for compliance packs).
- **Security:** treat MCP like any **RPC** surface: authn/z, rate limits, **audit**, dependency risk on server implementations; 2025 public analyses noted **outstanding** security topics—track **vendor** advisories.

---

## 5. Doctrine Mapping — What We Added (April 2026)

| Gap (before) | Close |
| --- | --- |
| No explicit **index/embedding lifecycle** in principles | [ai-ml-systems.md](../principles/ai-ml-systems.md) §7 |
| Tooling lacked **named pipeline layers** | [vector-retrieval-and-embedding-illustration.md](../tooling/vector-retrieval-and-embedding-illustration.md) |
| Glossary thin on **retrieval** vocabulary | [glossary.md](../glossary.md) (ANN, BM25, chunking, HNSW, hybrid search, reranking, MCP, …) |

---

## 6. References (URLs)

| Resource | URL |
| --- | --- |
| MCP documentation hub | https://modelcontextprotocol.io |
| Anthropic — Introducing MCP | https://www.anthropic.com/research/model-context-protocol |
| Anthropic — Code execution with MCP (agent efficiency) | https://www.anthropic.com/engineering/code-execution-with-mcp |
| Enterprise RAG architecture (practitioner guide) | https://www.applied-ai.com/briefings/enterprise-rag-architecture/ |
| OWASP LLM Top 10 | https://genai.owasp.org/llm-top-10/ |
| Portable AI principle | [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) |
| RAG retrieval baseline pattern | [../patterns/rag-retrieval-baseline.md](../patterns/rag-retrieval-baseline.md) |

---

*Research captured: 2026-04-06. Revisit yearly or when promoting a new embedding model fleet-wide.*
