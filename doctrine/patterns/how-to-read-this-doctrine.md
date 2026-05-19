# How To Read This Doctrine

Use this page when onboarding to the repository or deciding **what to adopt** in another org.

---

## Layers (Outermost To Innermost)

1. **`ENGINEERING.md`** (repo root) — **Umbrella** summary: the full list of headline principles and pointers. It can lag slightly; if in doubt, the **`doctrine/principles/`** file wins for detail.
2. **`doctrine/SEMANTIC_INDEX.md`** — **Route map**: task intent to the source files an agent or reader should ingest. It is navigation, not authority over the linked files.
3. **`doctrine/principles/`** — **Timeless** rules: platform-agnostic, with **rationale** and **references** per topic. Prefer citing these when embedding doctrine in another repo.
4. **`doctrine/patterns/`** — **Compositional** guidance: how build surfaces, trunk workflow, message operations, and similar ideas fit together. Not every pattern applies to every repo.
5. **`doctrine/tooling/`** — **Illustrative** stacks (task runners, CI mapping, bots). Swap freely; keep **surface meanings** from `principles/build.md`.
6. **`doctrine/tooling/estates/`** — **Optional** vendor/cloud notes (example: Azure). Never copy estate content into portable principles without generalising.

Meta-rule: **[principles/timeless-principles-and-tooling.md](../principles/timeless-principles-and-tooling.md)** explains why the split exists.

---

## Suggested Reading Order

Times are **rough first-pass** estimates (skim vs deep read varies). Use [`tldr-principles-and-mvp.md`](../tldr-principles-and-mvp.md) when you need **under ~15 minutes**.

| Audience | Path | Approx. reading |
| --- | --- | --- |
| **Sponsor / TL;DR** | [`tldr-principles-and-mvp.md`](../tldr-principles-and-mvp.md) → [`glossary.md`](../glossary.md) if jargon-heavy → `timeless-principles-and-tooling` or `adoption-playbook` | **15–35 min** (TL;DR **~8 min**, glossary skim **~12 min**) |
| **Agent / AI contributor** | [`SEMANTIC_INDEX.md`](../SEMANTIC_INDEX.md) → route matching the task → [`doctrine-library-change-harness.md`](doctrine-library-change-harness.md) if editing doctrine/ADR/umbrella files | **10-25 min** before focused work; more for the routed source docs |
| **New org adopting wholesale** | `timeless-principles-and-tooling` → `build` → `collaboration` → `ENGINEERING.md` | **~60–120 min** for those four; full §18 extended set **adds 2–4 h** |
| **Platform / SRE** | `observability` → `reliability-slo-incidents` → `data-and-migrations` → [platform-as-product-and-golden-paths.md](platform-as-product-and-golden-paths.md) → `platform-readiness` checklist | **~55–100 min** + checklist **~20 min** |
| **Developer experience / platform enablement** | [`developer-experience.md`](../principles/developer-experience.md) → [`developer-experience-scorecard.md`](../checklists/developer-experience-scorecard.md) → `measurement-and-dora` §4 → `documentation-knowledge` → `build` §3 | **~35–70 min** |
| **Security / API** | `api-boundaries-and-security` → `threat-modeling-stride-lite` → [`merge-path-evidence-and-pipeline-integrity.md`](../principles/merge-path-evidence-and-pipeline-integrity.md) → `ENGINEERING.md` §18 (extended principles) → `dependencies-supply-chain` | **~55–110 min** for core; **+1–2 h** if reading every extended principle |
| **GenAI / RAG / retrieval (product)** | [`ai-ml-systems.md`](../principles/ai-ml-systems.md) (esp. §§6–7) → [rag-retrieval-baseline.md](rag-retrieval-baseline.md) → [`tooling/vector-retrieval-and-embedding-illustration.md`](../tooling/vector-retrieval-and-embedding-illustration.md) → `privacy-and-data-governance` §5 → `api-boundaries-and-security` → (optional) [research-enterprise-rag-agents-indexing-2026-04.md](../evolution/research-enterprise-rag-agents-indexing-2026-04.md), [research-ai-ml-ops-landscape-2026-04.md](../evolution/research-ai-ml-ops-landscape-2026-04.md) skim | **~50–90 min** |
| **Internal AI / dev agents (enterprise)** | [`ai-ml-systems.md`](../principles/ai-ml-systems.md) §§4, 7 → [research-internal-ai-knowledge-factory-governance-2026-04.md](../evolution/research-internal-ai-knowledge-factory-governance-2026-04.md) → `collaboration` §3, `documentation-knowledge`, `audit-logging` → [`tooling/ai-assisted-development.md`](../tooling/ai-assisted-development.md) → (optional) [research-enterprise-rag-agents-indexing-2026-04.md](../evolution/research-enterprise-rag-agents-indexing-2026-04.md) §4 (MCP) | **~50–95 min** |
| **Async / events** | `event-contracts` → `state-machines-and-workflows` → `message-channel-operations` → `tooling/cloudevents.md` (optional `tooling/nats-jetstream` / `kafka-and-cloudevents`, examples below) | **~40–80 min** + **~15–25 min** per worked **fiction** example |

---

## Resolving Apparent Conflicts

- If **`ENGINEERING.md`** and a **principle file** disagree on detail, treat the **principle** as authoritative and propose an **ENGINEERING** edit.
- If **two principle files** seem to overlap (for example security vs API), apply the **stricter** consumer-facing requirement and open a PR to cross-link both.
- For **merge-path invariants** (binding gates, pipeline definitions in scope, evidence expectations), [merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md) §2 is authoritative over general build-surface wording where they differ until texts are harmonised.

---

## Checklists

- Repo rollout: `checklists/build-readiness.md`, `collaboration-readiness.md`, `platform-readiness.md`, `developer-experience-scorecard.md`.
- **Releases:** `checklists/release-readiness.md`.
- **Editing this library:** [doctrine-library-change-harness.md](doctrine-library-change-harness.md) (research, ADR, navigation); `checklists/doctrine-change-checklist.md`; [code-review-and-change-approval.md](code-review-and-change-approval.md) (review **duties** and **escalation** for contributors); [gitops-and-declarative-operations.md](gitops-and-declarative-operations.md) (declarative **ops** and **IaC** invariants); release labels and consumer impact: [doctrine-versioning-and-consumer-compatibility.md](doctrine-versioning-and-consumer-compatibility.md).
- **Adopting with a team:** `patterns/adoption-playbook.md`, `tooling/estates/minimum-viable-doctrine.template.md`, `principles/measurement-and-dora.md`.

---

## Forking, Subtrees, And Submodules (Adoption Mechanics)

- **Fork or copy** — simplest: treat this repo as **upstream** and merge periodically; good when you want **full** autonomy.
- **Git subtree** — vendor `doctrine/` (or the whole repo) into a **subdirectory** of another monorepo; preserves history and allows **selective** pulls from upstream.
- **Git submodule** — pins a **specific commit** of this library; reviewers see **exactly** which doctrine revision ships—at the cost of **submodule** ergonomics every developer must tolerate.

Pick one **mechanism** per org and document it in the **consumer** repo’s README so upgrades are **intentional**, not accidental drift.

Pin a **tag**, **commit**, subtree merge, or submodule revision for policy-sensitive adoption. Before importing upstream changes, read [doctrine-versioning-and-consumer-compatibility.md](doctrine-versioning-and-consumer-compatibility.md) to classify the update as **editorial**, **additive**, **normative**, **estate-only**, or **breaking** for the consumer.

---

## Worked Examples (Fiction)

| File | Topic | ~Time |
| --- | --- | --- |
| [example-order-jetstream-workflow.md](example-order-jetstream-workflow.md) | FSM + CloudEvents + JetStream subjects | **~15 min** |
| [example-saga-payment-workflow.md](example-saga-payment-workflow.md) | Saga, compensation, timeouts, events | **~12 min** |
