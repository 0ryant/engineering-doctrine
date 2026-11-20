# ADR 0064: Settle The Library's Own Rules, Records, And Tool Contract

- **Status:** Proposed
- **Decision date:** pending operator acceptance
- **Recorded date:** 2026-11-20
- **Retrospective:** No
- **Deciders:** Repository operator
- **Review provenance:** Decided item by item on 2026-11-20 by a model council at the operator's instruction, and by the operator himself where a decision says so; drafted and reviewed by models of one family; no independent human or domain review recorded
- **Research:** [Decision council, November 2026](../../doctrine/evolution/research-v080-decision-council-2026-11.md)
- **Canonical owner:** the [tool contract](../../contracts/doctrine-tool-contract.v1.schema.json) and [skill manifest schema](../../contracts/skill.v1.schema.json); [Agent Doctrine Consumption](../../doctrine/patterns/agent-doctrine-consumption.md); the [change harness](../../doctrine/maintainers/doctrine-library-change-harness.md); [GOVERNANCE.md](../../GOVERNANCE.md); the [versioning pattern](../../doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md); [`doctrine/impl/README.md`](../../doctrine/impl/README.md); the [honesty protocol](../../doctrine/test-protocols/test-5-honesty-rubric-v2.md); [Run Contracts](../../doctrine/patterns/run-contracts.md)
- **Derived landings:** the [change checklist](../../doctrine/checklists/doctrine-change-checklist.md); skills validator and manifests; nine research notes; [SECURITY.md](../../SECURITY.md); the [semantic index](../../doctrine/SEMANTIC_INDEX.md), [ADR index](README.md), and [review register](../../doctrine/evolution/review-full-doctrine-2026-11-findings.json); the `v0.8.0` sweep record; six earlier ADRs
- **Relationship to earlier decisions:** amends ADRs [0044](0044-adopt-agent-facing-consumption-contract-skill-schema-and-server-boundary.md) and [0048](0048-add-implementation-reference-layer.md); closes follow-ups from ADRs [0006](0006-add-governance-and-assurance-navigation-and-adopt-adrs.md), [0037](0037-land-mcp-cross-check-correction-batch.md), [0038](0038-adopt-a-doctrine-content-lifecycle.md), and [0039](0039-add-agent-loop-graph-decomposition-guidance.md); leaves [ADR 0027](0027-keep-public-doctrine-implementation-neutral.md) unamended. D1 and D2 ship with the exits in ADR 0061

## Context

On 2026-11-20 a model council decided the library's open questions. This record carries the seventeen about how the library governs and describes itself. A review seat changed one (D7). The operator answered three himself (D3, D4, D10), and his answers govern. Nothing binds until he accepts this record.

An implementation reference is a page under `doctrine/impl/` showing the normal way to do one task. The sweep is the review at each minor release. "§3" is the versioning pattern's list of change classes.

## Decision

### What the operator is accepting

1. Evidence cards can say a file was `superseded` or `rescinded`.
2. The layer list gains `impl` for implementation references.
3. Every non-editorial change has an ADR, new or cited.
4. Seven change classes join the seven in §3.
5. GOVERNANCE.md and the versioning pattern say patterns can hold rules.
6. An implementation reference draws on at least three owners.
7. No rule caps implementation references; the `v0.8.0` sweep checks them.
8. The honesty protocol is relabelled non-normative.
9. The `v0.8.0` notes carry no consolidated upgrade list.
10. The root hook files and tool configuration stay as they are.
11. Nine April 2026 research notes get a Historical banner.
12. Eighteen April and July 2026 proposals are rejected on the record.
13. The target-state research is not adopted; two reserved ADR numbers are released.
14. A retain verdict at the `v0.8.0` sweep closes the platform-engineering follow-up.
15. A short threat model for this repository is written.
16. Three protocol cross-check rows wait for the next specification revision.
17. The run-contract workflow deferral is reviewed and dated 2027-06-30.

### For the operator to confirm

Own calls, and points beyond the vote:

- D1, D2: the value name `impl`; contract version `1.1.0`, file still `v1`.
- D1: the skill status lists gain the same values now; no hash changes.
- D3: sitemap regeneration, Historical banners, and retain verdicts are editorial; research notes, sweep records, and changelog entries need no ADR.
- D4: the seven rows proposed, making fourteen classes; the contract's `change_class` list grows to match.
- D8: the protocol keeps its three capitalised keywords; the alternative lowers them.
- D10, D11: the register status `kept-0064` and the banner wording.
- D12: item 13 is the eighteenth; the council named seventeen singly.
- D13: numbers 0041 and 0042 stay unassigned.
- D14, D17: a demotion, or a real need to compose contracts, takes its own decision.
- D15: the threat model is a section of SECURITY.md.
- D9: whether to reverse it, given the fact in the table below.

### Decisions that leave the library as it is

| Question | Decision | Vote | Reason |
| --- | --- | --- | --- |
| D7. Cap implementation references until the sixteen are checked against their owners? | No rule; the `v0.8.0` sweep checks each. | 2 to 1 for a cap; changed by the council's review | A cap would pre-empt upgrades the operator set aside until 2026-12-18. (LIB-10) |
| D9. One list of every upgrade action in the `v0.8.0` notes? | Not adopted. | 3 to 2 against | Afterwards the operator stated that the library is in use in at least three enterprises (operator's statement, 2026-11-20). No seat knew this; he may want it reversed. |
| D10. Reword the hook scripts and style-checker configuration, where a review found private names? | They stay exactly as they are; the finding is closed as kept. | Operator, 2026-11-20; the council voted 3 of 5 to reword | His decision. (LIB-11) |
| D13. The August target-state research (nine items, no ADR after 100 days) and two reserved ADR numbers? | Not adopted; numbers released. Owner: repository operator. Trigger: 2027-04-30. Retires when an ADR on it is decided or he withdraws it. | 3 to 0 | His own proposition; this records a status only. |
| D14. Is the ADR that ADR 0038 asked for, on demoting the platform-engineering principle, still owed? | No. A retain verdict with reasons at the `v0.8.0` sweep closes it. | 2 to 1 | Only a demotion needs an ADR. |
| D16. Three additions ADR 0037 left open from a check against the Model Context Protocol (MCP) specification? | Carried into the re-check owed at the next revision. Owner: repository operator. Trigger: its publication. Retires when each is landed, replaced, or dropped. | 2 to 1 | The publisher: "For the next release, we're targeting March 30, 2027" (<https://blog.modelcontextprotocol.io/posts/mcp-release-cycle/>, read 2026-11-20). |
| D17. ADR 0039 deferred letting one run contract depend on another, for review at the first need "or a lifecycle sweep, whichever first". Four sweeps ran without it. | Stays deferred unless the `v0.8.0` sweep finds a real need. Owner: repository operator. Trigger: the first need or 2027-06-30. Retirement unchanged. | 2 to 1 | Nothing shows a need. |

```text
Review register, hook finding: status "kept-0064" (kept by the operator's decision, ADR 0064).
Semantic index: "(open gap — research only)" becomes "(not adopted; revisit by 2027-04-30)".
ADR index: "Numbers 0041–0042 are reserved for routed-but-unlanded work" becomes "Numbers 0041 and 0042 were reserved in August 2026 and never used. ADR 0064 released them; they stay unassigned."
Run Contracts §9: "or a lifecycle sweep, whichever first" becomes "or 2027-06-30, whichever first (reviewed at the `v0.8.0` sweep, ADR 0064)".
```

### D1. Entry status gains `superseded` and `rescinded`

**Question.** Each evidence card a tool server hands an agent carries a status. None says a file was replaced by a named successor, or disavowed.

**Now.** `entry_status` in the [tool contract](../../contracts/doctrine-tool-contract.v1.schema.json): `["active", "deprecated", "retired", "proposed"]`.

**Decision.** Add both. ADR 0061 has a file leave as Superseded in `v0.8.0`, with no status to carry. The versioning pattern §6 tells consumers to stop following Rescinded text "even on old pins"; today that arrives as `retired`. Skill status, in both schemas, gains the same values; the other schemas hold neither list. Council, 5 to 0. (GOV-05)

### D2. The layer list gains `impl`

**Question.** Each card names its layer, because agents take authority only from some layers. ADR 0048 made implementation references a layer, and the list has no value for them.

**Now.** `layer` lists ten values, `"umbrella"` to `"skill"`.

**Decision.** Add `impl`, named after its directory. Served as `pattern`, a reference gains authority `ENGINEERING.md` says it lacks. Council, 5 to 0; the name is this record's.

```text
entry_status: ["active", "deprecated", "superseded", "retired", "rescinded", "proposed"]
skill status, in both schemas: ["active", "deprecated", "superseded", "retired", "rescinded"]
layer: ["umbrella", "principle", "pattern", "impl", "checklist", "tooling", "estate", "evolution", "adr", "contract", "skill"]
change_class adds: "normative-addition", "normative-loosening", "correction", "clarification", "removal", "contract-revision", "maintainer-tooling"
contract_version and skill schema_version: "1.1.0"
Consumption pattern §2: "Deprecated and retired entries" becomes "Deprecated, superseded, retired, and rescinded entries"
Consumption pattern §3.3 adds: "`superseded` and `rescinded` skills are tombstones on the same terms as `retired`."
```

**Version.** `1.0.0` becomes `1.1.0`; the file stays `v1`. Values are added and nothing is removed. The verifier-pack schema took a minor number when it gained a value. No class in §3 fits; D4 adds "contract revision".

**Who has to act.** Anyone running a tool server built on this file, and nobody else: publish the contract document as `1.1.0`; serve each exited file with its banner's status, and `doctrine/impl/` as `impl`; update any schema copy clients validate against. A server pinned before `v0.8.0` is unaffected until it moves.

### D3. An ADR, new or cited, for every change that is not editorial

**Question.** When does a change to this library need an ADR? Three texts differ.

**Now.** GOVERNANCE.md accepts "an ADR or an explicit "why" in the PR". The harness says "Prefer at least one ADR". The checklist says "skip only for pure editorial".

**Decision.** The strictest becomes the rule. Operator, 2026-11-20: yes; the council had voted 2 to 1 for it. Normative tightening, for maintainers only. (GOV-08)

```text
Harness §3, opening sentence:
Every change to *this* library that is not editorial has an **ADR**, new or cited, per [docs/adr/README.md](../../docs/adr/README.md). Editorial means the Editorial class in versioning §3, sitemap regeneration, a Historical banner on a research note, and a sweep verdict that keeps a file. Cited means the change names an accepted ADR it carries out, or adds a dated amendment to the ADR it refines. Research notes, sweep records, and changelog entries need none.

Harness §3, last table row ("Prefer at least one ADR"): deleted.

GOVERNANCE review table, last row:
| Any change that is not **editorial** | Has an ADR, new or cited, per the change harness §3. A "why" in the PR does not replace it. |
```

### D4. Seven change classes join §3

**Question.** Release notes give each change a class, telling a consumer what an upgrade asks. §3 lists seven and asks for "one of these classes". Notes since `v0.6.0` also use clarification; correction (factual, normative); normative additions; normative loosening (permission); maintainer tooling (maintainer-process tightening); optional profile; citation; scoped typing; evidence only.

**Decision.** The labels in use join §3. Operator, 2026-11-20: agreed; the council had voted 3 to 2. Its three majority seats named three different sets, so this record proposes one. Removal and contract revision are new: files first leave in `v0.8.0`, and three releases asked hosts to re-pin under labels that do not say so. Additive guidance. (GOV-09)

```text
Versioning §3: "one of these classes" becomes "one or more of these classes".
Harness §§1, 9, and 10 and the checklist: each inline list of classes becomes "the classes in versioning §3".
```

Rows added to §3:

| Class | Examples | Consumer expectation |
| --- | --- | --- |
| Normative addition | A new typed rule | Check current practice against it. |
| Normative loosening | A rule weakens or becomes informative | No action; keep the stricter text if you rely on it. |
| Correction | A wrong fact or check is fixed | Re-check what you built on it. |
| Clarification | Wording or owner made explicit | Safe to absorb. |
| Removal | A deprecated file exits | Stop citing it; stop following Rescinded text even on old pins. |
| Contract revision | A schema, skill, or pack version changes | Re-pin if you pin or validate against it. |
| Maintainer tooling | Hooks, CI, scripts, maintainer-only rules | No action. |

Bracketed variants fold in; citation is a correction and scoped typing an addition. An optional profile and evidence only take no class.

### D5. Patterns can hold rules, and two texts say so

**Question.** `ENGINEERING.md` says "patterns own conditional operating models". Two texts speak as if only principles hold rules, which gives a pattern rule the lighter review.

**Now.** GOVERNANCE.md: "Additions in tooling, patterns, or examples (non-normative)". Versioning §1: "Normative expectations in `doctrine/principles/` and the umbrella `ENGINEERING.md`."

**Decision.** Both are brought into line. Council, 5 to 0. Release notes would say "clarification". On upgrade, a consumer also reviews the rules of activated patterns. (GOV-18)

```text
GOVERNANCE review table, first cells of rows 2 and 3:
| **Additions** in tooling or examples, and pattern text that states no rule (non-normative) |
| **Principles**, the **umbrella** `ENGINEERING.md`, and any **pattern** text that states a rule |

Versioning §1, first bullet:
- **Normative expectations** in `doctrine/principles/`, the umbrella `ENGINEERING.md`, and `doctrine/patterns/`, where a pattern's rules apply once its applicability conditions are met.
```

### D6. An implementation reference draws on at least three owners

**Question.** How many rule-owning files must an implementation reference draw on?

**Now.** The harness §1: "at least three canonical owners". ADR 0048: "several canonical files". The layer's README: "several canonical owners".

**Decision.** Three, written into the README. All sixteen references pass; each links 10 or more. Council, 2 to 1. A clarification for maintainers. (GOV-10)

```text
2. **Compression test:** it saves the reader from reconstructing one operating model from at least three canonical owners. If one or two canonical files already provide the same model, link to them instead.
```

### D8. The honesty protocol is relabelled non-normative

**Question.** `doctrine/test-protocols/test-5-honesty-rubric-v2.md` sits in a directory that no list of layers names, and calls itself canonical.

**Now.** Its status line begins "Canonical v2 protocol".

**Decision.** Relabelled; no layer is declared. Council, 3 to 0. The content lifecycle §3 calls this "a normative loosening" and asks for the migration story: only the sitemap and research and review notes link the file, so no reader was routed to its three typed sentences. (GOV-15, UMB-19)

```text
**Status:** Non-normative evaluation protocol. `ENGINEERING.md` names no test-protocol layer, so nothing in this file is an obligation of this library. The capitalised key words below are steps of the protocol and bind only someone who chooses to run it.
```

### D11. Nine April 2026 research notes are marked Historical

**Question.** ADR 0038 decision 7 named nine notes for a Historical banner, "each confirmed at execution". Four sweeps later none carries one.

**Decision.** All nine are marked. Live citations are repointed or marked as history. Instructions that point at a marked note change too, as the dissenting seat asked. Council, 4 to 1. Editorial and navigation.

| Note | Superseded by |
| --- | --- |
| [Mythos-era research](../../doctrine/evolution/mythos-era-engineering-principles-research-2026-04-28.md) | [ADR 0010](0010-record-mythos-era-vulnerability-storm-research-and-doctrine-gaps.md), which records its gaps as closed |
| [AI and ML ops landscape](../../doctrine/evolution/research-ai-ml-ops-landscape-2026-04.md); [enterprise RAG and indexing](../../doctrine/evolution/research-enterprise-rag-agents-indexing-2026-04.md) | The [AI gap audit](../../doctrine/evolution/research-bleeding-edge-ai-landscape-gap-audit-2026-08.md) of August 2026, with ADRs 0031 and 0037 |
| [Internal AI knowledge factory](../../doctrine/evolution/research-internal-ai-knowledge-factory-governance-2026-04.md); [section gaps](../../doctrine/evolution/deep-research-section-gaps.md); [MoSCoW review](../../doctrine/evolution/moscow-review.md); [benchmark gap analysis](../../doctrine/evolution/public-doctrine-benchmark-gap-analysis-2026-04.md); [taxonomy scorecard](../../doctrine/evolution/public-doctrine-taxonomy-scorecard-and-choice-2026-04-27.md); [scorecard against mainstream frameworks](../../doctrine/evolution/scorecard-vs-mainstream-frameworks.md) | Chair to confirm at execution; the August [lifecycle audit](../../doctrine/evolution/research-doctrine-lifecycle-audit-2026-08.md) names none |

```text
> **Historical** (marked at v0.8.0, ADR 0064): superseded by <links>. Kept as provenance; it is not current guidance.

Harness §5, last row: | **Related evolution notes** | **Optional:** a dated decision note or gap analysis for large shifts. |
Checklist, both mentions: "evolution/moscow-review.md or " is removed.
GOVERNANCE, Roadmap: the example link becomes doctrine/evolution/review-full-doctrine-2026-11.md.
```

### D12. Eighteen proposals are rejected on the record

**Question.** Eighteen proposals in April and July research notes were never taken up and never declined. The content lifecycle §8: "An ownerless deferral is a defect, not a plan."

**Decision.** All eighteen are closed, with no verdict on merit; any can return through the change harness with a source and an owner. Each was checked against its note. Council, 2 to 1; the third seat would have kept open the retirement of a service, which no note raised and D13 holds.

| Note | Proposals rejected |
| --- | --- |
| [Anti-patterns gap analysis](../../doctrine/evolution/anti-patterns-and-failure-modes-gap-analysis-2026-04.md), April | (1) failure-mode index; (2) capacity allocation; (3) data classification; (4) test smells; (5) build-versus-buy; (6) support communications; (7) worked bad examples; (8) review cadence; (9) "pitfall" glossary synonym; (10) self-assessment canvas |
| [Benchmark gap analysis](../../doctrine/evolution/public-doctrine-benchmark-gap-analysis-2026-04.md), April | (11) user-need handshake; (12) ADR and RFC templates; (13) adopter scorecard; (14) sustainability checklist; (15) code of conduct file |
| [AI and ML ops landscape](../../doctrine/evolution/research-ai-ml-ops-landscape-2026-04.md), April | (16) Azure AI Landing Zone estate page |
| [AI-native SDLC research](../../doctrine/evolution/research-ai-native-sdlc-2026-07.md), July | (17) "Universal record schema and global autonomy thresholds" |
| [NIST SP 800-171 profiles research](../../doctrine/evolution/research-nist-sp-800-171-control-profiles-2026-07.md), July | (18) "Encode every requirement in repository schemas now" |

### D15. A short threat model is written for this repository

**Question.** ADR 0006 promised: "Add a lightweight threat model for the doctrine repo itself." None was written, and the repository now ships skills that hosts inject into agents' prompts.

**Decision.** A short one is written, as a section of SECURITY.md. It binds nobody. Council, 2 to 1; the third seat would have struck the promise. Additive guidance.

It covers what is protected (rule text, skills, schemas, scripts, CI, tags), who can change each, the threats (a weakened rule merged as a small change, a poisoned skill, a compromised account or CI dependency, hostile source text steering an agent), and each control and gap. Only the operator knows who can merge and tag and how those accounts are protected. Owner: repository operator. Review trigger: a change to skills, contracts, CI, or merge rights.

### Dated notes for earlier ADRs

Appended on acceptance under `## Note (<acceptance date>): ADR 0064`.

```text
ADR 0006: The threat-model follow-up is carried out as a section of `SECURITY.md` (ADR 0064 D15).
ADR 0037, and the head of the cross-check note's §4: Rows 3 to 5 of the cross-check's action list were not landed. They wait for the cross-check owed at the next specification revision, targeted 2027-03-30. Owner: repository operator. They retire when it records each as landed, replaced, or dropped (ADR 0064 D16).
ADR 0038: Decision 7's Historical banners are carried out (ADR 0064 D11). A retain verdict with reasons at the `v0.8.0` sweep closes the platform-engineering follow-up; a demotion needs its own ADR (D14).
ADR 0039: The `v0.8.0` sweep reviews the workflow deferral, and its trigger names 2027-06-30 in place of "a lifecycle sweep" (ADR 0064 D17).
ADR 0044: The tool contract becomes 1.1.0: entry status gains `superseded` and `rescinded`, the layer list gains `impl`, and skills gain the same two exit states (ADR 0064 D1, D2).
ADR 0048: "several canonical files" is fixed at "at least three canonical owners" in `doctrine/impl/README.md` (ADR 0064 D6).
```

## Control Cost And Lifecycle

- D3 and D4 add recurring work; each can be reversed alone. The last sweep counted 1.85 record and maintainer words for each rule word, and D3 adds more.
- Six standing duties arise. Five are the operator's: accept an ADR or amendment for each non-editorial change (D3); sign release notes using fourteen classes (D4); review pattern rule changes as principle changes (D5); keep the threat model true (D15); answer the workflow-deferral review (D17). The sixth falls on anyone running a tool server: keep status, layer, and contract version true (D1, D2). Agents draft the D3 and D4 work.
- The council's review counted nine standing duties across all its decisions; these are six of them. It priced D4 at eleven classes.

## Alternatives Considered

- **A reduced status list mapped in prose.** No votes; an agent could not tell "replaced" from "stop following this".
- **An ADR only for structural changes and typed rules.** One seat of three; 35 of 67 principle and pattern files carry no typed keyword.
- **Map every label onto the original seven.** Two seats of five; it files a factual correction as editorial.
- **Strike the cross-check rows; withdraw the workflow deferral.** One seat of three each.

## Consumer Impact And Migration

No rule that an adopting team follows changes, and adopting teams do nothing. Anyone running a tool server follows the steps under D2 when it moves its pin to `v0.8.0`. A decision that names no change class has none. Pre-1.0 minor.

## Acceptance Criteria

- The tool contract carries the values under D2, in the release that carries ADR 0061's exits.
- A test loads that schema, accepts `superseded` and `impl`, and rejects an unknown status.
- The harness, GOVERNANCE.md, and the checklist give one rule for ADRs, and §3 lists fourteen classes.
- The `v0.8.0` sweep record covers the sixteen references, the platform-engineering verdict, and the workflow deferral.
- Each of the nine notes carries a banner naming its successor, or the sweep record says why not.
- The hook and configuration files are unchanged; SECURITY.md holds the threat model; the six dated notes are appended.
- The ADR index lists this decision and no reserved numbers, and doctrine preflight passes.

## Residual Risk

- Every seat, the review seat, and the drafter are models of one family. Ten of the seventeen decisions turned on one vote.
- In D1, D3, D4, and D8 the seats agreed a direction and meant different texts; this record chose one.
- The status list has no value for Historical, so the nine marked notes are served as `active`. Nobody has counted the servers built on the contract.
- D10 leaves private names in tracked files and published tags; a later reviewer will find them again.
