**Library record:** [ADR 0010](../../docs/adr/0010-record-mythos-era-vulnerability-storm-research-and-doctrine-gaps.md) — research adoption; **G1–G6** gaps **closed in corpus** (2026-04-28) with section pointers in the ADR.

---

# Research Memo: Engineering Principles for the Mythos Era

**To:** Engineering Doctrine Library Maintainer
**Date:** 2026-04-28
**Topic:** Codifying "Mythos-ready" engineering principles — AI-accelerated vulnerability discovery, compressed disclosure-to-weaponization timelines, and what the SDLC must change
**Sources:** CSA/SANS/OWASP April 2026 briefing; Anthropic red team report; NIST SSDF; SLSA; OWASP ASVS/SbD; Veracode/Qualys 2026 benchmarks; Mandiant TTE data
**Status:** Research draft — primary sources verified; speculative items labelled

---

## 1. Executive Thesis

**What actually changes for software engineering — not just for security teams:**

- **The exploit economics floor has dropped to near zero.** Anthropic's Frontier Red Team documented end-to-end exploit generation — from codebase access to working privilege-escalation chain — for under $50 in compute in some cases. When sophisticated offensive research is compute-priced, not skill-priced, the volume and breadth of attacks scales with attacker infrastructure, not headcount. Engineering teams can no longer rely on economic friction to protect secondary or tertiary attack surfaces. ([Futurum / Glasswing analysis](https://futurumgroup.com/insights/anthropic-glasswing-ai-vulnerability-detection-has-crossed-a-threshold/))

- **Disclosure-to-weaponization is now measured in hours, not weeks.** Mandiant data shows average time-to-exploit dropped from 32 days (2022) to under 24 hours (2024). Project Glasswing and the CSA briefing describe a 2026 baseline where sophisticated automated attack chains can be constructed and launched before most patch management pipelines even triage the CVE. ([CSA press release](https://cloudsecurityalliance.org/press-releases/2026/04/14/sans-institute-cloud-security-alliance-un-prompted-and-owasp-genai-security-project-release-emergency-strategy-briefing-as-ai-driven-vulnerability-discovery-compresses-exploit-timelines-from-weeks-to-hours))

- **The SDLC is the primary control surface, not the perimeter.** Patch velocity, SBOM fidelity, blast-radius architecture, and adversarial testing pipelines are now competitive survival variables — not compliance checkboxes. The briefing's first priority action is not a governance step: it's "point AI agents at your own code this week."

- **The asymmetry is structural, not cyclical.** Attackers gain full benefit from AI-discovered vulns immediately; defenders must still coordinate disclosure, validate patches, regression-test, stage, and deploy — across a dependency graph that is growing faster than engineering capacity. Black Duck 2026 OSSRA found open-source vulnerabilities per codebase doubled year-over-year (+107%), driven in part by AI-accelerated development itself. ([Pixee MTTR analysis](https://www.pixee.ai/blog/mttr-cybersecurity-guide))

- **Existing MTTR baselines are catastrophically mismatched.** Enterprise average MTTR is 5 months 10 days (Qualys 2026). CISA's KEV mandate is 15 days. Bitsight found organizations take a median of 137 days to remediate critical known-exploited vulnerabilities — nine times the mandated deadline. The gap between published SLOs and actual performance is now the primary risk vector. ([Qualys 2026 benchmark](https://blog.qualys.com/qualys-insights/2026/04/20/enterprise-patch-remediation-benchmark-2026))

- **AI-generated code increases the vulnerability surface at the same time AI-powered offense is scaling.** The same AI-acceleration that compresses developer time to ship also produces code that inherits training-data vulnerabilities and architecture debt that AI scanners can then find and chain rapidly. Organizations that have not established adversarial testing of AI-assisted code are operating on the wrong side of the asymmetry.

- **"VulnOps" must become a permanent engineering function, not a periodic audit.** The CSA briefing introduces Vulnerability Operations (VulnOps) — a continuously staffed and automated capability for discovery and remediation — as a 12-month structural goal. This is an engineering team design problem, not a security team resourcing problem.

- **Architecture decisions made today encode blast radius for years.** The Glasswing findings demonstrate that 17–27 year old vulnerabilities can be found, chained, and weaponized in hours. Long-lived systems inherit their original architectural blast radius indefinitely unless actively decomposed. Segmentation, egress filtering, and privilege boundaries are now risk-quantifiable architecture primitives. ([Glasswing / cybersecpro analysis](https://cybersecpro.me/posts/project-glasswing-ai-vulnerability-discovery/))

---

## 2. Principle Clusters

The following 16 principles are vendor-neutral and organized into four clusters: **speed**, **architecture**, **process**, and **organizational posture**.

### Cluster A — Speed and Responsiveness

**A1. Time-to-Remediate as a First-Class Engineering SLO**
Patch velocity is a measurable reliability indicator, not a compliance artefact. Organizations should define and enforce remediation SLOs by severity tier — with critical/exploitable findings targeting ≤72 hours and high-severity ≤15 days — and track these as SLIs alongside uptime. Absent explicit SLOs, MTTR drifts to industry average (5+ months), which now equals "exploited."

**A2. Continuous Vulnerability Discovery (Not Periodic Scanning)**
Point-in-time penetration tests and quarterly scans were calibrated for weeks-to-exploit timelines. In the Mythos era, vulnerability discovery must be a continuously running background process — either via AI-assisted scanners, automated adversarial pipelines, or funded bug bounty programs with aggressive triage SLAs. Discovery cadence must at minimum match adversary discovery cadence.

**A3. Automated Triage Before Automated Remediation**
The bottleneck in most organizations' MTTR is not the fix — it is the time from alert to prioritized ticket (often 80% of elapsed time). Automated risk-scoring using EPSS (Exploit Prediction Scoring System), CVSS, and asset context must precede remediation automation. Teams that automate remediation without fixing triage first create noise, false positives, and erosion of trust in the pipeline. ([Pixee MTTR analysis](https://www.pixee.ai/blog/mttr-cybersecurity-guide))

**A4. Coordinated Disclosure as an Engineering Input, Not a Legal Output**
Vulnerability disclosure programs (VDPs) should feed findings directly into engineering backlog triage — not routing through legal/communications bottlenecks first. NIST SSDF RV.1 calls for establishing disclosure programs; the Mythos era requires they be operationalized with engineering-owned SLAs, not just policy acknowledgement. ([NIST SP 800-218](https://csrc.nist.gov/publications/detail/sp/800-218/final))

### Cluster B — Architecture and Blast Radius

**A5. Blast-Radius Minimization by Design**
Every service, process, and credential should operate with the minimum privilege necessary for its purpose, and every system boundary should be designed to contain lateral movement. This is not new (OWASP ASVS V4.1.3 / OWASP Least Privilege Principle), but in the Mythos era it becomes the primary engineering constraint against AI-discovered exploit chains that traverse multiple small weaknesses. Design reviews should include explicit blast-radius analysis. ([OWASP Least Privilege](https://owasp.org/www-community/controls/Least_Privilege_Principle))

**A6. Egress Filtering and Network Segmentation as Code**
Defensive network controls — egress filtering, micro-segmentation, explicit deny-by-default — should be declared as code alongside application infrastructure and reviewed on every deploy. The CSA briefing calls these out as foundational hardening steps that increase attacker difficulty regardless of vulnerability density.

**A7. Secure-by-Default Configuration Baselines**
New services and libraries should ship with the most restrictive configuration that permits their intended function, not the most permissive configuration that avoids immediate breakage. TLS-only, private networking by default, minimum required scopes for all tokens and roles. OWASP Secure by Design Framework formalizes this as a design-phase principle. ([OWASP SbD](https://owasp.org/www-project-secure-by-design-framework/))

**A8. Defense in Depth / No Single Point of Exploitation**
Architecture should assume that any individual control will be bypassed. Glasswing's most significant findings were exploit chains — multiple smaller vulnerabilities composed into a single critical impact. A defense-in-depth architecture does not prevent each individual flaw from being found, but it prevents the chain from completing. Choke points between privilege tiers, between network segments, and between trust domains are primary architectural deliverables.

### Cluster C — Process and Tooling

**A9. Adversarial CI — AI-Powered Offense in the Build Pipeline**
Every code change that touches security-relevant paths (auth, access control, data handling, privilege boundaries) should be subjected to automated adversarial testing before merge. This means AI-assisted SAST/SCA with vulnerability chaining awareness, not just static pattern matching. The CSA briefing's first priority action is to deploy AI agents against your own code immediately. Tools in this space include Aikido Infinite (continuous autonomous pentest per release), Snyk Evo's CLI red teaming, and Basilisk for AI application testing. ([Aikido Infinite](http://www.aikido.dev/blog/introducing-aikido-infinite))

**A10. Provable Dependency Hygiene (SBOM + SLSA)**
Organizations must maintain machine-readable Software Bills of Materials (SBOMs) for all production artifacts, with automated scanning against vulnerability feeds on every build. SLSA v1.1 (April 2025) provides a tiered framework: L1 establishes provenance, L2 adds signed hosted builds, L3 hardens the build platform against tampering. The draft Dependency track adds inventory, triage, and producer-controlled sourcing. Open-source vulnerabilities per codebase doubled year-over-year (Black Duck 2026); SBOM without continuous scanning is a false assurance. ([SLSA](https://slsa.dev/))

**A11. Human-AI Joint Review for Security-Critical Paths**
AI-generated code and AI-assisted reviews should not be the sole gate on security-critical logic — authentication, authorization, cryptography, data boundary enforcement. Human review with explicit security focus should be preserved on these paths, calibrated by risk. The goal is not to slow down AI-assisted development, but to prevent AI-generated code with subtly wrong security assumptions from passing through an AI-only review gate that shares the same training distribution.

**A12. Incident-Driven Architecture Review**
Every security incident should trigger a structured review of architectural assumptions — not just a post-incident fix of the specific vulnerability. Root cause analysis (NIST SSDF RV.3) should ask whether the exploit succeeded because of a missing patch (fix the patch process) or because of an architectural property that amplified blast radius (fix the architecture). Incidents are the primary signal for where architecture decisions have encoded risk.

**A13. Reproducible, Artifact-Promoted Builds**
Build pipelines should produce identical, signed artifacts from a given commit hash regardless of when or where they run. Artifact promotion — not mutation — is the model: build once, verify, promote the same artifact through staging to production. This eliminates the class of CI/CD compromise attacks and supports SLSA L3 provenance guarantees. Declarative build infrastructure, pinned toolchains, and hermetic build environments are implementation requirements.

### Cluster D — Organizational Posture

**A14. VulnOps as a Permanent Engineering Function**
Vulnerability management should be a continuously operating, permanently staffed function with clear engineering ownership — not a periodic security audit or a CISO-owned spreadsheet. VulnOps owns: automated discovery integration, triage SLO enforcement, patch coordination, and retrospective architecture signalling. The CSA briefing treats standing up VulnOps as the 12-month structural goal for Mythos-ready programs.

**A15. Operational Downtime Tolerance Recalibrated for Patch Velocity**
Legacy risk tolerance models that treated patch-induced downtime as a greater risk than unpatched vulnerability exposure must be revisited. When exploitation timelines compress to hours, the expected cost of delayed patching rises faster than most downtime-tolerance calculations assumed. Engineering teams should document and explicitly review their change-freeze policies and high-availability assumptions against current TTE data.

**A16. Security Debt as an Engineering Metric, Not a Security Metric**
The 82% of organizations carrying security debt (Veracode 2026) is an engineering budget and prioritization failure before it is a security failure. Security debt — open findings beyond SLO — should appear in engineering planning cadences, sprint reviews, and team-level OKRs alongside feature and reliability work. Treating it as a CISO-owned backlog that engineering services on request is the structural cause of the 5-month MTTR average.

---

## 3. Tensions and Trade-offs

**T1. Patch Velocity vs. Stability**
Compressing MTTR for critical findings requires accepting higher change frequency and more aggressive deployment pipelines. Organizations with strict change windows (finance, healthcare, regulated infrastructure) face a structural conflict: the controls designed to prevent operational instability are the same controls that slow patch deployment. Resolution path: risk-tiered fast-track channels for confirmed exploited CVEs, pre-approved emergency change procedures, and canary/phased rollout to contain patch-induced regressions.

**T2. Automation vs. Accountability**
Automated remediation PRs (Aikido, Mondoo, Anthropic-assisted patching) can compress fix time from days to hours — but they shift accountability. If an automated fix introduces a regression or misconfiguration, ownership becomes ambiguous. Organizations need explicit policies defining when automated remediation requires human approval, at what severity thresholds, and who is accountable for merged auto-fixes. The SRE error-budget model is useful here: automated fixes within error budget, human-gated above it.

**T3. Openness vs. Exploitability**
Open-source dependency ecosystems, public vulnerability disclosure, and shared tooling are engineering goods. But open source vulnerability counts doubling per codebase per year (Black Duck 2026) means that openness now directly increases surface area that AI-powered scanners can enumerate. Resolution is not to abandon open source, but to enforce SLSA-level provenance and continuous scanning as the cost of participation, and to contribute upstream patches rather than only consuming fixes.

**T4. Speed-to-Ship vs. Security-of-Ship**
AI-assisted code generation enables developers to ship significantly more code per unit time. That acceleration compounds vulnerability surface area if security review cadence does not scale proportionally. Adversarial CI (Principle A9) is the architectural answer — security review moves into the pipeline rather than competing with it — but tooling maturity and false-positive rates remain genuine engineering cost factors.

**T5. AI-Powered Defense vs. AI-Powered Offense Asymmetry**
Both offense and defense can employ AI, but the asymmetry is structural: offense needs to find one exploitable path; defense must find and close all of them. AI-assisted discovery deployed defensively (Glasswing-model) helps, but does not eliminate the asymmetry. This shapes where defensive investment has highest marginal value: blast-radius architecture (limiting what any single path can reach) over exhaustive vulnerability closure.

**T6. Disclosure Coordination vs. Zero-Day Window**
Project Glasswing's model — gated access for defensive patching before public disclosure — compresses the zero-day window for patch-capable partners. For organizations outside the partner coalition, the window between "AI model discovers it" and "CVE is public" may be shorter than their patch cycle. This creates a two-tier world and raises equity questions about which organizations get advance access to threat intelligence.

**T7. Least Privilege vs. Developer Velocity**
Tightly scoped permissions, strict segmentation, and deny-by-default configurations are the correct security posture but impose real friction on developer workflows (service-to-service calls requiring explicit grants, local development environment parity with production, credential rotation). The principle should be "least privilege automated and invisible" — platform teams providing least-privilege defaults that require no individual developer action, not least-privilege as a manual checklist burden.

---

## 4. Academic and Industry Anchors

**NIST SP 800-218 (SSDF v1.1, February 2022)**
The Secure Software Development Framework's RV (Respond to Vulnerabilities) practice group — RV.1 (identify), RV.2 (assess, prioritize, remediate), RV.3 (root cause analysis) — is the most directly applicable existing standard. It does not specify numeric SLOs; those are organization-defined. The Mythos era makes SLO specification a minimum requirement, not an organizational option.
[https://csrc.nist.gov/publications/detail/sp/800-218/final](https://csrc.nist.gov/publications/detail/sp/800-218/final)

**NIST SP 800-218A (SSDF AI Community Profile)**
NIST extended the SSDF with a community profile for generative AI and dual-use foundation models, adding practices specific to AI model development. Relevant for organizations building AI-assisted tooling into their SDLC.
[https://csrc.nist.gov/Projects/SSDF](https://csrc.nist.gov/Projects/SSDF)

**SLSA v1.1 (Supply-chain Levels for Software Artifacts, April 2025)**
OpenSSF framework for build provenance and supply chain integrity, with a draft Dependency track covering SBOM-backed vulnerability triage. SLSA L3 (hardened builds with isolated runners, signed provenance) is the target state for production artifact pipelines.
[https://slsa.dev/](https://slsa.dev/)

**OWASP ASVS 4.0 And 5.0**
Codifies least privilege and fail-secure access control in the version reviewed. OWASP released ASVS 5.0.0 on 30 May 2025; consumers should pin requirement identifiers with the ASVS version because numbering changes between releases. The current stable project page is the authority for later mappings.
[https://owasp.org/www-project-application-security-verification-standard/](https://owasp.org/www-project-application-security-verification-standard/)

**OWASP Secure by Design Framework**
Design-phase principles: least privilege, defense in depth, secure defaults, minimized attack surface, simplicity. Explicitly a pre-implementation framework, complementing ASVS's implementation-phase verification.
[https://owasp.org/www-project-secure-by-design-framework/](https://owasp.org/www-project-secure-by-design-framework/)

**CISA Binding Operational Directive 22-01**
US federal mandate: remediate known exploited vulnerabilities within 14 days. De facto benchmark for critical/exploited findings across both public and private sectors. Current industry median (137 days for critical KEVs, Bitsight) represents a 9x miss.
[https://www.cisa.gov/news-events/directives/bod-22-01](https://www.cisa.gov/news-events/directives/bod-22-01)

**CSA / SANS / OWASP GenAI "AI Vulnerability Storm" Briefing (April 12, 2026)**
Foundational primary source for this memo. A 60-contributor expedited strategy briefing with 13-item risk register mapped to OWASP LLM Top 10 2025, OWASP Agentic Top 10 2026, MITRE ATLAS, and NIST CSF 2.0. Introduces the VulnOps concept. Licensed CC BY-NC 4.0.
[https://labs.cloudsecurityalliance.org/mythos-ciso/](https://labs.cloudsecurityalliance.org/mythos-ciso/)

**Anthropic Frontier Red Team Report on Claude Mythos Preview (April 7, 2026)**
Primary technical source for Glasswing capability demonstration: autonomous zero-day discovery and exploit chain construction across Linux kernel, OpenBSD, FreeBSD NFS, and major browsers. Documents ~90x improvement in exploit generation vs prior models, specific CVEs, and the mechanics of multi-vulnerability chain construction.
[https://red.anthropic.com/2026/mythos-preview/](https://red.anthropic.com/2026/mythos-preview/)

**Qualys Enterprise Patch & Remediation Benchmark 2026**
Industry MTTR baseline: 5 months 10 days average. Manual remediation fails to keep pace with attackers 88% of the time for actively weaponized vulnerabilities.
[https://blog.qualys.com/qualys-insights/2026/04/20/enterprise-patch-remediation-benchmark-2026](https://blog.qualys.com/qualys-insights/2026/04/20/enterprise-patch-remediation-benchmark-2026)

**Veracode State of Software Security 2026**
Flaw half-life: 243 days. 82% of organizations carry security debt. High-severity exploitable flaws up 36% year-over-year.

**Mandiant TTE Trend Data** *(via Mondoo / public reporting)*
Average time-to-exploit: 32 days (2022) → <24 hours (2024). Adversaries are operationalizing vulnerabilities before most patch pipelines complete triage.

---

## 5. Gaps for Doctrine: Where Existing Secure SDLC Guidance Under-Specifies

The following gaps are specific to AI-speed offense; they are not failures of existing frameworks on their own terms, but places where AI-era conditions expose the implicit assumptions behind those frameworks.

Update 2026-04-28: all six gaps below are now closed in corpus text. This section remains as the research record of what was missing before the follow-up synthesis pass. The authoritative closure map lives in [ADR 0010](../../docs/adr/0010-record-mythos-era-vulnerability-storm-research-and-doctrine-gaps.md).

~~**Gap 1: No SLO Prescriptions in the Dominant Frameworks**~~
Closed in corpus 2026-04-28: [secure-development-lifecycle.md](../principles/secure-development-lifecycle.md) §3, [dependencies-supply-chain.md](../principles/dependencies-supply-chain.md) §2, and [measurement-and-dora.md](../principles/measurement-and-dora.md) §2.1 now define remediation SLAs, exploit-signal triage, and measurable vulnerability-response SLIs.

NIST SSDF, OWASP ASVS, and SAFECode all treat remediation timelines as "risk-based, organization-defined." This was adequate when average TTE was measured in weeks. At <24-hour TTE for known CVEs, "organization-defined" produces the 5-month MTTR average. Doctrine should prescribe default SLO tiers (e.g., critical exploited: ≤72h; critical disclosed: ≤7d; high: ≤15d) as starting positions, with explicit guidance on how to assess whether organizational context justifies deviation — not leave timelines unspecified.

~~**Gap 2: Adversarial CI is Treated as Optional and Human-Driven**~~
Closed in corpus 2026-04-28: [merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md) §2 invariants 8-9 and §3, [testing-strategy.md](../principles/testing-strategy.md) §5, and [merge-path-and-pipeline-control-suite.md](../tooling/merge-path-and-pipeline-control-suite.md) §1 now make adversarial analysis a merge-path concern with server-enforced evidence expectations for security-relevant scope.

Existing SDLC guidance treats penetration testing and red teaming as periodic, human-led activities. None of the major frameworks (SSDF, ASVS, SAFECode) specify continuous adversarial testing as a pipeline gate. As AI-powered adversarial tools (Aikido Infinite, Adversa AI, Snyk Evo) become viable CI/CD integrations, doctrine should specify when adversarial CI is required (minimally: all changes to auth, access control, cryptography, and external-facing API surface) and what constitutes an acceptable adversarial testing gate.

~~**Gap 3: SBOM Guidance Stops at Generation; Continuous Scanning is Implied but Not Operationalized**~~
Closed in corpus 2026-04-28: [dependencies-supply-chain.md](../principles/dependencies-supply-chain.md) §3 and [merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md) §2 invariant 9 now define per-artifact SBOM retention, feed-backed re-evaluation at promotion, VEX-style dispositions, and blocking expectations for newly disclosed vulnerability state.

EO 14028 and SSDF call for SBOMs. SLSA provides provenance. But existing guidance under-specifies the operational loop: SBOM generated at build time, scanned against updated vulnerability feeds on every deploy, with automated blocking and SLO-tracked triage for new findings against existing artifacts in production. The Glasswing scenario — where a 27-year-old vulnerability is suddenly discovered and weaponizable — means SBOM freshness and continuous feed integration are operational requirements, not one-time deliverables.

~~**Gap 4: Blast-Radius Architecture is a Design Principle Without Engineering Acceptance Criteria**~~
Closed in corpus 2026-04-28: [threat-modeling-stride-lite.md](../principles/threat-modeling-stride-lite.md) §4 now defines portable blast-radius acceptance prompts, evidence expectations, and a review bar that makes containment claims falsifiable.

OWASP SbD and ASVS both call for least privilege and defense in depth. Neither provides acceptance criteria or architectural test cases. Doctrine should specify what blast-radius analysis looks like in a design review: explicit enumeration of what a compromised component can reach (data stores, credential material, adjacent services, egress paths), with a required mitigation narrative for any path that reaches critical assets. Without acceptance criteria, blast-radius "analysis" is a checkbox.

~~**Gap 5: AI-Generated Code Has No Specific Secure SDLC Treatment**~~
Closed in corpus 2026-04-28: [ai-ml-systems.md](../principles/ai-ml-systems.md) §4 and [code-review-and-change-approval.md](../patterns/code-review-and-change-approval.md) §6 now require human understanding and approval for AI-generated changes on security-critical paths, alongside the usual merge-path evidence.

No current major framework addresses AI-assisted code generation as a distinct SDLC input with specific security review requirements. The implicit assumption that code review processes are symmetric — human-written code reviewed by humans, AI-assisted code reviewed the same way — ignores that AI-generated code may inherit training-data vulnerability patterns at scale, and that an AI-only review gate for AI-generated code shares failure modes. Doctrine should specify that security-critical paths (auth, access control, data boundary enforcement) require human review even when AI-generated.

~~**Gap 6: Incident-to-Architecture Feedback Loop is Absent from Most Frameworks**~~
Closed in corpus 2026-04-28: [incident-lifecycle-and-on-call-operations.md](../patterns/incident-lifecycle-and-on-call-operations.md) §9 and [secure-development-lifecycle.md](../principles/secure-development-lifecycle.md) §3 now require architecture-class root-cause handling and tracked backlog items when system shape amplifies incident impact.

SSDF RV.3 specifies root cause analysis and process updates. But existing frameworks do not specify the architectural feedback loop: when a security incident reveals that architectural properties (insufficient segmentation, over-privileged service accounts, wide blast radius) amplified impact, that finding should trigger architectural review and backlog items — not just a patch. This gap means organizations close individual vulnerabilities without closing the architectural conditions that made exploitation impactful.

---

*Memo produced from primary source research. All cited statistics are attributed to named sources; Glasswing capability claims are drawn from Anthropic's own Frontier Red Team report (CC BY-NC 4.0 briefing; Anthropic public red team report). Speculative or forward-looking items are not present in this memo — all claims are anchored to published April 2026 or earlier sources.*
