# ADR 0046: Retire Private Vocabulary Where A Standard Term Exists

- **Status:** Accepted
- **Decision date:** 2026-11-18
- **Recorded date:** 2026-09-03; amended 2026-11-18
- **Retrospective:** No
- **Deciders:** Repository operator
- **Review provenance:** Operator-accepted on 2026-11-18 as amended; drafted by a model on 2026-09-03 and amended by a model on 2026-11-18 at the operator's direction, after the counts were re-measured; no independent human or domain review recorded
- **Responds to:** the 2026-09-03 cold-truth assessment, fix 2; findings SAI-21 and SAI-34 in the [2026-11 review](../../doctrine/evolution/review-full-doctrine-2026-11.md)
- **Canonical owner:** none changes. [ENGINEERING.md](../../ENGINEERING.md) stays canonical for core vocabulary; [normative-language-applicability-and-exceptions.md](../../doctrine/patterns/normative-language-applicability-and-exceptions.md) §3 gains one definition
- **Derived landings:** [glossary.md](../../doctrine/glossary.md); wording in the files that use the replaced compounds
- **Relationship to earlier decisions:** the three lifecycle terms wait for the ADR that rewrites the AI-native lifecycle pattern, which [ADR 0047](0047-separate-maintainer-doctrine-and-collapse-the-ai-native-sdlc.md) no longer carries

Accepted on 2026-11-18. Batch A (D1 to D3) is executed in the change that records this acceptance. Batch B (D4) waits for the lifecycle rewrite.

## Context

The assessment counted the library's private coinages and found them pervasive. Its charge is that a reader must learn a dialect before the rules become readable. The charge is partly right and partly wrong, and this ADR separates the two so the operator can decide term by term.

The test applied to each term: does a standard term exist that carries the same distinction? If yes, the coinage is retired. If the coinage names a distinction the library depends on and no standard term carries it, the coinage stays, is defined once, and is used consistently.

### What changed between the draft and this amendment

The counts were taken again on 2026-11-18 at `04d474a`, by the same method at the commit before the draft (`cb073f2`) and today. They are case-insensitive whole-word matches over the umbrella, principles, patterns, and checklists. The last column counts implementation references, which did not exist in September.

| Term | September | Now | Implementation references |
| --- | --- | --- | --- |
| estate | 199 in 46 files | 242 in 51 | 37 |
| compounds beginning "estate-" | 37 | 46 | 9 |
| of which "estate-governed" | 6 | 12 | 9 |
| materiality | 74 in 18 | 77 in 18 | 3 |
| candidate | 81 in 15 | 93 in 20 | 82 |
| governed execution | 21 in 9 | 22 in 9 | 4 |
| enactment | 17 in 5 | 17 in 5 | 8 |
| mandate class | 9 in 3 | 9 in 3 | 0 |
| closure mode | 3 in 2 | 3 in 2 | 0 |
| record families | 2 in 2 | 3 in 2 | 0 |
| membrane, typed denial, loud-not-silent | 7 | 2 | 0 |
| house law | 2 | 1 | 0 |

The first version of this amendment gave that row as five and zero. It had missed the hyphenated form "typed-denial", which the counts now include.

Three facts came out of the re-measurement and changed the draft.

1. **"Enactment" is constitution vocabulary.** Core Proposition 2 of the umbrella reads "Advice, implementation, verification, authorisation, and enactment are distinct duties". The draft treated the word as a gate name in one pattern and proposed "deployment, or execution, by context". "Execution" is already a different duty: the applicability table asks who may "propose, execute, authorise, and enact change". "Deployment" is narrower, because the word also covers an infrastructure apply, a data change, and an agent carrying out a pre-authorised action. The glossary has no entry for it.
2. **"Estate-governed" now sets the scope of rules.** The draft counted 11 compound uses and proposed replacing them. "Estate-governed" alone now has 26 uses across the published layers and scopes at least eight MUST or SHOULD rules: secretless workload identity, the pre-install gate, the protocol revision pin, the cryptographic inventory, model and dataset admission, GenAI telemetry, the method record, and the retrieval contract. It is defined nowhere. It also sits inside one skill's hashed priming block.
3. **"Materiality" is used outside the AI layer.** Cost, audit logging, the governance programme, and the reading guide all use it. The draft's "impact elsewhere" would add a second name for one idea, against the umbrella's rule of one authority per concept.

## Decision

### D1. Retired in September, finished here

| Term | Replacement |
| --- | --- |
| membrane | boundary |
| typed denial | explicit deny (a typed value, never an absent field) |
| loud-not-silent | a plain sentence ("a verdict is always emitted, so nothing can fail silently") |
| house law | "the library's own rules" |

"Membrane" and "loud-not-silent" were gone from rule text by November. "Typed denial" survived twice in hyphenated form in the run-contract pattern, as finding SAI-34 said, and one "house law" remained as the quoted title of an older review finding. Seven more uses of "loud-not-silent" and "typed denial" sat in two contract schema descriptions. All ten are replaced in the change that executes this ADR.

### D2. Kept, each defined once

| Term | Decision | Why |
| --- | --- | --- |
| estate | Keep | Ordinary British IT usage for everything one organisation runs, and the name of the `tooling/estates/` layer. "Organisation" is the legal entity and "environment" is one runtime; neither carries the meaning. |
| estate-governed | Keep and define | It is the scope of rules (Context, fact 2). Replacing 26 uses, one of them inside a hashed priming block, costs more than defining one term. |
| enactment | Keep and define | It names one of the five duties in Core Proposition 2, and no standard term carries the distinction (Context, fact 1). This reverses the draft. |
| materiality | Keep as the single name | Used wherever the library means how much is at stake. "Impact" is not introduced as a second name. This reverses the draft's "impact elsewhere". |
| candidate, change candidate | Keep | Names a change before it is merged, which "change" does not. [ADR 0043](0043-replace-agent-coauthorship-disclosure-with-a-method-record.md), the run-contract pattern, and Core Proposition 5 depend on it. |
| governed execution | Keep | Defined pair with "run contract". There is no standard term for an execution that has a run contract. |
| mandate | Keep | The noun stays; only its compound goes (D4). |
| run contract, verifier pack | Keep | Coinages for new objects. The assessment agrees. |

Definitions land as follows.

- **Estate-governed** is defined in the normative-language pattern §3, and the glossary derives from it. Wording accepted by the operator on 2026-11-18: *a delivery path, workload, or system is estate-governed when the adopting organisation's shared controls apply to it: its shared repositories, pipelines, and environments, and the identities that act in them. It need not be production. The contrast is local single-user work.*
- **Enactment** gains a glossary entry that restates Core Proposition 2: carrying out an authorised change against its target under an identity scoped to that action, as distinct from producing the change, running delegated work, and authorising it.
- **Materiality**: the glossary entry, now headed "Materiality (AI)", is widened to the general sense and points to its owners, [ai-ml-systems.md](../../doctrine/principles/ai-ml-systems.md) §2.1 for the AI tier table and the normative-language pattern §3 for the applicability dimensions. The applicability table keeps its row label.
- **Candidate** gains a glossary entry. It has none.
- **Estate**: the glossary entry describes only the `tooling/estates/` sense. It gains the general sense used in rule text: the systems, pipelines, and environments one adopting organisation runs, and that organisation as the party that sets local choices.

### D3. Compounds of "estate"

Seventy-nine compound uses stood in the umbrella, principles, patterns, checklists, implementation references, tooling, skills, glossary, TL;DR, semantic index, and doctrine README when this was measured. They fall into six groups.

| Compound | Uses | Decision |
| --- | --- | --- |
| estate-governed | 26 | Keep and define (D2) |
| estate-policy | 12 | Keep: it is a literal value in the skill schema, and every use refers to that value |
| estate-only | 5 | Keep: it is the name of a change class in the versioning pattern |
| estate-specific, estate-level, estate-wide | 14 | Keep: ordinary adjectives of a kept noun |
| estate-defined, estate-set, estate-tunable, estate-approved, estate-evaluated, estate-bound, estate-adaptable | 19 | Replace with "set by the adopting organisation" or the plain equivalent in context |
| estate-health, estate-stub | 3 | Leave: an example identifier and one line of sweep history |

The fifth row is the dialect: seven forms for one idea, that the adopting organisation decides a value. None of the 19 uses is inside a hashed priming block, so no skill is re-hashed. One more use of "estate-defined" sat in a contract schema description and is replaced with them.

Contract schemas, their examples, and the reference index were not part of the count. They carry four other forms, 13 uses in all: an example path `estate-evidence/`, and estate-selected, estate-qualified, and estate-owned. This ADR does not decide them.

### D4. Retired with the lifecycle rewrite

| Term | Uses | Replacement |
| --- | --- | --- |
| mandate class | 9 in 3 files | type of work |
| closure mode | 3 in 2 files | kind of closure |
| record families | 3 in 2 files | record types |

All three belong to the AI-native lifecycle pattern and the files that cite it. They change when that pattern is rewritten under its own ADR, so consumers get one migration. Until then they stay. The draft's "work-order class" is dropped because it is itself a coinage.

### D5. Not decided here

"ISC" appears once in a principle and on twenty lines of the agent-loop pattern, with no glossary entry. Finding SAI-21 asks to replace it. It is an attributed external term, not a library coinage, so it is left to that finding.

## Control Cost And Lifecycle

- D1 to D3 are one editorial batch: one definition, five glossary entries, 20 compound replacements, nine replacements of D1 terms, and one reworded quotation. No rule changes strength or scope: the accepted definition of "estate-governed" follows how the rules already use it.
- D4 costs nothing until the lifecycle rewrite, and then rides with it.
- The kept list is short enough to check by search. A new compound of "estate" or a new coinage is a finding at the next lifecycle sweep.

## Alternatives Considered

**Replace "estate" wholesale with "organisation".** Rejected. It loses the layer name, breaks the `tooling/estates/` path and every profile keyed on it, and substitutes a narrower word.

**Replace "estate-governed", as the draft proposed.** Rejected on re-measurement. It would re-hash a skill and rewrite the scope line of eight rules, to remove a term that only lacks a definition.

**Replace every compound.** Rejected. It would also rename a change class, a schema value, and a principle heading.

**Keep "estate-defined" as the one compound for local choices.** Workable: it already has eight uses. Rejected in favour of the plain phrase, because a second defined compound is one more term to learn. The operator can reverse this by choosing the compound.

**Retire "enactment", as the draft proposed.** Rejected. Both proposed replacements collide with duties the umbrella names separately.

**Keep everything and improve the glossary.** Rejected for the four single-file coinages in D1 and the seven forms in D3. Accepted for the kept terms, whose glossary entries are the fix.

## Consumer Impact And Migration

**Change class:** editorial for D1 and D3; clarification for the definitions in D2; normative replacement for D4 when it is executed.

- No rule changes strength. If applying the definition of "estate-governed" narrows or widens any rule's reach, that rule's owner records it as a normative change in the same batch.
- Consumers who cite "estate-defined" or one of its six siblings in their own text need no change; the phrases are not identifiers.
- The schema value `estate-policy` and the change class `estate-only` are unchanged.

## Acceptance Criteria

Batch A, the first executing change:

- "Estate-governed" is defined in the normative-language pattern §3, in the wording of D2.
- The glossary has entries for estate, estate-governed, materiality, candidate, governed execution, enactment, run contract, and verifier pack. Each states the distinction the term carries.
- A search for the seven forms in D3's fifth row returns nothing in the umbrella, principles, patterns, checklists, implementation references, tooling, skills, glossary, or indexes. ADRs and evolution notes are records and are not edited.
- A search for the four D1 terms, in spaced or hyphenated form, returns nothing in the same set or in the contract schemas.
- The skills validator reports every priming hash unchanged.

Batch B, with the lifecycle rewrite:

- A search for the three D4 terms returns nothing in the same set, and the two glossary entries that define them are removed or renamed.

## Residual Risk

- The definition of "estate-governed" was inferred from how eight rules use the term and accepted as drafted. If a rule turns out to need a narrower or wider reach, its owner changes it as a normative change.
- D4 depends on an ADR that does not yet exist. If the lifecycle rewrite stalls, three terms this ADR calls retired stay in rule text.
- "Materiality" keeps two owners in practice, the AI tier table and the applicability dimensions. This ADR names one word for both and does not merge them.
- The amendment was drafted by a model. The September draft's review note still applies: the operator can revert any D1 replacement in a line.
