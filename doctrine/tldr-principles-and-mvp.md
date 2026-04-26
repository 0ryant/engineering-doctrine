# TL;DR: Principles Synthesis And Minimum Viable Doctrine

**Audience:** sponsors, new leads, or teams who need the **shape** of this library in one pass before opening dozens of files. **Depth** always lives in linked principles—not here.

---

## What This Library Is

Portable **engineering intent** split from **replaceable tooling**: principles state what must stay true across estates; `tooling/` shows one way to implement today. The repo root **[`ENGINEERING.md`](../ENGINEERING.md)** is the headline index; when detail conflicts, the matching file under **`principles/`** wins. Meta: **[timeless-principles-and-tooling.md](principles/timeless-principles-and-tooling.md)**. **GenAI, RAG, agents, and retrieval** are **first-class**—not an exception path—see **[`ai-ml-systems.md`](principles/ai-ml-systems.md)**.

---

## Principles Spine (One Line Each)

| # | Idea | Canonical depth |
| --- | --- | --- |
| 1 | **Contracts first** — schemas (and examples) before callers; versioned; validate in CI. | [`ENGINEERING.md` §1](../ENGINEERING.md), [`event-contracts.md`](principles/event-contracts.md) for async |
| 2 | **Explicit build surfaces** — quality gate, build/publish, deploy, verify; local mirrors CI; **promote** the same artefact. | [`build.md`](principles/build.md), [`patterns/build-surface-model.md`](patterns/build-surface-model.md) |
| 3 | **Trunk and small change** — short-lived branches, reviewed merge, green `main`; flags for incomplete work. **Small PR default:** ~**400 lines** or ~**20 files**, one concern ([`collaboration.md`](principles/collaboration.md) §3, [`trunk-workflow.md`](patterns/trunk-workflow.md)). | [`collaboration.md`](principles/collaboration.md), [`patterns/trunk-workflow.md`](patterns/trunk-workflow.md) |
| 4 | **Idempotency and safe retries** — mutating work tolerates duplicate delivery (HTTP, messages, jobs). | [`ENGINEERING.md` §4](../ENGINEERING.md), [`patterns/idempotency-across-boundaries.md`](patterns/idempotency-across-boundaries.md) |
| 5 | **Security in the loop** — no secrets in git, scan dependencies, least privilege for CI/deploy, SDL-style design and response. | [`ENGINEERING.md` §5](../ENGINEERING.md), [`secure-development-lifecycle.md`](principles/secure-development-lifecycle.md), [`dependencies-supply-chain.md`](principles/dependencies-supply-chain.md) |
| 6 | **Single sources of truth** — one version line per publishable unit, one place for config/secrets **references** (not values). | [`semantic-versioning.md`](principles/semantic-versioning.md), [`single-source-of-truth.md`](principles/single-source-of-truth.md), [`configuration-and-secrets.md`](principles/configuration-and-secrets.md) |
| 7 | **Operability** — structured logs + trace correlation; runbooks; SLOs where users care; blameless learning. | [`observability.md`](principles/observability.md), [`reliability-slo-incidents.md`](principles/reliability-slo-incidents.md), [`documentation-knowledge.md`](principles/documentation-knowledge.md) |
| 8 | **Modular boundaries** — I/O at edges; ports/adapters or thin boundaries; interoperability specs without mandating a full vendor stack. | [`modularity-and-ports-adapters.md`](principles/modularity-and-ports-adapters.md), [`interoperability-and-standards.md`](principles/interoperability-and-standards.md) |
| 9 | **AI-assisted change** — repo stays **SoR**; tiers A–D for API-only → RAG → training → agents; **same** CI/review bar for agent-opened PRs; **index/embedding** lifecycle and **MCP**-class tools are **integration** surfaces. | [`ai-ml-systems.md`](principles/ai-ml-systems.md) §§6–8, [`tooling/ai-assisted-development.md`](tooling/ai-assisted-development.md), [`tooling/vector-retrieval-and-embedding-illustration.md`](tooling/vector-retrieval-and-embedding-illustration.md), [`patterns/rag-retrieval-baseline.md`](patterns/rag-retrieval-baseline.md) |
| 10 | **Developer experience** — safe small changes should be easy: fast local loop, findable docs, clear ownership, low cognitive load, timely review. | [`developer-experience.md`](principles/developer-experience.md), [`developer-experience-scorecard.md`](checklists/developer-experience-scorecard.md), [`measurement-and-dora.md`](principles/measurement-and-dora.md) §4 |

**Not** listed above does **not** mean “optional forever”—it means **second wave** for most teams (API hardening, threat modeling, privacy, K8s baseline, performance budgets, DORA metrics, etc.). Entry: [`ENGINEERING.md` §18](../ENGINEERING.md).

---

## Minimum Viable Doctrine (MVP)

**Definition:** the smallest set of practices that makes **further** doctrine adoption safe—usually **weeks**, not a big-bang program.

| Order | Do this | Why | Verify |
| --- | --- | --- | --- |
| 1 | **One quality gate** — fmt/lint/test/contract checks in CI **and** one local command that matches. | Without it, every process change is guesswork. | [`checklists/build-readiness.md`](checklists/build-readiness.md) (subset) |
| 2 | **Protected trunk** — no direct push to default branch; required checks; small PRs. | Stops integration debt and silent drift. | [`checklists/collaboration-readiness.md`](checklists/collaboration-readiness.md) (subset) |
| 3 | **Developer first-change path** — README says owner, setup, fast check, first safe change, and deeper docs. | Controls fail if the safe path is hidden or slow. | [`developer-experience-scorecard.md`](checklists/developer-experience-scorecard.md) (subset) |
| 4 | **One boundary contract** — OpenAPI/JSON Schema **or** CloudEvents + payload schema + examples + CI validation. | Stops tribal JSON and silent breaks. | [`event-contracts.md`](principles/event-contracts.md) or umbrella [`ENGINEERING.md` §1](../ENGINEERING.md) |
| 5 | **Observability baseline** — correlated logs/traces on main paths; owners know where dashboards live. | Incidents become diagnosable. | [`observability.md`](principles/observability.md) (§§1–2) |
| 6 | **Ownership and learning** — named service/repo owners; blameless postmortems with tracked actions when things fail. | Closes the loop without full SLO math on day one. | [`collaboration.md`](principles/collaboration.md) §8, [`reliability-slo-incidents.md`](principles/reliability-slo-incidents.md) (skim) |

**Team one-pager:** copy [`tooling/estates/minimum-viable-doctrine.template.md`](tooling/estates/minimum-viable-doctrine.template.md) to your estate folder and fill **5–7** rows with **your** pain and links—do not paste the whole tree.

**Phased adoption narrative:** [`patterns/adoption-playbook.md`](patterns/adoption-playbook.md) (including **§8 troubleshooting** for common blockers). **Outcome metrics (optional early, valuable soon):** [`principles/measurement-and-dora.md`](principles/measurement-and-dora.md).

---

## After MVP (Typical Wave 2)

Supply-chain automation; **AI/RAG/agents** when in scope ([`ai-ml-systems.md`](principles/ai-ml-systems.md), [`checklists/platform-readiness.md`](checklists/platform-readiness.md)); platform/readiness checklists, STRIDE-lite on internet-facing surfaces, data/migration discipline, release checklist for versioned artefacts—see [`checklists/platform-readiness.md`](checklists/platform-readiness.md) and [`checklists/release-readiness.md`](checklists/release-readiness.md).

---

## References (This Page Only)

- Full navigation: [`patterns/how-to-read-this-doctrine.md`](patterns/how-to-read-this-doctrine.md)  
- Terms and acronyms: [`glossary.md`](glossary.md)  
- Canonical external index: [`REFERENCES.md`](REFERENCES.md)  
