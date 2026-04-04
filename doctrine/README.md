# Doctrine

This folder captures the durable engineering doctrine that sits underneath repository scaffolds and project templates.

It is split intentionally:

- `principles/` contains the rules that should survive tooling changes.
- `tooling/` contains the current recommended implementation choices.
- `patterns/` shows how the surfaces fit together in real repositories.
- `checklists/` turns the doctrine into reviewable, repeatable execution.

The goal is not to force every repo into one exact shape. The goal is to make build, release, deployment, verification, execution, and evidence explicit enough that teams can change tools without losing the operating model.

Principles should move slowly. Tooling should change as the estate changes.

## Start Here

- [principles/build.md](principles/build.md) for enduring build rules
- [principles/branching-and-release.md](principles/branching-and-release.md) for trunk-based development, short-lived branches, and release flow
- [principles/collaboration.md](principles/collaboration.md) for review, communication, and team operating norms
- [tooling/build.md](tooling/build.md) for current default stack guidance
- [patterns/build-surface-model.md](patterns/build-surface-model.md) for how build and delivery layers fit together
- [patterns/environment-promotion.md](patterns/environment-promotion.md) for build-once and promote-through-environments guidance
- [checklists/build-readiness.md](checklists/build-readiness.md) for rollout and review.