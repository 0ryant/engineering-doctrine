# Secure Development Lifecycle And Vulnerability Response

Durable rules for building software with fewer defects and responding when defects ship. Carries [Core Proposition 7](../../ENGINEERING.md#7-protect-proportionately-to-risk) (Protect Proportionately To Risk) into organisational practice. Maps conceptually to NIST SSDF practice groups Prepare (PO), Protect (PS), Produce (PW), and Respond (RV)—see [NIST SP 800-218](https://csrc.nist.gov/publications/detail/sp/800-218/final). When AI participates in delivery, [AI-Native Software Development Lifecycle](../patterns/ai-native-software-development-lifecycle.md) composes these practices into evidence-backed transition gates; it does not replace them. When a law, contract, or estate decision applies an external control baseline, [Revision-Pinned External Control Profiles](../patterns/revision-pinned-control-profiles.md) binds its exact authority, revision, system/data boundary, assessment method, and evidence to this lifecycle rather than replacing SSDF or copying a catalogue into this principle.

### SSDF Practice Groups (Inline Summary)

| Group | NIST intent (compressed) | Where this library goes deeper |
| --- | --- | --- |
| **PO — Prepare** | People, process, org risk, supply-chain awareness, secure development environments (PO.5) | §4 training; [dependencies-supply-chain.md](dependencies-supply-chain.md); [timeless-principles-and-tooling.md](timeless-principles-and-tooling.md) §7 |
| **PS — Protect** | Protect all components of the software from tampering and unauthorised access | [build.md](build.md), [configuration-and-secrets.md](configuration-and-secrets.md), CI least privilege |
| **PW — Produce** | Secure design, code review, reuse, third-party use | §§1–2; [threat-modeling-stride-lite.md](threat-modeling-stride-lite.md); [testing-strategy.md](testing-strategy.md) |
| **RV — Respond** | Identify, analyze, disclose vulnerabilities in released software — including root cause that may require architecture change, not only a patch | §§3, 3.1; [dependencies-supply-chain.md](dependencies-supply-chain.md) §7; [incident-lifecycle-and-on-call-operations.md](../patterns/incident-lifecycle-and-on-call-operations.md) §9; coordinated disclosure refs |

Full control text remains NIST’s publication—this table is a navigation aid, not a substitute for SP 800-218.

---

## 1. Design And Review

- Threat assumptions for new surfaces (API, events, admin tools) recorded early—lightweight STRIDE pass per [threat-modeling-stride-lite.md](threat-modeling-stride-lite.md).
- Security-sensitive changes (auth, crypto, tenancy) get explicit review criteria in PR template or checklist—not only style review.

**Why:** SSDF PW emphasises secure design and reviews; late security review wastes rework.

---

## 2. Implementation Discipline

- Follow language-appropriate crypto, memory safety, and secret handling (see [configuration-and-secrets.md](configuration-and-secrets.md) and Core Proposition 7 in `ENGINEERING.md`).
- Static and dependency analysis on the merge path—aligned with [dependencies-supply-chain.md](dependencies-supply-chain.md).

**Why:** SSDF PS covers protecting components (including build pipelines) from tampering; PW covers producing well-secured software.

---

## 3. Vulnerability Response (RV)

- Ingest advisories (ecosystem, SCA, researcher reports) with severity and SLA to patch or mitigate—example targets live in [dependencies-supply-chain.md](dependencies-supply-chain.md) §2; align estate policy to one published table (adjust numbers by sector, exposure, and regulator—do not treat the library’s examples as universal law).
- **Exploit-signal triage** — incorporate machine-readable sources your estate trusts (for example [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) for known exploited issues; [FIRST EPSS](https://www.first.org/epss/) as a prioritisation input alongside asset exposure and reachability). Known exploited findings typically outrank generic CVSS-only backlog ordering.
- **Coordinated disclosure** — protect users: prepare fixes or mitigations before public detail when possible; credit researchers per policy.
- Customer and operator comms for exploitable issues in shipped software—template comms in runbooks.
- **Root-cause class** — after remediation, classify work as patch-level (fix the defect), process/control-level (detection, review, pipeline, training), or architecture-level (trust boundaries, segmentation, default permissions, secret distribution, platform defaults). Recurring same failure class implies process or architecture work, not only another ticket.

**Why:** SSDF RV is explicitly about residual risk after release; silence increases harm and legal exposure. NIST RV.3 expects analysis that reduces recurrence—not only ticket closure.

### 3.1 Regulatory Reporting Clocks (Profile-Gated)

- **Applicability first:** some regimes set deadlines for reporting an exploited vulnerability or a security incident to an authority. These duties are **not** universal doctrine: activate them by registering the regime as an external control profile ([Revision-Pinned External Control Profiles](../patterns/revision-pinned-control-profiles.md)). The profile carries the applicability decision (role, product scope, jurisdiction), the triggers, deadlines, recipient, channel, and pinned sources, not this file.
- **MUST (profile with a reporting clock active):** vulnerability-response and incident runbooks name each reporting trigger, the event that starts the clock, the deadlines, the recipient and channel, and who is authorised to submit. The vulnerability or incident record states **when** the estate became aware and **who** made that determination.
- **SHOULD (same scope):** exercise the reporting path before it is needed: access to the reporting channel works, the on-call route reaches an authorised submitter outside office hours, and triage asks the regime's trigger question early.
- **Worked example, not a scope claim:** under the EU Cyber Resilience Act (Regulation (EU) 2024/2847, Art 14, applying from **2026-09-11**), a manufacturer of a product with digital elements reports an **actively exploited vulnerability**, or a **severe incident** affecting the product's security, to the coordinator CSIRT and ENISA through the single reporting platform. Each has an early warning within **24 hours** of becoming aware and a notification within **72 hours**. The final report is due **14 days** after a corrective or mitigating measure is available for a vulnerability, and **one month** after the 72-hour notification for an incident. Users are informed under Art 14(8); the customer communications in §3 carry that.
- **Exceptions:** only the governing regime grants variances. A doctrine exception MUST NOT claim to waive a statutory deadline; record the regime's own exemptions in the profile.

**Why:** a 24-hour clock can start outside office hours and before root cause is known. A team that first has to find out who may file, and where, will miss it. The deadline is the regime's own. The preparation rule is this library's, admitted on the regulation plus a stated risk asymmetry: preparing costs a runbook section and an exercise, and missing a statutory deadline is regulatory exposure ([ADR 0055](../../docs/adr/0055-add-profile-gated-regulatory-reporting-clocks.md)).

---

## 4. Training And Roles (PO)

- Engineers know where security expectations live (this doctrine + estate policies); onboarding includes secrets, authz, and dependency hygiene.

**Why:** SSDF PO includes preparing people and processes—documentation is the portable minimum.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| SSDF vocabulary | Gives acquirers and GRC a mapping without pasting full control catalogues. |
| RV explicit | Distinguishes engineering quality from incident and disclosure process. |
| Inline SSDF table | Readers need a map before reading NIST PDF cover-to-cover. |
| Reporting clocks profile-gated (§3.1) | Deadlines bind only estates in a regime's scope, so the profile carries the legal decision; the runbook preparation is what makes a 24-hour clock reachable ([ADR 0055](../../docs/adr/0055-add-profile-gated-regulatory-reporting-clocks.md)). |

---

## Related

- AI-native, agent-assisted lifecycle control: [AI-Native Software Development Lifecycle](../patterns/ai-native-software-development-lifecycle.md) and [readiness checklist](../checklists/ai-native-sdlc-readiness.md).
- CUI and other contract/regulatory baselines: [Revision-Pinned External Control Profiles](../patterns/revision-pinned-control-profiles.md).
- Generative AI, RAG, fine-tuning, and agentic change paths in the SDLC: [ai-ml-systems.md](ai-ml-systems.md) (with SP 800-218A context for model-development practices).
- AI-accelerated vulnerability discovery and VulnOps-style response — background research: [evolution/mythos-era-engineering-principles-research-2026-04-28.md](../evolution/mythos-era-engineering-principles-research-2026-04-28.md); gap closure tracked in [ADR 0010](../../docs/adr/0010-record-mythos-era-vulnerability-storm-research-and-doctrine-gaps.md).

---

## References

- NIST SP 800-218, *Secure Software Development Framework* (SSDF) v1.1: https://csrc.nist.gov/publications/detail/sp/800-218/final  
- NIST SSDF project (overview): https://csrc.nist.gov/Projects/SSDF  
- FIRST Coordinated Vulnerability Disclosure (community practice): https://www.first.org/global/sigs/vulnerability-coordination  
- CISA Known Exploited Vulnerabilities (catalog and policy context): https://www.cisa.gov/known-exploited-vulnerabilities  
- FIRST EPSS (exploit likelihood scoring — triage input): https://www.first.org/epss/
- Regulation (EU) 2024/2847, **Cyber Resilience Act**, Art 14 reporting obligations and Art 71(2) application dates (S1; canonical identifier ELI `reg/2024/2847/oj`; accessed 2026-11-18): http://data.europa.eu/eli/reg/2024/2847/oj  
- European Commission — **CRA reporting** summary (S2; last update 2026-09-11; accessed 2026-11-18): https://digital-strategy.ec.europa.eu/en/policies/cra-reporting  
- European Commission — **guidance on the application of the Cyber Resilience Act**, C/2026/6013, section 9.1 on becoming aware (S2; OJ C 2026-11-17; not binding; accessed 2026-11-18): http://publications.europa.eu/resource/celex/52026XC06013  
