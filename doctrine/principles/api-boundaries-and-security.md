# API Boundaries, HTTP Semantics, And API Security

Durable rules for **externally exposed** HTTP and RPC surfaces: predictable behaviour under load, **abuse resistance**, and alignment with common **API security** failure modes.

---

## 1. Operational HTTP Hygiene

- **Pagination** with **maximum page size**; reject unbounded list endpoints.
- **Request body size limits** and **timeouts** at the edge and service.
- **Consistent error model** — machine-readable errors (for example Problem Details `application/problem+json`) with stable **type** URIs where helpful; avoid leaking stack traces to clients.

**Why:** Unbounded requests are a **denial-of-service** and cost vector; OWASP API Security **API4:2023 Unrestricted Resource Consumption** explicitly calls out missing limits.

---

## 2. Authentication And Authorisation

- **Authenticate** every protected route; **authorise** per **object** and **function** (not only “logged in”).
- **BOLA/BOPLA** (broken object / property level authorisation) are top OWASP API risks — validate **every** ID against the caller’s scope.

**Why:** OWASP **API1** and **API3** (2023) emphasise authorisation at **object** and **property** level, not only gateway auth.

---

## 3. Rate Limiting And Abuse

- Apply **rate limits** and **quotas** per client identity (API key, user, tenant) where possible — not **only** by IP.
- **Stricter** limits on authentication, password reset, and OTP endpoints than on read-only catalogue APIs.

**Why:** OWASP **API2** (broken authentication) and **API4** (resource consumption) both reference brute force and overload patterns; **API6** covers abuse of sensitive **business flows**.

---

## 4. Idempotency And Retries

- **Mutating** endpoints that clients retry (payments, provisioning) accept **idempotency keys** or equivalent deduplication.

**Why:** At-least-once networks and clients make **duplicate submits** inevitable; APIs must be explicit about safe retry.

---

## 5. GraphQL And Complex Queries

- If GraphQL (or similar) is exposed, enforce **depth/complexity limits**, **timeouts**, and **query cost** controls.

**Why:** OWASP API4 discusses **query complexity** and batching attacks.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Align with OWASP API Top 10 | Industry **checklist** for API-specific flaws; maps to concrete code review items. |
| Limits everywhere by default | **Fail closed** on size, time, and rate — matches security baseline in `ENGINEERING.md`. |
| Object-level auth | Prevents **IDOR**-class bugs that auth tokens alone cannot fix. |

---

## Related

- Architecture-level threat pass (trust boundaries): [threat-modeling-stride-lite.md](threat-modeling-stride-lite.md)

---

## References

- OWASP **API Security Top 10 (2023)** overview: https://owasp.org/API-Security/editions/2023/en/0x11-t10/  
- OWASP **API2:2023 Broken Authentication**: https://owasp.org/API-Security/editions/2023/en/0xa2-broken-authentication/  
- OWASP **API4:2023 Unrestricted Resource Consumption**: https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/  
- IETF **RFC 9457** — Problem Details for HTTP APIs: https://www.rfc-editor.org/rfc/rfc9457.html  
