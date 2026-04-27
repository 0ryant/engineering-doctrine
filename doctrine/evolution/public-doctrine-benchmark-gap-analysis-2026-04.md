# Public Doctrine Benchmark Gap Analysis

**Date:** 2026-04-26.  
**Companion (2026-04-27):** [public-doctrine-taxonomy-scorecard-and-choice-2026-04-27.md](public-doctrine-taxonomy-scorecard-and-choice-2026-04-27.md) — taxonomy of public *kinds* of doctrine, **refreshed** scorecard, and **which source to lead with when** (decision guide).  
**Question:** How does this portable engineering-doctrine library compare with public engineering handbooks, GitHub-hosted playbooks, and public standards? What is still missing or too quiet?

---

## Method

Compared this repository against:

- **Public engineering handbooks / playbooks:** Google engineering practices, Microsoft ISE Code-With Engineering Playbook, GitLab Engineering Handbook, 18F guides, thoughtbot playbook/guides, Trussworks Engineering Playbook, Artsy README, Sourcegraph handbook, GOV.UK Technology Code of Practice.
- **Public standards / research:** Google SRE books, DORA, SPACE, SLSA, NIST SSDF, OpenSSF Scorecard, OWASP ASVS, CNCF Platform Engineering Maturity Model, Twelve-Factor App, MADR, NIST Privacy Framework, WCAG 2.2.

This is not a request to become an organisation handbook. This repository's differentiator is still **portable doctrine**: principles stay vendor and estate agnostic; tooling and cloud choices stay illustrative or estate-specific.

**Source verification note:** URLs cited below were verified with WebFetch where possible. GOV.UK blocked WebFetch with 403 from the fetch environment, so the URL was checked with `curl` returning `200` and content was cross-checked via WebSearch snippets.

---

## Benchmark Corpus

| Source | Why it matters for comparison |
| --- | --- |
| [Google Engineering Practices](https://github.com/google/eng-practices) | Very deep code-review doctrine; narrow scope but high clarity. |
| [Microsoft Code-With Engineering Playbook](https://github.com/microsoft/code-with-engineering-playbook) | Broad public engineering playbook with checklists across delivery, quality, accessibility, DevEx, and security. |
| [GitLab Engineering Handbook](https://handbook.gitlab.com/handbook/engineering/) | Mature public company handbook: engineering management, reliability, process, AI operating rules, roadmaps, allocation, and culture. |
| [18F Guides](https://github.com/18F/guides) | Cross-agency public-service engineering guidance; strong on accessibility, compliance, open source, and delivery practice. |
| [thoughtbot Playbook](https://thoughtbot.com/playbook) and [thoughtbot Guides](https://github.com/thoughtbot/guides) | Consultancy-shaped product engineering and working agreements; strong on workflow and team practice. |
| [Trussworks Engineering Playbook](https://github.com/trussworks/Engineering-Playbook) | Federal delivery, infrastructure, security, documentation, and compliance-shaped engineering practice. |
| [Artsy README](https://github.com/artsy/README) | Public engineering culture, RFCs, ownership, onboarding, and "minimum viable process" style guidance. |
| [Sourcegraph Handbook](https://github.com/sourcegraph/handbook) | High-agency principles and incremental product engineering posture. |
| [GOV.UK Technology Code of Practice](https://www.gov.uk/guidance/the-technology-code-of-practice) | Public-sector technology criteria: user needs, accessibility, open source, open standards, privacy, security, sustainability. |
| [Google SRE Book](https://sre.google/sre-book/table-of-contents/) | Reliability, SLOs, toil, on-call, incident management, launch coordination, and operational examples. |
| [DORA metrics](https://dora.dev/guides/dora-metrics/) and [SPACE](https://queue.acm.org/detail.cfm?id=3454124) | Outcome metrics for delivery and developer experience without individual productivity theatre. |
| [SLSA v1.2](https://slsa.dev/spec/v1.2/) and [OpenSSF Scorecard](https://github.com/ossf/scorecard) | Supply-chain integrity, source/build provenance, branch protection, reviews, dependency hygiene, and release trust. |
| [NIST SSDF](https://csrc.nist.gov/Projects/SSDF) and [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Secure SDLC, vulnerability response, and application security verification vocabulary. |
| [CNCF Platform Engineering Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/) | Platform-as-product, golden paths, self-service, measurement, and adoption maturity. |
| [Twelve-Factor App](https://12factor.net/) | Portability, config, build/release/run separation, logs, process model, dev/prod parity. |
| [MADR](https://adr.github.io/madr/) | Lightweight architecture decision records and decision-log templates. |
| [NIST Privacy Framework](https://www.nist.gov/privacy-framework) and [WCAG 2.2](https://www.w3.org/TR/WCAG22/) | Privacy engineering and accessibility baselines. |

---

## Scorecard

Scale: **5 = distinctive / leads public corpus**, **4 = strong coverage**, **3 = present but too quiet or under-instrumented**, **2 = thin / mostly implicit**, **1 = effectively absent**.

| Category | Score | Current posture | Gap relative to public doctrines |
| --- | ---: | --- | --- |
| Portable layering: principles / tooling / estates | 5 | `timeless-principles-and-tooling.md` and `how-to-read-this-doctrine.md` are unusually clear. | Keep defending this split; it is the library's main advantage. |
| Contracts, schemas, events, and idempotency | 5 | Stronger than the benchmark corpus, especially CloudEvents + versioned payloads + state machines. | Add an OpenAPI / HTTP lifecycle worked example only if adoption needs it. |
| Build, delivery surfaces, provenance | 4.5 | Strong build surfaces, merge-path evidence, SLSA references, and control-suite framing. | Add a consumer-facing scorecard for "minimum acceptable repo gate" by repo criticality. |
| Supply chain and dependency hygiene | 4.5 | Strong SCA, SBOM, provenance, registry hygiene, and governance-program coverage. | Public open-source posture is still thin: security policy, disclosure intake, maintainership, release signing policy for this library. |
| Secure SDLC and vulnerability response | 4 | NIST SSDF mapping, STRIDE-lite, OWASP API / ASVS references, disclosure language. | Add compact "security issue intake and disclosure" pattern for portable projects. |
| Testing and quality gates | 4 | Pyramid, contracts, flakes, mutation/property/a11y testing, CI gates. | Code-review doctrine is less deep than Google eng-practices; add reviewer/author expectations if this becomes a template. |
| Collaboration and trunk workflow | 4.5 | Strong trunk, PR size, merge queue, branch protection, flags, LTS exception handling. | Review latency, reviewer rotation health, and escalation norms are present but could be made measurable. |
| Observability and reliability | 4.5 | SLOs, budgets, incidents, chaos, toil, profiling, OTel-style observability; [patterns/incident-lifecycle-and-on-call-operations.md](../patterns/incident-lifecycle-and-on-call-operations.md) adds **incident command** depth (comms, state doc, handoff) — **2026-04-27**. | Deeper per-estate playbooks, tooling, and RTO drills remain local. |
| On-call and operational human load | 4 | [patterns/incident-lifecycle-and-on-call-operations.md](../patterns/incident-lifecycle-and-on-call-operations.md) states escalation, roles, handoff, interrupt/fatigue posture; [checklists/platform-readiness.md](../checklists/platform-readiness.md) nudges adoption. | Calibrate thresholds and on-call product picks per estate. |
| Developer experience | 4 | Now first-class via `principles/developer-experience.md` and `checklists/developer-experience-scorecard.md`; SPACE, DORA 2024, CNCF platform guidance, and Google review practices are cited. | Keep calibrating the scorecard against real adopter friction: setup failures, review queues, docs findability, and cognitive load. |
| Documentation, ADRs, RFCs, onboarding | 4 | Strong enough in `documentation-knowledge.md` and adoption playbook. | Add templates or examples if the doctrine is used as a starter kit. |
| Accessibility and i18n | 4 | Better than most generic engineering doctrines; scoped and WCAG-aligned. | Navigation underplays it; public-service comparables treat accessibility as headline governance. |
| Privacy and data governance | 4 | Data minimisation, retention, DPIA/PIA triggers, consent UX, AI data handling are present. | Missing a portable data-classification / handling taxonomy, even if labels remain estate-specific. |
| Platform engineering / golden paths | 2.5 | Mentioned via portals, service catalog, and adoption playbook, but not a first-class pattern. | CNCF-style platform-as-product, self-service, golden paths, and service catalog are largely silent. |
| Open source and community governance | 3.5 | Root CONTRIBUTING, SECURITY, LICENSE, GOVERNANCE (2026-04-27) document contribution, disclosure, license, merge/review, and tag cadence. | Optional: CoC file if the community grows; triage labelling; GitHub “private reporting” must be enabled in settings for SECURITY.md to match process. |
| Product / user-need connection | 2.5 | User-facing quality exists; engineering practices are strong. | GOV.UK, 18F, and thoughtbot start from user needs and service outcomes; this library mostly starts from engineering control surfaces. |
| Support, customer communication, and status | 3 | Release checklist, secure vuln comms, incident customer comms exist. | No portable support model: support tiers, status-page cadence, customer-impact wording, known-issue ownership. |
| Sustainability / green software | 3 | Present in `performance-and-cost.md`. | Public-sector comparables make sustainability more explicit across lifecycle, procurement, and hosting choices. |
| AI / ML / agent governance | 4.5 | Strong and unusually current for a portable engineering doctrine. | Keep this as portable control language; avoid hyperscaler model-card or landing-zone templates in principles. |
| Adoption and change management | 4 | Strong adoption playbook, one-pager template, team-size heuristics, blockers. | Could add a maturity model / adoption scorecard so teams can self-assess without reading every file. |
| Doctrine lifecycle and distribution | 3 | Change checklist, sitemap, evolution notes exist. | Missing explicit versioning / release policy for the doctrine library itself and consumer compatibility notes. |

---

## True Silences And Recently Addressed Gaps

These are the areas where the repo is not merely "lighter than a company handbook" but materially quiet, plus items from this review that have since been addressed.

1. **Open-source governance for the doctrine itself — partially addressed 2026-04-27.**  
   Root [CONTRIBUTING.md](../../CONTRIBUTING.md), [SECURITY.md](../../SECURITY.md), [LICENSE](../../LICENSE) (Apache-2.0), and [GOVERNANCE.md](../../GOVERNANCE.md) now document license posture, contribution and proposal paths, maintainer/merge/review expectations, security intake, and release tagging cadence. Remaining soft spots: no formal code of conduct file (see CONTRIBUTING community note), no calendar roadmap (intentional), and no release *signing* policy until the repo ships signed binaries or packages beyond Markdown.

2. **Developer experience as a first-class outcome — addressed 2026-04-27.**  
   `principles/developer-experience.md` now states that a competent engineer should clone, run checks, understand ownership, and ship a safe small change quickly. `checklists/developer-experience-scorecard.md` adds a reviewable scorecard for time-to-first-change, local loop, docs findability, ownership, review flow, cognitive load, and feedback.

3. **Platform engineering / golden paths — addressed 2026-04-27.**  
   [patterns/platform-as-product-and-golden-paths.md](../patterns/platform-as-product-and-golden-paths.md) now says how a platform team packages engineering doctrine into a product: paved roads, self-service, enforced guardrails, service catalog metadata, scorecards, feedback loops, and recorded exceptions. Remaining soft spot: calibrate scorecard thresholds with real platform adopters; no specific portal or catalog product is mandated.

4. **Incident command and on-call operations — addressed 2026-04-27.**  
   [patterns/incident-lifecycle-and-on-call-operations.md](../patterns/incident-lifecycle-and-on-call-operations.md) adds a portable **lifecycle** (detect → command → communicate → stabilize → learn), **severity** matrix, **roles** (IC, comms lead, scribe, SMEs, escalation to exec/legal as needed), **comms cadence**, **incident state doc**, **escalation ladder**, **on-call handoff**, **fatigue / interrupt** posture, and **post-incident** action tracking; [reliability-slo-incidents.md](../principles/reliability-slo-incidents.md) §3 **links** the pattern. Remaining: estate-specific runbooks, paging tools, and **tuning** severities to your org.

5. **Engineering capacity allocation.**  
   Google SRE has toil budgets; GitLab publishes engineering allocation ideas; mature orgs protect reliability, maintenance, security, and enablement work from feature starvation. This repo mentions toil and adoption ROI, but does not state the portable principle: engineering capacity must be deliberately allocated, measured, and defended.

6. **Product / user-need handshake.**  
   As an engineering doctrine, it does not need to become product doctrine. But GOV.UK, 18F, thoughtbot, and SRE launch guidance all connect engineering standards to user need, non-functional requirements, supportability, and service outcomes. This repo should say how engineering accepts, challenges, and preserves those requirements.

7. **Support and customer-impact communication.**  
   Release and incident docs mention communication, but there is no support model: severity vs customer impact, known issues, status-page thresholds, comms ownership, rollback notices, and deprecation/sunset comms as an operating rhythm.

8. **Data classification and handling taxonomy.**  
   Privacy rules are good, but a portable baseline could say "data classes are explicit and drive handling requirements" without prescribing the labels. This bridges privacy, security, observability, analytics, AI prompts, and audit logs.

9. **Doctrine versioning and consumer compatibility — addressed 2026-04-27.**  
   [patterns/doctrine-versioning-and-consumer-compatibility.md](../patterns/doctrine-versioning-and-consumer-compatibility.md) now defines the doctrine contract, SemVer-shaped release labels, change classes, release-note minimums, downstream pinning, deprecation/removal rules, and maintainer checklist. Remaining soft spot: formal tags should start once there is a public consumer cadence; until then, consumers should pin a commit, subtree merge, or submodule revision.

---

## Not Gaps: Already Strong Or Intentionally Out Of Scope

| Area | Assessment |
| --- | --- |
| Full SOC2 / ISO / FedRAMP mapping | Keep out of portable principles. Add estate or control-crosswalk supplements only when needed. |
| Cloud-first mandates | Avoid in principles. GOV.UK can mandate this for government spend; a portable doctrine should not. |
| Specific platform products | Keep as estate examples. Do not turn Backstage, Kubernetes, Terraform Cloud, GitHub Actions, or a cloud SKU into doctrine law. |
| Dedicated SRE staffing model | Keep the reliability budget principle; leave team structure to org context. |
| Procurement process | Only add portable supplier / build-vs-buy risk language. Detailed procurement belongs to estates. |
| AI vendor landing zones | Keep AI/ML governance portable. Model-card templates, hyperscaler policies, and approved model lists belong in estates. |

---

## Recommendations

This section is refreshed from the **Gap Fill Status** table below. Completed recommendations stay visible so the review remains auditable; active recommendations are the remaining gaps.

### Completed From This Review

- **Public project governance — addressed 2026-04-27.** Root [CONTRIBUTING.md](../../CONTRIBUTING.md), [SECURITY.md](../../SECURITY.md), [LICENSE](../../LICENSE) (Apache-2.0), [GOVERNANCE.md](../../GOVERNANCE.md), and [README.md](../../README.md) now cover license posture, contribution/proposal paths, maintainer/review expectations, security intake, and release tagging cadence. Optional follow-up: enable GitHub private vulnerability reporting; add a formal CoC if the community grows.
- **Developer experience as a first-class outcome — addressed 2026-04-27.** [principles/developer-experience.md](../principles/developer-experience.md) names time-to-first-change, local loop, docs findability, cognitive load, review flow, and system-level DevEx measurement; [checklists/developer-experience-scorecard.md](../checklists/developer-experience-scorecard.md) makes those signals reviewable. Remaining work is calibration against real adopter friction, not missing doctrine.
- **Doctrine versioning and consumer compatibility — addressed 2026-04-27.** [patterns/doctrine-versioning-and-consumer-compatibility.md](../patterns/doctrine-versioning-and-consumer-compatibility.md) defines the doctrine contract, SemVer-shaped release labels, change classes, release-note minimums, consumer pinning, deprecation/removal rules, and maintainer checklist. Optional follow-up: start tagging formal doctrine releases when there is a public consumer cadence.
- **Platform engineering, golden paths, self-service, and service catalog — addressed 2026-04-27.** [patterns/platform-as-product-and-golden-paths.md](../patterns/platform-as-product-and-golden-paths.md) states platform-as-product posture, paved roads, self-service with enforced guardrails, tool-agnostic catalog metadata, scorecards, and recorded exceptions without mandating a portal product. Remaining work is adoption calibration, not absence of doctrine.
- **Incident command and on-call operations — addressed 2026-04-27.** [patterns/incident-lifecycle-and-on-call-operations.md](../patterns/incident-lifecycle-and-on-call-operations.md) (severity, roles, comms cadence, state doc, escalation, handoff, fatigue, post-incident actions); [reliability-slo-incidents.md](../principles/reliability-slo-incidents.md) updated; [chaos-engineering-and-game-days.md](../patterns/chaos-engineering-and-game-days.md) and [checklists/platform-readiness.md](../checklists/platform-readiness.md) **cross-link**. Remaining: calibrate to estate on-call and tooling.

### Must Still Do

*None* — the previous “Must” for incident lifecycle is **closed**; see **Gap Fill Status** below. Next tranche of gaps is under **Should** / open items in “True silences”.

### Should

- Add a **capacity allocation** principle: feature work, reliability, toil reduction, security fixes, dependency hygiene, and enablement need deliberate budgets.
- Add a **data classification and handling** principle or pattern that drives logging, analytics, AI prompt use, retention, and audit access.
- Add a **support and customer-impact communications** pattern for incidents, releases, known issues, and deprecations.
- Elevate **accessibility** in navigation for public-sector and enterprise readers; the content exists but is easy to underweight.

### Could

- Add a Google-style **code review author / reviewer guide**.
- Add ADR / RFC templates under tooling or examples.
- Add a compact **self-assessment scorecard** for adopting teams.
- Add a worked **OpenAPI lifecycle** example parallel to the event examples.
- Expand sustainability from a performance/cost subsection into a lifecycle checklist.

---

## Portable Doctrine Guardrail

The main risk is not missing content; it is over-correcting by copying company-handbook material into universal law. The right pattern is:

| Public handbook signal | Portable doctrine translation |
| --- | --- |
| GitLab / Google allocation numbers | "Capacity for reliability, security, toil reduction, and enablement is explicit and defended." |
| GOV.UK cloud-first | "Runtime and hosting choices are justified, portable enough for the estate, and avoid unnecessary lock-in." |
| CNCF platform products | "Golden paths are self-service, measured, owned, and allow recorded exceptions." |
| SRE staffing model | "Reliability ownership, escalation, and error-budget policy are explicit." |
| FedRAMP / ATO mechanics | "Compliance obligations are traceable, risk-based, and estate-specific." |
| Accessibility regulation | "User-facing software has an explicit accessibility target and test evidence." |

---

## Gap Fill Status

| Gap | Status |
| --- | --- |
| Public project governance (license, contribution, security disclosure, maintainer/review, release cadence, how consumers propose changes) | **Addressed** 2026-04-27 — root [CONTRIBUTING.md](../../CONTRIBUTING.md), [SECURITY.md](../../SECURITY.md), [LICENSE](../../LICENSE) (Apache-2.0), [GOVERNANCE.md](../../GOVERNANCE.md); [README.md](../../README.md) license posture. Optional follow-up: enable GitHub private vulnerability reporting; add a formal CoC if the community grows. |
| Developer experience as a first-class outcome | **Addressed** 2026-04-27 — [../principles/developer-experience.md](../principles/developer-experience.md) names time-to-first-change, local loop, docs findability, cognitive load, review flow, and system-level DevEx measurement; [../checklists/developer-experience-scorecard.md](../checklists/developer-experience-scorecard.md) makes those signals reviewable. Remaining work is calibration against real adopter friction, not missing doctrine. |
| Doctrine versioning and consumer compatibility (how consumers know whether an upstream doctrine update is editorial, additive, normative, estate-only, or breaking for their local estate) | **Addressed** 2026-04-27 — [../patterns/doctrine-versioning-and-consumer-compatibility.md](../patterns/doctrine-versioning-and-consumer-compatibility.md) defines the doctrine contract, SemVer-shaped release labels, change classes, release-note minimums, consumer pinning, deprecation/removal rules, and maintainer checklist. Optional follow-up: start tagging formal doctrine releases when there is a public consumer cadence. |
| Platform engineering, golden paths, self-service, and service catalog | **Addressed** 2026-04-27 — [../patterns/platform-as-product-and-golden-paths.md](../patterns/platform-as-product-and-golden-paths.md) states platform-as-product posture, paved roads, self-service with enforced guardrails, tool-agnostic catalog metadata, scorecards, and recorded exceptions—without mandating a specific portal or catalog product. Remaining work is adoption calibration, not missing doctrine. |
| Incident command and on-call (lifecycle, severity, roles, comms, state doc, escalation, handoff, fatigue, post-incident actions) | **Addressed** 2026-04-27 — [../patterns/incident-lifecycle-and-on-call-operations.md](../patterns/incident-lifecycle-and-on-call-operations.md); principle link in [../principles/reliability-slo-incidents.md](../principles/reliability-slo-incidents.md) §3; [../patterns/chaos-engineering-and-game-days.md](../patterns/chaos-engineering-and-game-days.md) §5; [../checklists/platform-readiness.md](../checklists/platform-readiness.md); [../glossary.md](../glossary.md). Remaining: estate playbooks, paging/status tools, and severity tuning. |

---

## Bottom Line

This doctrine is already ahead of most public engineering handbooks on **portable layering**, **contracts-first delivery**, **event semantics**, **idempotency**, **merge-path evidence**, and **AI/ML governance**. The next maturity step is not more CI/security basics. It is saying the still-quiet human and adoption mechanics out loud: **capacity allocation**, **support communication**, and **data classification**—and ongoing **tuning** of **incident** and **on-call** practice to each estate. **Public project governance**, **developer experience**, **doctrine versioning / consumer compatibility**, **platform golden paths**, and **incident lifecycle / on-call** moved from gap to **addressed** portable doctrine on 2026-04-27; see the **Gap Fill Status** table above.
