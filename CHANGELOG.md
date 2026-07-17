# Changelog

<!-- markdownlint-configure-file {"MD013": false, "MD024": {"siblings_only": true}} -->

All notable changes to this **engineering doctrine** library are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) (human-readable history). This repository uses **SemVer-shaped tags** for the *doctrine* contract, not for npm/cargo units—see [doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md](doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md) for patch / minor / major meaning, change classes, and release note expectations.

## [Unreleased]

**Compatibility proposal:** `v0.3.1` patch. The implemented changes are editorial and navigation corrections; the linked `v0.4.0` items remain non-normative tasking.

### Added

- [Post-v0.3.0 External Review Decisions And v0.4.0 Plan](doctrine/evolution/post-v0.3.0-external-review-decisions-and-v0.4.0-plan-2026-07.md) — take/defer/reject register and executable tasks for progressive disclosure, claim-level BCP 14 review, proportionate semantic challenge, and prospective published-release immutability.

### Fixed

- Standardised the six AI-delivery justification categories on the canonical term **mandate class** and added the term to the glossary.
- Restored `Exception`, `Governed execution`, `Mandate / mandate class`, `Normative terms`, and `Record families` to their alphabetical glossary sections.
- Updated the AI/ML principle's lifecycle decision route to cite ADR 0024 as amended by ADR 0030.

## [0.3.0] - 2026-07-17

Precision and applicability release. **Change classes:** normative replacement,
normative tightening, additive guidance, navigation, and editorial correction.
**Compatibility:** intentional pre-1.0 minor; pinned consumers must review the
migration before adoption.

### Added

- [Normative Language, Applicability, And Exceptions](doctrine/patterns/normative-language-applicability-and-exceptions.md) — claim-level BCP 14 strength, composable profiles, a portable bounded-exception contract, and control simplification/retirement rules; grounded by [research](doctrine/evolution/research-doctrine-authority-applicability-2026-07.md) and [ADR 0028](docs/adr/0028-adopt-claim-level-authority-applicability-and-exceptions.md).
- [Outcome And Portfolio Linkage](doctrine/patterns/outcome-and-portfolio-linkage.md) — optional objective → measures/guardrails → intervention → work/output → observed-outcome → continue/change/stop overlay for strategic work and externally required lineage. Routine maintenance and obligations do not invent KPIs.
- [ADR 0029](docs/adr/0029-adopt-a-compact-non-duplicative-core-constitution.md) — makes `ENGINEERING.md` a compact core constitution and route map rather than a duplicate canonical corpus.
- [ADR 0030](docs/adr/0030-refine-ai-native-sdlc-into-gates-records-and-applicability-overlays.md) — amends ADR 0024 with seven operational gates, five record families, governed-execution activation, typed claims, failure-mode-diverse challenge, federated authoritative records, and three closure modes.

### Changed

- [ENGINEERING.md](ENGINEERING.md) now owns ten compact propositions and routes detailed obligations to their canonical principle or pattern. Evolution notes remain available as evidence/history but are not default operating authority.
- [AI-Native Software Development Lifecycle](doctrine/patterns/ai-native-software-development-lifecycle.md) preserves the evidence/authority kernel while replacing S0–S10 as the primary operating vocabulary. Its four-column Mermaid uses equal vertical lanes, dark text, and bottom-to-top handoffs. The [readiness checklist](doctrine/checklists/ai-native-sdlc-readiness.md) now activates baseline, governed-execution, multi-agent/long-running, high-materiality, and strategic-outcome profiles separately.
- [Run Contracts](doctrine/patterns/run-contracts.md) now apply to governed execution rather than every incidental model interaction. Tool use, persistent mutation, sensitive data, asynchronous/delegated work, material budget, cross-system scope, controlled-path output, or material reliance still activate the contract. The v1 schema is unchanged; host/workflow policy owns limits that v1 cannot express.
- Multi-agent guidance now requires owned workspaces or an explicit merge protocol, authority attenuation, bounded delegation, typed handoffs treated as claims, cancellation propagation, resume revalidation, and shared-state reconciliation.
- Broad claims were made proportional: retry boundaries need a duplicate strategy without making every domain transition idempotent; audit evidence targets material actions; TDD is one evidence-producing technique; CloudEvents is the portable event-envelope default with a documented-equivalent path; cryptography follows maintained applicable profiles; ports/adapters, I/O placement, layering, module evolution, and replication are context-based.
- Material engineering controls now record the failure addressed, evidence, owner, operating cost, effectiveness, review trigger, and simplify/retire condition. Exceptions and failed evidence remain separate.

### Consumer Impact

- **All consumers:** review the compact constitution, claim-level strength, applicability composition, and exception semantics. A shorter umbrella does not weaken the linked topic rules.
- **AI-assisted delivery:** distinguish incidental assistance from governed execution; map existing S0–S10 fields to the seven gates; group linked records into the five families; keep challenge and authorisation separate; select technical, operational, or strategic outcome closure explicitly.
- **Strategic/product work:** use the outcome overlay when attempting to change a stakeholder outcome. Other mandate classes retain traceability without fictional product metrics.
- **Event-driven systems:** CloudEvents remains the portable default; a governing protocol, platform, external contract, legacy boundary, or material constraint may justify a documented equivalent while versioned payload and delivery-semantics obligations remain.
- **Control owners:** add lifecycle records for material controls, not a governance ticket for every low-risk lint rule.

### Repository History Repair

- Published branch and tag history is rewritten to remove a non-portable local coordination-path reference from ADR 0009. The doctrinal decision is unchanged, but affected commit and annotated-tag object identities change.
- Consumers with existing clones or branches based on the earlier history must force-refresh branches and tags, then rebase or cherry-pick private work onto the rewritten references. Do not merge the old and rewritten histories together.

### Migration

1. Refresh rewritten branches and tags before adopting `v0.3.0`; preserve private work by rebasing or cherry-picking it onto the new references.
2. Pin and review `v0.3.0`; map any copied `ENGINEERING.md` detail to the canonical topic links.
3. Classify material adopted claims and active profiles; migrate live exceptions into the bounded record while preserving failed or inconclusive evidence.
4. For AI delivery, replace mandatory eleven-status workflow encoding with the seven gates and activate run contracts only at the governed-execution boundary.
5. Keep routine maintenance, obligations, incidents, compatibility, risk-reduction, and enabling work on an accountable mandate; activate objective/measure/intervention lineage only where applicable.
6. Recalibrate material controls and remove duplicate ceremony only through accountable evidence and authority.

### Evidence

- Decisions and source limits: ADRs 0028–0030 and their linked research ledgers. External support is distinguished from vendor observation and library synthesis.
- Primary grounding rechecked on 2026-07-17: BCP 14/RFC 2119/8174, RFC 9110, NIST CSF 2.0/SP 1301/SP 1303, NIST SSDF/SP 800-218A, NIST AI RMF, OWASP guidance, CloudEvents, SLSA provenance, NCSC secure-AI guidance, DORA, and applicable legal/standards sources.
- Release-candidate checks: doctrine preflight, contract-schema validation, Python compilation, Markdown links, Mermaid render and visual inspection, portability/current-history scans, scenario sampling, whitespace checks, and Git object integrity.

## [0.2.0] - 2026-07-17

Second SemVer-tagged doctrine release. **Change classes:** additive guidance,
normative tightening for AI/agent consumers, normative replacement for the
portable-doctrine and licence boundaries, and repository-history repair.
**Compatibility:** intentional `0.x` minor; every pinned consumer must review
the migration notes before upgrading.

### Added

- [doctrine/patterns/ai-native-software-development-lifecycle.md](doctrine/patterns/ai-native-software-development-lifecycle.md) — **doctrine-grounded AI-native SDLC**: stakeholder need → objective/standing obligation → guardrailed outcome measures → intervention hypothesis → bounded work → outputs → observed outcomes → portfolio decision; S0 observed need → S10 reconciled; transition admissibility, layered evidence, authority separation, deterministic enactment, brownfield P0–P5; with [readiness checklist](doctrine/checklists/ai-native-sdlc-readiness.md), [research basis](doctrine/evolution/research-ai-native-sdlc-2026-07.md), and [ADR 0024](docs/adr/0024-adopt-a-doctrine-grounded-ai-native-software-development-lifecycle.md). **Consumer impact:** normative tightening for lifecycle-wide AI/agent consumers; adopt traceability and run contracts before expanding tool authority. **Compatibility proposal:** 0.x minor; pinned consumers must review before upgrading.
- [doctrine/patterns/revision-pinned-control-profiles.md](doctrine/patterns/revision-pinned-control-profiles.md) — revision-pinned external control profiles, using NIST SP 800-171 Rev. 3 and explicitly authorised Rev. 2 obligations as the worked example; with [research basis](doctrine/evolution/research-nist-sp-800-171-control-profiles-2026-07.md) and [ADR 0026](docs/adr/0026-adopt-revision-pinned-external-control-profiles.md). **Consumer impact:** only consumers with an applicable CUI or other external-profile authority need adopt the profile record and migration controls.
- [doctrine/patterns/ai-adoption-controls.md](doctrine/patterns/ai-adoption-controls.md) — **AI adoption controls**: system **inventory + materiality** tiers, named ownership with **independent challenge**, **harm-surface** testing, **third-party continuity**, workforce **literacy**; with [checklists/ai-adoption-readiness.md](doctrine/checklists/ai-adoption-readiness.md) (reviewable execution) and research basis [evolution/research-ai-adoption-control-gaps-2026-07.md](doctrine/evolution/research-ai-adoption-control-gaps-2026-07.md) (**A1–A8** gaps); [ADR 0023](docs/adr/0023-add-ai-adoption-control-coverage-inventory-challenge-testing-continuity-literacy.md).
- [doctrine/patterns/agentic-loop-design.md](doctrine/patterns/agentic-loop-design.md) — **agentic loop** design: ReAct, **verifiability gate**, ISC, **dual-path injection defence**, context engineering, verbal RL, **autonomy slider**.
- [doctrine/patterns/feature-flag-lifecycle.md](doctrine/patterns/feature-flag-lifecycle.md) — **feature flag** lifecycle (creation → rollout → retirement).
- [doctrine/principles/cost-and-finops.md](doctrine/principles/cost-and-finops.md) — **FinOps** / cost as an engineering concern.
- [doctrine/principles/platform-engineering.md](doctrine/principles/platform-engineering.md) — **platform engineering** principle layer.
- [evolution/scorecard-vs-mainstream-frameworks.md](doctrine/evolution/scorecard-vs-mainstream-frameworks.md) — competitive **scorecard vs 11 mainstream frameworks**.

- [evolution/mythos-era-engineering-principles-research-2026-04-28.md](doctrine/evolution/mythos-era-engineering-principles-research-2026-04-28.md) — **AI vulnerability storm / Mythos-era** engineering research (principle clusters, external anchors); [ADR 0010](docs/adr/0010-record-mythos-era-vulnerability-storm-research-and-doctrine-gaps.md) tracks research adoption and **G1–G6** closure in corpus. Wired from [doctrine/README](doctrine/README.md), [REFERENCES](doctrine/REFERENCES.md), [glossary](doctrine/glossary.md), [secure-development-lifecycle](doctrine/principles/secure-development-lifecycle.md), [ENGINEERING](ENGINEERING.md).

- [evolution/public-doctrine-taxonomy-scorecard-and-choice-2026-04-27.md](doctrine/evolution/public-doctrine-taxonomy-scorecard-and-choice-2026-04-27.md) — **Taxonomy** (A–J) of public doctrine types, **honest** refreshed scorecard vs April benchmark, **which external source to lead with when** table, when *this* library is wrong primary; cross-linked from [evolution](doctrine/README.md#meta-how-to-read-this-repo).

- [doctrine/patterns/code-review-and-change-approval.md](doctrine/patterns/code-review-and-change-approval.md) — author and reviewer **duties**, **blocker** vs **non-blocker** policy, **review latency** example targets, **high-risk** change classes, **agent-authored** / LLM diffs, **escalation** when review disagrees; [ADR 0008](docs/adr/0008-add-code-review-and-change-approval-pattern.md).
- [doctrine/patterns/gitops-and-declarative-operations.md](doctrine/patterns/gitops-and-declarative-operations.md) — **GitOps** invariants (declarative state, **reconciliation**, **drift**, **secrets**); [ADR 0009](docs/adr/0009-add-gitops-and-declarative-operations-pattern.md).

### Changed

- **Portable-doctrine boundary and history repair** — [ADR 0027](docs/adr/0027-keep-public-doctrine-implementation-neutral.md) removes organisation-private product names, internal repository links, and local execution/gap records from publishable doctrine; reusable decisions and examples now use capability-class wording. Reachable branch/tag history is rewritten, so commit-pinned consumers must re-fetch or re-clone and select a reviewed replacement pin. **Change class:** normative replacement plus history repair. **Compatibility proposal:** next `0.x` minor with an explicit breaking source-control notice.
- **Repository branch hygiene** — completed and superseded feature heads were removed after their exact rewritten history was made reachable from `archive/pre-v0.2.0-divergent-branches-20260717`; the two explicitly named stash-backup branches remain as unmerged recovery records rather than active delivery branches.
- **Project licence restored to Apache-2.0** — [ADR 0025](docs/adr/0025-restore-apache-2.0-as-project-license.md) supersedes the untagged AGPL-3.0-or-later default-branch experiment. Material published during that interval is additionally offered under Apache-2.0; prior AGPL grants remain valid. **Change class:** normative replacement, rights-expanding for consumers. **Consumer impact:** no migration required; consumers may adopt, copy, and adapt under Apache-2.0. **Compatibility proposal:** next `0.x` minor.
- **ADR 0024 anchors** — lifecycle composition in [ai-ml-systems.md](doctrine/principles/ai-ml-systems.md), [secure-development-lifecycle.md](doctrine/principles/secure-development-lifecycle.md), [tooling/ai-assisted-development.md](doctrine/tooling/ai-assisted-development.md), and navigation/vocabulary surfaces. No universal transition schema is adopted without representative brownfield evidence.
- **ADR 0024 vendor-source refinement** — AWS, Microsoft, and Anthropic observations add explicit multi-agent lineage/workspace ownership, long-running checkpoints and safe resume, isolated execution of untrusted candidates, action-level receipts without chain-of-thought dependence, operations-originated S0 feedback, and coordination/demand-amplification measures. Vendor speed claims, renamed rituals, and product stacks remain non-normative.
- **ADR 0024 objective-to-outcome grounding** — direct canonical citations to COBIT's goals cascade, GQM/GQM+Strategies, NIST AI RMF, DORA metric guidance, and Google's practitioner OKR guidance support strategy lineage and measurement. Human governance owns objectives, measure validity, priority, capacity, and stop/change/continue decisions; AI may propose mappings and bounded work, but task or output completion is not outcome proof.
- **ADR 0023 anchors** — adoption-control cross-wiring into normative text: [ai-ml-systems.md](doctrine/principles/ai-ml-systems.md) (around-the-system layer, capability × materiality), [reliability-slo-incidents.md](doctrine/principles/reliability-slo-incidents.md) §7 (**dependency continuity** for external model providers), [threat-modeling-stride-lite.md](doctrine/principles/threat-modeling-stride-lite.md); navigation + vocabulary: [glossary](doctrine/glossary.md), [REFERENCES](doctrine/REFERENCES.md), [ENGINEERING](ENGINEERING.md), [doctrine/README](doctrine/README.md), [SEMANTIC_INDEX](doctrine/SEMANTIC_INDEX.md), [SITEMAP](doctrine/SITEMAP.md).
- **Gap-fill expansions** — [observability.md](doctrine/principles/observability.md) (multi-window **burn-rate alerting**), [dependencies-supply-chain.md](doctrine/principles/dependencies-supply-chain.md) (**SLSA / Sigstore / SBOM**), [rag-retrieval-baseline.md](doctrine/patterns/rag-retrieval-baseline.md) (cross-links to agentic-loop-design).

- **ADR 0010 gap closure (G1–G6)** — Six parallel research passes (NIST/CISA/OWASP/FIRST/ISO anchors) synthesized into normative text: [secure-development-lifecycle.md](doctrine/principles/secure-development-lifecycle.md), [dependencies-supply-chain.md](doctrine/principles/dependencies-supply-chain.md), [measurement-and-dora.md](doctrine/principles/measurement-and-dora.md), [merge-path-evidence-and-pipeline-integrity.md](doctrine/principles/merge-path-evidence-and-pipeline-integrity.md), [testing-strategy.md](doctrine/principles/testing-strategy.md), [threat-modeling-stride-lite.md](doctrine/principles/threat-modeling-stride-lite.md), [incident-lifecycle-and-on-call-operations.md](doctrine/patterns/incident-lifecycle-and-on-call-operations.md), [ai-ml-systems.md](doctrine/principles/ai-ml-systems.md), [code-review-and-change-approval.md](doctrine/patterns/code-review-and-change-approval.md), [tooling/merge-path-and-pipeline-control-suite.md](doctrine/tooling/merge-path-and-pipeline-control-suite.md); [ADR 0010](docs/adr/0010-record-mythos-era-vulnerability-storm-research-and-doctrine-gaps.md) updated with closure table; [REFERENCES](doctrine/REFERENCES.md), [ENGINEERING](ENGINEERING.md).

- [doctrine/patterns/gitops-and-declarative-operations.md](doctrine/patterns/gitops-and-declarative-operations.md) — lead with **OpenGitOps** v1.0.0, **OWASP** CI/CD top risks, **NIST** SSDF and **12factor** config pointers; in-repo links moved to a **secondary** “alignment” section; [REFERENCES.md](doctrine/REFERENCES.md) and [glossary](doctrine/glossary.md) **GitOps** entry updated for external **bibliography**.

### Consumer impact

- **Commit-pinned, fork, subtree, and submodule consumers:** this release follows a history rewrite. Re-fetch with pruning or re-clone, review `v0.2.0`, and replace the old pin. Do not merge unrelated pre-rewrite and rewritten histories.
- **AI/agent delivery consumers:** adopt objective-to-outcome lineage, run contracts, independent challenge, evidence-bound authorisation, deterministic enactment, and runtime reconciliation before expanding agent authority.
- **Consumers subject to CUI or another external control profile:** record the governing authority, exact revision, boundary, organisation-defined parameters, assessment basis, exceptions, and migration state. Do not infer applicability from this library alone.
- **Other consumers:** the new control-profile material is optional unless an external authority makes it applicable. Apache-2.0 remains the project licence.

### Migration

1. Re-clone or fetch with pruning, then pin the reviewed `v0.2.0` tag.
2. AI/agent consumers should follow P0–P5 in the AI-native SDLC pattern; do not increase tool or production authority ahead of the corresponding evidence and authorisation controls.
3. Externally regulated consumers should select a revision from the governing agreement, not from a generic “latest” or “NIST compliant” label, and retain old and new evidence separately during migration.
4. Preserve estate-specific tooling and rollout records outside this portable library.

### Evidence

- Decisions and source grounding: ADRs 0023–0027 and their linked research notes.
- Delivery record: merged pull requests [#15](https://github.com/0ryant/engineering-doctrine/pull/15), [#16](https://github.com/0ryant/engineering-doctrine/pull/16), [#17](https://github.com/0ryant/engineering-doctrine/pull/17), and [#18](https://github.com/0ryant/engineering-doctrine/pull/18).
- Release comparison: [`v0.1.0...v0.2.0`](https://github.com/0ryant/engineering-doctrine/compare/v0.1.0...v0.2.0).
- Verification on the release revision: doctrine preflight, contract-schema positive and negative cases, Python compilation, Markdown links, Mermaid rendering, private-name/history scans, and Git object integrity.

## [0.1.0] - 2026-04-27

First public SemVer-tagged release ([`v0.1.0`](https://github.com/0ryant/engineering-doctrine/releases/tag/v0.1.0)). **Change classes** (summary): *navigation* + *additive guidance* with some *normative* additions in new files; *compatibility* treated as **0.x minor** (review before pin upgrade).

### Added

- **Project meta:** [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), [GOVERNANCE.md](GOVERNANCE.md), [LICENSE](LICENSE) (Apache-2.0), [.gitignore](.gitignore) (excludes local `.cursor/` and `.DS_Store`).
- **ADRs** under [docs/adr/](docs/adr/) (0001–0007: library shape, trunk and CloudEvents defaults, layer split, navigation and glossary, AI/ML and agents, governance navigation, developer experience as a first-class concern).
- **Patterns:** [incident-lifecycle-and-on-call-operations.md](doctrine/patterns/incident-lifecycle-and-on-call-operations.md), [platform-as-product-and-golden-paths.md](doctrine/patterns/platform-as-product-and-golden-paths.md), [engineering-controls-governance-program.md](doctrine/patterns/engineering-controls-governance-program.md), [doctrine-versioning-and-consumer-compatibility.md](doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md).
- **Principles / tooling:** [developer-experience.md](doctrine/principles/developer-experience.md), [merge-path-evidence-and-pipeline-integrity.md](doctrine/principles/merge-path-evidence-and-pipeline-integrity.md), [merge-path-and-pipeline-control-suite.md](doctrine/tooling/merge-path-and-pipeline-control-suite.md).
- **Checklists:** [developer-experience-scorecard.md](doctrine/checklists/developer-experience-scorecard.md), [governance-program-readiness.md](doctrine/checklists/governance-program-readiness.md).
- **Evolution / research:** [public-doctrine-benchmark-gap-analysis-2026-04.md](doctrine/evolution/public-doctrine-benchmark-gap-analysis-2026-04.md), [anti-patterns-and-failure-modes-gap-analysis-2026-04.md](doctrine/evolution/anti-patterns-and-failure-modes-gap-analysis-2026-04.md).

### Changed

- **Umbrella and navigation:** [README.md](README.md), [ENGINEERING.md](ENGINEERING.md), [doctrine/README.md](doctrine/README.md), [doctrine/REFERENCES.md](doctrine/REFERENCES.md), [doctrine/SITEMAP.md](doctrine/SITEMAP.md), [doctrine/glossary.md](doctrine/glossary.md), and touch-ups across build/collaboration/doctrine checklists, adoption playbook, chaos, how-to-read, documentation-knowledge, measurement, reliability, tldr, and related evolution notes.
- **Default branch license:** the canonical license for this tree is **Apache-2.0** (see README). An earlier default-branch commit added a **MIT** `LICENSE`; that line of history is superseded for **current** consumers—do not assume MIT for the library as it ships from `main` at this tag.

### Consumer impact

- **All consumers:** pin imports to **`v0.1.0`** (or this commit) when you need a stable policy snapshot; re-read [GOVERNANCE.md](GOVERNANCE.md) and [CONTRIBUTING.md](CONTRIBUTING.md) for process and security reporting.
- **Teams adopting governance / incident / platform / DevEx guidance:** start from the new patterns and checklists above, then map local `.doctrine/` overrides.
- **Forks and subtree users:** if you had copied MIT-only language from a prior `main` tip, reconcile with Apache-2.0 before redistributing.

### Evidence

- Git: tag **`v0.1.0`**, commit on `main` at time of tag (see [diff since merge of prior `main` tip](https://github.com/0ryant/engineering-doctrine/compare/93c2516...v0.1.0) for the release changeset).
- In-repo: [docs/adr/](docs/adr/) and [doctrine/evolution/](doctrine/evolution/) cross-links above.
