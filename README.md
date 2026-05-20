# Engineering Doctrine

[![License: AGPL-3.0-or-later](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](LICENSE)

Reusable engineering doctrine that separates stable principles from replaceable tooling.

This repository is intended to be a reference library for teams building applications, automation, CLIs, APIs, and infrastructure. The goal is to keep the operating model durable while allowing implementation details to evolve over time.

## License

This repository is licensed under **AGPL-3.0-or-later** (see [LICENSE](LICENSE)). You may use, copy, adapt, and redistribute the text and code **subject to the license** — including the AGPL network-use / source-disclosure obligations if you make a modified version available to users over a network. This is not legal advice; confirm with your counsel for regulated or commercial deployments.

**Why AGPL-3.0-or-later:** Engineering Doctrine is the OSS wedge of a larger ecosystem (see council D6 / `release-surfaces/public-vs-gated.md`). AGPL keeps the doctrine genuinely open and copyleft-protected: improvements made by downstream redistributors stay accessible to the community, while permissive embed in proprietary stacks requires a separate commercial arrangement.

**Pre-v0.2.0 caveat:** Versions of this repository tagged before `v0.2.0` were released under their original license (Apache-2.0; preserved as [LICENSE.old](LICENSE.old)). The AGPL-3.0-or-later relicense applies from `v0.2.0` forward. Pre-relicense versions remain available under their original terms.

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
