# Post-v0.3.0 External Review Decisions And v0.4.0 Plan

**Status:** Accepted tasking; non-normative until the referenced ADR and doctrine changes are separately reviewed and adopted.

**Date:** 2026-07-17

**Change classes:** editorial and navigation fixes proposed for `v0.3.1`; investigation and possible normative tightening/replacement proposed for `v0.4.0`.

## 1. Review Outcome

A retrospective review found `v0.3.0` materially stronger than `v0.2.0`, especially in its compact constitution and the preservation of the AI-delivery evidence/authority kernel. It also identified three concrete defects and four broader questions.

The concrete defects are accepted for a compatible patch:

1. use **mandate class** consistently instead of alternating with **justification class**;
2. restore new glossary entries to their alphabetical sections; and
3. route the AI/ML principle to ADR 0024 **as amended by ADR 0030**.

The wider questions require a decision pass rather than a drive-by rewrite. The current lifecycle taxonomies describe different dimensions—decision gates, diagnostic states, record ownership, mandate origin, claim type, evidence provenance, and closure—but their simultaneous presentation creates cognitive load. BCP 14 defines the meaning of selected capitalised terms; it does not create a keyword quota. Semantic challenge quality depends on competence and distinct failure modes, not reviewer count alone. Published version tags, however, are consumer-facing identities and should not be treated as movable pointers.

## 2. Decision Register

| Finding | Decision | Reason |
| --- | --- | --- |
| `justification class` / `mandate class` drift | **Take in v0.3.1** | One concept needs one portable name. |
| Mis-sorted glossary entries | **Take in v0.3.1** | Pure discoverability defect. |
| AI/ML principle cites only ADR 0024 | **Take in v0.3.1** | ADR 0030 is the current operating amendment. |
| Collapse the lifecycle's projections immediately | **Investigate for v0.4.0** | The projections are not interchangeable; removal without scenario testing could lose necessary evidence or authority semantics. |
| Make the seven gates the progressively disclosed default | **Take as design objective for v0.4.0** | A reader should be able to act without first memorising every reference taxonomy. |
| Add BCP 14 keywords throughout because counts are low | **Reject** | RFC 8174 makes uppercase usage semantically meaningful; frequency is not evidence of precision. |
| Classify material lifecycle obligations claim by claim | **Take for v0.4.0** | Ambiguous material obligations should gain explicit strength, applicability, evidence, and exception handling. |
| Require another actor for every doctrine change | **Reject** | Actor count does not establish independent failure modes and would add ceremony to editorial work. |
| Require a declared semantic challenge plan for material normative releases | **Take for v0.4.0** | Mechanical checks cannot validate portability, source interpretation, or policy consequences alone. |
| History repair lacked a decision record | **Reject as factually incorrect** | [ADR 0027](../../docs/adr/0027-keep-public-doctrine-implementation-neutral.md) explicitly authorised the repair and recorded consumer impact. |
| Protect published release tags from future rewriting | **Take for v0.4.0** | Version-specific releases are consumer pins; corrections should use a new version and advisory rather than silently changing prior content. |

## 3. External Grounding And Limits

| Source | Class | Supports | Does not establish |
| --- | --- | --- | --- |
| [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) §3 | External specification | Once released, a version's contents are not modified; changes receive a new version. | A complete emergency disclosure or repository-history procedure. |
| [BCP 14](https://www.rfc-editor.org/info/bcp14) / RFC 2119 and RFC 8174 | External standard | Capitalised requirement terms have defined meanings; lowercase forms do not inherit them automatically. | How many keywords a doctrine document should contain. |
| [Google engineering review guidance](https://google.github.io/eng-practices/review/reviewer/looking-for.html) | Public practitioner guidance | Review examines design, functionality, complexity, tests, context, and reviewer competence; tests need scrutiny rather than self-validating. | A universal requirement for a named host, reviewer count, or approval workflow. |
| [GitHub immutable releases](https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases) | Vendor capability observation | A host can prevent release-tag movement and asset mutation and can attest release identity. | A portable requirement to use GitHub or any particular release product. |
| ADRs [0027](../../docs/adr/0027-keep-public-doctrine-implementation-neutral.md), [0028](../../docs/adr/0028-adopt-claim-level-authority-applicability-and-exceptions.md), and [0030](../../docs/adr/0030-refine-ai-native-sdlc-into-gates-records-and-applicability-overlays.md) | Repository decisions | Existing portability, claim-strength, and AI-delivery decisions that follow-up work must preserve. | External validation of the seven-gate or five-record-family synthesis. |

The progressive-disclosure proposal is library synthesis. It must be evaluated with representative readers and scenarios before it changes canonical structure. The review source is useful challenge evidence but remains model-produced retrospective analysis, not independent human or cross-organisation validation.

## 4. v0.4.0 Work Lanes

### V40 — Test Progressive Disclosure Before Moving Taxonomies

- **Objective:** Let a first-time reader use the seven gates without memorising the reference projections, while preserving traceability and advanced diagnostic views.
- **Owned files:** `doctrine/patterns/ai-native-software-development-lifecycle.md`, `doctrine/checklists/ai-native-sdlc-readiness.md`, and at most one new companion/reference page if the evidence supports extraction.
- **Inputs and dependencies:** ADR 0030; this decision register; routine maintenance, vulnerability response, strategic intervention, and high-materiality governed-agent scenarios.
- **Acceptance criteria:** The default path explains mandate → claims → governed work when activated → candidate → challenge → authority → enact/observe/close; S0-S10, claim types, evidence classes, mandate classes, and closure modes remain findable without being prerequisites to the first pass; no evidence or authority obligation is silently removed.
- **Verification:** Time and error a cold-reader walkthrough for the four scenarios; ask each reader to identify the applicable gate, record owner, evidence, authority, and closure; compare before/after misses rather than using document length as the success metric.
- **Stop conditions:** Stop if extraction creates duplicate normative owners, makes the checklist authoritative, or prevents reconstruction of candidate-bound evidence and authority.

### V41 — Classify Material BCP 14 Claims

- **Objective:** Make the strength of material lifecycle obligations explicit without measuring keyword density.
- **Owned files:** `doctrine/patterns/ai-native-software-development-lifecycle.md`, `doctrine/patterns/outcome-and-portfolio-linkage.md`, and derived checklist wording only where necessary.
- **Inputs and dependencies:** ADR 0028; BCP 14; V40's settled structure.
- **Acceptance criteria:** Each material obligation has documented applicability, strength/content class, expected evidence, and exception authority; capitalised keywords appear only where their BCP 14 meaning is intended; contextual guidance and examples remain visibly non-normative.
- **Verification:** Claim inventory reviewed against three low/material/high-impact consumers; search for lowercase imperative duplicates and conflicting strength; consumer-impact classification for every strengthened claim.
- **Stop conditions:** Stop if the pass becomes a keyword quota, changes obligations without migration, or assigns one strength to an entire document.

### V42 — Adopt Published-Release Immutability

- **Objective:** Make version-specific tags and attached release content stable consumer identities.
- **Owned files:** next available ADR, `doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md`, `doctrine/checklists/release-readiness.md`, `GOVERNANCE.md`, and `CONTRIBUTING.md`.
- **Inputs and dependencies:** SemVer 2.0.0 §3; ADR 0027 consequences; applicable host capabilities as optional tooling.
- **Acceptance criteria:** A published version-specific release tag `MUST NOT` move or be reused; a correction uses a new version and advisory; compromised or legally unsafe content has an explicit withdraw/revoke path that preserves the old identity and records affected consumers; moving compatibility aliases, if used, is distinguished from immutable version tags; product-specific enforcement remains optional tooling.
- **Verification:** Simulate typo correction, severe defect, credential disclosure, legal removal, and withdrawn release scenarios; each produces an unambiguous new-version or revocation action without retagging an old release.
- **Stop conditions:** Stop if the rule prevents urgent containment, hides known-bad releases, prescribes one host, or represents mutable aliases as version-specific releases.

### V43 — Require Proportionate Semantic Challenge For Material Doctrine

- **Objective:** Ensure material normative changes receive challenge capable of finding semantic, portability, source, and consumer-impact defects.
- **Owned files:** next available ADR or amendment, `doctrine/patterns/doctrine-library-change-harness.md`, `doctrine/checklists/doctrine-change-checklist.md`, `GOVERNANCE.md`, and `CONTRIBUTING.md`.
- **Inputs and dependencies:** current code-review pattern; ADR 0030 failure-mode diversity; public review guidance; V41 claim inventory.
- **Acceptance criteria:** Material normative changes declare semantic risks and challenge surfaces; mechanical validation, source checking, domain/portability review, and authority remain distinct; an author or correlated model group is not represented as independent semantic review; a sole-maintainer path records the evidence limit and uses a public review window, qualified external review, or a bounded waiver proportionate to materiality; editorial changes remain lightweight.
- **Verification:** Apply the rule to an editorial typo, a new optional example, a normative security change, and a lifecycle-wide replacement; confirm increasing discrimination without a universal reviewer-count gate.
- **Stop conditions:** Stop if the policy makes another actor sufficient by presence alone, blocks emergency correction without a bounded path, or requires external review for low-risk editorial changes.

### V44 — Decide And Integrate v0.4.0

- **Objective:** Convert V40-V43 evidence into adopted decisions and a migration-safe release.
- **Owned files:** next available ADR or ADRs, affected canonical patterns/checklists, navigation, glossary, references, and changelog.
- **Inputs and dependencies:** V40-V43 complete; no unresolved source or scenario conflict.
- **Acceptance criteria:** ADRs state take/defer/reject decisions, alternatives, consumer impact, measures, and residual risks; progressive disclosure preserves the ADR 0030 kernel; normative changes are classified as a pre-1.0 minor; no published tag is rewritten.
- **Verification:** Doctrine preflight, links, claim/terminology consistency, scenario sampling, Mermaid rendering if changed, portability scan, Git integrity, and the newly adopted semantic challenge evidence.
- **Stop conditions:** Stop release on unresolved authority/evidence collapse, unmeasured usability regression, ambiguous tag-withdrawal behaviour, or a claimed independent review that shares the producer's material failure mode.

## 5. Measures

- **Terminology:** zero current canonical uses of `justification class` for the six mandate classes.
- **Discoverability:** glossary additions appear under their alphabetical headings and all AI lifecycle decision routes include ADR 0030.
- **Usability:** cold readers complete the four V40 scenarios with fewer taxonomy-selection errors and without consulting S0-S10 unless diagnosing or migrating.
- **Normative precision:** every strengthened claim has explicit consumer impact; keyword count is not a target.
- **Challenge quality:** every material normative PR identifies at least one semantic challenge surface that can fail differently from the producer; evidence limitations remain explicit.
- **Release integrity:** zero moved or reused version-specific release tags after the rule is adopted; withdrawals and corrections point to new identities and durable advisories.

## 6. Consumer Impact

The `v0.3.1` fixes are editorial/navigation corrections and do not change adoption expectations. V40-V44 are tasking only. Any resulting BCP 14 strength, review obligation, lifecycle structure, or release-integrity rule is a prospective `0.x` minor change and requires its own ADR, migration note, review evidence, and release decision.

## Related

- [External Honest Review — Synthesis](honest-review-synthesis.md)
- [v0.3.0 Release Plan](v0.3.0-release-plan.md)
- [Doctrine Versioning And Consumer Compatibility](../patterns/doctrine-versioning-and-consumer-compatibility.md)
- [Doctrine Library Change Harness](../patterns/doctrine-library-change-harness.md)
- [AI-Native Software Development Lifecycle](../patterns/ai-native-software-development-lifecycle.md)
