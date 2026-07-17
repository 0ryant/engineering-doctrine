# Engineering Doctrine

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

Reusable engineering doctrine that separates stable principles from replaceable tooling.

This repository is intended to be a reference library for teams building applications, automation, CLIs, APIs, and infrastructure. The goal is to keep the operating model durable while allowing implementation details to evolve over time.

## License

This repository is licensed under **Apache-2.0** (see [LICENSE](LICENSE)). You may use, copy, adapt, and redistribute the text and code subject to the licence's notice and attribution conditions. This is not legal advice; confirm with your counsel for regulated or commercial deployments.

**Why Apache-2.0:** Engineering Doctrine is an adoption-first reference library intended to be copied, forked, vendored, and adapted into internal and commercial engineering systems. Apache-2.0 keeps that path permissive and supplies an explicit patent grant without requiring downstream modifications to be published.

**Licence history:** `v0.1.0` and earlier were released under Apache-2.0. The default branch was offered under AGPL-3.0-or-later from commit `5f6d783` until the adoption-first decision recorded in [ADR 0025](docs/adr/0025-restore-apache-2.0-as-project-license.md). Effective 2026-07-17, the copyright holder also offers the repository material published during that interval under Apache-2.0. Existing AGPL grants remain valid; recipients may use that material under either applicable grant.

## Project governance (public trust)

For contribution workflow, **security reporting**, **maintainer and review** expectations, and **release tagging** (not calendar hype—when consumers should look at a version), see:

- [CONTRIBUTING.md](CONTRIBUTING.md) — how to propose changes, PR hygiene, and where content belongs
- [SECURITY.md](SECURITY.md) — what to report privately vs in issues
- [GOVERNANCE.md](GOVERNANCE.md) — maintainers, review policy, and release cadence
- [CHANGELOG.md](CHANGELOG.md) — version history aligned with **SemVer-shaped tags** (see [doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md](doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md))
- [AGENTS.md](AGENTS.md) — instructions for **AI / agent** contributors editing this library; links the **harness** for substantive changes
- [doctrine/SEMANTIC_INDEX.md](doctrine/SEMANTIC_INDEX.md) — semantic route map for humans and agents; links task intent to the source doctrine files to ingest

## Structure

- `ENGINEERING.md` is the umbrella engineering guide.
- `doctrine/principles/` contains **timeless**, platform-agnostic rules (collaboration, trunk, operational rigour, versioning, contracts, runtime **trade-offs**, interoperability posture). See `doctrine/principles/timeless-principles-and-tooling.md`.
- `doctrine/tooling/` contains **illustrative** implementation examples (build stack, CloudEvents baseline, Git host settings—swap freely). `doctrine/tooling/estates/` holds **optional** vendor-specific supplements.
- `doctrine/patterns/` shows how build and delivery surfaces fit together (including trunk workflow).
- `doctrine/checklists/` turns the doctrine into reviewable execution (build, collaboration, platform/SRE, release, and doctrine edits).
- `doctrine/evolution/` holds audit notes (for example MoSCoW reviews).
- `doctrine/SEMANTIC_INDEX.md` maps task intent to the highest-value doctrine files for humans and agents.
- `doctrine/REFERENCES.md` indexes authoritative external sources; each principle file documents rationale and citations.
- `docs/adr/` records decisions about this doctrine library itself. Retrospective ADRs must include both the original decision date and the date they were recorded.
- `scripts/generate-doctrine-sitemap.sh` regenerates `doctrine/SITEMAP.md` (all Markdown paths under `doctrine/`).

## How To Use This Repo

1. Adopt the principles first.
2. Tailor the tooling to your current estate and platform constraints.
3. Use the patterns to shape repository structure and delivery surfaces.
4. Use the checklists during rollout, review, and template updates.
5. For **team rollout**, start with `doctrine/patterns/adoption-playbook.md` and optionally `doctrine/tooling/estates/minimum-viable-doctrine.template.md` instead of handing new stakeholders the full tree.
6. For decisions about this library, use `docs/adr/` so structural changes are visible without relying on git history alone.

Principles should move slowly. Tooling should change when the stack, platform, or team context changes.
