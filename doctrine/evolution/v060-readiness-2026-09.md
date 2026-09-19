# v0.6.0 Readiness And Finding Reconciliation

Date: 2026-09-19
Status: Work in progress; not a release approval.
Evidence class: Repository inspection, executable checks where named, and model
review. No independent human cold-reader or domain review is claimed.

The [release roadmap](post-v0.3.0-external-review-decisions-and-v0.4.0-plan-2026-07.md)
owns acceptance criteria. This note reconciles its historical inputs against
commit `c82af3b3ee76b6888ca0787b2edcfff65b1f8181` and the linked correction batches.
The integrity batch landed in [PR #30](https://github.com/0ryant/engineering-doctrine/pull/30)
at `e21bb294d1010c4353d66a419c15d57c0acf3349`. The subsequent
[source-maintenance batch](research-v060-source-maintenance-2026-09.md) is
identified separately below. Neither weakens criteria to make a release pass.

## Accounting Correction

The [August corpus review](research-full-corpus-council-review-2026-08.md) reports
2 blockers, 20 majors and 31 minors. Its actual tables contain **2 blockers,
22 majors and 30 minors: 54 findings**. Minor IDs below identify their original
table order; no thirty-first minor has been invented. The historical report
remains intact apart from a pointer to this correction.

At the baseline, model source inspection classified 17 rows as resolved,
7 partial and 30 open. “Resolved” means the specific reported defect is fixed
or the allegation is explicitly rejected after inspection; it is not a verdict
on neighbouring content, external source currency or runtime effectiveness.

## Blockers And Majors

Paths in this table name the current canonical surface under `doctrine/`.
“This batch” in the original rows means the PR #30 integrity batch, not the
baseline or a released version. Later repairs explicitly say “source batch”.

| ID | Disposition | Evidence / remaining action |
| --- | --- | --- |
| B1 | Resolved before this batch | `patterns/feature-flag-governance.md` §§3.2–3.3 permits recorded reversal and distinguishes rollback after removal; ADR 0045 supersedes the old pattern. |
| B2 | Resolved at source before this batch | `tooling/observability.md` defines the four referenced burn-rate series and retains `job` labels. Runtime alert behaviour is not proved by source inspection. |
| M1 | Open — owner consolidation | AI/ML §4 and AI adoption §2 both enumerate oversight duties; preserve their activation differences when selecting one owner. |
| M2 | Open — owner consolidation | AI/ML §2.1 and AI adoption §1.1 duplicate materiality; preserve the capability-table clarification and impact-tolerance inheritance. |
| M3 | Resolved in this batch | Financial inventory field already existed; separated its concatenated readiness prompt in `checklists/ai-adoption-readiness.md`. |
| M4 | Resolved in this batch | Adaptive evaluation prompt already existed; separated the synthetic-media prompt from the preceding transparency item. |
| M5 | Open — V41 | Cost §2 has untyped tag keys and spend thresholds; decide strength, applicability and estate-set examples rather than capitalising blindly. |
| M6 | Resolved in this batch | Separated the existing memory-lifecycle prompt in `checklists/ai-native-sdlc-readiness.md`. |
| M7 | Resolved before this batch | Verifier kinds match the schema: eleven named kinds plus `custom`; direct-example checking is separate recurrence protection. |
| M8 | Resolved before this batch | Run-contract top-level prose is count-free and agrees with the schema. |
| M9 | Resolved before this batch | Priming verifier example parses and validates against the verifier-pack schema; recurrence gate is V47. |
| M10 | Open — owner consolidation | RAG §3 restates agentic-loop §9 dual-path controls. Keep RAG activation and route enforcement to its owner. |
| M11 | Partial — V41 | Agentic-loop §6 is typed; §§1.2/9.2 still contain untyped safety claims. Do not equate an action rationale with private chain-of-thought disclosure. |
| M12 | Resolved in this batch | Added flag-governance links in collaboration, trunk workflow, code review, collaboration readiness and the Semantic Index; replacement already owns the rules. |
| M13 | Resolved before this batch | Active flag replacement types requirements and makes numeric defaults estate-tunable. Frozen predecessor is not edited. |
| M14 | Resolved before this batch | Replacement uses neutral metadata and an EXAMPLE shape, with migration mapping in §10. |
| M15 | Resolved before this batch | Principle references point to existing umbrella propositions; V48 adds recurrence detection. |
| M16 | Open — source/scope decision | [Pinned SLSA review](research-v060-source-maintenance-2026-09.md#m16-slsa-attribution--decision-remains-open) separates provenance level, cache isolation, hermeticity and reproducibility. Dependencies §4 remains unchanged pending the scope/strength decision; an L2 minimum does not itself contradict an additional stronger library requirement. |
| M17 | Open — owner consolidation | Dependencies §2 and secure-development §3 differ on vulnerability triage; preserve first-party scope before routing to one owner. |
| M18 | Open — V41 | Dependencies §§3–5 need explicit SBOM, provenance and signing strength/scope, evidence and exception paths. |
| M19 | Open — V41 | Configuration/secrets and audit logging contain untyped prohibition cores; preserve mechanisms as contextual choices. |
| M20 | Resolved before this batch | PromQL moved from the principle to observability tooling. |
| M21 | Resolved before this batch | Burn-rate guidance has production/SLO activation, low-traffic variance and EXAMPLE defaults. |
| M22 | Open — owner consolidation | Reliability §5 and chaos §1 both carry safety bars; retain game-day intent and choose one detailed safety owner. |

## Every Minor Row

| ID | Disposition | Evidence / remaining action |
| --- | --- | --- |
| m01 | Resolved in source batch | AI/ML §7 retains the registry trust boundary; the still-preview status is dated in the source note rather than embedded in the rule. |
| m02 | Resolved in source batch | Zero trust §2.1 links the existing exception-review and permanent-deviation route; authority is unchanged. |
| m03 | Resolved in source batch | Removed the unbounded 2026 growth ranking and budget comparison; retained the usage-cost mechanism and existing controls. |
| m04 | Open — editorial | Fairness/drift anti-pattern appears in AI/ML §8 and AI adoption §6; warning summaries are not two typed control owners. |
| m05 | Open — V41 | RAG §4's “non-negotiable” heading cannot substitute for claim-level strength and activation. |
| m06 | Resolved in this batch | Run-contract §3 links the schema and identifies the exact `context.memory.mode` definition beside the context table. |
| m07 | Closed — allegation not sustained | Schema defines `RemoteSigned` as a provenance level, not a product. No enum rename is needed. |
| m08 | Resolved before this batch | Verifier registration rules refer to configured hosts, not a compulsory product list. |
| m09 | Resolved in this batch | Run-contract §7 and verifier §§7/9 distinguish constructed fixtures, printed-example validation and library skill checks from estate runtime/catalogue enforcement. |
| m10 | Closed — allegation not sustained | Semver §6.2's illustrative migration period is compatible with §9's blast-radius-based notice; §9 is not claimed as the source of the numbers. |
| m11 | Resolved in this batch | Renamed “merge queues of doom” to long-lived integration backlogs without changing merge-queue guidance. |
| m12 | Closed — allegation not sustained | Trunk workflow explicitly names collaboration §3 as the owner of PR-size defaults; no divergent numeric rule found. |
| m13 | Resolved in source batch | Split the merge-path definition/scope/attack narrative; activation, review duties and precedent boundaries are retained. |
| m14 | Resolved in source batch | CISA's 2025 draft is distinguished from its published 2026 successor; no adopted baseline is migrated. |
| m15 | Resolved before this batch | Flag-governance §4.4 permits predeclared/tested safe-default reversion inside `active`, distinct from human state transitions. |
| m16 | Open — layering | Move slopsquatting empirical incident detail out of the principle while retaining the threat distinction and evidence route. |
| m17 | Closed — allegation not sustained | Retaining a rescannable SBOM and declaring re-evaluation triggers are complementary properties, not duplicate rules. |
| m18 | Resolved in source batch | Removed blanket named-registry support claims; retained digest-associated SBOM attachment and promotion duties. |
| m19 | Resolved in this batch | Corrected “an caller” in the STRIDE table. |
| m20 | Resolved in this batch | Corrected the estate key-rotation possessive. |
| m21 | Resolved in source batch | GenAI illustration is pinned and dated; documented conventions are separated from untested implementation/default/adoption claims. |
| m22 | Resolved in this batch | Expanded the regulatory DORA name in reliability §7 to distinguish it from delivery research in §6. |
| m23 | Resolved in source batch | Article exists, but its PostgreSQL lock claim conflicts with primary docs; replaced its DDL support with pinned engine documentation, which also clarifies version boundaries, not a new database baseline. |
| m24 | Resolved in this batch | Corrected Google SRE Book label to match the linked publisher table of contents, retrieved 2026-09-19. |
| m25 | Retain — already illustrative | Governance-program §3 explicitly labels the revision-specific control example as candidates, not automatic obligations; relocation is unnecessary for this release. |
| m26 | Resolved in this batch | Converted real platform-engineering targets from inert code spans into relative links. |
| m27 | Resolved in source batch | Replaced the unsupported NPS leading-indicator assertion with bounded survey feedback, supported by the pinned CNCF paper. |
| m28 | Resolved before this batch | Umbrella compatibility note describes the actual v0.5.0 release, not the former v0.3.0 replacement. |
| m29 | Open — navigation ownership | Umbrella and TL;DR adoption lists are compatible but duplicate detail; keep a single detailed adoption owner. |
| m30 | Open — authority decision | Honesty test protocol calls itself canonical but lacks a declared layer/route; decide its authority before treating a link as sufficient repair. |

## Release Gates Still Open

### V40 Model Walkthrough, Not Human Evidence

A model reader inspected the seven-gate pattern at the baseline and followed
only necessary owner routes. Four scenarios were used:

| Scenario | Model interpretation | Navigation defect found |
| --- | --- | --- |
| Fully inspected AI-assisted dependency patch; no tools or sensitive data | Ordinary delivery controls; no activated run contract; normally technical closure | G3's conditional activation was easier to find in run-contracts than in the gate table |
| Critical vulnerability patch using agent tools | G3 activated; scoped emergency authority, candidate-bound security evidence and containment | Multiple owner roles were distributed across sections |
| Strategic conversion experiment | Ordinary candidate gates plus the outcome overlay and later outcome review | Technical delivery closure must not imply the strategic observation is complete |
| High-impact agent-operated tenant-isolation change | Bounded run, adversarial isolation evidence, accountable human approval and runtime observation | Observation owner/window must remain explicit; no universal duration can be inferred |

The accompanying editorial change points readers first to the gates, explains
conditional G3 activation beside them, gathers existing owner roles into one
sentence and makes open G7 follow-up explicit. No obligation or record family
was removed; ADR 0030 continues to govern the model. A before/after human
comprehension or timing improvement has **not** been demonstrated.

### Remaining Acceptance Work

- V40: model walkthroughs may identify defects. **Human cold-reader verification
  remains open**, at the operator's explicit direction. No timing improvement is claimed.
- V41: claim-level strength/scope and supporting-source admission, not a keyword sweep.
- V42/V43: immutable release identity and proportionate semantic challenge decisions.
  [Source-backed options and model scenarios](research-v060-release-and-review-options-2026-09.md)
  are prepared; no new policy or host setting has been adopted.
- Canonical-owner consolidations and machine-verdict precedence. The model-judge
  pattern currently permits sole calibrated authority where ADR 0034 forbids it.
- V45 proposal dispositions; V44 full-delta lifecycle, source and release closeout.

### Integrity Batch Verification

V46–V48 are implemented in the accompanying change, described in
[ADR 0049](../../docs/adr/0049-add-doctrine-integrity-gates-and-obligation-routing.md).
Source-local verification passed: 32 regression tests, contract fixtures, five
skill packs, generated navigation, the link/example gates and doctrine preflight.
The printed corpus contains 12 YAML examples: four complete local-schema
instances, six partial excerpts and two externally owned formats. Hosted CI on
the exact pushed revision is a separate merge gate recorded in the carrying PR;
it cannot be inferred from these local results.

No `v0.6.0` tag is justified by this reconciliation alone. Retained archive
material, unexpired evidence exceptions and deprecated content follow their
existing lifecycle; “cleanup” is not permission to delete their history.
