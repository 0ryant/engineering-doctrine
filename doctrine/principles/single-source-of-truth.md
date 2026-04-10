# Single Source Of Truth (DRY With Judgment)

Durable rules for **one authoritative definition** of versions, schemas, and constants—without **harmful** abstraction. Implements umbrella **DRY** with explicit trade-offs.

---

## 1. Derive, Don’t Duplicate

- **Version strings**, **dependency pins**, and **schema identifiers** live in **one** manifest or module; consumers **import** or generate from that source.
- **Generated** code and docs (OpenAPI clients, migration stubs) must be **regenerated** from the canonical artefact in CI, not hand-edited.

**Why:** Drift between “copy A” and “copy B” causes **silent** contract breaks; automation makes **truth** mechanical.

---

## 2. Duplication Vs Wrong Abstraction

- **Copy** when two paths have **different** reasons to change; **abstract** only when invariants truly match.
- **Premature** shared libraries coupling unrelated products are harder to unwind than temporary duplication (see Sandi Metz, *The Wrong Abstraction*).

**Why:** Industry guidance (often summarised as “**prefer duplication over the wrong abstraction**”) prevents **mega-utils** that ossify multiple teams.

---

## 3. Config And Constants

- **Magic numbers** and environment-specific URLs belong next to **configuration** principles—see [configuration-and-secrets.md](configuration-and-secrets.md).
- **Feature** defaults that affect security must be **explicit** in code or config, not scattered literals.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Aligns with build surfaces | [build.md](build.md) “one quality gate” mirrors **one version truth**. |
| Allows tactical duplication | Prevents **coupling** unrelated bounded contexts. |

---

## References

- *The Twelve-Factor App* — **Dependencies** / explicit declaration: https://12factor.net/dependencies  
- Sandi Metz — *The Wrong Abstraction* (blog): https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction  
- *Software Engineering at Google* — **Build** and **dependency management** (single graph truth): https://abseil.io/resources/swe-book  
