# ADR 0062: Close The Carried Release Criteria By Decision

- **Status:** Proposed
- **Decision date:** pending operator acceptance
- **Recorded date:** 2026-11-20
- **Retrospective:** No
- **Deciders:** Repository operator
- **Review provenance:** Decided item by item on 2026-11-20 by a model council at the operator's instruction, and by the operator himself where a decision says so; drafted and reviewed by models of one family; no independent human or domain review recorded
- **Research:** [Decision council, November 2026](../../doctrine/evolution/research-v080-decision-council-2026-11.md)
- **Canonical owner:** [Dependencies And Supply Chain](../../doctrine/principles/dependencies-supply-chain.md) §2; [Cost And FinOps](../../doctrine/principles/cost-and-finops.md) §4; [Doctrine Versioning](../../doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md), new §2.1
- **Derived landings:** [AI And ML Systems](../../doctrine/principles/ai-ml-systems.md) §4; [AI Adoption Controls](../../doctrine/patterns/ai-adoption-controls.md) §1.1; [RAG Retrieval Baseline](../../doctrine/patterns/rag-retrieval-baseline.md) §3; [Agentic Loop Design](../../doctrine/patterns/agentic-loop-design.md) §11; [GOVERNANCE.md](../../GOVERNANCE.md); [CONTRIBUTING.md](../../CONTRIBUTING.md); [change harness](../../doctrine/maintainers/doctrine-library-change-harness.md) §10; [plan note](../../doctrine/evolution/post-v0.3.0-external-review-decisions-and-v0.4.0-plan-2026-07.md); [CHANGELOG.md](../../CHANGELOG.md); doctrine README; semantic index; review register; ADR index
- **Relationship to earlier decisions:** amends [ADR 0034](0034-add-agent-definition-governance-memory-lifecycle-and-judge-discipline.md) decision 3 and [ADR 0059](0059-apply-three-constitution-rules-to-settled-inconsistencies.md) by dated notes; bears on [ADR 0027](0027-keep-public-doctrine-implementation-neutral.md) decision 6 and [ADR 0047](0047-separate-maintainer-doctrine-and-collapse-the-ai-native-sdlc.md) D7

## Context

In July and August 2026 a [plan note](../../doctrine/evolution/post-v0.3.0-external-review-decisions-and-v0.4.0-plan-2026-07.md) set ten acceptance criteria for a release. Six are met. Four were not met when `v0.5.0`, `v0.6.0`, and `v0.7.0` were cut, and each time the note carried them forward word for word ("retarget verbatim").

The four asked for:

- **Criterion 3, marking rule strength.** Mark every material rule in older files with a typed keyword (a capitalised MUST or SHOULD), keeping a backlog until none is unmarked.
- **Criterion 4, one owner per topic.** Where two pages state one rule, one owns it and the other points to it.
- **Criterion 5, automated judges.** Say which text governs when a judge is the final say on a high-stakes acceptance. A judge is an AI model that grades other AI output; its pass or fail gates a merge or release.
- **Criterion 9, three promises about the library.** A timed test with a human reader new to the library; a rule that a published version tag is never moved or reused; a promise that someone other than the author challenges rule changes before release.

This record gives every remaining part a disposition: done by an edit, left as written, dropped, or deferred with an owner, a dated trigger, and a retirement condition. Nothing moves to "the next release".

A model council voted on each item on 2026-11-20. Where the operator answered himself, his answer governs. A sweep is the periodic review the [content lifecycle pattern](../../doctrine/maintainers/doctrine-content-lifecycle.md) §8 requires; one is due by 2027-05-20.

## Decision

### What the operator is accepting

1. The open-ended promise to mark older rules MUST or SHOULD is withdrawn; a closed, dated list replaces it (D1).
2. Four sentences about secrets wait for the operator's typed-keyword review (D1).
3. Four agent-safety sentences wait for the ADR on agent authority (D1).
4. Three spend-alert figures become defaults; the tagging sentence and one heading stay (D1).
5. Typing two whole files goes with the lifecycle rewrite (D1).
6. The known-exploited rule covers first-party code too (D2a).
7. AI Adoption Controls §2 owns the human-oversight detail (D2b).
8. AI And ML Systems §2.1 owns the definition of materiality (D2c).
9. The dual-path bullet in RAG Retrieval Baseline becomes a pointer (D2d).
10. An independently calibrated judge may be the final say; ADR 0034 is amended to match (D3).
11. The timed reader test is dropped; a statement of real use stands in its place (D4a).
12. A published version tag is never moved or reused (D4b).
13. The promise of outside challenge before a release is dropped (D4c).
14. The July plan note becomes Historical; future release criteria go in the changelog (D5).

### For the operator to confirm

None of these is the operator's own words.

- Keeping the judge exception does not lift the rules that still require a person: human approval for high-impact change classes (AI And ML Systems §4), and the lifecycle pattern's rule that a model's output "is not merge or deployment authority" (D3).
- Under the fixed-tag rule, history is not rewritten again as ADR 0027 decision 6 once allowed; an unwanted version is withdrawn instead (D4b).
- The allocation-coverage figures in Cost And FinOps §2 stay as written; the council was not asked (D1).
- The timed reader test is dropped and real use stands in its place (D4a).
- Review outcomes are appended here as dated notes; an open row gets a reason and a new date (D1).
- In Agentic Loop Design §11, row ASI09, "automation-bias awareness" moves to the citation of AI Adoption Controls §2 (D2b).
- The wording of the Historical banner and the plan note's final update (D5).

### D1. Marking rule strength: one dated list replaces the open-ended promise

**Question.** Should the library keep promising a typed keyword on every material rule in older files?

**Now.** Criterion 3 wants no material "obligations left in the untyped register".

**Decision.** The promise is withdrawn. The table and the paragraph after it are the whole, closed list: a rule gains a typed keyword only through an ADR that names it. The repository operator owns every row.

| Sentence | File and section | Trigger | Retirement condition |
| --- | --- | --- | --- |
| "never treat as normal config" | [Configuration And Secrets](../../doctrine/principles/configuration-and-secrets.md) §1 | Operator's review of typed keywords: from 2026-12-18, verdict by 2027-01-15 | A recorded verdict: typed by an ADR, or left as written |
| "Defaults must be safe" | Same, §3 | Same | Same |
| "real secrets never committed" | Same, §4 | Same | Same |
| "**Do not** embed **secret values**" | [Audit Logging](../../doctrine/principles/audit-logging.md) §3 | Same | Same |
| "tool call must be preceded by explicit reasoning" | Agentic Loop Design §1.2 | ADR on agent authority accepted; reviewed 2027-01-15, then by 2027-05-20 | That ADR's verdict, or a recorded decision to leave it |
| "mandatory for Tier D" | Same, §1.2 | Same | Same |
| "must never be forwarded verbatim" | Same, §9.2 | Same | Same |
| "Enforcement must happen in deterministic code" | Same, §9.2 | Same | Same |

Whether the [AI-native lifecycle pattern](../../doctrine/patterns/ai-native-software-development-lifecycle.md) and [Outcome And Portfolio Linkage](../../doctrine/patterns/outcome-and-portfolio-linkage.md) take typed keywords goes to the ADR that rewrites the lifecycle pattern (ADR 0047 D7), reviewed at the sweep due by 2027-05-20. It retires on that ADR's answer or a recorded verdict.

The tagging sentence (Cost And FinOps §2) and the heading "Evaluation (Non-Negotiable For Production RAG)" stay as written.

**Proposed edit.** In Cost And FinOps §4, add at the end of the bullet "Define alert thresholds per service":

```text
The three figures are defaults; the adopting organisation sets its own.
```

**Who decided.** Operator, 2026-11-20, for the list. Council, awaiting his acceptance: secrets 3 to 2; agent safety 4 to 1; cost label 4 to 1; heading 3 to 2; two files 5 to 0.

**Change class.** No class in versioning §3 fits; release notes have used "clarification" for the cost label.

**Consumer impact.** None required.

### D2. One owner per topic: four consolidations, as an amendment to ADR 0059

**Question.** Four topics are still stated on two pages. Which page owns each?

**Decision.** Each topic has one owner, and the other page points to it. To repeat a check, read the two sections at `v0.7.0` beside the proposed text.

**D2a. Known-exploited vulnerabilities.** Dependencies And Supply Chain §2, the owner, says "when a component matches"; its pointer in [Secure Development Lifecycle](../../doctrine/principles/secure-development-lifecycle.md) §3 says "A known-exploited finding". In the owner's bullet, replace that phrase with line one below, and "non-KEV backlog" to the end with line two. No duty is lost: components stay covered.

```text
when a vulnerability is known to be exploited, in your own code or in a component that matches
the rest of the backlog, not to **ignore** a known-exploited finding.
```

**D2b. Human oversight at run time.** AI And ML Systems §4 repeats four duties that AI Adoption Controls §2 owns ("Human oversight is a runtime property"). In the principle's bullet, replace everything after "the gates above protect the repo;" with the text below. No duty is lost: all four stay in the pattern.

```text
a system that makes such decisions at runtime also needs a fallback to human handling, an overseer who can disregard, override, or halt its output, a contest path for affected people, and per-decision logging that can explain a decision. [../patterns/ai-adoption-controls.md](../patterns/ai-adoption-controls.md) §2 owns the detail.
```

**D2c. Materiality.** AI Adoption Controls §1.1 repeats AI And ML Systems §2.1 ("materiality says what its failure costs"). In §1.1, replace the first four sentences with the text below; the last, on impact tolerances, stays. No duty is lost: §2.1 states each point removed.

```text
[../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) §2.1 owns the definition: materiality is what a system's failure **costs**, tiered by **business impact**, and the controls in §§2–5 scale with the **max** of capability tier and materiality. Judge blast radius as in [../principles/threat-modeling-stride-lite.md](../principles/threat-modeling-stride-lite.md) §4.
```

**D2d. Dual-path injection defence.** RAG Retrieval Baseline §3 restates what Agentic Loop Design §9 owns ("enforces capability policies in deterministic code"). In that bullet, replace "Apply an architectural defence:" and all that follows, up to and including "§9;", with the text below. No duty is lost: the trigger and the pointer stay.

```text
Apply the architectural defence that [agentic-loop-design.md](agentic-loop-design.md) §9 owns;
```

Append to ADR 0059 on acceptance, with the acceptance date:

```text
## Amendment (YYYY-MM-DD): Four Further Consolidations

[ADR 0062](0062-close-the-carried-release-criteria-by-decision.md) D2 applies this ADR's D1 and D2 to four places they had not reached. Nothing decided above is reversed.

| Topic | Before | After |
| --- | --- | --- |
| Known-exploited vulnerabilities (D1) | The owner sentence in dependencies §2 spoke of a component that matches a known-exploited catalogue | It covers any vulnerability known to be exploited, in a component or in first-party code, as the pointer in secure development §3 has said since this ADR |
| Human oversight at run time (D2) | AI and ML systems §4 and AI adoption controls §2 both set out the four duties in full | AI adoption controls §2 owns the detail. AI and ML systems §4 names the four duties and points to it |
| Materiality (D2) | Defined in AI and ML systems §2.1 and again in AI adoption controls §1.1 | AI and ML systems §2.1 owns the definition. AI adoption controls §1.1 points to it and keeps its sentence on impact tolerances |
| Dual-path injection defence (D2) | RAG retrieval baseline §3 restated the mechanism before pointing to the agentic loop pattern §9 | The agentic loop pattern §9 owns the mechanism. RAG retrieval baseline §3 keeps the trigger and the pointer |

ADR 0062 states the check for each move. Change class: normative tightening for the first row, because the owner's wording now covers first-party findings; clarification for the other three.
```

**Who decided.** Council, awaiting the operator's acceptance: 5 to 0 on D2a, D2c, and D2d; 4 to 1 on D2b and on using an amendment.

**Change class.** D2a is normative tightening (scope). For the rest no class in §3 fits; ADR 0059 used "clarification".

**Consumer impact.** Check that vulnerability triage treats a flaw in your own code as highest urgency once it is known to be exploited.

### D3. A calibrated judge may be the final say; ADR 0034 is amended to match

**Question.** Can a judge be the only authority on a high-stakes acceptance?

**Now.** ADR 0034 decision 3 says a judge is "never sole authority for high-materiality acceptance". Agentic Loop Design §8.2 says: "A judge MUST NOT be the sole authority for a high-materiality acceptance decision unless its agreement and failure modes have been independently calibrated for that use." Both landed in one commit (`b30700b`, 2026-08-03), so they have disagreed from the start.

**Decision.** The exception stays and the pattern's sentence is unchanged: an adopting organisation may let an independently calibrated judge be the final say. ADR 0034 decision 3 is amended to match. No precedence clause is written; the two texts now agree. [AI-05]

**Proposed edit.** No rule file changes. Append to ADR 0034 on acceptance, with the acceptance date:

```text
## Amendment (YYYY-MM-DD): Sole-Authority Limit

Decision 3 says a judge is "never sole authority for high-materiality acceptance". The pattern this ADR landed says something else. Since the same commit, the "Sole-authority limit" bullet in [agentic-loop-design.md](../../doctrine/patterns/agentic-loop-design.md) §8.2 has allowed one exception: a judge whose "agreement and failure modes have been independently calibrated for that use".

The operator decided on 2026-11-20 that the exception stays ([ADR 0062](0062-close-the-carried-release-criteria-by-decision.md) D3). From this date decision 3 is read with it. A judge is not the sole authority for a high-materiality acceptance decision unless it has been independently calibrated for that use. An adopting organisation may rely on a judge that has. The pattern's bullet is the rule and does not change. The rest of decision 3 stands. The original sentence is kept above as history.
```

**Who decided.** Operator, 2026-11-20, overruling the council's 5 to 0 vote to delete the exception. He values automated judges and wants adopting organisations left free to rely on one.

**Change class.** No class in §3 fits. The rule file is unchanged and the decision record is loosened; release notes have used "clarification" and "normative loosening".

**Consumer impact.** None.

### D4. Three promises about the library itself

**D4a. The timed reader test is dropped.** The plan promised a timed test with readers new to the library ("Time and error a cold-reader walkthrough"). It was never run and is dropped. In its place: the library is in use in at least three enterprises (operator's statement, 2026-11-20). Real use is not the same thing as the timed test: it does not time a new reader or count their mistakes. Who decided: chair's reading of the operator's answer; to be confirmed. The council voted 3 to 2 to withdraw. Change class: none in §3 fits. Consumer impact: none.

**D4b. A published version tag is never moved or reused.** ADR 0059 tells adopters "A tag that can be moved is not one", yet nothing promises that this library's own tags stay put. Adopted: a published tag is never moved or reused; a correction takes a new version; a withdrawal is recorded without reusing the version; a hosting feature to enforce this stays optional. One typed keyword is added, in a new §2.1 of the versioning pattern, after the "Why" of §2:

```text
### 2.1 A Published Version Tag Is Fixed

Once a version tag of this library is published, maintainers MUST NOT move it to another commit or reuse its version for different content.

- **A correction takes a new version.** The corrected text ships under a new tag, and its release note names the versions it corrects.
- **A withdrawal keeps the version reserved.** If a release has to be withdrawn, the withdrawal is recorded with the version, the reason, and what a consumer should do. Nothing else is ever published under that version. Withdrawal fixes the identity, not the availability: unsafe content, such as an exposed credential, can be removed or restricted without assigning other content to the version.
- **Host enforcement is optional.** A hosting feature that locks published tags or releases is one way to enforce this. The rule does not depend on one.

**Why:** §5 tells consumers to pin a tag. A tag that moves changes the rules under a pinned consumer with no signal. The typed sentence applies [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) clause 3 to this library's tags (S1, pinned by version, accessed 2026-11-20): the contents of a released version are not modified, and any change is released as a new version. The risk is one-sided. The rule costs a maintainer one new version for each correction; without it, a pin stops meaning what the consumer checked. The rule binds maintainers. Consumers gain a promise and no duty ([ADR 0062](../../docs/adr/0062-close-the-carried-release-criteria-by-decision.md)).
```

`GOVERNANCE.md` (release section) and `CONTRIBUTING.md` (pull request expectations) gain the bullet below; the change harness §10 gains the checklist line.

```text
- **A published version tag is fixed.** It is never moved or reused ([versioning](doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md) §2.1).
[ ] Release: every published tag still points to its release commit (versioning §2.1)
```

Outside fact, read on the publisher's page on 2026-11-20 (Semantic Versioning 2.0.0, clause 3): "Once a versioned package has been released, the contents of that version MUST NOT be modified. Any modifications MUST be released as a new version." <https://semver.org/spec/v2.0.0.html>

Who decided: Council, 4 to 1; awaits the operator's acceptance. Change class: normative tightening, binding maintainers only. Consumer impact: none.

**D4c. The promise of outside challenge is dropped.** The plan promised that someone other than the author would challenge rule changes before a release ("a public review window, qualified external review, or a bounded waiver"). It is dropped. The operator's reason: organisations that adopt the library review changes themselves when they adopt them, and he has seen this first hand. Each ADR's "Review provenance" line stays as the library's own honest statement. Who decided: Operator, 2026-11-20; the council voted 4 to 1 likewise. Change class: none in §3 fits. Consumer impact: none.

### D5. Release criteria live in the changelog, and the July plan note becomes Historical

**Question.** The criteria sit in a note whose status line reads "Accepted tasking; non-normative". Where do release criteria live from now on?

**Decision.** The plan note is marked Historical. Future release criteria are stated in `CHANGELOG.md` under `## [Unreleased]` and graded in that release's entry. With none stated, the existing sentence in `GOVERNANCE.md` decides.

**Ordering constraint.** Historical means superseded, and until this record is accepted the plan note alone holds the open items. So: accept this record with the D1 list, add the final update, then the banner. Without D1, no banner.

**Proposed edit.** In the plan note, a final status update:

```text
**Plan status update (YYYY-MM-DD), final:** closed by [ADR 0062](../../docs/adr/0062-close-the-carried-release-criteria-by-decision.md). No criterion is retargeted; that record gives each remaining part its disposition.
```

Then the banner, first under the title:

```text
> **Historical** (YYYY-MM-DD): superseded by [ADR 0062](../../docs/adr/0062-close-the-carried-release-criteria-by-decision.md), which disposes of every remaining criterion and holds the dated list of what is still open. Kept as provenance.
```

**Who decided.** Council, 2 to 1 on a panel of three; awaits the operator's acceptance.

**Change class.** Editorial for the banner (lifecycle pattern §1). For the changelog practice none in §3 fits; release notes have used "maintainer tooling".

**Consumer impact.** None.

## Control Cost And Lifecycle

- **D1** ends an undated promise. Cost: one line per open row in each sweep record. It retires when its rows close.
- **D2, D3, D4a, and D4c** remove duplicated, contradictory, or unkept text. Cost: none for adopters.
- **D4b** stops a pin changing meaning unannounced. Cost: one check per release and a new version per correction.
- **D5** puts criteria where consumers look. Cost: one short list per release that sets any.

## Alternatives Considered

- **Carry the four criteria forward again.** Rejected: it is the practice this record ends.
- **Meet them as written.** Not taken: it needs a recruited reader.
- **Type the eight sentences now, or keep no list.** Not taken: the operator chose the dated list.
- **Delete the judge exception.** The council's 5 to 0 vote, overruled by the operator.

## Consumer Impact And Migration

Change classes: normative tightening for D2a (scope) and D4b (maintainers only); editorial for the D5 banner; none in versioning §3 fits the rest. Compatibility: pre-1.0 minor. Migration: the triage check in D2.

## Acceptance Criteria

- The phrase "retarget verbatim" is not needed again: no later plan update, release note, or sweep record carries these items forward unchanged.
- The plan note carries its final update and, added after acceptance, the Historical banner.
- Each D1 row has a dated outcome note here by its date, or a reason and a new date.
- Each D2 topic is stated in full on one page only.
- ADR 0034 and ADR 0059 carry their notes as worded here; the "Sole-authority limit" bullet is unchanged.
- The edits add one typed keyword in total, in versioning §2.1.
- Every tag points where it did on 2026-11-20: `v0.1.0` `18532b3`, `v0.2.0` `9d4883f`, `v0.3.0` `6478400`, `v0.3.1` `1afd31d`, `v0.4.0` `c2ae3c1`, `v0.5.0` `1c5c59a`, `v0.6.0` `e386eaa`, `v0.6.1` `31cdea8`, `v0.6.2` `8bd0c70`, `v0.7.0` `e0efe31`.

## Residual Risk

- D4a rests on the chair's reading. The statement of use was not verified by the council and does not stand in for the timed test.
- D3 leaves "independently calibrated" undefined; each organisation relying on the exception decides who counts as independent.
- The eight sentences stay untyped until their reviews, and four wait on an ADR with no acceptance date.
- D2b leaves the human-oversight duties in full only in a pattern, which `GOVERNANCE.md` reviews more lightly than a principle.
- D4b was not tested against a real withdrawal. Earlier tag movements, hosted tags, and host settings were not checked.
