# Privacy And Data Governance

Durable rules for **personal data**, **contractually or regulatorily controlled data**, **retention**, and **separation of concerns** between product telemetry and security or compliance records.

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

These are **four** separable obligations; teams may comply with **one** without the others in a given release. Track each with its **own** owner and evidence.

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
- **Portable AI delivery rules** (tiers, merge path, RAG governance): [ai-ml-systems.md](ai-ml-systems.md).
- **Telemetry content capture** (prompts/completions in observability pipelines) defaults **off**; the capture gate and per-call signal set: [observability.md](observability.md) §7.

**Why:** Models **memorise** and **leak**; prompt pipelines **log** unless designed not to.

### 5.4 AI Transparency Obligations (EU AI Act Article 50)

- **Applicability first:** these duties bind **providers** and **deployers** of AI systems in **EU AI Act** scope (Regulation (EU) 2024/1689) — systems that interact directly with natural persons or generate content exposed to them — and apply from **2026-08-02**. They are **not** universal doctrine: activate them by registering an **EU AI Act external control profile** ([Revision-Pinned External Control Profiles](../patterns/revision-pinned-control-profiles.md)); the profile registration carries the legal applicability decision (jurisdiction, role, article set), not this file.
- **MUST (profile active, provider role):** **AI-interaction disclosure** — a system intended to interact directly with natural persons tells the person they are interacting with an AI system, as **disclosure UX** delivered at the latest at first interaction, unless that is obvious to a reasonably well-informed, observant and circumspect person (Art 50(1)); and **machine-readable marking** — synthetic audio, image, video, or text outputs are marked in a machine-readable format and detectable as artificially generated or manipulated, with solutions as effective, interoperable, robust, and reliable as technically feasible (Art 50(2)). The Act's assistive/standard-editing carve-outs are recorded in the profile, not assumed.
- **MUST (profile active, deployer role):** **exposure notification** — natural persons exposed to an emotion-recognition or biometric-categorisation system are informed of its operation, with personal data handled per GDPR (Art 50(3)); and **deepfake labelling** — deep-fake image/audio/video content and AI-generated text published to inform the public on matters of public interest disclose that the content was artificially generated or manipulated, subject to the Act's artistic-work and editorial-responsibility carve-outs (Art 50(4)).
- **MUST (profile active):** disclosures are **clear and distinguishable at the latest at the time of first interaction or exposure**, meet applicable accessibility requirements (Art 50(5)), and are **verified pre-launch** as harm-surface evidence where the AI inventory points ([../patterns/ai-adoption-controls.md](../patterns/ai-adoption-controls.md) §§2–3).
- **SHOULD:** implement Art 50(2)/(4) marking and labelling via the Commission's **Code of Practice on Transparency of AI-generated Content** (final 2026-06-10; Commission adequacy opinion 2026-07-08) — adherence is a recognised compliance route, with equivalently adequate alternative means allowed — and design the disclosure UX against the Commission's transparency **guidelines** (2026-07-20).
- **Exceptions:** the Act's own exemptions (obviousness, law-enforcement authorisation, assistive functions, editorial control) are part of the external baseline — record which applies in the profile, with rationale. A doctrine exception MUST NOT claim to waive Art 50 itself; only the governing source recognises variances.
- **Direction disambiguation:** this subsection is the **outbound** duty — labelling **your own** generated content. **Inbound** synthetic-media attack testing (deepfakes against identity/fraud controls) stays with [threat-modeling-stride-lite.md](threat-modeling-stride-lite.md) §3.1 and the [../patterns/ai-adoption-controls.md](../patterns/ai-adoption-controls.md) §3 re-test cadence.

**Why:** transparency failures are fined under Art 99(4)(g) — up to **EUR 15 m or 3 %** of total worldwide annual turnover, whichever is higher — and retrofitting disclosure UX or an output-marking pipeline after launch is a redesign, not a patch. Content published before 2026-08-02 need not be marked retroactively (Commission guidance). Pending-legislation status (for example the Digital Omnibus) is tracked in the adopting ADR, not here.

---

## 6. Contractual And Regulated Data Profiles

- **Do not collapse classifications.** Personal data, CUI, export-controlled data, customer confidential data, secrets, and security evidence may overlap, but each retains its own authority, handling, dissemination, retention, deletion/decontrol, and incident rules.
- **Record applicability and revision.** When an external baseline applies, register the governing agreement, exact publication revision/update, data categories/markings, bounded systems and suppliers, parameters, assessment method, and exceptions using [Revision-Pinned External Control Profiles](../patterns/revision-pinned-control-profiles.md).
- **Follow data into derived and support paths.** Backups, logs, analytics, search indexes, model prompts/context, generated outputs, support tickets, screenshots, and evidence stores remain in scope when they contain or protect the controlled data.
- **Minimise control evidence.** Prefer stable identifiers, hashes, redacted samples, and protected references over copying regulated payloads into tickets, assessments, or audit packs.

**Why:** A privacy programme does not automatically satisfy CUI or another contractual data regime. Explicit profiles prevent both under-protection and accidental expansion of high-control boundaries.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Minimise by default | Reduces **blast radius** of breaches and simplifies **DSAR** / erasure. |
| Explicit retention | Makes cost and compliance **measurable**; avoids silent infinite growth. |
| Split audit vs analytics | **Least privilege** and clearer incident handling. |
| DPIA when high risk | **Accountability** expectation under GDPR-like regimes; avoids **surprise** supervisory questions. |
| Split §5 into four tracks | Teams can ship **consent UX** fixes without redoing full DPIA, etc.—**verifiable** partial compliance. |
| §5.4 profile-gated, not universal | Art 50 duties bind only estates in **EU AI Act** scope; the [control profile](../patterns/revision-pinned-control-profiles.md) carries the applicability decision, keeping doctrine free of regulatory claims for adopters. |
| Separate external profiles | Preserves the distinct authority, revision, boundary, and evidence rules of contractual or regulatory data classes. |

---

## References

- ICO (UK) overview of **data minimisation** (principle): https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/principles/data-minimisation/  
- GDPR **Article 5** principles (lawful basis, minimisation, storage limitation): official EUR-Lex text for EU law.  
- NIST **Privacy Framework** (organisational privacy risk): https://www.nist.gov/privacy-framework  
- ICO (UK) — **Data protection impact assessments (DPIAs)**: https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-lawful-basis/accountability-and-governance/data-protection-impact-assessments-dpias/  
- NIST **SP 800-218A** — SSDF community profile for **AI** systems (see SSDF project / news on csrc.nist.gov): https://csrc.nist.gov/Projects/ssdf  
- EU AI Act **Article 50** — transparency obligations for providers and deployers (applies 2026-08-02): https://artificialintelligenceact.eu/article/50/ — canonical text: Regulation (EU) 2024/1689, ELI: http://data.europa.eu/eli/reg/2024/1689/oj  
- European Commission — **Guidelines on transparency obligations** for providers and deployers of AI systems (2026-07-20): https://digital-strategy.ec.europa.eu/en/news/commission-publishes-guidelines-transparency-obligations-providers-and-deployers-certain-ai-systems  
- European Commission — **Code of Practice on Transparency of AI-generated Content** (final 2026-06-10; adequacy opinion 2026-07-08): https://digital-strategy.ec.europa.eu/en/news/commission-publishes-code-practice-marking-and-labelling-ai-generated-content  
