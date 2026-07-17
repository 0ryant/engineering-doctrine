# Agent instructions (engineering-doctrine)

This repository is the **canonical engineering-doctrine library** (Markdown principles, patterns, tooling, checklists). When a task **adds or substantially changes** `doctrine/`, `docs/adr/`, or the umbrella `ENGINEERING.md`, follow the **library change harness**:

- **Semantic index / ingestion map:** [doctrine/SEMANTIC_INDEX.md](doctrine/SEMANTIC_INDEX.md). Before substantive analysis or edits, read its **Critical Agent Context** and the matching **Task Route** so the right principle / pattern / tooling / checklist / ADR files are in context.
- **Full procedure:** [doctrine/patterns/doctrine-library-change-harness.md](doctrine/patterns/doctrine-library-change-harness.md)
- **Checklist:** [doctrine/checklists/doctrine-change-checklist.md](doctrine/checklists/doctrine-change-checklist.md)
- **Preflight:** `./scripts/doctrine-change-preflight.sh` from the repo root

**Minimum bar for meaningful additions:** researched basis (citations and/or `doctrine/evolution/` note), an **ADR** (new or explicitly referenced), correct **layering** with **cross-links** between principle / pattern / tooling, and **navigation** updates (sitemap via script, `glossary.md`, `REFERENCES.md`, `doctrine/README.md` as appropriate). Use the **copy-paste prompt** in harness §7 for structured agent tasks.

**Portability boundary:** do not name organisation-private products, portfolio
tools, internal repositories, or local programme artefacts anywhere in the
publishable library. Express the capability or control generically. External
standards and vendor material may be named only as cited grounding or clearly
optional illustration. Keep local work records under ignored `.local/` paths.

**Not applicable:** drive-by rewrites, vendor pitches in `principles/`, or new normative “musts” without consumer-impact labelling. See [CONTRIBUTING.md](CONTRIBUTING.md) and [GOVERNANCE.md](GOVERNANCE.md).
