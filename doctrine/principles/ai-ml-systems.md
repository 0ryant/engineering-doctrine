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
| **D** | **Agentic** flows — tools, multi-step side effects | **Least privilege** per tool, bounded loops/cost, **human** gates for irreversible actions; **workload identity** for runners ([zero-trust-and-workload-identity.md](zero-trust-and-workload-identity.md)); SSRF and outbound trust per [api-boundaries-and-security.md](api-boundaries-and-security.md) §§8–9; standard **tool protocols** (e.g. MCP) per §7. |

Teams **declare** the **highest** tier they operate in per system and **upgrade** controls when capability crosses a boundary.

### 2.1 Materiality Is A Second Axis

Capability tiers say what a system **can do**; **materiality** says what its failure **costs** (person-affected decisions, money movement, regulatory reporting, irreversibility, blast radius). A Tier-**A** API call drafting customer-facing decisions is **high-materiality**; a Tier-**D** agent refactoring test fixtures is not. Declare **both** per system in the **AI inventory**; the **adoption controls** (ownership/challenge, harm-surface testing, provider continuity, uplift — [../patterns/ai-adoption-controls.md](../patterns/ai-adoption-controls.md) §§2–5) scale with the **max** of the two, while the tier table above remains capability-keyed.

---

## 3. Organisational Governance (Map Before Scale)

- Use a **governance-first** order: **policies**, **roles**, **allowed data classes**, and **third-party AI** subprocessors **before** wide indexing or agent **automation**. Public scaffolds: **NIST AI RMF** (**Govern, Map, Measure, Manage**) and, for **model development** practices, **NIST SSDF** + **SP 800-218A**—see [evolution/research-internal-ai-knowledge-factory-governance-2026-04.md](../evolution/research-internal-ai-knowledge-factory-governance-2026-04.md) and [evolution/research-ai-ml-ops-landscape-2026-04.md](../evolution/research-ai-ml-ops-landscape-2026-04.md).
- **Separation of duties** (who authors change, who runs agents, who approves merge to protected branches) is **estate** policy; portable collaboration rules remain in [collaboration.md](collaboration.md).
- **Inventory before scale** — every AI system in production or on real data (including **embedded**, **vendor**, and **copilot**-class AI) appears in an **owned, materiality-tiered inventory** reconciled on material change (NIST AI RMF **GOVERN 1.6**); the **enforcement bar** is that a production system **above minimal materiality** missing from it is a **finding**. Ungoverned "shadow" AI is closed with a cheap **sanctioned path**, not punitive detection. Register shape and cadence: [../patterns/ai-adoption-controls.md](../patterns/ai-adoption-controls.md) §1.
- **Ownership with independent challenge** — a named **first-line owner** is accountable for purpose, data inputs, acceptable use, and human-oversight mode; **high-materiality** systems get pre-launch review by someone with the **incentives, competence, and influence** to force change (*effective challenge*, SR 11-7 vocabulary): [../patterns/ai-adoption-controls.md](../patterns/ai-adoption-controls.md) §2.
- **Capability uplift is role-based** — approved/prohibited-use boundaries are published, and literacy scales with role (builders ≠ reviewers ≠ everyday users; EU AI Act **Art 4** posture): [../patterns/ai-adoption-controls.md](../patterns/ai-adoption-controls.md) §5.

**Why:** Tool rollout without **Map/Measure** defaults to **incident-driven** governance.

---

## 4. Engineering Change Path (Agents And Humans)

- **Agents propose** — branches, diffs, PRs, or **draft** docs—not **silent** mutation of production or **protected** branches without the **same** gates as human contributors.
- **CI proves** — **required checks** for that repo **still apply**; non-deterministic outputs do **not** waive **contracts**, **lint**, or **security** gates ([build.md](build.md), [testing-strategy.md](testing-strategy.md)).
- **Humans approve** — **high-risk** areas (auth, tenancy, crypto, schema, **person**-affected automation) keep **explicit** review per [collaboration.md](collaboration.md) and [secure-development-lifecycle.md](secure-development-lifecycle.md) §1.
- **Security-critical paths are proposal-only until human sign-off** — changes touching **authn/authz**, **secrets or crypto**, **tenant isolation**, **CI/deploy privileges**, or **internet-exposed** trust boundaries remain **human-gated** for merge approval even when an LLM or agent authored the diff; green CI alone does not substitute where tests could be **weak** or **misaligned** with abuse cases. Disclosure and evidence expectations: [code-review-and-change-approval.md](../patterns/code-review-and-change-approval.md) §6.
- **Live person-affected decisions keep a human fallback** — the gates above protect the **repo**; systems that **decide about people** at runtime also need: a designed **fallback path** when the system is unavailable, low-confidence, or contested (degrade to human handling, not silent failure); overseer authority and affordance to **disregard, override, or halt** output (EU AI Act **Art 14** vocabulary, incl. **automation bias** awareness); a **contest/complaint path** reaching a human who can reverse the decision; and per-decision logging sufficient to reconstruct and explain it ([audit-logging.md](audit-logging.md)). Detail: [../patterns/ai-adoption-controls.md](../patterns/ai-adoption-controls.md) §2.

**Why:** Preserves **trunk**, **small PRs**, and **bisectability** while scaling throughput.

---

## 5. Security, Privacy, And Audit

- Treat **OWASP Top 10 for LLM Applications** as the **application-layer** GenAI checklist alongside **OWASP API** controls: https://genai.owasp.org/llm-top-10/
- **Personal data** in prompts, retrieval, or training: [privacy-and-data-governance.md](privacy-and-data-governance.md) §5; **DPIA** and **vendor** flows when required.
- **Automation** that affects users or operators **logs** with **correlation ids**, **actor** (human vs service), and **model/tool** version where material ([audit-logging.md](audit-logging.md)).

---

## 6. Evaluation And Operations

- **Production** RAG or user-visible model outputs have **regression** signals (retrieval quality, safety checks, or human rubric)—not **ship once** without measurement ([rag-retrieval-baseline.md](../patterns/rag-retrieval-baseline.md) §4, [testing-strategy.md](testing-strategy.md)).
- **Test the harm surface, not just retrieval** — person-affected outputs add **fairness/bias** evaluation (pre-launch and on retrain/model swap); all production models add **continuous drift** monitoring against the launch baseline (not only change-triggered eval); GenAI with policy constraints adds **jailbreak/guardrail-bypass** red-teaming; GenAI feeding downstream systems adds **output validation** (OWASP LLM05) and **data-leakage probing** (LLM02/LLM07). Test matrix and evidence expectations: [../patterns/ai-adoption-controls.md](../patterns/ai-adoption-controls.md) §3.
- **Reliability** treats external **model APIs** like any **critical dependency**—timeouts, fallbacks, and **error budgets** ([reliability-slo-incidents.md](reliability-slo-incidents.md) §7, [performance-and-cost.md](performance-and-cost.md)); **game days** may include provider impairment ([../patterns/chaos-engineering-and-game-days.md](../patterns/chaos-engineering-and-game-days.md)). **Provider continuity** — due diligence, concentration risk, tested **exit/substitution** plans — per [../patterns/ai-adoption-controls.md](../patterns/ai-adoption-controls.md) §4.

---

## 7. Retrieval, Indexes, Agent Context, And Tool Surfaces

- **Ingestion** (parse, chunk, embed, write indexes) and **online query** (retrieve, rerank, build context) are **separate** operational paths with explicit **freshness** SLAs and **rollback**; align idempotent rebuilds with [data-and-migrations.md](data-and-migrations.md) where indexes are **derived** data.
- **Embedding model**, **dimensions**, or **distance metric** change ⇒ treat as a **migration**: re-embed (or backfill), rebuild or reconfigure **ANN** indexes, and **regress** retrieval on a **golden** set before promotion ([rag-retrieval-baseline.md](../patterns/rag-retrieval-baseline.md) §4).
- **Approximate nearest neighbour (ANN)** indexes trade **recall**, **latency**, and **memory**—**measure** Recall@K (or equivalent) and tail latency in **production**; vendor defaults are not a substitute for **estate** tuning ([observability.md](observability.md), [performance-and-cost.md](performance-and-cost.md)).
- Apply **tenant**, **sensitivity**, and **document-type** **metadata filters** **before** or **with** vector search where possible—reduces **cross-tenant** retrieval risk and cost ([rag-retrieval-baseline.md](../patterns/rag-retrieval-baseline.md) §3).
- **Short-term agent context** (conversation buffer, scratch tool output) is **ephemeral**; it does **not** replace **governed** corpora or **versioned** policy in **git** (§1). Persisting agent memory to a store **reopens** Tier **B** retrieval rules (ACL, eval, injection).
- **Tool protocols** (for example **MCP**-style client/server tool access) are **integration** surfaces: **authenticate** servers and callers, **authorise** per tool, **rate-limit**, **audit** invocations, and track **dependencies** of server implementations ([api-boundaries-and-security.md](api-boundaries-and-security.md) §§8–9, [dependencies-supply-chain.md](dependencies-supply-chain.md), [audit-logging.md](audit-logging.md)). **Estate** documents allowed servers and data scopes.

**Why:** First-class enterprise RAG fails in **operations** (stale index, wrong embedding version) and **agents** fail on **unbounded** tool trust—not only in prompt wording.

---

## 8. Anti-Patterns

- **Undifferentiated** “index everything” corpora without **ACLs** or **classification**.
- **Fine-tuning** on **production** **PII** or **unreviewed** third-party text without **legal** clearance.
- **Autopilot merge** to `main` **skipping** required checks.
- **Long-lived** **secrets** in **prompts** or **logged** context.
- **Multi-agent “council”** outcomes treated as **approval** without **CI** or **human** sign-off for high-risk change.
- **Shadow AI** — copilots, wrappers, or vendor AI features in production **outside the inventory** ([../patterns/ai-adoption-controls.md](../patterns/ai-adoption-controls.md) §1); or registration made so heavy that teams route around it.
- **Fairness and drift as launch-only checks** — person-affected outputs never re-evaluated after retrain or silent vendor model upgrade.

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

- Adoption operating model (inventory, challenge, harm-surface tests, provider continuity, uplift): [../patterns/ai-adoption-controls.md](../patterns/ai-adoption-controls.md) + [../checklists/ai-adoption-readiness.md](../checklists/ai-adoption-readiness.md)
- Adoption-control gap research (2026-07): [../evolution/research-ai-adoption-control-gaps-2026-07.md](../evolution/research-ai-adoption-control-gaps-2026-07.md)
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
- Federal Reserve **SR 11-7** — Model Risk Management (effective challenge): https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm  
- PRA **SS1/23** — Model risk management principles for banks: https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss  
- **EU AI Act** — Art 4 literacy / Art 14 human oversight / Art 15 lifecycle accuracy: https://artificialintelligenceact.eu/  
- **Model Context Protocol** — documentation hub: https://modelcontextprotocol.io  
- Anthropic — **Introducing MCP**: https://www.anthropic.com/research/model-context-protocol  
