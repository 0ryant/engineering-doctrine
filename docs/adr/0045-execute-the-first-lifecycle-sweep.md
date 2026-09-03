# ADR 0045: Execute The First Lifecycle Sweep

- **Status:** Accepted
- **Decision date:** 2026-09-03
- **Recorded date:** 2026-09-03
- **Retrospective:** No
- **Executes:** [ADR 0038](0038-adopt-a-doctrine-content-lifecycle.md) decision 5 (first sweep scope) and decision 4 (90-day rule for Proposed ADRs)
- **Sweep record:** [evolution/sweep-2026-09.md](../../doctrine/evolution/sweep-2026-09.md)

## Context

[ADR 0038](0038-adopt-a-doctrine-content-lifecycle.md) built the retirement machinery for this library and scoped its first sweep to three pieces of real work: decide [ADR 0021](0021-audit-as-discipline-applies-to-runner-itself.md), Proposed since 2026-05-20 and past the 90-day rule; make a fill-or-retire decision on the AWS and GCP estate stubs; and execute the feature-flag supersession that the forward plan had queued. It tied that sweep to "the next minor release". No minor release has been cut since, so the machinery has never turned over: no file has ever been deleted, [DEPRECATED.md](../../doctrine/DEPRECATED.md) is empty in every table, and the corpus's own assessment on 2026-09-03 named this as the single strongest signal that the meta-governance layer is description rather than practice.

The lifecycle pattern's own §8 provides for this case. A standalone sweep is a maintenance obligation independent of the release calendar; it records verdicts, and only the verdicts that require a tag (a deprecation banner's "since", a removal) wait for the next tagged release.

## Decision

1. **This is the first sweep, run standalone.** Its record is [evolution/sweep-2026-09.md](../../doctrine/evolution/sweep-2026-09.md) and its ledger row is the first entry in [DEPRECATED.md](../../doctrine/DEPRECATED.md). Its cohort is exactly the ADR 0038 scope; the 12-month staleness cohort and the default-fade arm are not yet armed (epoch `v0.5.0`, which has not been tagged) and are recorded as such.

2. **ADR 0021 is Accepted and landed.** Its six-point decision is coherent with the run-contract pattern and adds one thing that pattern lacked: the executor must prove its own substrate before it measures anything. It lands as the "Executor preflight" clause in [run-contracts.md §8](../../doctrine/patterns/run-contracts.md). Change class: normative tightening for run-contract executors; consumers that already verify runner preconditions have no migration.

3. **The AWS and GCP estate stubs are retired, not filled.** [aws-container-runtimes.md](../../doctrine/tooling/estates/aws-container-runtimes.md) and [gcp-container-runtimes.md](../../doctrine/tooling/estates/gcp-container-runtimes.md) have been placeholders for five months with no owner; each says on its face not to treat it as guidance. A stub with no owner is the ownerless deferral the lifecycle pattern calls a defect. Their replacement is [TEMPLATE.md](../../doctrine/tooling/estates/TEMPLATE.md), which is what an adopter would have copied anyway. They enter the dying table now; their Deprecated banner takes effect at the next tagged release and their earliest removal is the release after that. The Azure supplement is not a stub and is retained.

4. **feature-flag-lifecycle.md is superseded.** The retyped replacement, [feature-flag-governance.md](../../doctrine/patterns/feature-flag-governance.md), lands Active with a complete state machine, typed claims, no vendor or tracker names, and no plan-lane references. The old file enters the dying table with the replacement named; its banner reads Deprecated at the next tagged release and moves to Superseded per lifecycle §§4–6 when the tombstone is written. Inbound links are repointed now. Change class: normative replacement; migration note in the new file's Consumer Impact section.

5. **Reference-status leg, bounded to the cohort.** Link health was checked for every external citation in the three cohort files and in ADR 0021's related files; results are in the sweep record. The exhaustive re-check of every MUST-supporting citation in the corpus is not part of this cohort and is scheduled for the release-coupled sweep at the next minor.

6. **The next tagged release executes what this sweep could not.** Cutting the pending release stamps the three banners and starts the removal clocks. Until then the dying-table rows say so explicitly.

## Alternatives Considered

### Wait for the next minor release, as ADR 0038 assumed

Rejected. The release has not happened in the four weeks since ADR 0038 and nothing in GOVERNANCE.md promises one. Waiting keeps the machinery unexercised for an unbounded period, which is the defect being fixed.

### Withdraw ADR 0021 as stale

Rejected. Staleness is a property of the process, not the decision. The decision is small, portable, and consistent with the pattern it extends; the fixtures its Verification section describes do not exist in this library, and that is stated in the sweep record rather than pretended away.

### Fill the estate stubs

Rejected. Filling them means asserting vendor product choices that no adopting organisation has made. That is estate content by definition and cannot be authored from the library.

### Amend feature-flag-lifecycle.md in place

Rejected. ADR 0038 explicitly chose supersession for this file as the test case for the mechanism, and the rewrite changes the state machine, which is a normative replacement rather than a refinement.

## Consequences

- [DEPRECATED.md](../../doctrine/DEPRECATED.md) is no longer empty. Three dying-table rows and one ledger row exist; the "empty register is a meaningful statement" sentence is now false and is replaced.
- The next release checklist has three banner stamps and a clock start to execute, and the release notes must carry the deprecation change class.
- The library has one worked example of each lifecycle move it defined except restoration.

## Consumer Impact

**Change class:** deprecation (three files), normative replacement (feature-flag pattern), normative tightening (run-contract executors). Consumers linking `patterns/feature-flag-lifecycle.md` repoint to `patterns/feature-flag-governance.md`; consumers who copied an estate stub lose nothing, since the stubs carried no guidance.

## Acceptance Evidence

- ADR 0021's status line reads Accepted with the landing location; the index row agrees.
- `run-contracts.md` §8 carries the executor preflight clause; `scripts/validate-contracts-v1.py` remains green.
- `feature-flag-governance.md` exists, is linked from the README, sitemap, semantic index, and the old file's notice; no inbound link to the old path remains in normative files.
- `DEPRECATED.md` dying table has three rows and the sweep ledger has one, each linking this ADR and the sweep record.
- The sweep record lists every cohort citation with its link-health result.

## Review Note

Drafted and executed in a single agent session under the owner's direction, in response to the 2026-09-03 assessment. No council was convened; no independent human review has been recorded. The verdicts on the estate stubs and ADR 0021 are the owner's to reverse at the next sweep if they disagree.
