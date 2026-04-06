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
- [principles/event-contracts.md](principles/event-contracts.md) for event and message contracts (CloudEvents envelope + versioned payloads)
- [principles/collaboration.md](principles/collaboration.md) for trunk-based workflow, team collaboration, DevOps and SRE rigour
- [tooling/build.md](tooling/build.md) for current default stack guidance
- [tooling/cloudevents.md](tooling/cloudevents.md) for CloudEvents spec baseline, bindings, and validation defaults
- [tooling/collaboration.md](tooling/collaboration.md) for GitHub/GitLab branch protection, merge queue / merge trains, and review defaults
- [patterns/build-surface-model.md](patterns/build-surface-model.md) for how the layers fit
- [patterns/trunk-workflow.md](patterns/trunk-workflow.md) for how trunk-based delivery connects to build surfaces
- [checklists/build-readiness.md](checklists/build-readiness.md) for rollout and review
- [checklists/collaboration-readiness.md](checklists/collaboration-readiness.md) for branch protection, review, and operations readiness
