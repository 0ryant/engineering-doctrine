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

These are **three** separable obligations; teams may comply with **one** without the others in a given release. Track each with its **own** owner and evidence.

### 5.1 DPIA / PIA Triggers (Assessment)

- **Must:** when processing is likely to result in **high risk** to individuals—examples include large-scale **special-category** data, **systematic monitoring** of public areas, **automated decision-making** with legal or similarly significant effects, or **new technologies** (including novel **AI** uses) per supervisory guidance.
- **Deliverable:** completed assessment **before** go-live; **update** when purpose, scope, or risk materially changes.

**Why:** Accountability regimes expect **proportional** analysis **before** harm, not after headlines.

### 5.2 Consent UX (Lawful Basis = Consent)

- **Must (when consent is the basis):** **granular** choices, **withdraw** as easy as **give**, plain language, and **no dark patterns**; record **what** was consented to and **when**.
- **Out of scope here:** legal basis choice (consent vs contract vs legitimate interests)—that is **legal** sign-off; engineering implements the **documented** basis.

**Why:** Bad consent UX is both **regulatory** and **trust** failure.

### 5.3 Personal Data In AI Training, Evaluation, Or Prompt Context

- **Must:** treat as a **high-risk** change until legal/privacy review says otherwise: **minimisation**, **retention** caps, **DPA** / vendor flow review, and **no** production PII in **dev** prompts/logs without clearance.
- **Should:** map controls to **NIST SSDF** and **SP 800-218A** where the org adopts them (see [secure-development-lifecycle.md](secure-development-lifecycle.md)).

**Why:** Models **memorise** and **leak**; prompt pipelines **log** unless designed not to.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Minimise by default | Reduces **blast radius** of breaches and simplifies **DSAR** / erasure. |
| Explicit retention | Makes cost and compliance **measurable**; avoids silent infinite growth. |
| Split audit vs analytics | **Least privilege** and clearer incident handling. |
| DPIA when high risk | **Accountability** expectation under GDPR-like regimes; avoids **surprise** supervisory questions. |
| Split §5 into three tracks | Teams can ship **consent UX** fixes without redoing full DPIA, etc.—**verifiable** partial compliance. |

---

## References

- ICO (UK) overview of **data minimisation** (principle): https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/principles/data-minimisation/  
- GDPR **Article 5** principles (lawful basis, minimisation, storage limitation): official EUR-Lex text for EU law.  
- NIST **Privacy Framework** (organisational privacy risk): https://www.nist.gov/privacy-framework  
- ICO (UK) — **Data protection impact assessments (DPIAs)**: https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-lawful-basis/accountability-and-governance/data-protection-impact-assessments-dpias/  
- NIST **SP 800-218A** — SSDF community profile for **AI** systems (see SSDF project / news on csrc.nist.gov): https://csrc.nist.gov/Projects/ssdf  
