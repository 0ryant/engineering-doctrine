# Adoption Playbook (Team And Org Migration)

This library is a **reference**, not a single onboarding read. Use this pattern when moving a **team** (or org slice) from current practice toward the principles here—especially when **starting conditions** are far from the target (feature branches only, sparse tests, manual deploys, weak contracts).

Companion: [how-to-read-this-doctrine.md](how-to-read-this-doctrine.md), [../tooling/estates/minimum-viable-doctrine.template.md](../tooling/estates/minimum-viable-doctrine.template.md), [../principles/measurement-and-dora.md](../principles/measurement-and-dora.md).

---

## 1. Staging Reality

Doctrine succeeds when it reflects **observed** improvements and negotiable trade-offs, not only aspiration. Expect:

- **Disagreement** on specific principles; resolve with **evidence**, **pilots**, and **written exceptions**.
- **Stakeholder pressure** (“no time for contracts”)—counter with **risk** (production incidents, rework) and **smallest** contract slice (one boundary, one schema).
- **Legacy** that violates many rules at once—**sequence** work; don’t block all progress on total cleanup.

Solo-maintained doctrine that moves into a **multi-person** context needs **explicit** priorities (see minimum-viable doctrine template)—not all 20+ principle files on day one.

---

## 2. Reference Library Vs One-Pager

- **Full tree** — `doctrine/` for depth, audits, and evolving standards.
- **Team entry** — one **estate-specific** page ([minimum-viable-doctrine.template.md](../tooling/estates/minimum-viable-doctrine.template.md)): **5–7** principles tied to **this** team’s pain, each linking to the canonical principle file.

Hand new leaders the **one-pager first**; link the library for depth.

---

## 3. Suggested Adoption Order (Typical)

Order is **dependency-aware**, not dogmatic. Skip steps already healthy.

| Phase | Focus | Why first |
| --- | --- | --- |
| **1** | **Quality gate** — one command (or CI job) that fails on fmt/lint/tests for the **main** branch workflow | Creates safety to change process; mirrors [build.md](../principles/build.md) surfaces |
| **2** | **Trunk-oriented integration** — short-lived branches, PR review, green **main** | Reduces drift and batch risk; see [trunk-workflow.md](trunk-workflow.md), [collaboration.md](../principles/collaboration.md) |
| **3** | **Contracts at boundaries** — API or events: schemas + examples + CI validation where possible | Stops “tribal JSON”; [event-contracts.md](../principles/event-contracts.md), umbrellas in `ENGINEERING.md` |
| **4** | **Observability baseline** — correlated logs/traces for main paths; basic SLO thinking where user-facing | Makes incidents diagnosable; [observability.md](../principles/observability.md) |
| **5** | **Reliability habits** — incident severity, blameless reviews, error budget **policy** if SLOs exist | Ties delivery to risk; [reliability-slo-incidents.md](../principles/reliability-slo-incidents.md) |

Later phases often include supply-chain automation, broader platform readiness, threat modelling for exposed surfaces, and fuller checklists ([platform-readiness.md](../checklists/platform-readiness.md)).

---

## 4. Migration Recipes (Short)

**Feature branches + long review queues** — shorten branch lifetime caps; enforce **small** PRs; optional pairing to clear backlog. Document **why** trunk reduces merge pain (collaboration principle).

**Few tests** — add **characterization** tests around saves/refactors first; then contract tests at boundaries ([testing-strategy.md](../principles/testing-strategy.md)). Don’t mandate organisation-wide TDD day one; **gate** regressions.

**Manual deploys** — script one **repeatable** path; attach to CI artefact for **promotion** (same binary); see [build-surface-model.md](build-surface-model.md).

**No contracts** — pick **one** producer/consumer pair; CloudEvents + schema + CI validation; expand outward ([event-contracts.md](../principles/event-contracts.md)).

---

## 5. Team Size Heuristics

| Scale | Emphasis |
| --- | --- |
| **Small (e.g. ≤5 engineers)** | Thin process: quality gate + trunk + contracts on **shared** boundaries; skip heavy platform checklist until something ships to users |
| **Growing / multi-team** | Explicit **ownership** per service; platform readiness and SLO/error budgets; estate supplements for cloud choices |
| **Large / regulated** | Full checklists, audit trails, accessibility and privacy where UI/data warrant [user-facing-quality.md](../principles/user-facing-quality.md), [privacy-and-data-governance.md](../principles/privacy-and-data-governance.md) |

---

## 6. Measure Progress

Use **outcome** metrics, not checkbox counts—see [measurement-and-dora.md](../principles/measurement-and-dora.md). Improvement in deployment frequency and stability **validates** the playbook; doctrine text alone does not.

---

## References

- DORA / *Accelerate* — organisational performance correlates with technical practices: https://dora.dev/  
- Use checklists in `doctrine/checklists/` as **audits**, not replacements for team conversation.
