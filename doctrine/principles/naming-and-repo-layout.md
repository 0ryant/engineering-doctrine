# Naming And Repository Layout

Durable rules for **consistent** names and **discoverable** structure so contributors and automation find the right surface quickly. Deepens umbrella **Naming And Project Structure Conventions** in `ENGINEERING.md`.

---

## 1. Predictable Layout

- **Contracts** live under an agreed tree (for example `contracts/`, `api/`, `schemas/`) with **schemas** and **examples** adjacent.
- **Tests** mirror source structure or use a single top-level `tests/` convention—**document** which pattern the repo uses.
- **Tooling** entrypoints (`scripts/`, task runner files) are **named** in README and match CI invocation.

**Why:** *Software Engineering at Google* and similar guides stress **discoverability**; ad-hoc layout raises onboarding cost and breaks path filters.

---

## 2. Naming Conventions

- **Packages and modules** use ecosystem norms (Rust crates, npm scopes, Python namespaces); avoid **clever** abbreviations shared across org boundaries.
- **Resources** in IaC and cloud use **consistent** prefixes: environment, service, component—support **cost** and **ownership** tags (see [performance-and-cost.md](performance-and-cost.md)).

---

## 3. Monorepo Vs Polyrepo

- **Monorepos** — shared build tooling and atomic refactors; require explicit **ownership** boundaries (CODEOWNERS, path rules) to avoid silent coupling.
- **Polyrepos** — clear **version** contracts between repos; publish and consume **semver** honestly per [semantic-versioning.md](semantic-versioning.md).

**Why:** Layout follows **organisational** boundary choice; neither layout is universally superior.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Convention over novelty | Reduces **cognitive load** in incident response and code review. |
| Document exceptions | Legacy paths are fine if **called out** in README. |

---

## References

- *Software Engineering at Google* — **Version control and branch management** (structure at scale): https://abseil.io/resources/swe-book  
- GitHub — **CODEOWNERS** (ownership at path level): https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners  
