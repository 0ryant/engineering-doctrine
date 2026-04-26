# Project governance

This file describes how **this repository** is run so that people forking, citing, or importing the doctrine can trust the process. It does not replace the doctrine inside `doctrine/`; it is **meta** policy for the library as an open project.

## Goals

- Keep **portable** layering clear: `doctrine/principles/` vs `doctrine/tooling/` vs `tooling/estates/` (see [doctrine/patterns/how-to-read-this-doctrine.md](doctrine/patterns/how-to-read-this-doctrine.md)).
- Make **change class** and **consumer impact** explicit for substantive edits (see [doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md](doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md)).
- Avoid process theatre: if a step does not help reviewers or consumers, it should not be mandatory.

## Maintainers

**Maintainers** are people with merge rights on this repository. The current list is whoever holds **admin or maintain** role on the GitHub (or other host) project; this file does not name individuals so it does not go stale. Maintainers are responsible for:

- Enforcing [CONTRIBUTING.md](CONTRIBUTING.md) expectations (principles vs tooling, smallest useful diff).
- Merging or closing contributions with a clear rationale when something does not fit.
- Cutting **release tags** when a release is declared (see below).

There is no separate "core team" document unless the project adds one; use the **code hosting** project’s list of people with merge rights (for example GitHub **Maintainers** or organization teams).

## Review and merge policy

| Change type | Expectation |
| --- | --- |
| Obvious **editorial** (typos, links, sitemap regen) | May merge with a single maintainer after quick self-check. |
| **Additions** in tooling, patterns, or examples (non-normative) | At least one review from another person when available; if you are the only active maintainer, document what you checked. |
| **Principles** or **umbrella** `ENGINEERING.md` | Prefer review by someone who can judge portability and change class; call out **normative** impact in the PR. |
| **New ADRs** or **structural** repo decisions | Use [docs/adr/](docs/adr/) and [docs/adr/README.md](docs/adr/README.md); do not merge large structural rewrites without an ADR or an explicit "why" in the PR. |

**Branch model:** [Trunk-style](doctrine/patterns/trunk-workflow.md) is the default: short-lived branches, merge to the shared default branch after review, no long-lived "develop" line unless the project later adopts it for a good reason (record that in an ADR).

## Release cadence and tags

- **No fixed calendar** is promised before `1.0.0` (or while the project uses `0.y.z` semantics). Tags are created when a **batch of changes** is worth signalling to consumers, or when there is a **normative** or **deprecation** change that benefits from a version pin.
- **SemVer-shaped tags** and change meaning follow [doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md](doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md): patch vs minor vs major (and `0.x` caveats) apply to the **doctrine** contract, not to npm/cargo crates unless this repo later ships them.
- **Dated** files under [doctrine/evolution/](doctrine/evolution/) stay as research and audit context; they are not a substitute for tagged releases when you need a compatibility signal.
- If the project starts publishing **release notes** in GitHub Releases, each material release should list **change classes** and **consumer impact** (minimum in that pattern doc, §4).

## Roadmap

- There is no separate commercial roadmap. **Backlog and gaps** are discussed in the open in [doctrine/evolution/](doctrine/evolution/) (for example [public-doctrine-benchmark-gap-analysis-2026-04.md](doctrine/evolution/public-doctrine-benchmark-gap-analysis-2026-04.md)) and in issues. Priorities follow maintainer and contributor time.

## License posture

See [README.md](README.md#license). The SPDX identifier for the project default is in the root [LICENSE](LICENSE) file.

## Security and conduct

- **Security:** [SECURITY.md](SECURITY.md)
- **Contributing and behaviour:** [CONTRIBUTING.md](CONTRIBUTING.md)

## Changing this file

Edits to governance should be small and reviewable. If governance itself forks (e.g. different merge rules for a foundation), add an ADR in [docs/adr/](docs/adr/) and link it here.
