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
| **Agent runner** | Scheduled or triggered **multi-step** jobs (open PR, run tests) | [ai-ml-systems.md](../principles/ai-ml-systems.md) §§2–4; [run-contracts.md](../patterns/run-contracts.md); [zero-trust-and-workload-identity.md](../principles/zero-trust-and-workload-identity.md); [audit-logging.md](../principles/audit-logging.md) |
| **Coordination/control plane** | Parent/child runs, scoped task graph, workspace ownership, checkpoints, escalation, cancellation, and safe resume | [run-contracts.md](../patterns/run-contracts.md); [ai-native-software-development-lifecycle.md](../patterns/ai-native-software-development-lifecycle.md) §§4, 7–8 |
| **Isolated preview/test environment** | Executes agent-produced code with ephemeral resources, restricted egress/data, no production credentials, and disposable state | [secure-development-lifecycle.md](../principles/secure-development-lifecycle.md); [zero-trust-and-workload-identity.md](../principles/zero-trust-and-workload-identity.md); [ai-native-software-development-lifecycle.md](../patterns/ai-native-software-development-lifecycle.md) §2 |
| **Gateway / policy layer** | Central **routing**, quotas, **PII** redaction, logging for model calls | [api-boundaries-and-security.md](../principles/api-boundaries-and-security.md); [observability.md](../principles/observability.md) |
| **Objective/transition/evidence view** | Links objective, measure contract and guardrails, intervention hypothesis, task/run, output, PR, CI, artefact, approval, deployment receipt, observed outcome, and portfolio decision | [ai-native-software-development-lifecycle.md](../patterns/ai-native-software-development-lifecycle.md); [measurement-and-dora.md](../principles/measurement-and-dora.md) §2.2; [merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md) |

---

## 2. Filename And Wiring Conventions (Examples)

Estate-specific repos often add:

- `.github/workflows/` or `.gitlab-ci.yml` jobs that **only** run on `pull_request` and **comment**—never **merge**.
- A **small** `docs/ai-usage.md` or ADR stating **tier** (A–D), **allowed** corpora, and **retention** for logs.
- Issue/PR fields for lifecycle state, owner, materiality, claims, affected scope, evidence links, and rollback; CI or release receipts bind those records to a commit and artefact digest.
- Run-contract and verifier-pack validation before an agent runner receives tool authority.
- Parent/child run identifiers, owned worktrees/branches, checkpoint expiry, cancellation, and resume receipts for parallel or long-running work.
- Disposable preview/test environments for executable candidates; action/tool receipts are retained, not private model reasoning.

This repository’s **portable** expectation: those conventions **exist** where AI touches **merge path** or **production**—exact paths are **template** choices.

---

## 3. Estate Supplements

Hyperscaler **landing zones** and **AI gateways** (for example Azure AI Landing Zone patterns) belong in **`tooling/estates/`** when you document a **specific** org—see [../evolution/research-ai-ml-ops-landscape-2026-04.md](../evolution/research-ai-ml-ops-landscape-2026-04.md) §2.

Do not buy or build a central “AI SDLC platform” merely to satisfy the lifecycle vocabulary. First reconstruct one real change across the estate's current issue, repository, CI/CD, artefact, policy, and observability systems; automate only the missing control surfaces the pilot exposes.

---

## References

- Portable rules: [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md)  
- AI-native lifecycle: [../patterns/ai-native-software-development-lifecycle.md](../patterns/ai-native-software-development-lifecycle.md)
- RAG baseline: [../patterns/rag-retrieval-baseline.md](../patterns/rag-retrieval-baseline.md)  
- Vector / embedding stack layers: [vector-retrieval-and-embedding-illustration.md](vector-retrieval-and-embedding-illustration.md)  
- Research: [../evolution/research-enterprise-rag-agents-indexing-2026-04.md](../evolution/research-enterprise-rag-agents-indexing-2026-04.md)  
