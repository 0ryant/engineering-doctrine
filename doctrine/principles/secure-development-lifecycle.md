# Secure Development Lifecycle And Vulnerability Response

Durable rules for **building** software with fewer defects and **responding** when defects ship. Bridges umbrella **Shift Security Left** to **organisational** practice. Maps conceptually to NIST **SSDF** practice groups **Prepare (PO)**, **Protect (PS)**, **Produce (PW)**, and **Respond (RV)**—see [NIST SP 800-218](https://csrc.nist.gov/publications/detail/sp/800-218/final). When AI participates in delivery, [AI-Native Software Development Lifecycle](../patterns/ai-native-software-development-lifecycle.md) composes these practices into evidence-backed transition gates; it does not replace them. When a law, contract, or estate decision applies an external control baseline, [Revision-Pinned External Control Profiles](../patterns/revision-pinned-control-profiles.md) binds its exact authority, revision, system/data boundary, assessment method, and evidence to this lifecycle rather than replacing SSDF or copying a catalogue into this principle.

### SSDF Practice Groups (Inline Summary)

| Group | NIST intent (compressed) | Where this library goes deeper |
| --- | --- | --- |
| **PO — Prepare** | People, process, org risk, supply-chain **awareness** | §4 training; [dependencies-supply-chain.md](dependencies-supply-chain.md); [timeless-principles-and-tooling.md](timeless-principles-and-tooling.md) §6 |
| **PS — Protect** | Harden **environments**, tools, and pipelines against tampering | [build.md](build.md), [configuration-and-secrets.md](configuration-and-secrets.md), CI least privilege |
| **PW — Produce** | Secure **design**, code review, reuse, third-party use | §§1–2; [threat-modeling-stride-lite.md](threat-modeling-stride-lite.md); [testing-strategy.md](testing-strategy.md) |
| **RV — Respond** | **Identify**, **analyze**, **disclose** vulnerabilities in **released** software — including **root cause** that may require **architecture** change, not only a patch | §3; [dependencies-supply-chain.md](dependencies-supply-chain.md) §5; [incident-lifecycle-and-on-call-operations.md](../patterns/incident-lifecycle-and-on-call-operations.md) §9; coordinated disclosure refs |

Full control text remains **NIST’s** publication—this table is a **navigation aid**, not a substitute for SP 800-218.

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

- **Ingest** advisories (ecosystem, SCA, researcher reports) with **severity** and **SLA** to patch or mitigate—**example** merge targets live in [dependencies-supply-chain.md](dependencies-supply-chain.md) §2; align estate policy to **one published table** (adjust numbers by sector, exposure, and regulator—**do not** treat the library’s examples as universal law).
- **Exploit-signal triage** — incorporate **machine-readable** sources your estate trusts (for example [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) for **known exploited** issues; [FIRST EPSS](https://www.first.org/epss/user-guide) as a **prioritisation** input alongside asset exposure and reachability). **Known exploited** findings typically **outrank** generic CVSS-only backlog ordering.
- **Coordinated disclosure** — protect users: prepare **fixes** or **mitigations** before public detail when possible; credit researchers per policy.
- **Customer** and **operator** comms for exploitable issues in shipped software—template comms in runbooks.
- **Root-cause class** — after remediation, classify work as **patch-level** (fix the defect), **process/control-level** (detection, review, pipeline, training), or **architecture-level** (trust boundaries, segmentation, default permissions, secret distribution, platform defaults). Recurring **same failure class** implies **process** or **architecture** work, not only another ticket.

**Why:** SSDF **RV** is explicitly about **residual** risk after release; silence increases harm and legal exposure. NIST **RV.3** expects analysis that reduces **recurrence**—not only ticket closure.

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
| Inline SSDF table | Readers need a **map** before reading NIST PDF cover-to-cover. |

---

## Related

- AI-native, agent-assisted lifecycle control: [AI-Native Software Development Lifecycle](../patterns/ai-native-software-development-lifecycle.md) and [readiness checklist](../checklists/ai-native-sdlc-readiness.md).
- CUI and other contract/regulatory baselines: [Revision-Pinned External Control Profiles](../patterns/revision-pinned-control-profiles.md).
- Generative AI, RAG, fine-tuning, and **agentic** change paths in the SDLC: [ai-ml-systems.md](ai-ml-systems.md) (with **SP 800-218A** context for model-development practices).
- **AI-accelerated** vulnerability discovery and **VulnOps**-style response — background research: [evolution/mythos-era-engineering-principles-research-2026-04-28.md](../evolution/mythos-era-engineering-principles-research-2026-04-28.md); gap closure tracked in [ADR 0010](../../docs/adr/0010-record-mythos-era-vulnerability-storm-research-and-doctrine-gaps.md).

---

## References

- NIST **SP 800-218**, *Secure Software Development Framework* (SSDF) v1.1: https://csrc.nist.gov/publications/detail/sp/800-218/final  
- NIST **SSDF project** (overview): https://csrc.nist.gov/Projects/SSDF  
- FIRST **Coordinated Vulnerability Disclosure** (community practice): https://www.first.org/global/sigs/vulnerability-coordination  
- CISA **Known Exploited Vulnerabilities** (catalog and policy context): https://www.cisa.gov/known-exploited-vulnerabilities  
- FIRST **EPSS** (exploit likelihood scoring — triage input): https://www.first.org/epss/user-guide  
