# Engineering Doctrine

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

Reusable engineering doctrine that separates stable principles from replaceable tooling.

This repository is intended to be a reference library for teams building applications, automation, CLIs, APIs, and infrastructure. The goal is to keep the operating model durable while allowing implementation details to evolve over time.

## License

The default license for this repository is **Apache-2.0** (see [LICENSE](LICENSE)). You may use, copy, and adapt the text for your own handbooks, templates, and internal policy **subject to the license** (attribution, NOTICE if you redistribute derivative works, etc.). This is not legal advice; confirm with your counsel for regulated environments.

**Why Apache-2.0:** It is a permissive, widely understood license for mixed documentation and code (including the scripts in this repo) and is familiar to many enterprises.

## Project governance (public trust)

For contribution workflow, **security reporting**, **maintainer and review** expectations, and **release tagging** (not calendar hype—when consumers should look at a version), see:

- [CONTRIBUTING.md](CONTRIBUTING.md) — how to propose changes, PR hygiene, and where content belongs
- [SECURITY.md](SECURITY.md) — what to report privately vs in issues
- [GOVERNANCE.md](GOVERNANCE.md) — maintainers, review policy, and release cadence

## Structure

- `ENGINEERING.md` is the umbrella engineering guide.
- `doctrine/principles/` contains **timeless**, platform-agnostic rules (collaboration, trunk, operational rigour, versioning, contracts, runtime **trade-offs**, interoperability posture). See `doctrine/principles/timeless-principles-and-tooling.md`.
- `doctrine/tooling/` contains **illustrative** implementation examples (build stack, CloudEvents baseline, Git host settings—swap freely). `doctrine/tooling/estates/` holds **optional** vendor-specific supplements.
- `doctrine/patterns/` shows how build and delivery surfaces fit together (including trunk workflow).
- `doctrine/checklists/` turns the doctrine into reviewable execution (build, collaboration, platform/SRE, release, and doctrine edits).
- `doctrine/evolution/` holds audit notes (for example MoSCoW reviews).
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
