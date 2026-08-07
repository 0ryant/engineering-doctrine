# How To Read This Doctrine

Use this page when onboarding to the repository or deciding **what to adopt** in another org.

---

## Layers (Outermost To Innermost)

1. **`ENGINEERING.md`** (repo root) — **Core constitution and route map**: canonical for the small set of core propositions, normative vocabulary, applicability/exception entry points, and adoption routes. It does not duplicate topic detail.
2. **`doctrine/SEMANTIC_INDEX.md`** — **Route map**: task intent to the source files an agent or reader should ingest. It is navigation, not authority over the linked files. [`doctrine/DEPRECATED.md`](../DEPRECATED.md) is the companion **lifecycle register**: what is scheduled for removal, what has exited, and what the sweeps decided.
3. **`doctrine/principles/`** — **Durable topic authority**: platform-agnostic outcomes, constraints, and trade-offs, with rationale and references. Prefer citing these when embedding doctrine in another repo.
4. **`doctrine/patterns/`** — **Compositional and conditional guidance**: how principles fit together in an operating model. A pattern's scoped obligations activate only when its applicability conditions are met.
5. **`doctrine/checklists/`** — **Derived review surfaces**: questions and evidence prompts for applicable principles and patterns. A checklist is not the sole authority for a new obligation.
6. **`doctrine/tooling/`** — **Illustrative** stacks, filenames, and implementation options. Swap freely while preserving the applicable outcomes and contracts.
7. **`doctrine/tooling/estates/`** — **Optional** organisation/cloud supplements. Never copy estate content into portable principles without generalising.
8. **`doctrine/evolution/`** — **Non-normative evidence and history**: research, audits, and change rationale. Use it when investigating why, not as default operating authority.

Meta-rule: **[principles/timeless-principles-and-tooling.md](../principles/timeless-principles-and-tooling.md)** explains why the split exists.

## Normative Language, Applicability, And Exceptions

Before applying a material claim, read
[normative-language-applicability-and-exceptions.md](normative-language-applicability-and-exceptions.md):

1. determine which baseline, named profile, and external authority apply;
2. interpret capitalised `MUST`, `SHOULD`, and `MAY` at claim level;
3. treat `CONTEXT-DEPENDENT` guidance as a required trade-off decision and
   `EXAMPLE` content as non-normative;
4. bind the claim to expected evidence; and
5. keep any authorised exception separate from the rule and evidence result.

Applicability is an overlay on the layers above, not another directory
hierarchy. A high-materiality or externally governed surface can activate a
stricter profile without making that profile universal doctrine.

---

## Suggested Reading Order

Times are **rough first-pass** estimates (skim vs deep read varies). Use [`tldr-principles-and-mvp.md`](../tldr-principles-and-mvp.md) when you need **under ~15 minutes**.

| Audience | Path | Approx. reading |
| --- | --- | --- |
| **Sponsor / TL;DR** | [`tldr-principles-and-mvp.md`](../tldr-principles-and-mvp.md) → [`glossary.md`](../glossary.md) if jargon-heavy → `timeless-principles-and-tooling` or `adoption-playbook` | **15–35 min** (TL;DR **~8 min**, glossary skim **~12 min**) |
| **Agent / AI contributor** | [`SEMANTIC_INDEX.md`](../SEMANTIC_INDEX.md) → route matching the task → [`doctrine-library-change-harness.md`](doctrine-library-change-harness.md) if editing doctrine/ADR/umbrella files | **10-25 min** before focused work; more for the routed source docs |
| **New org adopting wholesale** | `ENGINEERING.md` → `normative-language-applicability-and-exceptions` → `timeless-principles-and-tooling` → `adoption-playbook` → routed topic principles | **~45–90 min** before topic depth |
| **Platform / SRE** | `observability` → `reliability-slo-incidents` → `data-and-migrations` → [platform-as-product-and-golden-paths.md](platform-as-product-and-golden-paths.md) → `platform-readiness` checklist | **~55–100 min** + checklist **~20 min** |
| **Developer experience / platform enablement** | [`developer-experience.md`](../principles/developer-experience.md) → [`developer-experience-scorecard.md`](../checklists/developer-experience-scorecard.md) → `measurement-and-dora` §4 → `documentation-knowledge` → `build` §3 | **~35–70 min** |
| **Security / API** | `api-boundaries-and-security` → `threat-modeling-stride-lite` → [`merge-path-evidence-and-pipeline-integrity.md`](../principles/merge-path-evidence-and-pipeline-integrity.md) → `dependencies-supply-chain`; when a contract/regulation applies, add [`revision-pinned-control-profiles.md`](revision-pinned-control-profiles.md) | **~55–110 min** for core; **+20–35 min** for the external-profile path |
| **GenAI / RAG / retrieval (product)** | [`ai-ml-systems.md`](../principles/ai-ml-systems.md) (esp. §§6–7) → [rag-retrieval-baseline.md](rag-retrieval-baseline.md) → [`tooling/vector-retrieval-and-embedding-illustration.md`](../tooling/vector-retrieval-and-embedding-illustration.md) → `privacy-and-data-governance` §5 → `api-boundaries-and-security` → (optional) [research-enterprise-rag-agents-indexing-2026-04.md](../evolution/research-enterprise-rag-agents-indexing-2026-04.md), [research-ai-ml-ops-landscape-2026-04.md](../evolution/research-ai-ml-ops-landscape-2026-04.md) skim | **~50–90 min** |
| **Internal AI / dev agents (enterprise)** | [`ai-ml-systems.md`](../principles/ai-ml-systems.md) §§4, 7 → [`agentic-loop-design.md`](agentic-loop-design.md) (loops, autonomy, multi-agent) → [`run-contracts.md`](run-contracts.md) (governed execution) → `collaboration` §3, `documentation-knowledge`, `audit-logging` → [`tooling/ai-assisted-development.md`](../tooling/ai-assisted-development.md); consult evolution notes only for rationale or research | **~60–100 min** |
| **Async / events** | `event-contracts` → `state-machines-and-workflows` → `message-channel-operations` → `tooling/cloudevents.md` (optional `tooling/nats-jetstream` / `kafka-and-cloudevents`, examples below) | **~40–80 min** + **~15–25 min** per worked **fiction** example |

---

## Resolving Apparent Conflicts

- `ENGINEERING.md` owns core propositions; principle files own durable topic
  detail. A contradiction between them is a defect: block the affected policy
  decision, record the conflict, and propose a harmonising change rather than
  selecting the convenient wording.
- If two applicable principles overlap, satisfy both compatible obligations
  and use the stricter result for the shared property. If their required
  methods or authorities conflict, escalate an explicit authority decision.
- A binding law, regulation, contract, or external profile keeps its own
  authority and revision rules. Use
  [revision-pinned-control-profiles.md](revision-pinned-control-profiles.md);
  this library cannot grant an exception from an external obligation.
- Patterns are authoritative for their activated operating model; checklists
  derive review questions; tooling and examples do not override principles or
  activated patterns; evolution notes never create an obligation by themselves.
- For merge-path invariants, [merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md)
  owns the detailed controlled-channel and evidence requirements. Any broader
  build wording must remain compatible with it.

---

## Checklists

- Repo rollout: `checklists/build-readiness.md`, `collaboration-readiness.md`, `platform-readiness.md`, `developer-experience-scorecard.md`.
- **Releases:** `checklists/release-readiness.md`.
- **Editing this library:** [doctrine-library-change-harness.md](doctrine-library-change-harness.md) (research, claim strength/applicability, ADR, navigation); [normative-language-applicability-and-exceptions.md](normative-language-applicability-and-exceptions.md); `checklists/doctrine-change-checklist.md`; [code-review-and-change-approval.md](code-review-and-change-approval.md) (review **duties** and **escalation** for contributors); release labels and consumer impact: [doctrine-versioning-and-consumer-compatibility.md](doctrine-versioning-and-consumer-compatibility.md); status vocabulary and supersession/retirement mechanics: [doctrine-content-lifecycle.md](doctrine-content-lifecycle.md).
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
