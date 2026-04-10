# Secure Development Lifecycle And Vulnerability Response

Durable rules for **building** software with fewer defects and **responding** when defects ship. Bridges umbrella **Shift Security Left** to **organisational** practice. Maps conceptually to NIST **SSDF** practice groups **Prepare (PO)**, **Protect (PS)**, **Produce (PW)**, and **Respond (RV)**—see [NIST SP 800-218](https://csrc.nist.gov/publications/detail/sp/800-218/final).

---

## 1. Design And Review

- **Threat assumptions** for new surfaces (API, events, admin tools) recorded early—lightweight STRIDE pass per [threat-modeling-stride-lite.md](threat-modeling-stride-lite.md).
- **Security-sensitive** changes (auth, crypto, tenancy) get **explicit** review criteria in PR template or checklist—not only style review.

**Why:** SSDF **PW** emphasises **secure design** and **reviews**; late security review wastes rework.

---

## 2. Implementation Discipline

- Follow language-appropriate **crypto**, **memory safety**, and **secret** handling (see `ENGINEERING.md` §5 and [configuration-and-secrets.md](configuration-and-secrets.md)).
- **Static** and **dependency** analysis on the merge path—aligned with [dependencies-supply-chain.md](dependencies-supply-chain.md).

**Why:** SSDF **PS** covers **protecting** components (including build pipelines) from tampering; **PW** covers producing **well-secured** software.

---

## 3. Vulnerability Response (RV)

- **Ingest** advisories (ecosystem, SCA, researcher reports) with **severity** and **SLA** to patch or mitigate.
- **Coordinated disclosure** — protect users: prepare **fixes** or **mitigations** before public detail when possible; credit researchers per policy.
- **Customer** and **operator** comms for exploitable issues in shipped software—template comms in runbooks.

**Why:** SSDF **RV** is explicitly about **residual** risk after release; silence increases harm and legal exposure.

---

## 4. Training And Roles (PO)

- Engineers know **where** security expectations live (this doctrine + estate policies); onboarding includes **secrets**, **authz**, and **dependency** hygiene.

**Why:** SSDF **PO** includes preparing **people** and **processes**—documentation is the portable minimum.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| SSDF vocabulary | Gives **acquirers** and **GRC** a mapping without pasting full control catalogues. |
| RV explicit | Distinguishes **engineering** quality from **incident** and **disclosure** process. |

---

## References

- NIST **SP 800-218**, *Secure Software Development Framework* (SSDF) v1.1: https://csrc.nist.gov/publications/detail/sp/800-218/final  
- NIST **SSDF project** (overview): https://csrc.nist.gov/Projects/SSDF  
- FIRST **Coordinated Vulnerability Disclosure** (community practice): https://www.first.org/global/sigs/vulnerability-coordination  
