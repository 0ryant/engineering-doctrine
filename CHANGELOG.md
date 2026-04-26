# Changelog

All notable changes to this **engineering doctrine** library are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) (human-readable history). This repository uses **SemVer-shaped tags** for the *doctrine* contract, not for npm/cargo units—see [doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md](doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md) for patch / minor / major meaning, change classes, and release note expectations.

## [Unreleased]

## [0.1.0] - 2026-04-27

First public SemVer-tagged release ([`v0.1.0`](https://github.com/0ryant/engineering-doctrine/releases/tag/v0.1.0)). **Change classes** (summary): *navigation* + *additive guidance* with some *normative* additions in new files; *compatibility* treated as **0.x minor** (review before pin upgrade).

### Added

- **Project meta:** [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), [GOVERNANCE.md](GOVERNANCE.md), [LICENSE](LICENSE) (Apache-2.0), [.gitignore](.gitignore) (excludes local `.cursor/` and `.DS_Store`).
- **ADRs** under [docs/adr/](docs/adr/) (0001–0007: library shape, trunk and CloudEvents defaults, layer split, navigation and glossary, AI/ML and agents, governance navigation, developer experience as a first-class concern).
- **Patterns:** [incident-lifecycle-and-on-call-operations.md](doctrine/patterns/incident-lifecycle-and-on-call-operations.md), [platform-as-product-and-golden-paths.md](doctrine/patterns/platform-as-product-and-golden-paths.md), [engineering-controls-governance-program.md](doctrine/patterns/engineering-controls-governance-program.md), [doctrine-versioning-and-consumer-compatibility.md](doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md).
- **Principles / tooling:** [developer-experience.md](doctrine/principles/developer-experience.md), [merge-path-evidence-and-pipeline-integrity.md](doctrine/principles/merge-path-evidence-and-pipeline-integrity.md), [merge-path-and-pipeline-control-suite.md](doctrine/tooling/merge-path-and-pipeline-control-suite.md).
- **Checklists:** [developer-experience-scorecard.md](doctrine/checklists/developer-experience-scorecard.md), [governance-program-readiness.md](doctrine/checklists/governance-program-readiness.md).
- **Evolution / research:** [public-doctrine-benchmark-gap-analysis-2026-04.md](doctrine/evolution/public-doctrine-benchmark-gap-analysis-2026-04.md), [anti-patterns-and-failure-modes-gap-analysis-2026-04.md](doctrine/evolution/anti-patterns-and-failure-modes-gap-analysis-2026-04.md).

### Changed

- **Umbrella and navigation:** [README.md](README.md), [ENGINEERING.md](ENGINEERING.md), [doctrine/README.md](doctrine/README.md), [doctrine/REFERENCES.md](doctrine/REFERENCES.md), [doctrine/SITEMAP.md](doctrine/SITEMAP.md), [doctrine/glossary.md](doctrine/glossary.md), and touch-ups across build/collaboration/doctrine checklists, adoption playbook, chaos, how-to-read, documentation-knowledge, measurement, reliability, tldr, and related evolution notes.
- **Default branch license:** the canonical license for this tree is **Apache-2.0** (see README). An earlier default-branch commit added a **MIT** `LICENSE`; that line of history is superseded for **current** consumers—do not assume MIT for the library as it ships from `main` at this tag.

### Consumer impact

- **All consumers:** pin imports to **`v0.1.0`** (or this commit) when you need a stable policy snapshot; re-read [GOVERNANCE.md](GOVERNANCE.md) and [CONTRIBUTING.md](CONTRIBUTING.md) for process and security reporting.
- **Teams adopting governance / incident / platform / DevEx guidance:** start from the new patterns and checklists above, then map local `.doctrine/` overrides.
- **Forks and subtree users:** if you had copied MIT-only language from a prior `main` tip, reconcile with Apache-2.0 before redistributing.

### Evidence

- Git: tag **`v0.1.0`**, commit on `main` at time of tag (see [diff since merge of prior `main` tip](https://github.com/0ryant/engineering-doctrine/compare/93c2516...v0.1.0) for the release changeset).
- In-repo: [docs/adr/](docs/adr/) and [doctrine/evolution/](doctrine/evolution/) cross-links above.
