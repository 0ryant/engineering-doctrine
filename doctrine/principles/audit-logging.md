# Audit Logging

Durable rules for **append-only**, **structured** records of **security- and compliance-relevant** actions. Complements umbrella **Audit Everything** in `ENGINEERING.md` and [privacy-and-data-governance.md](privacy-and-data-governance.md) (retention, PII, separation from product analytics).

---

## 1. Minimum Fields

Per high-value operations, capture at least:

- **Who** — actor identity (user id, service principal, API client id).
- **What** — operation name and **resource** identifier (stable id, not only display name).
- **When** — UTC timestamp with agreed precision.
- **Outcome** — success / failure; **reason** or error **code** on failure without leaking secrets.
- **Correlation** — request id or trace id where available for cross-service investigation.

**Why:** Fields align with common **audit** and **forensics** expectations; missing dimensions make post-incident timelines unreconstructable. NIST SSDF **RV** practices include **identifying** and **responding** to vulnerabilities—audit trails support that response.

---

## 2. Integrity And Immutability

- Treat audit streams as **append-only** from the application’s perspective; **tamper** protection (WORM storage, hash chaining, central SIEM) is an **estate** decision—document it.
- **Do not** embed **secret values** or **decryptable** sensitive payloads in audit entries; use **references** and **hashes** where needed (see [event-contracts.md](event-contracts.md) on sensitive fields).

**Why:** Mutable logs destroy **non-repudiation**; over-collection increases **breach** and **privacy** impact.

---

## 3. Retention And Access

- **Retention** per legal and product policy; **shorter** than cold storage backups where regulation requires minimisation.
- **Access** to audit logs is **least privilege** and itself **logged** where platforms allow.

**Why:** [privacy-and-data-governance.md](privacy-and-data-governance.md) separates **audit** from **analytics**; retention must be **explicit**, not “forever by default.”

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Structured (JSON/JSONL) | Enables **query** and **correlation** at scale vs unstructured prose. |
| Failures recorded | Failed auth and denied authz are often **higher signal** than successes. |

---

## References

- NIST **SP 800-218** (SSDF) — **Respond to vulnerabilities** (RV) and organisational logging expectations: https://csrc.nist.gov/publications/detail/sp/800-218/final  
- OWASP **Logging** Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html  
- CloudEvents (for **event-shaped** audit export at boundaries): https://github.com/cloudevents/spec  
