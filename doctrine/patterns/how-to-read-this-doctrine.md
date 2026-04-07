# How To Read This Doctrine

Use this page when onboarding to the repository or deciding **what to adopt** in another org.

---

## Layers (Outermost To Innermost)

1. **`ENGINEERING.md`** (repo root) — **Umbrella** summary: the full list of headline principles and pointers. It can lag slightly; if in doubt, the **`doctrine/principles/`** file wins for detail.
2. **`doctrine/principles/`** — **Timeless** rules: platform-agnostic, with **rationale** and **references** per topic. Prefer citing these when embedding doctrine in another repo.
3. **`doctrine/patterns/`** — **Compositional** guidance: how build surfaces, trunk workflow, message operations, and similar ideas fit together. Not every pattern applies to every repo.
4. **`doctrine/tooling/`** — **Illustrative** stacks (task runners, CI mapping, bots). Swap freely; keep **surface meanings** from `principles/build.md`.
5. **`doctrine/tooling/estates/`** — **Optional** vendor/cloud notes (example: Azure). Never copy estate content into portable principles without generalising.

Meta-rule: **[principles/timeless-principles-and-tooling.md](../principles/timeless-principles-and-tooling.md)** explains why the split exists.

---

## Suggested Reading Order

| Audience | Path |
| --- | --- |
| **New org adopting wholesale** | `timeless-principles-and-tooling` → `build` → `collaboration` → `ENGINEERING.md` |
| **Platform / SRE** | `observability` → `reliability-slo-incidents` → `data-and-migrations` → `platform-readiness` checklist |
| **Security / API** | `api-boundaries-and-security` → `threat-modeling-stride-lite` → `ENGINEERING.md` §18 (extended principles) → `dependencies-supply-chain` |
| **Async / events** | `event-contracts` → `state-machines-and-workflows` → `message-channel-operations` → `tooling/cloudevents.md` (optional `tooling/nats-jetstream`) |

---

## Resolving Apparent Conflicts

- If **`ENGINEERING.md`** and a **principle file** disagree on detail, treat the **principle** as authoritative and propose an **ENGINEERING** edit.
- If **two principle files** seem to overlap (for example security vs API), apply the **stricter** consumer-facing requirement and open a PR to cross-link both.

---

## Checklists

- Repo rollout: `checklists/build-readiness.md`, `collaboration-readiness.md`, `platform-readiness.md`.
- **Releases:** `checklists/release-readiness.md`.
- **Editing this library:** `checklists/doctrine-change-checklist.md`.
- **Adopting with a team:** `patterns/adoption-playbook.md`, `tooling/estates/minimum-viable-doctrine.template.md`, `principles/measurement-and-dora.md`.
