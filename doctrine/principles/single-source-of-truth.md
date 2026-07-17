# Authoritative Sources And Intentional Duplication

Durable rules for **one identified authority per concept**, explicit derivatives, and intentional replication—without turning “DRY” into mandatory centralisation or harmful abstraction.

---

## 1. One Authority Per Concept

- For each version, schema, policy, configuration value, or other shared concept, identify the authoritative record, its owner, and how conflicts are resolved. Two values that happen to be equal are not necessarily the same concept.
- Within an independently publishable unit, each **version string**, dependency-graph declaration, and schema identifier has one authoritative declaration; consumers import, resolve, or generate from it rather than maintaining competing definitions.
- **Generated** code and docs (OpenAPI clients, migration stubs) are traceable derivatives of the canonical artefact and are regenerated or reconciled by a declared process rather than silently hand-edited.

**Why:** Authority removes ambiguity. Centralising unrelated concepts merely because they share a value creates coupling and an unnecessary failure domain.

---

## 2. Intentional Replication And Derivatives

- Caches, read models, generated clients, indexes, denormalised data, and offline copies may intentionally replicate authoritative data. Declare the source, freshness or consistency expectation, reconciliation mechanism, and behaviour when the source is unavailable.
- A derivative does not become a second authority merely because it is easier to query. Corrections flow from the authority or through an explicit conflict-resolution process.
- Replication may be safer than synchronous central dependency when availability, latency, isolation, or ownership demands it. Measure drift and recovery instead of banning copies.

**Why:** “Single source” describes decision authority, not a requirement that every consumer make a live call to one global system.

---

## 3. Duplication Vs Wrong Abstraction

- **Copy** when two paths have **different** reasons to change; **abstract** only when invariants truly match.
- **Premature** shared libraries coupling unrelated products are harder to unwind than temporary duplication (see Sandi Metz, *The Wrong Abstraction*).

**Why:** Industry guidance (often summarised as “**prefer duplication over the wrong abstraction**”) prevents **mega-utils** that ossify multiple teams.

---

## 4. Config And Constants

- **Magic numbers** and environment-specific URLs belong next to **configuration** principles—see [configuration-and-secrets.md](configuration-and-secrets.md).
- **Feature** defaults that affect security must be **explicit** in code or config, not scattered literals.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Aligns with build surfaces | [build.md](build.md) “one quality gate” mirrors **one version truth**. |
| Allows tactical duplication | Prevents **coupling** unrelated bounded contexts. |
| Allows declared replication | Avoids turning an authority into a global runtime bottleneck or shared failure domain. |

---

## References

- *The Twelve-Factor App* — **Dependencies** / explicit declaration: https://12factor.net/dependencies  
- Sandi Metz — *The Wrong Abstraction* (blog): https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction  
- *Software Engineering at Google* — **Build** and **dependency management** (single graph truth): https://abseil.io/resources/swe-book  
