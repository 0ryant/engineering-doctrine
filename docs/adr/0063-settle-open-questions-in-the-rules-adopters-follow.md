# ADR 0063: Settle Open Questions In The Rules Adopters Follow

- **Status:** Proposed
- **Decision date:** pending operator acceptance
- **Recorded date:** 2026-11-20
- **Retrospective:** No
- **Deciders:** Repository operator
- **Review provenance:** Decided item by item on 2026-11-20 by a model council at the operator's instruction, and by the operator himself where a decision says so; drafted and reviewed by models of one family; no independent human or domain review recorded
- **Research:** [Decision council, November 2026](../../doctrine/evolution/research-v080-decision-council-2026-11.md)
- **Canonical owners:** [zero trust](../../doctrine/principles/zero-trust-and-workload-identity.md) §2.1; [run contracts](../../doctrine/patterns/run-contracts.md) §1.1; [dependencies](../../doctrine/principles/dependencies-supply-chain.md) §§2, 5; [code review](../../doctrine/patterns/code-review-and-change-approval.md) §6; [documentation](../../doctrine/principles/documentation-knowledge.md) §3; [cost and FinOps](../../doctrine/principles/cost-and-finops.md) §7; [feature flag governance](../../doctrine/patterns/feature-flag-governance.md) §§2, 4.4, 6; [AI and ML systems](../../doctrine/principles/ai-ml-systems.md) §8 and [agentic loop design](../../doctrine/patterns/agentic-loop-design.md) §12
- **Derived landings:** [Privileged Automation](../../doctrine/impl/privileged-automation.md), [Dependency Adoption](../../doctrine/impl/dependency-adoption.md), [Infrastructure Delivery](../../doctrine/impl/infrastructure-delivery.md), [Database Migration](../../doctrine/impl/database-migration.md), [Application Deployment](../../doctrine/impl/application-deployment.md) and [Release And Rollback](../../doctrine/impl/release-and-rollback.md); the [AI-native SDLC readiness](../../doctrine/checklists/ai-native-sdlc-readiness.md) checklist and [developer experience scorecard](../../doctrine/checklists/developer-experience-scorecard.md); the [glossary](../../doctrine/glossary.md); amendment notes on [ADR 0043](0043-replace-agent-coauthorship-disclosure-with-a-method-record.md) and [ADR 0052](0052-close-owner-gaps-from-implementation-batch-2.md); the [review register](../../doctrine/evolution/review-full-doctrine-2026-11-findings.json) and [batch 3 owner audit](../../doctrine/evolution/research-impl-backlog-batch-3-composition-2026-11.md)
- **Relationship to earlier decisions:** closes the sign-off gap ADR 0043 left open (D7); narrows ADR 0052 D1 (D3); settles twelve of the 22 review decisions [ADR 0059](0059-apply-three-constitution-rules-to-settled-inconsistencies.md) left open, and five batch 3 owner gaps

## Context

After ADR 0059 the November 2026 review still had 22 choices open. On 2026-11-20 the operator asked a model council to decide every open question. This record carries the nineteen about rules adopters follow.

Three or five seats voted on each, and a chair put some to the operator. His answer governs where he gave one. Every other decision is the council's and awaits his acceptance.

Two questions are not decided here: whether an AI agent may carry out a change in production, and who can stop a standing agent. Both go to an agent-authority ADR, to be drafted by 2027-01-15. ADR 0059 kept the first for the operator, as one that will "need the maintainer's judgement on what an agent may enact".

An owner is the principle or pattern that states a rule. Change classes are the seven in [versioning](../../doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md) §3; where none fits, the quoted label is one release notes have used. Fenced text is exact, and every edit is proposed wording.

## Decision

### What the operator is accepting

1. An agent that runs on its own keeps its own account; only the trigger label "Tier D" goes.
2. The three tests for when agent rules apply stay independent.
3. A bot-only update path does not merge a change to a privileged pipeline definition.
4. Isolated execution of agent-run code does not become a rule.
5. A developer's interactive, tool-using coding assistant needs a run contract, and a minimal one is enough.
6. The signing rule names a capability and keeps the product as its example.
7. A tool is never named in a commit's `Signed-off-by` line.
8. One reference gains a non-normative caution about secrets in saved plan files.
9. The library says nothing further about provenance for an internal production artefact.
10. The pinning rule is not extended to infrastructure modules and providers.
11. The known-exploited vulnerability rule is unchanged, with nothing added about the directive replaced in 2026.
12. The minimum form of an owner is a team.
13. A team leaving a golden path keeps the pattern's reviewed record with an expiry.
14. The reference's sentence on one-off data fixes is labelled non-normative.
15. Cost per result for AI features is due as the system matures, not from the first tier.
16. A kill switch's default stays `on`, and its two states are named "normal" and "tripped".
17. Two unsourced context-fill thresholds, 90% and 95%, are removed.
18. A recovery exercise before first production release is deferred to the operator's review, not before 2026-12-18.
19. No rule for retiring a service is added.

### For the operator to confirm

- Dropping the label "Tier D" has one effect in practice: a tool-using agent that neither writes to production nor runs unattended with large impact may share a team account, where today the label gives it its own (D1).
- The sentence on the three agent tests lands in run contracts §1.1. The vote did not say where (D2).
- "Minimal" means a contract with only the keys §3 marks as required, and the executor duties in §8 are untouched (D5).
- Naming the kill-switch states touches two further lines: the metadata sentence in §6 and invariant 7 of Release And Rollback (D16).
- A sign-off line that a platform adds for an update bot stays outside the rule (D7).
- The recovery-exercise deferral has no latest date (D18).
- "A tool is never named in a sign-off line" is the chair's reading of his answer (D7).

### D1. An agent's own account

**Question.** When does an AI agent need an account (a principal) of its own? The trigger list includes "Tier D", the label for any agent that uses tools, so it catches every agent [AI-01, SEC-15].

**Decision.** The rule stays. An agent that runs on its own keeps a narrow account with a named person responsible; an assistant inside a person's session uses that person's login. Only the label goes.

**Proposed edit.** Zero trust §2.1 and Privileged Automation invariant 5:

```text
Now:      (Tier D, write access to production, or unattended operation at material blast radius)
Proposed: (write access to production, or unattended operation at material blast radius)
```

**Who decided.** Operator, 2026-11-20. The council voted 5 to 0 to drop the label; four seats also meant to add two triggers. **Change class.** None fits; "normative loosening". **Impact.** None required.

### D2. Three tests for agents, stated once

**Question.** Three owners each set a test for when their agent rules apply, and the tests disagree. Only a reference says so: "The owners draw three lines that do not coincide".

**Decision.** No test decides another, and one owner says so.

**Proposed edit.** Added at the end of run contracts §1.1:

```text
This test is one of three that are answered separately, each by its own owner: whether a run is governed (this section), whether an agent is its own principal (zero trust §2.1), and whether an agent's definition is in the pipeline-definition trust class (merge path §1). The answer to one does not settle another.
```

**Who decided.** Council, 5 to 0. The choice of owner is the drafter's. **Change class.** None fits; "clarification". **Impact.** None.

### D3. The bot-only update path

**Question.** ADR 0052 lets low-risk dependency updates merge on a bot-only path; "other updates get **human review**." May that path merge a change to a privileged pipeline definition, one that can read secrets, change production or publish packages?

**Decision.** No.

**Proposed edit.** Added after that sentence in dependencies §2, and echoed in Privileged Automation and Dependency Adoption:

```text
A change to a privileged pipeline definition (merge path §2 invariant 2) is not in the low-risk class: it is one of the change classes that keep accountable human approval (AI and ML systems §4).
```

Appended to ADR 0052 on acceptance:

```text
## Amendment (YYYY-MM-DD): Bot-Only Path

[ADR 0063](0063-settle-open-questions-in-the-rules-adopters-follow.md) D3 narrows D1. A change to a privileged pipeline definition is not in the low-risk class that may merge on the bot-only path. The rest of D1 stands.
```

**Who decided.** Council, 5 to 0. One seat named a keyword (MUST NOT); the vote set none, so none is added. **Change class.** Normative tightening. **Impact.** A person approves bot updates to privileged pipeline definitions.

### D4. Isolated execution and the checklist prompt

**Question.** A checklist asks that agent-produced code runs in an isolated environment, and no owner requires that [AI-14].

**Decision.** It does not become a rule. The prompt takes its owner's wording.

**Proposed edit.** AI-native SDLC readiness checklist:

```text
Now:      Agent-produced executable content runs in an isolated preview/test environment without standing production credentials.
Proposed: Agent-produced candidates are built in a short-lived isolated workspace, with no protected-branch or standing production mutation (AI-native lifecycle §10).
```

**Who decided.** Council, 4 to 1. **Change class.** None fits; "correction". **Impact.** The prompt asks for less; the finding that no owner requires sandboxing stays open [SAI-12].

### D5. A run contract for an interactive assistant

The operator should read this one with care. Two of the three seats said it turns on whether he counts such a session as incidental assistance, which is his to say. Both majority seats asked for a worked minimal example before it is carried out.

**Question.** Does a developer's interactive coding assistant need a run contract, the declared tools, authority, outputs and checks of a model-driven run? The review's only critical finding says requiring one is unworkable [SAI-01].

**What the text says now.** The majority relied on run contracts §1.1, whose first trigger is "it invokes tools or subprocesses;", and AI and ML systems §4: "**Every governed execution has a run contract**". The dissent relied on Core Proposition 10: "Incidental assistance remains lightweight".

**Decision.** Yes, a minimal one.

**Proposed edit.** Added to run contracts §1.1, in the same change as D2:

```text
An interactive session in which a developer's assistant invokes tools is governed by the first trigger. Its contract can be minimal: an instance of the same envelope that carries only the keys §3 marks as required, written once for a kind of work and reused for each session of that kind. Minimal describes the size of the contract. It adds no second schema and removes no executor duty in §8.
```

**Who decided.** Council, 2 to 1, by one vote. **Change class.** None fits; "clarification". **Impact.** No new duty; the executor duties in §8 still apply.

### D6. The signing rule names a capability

**Question.** Principles state outcomes and leave products to tooling pages, yet the signing rule names one tool [UMB-18].

**Decision.** It names a capability, with the product as its example. The strength stays SHOULD.

**Proposed edit.** Dependencies §5, first, second and fourth bullets:

```text
Now:      sign them using **cosign** with keyless signing via OIDC.
Proposed: sign them with keyless signing that binds each signature to the build's workload identity and records it in a transparency log. Example: **cosign** via OIDC, as the rest of this bullet describes.

Now:      against the Rekor ledger
Proposed: against the transparency log (Rekor, in the example)

Now:      use **cosign** with a KMS-backed key
Proposed: sign with a key held in a key-management service, for example **cosign** with a KMS-backed key,
```

**Who decided.** Council, 5 to 0. **Change class.** None fits; [ADR 0058](0058-sharpen-four-rules-after-the-november-2026-review.md) used "normative clarification" for provenance. **Impact.** None for teams using the named tool.

### D7. Sign-off lines

**Question.** Some projects ask each commit for a `Signed-off-by` line, where the submitter certifies the right to submit. ADR 0043 barred tools from authorship fields and left this line "open for a later ADR" [GOV-03].

**Decision.** The ban covers it: a tool is never named there. This is that later ADR.

**Proposed edit.** Code review §6 row 1; the glossary entry takes the same field:

```text
Now:      (`Author`, `Co-Authored-By`, or any successor conferring authorship standing)
Proposed: (`Author`, `Co-Authored-By`, `Signed-off-by`, or any successor conferring authorship standing)
```

Appended to ADR 0043 on acceptance:

```text
## Amendment (YYYY-MM-DD): Sign-Off Lines

[ADR 0063](0063-settle-open-questions-in-the-rules-adopters-follow.md) D7 closes the gap recorded above as "`Signed-off-by` is unresolved". A non-human tool is not named in a `Signed-off-by` line. Code review and change approval §6 row 1 now lists the field, as decision 1 of this ADR already did. A person's own sign-off is unaffected. The rest of this ADR stands. Change class: normative tightening.
```

**Who decided.** Chair's reading of the operator's answer; to be confirmed. The council voted 4 to 1 the same way. **Change class.** Normative tightening: the existing MUST NOT reaches one more field. **Impact.** Tooling stops naming itself in sign-off lines on agent-assisted changes.

### D12. The minimum form of an owner

**Question.** The library accepts a team as owner of a service, and a team or a channel for a repository [UMB-13, XC-29].

**Decision.** The least that counts is a team. A channel is a way to reach it.

**Proposed edit.** Documentation §3, then the developer experience scorecard:

```text
Now:      **Ownership** (team or channel) is obvious for the repo.
Proposed: **Ownership** (a named team, as collaboration §8 states) is obvious for the repo. A channel is a way to reach the owner.

Now:      Ownership clarity: team/channel/on-call or maintainer route is obvious
Proposed: Ownership clarity: the owner team is named, and the channel, on-call or maintainer route for reaching it is obvious
```

**Who decided.** Council, 3 to 0. **Change class.** Normative tightening, a small one. **Impact.** A README that names only a channel names a team.

### D15. Cost per result for AI features

**Question.** Cost and FinOps §3 says to "establish cost-per-token baselines at Tier A" and expand "as the system matures"; §7 requires cost per outcome from the first tier [OPS-11].

**Decision.** It is due as the system matures.

**Proposed edit.** Cost and FinOps §7; Application Deployment follows:

```text
Now:      token budgets, circuit breakers for daily spend, model selection policy, and cost-per-outcome tracking.
Proposed: token budgets, circuit breakers for daily spend, model selection policy, and cost tracking that starts with cost per token and expands to cost per outcome as the system matures (§3).
```

**Who decided.** Operator, 2026-11-20. The council voted the same way, 3 to 0. **Change class.** None fits; "normative loosening". **Impact.** None required.

### D16. Kill-switch states

**Question.** The pattern gives a kill switch the safe default `on`, and says automation trips it "to its safe default". A reader cannot tell which way is safe [DEL-10].

**Decision.** `on` stays the default. Normal is the default state, and tripped is the fallback, recorded on the flag.

**Proposed edit.** Feature flag governance §2, §4.4 and §6; invariant 7 of Release And Rollback follows:

```text
Now:      `on` (the safe state)
Proposed: `on` (the normal state)

Now:      an ops switch defaulting `off`
Proposed: an ops switch whose default is its tripped state

Added before "Prevents:":
An ops flag has two states: normal, which is its default, and tripped, the fallback it is switched to.

Now:      An ops flag MAY be tripped to its safe default by automation when the trip condition, safe default, and alert are recorded on the flag and the trip was tested before GA.
Proposed: An ops flag MAY be tripped by automation, from its normal state to its tripped state, when the trip condition, tripped state, and alert are recorded on the flag and the trip was tested before GA.

Now:      a description stating the safe default
Proposed: a description stating the safe default, or for an ops flag the tripped state,
```

**Who decided.** Council, 2 to 1, by one vote. **Change class.** None fits; "clarification". The MAY is the existing one. **Impact.** Each ops flag's description states its tripped state.

### D17. Context-fill thresholds

**Question.** Two pages give different figures for when a full context window degrades model quality, and neither cites a source [AI-28].

**Decision.** Both figures go.

**Proposed edit.** AI and ML systems §8, then agentic loop design §12:

```text
Now:      Model quality degrades steeply at 90%+ context fill.
Now:      At 95%+ context fill, model degradation is steep.
Proposed: Model quality can degrade as the context window fills.
```

**Who decided.** Council, 3 to 0. **Change class.** None fits; "correction". **Impact.** None.

### Eight decisions that leave rule text alone

| Question | Decision | Vote | Reason |
| --- | --- | --- | --- |
| D8. Saved plan files can hold secrets. Rule, caution or nothing? | A non-normative caution in one reference | 4 to 1 | The publisher says such data "will be saved in cleartext in the plan file" (https://developer.hashicorp.com/terraform/cli/commands/plan, read 2026-11-20). |
| D9. What provenance is expected of an internal production artefact? [XC-28] | Nothing further is said | 2 to 1 | ADR 0053 scoped the target to external and regulated artefacts. |
| D10. Is pinning extended to infrastructure modules and providers? | No | 2 to 1 | The majority read no source. The dissent cited a publisher page saying its lock file records providers only (https://developer.hashicorp.com/terraform/language/files/dependency-lock, read 2026-11-20). |
| D11. Does the known-exploited rule change now its catalogue's directive was replaced? | No, and nothing is added | 2 to 1 | The library cites the catalogue and names no directive (https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk, read 2026-11-20). ADR 0062 D2 rewords the same sentence to cover first-party findings; that edit is carried out first. |
| D13. Leaving a golden path: a reason, or a reviewed record? [UMB-11] | The pattern's form: "reason, reviewer, and expiry or trigger to revisit" | 2 to 1 | The principle hands the exception record to the pattern. |
| D14. Is a one-off data fix governed like a backfill? [OPS-02] | The reference's sentence is labelled non-normative | 2 to 1 | A reference cannot create a rule. |
| D18. Is a recovery exercise required before first production release? | Deferred | 2 to 1 | Any answer would pre-empt the operator's review of typed rules. |
| D19. Is a rule for retiring a service added? | No; "decommissioning a service is out of scope." stays | 2 to 1 | No owner covers it and no source was read. |

**Proposed edits.** Infrastructure Delivery (Boundaries and invariant 6) and Database Migration:

```text
D8, added: **Saved plan files (non-normative caution):** some plan tools can save a plan to a file that holds sensitive values in clear text, even where the terminal output hides them. Where a tool does this, keep the reviewed diff as the evidence and handle the saved file as sensitive. No canonical owner states a rule on secrets in retained evidence, so this is a caution only.

D8, now:      Plans are durable evidence.
D8, proposed: Plans are durable evidence; see the caution on saved plan files under Boundaries.

D14, now:      A one-off fix to persisted data follows the same batching, stop conditions, reconciliation, and schema-and-migration review as a backfill.
D14, proposed: Non-normative: no canonical owner states a rule for a one-off fix to persisted data. A sound choice is to treat it like a backfill, with the same batching, stop conditions, reconciliation, and schema-and-migration review.
```

**Deferral record for D18.** Owner: the repository operator. Trigger: 2026-12-18, the earliest date he has set for that review. It retires when he records a decision either way.

**Who decided.** Council for all eight. **Change class.** Additive guidance for D8; "correction" for D14; none for the rest. **Impact.** None required.

### The count

Six decisions add rule text (D2, D3, D5, D6, D7, D16), five remove or narrow it (D1, D4, D12, D15, D17), and eight leave it alone. No edit adds a capitalised keyword.

Nine were decided by one vote: D5, D9, D10, D11, D13, D14, D16, D18 and D19.

## Control Cost And Lifecycle

- D3: a person approves each bot update to a privileged pipeline definition. Review if that queue proves unworkable.
- D5: one small contract per kind of interactive work. Review when the agent-authority ADR lands.
- The rest cost one-off edits at most, and each can be reversed by a dated amendment to this record.

## Alternatives Considered

- **D1.** Add regulated data and money movement as triggers, as four of five seats meant.
- **D5.** Exempt interactive assistance that a person fully inspects. One seat.
- **D4, D8, D14.** An owner rule in each case. One seat each; one called leaving live data fixes without a rule unsafe.
- **D7, D16.** Take the field out of the skill until decided; treat "safe default" as the tripped state. One seat each.
- **D9, D10, D11, D19.** A stronger provenance target, pinning at SHOULD, a note on the directive, a retirement rule. One seat each.

## Consumer Impact And Migration

Change classes: **normative tightening** for D3, D7 and D12; **additive guidance** for D8; for the rest, each decision names its label. Compatibility: pre-1.0 minor.

Migration: take privileged pipeline definitions out of the low-risk update class (D3); stop tooling naming itself in `Signed-off-by` lines (D7); name a team where a README names only a channel (D12); state the tripped state in each ops flag's description (D16).

## Acceptance Criteria

- The operator has answered each bullet under "For the operator to confirm".
- Each owner and derived landing carries its proposed text as accepted.
- Run contracts §1.1 takes D2 and D5 in one change.
- ADR 0043 and ADR 0052 carry their amendment notes as worded here.
- The review register marks AI-01, AI-14, AI-28, DEL-10, GOV-03, OPS-02, OPS-11, SEC-15, UMB-11, UMB-13, UMB-18, XC-28 and XC-29 as settled here.
- The batch 3 owner audit marks findings 13, 15, 16, 19 and 24 as decided, and 22 as part decided, part deferred.
- The ADR index lists this decision, and doctrine preflight passes.

## Residual Risk

- The seats, the chair and this record's drafter are models of one family. No adopter was consulted.
- D5 keeps a trigger the review's only critical finding calls unworkable. A smaller contract does not make an assistant product enforce it.
- D7 and D16 rest on readings of the operator's meaning. If "safe default" meant the tripped state, D16's edits are wrong.
- D3 applies a list from the AI principle to changes a deterministic update bot opens.
- D4, D8 and D14 leave agent-run code, secrets in retained evidence and live data fixes with no owner rule. D6 leaves a wider signing finding open [SSEC-05].
