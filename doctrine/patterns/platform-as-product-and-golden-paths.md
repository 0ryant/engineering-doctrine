# Platform As Product, Golden Paths, And Service Catalog

Use this pattern when **several teams** share runtime, delivery, and security baselines—so “the platform” must be **discoverable**, **self-serve by default**, and **governed** without becoming a ticket bottleneck.

This is **portable doctrine**: it states **outcomes** and **metadata contracts** between product teams and platform/enabling teams. It does **not** require a named developer portal, service-catalog product, or CNCF project. Map these ideas to **your** estate (wiki, Git repo index, internal marketplace, or a catalog tool).

**External framing (optional read):** CNCF TAG App Delivery — [Platform Engineering Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/) (product mindset, self-service, adoption stages—verify current URL if the whitepaper moves).

Companion principles: [build.md](../principles/build.md), [container-runtime-choice.md](../principles/container-runtime-choice.md), [documentation-knowledge.md](../principles/documentation-knowledge.md), [measurement-and-dora.md](../principles/measurement-and-dora.md), [merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md). Related patterns: [build-surface-model.md](build-surface-model.md), [adoption-playbook.md](adoption-playbook.md); governance: [engineering-controls-governance-program.md](engineering-controls-governance-program.md).

---

## 1. Platform As Product

- **Customers** — Treat internal product teams as **users** of the platform: their jobs-to-be-done are **ship, operate, and comply** with minimal surprise.
- **Offerings** — Publish **what** the platform provides (templates, paved paths, managed runtimes, CI integrations, observability baselines) and **what** it does **not** promise.
- **Roadmap and feedback** — Prioritise work from **adoption friction**, **incident themes**, **toil**, and **security/compliance** gaps—not only infrastructure renewal. Lightweight feedback (office hours, surveys, defect tags on golden-path failures) beats no loop.
- **Support posture** — Define how teams get **help** and **escalation** for platform-owned paths (even informally at small scale). Ambiguous ownership recreates shadow IT.

**Why:** A “platform” that is only a cluster and a wiki page does not reduce organisational entropy; a **product** lens aligns enablement work with delivery outcomes ([measurement-and-dora.md](../principles/measurement-and-dora.md), SPACE-style developer experience in the same file).

---

## 2. Golden Paths (Paved Roads)

A **golden path** is the **blessed default** for the common case: scaffold → version control → quality gates → build/promote → deploy → operate—without every team reinventing glue.

- **Opinionated defaults** — Choose **sane** stacks and patterns where **variance is expensive** (authn/z hooks, secret handling, network posture, merge-path gates). Document **why** the default exists (ADR or short rationale).
- **Versioned recipes** — Paths are **versioned** or **dated** like other software: teams must know which template or baseline they are on and how to **upgrade**.
- **Same surfaces, clearer wiring** — Technical entrypoints stay consistent with [build.md](../principles/build.md) and [build-surface-model.md](build-surface-model.md); the golden path **composes** those surfaces into an end-to-end story.
- **Not the only path** — Teams may leave the path for **documented reasons** (see §6). The anti-pattern is **unmarked** divergence that bypasses guardrails.

---

## 3. Self-Service First, Guardrails Always

- **Automation over tickets** — The **default** request (new service namespace, standard database tier, pipeline from template) should complete via **API, template, or policy-driven workflow**—not a manual queue—subject to policy.
- **Guardrails in enforcement** — Org rules belong in **enforced** layers (pipeline required checks, admission/policy, IAM guardrails, merge protection per [merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md))—not only in prose.
- **Fast, actionable errors** — When someone violates a guardrail, failures should **name the rule**, **link to remediation**, and **suggest** the golden path—reducing trial-and-error toil.
- **Human path when needed** — Complex or high-risk changes still use **review** or **consultation**; self-service is the **default**, not a ban on judgment.

---

## 4. Service Catalog (System Of Record)

A **service catalog** is the **searchable index of systems** the organisation runs—not necessarily a separate product. Minimum useful **metadata** per service (or per bounded context) should answer “what is this, who owns it, what does it touch?”:

| Dimension | Examples (illustrative) |
| --- | --- |
| **Identity** | Name, short description, **tier** / criticality |
| **Ownership** | Team, escalation channel, on-call or equivalent |
| **Interfaces** | HTTP APIs, **event types** produced/consumed—**links** to `contracts/` or equivalent |
| **Runtime** | Managed platform vs cluster; region; aligns with [container-runtime-choice.md](../principles/container-runtime-choice.md) and estate catalogue |
| **Data** | Primary stores; sensitivity / PII notes per [privacy-and-data-governance.md](../principles/privacy-and-data-governance.md) |
| **Dependencies** | Upstream/downstream services or integrations |
| **Operations** | SLOs or criticality, **runbooks**, dashboards—per [documentation-knowledge.md](../principles/documentation-knowledge.md) |
| **Lifecycle** | Deploy model, deprecation / sunset status |

**Why:** Incidents, audits, and refactors all start with **graph and ownership**. Without a catalog (even a thin Git-maintained index), teams rediscover dependencies under pressure.

---

## 5. Scorecards And Health Signals

- Prefer a **small** set of **outcome-linked** signals: merge-path health, dependency freshness, incident rate, SLO burn, golden-path **failure** rate—not vanity counts.
- Reuse org **governance** mechanics where they exist: waiver/expiry discipline from [engineering-controls-governance-program.md](engineering-controls-governance-program.md); evidence expectations from merge-path principles.
- Avoid **individual** productivity theatre; team-level and **system** health align better with DORA and SPACE ([measurement-and-dora.md](../principles/measurement-and-dora.md)).

---

## 6. Exceptions And Drift

- **Recorded exceptions** — When a team **cannot** use the golden path, capture **reason**, **reviewer**, and **expiry or trigger to revisit** (ADR, risk register, or governance waiver—match your org).
- **No silent snowflakes** — Undocumented divergence becomes **unpatchable** debt and invalidates shared guardrails.
- **Re-absorb** — Periodically fold repeated exceptions into the **path** (new template, new policy parameter) so the platform learns.

---

## 7. Adoption Staging (Typical)

| Stage | Focus |
| --- | --- |
| **Early** | One **blessed** repo template + documented build/deploy path; README ownership; optional single markdown **index** of services |
| **Growing** | Catalog fields populated for **new** services; CI templates; enforced merge gates; runbook links mandatory for tier-1 |
| **Mature** | Broad self-service with policy enforcement; scorecards; exception workflow; platform roadmap tied to metrics |

[adoption-playbook.md](adoption-playbook.md) sequences team migration; this pattern describes **what “good” looks like** for the enabling layer that multiple teams consume.

---

## Checklist Touchpoint

Multi-team platform adoption: add rows from [checklists/platform-readiness.md](../checklists/platform-readiness.md) and the catalog/golden-path row in the same file.
