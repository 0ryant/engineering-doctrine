# Contributing

Thanks for helping improve this library. The goal is **trustworthy portable doctrine**: clear layering, reviewable changes, and honest compatibility signals—not bureaucracy.

## License

By contributing, you agree your contributions are under the same license as the project ([LICENSE](LICENSE), Apache-2.0). If your employer needs a formal sign-off, obtain it before you submit substantial work.

## Where things live (read this before a big PR)

- **Principles** — `doctrine/principles/`: durable, vendor-agnostic intent. Change rarely; cite rationale and references.
- **Tooling** — `doctrine/tooling/`: illustrative stacks and examples; swap in your own estate.
- **Estates** — `doctrine/tooling/estates/`: optional, organisation-specific supplements only.
- **Patterns, checklists, evolution** — as named in [doctrine/README.md](doctrine/README.md) and [doctrine/patterns/how-to-read-this-doctrine.md](doctrine/patterns/how-to-read-this-doctrine.md).

If you are unsure, open an issue or a **draft PR** and ask. Mis-layered text is the main avoidable review churn.

## How to propose doctrine changes (public consumers and contributors)

1. **Small, safe fixes** (typos, broken links, obvious clarifications) — open a PR directly. Run the checklist items that apply in [doctrine/checklists/doctrine-change-checklist.md](doctrine/checklists/doctrine-change-checklist.md).
2. **New or moved guidance** (new pattern, new checklist, reshaped principle) — open an **issue first** (or a draft PR with a short “intent” in the description) so maintainers can confirm fit and layer. Point to a **change class** (editorial, additive, normative tightening, etc.) as in [doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md](doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md).
3. **Structural or governance decisions** about this repo (naming, ADR policy, big navigation changes) — add or update an ADR under [docs/adr/](docs/adr/) per [docs/adr/README.md](docs/adr/README.md), then link it from the PR.

**Material additions to the library** (new normative area, new principle/pattern, policy-shaping change): follow [doctrine/patterns/doctrine-library-change-harness.md](doctrine/patterns/doctrine-library-change-harness.md) — **research**, **ADR** (create or reference), **cross-linked layers**, and **sitemap / glossary / REFERENCES** (and related entry points). Use `./scripts/doctrine-change-preflight.sh` before opening the PR. **Claude skill (optional):** [docs/skill/DoctrineLibraryChange/](docs/skill/DoctrineLibraryChange/) — copy to `~/.claude/skills/DoctrineLibraryChange`. Optional Cursor rule: copy [docs/cursor/doctrine-library-change.mdc](docs/cursor/doctrine-library-change.mdc) to `.cursor/rules/` (see [docs/cursor/README.md](docs/cursor/README.md)).

**Consumers** who do not have write access: fork the repository, make your branch, open a pull request to the default branch, and describe **consumer impact** (who must react: everyone, only event-driven teams, only AI/RAG, etc.).

## Pull request expectations

- **Smallest diff** that achieves the goal; no drive-by renames or unrelated formatting sweeps.
- **Label the change class** in the PR description (at least for substantive edits to `doctrine/` or `ENGINEERING.md`).
- **Regenerate** [doctrine/SITEMAP.md](doctrine/SITEMAP.md) when you add, remove, or rename Markdown under `doctrine/`: run `./scripts/generate-doctrine-sitemap.sh` from the repo root.
- **Cross-links**: avoid orphan pages; update [doctrine/README.md](doctrine/README.md) or [doctrine/REFERENCES.md](doctrine/REFERENCES.md) when you add a first-class document.

## Review

Reviewers look for **correct layer**, **clear rationale**, **references** where a principle is asserted, and **compatibility** language for any normative shift. See [GOVERNANCE.md](GOVERNANCE.md) for maintainer and merge expectations.

## Security

If your finding should not be public first, read [SECURITY.md](SECURITY.md).

## Community

Be constructive and specific. Disagree in writing in issues and PRs; prefer proposals over complaints. If the project later adopts a formal code of conduct, it will be linked from this file and from the README.

## What we do not need

- Perfect prose on the first try—iterative review is normal.
- Vendor product pitches in **principles**; put product specifics in **tooling** or **estates**.

## Related

- [GOVERNANCE.md](GOVERNANCE.md) — releases, maintainers, scope of this meta policy.
- [doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md](doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md) — how upgrades are communicated.
- [doctrine/checklists/doctrine-change-checklist.md](doctrine/checklists/doctrine-change-checklist.md) — pre-merge checks for library edits.
