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

## 5. Impact Assessments, Consent UX, And AI-Related Processing

- **DPIA / PIA** — when processing is likely to result in **high risk** to individuals (large-scale sensitive categories, systematic monitoring, automated decision-making with legal effects, **new** technologies), run a **Data Protection Impact Assessment** (or **Privacy Impact Assessment**) **before** go-live and **update** when processing changes materially.
- **Consent UX** — where **consent** is the lawful basis, make it **granular**, **withdrawable**, and **documented**; avoid **dark patterns** that obscure real choice.
- **AI / model training** — when **personal data** feeds **training**, evaluation, or **prompt** context, treat it as a **high-risk** processing change: minimisation, **retention** limits, and **vendor** DPAs. Map engineering tasks to **NIST SSDF** and the **SP 800-218A** community profile where your org adopts them (see [secure-development-lifecycle.md](secure-development-lifecycle.md)).

**Why:** ICO and EU supervisory guidance emphasise **accountability** and **proportionality**; AI systems amplify **re-identification** and **leakage** risks if training data is unconstrained.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Minimise by default | Reduces **blast radius** of breaches and simplifies **DSAR** / erasure. |
| Explicit retention | Makes cost and compliance **measurable**; avoids silent infinite growth. |
| Split audit vs analytics | **Least privilege** and clearer incident handling. |
| DPIA when high risk | **Accountability** expectation under GDPR-like regimes; avoids **surprise** supervisory questions. |

---

## References

- ICO (UK) overview of **data minimisation** (principle): https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/principles/data-minimisation/  
- GDPR **Article 5** principles (lawful basis, minimisation, storage limitation): official EUR-Lex text for EU law.  
- NIST **Privacy Framework** (organisational privacy risk): https://www.nist.gov/privacy-framework  
- ICO (UK) — **Data protection impact assessments (DPIAs)**: https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-lawful-basis/accountability-and-governance/data-protection-impact-assessments-dpias/  
- NIST **SP 800-218A** — SSDF community profile for **AI** systems (see SSDF project / news on csrc.nist.gov): https://csrc.nist.gov/Projects/ssdf  
