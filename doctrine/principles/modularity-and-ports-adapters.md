# Modularity, Ports, Adapters, And Layering

Durable rules for **replaceable** components, **explicit boundaries**, and **dependency direction** so systems stay testable and evolvable. Ports and adapters and layered architecture are strong patterns where their trade-offs fit; they are not a required four-layer shape for every system.

---

## 1. Ports And Adapters (When Applicable)

- Where domain or application rules need to outlive infrastructure choices, make the core depend on **abstractions** (ports) rather than database, HTTP-client, or broker implementations.
- **Adapters** implement ports for a technology and can be replaced without rewriting the protected rules.
- Domain logic **SHOULD** be separable from infrastructure I/O when that improves testability or replacement. I/O libraries remain appropriate when file, network, database, telemetry, or messaging access is their explicit responsibility.

**Why:** Alistair Cockburn’s **hexagonal architecture** and similar **ports-and-adapters** descriptions reduce “everything calls the ORM” coupling; see [Hexagonal architecture](https://alistair.cockburn.us/hexagonal-architecture/) (authoritative summary on author site).

---

## 2. Responsibility And Dependency Direction

- Give each module or layer a coherent responsibility and make boundary crossings explicit. A delivery/application/domain/infrastructure split is one useful shape, alongside vertical slices, pipelines, plugins, dataflow, functional cores, and bounded components.
- Declare and enforce dependency direction so stable policy does not depend accidentally on volatile infrastructure. “Inward” is meaningful only when the chosen architecture defines an inside and outside.
- Keep boundaries testable and coupling controlled; do not add layers that merely forward calls or duplicate types without protecting a real invariant.

**Why:** Dependency direction and explicit responsibility survive changes in architectural style; a fixed stack does not.

---

## 3. Coherent Evolution

- Preserve stable public contracts where compatibility matters. Extend or refactor existing modules when that produces the simpler coherent design; add a module or adapter when the behaviour has a genuinely separate responsibility or reason to change.
- **Feature flags** or **conditional compilation** beat long-lived forks for optional capabilities.

**Why:** Compatibility deserves protection, but extension-only accretion creates duplicate concepts, indirection, and permanent adapters. High-trust paths need stronger evidence for either refactoring or extension—not a blanket ban on modification.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Explicit ports | Makes **contract tests** and **fakes** natural at boundaries. |
| Aligns with build surfaces | [build.md](build.md) deployable units map cleanly to **bounded** components. |
| Architecture shape is contextual | The durable controls are responsibility, dependency direction, testability, and coupling. |

---

## References

- Alistair Cockburn — **Hexagonal architecture**: https://alistair.cockburn.us/hexagonal-architecture/  
- Robert C. Martin — **Clean Architecture** (book; dependency rule and use cases): widely cited for layered boundaries.  
- *Domain-Driven Design* (Eric Evans) — **bounded contexts** for large systems: complements ports/adapters at **team** scale.  
