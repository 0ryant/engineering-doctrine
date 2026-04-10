# Illustrative AI-Assisted Development Tooling

**Illustrative only** — names **categories** teams commonly plug in under [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md). **Your estate** picks specific products and records them in **ADRs** or `tooling/estates/`—not here.

---

## 1. Categories (Swap Freely)

| Category | Typical role | Principle touchpoints |
| --- | --- | --- |
| **IDE / editor assistance** | Inline completion, refactor suggestions in the **local** workspace | [configuration-and-secrets.md](../principles/configuration-and-secrets.md) — **no** secrets in files the assistant reads; [single-source-of-truth.md](../principles/single-source-of-truth.md) — generated code policy |
| **Managed model API** | Hosted **LLM** inference with enterprise terms | [performance-and-cost.md](../principles/performance-and-cost.md) §3; [api-boundaries-and-security.md](../principles/api-boundaries-and-security.md) |
| **Internal corpus / RAG** | Embeddings + **search** over docs, ADRs, tickets (exports) | [rag-retrieval-baseline.md](../patterns/rag-retrieval-baseline.md); [vector-retrieval-and-embedding-illustration.md](vector-retrieval-and-embedding-illustration.md) (pipeline **layers**); [privacy-and-data-governance.md](../principles/privacy-and-data-governance.md) §5 |
| **Tool protocol hosts** | MCP-style **clients** connecting to approved **servers** (data + tools) | [ai-ml-systems.md](../principles/ai-ml-systems.md) §7; [api-boundaries-and-security.md](../principles/api-boundaries-and-security.md); [dependencies-supply-chain.md](../principles/dependencies-supply-chain.md) |
| **CI / PR bots** | Summaries, **risk** hints, suggested reviewers—**non-binding** | [build.md](../principles/build.md); [collaboration.md](../principles/collaboration.md) — **required checks** unchanged |
| **Agent runner** | Scheduled or triggered **multi-step** jobs (open PR, run tests) | [ai-ml-systems.md](../principles/ai-ml-systems.md) §§2–4; [zero-trust-and-workload-identity.md](../principles/zero-trust-and-workload-identity.md); [audit-logging.md](../principles/audit-logging.md) |
| **Gateway / policy layer** | Central **routing**, quotas, **PII** redaction, logging for model calls | [api-boundaries-and-security.md](../principles/api-boundaries-and-security.md); [observability.md](../principles/observability.md) |

---

## 2. Filename And Wiring Conventions (Examples)

Estate-specific repos often add:

- `.github/workflows/` or `.gitlab-ci.yml` jobs that **only** run on `pull_request` and **comment**—never **merge**.
- A **small** `docs/ai-usage.md` or ADR stating **tier** (A–D), **allowed** corpora, and **retention** for logs.

This repository’s **portable** expectation: those conventions **exist** where AI touches **merge path** or **production**—exact paths are **template** choices.

---

## 3. Estate Supplements

Hyperscaler **landing zones** and **AI gateways** (for example Azure AI Landing Zone patterns) belong in **`tooling/estates/`** when you document a **specific** org—see [../evolution/research-ai-ml-ops-landscape-2026-04.md](../evolution/research-ai-ml-ops-landscape-2026-04.md) §2.

---

## References

- Portable rules: [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md)  
- RAG baseline: [../patterns/rag-retrieval-baseline.md](../patterns/rag-retrieval-baseline.md)  
- Vector / embedding stack layers: [vector-retrieval-and-embedding-illustration.md](vector-retrieval-and-embedding-illustration.md)  
- Research: [../evolution/research-enterprise-rag-agents-indexing-2026-04.md](../evolution/research-enterprise-rag-agents-indexing-2026-04.md)  
