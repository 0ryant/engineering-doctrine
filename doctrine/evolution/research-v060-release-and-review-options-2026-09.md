# v0.6.0 Release Identity And Semantic Review Options

Date: 2026-09-19
Status: Decision preparation only; no policy adopted.
Evidence: Repository inspection, primary-source checks and model scenario review.
No independent human review, operational trial or release approval is claimed.

This note prepares [roadmap V42–V43](post-v0.3.0-external-review-decisions-and-v0.4.0-plan-2026-07.md).
The [readiness ledger](v060-readiness-2026-09.md) still owns open-work accounting.
Existing [versioning](../patterns/doctrine-versioning-and-consumer-compatibility.md),
[review](../patterns/code-review-and-change-approval.md),
[claim authority](../patterns/normative-language-applicability-and-exceptions.md)
and [source admission](../patterns/source-authority-and-evidence-grading.md)
remain authoritative. This note neither changes their duties nor accepts a new ADR.

## V42: Stable Release Identity, With A Containment Path

The current versioning pattern defines compatibility and consumer pinning but
does not yet land the roadmap's full tag-immutability and withdrawal procedure.
Three options are ready for a final decision:

| Option | Consumer effect | Unresolved cost or defect |
| --- | --- | --- |
| Keep existing policy only | No new maintainer duty | V42 remains unmet; correction and withdrawal behaviour stays incomplete |
| Preserve version identity; issue corrections under new versions; record withdrawal without reusing the identity | Consumers can distinguish the revision they adopted from its replacement | Needs an accepted ADR, advisory/withdrawal procedure and evidence retention boundary |
| Require one host's immutable-release feature | Enforced tag/asset protection on that host | Couples portable policy to a product; metadata and emergency containment still need separate treatment |

The second option is the recommended proposal, **not an adopted requirement**.
Its boundary is identity, not an obligation to keep dangerous bytes publicly
available. A withdrawn version remains reserved in the advisory/history even
when access to affected content must be restricted or removed. No replacement
bytes inherit the old version. Moving aliases, if introduced, are clearly
different from version-specific tags.

### Model Scenario Checks

These are desk exercises against the proposed second option, not live host tests.

| Scenario | Proposed response | Evidence needed before closure |
| --- | --- | --- |
| Typo in released doctrine | Correct source and publish a new version when shipping the correction; leave the old version identifiable | Old/new commit IDs, change class and correction note |
| Severe semantic defect | Advisory and correction under a new version; identify affected pins and discourage unsafe adoption | Defect scope, replacement, consumer notification or documented discovery limits |
| Credential disclosure | Revoke/rotate immediately, restrict or remove exposed bytes as needed, record withdrawal; never repurpose the old version | Containment record, affected identities, secure evidence handling; no secret copied into the advisory |
| Legally unsafe content | Follow the applicable removal decision while retaining only permissible identity/tombstone metadata | Responsible authority and permitted record boundary; no assertion that public archival retention is always lawful |
| Withdrawn release without replacement | Reserve the version and publish its status; do not point its tag at a different candidate | Withdrawal reason, scope, consumer guidance and any still-supported alternative |

The proposal preserves urgent containment and distinguishes immutable identity
from perpetual availability. Exact host actions, legal authority and advisory
ownership are final-phase decisions. No tag, release asset or repository setting
has been changed by this investigation.

## V43: Challenge The Meaning, Not Just The Markdown

Existing review doctrine already separates blockers, high-risk paths and human
accountability. The remaining V43 decision is how the **library itself** records
proportionate semantic challenge without counting reviewers as proof.

Proposed evidence separation:

| Surface | What it can show | What it cannot establish alone |
| --- | --- | --- |
| Mechanical checks | Links, schema examples, formatting and repository invariants | Correct engineering policy |
| Source checks | The cited revision actually supports a scoped statement | Applicability to every consumer |
| Semantic/domain challenge | Counterexamples, authority conflicts, portability and adoption consequences | Maintainer acceptance authority |
| Acceptance record | Who accepted the candidate, scope, exceptions and residual risk | That an unperformed review occurred |

An author re-read or correlated model review can expose defects, but is not
independent human evidence. A sole-maintainer policy could use a materiality-
appropriate public review window, qualified external review, or a bounded waiver
with owner, expiry, review trigger and compensating evidence. Silence during a public
window is not a favourable review. A model reviewer is not a substitute for the
human usability evidence still outstanding under V40.

### Model Scenario Checks

| Change | Proposed challenge | Deliberately not prescribed |
| --- | --- | --- |
| Editorial typo | Diff review and applicable mechanical checks; confirm meaning unchanged | External review or a universal waiting period |
| Optional example | Check owner traceability, applicability, runnable claims and accidental obligations | A full policy review solely because a file is new |
| Normative security change | Claim/source admission, abuse counterexample, affected-consumer and exception review; disclose reviewer limitations | Green CI as semantic approval |
| Lifecycle-wide replacement | Trace old duties to new owners, test low/material/high-impact consumers and migration/closure cases; record unresolved losses | Document shortening as proof of usability |

Options for the final phase are to adopt this risk-scaled record through an ADR,
retain the current process and leave V43 open, or adopt a fixed reviewer-count
rule. The last option does not itself discriminate correlated failures and is
not recommended. No minimum count or arbitrary review-window duration is
introduced here.

## Source Ledger And Admission Limits

All entries were accessed on 2026-09-19. Classes follow the existing source
pattern; class does not imply support for an unrelated policy. The full V42/V43
proposals are repository design judgments, not requirements attributed to these
publishers. Any later typed obligation still needs claim-level admission and,
where applicable, an explicit risk-asymmetry rationale or registered exception.

| Source | Class / pin / role | Supports | Does not establish |
| --- | --- | --- | --- |
| [SemVer 2.0.0 §3](https://semver.org/spec/v2.0.0.html) | S1, version-pinned norm, primary; published specification | Released version content is stable; modified content receives a new version | This library's full withdrawal, notification or retention policy |
| [GitHub immutable releases](https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases) | S5, rolling product documentation, primary; recheck before any host configuration | Protection of published release tags/assets; notes and some metadata remain editable; platform-specific deletion constraints | That this repository enabled the feature, or that host mechanics define portable policy |
| [Google review guidance](https://google.github.io/eng-practices/review/reviewer/looking-for.html) | S6, rolling first-party practice, primary; recheck if relied on at adoption | Review includes design, functionality, complexity and test quality | A causal improvement estimate or a universal review quorum |
| [NIST SP 800-218, SSDF 1.1, PW.7.1–PW.7.2](https://doi.org/10.6028/NIST.SP.800-218) | S2, February 2022 publication pin, primary; inspected the published PDF, not a claim that it is the latest revision | Organisation-defined review/analysis methods and recording/triage of findings | A mandate for this doctrine's proposed semantic-review procedure |

No public archived URLs were created. Local captures permit reproduction only
where retained; they are not public durable archives. Capture SHA-256 values:

| Source | SHA-256 |
| --- | --- |
| SemVer HTML | `f9d4b8b1a5e9a0de6621dbbc70d69fdf05310b7a737509317b94a7bddfb9409e` |
| GitHub HTML | `372c143feb9ad2538479a4d53ff0a465f38bebf40ae3aa95958ab5f2bc236aa4` |
| Google HTML | `5946a2fa713dbafed9a2846e187be7705e3f3240c2b925f13d45530791c0e4af` |
| NIST PDF | `617746e553a9e2da49bfbd4eef0dfc3094758a39b869314e4173ac36605cde22` |

## Final-Phase Landing, If Approved

V42 would land in a new ADR, versioning, release readiness, governance and
contribution instructions. V43 would land in an ADR or amendment, the change
harness, doctrine-change checklist, governance and contribution instructions.
Both need consumer-impact labels and derived-route checks under
[ADR 0049](../../docs/adr/0049-add-doctrine-integrity-gates-and-obligation-routing.md).
Until then, source research and simulated scenarios are preparation, not closure.
