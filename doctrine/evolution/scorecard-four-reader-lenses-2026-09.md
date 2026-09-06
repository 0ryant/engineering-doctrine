# Scorecard: The Library Through Four Reader Lenses (September 2026)

**Date:** 2026-09-06
**Status:** Non-normative research note. Nothing here changes doctrine by itself; the fix list at the end routes through ADRs or editorial commits.
**Scope:** The full corpus at commit `e635563` (main, after the per-principle glance landed).
**Method:** Four reviewers, each playing one reader persona against a fixed reading path, scored the library 1 to 5 on criteria that matter to that reader, with a file citation for every score. The reviewers were agent critics; this is model self-review in the sense recorded in [docs/adr/README.md](../../docs/adr/README.md), not a survey of four humans. Every score is checkable against the cited file. Two of the sharpest factual claims (the SLSA hermeticity wording and the duplicate AWS bulletin identifier) were re-verified against the files before this note was written.

Scale: 5 needs evidence a skeptic would accept; 3 is adequate; 1 is absent.

---

## 1. Summary

| Lens | Mean | Verdict | Biggest gap |
| --- | --- | --- | --- |
| Engineering manager, two product teams, ~14 engineers | 3.2 | Adopt a slice | No filled-in example of the one-page team rule set; the template is empty |
| CIO, regulated organisation, ~400 technology staff | 3.0 | Pilot only (AI adoption controls plus the controls governance programme) | No auditor-consumable crosswalk to ISO 27001, SOC 2, or CSF 2.0; recorded as a deliberate "Won't" |
| Senior application and platform security engineer | 3.0 | Adopt with a local control mapping | The SLSA section mandates hermetic, network-free builds unconditionally and labels L3 "hermetic"; flagged as M16 in August 2026, still live |
| Non-technical sponsor who depends on a software team | 2.3 | Send with a cover note | Nothing is written for a non-coder; lost at the README's first sentence; no page states cost |

**Where the lenses agree.** The newer stratum (AI adoption controls, agent identity, run contracts, models as dependencies, merge-path integrity) scores highest with every reviewer who reached it. The older core (secure development lifecycle, secrets, Kubernetes, the entry pages) is where scores fall: untyped, thinner, and front-loaded with governance machinery. Three of four said the entry path pulls a reader back into normative-language and profile mechanics before they hold a usable slice. No reviewer found sales language; honesty about limits was the top-scoring criterion for the CIO and the sponsor.

---

## 2. Engineering Manager

Persona: runs two product teams, mixed seniority, a web app plus a few services on a managed platform; wants rules the team can adopt this quarter and defend in code review; has 90 minutes.

| Criterion | Score | Evidence |
| --- | --- | --- |
| Rule set in 90 minutes | 3 | The prescribed path is ~14,000 words across 12 files; the tree is 133 files. [doctrine/README.md](../README.md) front-loads Governance & Assurance before Adoption, so time goes to the wrong shelf first. |
| Enforceable in PR review | 4 | [collaboration.md §3](../principles/collaboration.md) gives a numeric bound (~400 lines or ~20 files); [code-review-and-change-approval.md](../patterns/code-review-and-change-approval.md) §3 has a blocker/nit/editorial table and §4 a latency table; [testing-strategy.md §1](../principles/testing-strategy.md) gives pyramid targets. Docked because the same code-review file spends §5 to §6.1 on agent-definition paths and method-record trailers a web team must skip. |
| Wins the argument | 4 | Every principle file ends in a Rationale And Decisions table plus references. Not a 5: rationale rows are one-liners, enough to cite, not to persuade a senior who wants trade-offs. |
| First, second, third, and what to skip | 3 | [adoption-playbook.md §3](../patterns/adoption-playbook.md) gives an ordered five-phase table; §6 covers "≤5" and "growing / multi-team" only, so a 14-person two-team shop falls between rows and gets no skip list. |
| Scales down | 2 | [tldr-principles-and-mvp.md](../tldr-principles-and-mvp.md) tells the newcomer to apply the normative-language pattern before adding profiles; ENGINEERING.md opens with BCP 14 mechanics; [build-readiness.md](../checklists/build-readiness.md) routes to RAG tenant isolation and SLSA attestations in a checklist billed for creating a repo. |
| Quarter-one cost versus saving | 3 | The six MVD rows and playbook §8 are cheap and reuse branch-protection features; the cost is discovery and translation, since [minimum-viable-doctrine.template.md](../tooling/estates/minimum-viable-doctrine.template.md) is an empty table. |

**Verdict:** adopt a slice: collaboration §1 to §5 and §10; code-review §1 to §4 and §7; testing-strategy §1 to §4; collaboration-readiness checklist; adoption-playbook §3 and §8. Keep ENGINEERING.md, the doctrine README, the semantic index, and the normative-language, control-profile, and AI-native-SDLC patterns away from the team this quarter.

**Hand to team tomorrow:** collaboration §2 to §3 plus the code-review §3 blocker table. Together they are one page and every item maps to a branch-protection toggle or a sentence a reviewer can quote.

---

## 3. CIO

Persona: regulated organisation, several vendors, an audit function, board reporting, an active AI adoption programme; deciding whether to make the library the organisational standard; two hours plus a deputy.

| Criterion | Score | Evidence |
| --- | --- | --- |
| Auditor defensibility | 2 | The only crosswalk is [timeless-principles-and-tooling.md §6](../principles/timeless-principles-and-tooling.md), self-described as illustrative and non-exhaustive; SOC 2 and ISO mapping is recorded as "Absent (by design)" and a standing Won't in [deep-research-section-gaps.md](deep-research-section-gaps.md) and [scorecard-vs-mainstream-frameworks.md](scorecard-vs-mainstream-frameworks.md). The SP 800-171 profile pattern is a good mechanism, but the worked example is CUI. |
| Regulatory currency | 4 | [privacy-and-data-governance.md §5.4](../principles/privacy-and-data-governance.md) gives Art 50 with the provider/deployer split, the 2026-08-02 application date, the fine basis, dated Code of Practice and guidelines, and EUR-Lex canonical links; DORA Arts 28 to 29 cited canonically in [ai-adoption-controls.md §4](../patterns/ai-adoption-controls.md). Deduction: Annex III high-risk obligations appear only as vocabulary. |
| Vendor neutrality | 4 | Principles carry 19 vendor mentions across 9 of 34 files, nearly all in cost-and-finops reference lists; vendor detail is quarantined in estates. Mild pull: only the Azure supplement is filled, and CONTRIBUTING offers assistant-specific tooling. |
| Provenance and review quality | 2 | Honesty is exemplary: [docs/adr/README.md](../../docs/adr/README.md) states no ADR has independent human review and eleven ADRs carry that line. But git shows one author and one bot across 93 commits, GOVERNANCE.md names no maintainers, and ADR 0023's source paper is unidentified. |
| Maintenance model | 3 | Versioning and deprecation design is above par ([doctrine-versioning-and-consumer-compatibility.md](../patterns/doctrine-versioning-and-consumer-compatibility.md), [DEPRECATED.md](../DEPRECATED.md)). Reality: five tags in five months, three on one day, two published history rewrites requiring consumers to re-clone, and no fixed calendar. |
| Organisational cost of adoption | 3 | Tiering exists (ENGINEERING.md Minimum Viable Adoption; playbook §3 and §6). The corpus is ~96k words across 34 principles and 32 patterns, and ADR 0047 is still Proposed, so the consumer path includes library-internal governance today. |
| Executive legibility | 3 | The ten propositions are board-summarisable; playbook §4 gives three bullets of executive narrative. No executive one-pager; README's opening line is engineer-facing. |

**Verdict:** pilot only, scoped to [ai-adoption-controls.md](../patterns/ai-adoption-controls.md) with [ai-adoption-readiness.md](../checklists/ai-adoption-readiness.md) for the AI programme and [engineering-controls-governance-program.md](../patterns/engineering-controls-governance-program.md) for the audit function, under a local estate profile. Not adoptable as the engineering standard while it refuses the ISO/SOC 2 crosswalk, has a single maintainer, and has no independent domain review on record.

**Board risk as briefed:** a standard authored and reviewed by one person and their agents, with no recorded independent review, no named maintainer, and a history of rewriting published tags; if it is wrong on the EU AI Act or DORA the defence is ours alone, and if the maintainer stops we own a 96,000-word fork.

---

## 4. Security Engineer

Persona: embedded application and platform security engineer; owns CI security gates, runs threat models, has read OWASP, SSDF, SLSA, and the agentic Top 10; wants controls specific enough to implement and verify; two to three hours; checks citations.

| Criterion | Score | Evidence |
| --- | --- | --- |
| Control specificity | 3 | Strong where new: [run-contracts.md §3.2](../patterns/run-contracts.md) typed deny defaults; [dependencies-supply-chain.md §7 to §8](../principles/dependencies-supply-chain.md) pre-install registry check, digest pinning, safetensors-or-sandbox; [api-boundaries-and-security.md §5](../principles/api-boundaries-and-security.md) numeric depth and cost limits; [webhook-ingress-security.md §2](../patterns/webhook-ingress-security.md) replay window. Weak where old: [secure-development-lifecycle.md](../principles/secure-development-lifecycle.md) §1 to §4 has no gate, cadence, or evidence field; [configuration-and-secrets.md §2](../principles/configuration-and-secrets.md) says rotate on a cadence with no cadence; [kubernetes-platform-security.md](../principles/kubernetes-platform-security.md) is a headings list. |
| Threat coverage | 3 | Present: OWASP API 2023 table, merge-path invariants 1 to 9, supply chain including models, ASI01 to ASI10 crosswalk. Missing: classic app-layer OWASP Top 10 (injection, output encoding, deserialisation, file upload, session management); CI runner isolation and self-hosted-runner risk; cloud IAM beyond workload identity; redaction at emit time; detection and SIEM; sandboxed agent code execution and inter-agent signing (both admitted as not mandated in [agentic-loop-design.md](../patterns/agentic-loop-design.md)). |
| Typed strength discipline | 3 | 38 MUST/SHOULD across 8 principle files; zero in secure-development-lifecycle, api-boundaries, configuration-and-secrets, audit-logging, kubernetes, webhook-ingress, and merge-path (which uses bold "must"). New material is typed with activation conditions. The August review logged this as M18; known, unfixed. |
| Evidence quality | 3 | Spot-checks that held: the slopsquatting study figures, the Reflexion and adaptive-evaluation figures. Failures: dependencies §4 presents SLSA L3 as hermetic with separation of duties between build and signing, which SLSA v1.x does not define; [audit-logging.md](../principles/audit-logging.md) cites SP 800-53 release 5.2.0 but links the r5 update 1 URL; the same Amazon Q incident is cited as AWS-2025-019 ([REFERENCES.md](../REFERENCES.md) line 227, merge-path §3) and as AWS-2025-015 / CVE-2025-8217 (REFERENCES.md line 261, agentic-loop), and the register carries both. Verified: both identifiers are present; which is correct was not established offline. |
| Honesty about gaps | 4 | Real admissions: run-contracts §9, verifier-packs §11, the ASI crosswalk's no-coverage rows for ASI04/07/09/10, "described practice, not a mandated control", "no ratified SLSA AI/ML track", CISA 2025 elements marked draft. Loses a point because the SDL claims an SSDF mapping while covering a fraction of the 42 practices without saying so, and the Kubernetes file has no scope statement. |
| Noise | 3 | Little theatre; standards-watch blocks name vendors but flag them informative. Duplication is real: KEV/EPSS in SDL §3 and deps §2 (already drifted, M17); slopsquatting text in four places; the lethal trifecta and flat-injection-defence text repeated across ai-ml-systems and agentic-loop; SBOM obligations across deps §3, merge-path invariant 6, and build §14. Agentic-loop §§1 to 4 is a design essay with no control content. |
| Usability under fire | 2 | No one page per surface. API is closest (the OWASP table). Pipeline needs merge-path plus the tooling suite plus deps §4 to §5 plus testing §5. Agent needs agentic-loop (440 lines) plus ai-ml-systems §4 and §7 plus zero-trust §2.1 plus run-contracts. [release-readiness.md](../checklists/release-readiness.md) has one SBOM line and nothing on signature verification, secret scanning, or the adversarial gate. |

**Verdict:** adopt with a local control mapping. The CI/CD, supply-chain, and agentic material is better than most internal standards; the SDL, secrets, and Kubernetes files must be mapped onto local controls (SSDF practice IDs, rotation cadences, pod security levels) before anyone is measured against them.

**First control to enforce:** [merge-path-evidence-and-pipeline-integrity.md §2](../principles/merge-path-evidence-and-pipeline-integrity.md) invariants 2 and 3: pipeline definitions and agent-definition artefacts in the same trust class as code, owner-gated, no self-review, and any claimed gate fails the merge rather than warns. One branch-protection change, server-verifiable, closes the rules-file-backdoor class.

**Most dangerous finding:** dependencies-supply-chain §4. L2 is the baseline; the hermetic-builds bullet unconditionally mandates that the build environment cannot fetch packages from the network and that two builds produce the same output; the level table and Rationale label L3 "hermetic" with separation of duties between build and signing. SLSA v1.x defines no hermeticity requirement at any build level, and every hosted-CI L2 pipeline that resolves from a lockfile violates the bullet as written. A team can be blocked by a control SLSA does not impose, or claim L3 on a false definition. Flagged as M16 in [research-full-corpus-council-review-2026-08.md](research-full-corpus-council-review-2026-08.md); still live.

---

## 5. Non-Technical Sponsor

Persona: a small-business owner, a product lead from a marketing background, or a head of operations; knows nothing about DevOps; frustrated that the team ships late and breaks things; 30 minutes, reading like a normal person, stops at a wall of jargon.

| Criterion | Score | Evidence |
| --- | --- | --- |
| What is this, is it for me | 2 | [README.md](../../README.md) opens "Reusable engineering doctrine that separates stable principles from replaceable tooling"; neither half means anything to the persona, and nothing says who it is for. |
| Written for non-coders | 2 | The nearest thing is the Sponsor / TL;DR row in [how-to-read-this-doctrine.md](../patterns/how-to-read-this-doctrine.md), which sends the reader to the TL;DR page, whose first bullet is "Material boundaries are explicit, versioned, and verified." No page was written for this reader. |
| Jargon wall and glossary | 2 | Lost at the README's first sentence. The glossary helped once ("Quality gate") but explains "Trunk-based development" with three more unknown terms. |
| Holds my team to something | 3 | The Minimum Viable Doctrine table's Evidence column ("A new contributor can reach a checked change without private instructions"; "Owner can diagnose a representative failure") translates into questions. |
| Cost | 1 | [adoption-playbook.md §4](../patterns/adoption-playbook.md) says to "keep ranges honest" and gives no range, headcount, weeks, or disruption warning. The only numbers are reading times. |
| Trust and honesty | 4 | Playbook §1 "Expect: disagreement on specific principles"; §7 "doctrine text alone does not validate"; ENGINEERING.md "It does not make every control applicable to every system." Nobody is selling a miracle. |

**Would send it:** yes, with a cover note asking the team to read the TL;DR page and the playbook, say which of the six basics exist, and estimate weeks, people, and risk for the missing ones.

**Monday questions the persona could derive** (four with confidence, a fifth as a stretch): is there one automatic check on every change that never gets skipped; can anyone push straight to live without a second person looking; could a new hire make a small safe change by Friday from what is written down; when something breaks, who owns undoing it and where is the learning written; and (stretch) are we shipping smaller and breaking less than three months ago, with numbers.

**Where the persona got lost:** README.md, first sentence. Did not recover in ENGINEERING.md; stopped at "preserve an activated contract, authority, or interoperability boundary".

**Where it clicked:** adoption-playbook §8, the row "Leadership wants a date, not doctrine" and its answer about fewer rollbacks and faster patches; and §3 Phase 1, "one command that fails on fmt/lint/tests" paired with "creates safety to change process".

---

## 6. Fix List

Ranked by how many lenses each moves. None is executed by this note.

| # | Fix | Lenses moved | Route |
| --- | --- | --- | --- |
| 1 | Correct dependencies-supply-chain §3 to §5: type the claims, split reproducible inputs (required) from hermeticity (context-dependent), fix the L3 row against the current SLSA spec; resolve M16 and M18 together. Reconcile the AWS bulletin identifier across REFERENCES.md lines 227 and 261, merge-path §3, and the CHANGELOG. | Security, CIO | ADR (normative tightening) |
| 2 | Ship one worked instance of the minimum-viable-doctrine template for a two-team web shop, each row linking a section, beside the empty template; add a mid-size row to playbook §6 that names what to skip. | Manager, sponsor | Editorial plus estate example |
| 3 | A one-screen page for sponsors and non-engineers: the six MVD rows as plain questions with what a good answer sounds like, linked from the README's first paragraph; an honest cost table in playbook §4. | Sponsor, CIO | Editorial (navigation) |
| 4 | Reorder the doctrine README so Adoption precedes Governance & Assurance; drop the TL;DR instruction to read the normative-language pattern before starting the MVD. | Manager, sponsor | Editorial; partly addressed by ADR 0047 |
| 5 | A conceptual control crosswalk as an estate supplement (principle or pattern to CSF 2.0 category, ISO 27001:2022 Annex A ID, SOC 2 criterion), banner-marked non-normative. Revisits the standing Won't in scorecard-vs-mainstream-frameworks.md. | CIO | ADR (reverses a recorded decision) |
| 6 | Three security surface cards (API, pipeline, agent) listing only typed controls with the verifying check and file anchor; expand release-readiness with signature verification, secret scan, and adversarial-gate evidence lines. | Security | Checklist plus editorial |
| 7 | One independent human review on record: named role, date, findings, disposition, on one ADR. | CIO | Governance |

Two items are already in flight: ADR 0047 addresses the entry-path problem in items 3 and 4, and the per-principle glance landed at `e635563` is a first step on item 4.

---

## 7. Provenance

Four agent reviewers, one per persona, each given the persona, a fixed reading path, and the criteria above; run in parallel on 2026-09-06 against the working tree at `e635563`. Their reports were condensed into this note without changing scores or evidence. The security reviewer's two sharpest claims were re-verified by reading the cited lines. This is model self-review; no human played any of the four roles. The persona for the sponsor is a stipulated non-expert, so its scores measure the library's reachability, not its correctness.
