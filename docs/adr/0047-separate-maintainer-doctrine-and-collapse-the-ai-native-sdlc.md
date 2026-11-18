# ADR 0047: Separate Maintainer Doctrine From The Consumer Path

- **Status:** Accepted
- **Decision date:** 2026-11-18
- **Recorded date:** 2026-09-03; amended 2026-11-18
- **Retrospective:** No
- **Deciders:** Repository operator
- **Review provenance:** Operator-accepted on 2026-11-18 as amended; drafted by a model on 2026-09-03 and amended by a model on 2026-11-18 at the operator's direction, after the structure was re-measured; no independent human or domain review recorded
- **Responds to:** the 2026-09-03 cold-truth assessment, fix 5; findings SAI-32, SAI-33, and SAI-41 in the [2026-11 review](../../doctrine/evolution/review-full-doctrine-2026-11.md)
- **Canonical owner:** none changes. Three patterns move directory and keep their content
- **Derived landings:** [ENGINEERING.md](../../ENGINEERING.md) (one clause in the layer sentence); [how-to-read-this-doctrine.md](../../doctrine/patterns/how-to-read-this-doctrine.md); [doctrine/README.md](../../doctrine/README.md); the sitemap and semantic index; the preflight script; two contract schema descriptions
- **Relationship to earlier decisions:** the September draft's decision 3, the collapse of the AI-native lifecycle pattern, is withdrawn from this ADR (D7). [ADR 0046](0046-retire-private-vocabulary-where-a-standard-term-exists.md) D4 waits for the ADR that replaces it

Accepted on 2026-11-18. D1 to D5 are executed in the change that records this acceptance. D6 applies from the next sweep.

The title was shortened on amendment. The file keeps its original name so existing links hold.

## Context

The assessment made two charges. Maintainer material sits in the path a consumer reads first, and the AI-native lifecycle pattern is too long for a senior reader to accept. Both are structure problems. Nothing in the maintainer patterns is wrong; it is in the wrong place.

### What changed between the draft and this amendment

The structure was measured again on 2026-11-18 at `04d474a`, by the same method at the commit before the draft (`cb073f2`) and today. Word counts split Markdown on whitespace.

| Measure | September | Now |
| --- | --- | --- |
| Rule text: principles, patterns, checklists | 94,996 words | 107,197 |
| The same with implementation references | 94,996 | 131,117 |
| Record text: ADRs and evolution notes | 114,755 | 175,072 |
| Record words per rule word | 1.21 | 1.63 (1.34 with implementation references) |
| AI-native lifecycle pattern | about 4,000 words, 18 sections | 4,094 words, 18 sections |

Four findings changed the draft.

1. **Two skills pin the register paths.** The navigation skill's hashed priming block names `doctrine/DEPRECATED.md` and the citation skill's names `doctrine/EVIDENCE-EXCEPTIONS.md`. Moving the registers forces two re-hashes and a re-pin by every host that pins skills by hash. Consumers and agents are also told to check the deprecation register, so it is consumer material.
2. **The versioning split moves very little.** The draft assigned §§1–5 to consumers and §§4 and 8 to maintainers, which puts §4 in both halves and §§6–7 in neither. The maintainer half is 239 words of 1,289. A split and a rename would touch 28 files to relocate it.
3. **The draft gave the new directory no standing.** The navigation skill tells an agent to take authority only from the umbrella, principles, and patterns. The draft did not say what a file under `maintainers/` is.
4. **The lifecycle collapse would move rules into a note.** Three sections the draft sent to an evolution note hold rules: transition admissibility (§9), the authority duty table (§10), and the rule in §13 that an agent cannot detect, implement, approve, and deploy its own change as one closed authority loop. The umbrella says research under `doctrine/evolution/` "is evidence and history, not adopted doctrine by itself". Three files cite §10 as an owner. The review reached the same view independently in finding SAI-32.

## Decision

### D1. A `doctrine/maintainers/` directory holds three patterns

- [doctrine-content-lifecycle.md](../../doctrine/maintainers/doctrine-content-lifecycle.md)
- [source-authority-and-evidence-grading.md](../../doctrine/maintainers/source-authority-and-evidence-grading.md)
- [doctrine-library-change-harness.md](../../doctrine/maintainers/doctrine-library-change-harness.md)

Files move with their history. A short README in the directory is its landing page. Every link in a live file is repointed in the same change, along with the preflight script, the two schema descriptions that name the lifecycle pattern's path, `AGENTS.md`, `CONTRIBUTING.md`, `GOVERNANCE.md`, and the two skills that cite these patterns outside their priming blocks. The doctrine README's "Start Here" and the reading guide gain one sentence: "If you maintain this library rather than consume it, start at `maintainers/`."

### D2. The moved files remain patterns

Their applicability condition is that you are changing this library. They bind the people and agents who do that and nobody else. The operator accepted this standing on 2026-11-18. The umbrella's layer sentence and the reading guide say so, and the executing change shows the exact clause. The tool contract's layer list is unchanged. No priming block is edited: an agent consuming the library takes no authority from the directory, which is the intended result.

Two path rules inside the library learn what a tool server must. The skills validator and the navigation verifier pack's authority check now count a path under `doctrine/maintainers/` as a pattern, so a skill governed by a moved pattern still validates and a citation that passed before the move still passes. The pack takes a patch version.

### D3. The two registers stay where they are

[DEPRECATED.md](../../doctrine/DEPRECATED.md) and [EVIDENCE-EXCEPTIONS.md](../../doctrine/EVIDENCE-EXCEPTIONS.md) stay at the `doctrine/` root (Context, finding 1). This reverses the draft.

### D4. The versioning pattern stays in the consumer path under its name

[doctrine-versioning-and-consumer-compatibility.md](../../doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md) is not split or renamed. Its two maintainer sections, §4 (release notes minimum) and §8 (maintainer checklist), move into the change harness as new sections after its existing ones. In the versioning pattern §4 and §8 keep their numbers and become one-line pointers, so no section in either file is renumbered. This replaces the draft's decision 2.

### D5. Old paths redirect, then retire on the ordinary clock

A one-line redirect stub stays at each of the three old paths. Each stub enters the deprecation register and exits under the lifecycle's ordinary clock. Its exit state is Superseded: the lifecycle pattern §5 forbids hard deletion, so the path then stays as a tombstone that points forward. ADRs, evolution notes, and the changelog are records: they keep their old links, which resolve through the stub and then the tombstone.

This paragraph was corrected when the ADR was executed. The accepted text had the stubs removed and the record links repointed at that point, which the lifecycle pattern does not allow.

### D6. The word ratio is published each sweep

Each sweep record reports rule words (principles, patterns, and checklists, with and without implementation references) against record and maintainer words (ADRs, evolution notes, and `maintainers/`). No threshold is set. The Context table is the first reading, taken before the move.

### D7. The lifecycle collapse is withdrawn from this ADR

The draft's decision 3 does not proceed here. It needs its own ADR, with a collapsed draft the operator has read, as the September review note already required. That ADR has to answer what this one could not:

- **Which sections hold rules and stay.** The review names §3, §5, §9, and one bullet of §13. Section 10 is cited as an owner by three files.
- **Where ten citations go.** Every section citation of the pattern from a live file points at least partly at a section the draft's keep-list left out (§§4, 7, 10, 13, 16).
- **Whether its statements become typed.** The pattern contains no MUST, SHOULD, or MAY.
- **Whether routine change gets a floor.** Finding SAI-33 asks for one, and Core Proposition 10 says "Incidental assistance remains lightweight". A floor loosens the pattern, so it is the operator's decision.
- **Its size.** The sections on the draft's keep-list total 1,658 words today. With §§9, 10, and 13 the total is about 2,200.
- **Its order.** The open review decisions on agent authority (AI-02, AI-04, AI-05, AI-14) would rewrite §10. Collapsing first means editing it twice.

## Control Cost And Lifecycle

- 33 live files and 34 record files reference the three patterns. The live files change once; the record files do not change.
- Three stubs join the deprecation register and are swept like any other entry.
- D6 adds one line to each sweep record.
- No skill is re-hashed and no contract enum changes. The navigation verifier pack takes a patch version (1.0.3).

## Alternatives Considered

**Leave the structure and improve the README's reading order.** Rejected. The harness sits under "Start Here" today, and search and the semantic index do not respect reading order.

**Delete the maintainer patterns.** Rejected. They are the reason the library can retire content at all, and two sweeps have now exercised them.

**Move the registers too, as the draft proposed.** Rejected (Context, finding 1).

**Split and rename the versioning pattern, as the draft proposed.** Rejected (Context, finding 2).

**Move the maintainer-only change checklist as well.** Not done. Checklists are a derived layer with their own directory, the file's title already marks its audience, and a second kind of file in `maintainers/` blurs what the directory holds.

**Collapse the lifecycle pattern here.** Withdrawn (D7).

## Consumer Impact And Migration

**Change class:** navigation for D1, D3, D4, and D5; clarification for D2; maintainer tooling for D6.

- No rule changes. Consumer-visible patterns drop from 33 to 30, and 7,379 words leave the pattern list.
- Links to the three old paths keep resolving, through the stub and then through its tombstone.
- A retrieval server that derives an entry's layer from its path needs one rule: files under `doctrine/maintainers/` are patterns.
- Hosts that pin verifier packs by version move to navigation pack 1.0.3.
- Citations of the versioning pattern by section number are unaffected.

## Acceptance Criteria

- `doctrine/maintainers/` holds the three patterns and a README, and each file's history follows it.
- A search for the three old paths returns only the stubs, the deprecation register, the sitemap, ADRs, evolution notes, and the changelog.
- The preflight script passes from the new harness path, and the Markdown link check passes.
- The skills validator reports every priming hash unchanged.
- The versioning pattern's §4 and §8 are pointers, the harness holds their text, and no section in either file is renumbered.
- The deprecation register lists the three stubs.
- The umbrella and the reading guide state the directory's standing as D2 gives it.
- The next sweep record carries the word ratio.

## Residual Risk

- The lifecycle pattern stays at 4,094 words until its own ADR lands. Findings SAI-32 and SAI-33 stay open.
- Finding SAI-41 asks to move the agent-consumption pattern, the skills register, and the contract schemas as well. That is not decided here.
- The maintainer-only change checklist stays in the checklist list a consumer sees.
- The navigation skill's priming block still names only `doctrine/principles/` and `doctrine/patterns/` as authority. It was left alone to avoid a re-hash, so its wording and its pack's check now differ for maintainer patterns.
- The ratio in D6 will read worse after this change: 7,379 words move from the rule side to the maintainer side.
- The amendment was drafted by a model and changes three of the draft's four decisions. No independent review is recorded.
