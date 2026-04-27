# Agent instructions (engineering-doctrine)

This repository is the **canonical engineering-doctrine library** (Markdown principles, patterns, tooling, checklists). When a task **adds or substantially changes** `doctrine/`, `docs/adr/`, or the umbrella `ENGINEERING.md`, follow the **library change harness**:

- **Full procedure:** [doctrine/patterns/doctrine-library-change-harness.md](doctrine/patterns/doctrine-library-change-harness.md)
- **Checklist:** [doctrine/checklists/doctrine-change-checklist.md](doctrine/checklists/doctrine-change-checklist.md)
- **Preflight:** `./scripts/doctrine-change-preflight.sh` from the repo root

**Minimum bar for meaningful additions:** researched basis (citations and/or `doctrine/evolution/` note), an **ADR** (new or explicitly referenced), correct **layering** with **cross-links** between principle / pattern / tooling, and **navigation** updates (sitemap via script, `glossary.md`, `REFERENCES.md`, `doctrine/README.md` as appropriate). Use the **copy-paste prompt** in harness §7 for structured agent tasks.

**Not applicable:** drive-by rewrites, vendor pitches in `principles/`, or new normative “musts” without consumer-impact labelling. See [CONTRIBUTING.md](CONTRIBUTING.md) and [GOVERNANCE.md](GOVERNANCE.md).
