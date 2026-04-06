# Engineering Doctrine

Reusable engineering doctrine that separates stable principles from replaceable tooling.

This repository is intended to be a reference library for teams building applications, automation, CLIs, APIs, and infrastructure. The goal is to keep the operating model durable while allowing implementation details to evolve over time.

## Structure

- `ENGINEERING.md` is the umbrella engineering guide.
- `doctrine/principles/` contains stable rules that should survive tooling changes (including collaboration, trunk-based workflow, operational rigour, and event/message contracts).
- `doctrine/tooling/` contains current recommended implementation defaults (build stack, CloudEvents, and Git host collaboration settings).
- `doctrine/patterns/` shows how build and delivery surfaces fit together (including trunk workflow).
- `doctrine/checklists/` turns the doctrine into reviewable execution (build and collaboration).

## How To Use This Repo

1. Adopt the principles first.
2. Tailor the tooling to your current estate and platform constraints.
3. Use the patterns to shape repository structure and delivery surfaces.
4. Use the checklists during rollout, review, and template updates.

Principles should move slowly. Tooling should change when the stack, platform, or team context changes.
