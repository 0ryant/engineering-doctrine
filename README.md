# Engineering Doctrine

Reusable engineering doctrine that separates stable principles from replaceable tooling.

This repository is intended to be a reference library for teams building applications, automation, CLIs, APIs, and infrastructure. The goal is to keep the operating model durable while allowing implementation details to evolve over time.

## Structure

- `ENGINEERING.md` is the umbrella engineering guide.
- `doctrine/principles/` contains **timeless**, platform-agnostic rules (collaboration, trunk, operational rigour, versioning, contracts, runtime **trade-offs**, interoperability posture). See `doctrine/principles/timeless-principles-and-tooling.md`.
- `doctrine/tooling/` contains **illustrative** implementation examples (build stack, CloudEvents baseline, Git host settings—swap freely). `doctrine/tooling/estates/` holds **optional** vendor-specific supplements.
- `doctrine/patterns/` shows how build and delivery surfaces fit together (including trunk workflow).
- `doctrine/checklists/` turns the doctrine into reviewable execution (build, collaboration, platform/SRE, release, and doctrine edits).
- `doctrine/evolution/` holds audit notes (for example MoSCoW reviews).
- `doctrine/REFERENCES.md` indexes authoritative external sources; each principle file documents rationale and citations.
- `scripts/generate-doctrine-sitemap.sh` regenerates `doctrine/SITEMAP.md` (all Markdown paths under `doctrine/`).

## How To Use This Repo

1. Adopt the principles first.
2. Tailor the tooling to your current estate and platform constraints.
3. Use the patterns to shape repository structure and delivery surfaces.
4. Use the checklists during rollout, review, and template updates.
5. For **team rollout**, start with `doctrine/patterns/adoption-playbook.md` and optionally `doctrine/tooling/estates/minimum-viable-doctrine.template.md` instead of handing new stakeholders the full tree.

Principles should move slowly. Tooling should change when the stack, platform, or team context changes.
