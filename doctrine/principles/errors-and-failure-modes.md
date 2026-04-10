# Errors And Failure Modes (APIs, CLIs, Operators)

Durable rules for **predictable** failures: what **users** see, what **operators** log, and how **retries** behave. Complements [api-boundaries-and-security.md](api-boundaries-and-security.md) (HTTP) and umbrella **Error Handling** in `ENGINEERING.md`.

---

## 1. Machine-Readable Errors At Boundaries

- **HTTP APIs** — stable **problem types** (for example [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html) Problem Details) with **actionable** messages for clients; **no** stack traces in production responses unless a documented debug mode.
- **Events and webhooks** — distinguish **retryable** vs **permanent** failures in consumer handling; align with [patterns/message-channel-operations.md](../patterns/message-channel-operations.md).

**Why:** Clients and automation need **stable** discrimination; humans need **context** in logs, not in every JSON body.

---

## 2. CLIs And Desktop Tools

- **Exit codes** — document meaning (`0` success, distinct non-zero for usage vs internal error); avoid reusing one code for all failures.
- **Stderr** for errors; **stdout** for machine-consumable output when scripts parse results.
- **Operator** detail (correlation id, remediation hint) may appear on stderr or structured log—match [audit-logging.md](audit-logging.md) for sensitive ops.

**Why:** Scriptability and supportability depend on **consistent** CLI contracts (POSIX expectations and common CLI practice).

---

## 3. Retries And Idempotency

- Document which operations are **safe to retry**; require **idempotency keys** for user-triggered mutating HTTP where duplicates are costly—see [patterns/idempotency-across-boundaries.md](../patterns/idempotency-across-boundaries.md).

**Why:** At-least-once networks make **duplicate** submits inevitable without explicit design.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Split user vs operator detail | Prevents **information leakage** while preserving **debuggability**. |
| CLI as contract | CLIs are **APIs** for scripts; treat them with the same rigour as HTTP. |

---

## References

- IETF **RFC 9457** — Problem Details for HTTP APIs: https://www.rfc-editor.org/rfc/rfc9457.html  
- OWASP **API Security** — consistent error handling (avoid verbose errors): https://owasp.org/API-Security/editions/2023/en/0x11-t10/  
- POSIX **exit status** conventions: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_08  
