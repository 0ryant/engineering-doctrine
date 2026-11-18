# OWASP LLM Top 10 2026 Edition: Identifier Adoption

Date and source access date: 2026-11-18. Repository basis: `8b518c9` and the companion change.
Status: research basis for [ADR 0056](../../docs/adr/0056-cite-the-owasp-llm-top-10-2026-edition.md) (accepted 2026-11-18). Model research and model review; no independent human or domain review.

## Question

The [latest-developments note](research-latest-developments-2026-11.md) suffixed the library's OWASP LLM identifiers with `:2025` and deferred adoption of the 2026 edition until its text had been read. What does the 2026 edition change, and should the library cite it?

## Source Ledger

Classes follow [Source Authority And Evidence Grading](../patterns/source-authority-and-evidence-grading.md) §2. A delegated agent downloaded the PDF from the OWASP landing page and extracted its text; the lead author re-read the table of contents, the "What's New" section, and the entry 8 description in that extraction, and read the landing page live. No archive copy was captured.

| Source | Class and scope | Supports | Does not establish |
| --- | --- | --- | --- |
| [OWASP GenAI LLM Top 10 2026 landing page](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) | S4 awareness document, publisher page | The edition exists and the page dates it 2026-08-03 | Entry names; the page only links the download |
| OWASP Top 10 for LLM Applications 2026, "Version 2026" PDF (122 pages; served from the landing page as `OWASP-GenAI-LLM-Top-10-2026-v1.0.pdf`; CC BY-SA 4.0) | S4 awareness document | The ten entries and identifiers below; that no entry is new or merged; the rename of entry 7 to Hidden Context Exposure; scope growth in several entries; the boundary with the agentic list | Prevalence or severity as measured fact. An awareness list supports risk salience only |
| [OWASP rolling list page](https://genai.owasp.org/llm-top-10/) and the [OWASP Foundation project page](https://owasp.org/www-project-top-10-for-large-language-model-applications/) (read by the delegated agent) | S4, publisher pages | Both still present the 2025 edition on the access date | That the 2026 edition is withdrawn or provisional; neither page says so |

Document condition: the PDF cover reads "August 4th, 2026" over an unfilled date placeholder, and its revision history still shows a placeholder for the 2026 release date. The landing page says 3 August. The library cites the landing page date and records the discrepancy here.

## What Changed

The document says it added no categories: newer risks were folded into existing entries. The order moved, and one entry was renamed and widened.

| 2025 edition | 2026 edition | Basis |
| --- | --- | --- |
| LLM01:2025 Prompt Injection | LLM01:2026 Prompt Injection | Stated in the text; scope now includes cross-modal injection |
| LLM02:2025 Sensitive Information Disclosure | LLM02:2026 Sensitive Information Disclosure | Stated in the text |
| LLM03:2025 Supply Chain | LLM04:2026 Supply Chain | Same title in both lists |
| LLM04:2025 Data and Model Poisoning | LLM05:2026 Data and Model Poisoning | Same title in both lists |
| LLM05:2025 Improper Output Handling | LLM10:2026 Improper Output Handling | Stated in the text ("from fifth to tenth"); scope now includes insecure generated code |
| LLM06:2025 Excessive Agency | LLM03:2026 Excessive Agency | Stated in the text |
| LLM07:2025 System Prompt Leakage | LLM08:2026 Hidden Context Exposure | Stated in the text as a rename and wider scope: system prompt, developer instructions, retrieved policy text, and tool schemas placed in the model's context |
| LLM08:2025 Vector and Embedding Weaknesses | LLM09:2026 Vector and Embedding Weaknesses | Same title in both lists |
| LLM09:2025 Misinformation | LLM07:2026 Misinformation | Same title in both lists |
| LLM10:2025 Unbounded Consumption | LLM06:2026 Unbounded Consumption | Stated in the text |

Eight of ten numbers changed. The same number now names a different risk in several places: LLM05 is Improper Output Handling in 2025 and Data and Model Poisoning in 2026. A bare `LLM05` is ambiguous in either direction, so the year suffix has to stay on every identifier.

## Library Use Today

The library cites four identifiers in two files: `LLM01`, `LLM02`, `LLM05`, and `LLM07`, all suffixed `:2025`, in the [AI adoption controls](../patterns/ai-adoption-controls.md) §3 test matrix and [AI and ML-assisted systems](../principles/ai-ml-systems.md) §6. Edition statements sit in those two files, the [glossary](../glossary.md), the [RAG retrieval baseline](../patterns/rag-retrieval-baseline.md) references, and [REFERENCES](../REFERENCES.md). No control depends on an entry's rank.

Two observations that do not need a change:

- The [agentic crosswalk](../patterns/agentic-loop-design.md) §11 says the agentic list cross-maps to the 2025 LLM list. That remains a true statement about that document.
- The 2026 text treats jailbreaking as a subset of prompt injection. The library's test matrix keeps a separate jailbreak row because the test differs; the row cites no identifier, so nothing conflicts.

## Synthesis

1. **The mapping is one-to-one.** Every identifier the library uses has exactly one successor, so citing the new edition changes labels, not controls.
2. **Wider scope lands on existing controls.** Insecure generated code is already treated as untrusted output by the library's review and output-validation rules; hidden context beyond the system prompt is already covered by the rule that context is not a security boundary. Neither widening needs a new obligation.
3. **Dual citation costs one clause per use.** Naming the prior identifier beside the new one lets a reader working from either edition follow the reference.
4. **The publisher's own pages lag.** Citing the 2026 edition while the rolling page shows 2025 is defensible because the edition is published on the publisher's site under its own version label, but it should carry a review trigger.

## Decision Input

Cite the 2026 edition; keep the year suffix mandatory; name the 2025 identifier beside each renumbered one; keep the 2025 edition in the references as the prior edition; add no control. Change class: editorial and citation.

## Residual Risk

The entry mapping for four rows rests on identical titles and the document's rank-migration figure, which is an image. The PDF has unfilled date placeholders and may be reissued. The rolling page will change edition without notice, so unnumbered links to it will silently move. Model review only.
