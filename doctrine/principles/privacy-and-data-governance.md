# Privacy And Data Governance

Durable rules for **personal data**, **retention**, and **separation of concerns** between product telemetry and security or compliance records.

---

## 1. Data Minimisation

- Collect and store **only** what the product and legal basis require.
- Prefer **identifiers** that can be **revoked or rotated** over long-lived durable secrets in application logs.

**Why:** GDPR and similar regimes emphasise **purpose limitation** and **minimisation**; excess data increases breach impact and operational burden.

---

## 2. Retention And Deletion

- **Retention periods** are explicit per data category (account data, logs, analytics, backups).
- **Deletion** paths (user offboarding, legal erasure requests) are **tested** where feasible—not only documented.

**Why:** “Keep everything” conflicts with cost and legal exposure; deletion bugs are **compliance** incidents.

---

## 3. Residency And Subprocessors

- **Data residency** constraints (region, cloud) are **architecture inputs**, not post-hoc labels.
- **Subprocessors** and **cross-border** transfers follow legal review and customer contracts.

**Why:** Moving data across regions after build-out is expensive; mistakes become contractual breaches.

---

## 4. Separate Product Analytics From Security Audit

- **Security audit logs** (who did what) have different access controls and retention than **product analytics**.
- Do not ship **PII** to analytics pipelines without review and **contractual** basis.

**Why:** Mixing streams causes **over-collection** and confused access patterns during incidents.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Minimise by default | Reduces **blast radius** of breaches and simplifies **DSAR** / erasure. |
| Explicit retention | Makes cost and compliance **measurable**; avoids silent infinite growth. |
| Split audit vs analytics | **Least privilege** and clearer incident handling. |

---

## References

- ICO (UK) overview of **data minimisation** (principle): https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/principles/data-minimisation/  
- GDPR **Article 5** principles (lawful basis, minimisation, storage limitation): official EUR-Lex text for EU law.  
- NIST **Privacy Framework** (organisational privacy risk): https://www.nist.gov/privacy-framework  
