# Engineering Doctrine

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

Reusable engineering doctrine that separates stable principles from replaceable tooling.

This repository is intended to be a reference library for teams building applications, automation, CLIs, APIs, and infrastructure. The goal is to keep the operating model durable while allowing implementation details to evolve over time.

## Where To Look

| If you want | Go to |
| --- | --- |
| The normal way to do a common task, in a few minutes | [`doctrine/impl/`](doctrine/impl/README.md): CI/CD delivery, testing, branching, service APIs, event consumers, secretless workload identity, database migrations, observability, release and rollback, dependency adoption, application deployment, infrastructure delivery, new services, privileged automation, git hooks, worktrees |
| The rules and why they exist | [`doctrine/principles/`](doctrine/principles/), starting with the [one-line glance at every principle](doctrine/tldr-principles-and-mvp.md#every-principle-at-a-glance) |
| How the pieces fit together, with trade-offs and failure modes | [`doctrine/patterns/`](doctrine/patterns/) |
| Examples with specific products and commands | [`doctrine/tooling/`](doctrine/tooling/) (illustrations; swap freely) |
| A list to review your work against | [`doctrine/checklists/`](doctrine/checklists/) |
| The core rules on one page | [ENGINEERING.md](ENGINEERING.md) |
| The right files for a specific task (people and agents) | [doctrine/SEMANTIC_INDEX.md](doctrine/SEMANTIC_INDEX.md) |
| Why the library changed | [`docs/adr/`](docs/adr/README.md) for decisions, [`doctrine/evolution/`](doctrine/evolution/) for research |
| A term you don't recognise | [doctrine/glossary.md](doctrine/glossary.md) |

`impl/` pages summarise; they add no rules of their own. If one disagrees with a principle or pattern, the principle or pattern wins.

## License

This repository is licensed under **Apache-2.0** (see [LICENSE](LICENSE)). You may use, copy, adapt, and redistribute the text and code subject to the licence's notice and attribution conditions. This is not legal advice; confirm with your counsel for regulated or commercial deployments.

**Why Apache-2.0:** Engineering Doctrine is an adoption-first reference library intended to be copied, forked, vendored, and adapted into internal and commercial engineering systems. Apache-2.0 keeps that path permissive and supplies an explicit patent grant without requiring downstream modifications to be published.

**Licence history:** the repository carried an MIT licence file from 2026-04-18 (commit `6e41b70`) until the `v0.1.0` release commit (`18532b3`, 2026-04-27) replaced it with Apache-2.0; `v0.1.0` was released under Apache-2.0. The default branch was offered under AGPL-3.0-or-later from commit `66c9398` (2026-05-20) until the adoption-first decision recorded in [ADR 0025](docs/adr/0025-restore-apache-2.0-as-project-license.md), which cites that commit by an identifier, `5f6d783`, that no longer resolves. Effective 2026-07-17, the copyright holder also offers the repository material published during that interval under Apache-2.0. Existing AGPL grants remain valid; recipients may use that material under either applicable grant.

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
- `doctrine/impl/` gives short, implementation-neutral walkthroughs of common activities, composed from principles and patterns; they add no rules of their own.
- `doctrine/checklists/` turns the doctrine into reviewable execution (build, collaboration, platform/SRE, release, and doctrine edits).
- `doctrine/evolution/` holds audit notes (for example MoSCoW reviews).
- `doctrine/maintainers/` holds the patterns that govern changes to this library; they bind only the people and agents changing it, not consumers.
- `contracts/` holds the JSON schemas for agent-facing contracts, and `doctrine/skills/` the skills built on them, each with its verifier pack (see `doctrine/patterns/agent-doctrine-consumption.md`).
- `doctrine/SEMANTIC_INDEX.md` maps task intent to the highest-value doctrine files for humans and agents.
- `doctrine/REFERENCES.md` indexes authoritative external sources; each principle file documents rationale and citations.
- `docs/adr/` records decisions about this doctrine library itself. Retrospective ADRs must include both the original decision date and the date they were recorded.
- `scripts/generate-doctrine-sitemap.sh` regenerates `doctrine/SITEMAP.md` (all Markdown paths under `doctrine/`); `scripts/doctrine-change-preflight.sh` runs it with the other local checks before a library change.

## How To Use This Repo

1. Adopt the principles first.
2. Tailor the tooling to your current estate and platform constraints.
3. Use the patterns to shape repository structure and delivery surfaces.
4. Use the checklists during rollout, review, and template updates.
5. For **team rollout**, start with `doctrine/patterns/adoption-playbook.md` and optionally `doctrine/tooling/estates/minimum-viable-doctrine.template.md` instead of handing new stakeholders the full tree.
6. For decisions about this library, use `docs/adr/` so structural changes are visible without relying on git history alone.

Principles should move slowly. Tooling should change when the stack, platform, or team context changes.
