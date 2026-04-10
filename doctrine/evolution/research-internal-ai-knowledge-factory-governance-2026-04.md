# Research: Internal AI Knowledge Layer, Handoffs, Councils, Agentic Workflows — Governance-First (April 2026)

**Purpose:** Frame how an organisation might build an **internal AI-assisted development capability**—grounded in **this doctrine**, business rules, architecture patterns, and templates—**without** prescribing **build recipes**, **vendor stacks**, or **operational runbooks** in this repository. This file is **strategy, risk, and doctrine mapping** only.

**Explicit non-goals (per repo change discipline):**

- No **step-by-step** “deploy the factory” or **training pipeline** documentation here.
- No new **tooling/** playbooks that imply a chosen product or cloud path.
- No substitution for **legal**, **procurement**, or **InfoSec** sign-off.

**Companion:** operational ML/RAG/Azure landing-zone landscape → [research-ai-ml-ops-landscape-2026-04.md](research-ai-ml-ops-landscape-2026-04.md). Enterprise RAG / indexing / MCP → [research-enterprise-rag-agents-indexing-2026-04.md](research-enterprise-rag-agents-indexing-2026-04.md). Retrieval baseline pattern → [../patterns/rag-retrieval-baseline.md](../patterns/rag-retrieval-baseline.md).

---

## 1. Capability You Described (Compressed)

A system that can **ingest** a curated corpus—**engineering doctrine**, architecture decisions, security constraints, **approved** templates, and **business rules** (where legally and contractually allowed)—so that **agents** (or assistant UIs) help **author**, **refactor**, **review**, and **automate** change, while **governance** constrains what may run, what may ship, and what may be learned from production.

That vision is **coherent** but **high-risk** if “automate everything” bypasses **accountability**, **separation of duties**, and **truth in repo**. **SoD** detail (who may run agents vs approve production merge vs hold break-glass) is **estate** policy; portable doctrine supplies **protected branch**, **required checks**, and **review** norms ([collaboration.md](../principles/collaboration.md)). This research assumes **git + CI + human merge** remain the **system of record** for shipped software—agents **propose**, pipelines **prove**, people **approve** for high-risk classes (see [build.md](../principles/build.md)).

---

## 2. Governance-First (Enterprise) — Order Of Operations

Before scaling **context** or **agents**, fix **who may do what** and **what evidence** is required. A useful public scaffold is **NIST AI RMF 1.0**: **Govern** (cross-cutting), then **Map**, **Measure**, **Manage** for each system/use case.

| AI RMF function | Enterprise intent (compressed) | Where **this** doctrine already supports it |
| --- | --- | --- |
| **Govern** | Policies, roles, third-party AI use, escalation | [secure-development-lifecycle.md](../principles/secure-development-lifecycle.md), [collaboration.md](../principles/collaboration.md), [documentation-knowledge.md](../principles/documentation-knowledge.md) |
| **Map** | Stakeholders, data flows, failure modes, “what is the AI allowed to touch?” | [threat-modeling-stride-lite.md](../principles/threat-modeling-stride-lite.md), [privacy-and-data-governance.md](../principles/privacy-and-data-governance.md) §5, [api-boundaries-and-security.md](../principles/api-boundaries-and-security.md) |
| **Measure** | Evals, regression, monitoring, incident learning | [testing-strategy.md](../principles/testing-strategy.md), [observability.md](../principles/observability.md), [reliability-slo-incidents.md](../principles/reliability-slo-incidents.md), [rag-retrieval-baseline.md](../patterns/rag-retrieval-baseline.md) §4 |
| **Manage** | Prioritise mitigations, incident response, continuous improvement | [reliability-slo-incidents.md](../principles/reliability-slo-incidents.md), SDL **Respond** in [secure-development-lifecycle.md](../principles/secure-development-lifecycle.md) |

**NIST SSDF** + **SP 800-218A** remain the right **development** anchor when **models** or **training data** are in scope; **AI RMF** broadens **organisational** risk and **runtime** behaviour. Use them **together**, not as duplicates.

**References:** [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework), [AI RMF Playbook](https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook), [NIST AI 100-1 (PDF)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), **Generative AI profile** [NIST AI 600-1 (PDF)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) — [publication landing](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) (July 2024; pair with AI RMF 1.0).

---

## 3. Truth Hierarchy (Non-Negotiable For A “Factory”)

1. **Versioned repository state** (code, doctrine, ADRs, **declarative** infra) is **authoritative** for what **ships**.
2. **Model weights** and **retrieval indexes** are **derivatives**—useful, **replaceable**, and **never** the sole record of policy.
3. **Chat transcripts** are **not** configuration; decisions that matter **close** in **ADRs** or **tickets** with links ([documentation-knowledge.md](../principles/documentation-knowledge.md)).

**Why:** Prevents “the model said we could” as an audit answer; aligns with **Truth in repo** in global doctrine and **async-first** collaboration.

---

## 4. Corpus Design (Abstract Layers)

Think in **layers** with different **sensitivity** and **refresh** cadence—**not** “dump the whole monorepo into one embedding index.”

| Layer | Typical content | Governance notes |
| --- | --- | --- |
| **A — Public / portable doctrine** | This `doctrine/` tree | Safe to share with contractors **if** the repo is already cleared for them |
| **B — Organisational decisions** | ADRs, RFC outcomes, architecture diagrams (as text or structured snippets) | **Access-controlled**; may contain **strategy** |
| **C — Business rules** | Policy excerpts, pricing logic descriptions, eligibility rules | Often **confidential** or **regulated**; legal review for **retention** and **training** use |
| **D — Live operational** | Runbooks, on-call context | **PII** and **credentials** risk; usually **RAG with strict ACLs**, not model **fine-tuning** |
| **E — Build templates / scaffolds** | Internal cookiecutters, module templates | **Supply-chain** artifact—treat like [dependencies-supply-chain.md](../principles/dependencies-supply-chain.md) |

**Separation:** Layer C/D often requires **per-tenant** or **per-role** retrieval (see [rag-retrieval-baseline.md](../patterns/rag-retrieval-baseline.md) §3). **Do not** flatten into one **shared** vector store without **documented** isolation proof.

---

## 5. Handoffs (Human ↔ Agent ↔ Team)

**Handoff** here means a **structured** transfer of **goal**, **constraints**, **verified state**, and **next actions**—the same information you’d put in a good PR description and design note, not a raw chat log.

**Synthesised practice themes** (vendor-agnostic; common guidance and field experience—not a single formal standard):

- **Package** context: *what* changed, *why*, *how to verify*, *what must not change* (invariants)—mirrors [collaboration.md](../principles/collaboration.md) §3 PR discipline.
- **Bound** tokens: prefer **links** to canonical files and **section anchors** over pasting megabytes into prompts.
- **Attach** verification: failing tests, threat-model delta, or checklist name—so the **next** actor (human or agent) cannot “skip” evidence without it being obvious.
- **Escalate** explicitly when touching **auth**, **tenancy**, **crypto**, **schema**—already **security-sensitive** review topics in SDL.

**Doctrine fit:** Handoffs are **documentation and collaboration** first; AI is an **accelerator** on top of norms you already mandate.

---

## 6. Councils And Multi-Agent Deliberation

**Councils** (multiple LLM roles or agents critiquing a proposal) can mimic **design review** diversity—**architecture**, **security**, **reliability** “voices”—before a human approves.

**Strengths (when bounded):**

- Surfaces **contradictions** between requirements and proposed approach.
- Encourages **explicit** trade-off statements (fits **ADRs**).

**Failure modes (documented in practice literature and OWASP GenAI discourse):**

- **Sycophancy / agreement bias** — models reinforce a flawed plan.
- **False confidence** — fluent consensus without **executable** checks.
- **Cost and latency** — council loops multiply **token** spend ([performance-and-cost.md](../principles/performance-and-cost.md)).
- **Data exfiltration** if one stage sends **secrets** or **unredacted** PII to an external API.

**Doctrine fit:** Treat councils as **optional** **pre-review** automation, **subordinate** to **CI**, **checklists**, and **human** merge for high-risk changes. Map to [threat-modeling-stride-lite.md](../principles/threat-modeling-stride-lite.md) and **OWASP LLM** categories (prompt injection, excessive agency). **Do not** encode council choreography as **law** in `principles/` without an **ADR**.

---

## 7. Agentic Workflows (Plan → Act → Verify)

**Agentic** systems **plan**, call **tools** (APIs, CLIs, browsers), and **iterate**. Mapping to existing doctrine:

| Agentic concern | Doctrine anchor |
| --- | --- |
| Tool = outbound HTTP / SSRF | [api-boundaries-and-security.md](../principles/api-boundaries-and-security.md) §§8–9 |
| **Service identity** for automation (OIDC, workload ID) | [zero-trust-and-workload-identity.md](../principles/zero-trust-and-workload-identity.md) — agent runners are **workloads**, not anonymous scripts |
| Unbounded loops / cost | [performance-and-cost.md](../principles/performance-and-cost.md); rate limits |
| Side effects (deploy, data write) | [idempotency-across-boundaries.md](../patterns/idempotency-across-boundaries.md), [state-machines-and-workflows.md](../principles/state-machines-and-workflows.md) |
| Secrets | [configuration-and-secrets.md](../principles/configuration-and-secrets.md) — agents must **not** receive **long-lived** prod secrets in prompts |
| Audit | [audit-logging.md](../principles/audit-logging.md) — **who** triggered **what** automation, with **correlation id** |
| Supply chain of “skills” / plugins | [dependencies-supply-chain.md](../principles/dependencies-supply-chain.md) |

**Safe pattern:** **Plan** and **diff** in branch; **Act** only through **narrow** tools with **allowlisted** scopes; **Verify** via **same** CI as humans ([build.md](../principles/build.md)).

---

## 8. “Software Factory” — A Doctrine-Compatible Interpretation

| Risky interpretation | Compatible interpretation |
| --- | --- |
| Agent **directly** mutates prod | Agent opens **PR**; pipeline **tests**; human or **break-glass** policy **merges** |
| One brain trains on **everything** | **Layered** corpus, **ACL’d** retrieval, **no** secrets in training set |
| Automation **replaces** review | Automation **prepares** review (summaries, test gaps, diff narratives) |
| Doctrine drifts in **chat** | Doctrine changes only via **versioned** edits + **doctrine-change** checklist ([checklists/doctrine-change-checklist.md](../checklists/doctrine-change-checklist.md)) |

This preserves **small PRs**, **one concern**, and **green main** from [collaboration.md](../principles/collaboration.md) while still **scaling** throughput.

---

## 9. Security And Compliance Checklist (Research-Level)

Use with your **InfoSec** team; not exhaustive.

- **OWASP Top 10 for LLM Applications** — especially prompt injection, **indirect** injection via retrieved docs, **excessive agency**, vector/embedding weaknesses: https://genai.owasp.org/llm-top-10/
- **DLP / logging** — prompts and retrieved chunks may contain **PII**; align with [privacy-and-data-governance.md](../principles/privacy-and-data-governance.md).
- **Third-party AI** subprocessors — DPAs, **data residency**, **retention**, **training** opt-out.
- **Red team** — include **malicious** internal-docs scenarios for RAG ([rag-retrieval-baseline.md](../patterns/rag-retrieval-baseline.md)).
- **Licence** — training or RAG over **third-party** code/docs: copyright and **licence** boundaries are **legal**, not engineering-only.

---

## 10. Doctrine Map (Where To Hang Future Work)

| Topic | Preferred location in **this** repo |
| --- | --- |
| Organisational AI policy, roles, allowed tools | **Outside** portable doctrine—**GRC** handbook; **cross-link** from SDL if needed |
| RAG retrieval, eval, tenant isolation | [patterns/rag-retrieval-baseline.md](../patterns/rag-retrieval-baseline.md) + estate supplements |
| Agent tool safety, SSRF | [api-boundaries-and-security.md](../principles/api-boundaries-and-security.md) |
| Handoff structure, ADR linkage | [documentation-knowledge.md](../principles/documentation-knowledge.md), [collaboration.md](../principles/collaboration.md) |
| Automation audit trail | [audit-logging.md](../principles/audit-logging.md) |
| CI as gatekeeper | [build.md](../principles/build.md), [testing-strategy.md](../principles/testing-strategy.md) |
| Chaos / resilience for AI dependencies | [chaos-engineering-and-game-days.md](../patterns/chaos-engineering-and-game-days.md) |
| Cost of models at scale | [performance-and-cost.md](../principles/performance-and-cost.md) |
| Portable **AI / ML-assisted systems** principle | [`principles/ai-ml-systems.md`](../principles/ai-ml-systems.md) — tiers, SoR, merge path, OWASP LLM / NIST pointers |

---

## 11. Anti-Patterns (For Executives And Architects)

- **“Train on all Slack”** — maximises **leakage** and **toxic** context; conflicts with minimisation and retention discipline.
- **Single shared index** for **all** employees without **ACLs** — **cross-tenant** retrieval incident waiting to happen.
- **Autopilot merge** on **main** without **required checks** — violates trunk discipline and incident learning.
- **Doctrine in prompts only** — **bypasses** review and **bisect**; **git** must win.

---

## 12. Suggested Next Steps (All ADR- Or Legal-Gated)

1. **Charter** — scope, **risk tier**, **allowed** data classes for indexing and for **fine-tuning** (often: **none** for prod PII).
2. **Map** one **pilot** workflow (e.g. “draft ADR from template + links”) under full **audit** and **DLP** review.
3. **Measure** — retrieval **hit rate**, **human edit distance** on agent drafts, **incident** count—before broadening automation.
4. **Optional** future pattern: `patterns/agent-assisted-change-governance.md` — **checklist** for tool allowlists, PR requirements, and council **when** to use—**only** if the org commits to maintenance. (Baseline portable rules now live in [`principles/ai-ml-systems.md`](../principles/ai-ml-systems.md).)

---

## 13. References (URLs)

| Resource | URL |
| --- | --- |
| NIST AI Risk Management Framework | https://www.nist.gov/itl/ai-risk-management-framework |
| NIST AI RMF Playbook | https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook |
| NIST AI RMF 1.0 (AI 100-1 PDF) | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf |
| AI RMF Core (AIRC excerpt) | https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ |
| OWASP LLM Top 10 (GenAI) | https://genai.owasp.org/llm-top-10/ |
| NIST SSDF SP 800-218 | https://csrc.nist.gov/publications/detail/sp/800-218/final |
| NIST SP 800-218A (GenAI / foundation models profile) | https://csrc.nist.gov/pubs/sp/800/218/a/final |
| NIST AI 600-1 — AI RMF Generative AI Profile (PDF) | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf |
| NIST AI 600-1 — publication page | https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence |

---

*Research captured: 2026-04-06. Revisit when an **ADR** adopts internal agentic development at scale.*
