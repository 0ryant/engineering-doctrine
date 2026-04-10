# Modularity, Ports, Adapters, And Layering

Durable rules for **replaceable** components, **explicit boundaries**, and **dependency direction** so systems stay testable and evolvable. Implements umbrella **Lego Extensibility** and **Layered Architecture** in depth.

---

## 1. Ports And Adapters (Hexagonal)

- **Domain / application core** depends on **abstractions** (ports)—not on databases, HTTP clients, or message brokers.
- **Adapters** implement ports for a given technology; they are **swapped** without rewriting core rules.
- **I/O at the edges** — file, network, clock, randomness injected or wrapped at boundaries for tests.

**Why:** Alistair Cockburn’s **hexagonal architecture** and similar **ports-and-adapters** descriptions reduce “everything calls the ORM” coupling; see [Hexagonal architecture](https://alistair.cockburn.us/hexagonal-architecture/) (authoritative summary on author site).

---

## 2. Layered Responsibility

- Each **layer** has one job: e.g. **delivery** (HTTP/CLI), **application** (use cases), **domain** (rules), **infrastructure** (persistence, messaging).
- **Dependencies point inward** — inner layers do not import outer layers’ concrete types.

**Why:** Matches the umbrella **layered architecture** sketch in `ENGINEERING.md` while staying **vendor-neutral**.

---

## 3. Extension Without Mutation

- **New behaviour** prefers **new modules** or **adapters** over editing stable core modules for unrelated features.
- **Feature flags** or **conditional compilation** beat long-lived forks for optional capabilities.

**Why:** Reduces merge conflict and regression risk on **high-trust** paths (money, auth, crypto).

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Explicit ports | Makes **contract tests** and **fakes** natural at boundaries. |
| Aligns with build surfaces | [build.md](build.md) deployable units map cleanly to **bounded** components. |

---

## References

- Alistair Cockburn — **Hexagonal architecture**: https://alistair.cockburn.us/hexagonal-architecture/  
- Robert C. Martin — **Clean Architecture** (book; dependency rule and use cases): widely cited for layered boundaries.  
- *Domain-Driven Design* (Eric Evans) — **bounded contexts** for large systems: complements ports/adapters at **team** scale.  
