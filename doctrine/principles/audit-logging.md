# Audit Logging

Durable rules for **protected**, **structured** records of actions that require accountable reconstruction. Formal audit evidence is distinct from operational logs, metrics, traces, business transaction history, and event sourcing. Complements [privacy-and-data-governance.md](privacy-and-data-governance.md) (retention, PII, controlled data, separation from product analytics) and [Revision-Pinned External Control Profiles](../patterns/revision-pinned-control-profiles.md) (authority, revision, boundary, assessment evidence, exceptions).

---

## 1. Applicability And Event Selection

- Produce durable audit evidence for **privileged**, **security-sensitive**, **policy-relevant**, **financially material**, and **externally consequential** actions, and wherever law, contract, regulation, or an adopted control profile requires it.
- Select events and detail from the threat model, materiality, accountability need, and governing authority. Record both allowed and denied attempts where either is material to investigation or control evidence.
- Ordinary internal state transitions may need operational logs, metrics, traces, or domain history rather than a formal audit record. Do not turn every mutation into an audit event without a stated purpose.
- Keep security-event, audit, transaction, and operational records separate when their access, retention, integrity, or consumers differ; correlate them through stable identifiers instead of forcing them into one stream.

**Why:** OWASP distinguishes security-event logging from process, audit, and transaction trails and warns against logging either too much or too little. Purpose and materiality determine the evidence required.

---

## 2. Minimum Fields

For each in-scope audit event, capture at least:

- **Who** — actor identity (user id, service principal, API client id).
- **What** — operation name and **resource** identifier (stable id, not only display name).
- **When** — UTC timestamp with agreed precision.
- **Outcome** — success / failure; **reason** or error **code** on failure without leaking secrets.
- **Correlation** — request id or trace id where available for cross-service investigation.

**Why:** These dimensions support accountability, timeline reconstruction, and correlation with security-event and operational evidence. A missing actor, action, time, or disposition materially limits investigation.

---

## 3. Integrity And Immutability

- Treat audit streams as **append-only** from the application’s perspective. Select tamper protection and independent retention proportionate to the event and any governing profile; a storage mechanism is not portable doctrine by itself.
- **Do not** embed **secret values** or **decryptable** sensitive payloads in audit entries; use **references** and **hashes** where needed (see [event-contracts.md](event-contracts.md) on sensitive fields).

**Why:** Uncontrolled mutation undermines forensic and accountability value; over-collection increases **breach**, privacy, and operating impact. Logs can assist non-repudiation controls but do not establish non-repudiation by themselves.

---

## 4. Retention And Access

- **Retention** per legal and product policy; **shorter** than cold storage backups where regulation requires minimisation.
- **Access** to audit logs is **least privilege** and itself **logged** where platforms allow.
- For a declared external control profile, retain the profile/revision, scoped system or component, evidence period, actor/assessor identity, assessment or control result, and exception reference without duplicating protected payloads unnecessarily.

**Why:** [privacy-and-data-governance.md](privacy-and-data-governance.md) separates **audit** from **analytics**; retention must be **explicit**, not “forever by default.”

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Structured, machine-readable records | Enable **query**, validation, and correlation without mandating one serialization. |
| Failures recorded | Failed auth and denied authz are often **higher signal** than successes. |
| Purpose-scoped event selection | Preserves material accountability without treating telemetry volume as assurance. |

---

## References

- NIST **SP 800-53 Rev. 5** — Audit and Accountability (**AU**) control family: https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final
- OWASP **Logging** Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html
- CloudEvents (an optional envelope for **event-shaped** audit export at boundaries): https://github.com/cloudevents/spec
