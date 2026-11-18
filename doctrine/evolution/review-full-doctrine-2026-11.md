# Full Doctrine Review, November 2026

Date: 2026-11-18. Repository basis: `1eedc9e`.
Status: non-normative review record. It adopts no control and changes no consumer obligation. Model review only; no independent human or domain review.

Every finding, with its quoted evidence and proposed change, is in the [findings register](review-full-doctrine-2026-11-findings.json).

## Standing Of These Findings

The rules in this library are the maintainer's own, drawn from operating experience and from incidents. Models draft wording and check sources at his direction. A reviewer's grade, severity, or objection below is an input to his decision, not a ruling. Reviewers judged the text without knowing the experience behind a rule, because the text does not record it.

This note therefore separates two things. Checkable facts (a standard misquoted, a command that does not exist, a withdrawn citation, a derived page that contradicts its principle) were corrected. Objections to what a rule asks were not acted on; they are listed for the maintainer to keep, sharpen, or change.

## Question

Is the doctrine accurate, calibrated, usable, and consistent with itself, and what has changed since the August corpus review and the September scorecard?

## Method And Limits

Twelve model reviewers read the tree at the basis commit, each without sight of the others' output.

- **Seven consistency reviewers.** Six read one slice in full: delivery and build; security and identity; reliability, data, and events; AI and agents; summaries and navigation; glossary and library governance. One swept 26 concepts across the whole library to catch conflicts between slices.
- **Four substance reviewers.** Each took one domain as a senior practitioner and judged correctness, strength, testability, omissions, proportionality, weight, evidence, and portability, then graded every principle, pattern, and implementation reference.
- **One whole-library assessor.** Structure, reader path, weight, provenance, rate of change, and progress since earlier assessments.

Checks on the reviewers: every finding quotes the text it relies on, and a script confirmed each of the 360 quotes as an exact substring of the named file. A second script confirmed that every `file.md §N` reference and heading anchor in the library resolves to a section that exists.

Limits. All twelve reviewers are instances of one model family, which is the library's central review weakness and is not cured by this note. The lead author spot-read findings while applying corrections but did not re-derive each one. Most external facts were not re-checked; where a reviewer relied on one, the register says whether it was confirmed on the publisher's page. Substance grades are one reviewer's judgement per file.

## Verdict

1. **The classical core is mainstream and mostly sound, and thin on mechanics.** Reviewers would adopt the build, merge-path, review, declarative-operations, idempotency, acknowledgement, supply-chain, and workload-identity material after fixes. They would not put a team under the API boundary, audit logging, cluster security, privacy, data and migrations, incident, testing, cost, feature-flag, platform-engineering, or trunk-workflow files as written.
2. **The AI and agent third grades lowest.** Two-thirds of its files grade C or D. Any tool call makes a run "governed"; run contracts and verifier packs bind an executor nobody ships; the capability tiers are kinds, not a ladder, so they cannot trigger controls.
3. **The library is accreting, not converging.** Words are up 80% in fifteen weeks. Nothing has been retired. The two decisions that would subtract (ADRs 0046 and 0047) have sat Proposed since 2026-09-03, while eight that add were accepted between 15 and 18 November.
4. **The rules rest on the maintainer's experience, and the text does not show it.** No rule records the incident or practice behind it, and no ADR records an independent review, so a reader cannot see what a rule rests on. The README, the umbrella, and the governance file do not say whose rules these are or how the text is drafted and checked. On the library's own source scale, dated first-party experience is admissible evidence once it is written down.
5. **It was inconsistent in 179 places.** 107 are corrected in the change that lands this note. 52 need a decision, and one is settled by ADR 0058.

## Measurements

From the whole-library assessment; commands are in the register.

| Measure | Value |
| --- | --- |
| Size | 331,679 words in 231 Markdown files; 183,760 at v0.4.0 (2026-08-03) |
| Share of words | 37% rules and guidance an engineer applies; 6% navigation; 57% the library about itself, mostly research notes and ADRs |
| Typed keywords in principles | 85 typed, 85 lower-case "must" or "should"; 19 of 34 files have no typed keyword |
| Typed keywords in patterns | 188 typed, 115 lower-case; 54 of 164 MUSTs sit in patterns that govern the library itself |
| ADR status | 44 Accepted, 2 Proposed, 1 Rejected, none Superseded |
| Review provenance | 0 of 47 ADRs record independent human or domain review |
| Lifecycle | 3 deprecated files, no tombstones, 0 of 47 research notes marked Historical |
| Since the last tag (v0.5.0, 2026-09-15) | 9 ADRs and 127 changed files, unreleased |
| Scorecard lenses, September to now | Engineering manager 3.2 to 3.3; CIO 3.0 to 3.0; security engineer 3.0 to 3.1; non-technical sponsor 2.3 to 2.3 |

## Grades

A: adopt as is. B: adopt with minor fixes. C: needs substantial rework before a team relies on it. D: remove or rewrite.

### Delivery And Platform

| File | Grade | Reason |
| --- | --- | --- |
| principles/build | B | Sound; the local-gate rule lacks a carve-out |
| principles/collaboration | B | Conventional; loose trunk threshold; a solo maintainer cannot meet the review rule |
| principles/merge-path-evidence-and-pipeline-integrity | B | Invariants 1 to 7 strong; 8 binds nothing; 9 blocks on any severity |
| principles/semantic-versioning | B | Patch definition contradicts SemVer |
| principles/single-source-of-truth | A | Calibrated |
| principles/naming-and-repo-layout | C | Too thin; monorepos unaddressed |
| principles/modularity-and-ports-adapters | A | Contextual, no overreach |
| principles/documentation-knowledge | B | Sound; unsourced cadences |
| principles/developer-experience | B | Accurate; no bound on gate time |
| principles/platform-engineering | C | Unsourced numbers; reads as a book summary |
| principles/measurement-and-dora | B | Five metrics right; scope stated wrongly |
| principles/timeless-principles-and-tooling | B | Clear layering |
| principles/container-runtime-choice | B | Sensible; ignores managed clusters |
| patterns/build-surface-model | B | Useful shapes |
| patterns/trunk-workflow | C | Hotfix direction; release branches only as a legal exception |
| patterns/code-review-and-change-approval | B | Strong duties; method-record rules unenforceable |
| patterns/gitops-and-declarative-operations | B | Accurate on OpenGitOps; push overstated as equivalent |
| patterns/feature-flag-governance | C | Good taxonomy; full lifecycle unusable as a baseline |
| patterns/platform-as-product-and-golden-paths | A | Proportionate and staged |
| patterns/adoption-playbook | B | Practical |
| patterns/outcome-and-portfolio-linkage | B | Well bounded; abstract |
| impl/cicd-delivery | A | Best composition |
| impl/git-hooks | A | Concrete and correct |
| impl/branching-and-integration, git-worktrees, release-and-rollback, infrastructure-delivery, testing-and-verification | B | Keep |
| impl/application-deployment | C | An index of fifteen owners |
| impl/new-service | C | Restates; only its routing table earns a place |

### Security And Privacy

| File | Grade | Reason |
| --- | --- | --- |
| principles/secure-development-lifecycle | C | Vulnerability response sound; the rest is five untyped bullets |
| principles/dependencies-supply-chain | B | Build-level table correct; signing and registry sections need fixing |
| principles/threat-modeling-stride-lite | B | Strong acceptance bar; no typed trigger or ranking |
| principles/zero-trust-and-workload-identity | B | Right design; the MUST is mis-scoped; no trust-policy rule |
| principles/configuration-and-secrets | B | Correct but thin; no leaked-secret response |
| principles/api-boundaries-and-security | C | Authorisation is two bullets; no transport or input rules |
| principles/kubernetes-platform-security | D | A dozen untyped bullets |
| principles/audit-logging | C | Would not satisfy an auditor on integrity, time, or retention |
| principles/privacy-and-data-governance | C | Transparency duties accurate; data-protection duties stated as universal |
| patterns/webhook-ingress-security | B | Sound |
| patterns/revision-pinned-control-profiles | C | Over-fitted to one baseline; no applicability screen |
| patterns/normative-language-applicability-and-exceptions | B | Strong admissibility rules |
| patterns/engineering-controls-governance-program | B | Good calibration |
| impl/service-api, secretless-workload-identity, dependency-adoption | B | Usable; inherit owner gaps |
| impl/privileged-automation | C | Restates invariants with no worked example |

### Reliability, Data, And Events

| File | Grade | Reason |
| --- | --- | --- |
| principles/reliability-slo-incidents | B | Runtime-shape section right; objective and budget rules untyped |
| principles/observability | B | Burn-rate table matches its source; low-traffic rule wrong |
| principles/errors-and-failure-modes | C | Error formats only; nothing on timeouts, retries, or overload |
| principles/data-and-migrations | C | Expand order wrong; unsafe batch range |
| principles/event-contracts | B | Envelope guidance accurate |
| principles/state-machines-and-workflows | B | Sound |
| principles/performance-and-cost | C | Budgets unmeasured |
| principles/cost-and-finops | C | Enterprise-only; unsourced numbers; unsafe utilisation default |
| principles/testing-strategy | C | Good opening; flaky and contract rules two lines each |
| principles/user-facing-quality | B | Accessibility level accurate; legal framing dated |
| principles/interoperability-and-standards | B | Harmless |
| patterns/idempotency-across-boundaries | B | Best text in the slice |
| patterns/message-channel-operations | B | Acknowledgement rule strong |
| patterns/incident-lifecycle-and-on-call-operations | C | Not executable on call; a quarter is about agents |
| patterns/chaos-engineering-and-game-days | B | Usable template |
| patterns/example-order-jetstream-workflow, example-saga-payment-workflow | C | Technically wrong in places |
| impl/database-migration, testing-and-verification | A | Correct and useful |
| impl/event-consumer | B | Usable |
| impl/service-observability | C | Restates headings |

### AI And Agents

| File | Grade | Reason |
| --- | --- | --- |
| principles/ai-ml-systems | C | Tiering unusable as a trigger; good rules buried |
| patterns/agentic-loop-design | C | Strong sections inside a dated tutorial; one withdrawn source |
| patterns/ai-adoption-controls | B | Regulation cited accurately; no scale-down |
| patterns/ai-native-software-development-lifecycle | C | Still 4,084 words; no floor for routine change |
| patterns/run-contracts | C | Right idea, written for one runtime |
| patterns/verifier-packs | D | Kind list fits one tool |
| patterns/rag-retrieval-baseline | B | Sound; thin on isolation and output exfiltration |
| patterns/anti-confabulation-priming | D | 150 lines around a six-line prompt |
| patterns/agent-doctrine-consumption | D | Maintainer doctrine in the consumer path |
| patterns/agent-ready-application-shipping-profile | C | Mandates autocomplete; omits agent operability |
| Observability §7 | A | Best section in the slice |
| Zero trust §2.1, merge path §§1–2, cost §§7–7.1, dependencies §§7–8, incident lifecycle §10 | B | Sound with fixes |
| Code review §§6–6.1 | C | Preference typed as MUST |
| impl/git-worktrees | A | Concrete and correct |

## What Is Strong

Reviewers named eighteen things that later fixes should not weaken. Among them: the gate-versus-telemetry distinction in merge path; the blocker-versus-nit rule in code review; idempotency §1; acknowledgement after a durable effect; the workload runtime shape; the statement of what provenance and signatures do not prove; the secretless default with a registered fallback; the falsifiable blast-radius bar in threat modelling; the rule that exceptions cannot rewrite results or waive law; schema-neutral model-call telemetry with content capture off; model artefacts admitted like code; and enforcement of agent limits outside the model.

## Most Consequential Substance Findings

163 findings: 1 critical, 127 major, 35 minor. By the reviewers' own classification: 36 rules they thought too weak, 25 omissions, 19 statements they called wrong, 18 rules they thought too strong.

**Facts corrected in this change.** Each was checked on the publisher's page on the access date. None changes what a rule asks.

- The secure-development practice groups were mislabelled in four files; the publisher's descriptions are now used.
- The burn-rate tooling example carried two of the three tiers in the principle's own table; it now carries all three.
- The burn-rate failure-mode table described the comparison incorrectly, and the thresholds' 30-day window was unstated.
- The messaging example and tooling page used another transport's header names for CloudEvents attributes, and described a binding mode that the released binding does not define.
- The messaging example offered a retention mode that removes acknowledged messages, then promised replay.
- A lockfile check named a command that does not exist.
- A citation that its host withdrew on 2026-11-03 is removed. The rule it sat under is unchanged and rests on its other source.

**Rules a reviewer disputed.** These are the maintainer's rules. Each line gives the reviewer's objection and what was verified. The review changed none of them. The maintainer then chose the first four below to redraft, in [ADR 0058](../../docs/adr/0058-sharpen-four-rules-after-the-november-2026-review.md) (accepted 2026-11-18); the other nine stay as written.

| Rule as written | Reviewer's objection | Verified |
| --- | --- | --- |
| On a termination signal a workload stops taking new work (reliability §8) | Routing stops concurrently with the signal on the commonest orchestrator, so refusing work at once still drops requests | The orchestrator's documentation says both happen at the same time |
| Expand, move writers and readers, backfill, remove (data and migrations §1) | Readers would move before the backfill; the implementation reference backfills first | A widely cited practitioner account backfills before switching reads |
| Attach provenance with a signing tool in a build step (dependencies §4) | The specification asks for provenance generated by the platform's control plane, not by a tenant step | The specification says so for Build L2 |
| Delivery metrics describe how the organisation delivers (measurement and DORA, introduction) | The research applies them to one application or service | The publisher's guide says so |
| A patch release may carry additive behaviour (semantic versioning §2) | The specification reserves patches for bug fixes and requires a minor for additions | The specification says so in items 6 and 7 |
| Peak CPU 60 to 75% as the rightsizing default (cost and FinOps §5) | A service sized to lose one of N instances can use at most (N−1)/N at peak | Arithmetic only |
| A low-traffic service may use a single-tier alert (observability §6) | One tier does not address too few requests; the source suggests synthetic traffic, grouping, or longer windows | The source lists those remedies |
| Resolve internal packages from the private registry first (dependencies §7) | Some resolvers take the highest version across sources, so precedence is not a setting that holds everywhere | Not checked |
| The API risk table credits §§2 and 3 with controls | Some named controls appear only in the table | Confirmed by reading the file |
| A wildcard origin with credentials is a code smell (API boundaries §6) | Browsers already block it; reflected origins are the exploitable case | Browser documentation confirms the block |
| Typed tool output so the model reads values, not instructions (agentic loop design §9.3) | A string in a typed field is still read as text | Not checked |
| The order example's committed transition; the saga example's step order and compensation path | A dual write can lose events; compensation has no failure path | Not checked |
| A stream consumer type offered as a partition analogue (message channel operations) | That consumer type is meant for restartable reads | Could not be confirmed on the publisher's pages |

**Graded critical by its reviewer.** Any tool call makes a model run "governed" and demands a full run contract, so every interactive coding session is in scope.

**Omissions the reviewers ranked first.** Timeouts, retry discipline, and overload protection. Input validation, transport security, and request forgery. Unreviewed changes running with secrets or privileged tokens. Approval bound to the reviewed revision. Sandboxed execution and egress control for agents. Model version pinning. Backups isolated from the primary's failure and credential domain.

**Rules reviewers thought too strong.** The full flag lifecycle as a baseline for any runtime flag. A promotion gate that blocks on any new advisory at any severity. A dual-model architecture required of every tool-using agent. Bans on tool co-author fields that hosting platforms set by default.

### Sources For The Four Redrafted Rules

Classes follow [Source Authority And Evidence Grading](../patterns/source-authority-and-evidence-grading.md) §2. Each page was read by the lead author on 2026-11-18. No archive copies were captured.

| Rule | Source | Class | Supports |
| --- | --- | --- | --- |
| Graceful stop | [Kubernetes: Termination of Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-termination/) | S5, product-scoped | Removal from service endpoints starts at the same time as graceful shutdown of the workload |
| Migration order | [Stripe: Online migrations at scale](https://stripe.com/blog/online-migrations) (2017) | S6, vendor engineering account | Dual write and backfill come before read paths change; old data is removed last |
| Provenance mechanism | [SLSA v1.2 build requirements](https://slsa.dev/spec/v1.2/build-requirements) | S4, versioned foundation specification | At Build L2 the provenance is generated by the platform's control plane, not by a tenant |
| Delivery-metric framing | [DORA: software delivery performance metrics](https://dora.dev/guides/dora-metrics/) | S4, disclosed-methodology research programme | The metrics apply at the application or service level; deployment frequency is a count or interval of deployments |

## Findings Against Text Added This Month

ADRs 0051 to 0057 were drafted by a model at the maintainer's direction and accepted by him in the week before this review. The security reviewer found that text more accurate than the older text around it. It still drew objections:

- The SBOM MUST requires attaching the SBOM to the artefact, which the cited regimes do not.
- The secretless MUST tests only the target, gives brownfield estates no migration path, and says nothing about the federation trust policy.
- Saved infrastructure plans can hold secrets, and three files say to keep plans as evidence.
- Drift has a third legitimate ending the new invariant omits: excluding a field from management.
- Graceful stop is worded wrongly, as above.
- Three of the four newest implementation references grade C.
- Composing implementation references generated 39 owner gaps and two decisions adding rules in one month. The layer that must create no requirements has no stopping rule.

## Corrections Applied In This Change

131 edits in about fifty-five files: 110 for consistency and 21 for the facts listed above. Each aligns wording, a pointer, or a stated fact with what a canonical owner, an accepted decision, or the cited publisher already says. None changes a rule's strength, scope, threshold, or ordering.

- **Stale pointers:** semantic versioning §8 to §9; the secure-development map from timeless principles §6 to §7 and from dependencies §5 to §§2 and 7; glossary and principle references to umbrella sections that no longer exist; tooling rows citing the wrong lifecycle sections.
- **Leftovers of recent decisions:** workload identity still "preferred" in three files after ADR 0051; an SBOM trigger in a checklist and a rationale row that overstated ADR 0053; first uses of renumbered OWASP identifiers without the prior identifier, and prior identifiers without a year (ADR 0056); declared-state rollback described as review-first in two references after ADR 0057.
- **Derived pages against owners:** checklist prompts stronger or narrower than their owners; glossary entries for outbox, hermetic build, acknowledgement, agent-definition artefact, agent responder, and four others; the semantic index had no route to the platform-engineering principle.
- **One fact:** the same incident was cited under two vendor bulletin numbers. The vendor's pages confirm which is correct, and the other row is removed.
- **Terminology:** delivery metrics named by their current definitions in five places; one name for the fourth content class; secure-development practice groups labelled correctly.

## Decisions Needed

52 consistency findings need a choice between positions or a change of strength. Grouped, they are about thirty decisions:

| Topic | Findings |
| --- | --- |
| Agent and automation authority: the principal tiers, "agents propose" against agents that write to production, the lists of changes needing human approval, a judge as sole authority, runtime human fallback, isolated execution | AI-01 to AI-05, AI-14, AI-18, SEC-15 |
| Immutable references: digest, version, or tag | DEL-02, SEC-16, XC-14 |
| Data corrections with no owner (the migration sequence itself is redrafted in ADR 0058) | OPS-02 |
| Threat-model trigger | SEC-07, XC-30 |
| Ownership form: team, alias, or role with a named holder | UMB-13, XC-29 |
| Same-artefact promotion: conditional or not | DEL-18, UMB-09 |
| Known-exploited vulnerabilities: always first, or usually | SEC-08, XC-31 |
| Flags: what "safe default" means for an ops flag | DEL-10 |
| Claimed platforms: exercise each, or one other | DEL-13 |
| Exercise windows, and two owners for fault-injection safety | OPS-04, OPS-05, XC-09, XC-32 |
| Cost: tag keys, cost-per-outcome timing, agent payment duplicates | OPS-10, OPS-11, XC-10, XC-20 |
| Prompts and references with no owner behind them | DEL-05, DEL-12, OPS-13, OPS-16, SEC-14 |
| Precedence and layering: "this file wins", golden-path departure, illustrative examples, the test-protocols folder | UMB-08, UMB-11, UMB-18, UMB-19, GOV-15 |
| The library's rules about itself: when an ADR is required, change-class vocabulary, exit states in skill and tool contracts, owner count for a reference, where normative text may live, tool sign-off lines | GOV-03, GOV-05, GOV-08, GOV-09, GOV-10, GOV-18 |
| Smaller scope and strength mismatches | DEL-08, XC-16, XC-23, XC-25, XC-26, XC-28 |

[ADR 0059](../../docs/adr/0059-apply-three-constitution-rules-to-settled-inconsistencies.md) (accepted 2026-11-18) settles 30 of the 52 by applying three rules already in `ENGINEERING.md`: the stricter result where two rules protect one property, one authority per concept, and checklists that derive from owners. It covers the rows above on immutable references, the threat-model trigger, same-artefact promotion, known-exploited vulnerabilities, claimed platforms, exercise windows and fault-injection safety, and prompts with no owner; the human-approval lists and runtime human fallback from the first row; tag keys and agent payment duplicates from the cost row; "this file wins" from the precedence row; and five of the six smaller mismatches. It also closes two findings left open: the missing rules for timeouts, retries, and overload (SOPS-01), and a duplicate of the pinning finding (AI-10). Twenty-two decisions remain: agent and automation authority (AI-01, AI-02, AI-04, AI-05, AI-14, SEC-15), ownership form, data corrections, ops-flag defaults, cost-per-outcome timing, provenance for internal artefacts (XC-28), the rest of the precedence row, and the library's rules about itself.

Fifteen more corrections are held, not decided. Eight touch hash-pinned skills and versioned contract files, including a navigation skill that tells agents the umbrella is not authority. Those need a version bump the maintainer should approve.

## Recommended Order

The whole-library assessment and the domain reviews point the same way: subtract and correct before adding.

1. **Decide ADRs 0046 and 0047**, then execute them: maintainer doctrine out of the consumer path, the AI-native lifecycle pattern collapsed, private vocabulary retired.
2. **Freeze normative additions and tag a release** of what has landed since v0.5.0. (`v0.6.0` was tagged on 2026-11-18.)
3. **Say at the front door whose rules these are and what they rest on**: the maintainer's operating experience, cited sources, and model-assisted drafting and checking.
4. **Settle the disputed rules** in the table above: keep, sharpen, or change each. Four are redrafted in ADR 0058; nine are kept. Where a rule is kept against an objection, a line recording the experience behind it would answer the next reviewer.
5. **Record the experience behind the rules that matter most.** A dated first-party account is evidence on the library's own scale. An independent review, starting with the supply-chain sections, would add a second.
6. **Type the classical core by deciding old claims**, not by adding new ones.
7. **Narrow governed execution** to unattended or production-authority runs, and reduce run contracts to a minimum any harness can meet.
8. **Take the decisions above in themed batches**, agent authority first. ADR 0059 takes the thirty that the constitution already decides.
9. **Only then fill the ranked omissions**, each through its own decision with an external source.
10. **Produce adopter evidence**: one filled estate instance and one recorded trial.

## Residual Risk

One model family reviewed text that one model family drafted. Reviewers could be wrong together, and they judged rules without knowing the incidents that produced them. Grades and severities are single judgements. The corrections applied were chosen for being uncontroversial, and a correction that looked editorial may still shift a reader's understanding of a rule. External facts behind several findings rest on the reviewers' recall. The register preserves the evidence so each finding can be re-checked.
