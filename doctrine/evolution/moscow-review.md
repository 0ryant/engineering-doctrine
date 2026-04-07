# Doctrine Audit: Thin Areas, Hard Review, And MoSCoW

**Date:** 2026-04-06 (maintenance snapshot).  
**Purpose:** Record where the library was **thin**, what a **skeptical** read surfaced, and how work was **prioritised**. Update this file when a major doctrine pass completes.

---

## Where Directories Were Thin

| Area | Before | Action |
| --- | --- | --- |
| `patterns/` | Only `build-surface-model` and `trunk-workflow` | Added **navigation** and **message-channel operations** patterns |
| `checklists/` | No meta-checklist for editing doctrine; no release-focused checklist | Added **doctrine-change** and **release-readiness** checklists |
| `evolution/` | Did not exist | Added this folder for **audit trail** and backlog |
| `tooling/estates/` | Only Azure; no scaffold for other estates | Added **TEMPLATE**; **AWS/GCP stubs** (no product picks until owners) |
| Threat modeling | Relied on API + supply-chain only | Added **STRIDE-lite** principle |
| Doctrine navigation | Manual file hunting | **SITEMAP.md** from `scripts/generate-doctrine-sitemap.sh` |
| `REFERENCES.md` internal map | Listed extended principles only; omitted core files | **Completed** the map |
| Event / queue **operations** | Contracts strong; **DLQ / replay / poison** thin | New pattern + pointer from `event-contracts.md` |
| Team **onboarding** | Full tree too large; no migration narrative | **`adoption-playbook.md`**, **MVD estate template**, **`measurement-and-dora.md`** |
| **Preference vs principle** blur | Language/container rows read as universal | **`timeless-principles` §5**, **`ENGINEERING` §6 note**, **§11 estate** wording |
| **A11y** depth vs headless repos | Thin + ambiguous scope | **`user-facing-quality` §0** + expanded §1 |
| External **review** signal | Chat-only | **`honest-review-synthesis.md`** |

---

## Hard-Nosed Review (Findings)

1. **Single mega-umbrella** — `ENGINEERING.md` is long; readers can miss deep principle files. **Mitigation:** explicit **how to read** pattern and README pointer.
2. **Navigability** — Internal reference index omitted **core** principles (`build`, `collaboration`, `event-contracts`, `semantic-versioning`, `timeless`). **Fixed** in `REFERENCES.md`.
3. **Residual prescriptiveness** — Container section still named `Dockerfile.build` / `Dockerfile.dev` as if universal. **Softened** to template-level naming.
4. **Async operations gap** — Event contracts covered **schema** and **semantics**; **operational** handling of bad messages was under-specified. **Closed** with `message-channel-operations.md`.
5. **Governance** — No checklist for **contributors** changing doctrine (drift risk). **Added** `doctrine-change-checklist.md`.
6. **Release discipline** — SemVer exists; **release checklist** not co-located with trunk/hotfix pattern. **Added** `release-readiness.md`.
7. **REFERENCES Kubernetes row** — Still pointed only at AKS for “cluster security.” **Generalised** to provider-agnostic entry.
8. **Deprecation** — SemVer described bumps; **sunset and notice period** for consumers was light. **Strengthened** in `semantic-versioning.md`.

---

## MoSCoW

### Must (done)

- Complete **internal doctrine map** in `REFERENCES.md`.
- **Navigation** aid (`patterns/how-to-read-this-doctrine.md`).
- **Message channel operations** pattern + link from `event-contracts.md`.
- **Doctrine change** checklist.
- **Release readiness** checklist.
- Soften **Dockerfile** naming prescriptiveness in `ENGINEERING.md`.
- **Deprecation** bullets in `semantic-versioning.md`.
- Generalise **K8s** reference line in `REFERENCES.md`.

### Should (done)

- **MoSCoW + audit** artefact in `evolution/moscow-review.md` (this file).
- **Estate TEMPLATE** for non-Azure clouds.
- Wire new artefacts into `doctrine/README.md`.

### Could (done)

- Dedicated short **threat-modeling** principle (STRIDE-lite) — `principles/threat-modeling-stride-lite.md`; cross-linked from API principle and platform checklist.
- **AWS / GCP** estate stubs with no product picks — `tooling/estates/aws-container-runtimes.md`, `gcp-container-runtimes.md`.
- Auto-generated **sitemap** — `scripts/generate-doctrine-sitemap.sh` writes `doctrine/SITEMAP.md`.

### Won’t (now)

- **Merging** all principles into one file — hurts modular adoption.
- **Binding** semver to a single package manager grammar — already generic per unit.

---

## Follow-Up

Re-run a skim **quarterly** or when adding a new principle domain: update this file’s thin-area table and MoSCoW **Could** / **Won’t** as appropriate.

**Post-review wiring (same maintenance pass):** `ENGINEERING.md` §18 and pointer block link how-to-read, message-channel ops, release and doctrine-change checklists, and this audit; `trunk-workflow.md` checklist touchpoints include release + message channels; `platform-readiness.md` and `build-readiness.md` include async/event and DLQ rows; `tooling/estates/README.md` links **TEMPLATE**; root `README.md` mentions `evolution/`.

**MoSCoW Could closure:** STRIDE-lite principle, AWS/GCP estate stubs, sitemap generator + `SITEMAP.md`, indexes and checklists updated per `doctrine-change-checklist.md`.
