# Testing Strategy

Durable rules for **automated test portfolios**: what to emphasise, how to avoid common failure modes, and how **contract** and **integration** tests fit the build model.

---

## 1. Test Pyramid (Rough Guide)

- **Many narrow, fast tests** — unit or small-scope tests that exercise logic with minimal I/O.
- **Some medium tests** — integration across a **few** real components (e.g. service + DB + fake external APIs).
- **Few full-system end-to-end tests** — slow, brittle, expensive; reserve for **critical journeys** and regressions that smaller tests cannot catch.

**Why:** Google’s *Software Engineering at Google* (Chapter 11) documents rough targets (~80% / 15% / 5%) and explains why **E2E-heavy** suites become slow and flaky. The **hourglass** anti-pattern (many unit + many E2E, few integration tests) hides integration bugs until late.

---

## 2. Contract Tests

- At service boundaries, validate **schemas and behaviour** with **consumer–provider contract tests** or **schema-based** checks in CI.
- **Events** follow the same idea: versioned payload schemas and fixtures validated in CI (aligned with `event-contracts.md`).

**Why:** Integration failures often show up as **contract drift**; catching drift pre-merge is cheaper than production discovery.

---

## 3. Flaky Tests

- **Flaky tests are defects** — fix, quarantine with an **owner and deadline**, or delete redundant coverage.
- Do not **silence** or **retry indefinitely** without owning the root cause.

**Why:** Flaky CI erodes trust; teams start ignoring red builds and real regressions slip through.

---

## 4. Risk-Based Depth

- Increase automated coverage for **high-blast-radius** areas: money movement, authentication, migrations, crypto, and data integrity.

**Why:** Uniform coverage targets waste effort on low-risk code while under-testing catastrophic paths.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Favour fast tests for most logic | **Short feedback loops** and cheaper CI. |
| Avoid E2E as the default hammer | E2E is **high cost per assertion** and often **nondeterministic**. |
| Contract tests at boundaries | Matches **contracts-first** engineering and reduces distributed surprises. |
| Zero tolerance for unowned flakiness | Protects **merge discipline** and signal quality. |

---

## References

- *Software Engineering at Google*, Chapter 11 — **Testing** (scope, pyramid, antipatterns): https://abseil.io/resources/swe-book/html/ch11.html  
- Google Testing Blog, **Fixing a Test Hourglass**: https://testing.googleblog.com/2020/11/fixing-a-test-hourglass.html  
- Google Testing Blog, **Just Say No to More End-to-End Tests** (Mike Wacker): https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html  
