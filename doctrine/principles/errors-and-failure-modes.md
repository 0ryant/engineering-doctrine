# Errors And Failure Modes (APIs, CLIs, Operators)

Durable rules for predictable failures: what users see, what operators log, and how retries behave. Complements [api-boundaries-and-security.md](api-boundaries-and-security.md) (HTTP) and Core Proposition 6 (Design Failure, Retry, Recovery, And Reconciliation) in `ENGINEERING.md`.

---

## 1. Machine-Readable Errors At Boundaries

- **HTTP APIs** — stable problem types (for example [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html) Problem Details) with actionable messages for clients; no stack traces in production responses unless a documented debug mode.
- **Events and webhooks** — distinguish retryable vs permanent failures in consumer handling; align with [patterns/message-channel-operations.md](../patterns/message-channel-operations.md).

**Why:** Clients and automation need stable discrimination; humans need context in logs, not in every JSON body.

---

## 2. CLIs And Desktop Tools

- **Exit codes** — document meaning (`0` success, distinct non-zero for usage vs internal error); avoid reusing one code for all failures.
- Stderr for errors; stdout for machine-consumable output when scripts parse results.
- Operator detail (correlation id, remediation hint) may appear on stderr or structured log—match [audit-logging.md](audit-logging.md) for sensitive ops.

**Why:** Scriptability and supportability depend on consistent CLI contracts (POSIX expectations and common CLI practice).

---

## 3. Retries And Idempotency

- Document which operations are safe to retry. Where duplicate user-triggered mutation could be costly, enforce an idempotency, duplicate-detection, conditional-transition, or first-outcome strategy at the controlling HTTP boundary; an idempotency key is one common mechanism. See [idempotency-across-boundaries.md](../patterns/idempotency-across-boundaries.md).

For messages and events, duplicate handling is owned by [idempotency-across-boundaries.md](../patterns/idempotency-across-boundaries.md) §3 and [message-channel-operations.md](../patterns/message-channel-operations.md).

**Why:** At-least-once networks make duplicate submits inevitable without explicit design.

---

## 4. Timeouts, Retries, And Overload

**Applicability:** production services that call, or are called by, other services over a network. Each rule is a **SHOULD** ([ADR 0059](../../docs/adr/0059-apply-three-constitution-rules-to-settled-inconsistencies.md)).

- **Every remote call has a timeout.** No call waits without bound or on a library default nobody chose. Where the protocol carries a deadline, pass the remaining time downstream, so a callee stops work its caller has given up on.
- **Retry only what can succeed.** Retry transient failures. Do not retry permanent errors or malformed requests, and retry a call with side effects only where duplicate handling exists (§3).
- **Bound and spread retries.** Cap attempts per request, wait longer between attempts using exponential backoff with jitter, and limit the share of traffic that may be retries.
- **Retry at one layer.** Retries at several layers multiply against the lowest one. Choose the layer; the others fail fast and report why.
- **Stop calling what keeps failing.** After repeated failure, stop sending requests to that dependency for a period and probe before resuming (circuit breaking).
- **Shed load before saturating.** A service bounds its concurrent work and queue length, rejects the excess early and cheaply, and returns a distinct overload response so callers back off.

What the caller does while a dependency is unavailable (fail, serve stale, reduce the feature, or hand to a person) is chosen in advance. [reliability-slo-incidents.md](reliability-slo-incidents.md) §7 owns that choice for third-party dependencies in critical journeys.

**Why:** Unbounded waits and retries turn one slow dependency into a wider outage. Callers hold resources for answers they no longer need, and every layer that retries multiplies the load on the layer already failing.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Split user vs operator detail | Prevents information leakage while preserving debuggability. |
| CLI as contract | CLIs are APIs for scripts; treat them with the same rigour as HTTP. |
| Timeouts, retries, and overload stated here | Core Proposition 6 names timeouts and partial-failure behaviour, and reliability §7 pointed here for them; before ADR 0059 this file held neither. |

---

## References

- IETF RFC 9457 — Problem Details for HTTP APIs: https://www.rfc-editor.org/rfc/rfc9457.html  
- OWASP API Security — consistent error handling (avoid verbose errors): https://owasp.org/API-Security/editions/2023/en/0x11-t10/  
- POSIX exit status conventions: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_08  
- Google SRE Book — **Addressing Cascading Failures** (ch. 22; deadlines and deadline propagation, randomised exponential backoff, retry limits and budgets, retries at one level, load shedding) (S4; accessed 2026-11-18): https://sre.google/sre-book/addressing-cascading-failures/  
- Google SRE Book — **Handling Overload** (ch. 21; per-request and per-client retry budgets, retry only at the layer above) (S4; accessed 2026-11-18): https://sre.google/sre-book/handling-overload/  
- AWS Well-Architected Framework — **REL05** (throttle requests, control and limit retries, fail fast and limit queues, set client timeouts) (S5; accessed 2026-11-18): https://docs.aws.amazon.com/wellarchitected/latest/framework/rel05.html  
- Marc Brooker — **Timeouts, retries, and backoff with jitter** (Amazon Builders' Library, 2019; S6, vendor engineering; accessed 2026-11-18): https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/  
- Azure Architecture Center — **Retry pattern** (transient faults only, nested retries, hand-off to a circuit breaker) (S5; accessed 2026-11-18): https://learn.microsoft.com/en-us/azure/architecture/patterns/retry  
- gRPC — **Deadlines** (no deadline by default; always set one; propagation) (S5, product-scoped; accessed 2026-11-18): https://grpc.io/docs/guides/deadlines/  
