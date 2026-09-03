# ADR 0046: Retire Private Vocabulary Where A Standard Term Exists

- **Status:** Proposed
- **Decision date:** —
- **Recorded date:** 2026-09-03
- **Retrospective:** No
- **Responds to:** the 2026-09-03 cold-truth assessment, fix 2

## Context

The assessment counted the library's private coinages and found them pervasive: "estate" in 46 normative files (206 uses), "materiality" in 18 (74), "candidate" in 15 (81), "governed execution" in 9 (21), "enactment" in 5 (17), "mandate class" in 3 (9), plus single-file terms ("membrane", "typed denial", "loud-not-silent", "house law", "closure mode", "record families"). Its charge is that a reader must learn a dialect before the rules become readable, and that novel words where standard ones exist are a machine-drafting tell. The charge is partly right. It is also partly wrong, and this ADR separates the two so the owner can decide term by term rather than accept or reject a slogan.

The test applied to each term: **does a standard term exist that carries the same distinction?** If yes, the coinage is retired. If the coinage names a distinction the library actually depends on and no standard term carries it, the coinage stays, is defined once in the glossary, and is used consistently.

## Proposed Decision

### Retired now (editorial, executed with this batch)

| Term | Uses | Replacement | Why |
| --- | --- | --- | --- |
| membrane | 2 | boundary | Metaphor for a thing the same sentence already calls the authority boundary. |
| typed denial | 1 | explicit deny (a typed value, never an absent field) | The phrase was shorthand for a schema property; the long form is clearer. |
| loud-not-silent | 2 | plain sentence ("a verdict is always emitted, so nothing can fail silently") | Slogan standing in for a sentence. |
| house law | 2 | "the library's own rules" | Coinage for reflexivity; plain English says it. |

### Proposed for retirement (needs this ADR accepted; touches normative text)

| Term | Uses | Replacement | Notes |
| --- | --- | --- | --- |
| enactment | 17 in 5 files | deployment, or execution, by context | The AI-native SDLC uses it as a gate name. Renaming the gate is a normative-replacement edit to that pattern and should ride with [ADR 0047](0047-separate-maintainer-doctrine-and-collapse-the-ai-native-sdlc.md). |
| mandate class | 9 in 3 files | change intent, or work-order class | Same file family as enactment; same vehicle. |
| closure mode, record families | 5 in 3 files | outcome of closure; artefact types | Same vehicle. |

### Kept, with rationale

| Term | Uses | Decision | Why |
| --- | --- | --- | --- |
| estate | 206 | Keep; define once; stop compounding | Ordinary British IT usage for an organisation's whole set of systems, and the term that names the `tooling/estates/` layer. "Organisation" is the legal entity; "environment" is one runtime; neither carries "everything this organisation runs". The compounds ("estate-governed", "estate-evaluated") are the readability tax and are replaced by "in governed delivery paths" and "evaluated by the adopting organisation" where they occur (11 uses). |
| materiality | 74 | Keep where the SR 11-7 sense is meant; "impact" elsewhere | The AI-governance layer borrows the term from model-risk regulation deliberately and cites it. Outside that layer the word is used loosely and "impact" or "blast radius" reads better; those uses are identified in the sweep that executes this ADR. |
| candidate, change candidate | 81 | Keep | Names a change before it is merged, which "change" does not. [ADR 0043](0043-replace-agent-coauthorship-disclosure-with-a-method-record.md) and the run-contract pattern depend on the distinction. |
| governed execution | 21 | Keep | Defined pair with "run contract"; there is no standard term for "an execution that has a run contract". |
| run contract, verifier pack | — | Keep | Genuine coinages for genuinely new objects; the assessment agrees. |

## Alternatives Considered

**Replace "estate" wholesale with "organisation".** Rejected. It loses the layer name, breaks the `tooling/estates/` path and every profile that keys on it, and substitutes a narrower word. The tax is in the compounds, not the noun.

**Keep everything and improve the glossary.** Rejected for the four single-file coinages: a glossary entry for a word used twice is the wrong fix. Accepted in spirit for the kept terms, whose glossary entries are the fix.

**Do it all in one editorial sweep.** Rejected. Renaming a gate in a normative pattern changes what consumers cite; it is a normative replacement and needs its own migration note.

## Consequences

- Four terms disappear from normative text with no change in meaning.
- The kept terms become a deliberate, short list a reader can learn from the glossary in one sitting, rather than an open-ended dialect.
- The SDLC-family terms wait for ADR 0047 so that consumers get one migration, not two.

## Consumer Impact

**Change class:** editorial for the retired-now table; normative replacement for the proposed table when executed; navigation for the compound "estate-" replacements.

## Acceptance Evidence (when accepted)

- Grep for each retired term returns zero hits in principles, patterns, checklists, and the umbrella.
- Glossary entries for estate, materiality, candidate, governed execution, run contract, and verifier pack each state the distinction the term carries and name the nearest standard term it was chosen over.

## Review Note

Drafted by an agent under the owner's direction; not yet reviewed by the owner. The retired-now table was executed as editorial work because the four replacements are plain restatements; the owner can revert any of them in a line.
