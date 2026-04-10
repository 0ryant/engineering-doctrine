# Deep Research: Gaps By Doctrine Section

**Date:** 2026-04-07.  
**Method:** Compared the repo’s **structure and line depth** (~50 Markdown sources under `doctrine/` + `ENGINEERING.md`) against common **regulatory and industry frameworks** (NIST SSDF, DORA, SRE, OWASP families, FinOps, platform engineering practice) and against **typical internal-handbook coverage** at mature product orgs. This is a **gap map**, not a commitment to implement everything—many gaps are intentionally out of scope for a portable library.

**Line counts (rough):** thinnest first — `release-readiness` (~15), `doctrine-change-checklist` (~16), estate stubs (~19), `platform-readiness` (~26), `build-readiness` (~35), several principles ~45–58 lines (`documentation`, `interoperability`, `performance`, `privacy`, `testing`, `measurement`).

---

## 1. Umbrella `ENGINEERING.md` (only)

Sections **1, 13, 14, 18** have strong mirrors in `doctrine/principles/` and patterns. These exist **mostly in the umbrella** without a dedicated deep principle file:

| § | Topic | Gap / risk | If you deepen |
| --- | --- | --- | --- |
| 2 | TDD | `testing-strategy.md` covers pyramid/contracts/flake—not **TDD ceremony**, red-green-refactor, or “when TDD is wrong” | Optional `principles/test-driven-development.md` or expand §2 pointer |
| 3 | DRY / SSOT | No principle on **duplication vs wrong abstraction**, generated code, config SSOT | Short `principles/single-source-of-truth.md` or fold into `build.md` |
| 4 | Idempotency | Scattered; no **unified** idempotency + outbox + HTTP idempotency keys | Pattern or principle linking API + events + infra |
| 5 | Shift security (crypto) | Strong **implementation** detail here; **thin** on SDL, secure design review, vuln disclosure | Bridge to SSDF PW/RV; optional `principles/secure-development-lifecycle.md` |
| 7 | Lego / ports-adapters | High value, **no** standalone file—only umbrella | `principles/modularity-and-ports-adapters.md` |
| 8 | Zero Trust | **No** deep principle (workload identity, service-to-service, SPIFFE mention) | `principles/zero-trust-and-workload-identity.md` or estate-specific |
| 9 | Layered architecture | **No** standalone file vs DDD/hexagonal nuance | `principles/layered-and-hexagonal-architecture.md` |
| 10 | Audit everything | **No** principle file—only umbrella + product examples | `principles/audit-logging.md` (fields, PII, retention link to privacy) |
| 15 | Error handling | Partially in `api-boundaries`; **CLI/desktop** error UX thin | Extend API doc or `principles/errors-and-failure-modes.md` |
| 16 | Configuration & secrets | **No** principle—rotation, dynamic config, **12-factor** config vs secrets split | `principles/configuration-and-secrets.md` |
| 17 | Naming & structure | **No** principle—only umbrella | `principles/naming-and-repo-layout.md` |

---

## 2. Principles (`doctrine/principles/`)

| File | Strength | Notable gaps (research) |
| --- | --- | --- |
| **timeless-principles-and-tooling** | Meta split is best-in-class | Optional explicit **mapping** to NIST SSDF PO/PS/PW/RV one-pager |
| **build** | Surfaces, CI vs scripts, promotion | **Hermetic builds**, **build provenance** (SLSA-style attestation) only implicit |
| **collaboration** | Trunk, PRs, flags, async | **On-call** health (handoff quality, alert budget), **review SLAs**, **CODEOWNERS** depth, **merge queue** ops |
| **event-contracts** | CloudEvents, semantics | **Webhook** security (signature, timestamp, replay window), **scheduled** and **batch** event semantics |
| **state-machines-and-workflows** | FSM → events, replay | **Saga / compensation** naming, **timeouts** per state, **human-in-the-loop** |
| **semantic-versioning** | Per unit, deprecation | **Pre-release** channels, **API versioning** in URL vs header (HTTP) |
| **interoperability-and-standards** | Spec vs stack | **gRPC** / **Protobuf** as first-class alternative to REST+JSON where relevant |
| **container-runtime-choice** | Managed vs K8s | **Edge / device** runtimes, **Windows containers** estate notes |
| **kubernetes-platform-security** | PSA, network policy pointer | **RBAC** defaults, **secrets** in cluster (encryption at rest, External Secrets), **service mesh** “when” not “which vendor” |
| **data-and-migrations** | Expand/contract, backups | **DR** and **RTO** beyond backup, **multi-region**, **failover** drills |
| **observability** | Three pillars, cardinality | **Profiling** / continuous profiling, **eBPF** as optional depth; **SLI** definition link to SLO doc |
| **testing-strategy** | Pyramid, contracts, flake | **Mutation testing** (you reference in other contexts—not here), **property-based** tests, **accessibility** testing in CI |
| **api-boundaries-and-security** | OWASP API, limits | **Browser** security (CSP, CORS depth), **GraphQL** abuse, **mTLS** service mesh mention |
| **threat-modeling-stride-lite** | STRIDE lite | **Attack trees**, **data-flow** diagram tooling, **supply-chain** threats in TM |
| **privacy-and-data-governance** | Minimisation, retention | **DPIA** / **PIA** trigger, **consent** UX, **AI** training data & PII (NIST Privacy + **SP 800-218A** AI profile) |
| **reliability-slo-incidents** | SLO, error budget, incidents | **Chaos** / **Gamedays**, **toil** budget, **post-incident** metrics into DORA |
| **performance-and-cost** | Budgets, load, FinOps tags | **Carbon** / sustainability (growing enterprise ask), **quota** governance at org level |
| **documentation-knowledge** | ADR, runbook | **Onboarding curricula**, **internal search** / portal (see Platform below), **RFC** lifecycle vs ADR |
| **dependencies-supply-chain** | Lockfiles, SBOM, licence | **Provenance** (SLSA), **typosquatting**, **package registry** hygiene, **vuln disclosure** to users |
| **user-facing-quality** | WCAG, i18n scope | **Mobile** a11y, **voice** UIs, **PDF** accessibility if shipping docs |
| **measurement-and-dora** | Four Keys map | **SPACE** metrics (developer experience), **North Star** product metrics (explicitly “not this doc”) |

---

## 3. Patterns (`doctrine/patterns/`)

| File | Strength | Gaps |
| --- | --- | --- |
| **how-to-read-this-doctrine** | Layers, conflicts | **Forking** / **subtree** / **submodule** of this repo as adoption mechanic |
| **build-surface-model** | Surfaces | **Monorepo** vs polyrepo implications on surfaces |
| **trunk-workflow** | Hotfix, release | **Long-term support** branches when legally required |
| **message-channel-operations** | DLQ, replay | **Exactly-once illusions**, **ordering** guarantees table by broker class |
| **adoption-playbook** | Phased adoption | **Executive** narrative, **ROI** framing, **vendor** migration (e.g. Jenkins→GitHub Actions) |
| **example-order-jetstream** | End-to-end fiction | Optional second example (**saga** or **webhook** ingress) |

---

## 4. Tooling (`doctrine/tooling/` + estates)

| Area | Strength | Gaps |
| --- | --- | --- |
| **build / ci / collaboration / observability / cloudevents** | Illustrative | **Kafka** or **Pulsar** sibling to `nats-jetstream.md` if multi-estate |
| **dependency-automation** | Renovate/Dependabot | **OSV**, **GitHub** advisory API, **license** scanning tools |
| **estates** | Azure + stubs + MVD | **No** filled AWS/GCP; **no** “default SME laptop” estate (Podman/Docker detail) |
| **nats-jetstream** | Ops + binding | **Key management**, **TLS**, **auth** (NKeys, JWT) cross-link to Zero Trust if added |

---

## 5. Checklists (`doctrine/checklists/`)

| File | Gap |
| --- | --- |
| **build-readiness** | **SLSA** / provenance checkbox row optional |
| **collaboration-readiness** | **CODEOWNERS**, **merge queue**, **review latency** SLO |
| **platform-readiness** | **Chaos** / game day, **DR** drill, **multi-region**, **webhook** hardening |
| **release-readiness** | Very short—expand **communicate** release, **customer** comms, **deprecation** execution |
| **doctrine-change-checklist** | **Version** or **changelog** for the doctrine repo itself |

---

## 6. Meta (`evolution/`, `REFERENCES.md`, `SITEMAP`)

| Area | Gap |
| --- | --- |
| **REFERENCES** | **NIST SSDF** (SP 800-218), **SLSA**, **OWASP ASVS** (application not only API), **CIS** benchmarks cross-link |
| **evolution** | No **decision log** for “why we didn’t add X” (Won’t list lives in MoSCoW only) |
| **Honest review synthesis** | Refresh after this gap pass |

---

## 7. Cross-Cutting “Industry Shape” You Mostly Skip (Often Intentionally)

| Domain | Typical external expectation | Your doctrine posture |
| --- | --- | --- |
| **NIST SSDF** | PO/PS/PW/RV full SDLC | You cover **many** PW/PS tasks via build, deps, secrets; **light** on formal PO (training, roles) and **RV** (coordinated disclosure, customer comms) |
| **Internal Developer Platform** | Golden paths, service catalog, self-service infra | **Not present**—would be `tooling/estates/` or separate “platform doctrine” |
| **AI / ML systems** | Model cards, eval gates, data lineage, SP 800-218A | **Portable coverage** — [principles/ai-ml-systems.md](../principles/ai-ml-systems.md), [patterns/rag-retrieval-baseline.md](../patterns/rag-retrieval-baseline.md), vector tooling illustration, `evolution/research-*.md`; **estate** ADRs for model cards and hyperscaler IaC remain org-specific |
| **Compliance regimes** | SOC2, ISO 27001 control mapping | **Absent** (by design for portability) |
| **Chaos engineering** | Gremlin / custom fault injection | **Absent** in reliability principle |
| **Sustainability / Green Software** | SCI, carbon aware | **Absent** in performance-and-cost |

---

## 8. Consolidated Backlog (MoSCoW)

### Must (if you want “regulatory-shaped” completeness)

- Add **REFERENCES** rows: NIST SSDF SP 800-218, SLSA homepage, OWASP ASVS (link only).
- Expand **release-readiness** to non-trivial length (comms, rollback evidence, deprecation execution).

### Should

- Extract **2–3** umbrella-only topics into principles: **configuration-and-secrets**, **audit-logging**, **modularity/ports** (or one combined “architecture invariants”).
- **Webhook** subsection under `event-contracts` or small **patterns/webhook-ingress-security.md`.
- **DR / failover** subsection in `data-and-migrations` or reliability.

### Could

- **Chaos / gameday** pattern or reliability subsection.
- **Kafka** tooling file mirroring NATS depth.
- **Testing-strategy**: mutation + property-based bullets.
- **SPACE** or **developer experience** one-pager linked from `measurement-and-dora`.

### Won’t (unless scope changes)

- Full **SOC2** control mapping.
- **Vendor-specific** ML platform runbooks, **model-card** templates, and **hyperscaler** landing-zone IaC as **portable** files in this library (use [principles/ai-ml-systems.md](../principles/ai-ml-systems.md) + **NIST SP 800-218A** + **estate** supplements).
- **Enterprise portal** / IDP product doctrine.

---

## 9. References For This Research

- NIST **SSDF** / SP 800-218: https://csrc.nist.gov/Projects/SSDF  
- NIST **SP 800-218A** (AI community profile): https://csrc.nist.gov/ (see SSDF project news)  
- **DORA**: https://dora.dev/  
- **SLSA** supply-chain levels: https://slsa.dev/  
- OWASP **ASVS**: https://owasp.org/www-project-application-security-verification-standard/  
- **FinOps** (already in performance doc): https://www.finops.org/  

---

## Follow-Up

Re-run or narrow this audit when adding a **new principle domain** (e.g. AI, compliance) or yearly. Prefer **one** new file per domain over silent scope creep in `ENGINEERING.md`.

---

## 10. Gap Fill Status (2026-04-06)

Most **Should** / **Could** items from §8 and the per-file gaps in §§2–5 have been **addressed in-repo** with **cited** sources: new umbrella-aligned principles (`configuration-and-secrets`, `audit-logging`, `modularity-and-ports-adapters`, `secure-development-lifecycle`, `zero-trust-and-workload-identity`, `single-source-of-truth`, `errors-and-failure-modes`, `naming-and-repo-layout`), patterns (`webhook-ingress-security`, `idempotency-across-boundaries`), tooling (`kafka-and-cloudevents.md`), expansions to **build**, **collaboration**, **reliability**, **testing**, **event-contracts**, **semantic-versioning**, **interoperability**, **kubernetes**, **dependencies**, **privacy**, **performance**, **documentation**, **api-boundaries**, **threat-modeling**, **state-machines**, **observability**, **measurement**, **timeless** (SSDF map), **user-facing-quality**, plus checklist and **ENGINEERING.md** / **REFERENCES.md** / **README** navigation.

**Still Won’t (unless scope changes):** full SOC2/ISO control mapping, enterprise IDP product doctrine, filled AWS/GCP estate stubs—unchanged from §8 **Won’t**.

**Optional next pass:** refresh `honest-review-synthesis.md` after a human read of the expanded tree; validate external URLs on a schedule (especially OWASP community pages).

---

## 11. Residual 9.5+ Items (Status)

| Gap | Status |
| --- | --- |
| Second worked example (saga or HTTP API lifecycle) | **Done** — `patterns/example-saga-payment-workflow.md` (HTTP API lifecycle remains a **Could** if teams want OpenAPI-only fiction later). |
| Kafka tooling parity with NATS | **Done** — expanded `tooling/kafka-and-cloudevents.md` (companion links, core concepts table, naming hygiene, references). |
| OWASP API Top 10 explicit enumeration | **Done** — table + §§8–9 in `principles/api-boundaries-and-security.md` with official links. |
| Chaos / game day dedicated pattern | **Done** — `patterns/chaos-engineering-and-game-days.md`; linked from reliability principle and platform checklist. |
| Numeric “small PR” surfacing | **Done** — `collaboration.md` §3 (already), plus `trunk-workflow.md` and `tldr-principles-and-mvp.md` explicit pointers. |
| Reading time estimates on paths | **Done** — `patterns/how-to-read-this-doctrine.md` (table + worked-example timings). |
| **AI/ML systems in portable doctrine** (historical gap: “full ML dev doctrine”) | **Done** — [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) (§§6–7 eval, retrieval, MCP), [../tooling/ai-assisted-development.md](../tooling/ai-assisted-development.md), [../tooling/vector-retrieval-and-embedding-illustration.md](../tooling/vector-retrieval-and-embedding-illustration.md); **research**: [research-ai-ml-ops-landscape-2026-04.md](research-ai-ml-ops-landscape-2026-04.md), [research-internal-ai-knowledge-factory-governance-2026-04.md](research-internal-ai-knowledge-factory-governance-2026-04.md), [research-enterprise-rag-agents-indexing-2026-04.md](research-enterprise-rag-agents-indexing-2026-04.md); [glossary.md](../glossary.md) (**GenAIOps**, retrieval terms). **Not duplicated here:** model **cards**, hyperscaler **landing zone** IaC (estate ADRs); optional `patterns/agent-assisted-change-governance.md`; training-data rules in [privacy-and-data-governance.md](../principles/privacy-and-data-governance.md) §5.3. External SDLC profile: **NIST SP 800-218A** where adopted. |
