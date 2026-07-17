# Testing Strategy

Durable rules for **behavioural evidence and regression protection**: what to emphasise, how to avoid common failure modes, and how **contract**, integration, and other tests fit the build model.

---

## Evidence-Driven Development

- Specify the behaviour, invariant, risk, or compatibility claim that a change must support, then choose evidence capable of discriminating success from failure.
- Preserve regression protection for accepted behaviour at a level proportionate to impact. Tests are a primary evidence source, but static analysis, schema validation, formal checks, benchmarks, review, and runtime observation may be required for different claims.
- **Test-driven development (TDD)** is a useful technique when executable examples and a fast feedback loop improve design. It is not a universal ordering rule: exploratory work, visual design, data science, integration investigation, performance work, and legacy remediation may establish evidence differently.
- A spike may defer durable regression coverage while it remains disposable and isolated. Code entering a controlled delivery path still needs the applicable behavioural and risk evidence before authorisation.

**Why:** The durable requirement is discriminating evidence and maintained regression protection, not whether every test was written before implementation.

---

## 1. Test Pyramid (Default Shape)

- **Many narrow, fast tests** — unit or small-scope tests that exercise logic with minimal I/O.
- **Some medium tests** — integration across a **few** real components (e.g. service + DB + fake external APIs).
- **Few full-system end-to-end tests** — slow, brittle, expensive; reserve for **critical journeys** and regressions that smaller tests cannot catch.

**Default portfolio targets** (for typical service repos with an HTTP or RPC API—**adjust** with a short ADR or team guide if you differ):

| Layer | Default share of tests (by **count**, rough) | Purpose |
| --- | --- | --- |
| **Fast** (unit / small) | **~70–85%** | Logic, edge cases, fast feedback |
| **Medium** (integration / contract) | **~10–25%** | Real wiring, schemas, DB semantics |
| **E2E** | **~1–5%** | Critical user or **money** paths only |

**Why:** *Software Engineering at Google* (Chapter 11) documents similar **order-of-magnitude** splits and explains why **E2E-heavy** suites become slow and flaky. The **hourglass** anti-pattern (many unit + many E2E, few integration tests) hides integration bugs until late. These numbers are a **starting bias**, not a religion—**violate** them deliberately, not by accident.

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

## 5. Adversarial CI And Negative-Security Testing

- Treat **abuse-case** and adversarial analysis as **complements** to the pyramid: they hunt **classes** of failures (authz bypass, unsafe data flow, secret exposure, **SSRF**, dependency confusion hints) that happy-path tests miss.
- **Pre-merge** — for **security-relevant** diffs (see [merge-path-evidence-and-pipeline-integrity.md](merge-path-evidence-and-pipeline-integrity.md) §2 invariant 8), run **scoped** adversarial or SAST-with-chaining checks on **changed** surfaces; failures are **defects** to fix or **policy** violations, not noise to silence.
- **Scheduled / broader** runs — full-repo or deeper passes catch **new** rule packs and **latent** issues; align cadence with estate risk.
- **Risk tiers (portable shape)** — **Tier 0** (privileged paths, pipeline definitions): blocking gate on every relevant change. **Tier 1** (internet-exposed or sensitive data): blocking on scoped changes. **Tier 2** (ordinary logic): recommended; may be non-blocking telemetry by policy. **Tier 3** (docs-only): typically out of scope.

**Why:** OWASP CI/CD risk work and SSDF **PS/PW** expect **flow control** and **well-secured** output; periodic pentests alone lose the race when disclosure-to-exploit timelines compress.

---

## 6. Mutation, Property-Based, And Accessibility Testing

- **Mutation testing** — optional gate for **high-risk** modules; surviving mutants highlight **weak** assertions (see *An Introduction to Mutation Testing* and tooling such as **Stryker**, **cargo-mutants**).
- **Property-based** tests — useful for parsers, codecs, state machines, and invariants that **example-based** tests miss; libraries such as **Hypothesis**, **QuickCheck**, **proptest** (ecosystem-specific).
- **Accessibility** — automated **a11y** linting in CI for web UIs where applicable; does not replace manual assistive-tech checks per [user-facing-quality.md](user-facing-quality.md).

**Why:** Google and industry experience show **coverage percentage** without **assertion quality** is misleading; WCAG-oriented automation catches **regressions** early.

---

## 7. Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Evidence before ideology | Behaviour and material risks need credible evidence; TDD is one technique for producing it. |
| Favour fast tests for most logic | **Short feedback loops** and cheaper CI. |
| Avoid E2E as the default hammer | E2E is **high cost per assertion** and often **nondeterministic**. |
| Contract tests at boundaries | Matches **contracts-first** engineering and reduces distributed surprises. |
| Zero tolerance for unowned flakiness | Protects **merge discipline** and signal quality. |
| Mutation/property optional | Raises **assertion quality** on parsers, codecs, and money paths where **coverage** alone lies. |
| Default pyramid percentages | Gives teams a **concrete** starting point; deviations require **explicit** rationale. |
| Adversarial CI named | Closes the gap between **functional** tests and **abuse** reality without mandating a vendor tool. |

---

## References

- *Software Engineering at Google*, Chapter 11 — **Testing** (scope, pyramid, antipatterns): https://abseil.io/resources/swe-book/html/ch11.html  
- Google Testing Blog, **Fixing a Test Hourglass**: https://testing.googleblog.com/2020/11/fixing-a-test-hourglass.html  
- Google Testing Blog, **Just Say No to More End-to-End Tests** (Mike Wacker): https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html  
- *An Introduction to Mutation Testing* (concept): https://mutationtesting.org/  
- Hypothesis (property-based testing, Python): https://hypothesis.readthedocs.io/  
- OWASP **Top 10 CI/CD Security Risks** (pipeline abuse, flow control): https://owasp.org/www-project-top-10-ci-cd-security-risks/  
