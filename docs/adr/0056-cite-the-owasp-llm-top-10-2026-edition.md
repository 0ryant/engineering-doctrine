# ADR 0056: Cite The OWASP LLM Top 10 2026 Edition

- **Status:** Accepted
- **Decision date:** 2026-11-18
- **Recorded date:** 2026-11-18
- **Retrospective:** No
- **Deciders:** Repository operator
- **Review provenance:** Operator-directed and operator-accepted on 2026-11-18; drafted and reviewed by a model, no independent human or domain review recorded
- **Research:** [OWASP LLM Top 10 2026 edition: identifier adoption](../../doctrine/evolution/research-owasp-llm-top-10-2026-adoption-2026-11.md); finding 6 in the [latest-developments note](../../doctrine/evolution/research-latest-developments-2026-11.md)
- **Canonical owner:** [AI And ML-Assisted Systems](../../doctrine/principles/ai-ml-systems.md) §6 (edition statement)
- **Derived landings:** [AI Adoption Controls](../../doctrine/patterns/ai-adoption-controls.md) §3; [RAG Retrieval Baseline](../../doctrine/patterns/rag-retrieval-baseline.md) references; [glossary](../../doctrine/glossary.md); [REFERENCES](../../doctrine/REFERENCES.md)

## Context

OWASP published a 2026 edition of its Top 10 for LLM Applications on 2026-08-03. It adds no categories, renames one entry, and renumbers eight. The library cites four identifiers from the 2025 edition and had deferred adoption until the 2026 text was read. It has now been read.

## Decision

1. The library cites the **2026 edition** as its LLM application-layer risk list.
2. Every identifier carries its edition year (`LLM10:2026`). A bare identifier is a defect, because the same number names different risks across editions.
3. Where an identifier was renumbered, the first use in a file names the 2025 identifier beside it.
4. The 2025 edition stays in the references as the prior edition.
5. No control, strength, applicability rule, or exception path changes. The list remains an awareness source that supports risk salience, not an obligation.

Mapping for the identifiers the library uses:

| 2025 | 2026 |
| --- | --- |
| LLM01:2025 Prompt Injection | LLM01:2026 Prompt Injection |
| LLM02:2025 Sensitive Information Disclosure | LLM02:2026 Sensitive Information Disclosure |
| LLM05:2025 Improper Output Handling | LLM10:2026 Improper Output Handling |
| LLM07:2025 System Prompt Leakage | LLM08:2026 Hidden Context Exposure |

The full ten-row mapping is in the research note.

## Control Cost And Lifecycle

No control is added. The cost is keeping citations current. Review triggers: OWASP reissues the 2026 PDF, its rolling list page moves to the 2026 edition, or a later edition is published.

## Alternatives Considered

- **Stay on the 2025 edition until the rolling page moves.** A reasonable choice, since OWASP's rolling page and Foundation project page still present 2025. Not taken because the 2026 edition is published on the publisher's site under its own version label, the mapping is one-to-one, and dual citation keeps 2025 readers oriented.
- **Cite both editions with equal weight.** Rejected; two current identifiers per risk invites the ambiguity the year suffix exists to prevent.
- **Add controls for the widened entries.** Rejected; insecure generated code and hidden context are already covered by existing rules, and an awareness list does not ground a new obligation.

## Consumer Impact And Migration

Change class: **editorial and citation**. No consumer obligation changes. Consumers who map their own controls to OWASP identifiers can use the mapping table to update labels.

## Acceptance Criteria

- AI and ML-assisted systems §6 names the 2026 edition and the year-suffix rule.
- The AI adoption controls test matrix cites 2026 identifiers and names the 2025 ones where renumbered.
- The glossary, RAG baseline references, and REFERENCES name the 2026 edition and keep the 2025 edition as prior.
- No bare `LLM0x` identifier remains outside research notes.
- The ADR index lists this decision, and doctrine preflight passes.

## Residual Risk

The 2026 PDF has unfilled date placeholders and may be reissued. Four rows of the full mapping rest on identical titles and a figure. Unnumbered links to the rolling list page will change edition without notice. Model review only.
