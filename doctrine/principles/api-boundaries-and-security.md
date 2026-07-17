# API Boundaries, HTTP Semantics, And API Security

Durable rules for **externally exposed** HTTP and RPC surfaces: predictable behaviour under load, **abuse resistance**, and alignment with common **API security** failure modes.

---

## OWASP API Security Top 10 (2023) — Cross-Reference

Portable controls in this file map to the **OWASP API Security Top 10 (2023)**. Use this table in **reviews** and **threat modeling** so no category is silently ignored.

| ID | Risk (title) | Primary controls in this document |
| --- | --- | --- |
| **API1** | Broken object level authorisation (BOLA / IDOR) | §2 authenticate + **object-level** checks on **every** ID |
| **API2** | Broken authentication | §2–3; strong session/token handling; rate limits on auth paths |
| **API3** | Broken object property level authorisation (mass assignment / BOPLA) | §2 expose **allowlists** for writable fields; never bind client JSON straight to domain models without filtering |
| **API4** | Unrestricted resource consumption | §1 size/time limits; §3 rate limits; §5 GraphQL cost/depth |
| **API5** | Broken function level authorisation | §2 enforce **role/claim** per **route and method**, not only “logged in” |
| **API6** | Unrestricted access to sensitive business flows | §3 **stricter** limits and **step-up** for transfers, admin, bulk export |
| **API7** | Server side request forgery (SSRF) | §8 URL validation, allowlists, network controls for **outbound** fetches |
| **API8** | Security misconfiguration | §1 error model; §6 headers; disable **debug**, default **secure** stack, patch defaults |
| **API9** | Improper inventory management | **OpenAPI** (or equivalent) as **live** inventory; deprecate old versions per [semantic-versioning.md](semantic-versioning.md) §6–9 |
| **API10** | Unsafe consumption of APIs | §9 treat **outbound** calls like **untrusted** ingress; timeouts, schema validation, no blind relay |

Official overview: https://owasp.org/API-Security/editions/2023/en/0x11-t10/

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

### 2.1 Cryptographic Choices At Boundaries

- Use platform-approved, authenticated cryptography through maintained libraries, cryptographic modules, or managed services; do not design custom cryptographic algorithms or protocols.
- Bind algorithm suites, key sizes, key lifecycle, password-storage parameters, and transition dates to the applicable threat model and maintained security or external-control profile. A portable principle does not freeze one short algorithm menu for every platform and jurisdiction.
- Select the layer for encryption—application, database, filesystem, hardware, or managed service—from the threat model and governing authority. Record which threats the selected layer does and does not address.
- Treat password hashing as a distinct purpose from deriving or protecting encryption keys. Follow the active password-storage profile and migration path; do not reuse a legacy password hash merely because it is available.

**Why:** Cryptographic suitability changes with purpose, implementation quality, platform support, external approval, and transition guidance. Maintained profiles allow algorithms and parameters to change without inventing application-specific cryptography.

---

## 3. Rate Limiting And Abuse

- Apply **rate limits** and **quotas** per client identity (API key, user, tenant) where possible — not **only** by IP.
- **Stricter** limits on authentication, password reset, and OTP endpoints than on read-only catalogue APIs.

**Why:** OWASP **API2** (broken authentication) and **API4** (resource consumption) both reference brute force and overload patterns; **API6** covers abuse of sensitive **business flows**.

---

## 4. Idempotency And Retries

- **Mutating** endpoints that clients may retry, or whose response may be lost, declare an idempotency, duplicate-detection, or recovery strategy. Where a duplicate payment, allocation, or external action could cause material harm, enforce the strategy at the controlling boundary. See [idempotency-across-boundaries.md](../patterns/idempotency-across-boundaries.md).

**Why:** At-least-once networks and clients make **duplicate submits** inevitable; APIs must be explicit about safe retry.

---

## 5. GraphQL And Complex Queries

If GraphQL (or similar) is exposed, treat **query planning** as part of the **security** and **capacity** boundary—not only a feature.

- **Depth limit** — cap **maximum field nesting** (typical starting range **5–10** levels; **lower** for public internet). Reject deeper queries with a **stable** error code.
- **Complexity / cost score** — assign **weights** to fields (especially lists, unions, and expensive resolvers); reject queries above a **server-wide** budget per request (tune from baseline: e.g. **1000–5000** arbitrary cost units for **read** APIs—**measure** and adjust). Prefer **per-client** or **per-user** budgets for **multi-tenant** APIs.
- **Pagination** — list fields return **cursor** or **offset** pages with **max page size**; **no** unbounded `users { ... }` without limits.
- **Batching / DataLoader** — use deliberate **N+1** controls; **timeouts** on the whole request (e.g. **2–30 s** at the gateway depending on product) and **per-field** timeouts where the runtime supports them.
- **Introspection** — **disable** or **restrict** in production for **public** APIs unless you accept **schema** disclosure risk.
- **Authz** — resolvers enforce **object-level** checks; **global** middleware is not enough (BOLA applies **per** node).

**Why:** OWASP **API4** and the **GraphQL cheat sheet** describe **complexity** and **batching** abuse; without numeric guardrails, one query can **DoS** the service.

---

## 6. Browser-Facing Controls (CSP, CORS)

- **Content Security Policy (CSP)** — restrict **script**, **connect**, and **frame** sources for web apps that render **user** or **third-party** content; iterate toward **strict** policies without breaking legitimate integrations.
- **CORS** — treat `Access-Control-Allow-Origin: *` paired with **credentials** as a **code smell**; prefer **explicit** origins for **authenticated** APIs.
- **Cookies** — `SameSite`, `Secure`, and **HttpOnly** defaults for **session** security; align with OWASP **Session Management** cheat sheet.

**Why:** OWASP **ASVS** and cheat sheets frame CSP/CORS as **defence in depth** against XSS and **cross-origin** data theft—not substitutes for **server-side** authz.

---

## 7. Service-To-Service mTLS

- For **internal** east-west traffic, prefer **mutual TLS** or **workload identity** (SPIFFE/SPIRE, mesh, or platform feature) so **caller** identity is **cryptographic**, not only network placement.
- **Public** HTTP APIs typically remain **TLS + OAuth/OIDC**; mTLS is usually **internal** mesh or **B2B** integration.

**Why:** NIST **Zero Trust** (SP 800-207) expects **continuous** verification; mTLS is one **mature** pattern for service identity—see [zero-trust-and-workload-identity.md](zero-trust-and-workload-identity.md).

---

## 8. SSRF And Server-Initiated HTTP

**API7** — Any endpoint or job that **fetches** a URL supplied by users or **untrusted** integrations is an **SSRF** surface.

- **Allowlist** hosts/schemes where possible; **block** cloud metadata addresses (`169.254.169.254`, `fd00:ec2::`) and **RFC1918** / **link-local** targets from **public** callers unless explicitly required and **network-segmented**.
- **Do not** follow redirects blindly; cap **response** size and **timeouts**; log **denied** attempts.
- Prefer **dedicated** egress proxies or **service mesh** egress policy for **outbound** calls from backends.

**Why:** SSRF turns a small **feature** (“preview this URL”) into **internal** network access.

---

## 9. Inventory, Misconfiguration, And Outbound API Consumption

**API8 / API9 / API10** — **Configuration** drift, **unknown** endpoints, and **trusting** third-party APIs **without** validation.

- **Inventory:** publish **OpenAPI** (or equivalent) for **every** public major version; **sunset** old paths on a **calendar**; avoid **undocumented** admin routes on the same host as **public** API.
- **Misconfiguration:** default **deny**, **disable** verbose errors in prod, **security** headers at edge (see §6), **dependency** and **container** baselines per [dependencies-supply-chain.md](dependencies-supply-chain.md) and [kubernetes-platform-security.md](kubernetes-platform-security.md) where applicable.
- **Outbound consumption:** validate **responses** against **expected** schema where feasible; **timeouts** and **circuit breakers**; for **webhooks you call**, same discipline as [../patterns/webhook-ingress-security.md](../patterns/webhook-ingress-security.md) in reverse—**you** are the client.

**Why:** APIs are a **system**—unknown routes and **implicit** trust of remote JSON cause **incident** classes that BOLA checks alone will not catch.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Align with OWASP API Top 10 | Industry **checklist** for API-specific flaws; maps to concrete code review items. |
| Limits everywhere by default | **Fail closed** on size, time, and rate — matches security baseline in `ENGINEERING.md`. |
| Object-level auth | Prevents **IDOR**-class bugs that auth tokens alone cannot fix. |
| CSP + CORS explicit | Reduces **XSS** and **origin** confusion on browser clients. |
| GraphQL numeric guardrails | **Depth/cost** limits make abuse **testable**; introspection policy is explicit. |
| OWASP Top 10 table | Makes **review** and **audit** questions answerable from one map. |
| SSRF §8 | **URL fetch** features are **always** in scope for security review. |
| Inventory + outbound §9 | **API9/API10** are **operational** discipline, not only code bugs. |

---

## Related

- Architecture-level threat pass (trust boundaries): [threat-modeling-stride-lite.md](threat-modeling-stride-lite.md)
- **LLM / RAG / agents** — portable governance and tiered obligations: [ai-ml-systems.md](ai-ml-systems.md). **Retrieval** (tenant isolation, indirect injection via documents, cached context) and **tool** calls (SSRF-class fetches) still map to **this** file’s HTTP/RPC boundaries. Baseline: [../patterns/rag-retrieval-baseline.md](../patterns/rag-retrieval-baseline.md); OWASP **LLM** list: https://genai.owasp.org/llm-top-10/

---

## References

- OWASP **API Security Top 10 (2023)** overview: https://owasp.org/API-Security/editions/2023/en/0x11-t10/  
- OWASP **API2:2023 Broken Authentication**: https://owasp.org/API-Security/editions/2023/en/0xa2-broken-authentication/  
- OWASP **API4:2023 Unrestricted Resource Consumption**: https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/  
- OWASP **API1:2023 Broken Object Level Authorization**: https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/  
- OWASP **API3:2023 Broken Object Property Level Authorization**: https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/  
- OWASP **API5:2023 Broken Function Level Authorization**: https://owasp.org/API-Security/editions/2023/en/0xa5-broken-function-level-authorization/  
- OWASP **API6:2023 Unrestricted Access to Sensitive Business Flows**: https://owasp.org/API-Security/editions/2023/en/0xa6-unrestricted-access-to-sensitive-business-flows/  
- OWASP **API7:2023 Server Side Request Forgery**: https://owasp.org/API-Security/editions/2023/en/0xa7-server-side-request-forgery/  
- OWASP **API8:2023 Security Misconfiguration**: https://owasp.org/API-Security/editions/2023/en/0xa8-security-misconfiguration/  
- OWASP **API9:2023 Improper Inventory Management**: https://owasp.org/API-Security/editions/2023/en/0xa9-improper-inventory-management/  
- OWASP **API10:2023 Unsafe Consumption of APIs**: https://owasp.org/API-Security/editions/2023/en/0xaa-unsafe-consumption-of-apis/  
- IETF **RFC 9457** — Problem Details for HTTP APIs: https://www.rfc-editor.org/rfc/rfc9457.html  
- OWASP **Cheat Sheet Series** — **Content Security Policy**: https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html  
- OWASP **Cheat Sheet Series** — **REST Security** (CORS and related): https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html  
- OWASP **GraphQL Cheat Sheet**: https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html  
- OWASP **ASVS** (application verification, browser controls): https://owasp.org/www-project-application-security-verification-standard/  
- OWASP **Cryptographic Storage Cheat Sheet** (threat-modelled encryption layer, authenticated modes, key lifecycle): https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html
- OWASP **Password Storage Cheat Sheet** (password hashing is a separate purpose; legacy algorithm migration): https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html
- NIST **SP 800-131A** — transition guidance for cryptographic algorithms and key lengths: https://csrc.nist.gov/pubs/sp/800/131/a/r2/final
