# AI And ML-Assisted Systems (Governance And Delivery)

**First-class** delivery: GenAI, RAG, indexes, and agents get **explicit ownership**, **operational** discipline (freshness, eval, migrations), and the **same** CI, review, and security expectations as the rest of the stack—not a side channel that bypasses gates.

Durable rules when products or **internal engineering** use **generative AI**, **retrieval-augmented** context, **fine-tuned** models, or **agentic** automation. Complements [api-boundaries-and-security.md](api-boundaries-and-security.md), [privacy-and-data-governance.md](privacy-and-data-governance.md) §5, [secure-development-lifecycle.md](secure-development-lifecycle.md), [dependencies-supply-chain.md](dependencies-supply-chain.md), and [performance-and-cost.md](performance-and-cost.md).

**Not in scope here:** model architecture choice, benchmark leaderboards, or **vendor-specific** deployment steps—those belong in **estate** supplements and ADRs. Illustrative tooling: [../tooling/ai-assisted-development.md](../tooling/ai-assisted-development.md), [../tooling/vector-retrieval-and-embedding-illustration.md](../tooling/vector-retrieval-and-embedding-illustration.md).

---

## 1. Truth And System Of Record

- **Versioned repository state** (code, doctrine, contracts, declarative infra, **ADRs**) is **authoritative** for what **ships** and what **policy** is.
- **Model weights**, **retrieval indexes**, and **prompt caches** are **derivatives**—replaceable; they **must not** be the **only** record of obligations or decisions.
- **Chat transcripts** and assistant threads are **not** configuration; outcomes that matter **close** in **tickets**, **ADRs**, or **merged** docs ([documentation-knowledge.md](documentation-knowledge.md)).

**Why:** Auditors and incident reviewers need **git history**, not “the model agreed.”

---

## 2. Risk Tiers (What Extra Discipline Applies)

| Tier | Typical capability | Additional expectations |
| --- | --- | --- |
| **A** | Call a **managed** model API from app code; no custom corpus | Secrets and quotas ([configuration-and-secrets.md](configuration-and-secrets.md), [performance-and-cost.md](performance-and-cost.md) §3); **no** production **PII** in dev logs without clearance; abuse limits per [api-boundaries-and-security.md](api-boundaries-and-security.md). |
| **B** | **RAG** — chunking, embeddings, vector or hybrid search | **Eval** and regression on retrieval; **tenant isolation** on indexes; threat model for **indirect** injection via documents. Baseline: [../patterns/rag-retrieval-baseline.md](../patterns/rag-retrieval-baseline.md). |
| **C** | **Fine-tuning** or **custom training** | Data **lineage**, pipeline **integrity**, model **verification**, supply chain for **artifacts**—align with **NIST SP 800-218A** where the org adopts it ([secure-development-lifecycle.md](secure-development-lifecycle.md)); treat weights like **dependencies** ([dependencies-supply-chain.md](dependencies-supply-chain.md)). |
| **D** | **Agentic** flows — tools, multi-step side effects | **Least privilege** per tool, bounded loops/cost, **human** gates for irreversible actions; **workload identity** for runners ([zero-trust-and-workload-identity.md](zero-trust-and-workload-identity.md)); SSRF and outbound trust per [api-boundaries-and-security.md](api-boundaries-and-security.md) §§8–9; standard **tool protocols** (e.g. MCP) per §7. **Harness design**: prefer deterministic **workflows** before introducing autonomous agents; automate only what you can **verify**; default to a **conservative autonomy slider** and earn greater autonomy from empirical ISC pass-rate data. Loop architecture: [../patterns/agentic-loop-design.md](../patterns/agentic-loop-design.md). |

Teams **declare** the **highest** tier they operate in per system and **upgrade** controls when capability crosses a boundary.

---

## 3. Organisational Governance (Map Before Scale)

- Use a **governance-first** order: **policies**, **roles**, **allowed data classes**, and **third-party AI** subprocessors **before** wide indexing or agent **automation**. Public scaffolds: **NIST AI RMF** (**Govern, Map, Measure, Manage**) and, for **model development** practices, **NIST SSDF** + **SP 800-218A**—see [evolution/research-internal-ai-knowledge-factory-governance-2026-04.md](../evolution/research-internal-ai-knowledge-factory-governance-2026-04.md) and [evolution/research-ai-ml-ops-landscape-2026-04.md](../evolution/research-ai-ml-ops-landscape-2026-04.md).
- **Separation of duties** (who authors change, who runs agents, who approves merge to protected branches) is **estate** policy; portable collaboration rules remain in [collaboration.md](collaboration.md).

**Why:** Tool rollout without **Map/Measure** defaults to **incident-driven** governance.

---

## 4. Engineering Change Path (Agents And Humans)

- **Agents propose** — branches, diffs, PRs, or **draft** docs—not **silent** mutation of production or **protected** branches without the **same** gates as human contributors.
- **CI proves** — **required checks** for that repo **still apply**; non-deterministic outputs do **not** waive **contracts**, **lint**, or **security** gates ([build.md](build.md), [testing-strategy.md](testing-strategy.md)).
- **Humans approve** — **high-risk** areas (auth, tenancy, crypto, schema, **person**-affected automation) keep **explicit** review per [collaboration.md](collaboration.md) and [secure-development-lifecycle.md](secure-development-lifecycle.md) §1.
- **Security-critical paths are proposal-only until human sign-off** — changes touching **authn/authz**, **secrets or crypto**, **tenant isolation**, **CI/deploy privileges**, or **internet-exposed** trust boundaries remain **human-gated** for merge approval even when an LLM or agent authored the diff; green CI alone does not substitute where tests could be **weak** or **misaligned** with abuse cases. Disclosure and evidence expectations: [code-review-and-change-approval.md](../patterns/code-review-and-change-approval.md) §6.
- **Maintain observable plan state** — agents that expose their current plan, active criteria, and intermediate reasoning traces are auditable and debuggable; opaque chains are not. Operators must be able to see what an agent intends to do before it does it, not only after.

**Why:** Preserves **trunk**, **small PRs**, and **bisectability** while scaling throughput.

---

## 5. Security, Privacy, And Audit

- Treat **OWASP Top 10 for LLM Applications** as the **application-layer** GenAI checklist alongside **OWASP API** controls: https://genai.owasp.org/llm-top-10/
- **Personal data** in prompts, retrieval, or training: [privacy-and-data-governance.md](privacy-and-data-governance.md) §5; **DPIA** and **vendor** flows when required.
- **Automation** that affects users or operators **logs** with **correlation ids**, **actor** (human vs service), and **model/tool** version where material ([audit-logging.md](audit-logging.md)).

---

## 6. Evaluation And Operations

- **Production** RAG or user-visible model outputs have **regression** signals (retrieval quality, safety checks, or human rubric)—not **ship once** without measurement ([rag-retrieval-baseline.md](../patterns/rag-retrieval-baseline.md) §4, [testing-strategy.md](testing-strategy.md)).
- **Reliability** treats external **model APIs** like any **critical dependency**—timeouts, fallbacks, and **error budgets** ([reliability-slo-incidents.md](reliability-slo-incidents.md), [performance-and-cost.md](performance-and-cost.md)); **game days** may include provider impairment ([../patterns/chaos-engineering-and-game-days.md](../patterns/chaos-engineering-and-game-days.md)).

---

## 7. Retrieval, Indexes, Agent Context, And Tool Surfaces

- **Ingestion** (parse, chunk, embed, write indexes) and **online query** (retrieve, rerank, build context) are **separate** operational paths with explicit **freshness** SLAs and **rollback**; align idempotent rebuilds with [data-and-migrations.md](data-and-migrations.md) where indexes are **derived** data.
- **Embedding model**, **dimensions**, or **distance metric** change ⇒ treat as a **migration**: re-embed (or backfill), rebuild or reconfigure **ANN** indexes, and **regress** retrieval on a **golden** set before promotion ([rag-retrieval-baseline.md](../patterns/rag-retrieval-baseline.md) §4).
- **Approximate nearest neighbour (ANN)** indexes trade **recall**, **latency**, and **memory**—**measure** Recall@K (or equivalent) and tail latency in **production**; vendor defaults are not a substitute for **estate** tuning ([observability.md](observability.md), [performance-and-cost.md](performance-and-cost.md)).
- Apply **tenant**, **sensitivity**, and **document-type** **metadata filters** **before** or **with** vector search where possible—reduces **cross-tenant** retrieval risk and cost ([rag-retrieval-baseline.md](../patterns/rag-retrieval-baseline.md) §3).
- **Short-term agent context** (conversation buffer, scratch tool output) is **ephemeral**; it does **not** replace **governed** corpora or **versioned** policy in **git** (§1). Persisting agent memory to a store **reopens** Tier **B** retrieval rules (ACL, eval, injection).
- **Context engineering** — deciding what enters the model's context window at each step is a first-class discipline; context failures are now the dominant agent failure mode (not model failures). Four strategies: Write (scratchpad/episodic memory), Select (RAG/procedural), Compress (summarise/trim), Isolate (sub-agents with narrow contexts). See [../patterns/agentic-loop-design.md](../patterns/agentic-loop-design.md) §5.
- **Retrieved and external text is untrusted input**: treat it the way you treat SQL user input. The planning model must never receive raw external content as trusted context. For agentic systems touching external content + private data + write tools simultaneously (the **lethal trifecta**), apply the **dual-path architectural defence** (separate planning LLM from quarantined data processor; enforce capability policy in the controller layer by code, not by another LLM). Full pattern: [../patterns/agentic-loop-design.md](../patterns/agentic-loop-design.md) §9.
- **Tool protocols** (for example **MCP**-style client/server tool access) are **integration** surfaces: **authenticate** servers and callers, **authorise** per tool, **rate-limit**, **audit** invocations, and track **dependencies** of server implementations ([api-boundaries-and-security.md](api-boundaries-and-security.md) §§8–9, [dependencies-supply-chain.md](dependencies-supply-chain.md), [audit-logging.md](audit-logging.md)). **Estate** documents allowed servers and data scopes.

**Why:** First-class enterprise RAG fails in **operations** (stale index, wrong embedding version) and **agents** fail on **unbounded** tool trust—not only in prompt wording.

---

## 8. Anti-Patterns

- **Undifferentiated** “index everything” corpora without **ACLs** or **classification**.
- **Fine-tuning** on **production** **PII** or **unreviewed** third-party text without **legal** clearance.
- **Autopilot merge** to `main` **skipping** required checks.
- **Long-lived** **secrets** in **prompts** or **logged** context.
- **Multi-agent “council”** outcomes treated as **approval** without **CI** or **human** sign-off for high-risk change.
- **Self-certifying output verification**: the agent evaluates its own output with no external signal (test run, structured rubric, human check). Without an external verifier, the loop is open; confident wrong answers are worse than uncertain right ones.
- **Flat injection defence**: relying on a probabilistic LLM-based filter to detect indirect injection instead of architectural separation of untrusted content from the planning model. Probabilistic guards fail at scale; enforcement belongs in deterministic code.
- **Unscoped tool access at startup**: all tools loaded and available regardless of which task phase the agent is in. Increases attack surface and degrades tool selection accuracy. Scope tools to the current task stage; use tool RAG for large libraries.
- **Context window saturation**: raw tool outputs accumulate in context without compression. Model quality degrades steeply at 90%+ context fill. Compress before the limit is reached ([../patterns/agentic-loop-design.md](../patterns/agentic-loop-design.md) §5).
---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Repo remains SoR | Keeps **compliance** and **engineering** aligned; models stay **replaceable**. |
| Tiered obligations | **Proportionality**—not every API call needs a training pipeline. |
| Same merge bar for agents | Avoids a **second-class** quality path that becomes the **default**. |
| §7 retrieval / ANN / tools | **POC** RAG rarely documents **index lifecycle** or **protocol** trust—explicit rules prevent silent drift. |
| External refs (NIST, OWASP) | **Auditable** vocabulary without pasting full control catalogues. |
| Tooling in `tooling/` | **Products** change quarterly; **intent** lives here. |

---

## Related

- Retrieval implementation baseline: [../patterns/rag-retrieval-baseline.md](../patterns/rag-retrieval-baseline.md)
- Internal factory / handoffs / councils (research): [../evolution/research-internal-ai-knowledge-factory-governance-2026-04.md](../evolution/research-internal-ai-knowledge-factory-governance-2026-04.md)
- ML/RAG/Azure landscape (research): [../evolution/research-ai-ml-ops-landscape-2026-04.md](../evolution/research-ai-ml-ops-landscape-2026-04.md)
- Enterprise RAG, indexing, agents (research): [../evolution/research-enterprise-rag-agents-indexing-2026-04.md](../evolution/research-enterprise-rag-agents-indexing-2026-04.md)
- Illustrative tooling categories: [../tooling/ai-assisted-development.md](../tooling/ai-assisted-development.md)
- Vector / embedding pipeline layers: [../tooling/vector-retrieval-and-embedding-illustration.md](../tooling/vector-retrieval-and-embedding-illustration.md)

---

## References

- NIST **AI Risk Management Framework** (AI RMF 1.0): https://www.nist.gov/itl/ai-risk-management-framework  
- NIST **AI 100-1** (AI RMF, PDF): https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf  
- NIST **AI 600-1** — Generative AI Profile (PDF): https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf  
- NIST **SP 800-218** (SSDF): https://csrc.nist.gov/publications/detail/sp/800-218/final  
- NIST **SP 800-218A** (GenAI / foundation models, SSDF profile): https://csrc.nist.gov/pubs/sp/800/218/a/final  
- OWASP **Top 10 for LLM Applications**: https://genai.owasp.org/llm-top-10/  
- **Model Context Protocol** — documentation hub: https://modelcontextprotocol.io  
- Anthropic — **Introducing MCP**: https://www.anthropic.com/research/model-context-protocol  
