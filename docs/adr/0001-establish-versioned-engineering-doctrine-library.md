# 0001. Establish A Versioned Engineering Doctrine Library

Status: Accepted (retrospective)  
Decision date: 2026-04-04  
Recorded date: 2026-04-26  
Retrospective: Yes

## Context

The repository began as a shared engineering-doctrine library rather than a product-specific implementation repo. The first commit introduced a root umbrella, a doctrine folder, build principles, build tooling, build-readiness checklist, and a build-surface pattern.

Evidence:

- Commit `651a709` — "Add initial engineering doctrine" (`2026-04-04`)
- Files introduced included `ENGINEERING.md`, `doctrine/principles/build.md`, `doctrine/tooling/build.md`, `doctrine/patterns/build-surface-model.md`, and `doctrine/checklists/build-readiness.md`

## Decision

Keep engineering doctrine as **versioned repository content** with a root umbrella and topic files under `doctrine/`.

The library should be reviewable, diffable, and usable by other repos as a canonical source of engineering intent.

## Consequences

- Doctrine changes become normal code-review artefacts, not chat-only guidance.
- The repository needs navigation, checklists, and update discipline as it grows.
- Downstream consumers can pin, copy, or vendor doctrine, but this repo remains the canonical source unless a consumer repo deliberately overrides it.

## Honesty Note

This ADR was written after the commit landed. It reconstructs the decision from repository evidence and should not be read as proof that an ADR existed on 2026-04-04.
