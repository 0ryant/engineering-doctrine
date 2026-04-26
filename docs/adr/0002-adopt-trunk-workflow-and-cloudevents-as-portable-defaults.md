# 0002. Adopt Trunk Workflow And CloudEvents As Portable Defaults

Status: Accepted (retrospective)  
Decision date: 2026-04-07  
Recorded date: 2026-04-26  
Retrospective: Yes

## Context

After the initial build doctrine, the repo added collaboration principles, a trunk-workflow pattern, an event-contracts principle, and CloudEvents tooling guidance. This moved the library beyond build mechanics into collaboration and asynchronous boundary contracts.

Evidence:

- Commit `7316003` — "Add collaboration, trunk workflow, CloudEvents doctrine" (`2026-04-07`)
- Files introduced included `doctrine/principles/collaboration.md`, `doctrine/patterns/trunk-workflow.md`, `doctrine/principles/event-contracts.md`, `doctrine/tooling/cloudevents.md`, and `doctrine/checklists/collaboration-readiness.md`

## Decision

Adopt **trunk-based collaboration** as the portable workflow baseline and **CloudEvents** as the default event envelope for asynchronous boundaries.

CloudEvents is a portable interoperability choice; product-specific messaging systems remain tooling or estate choices.

## Consequences

- Collaboration and event contracts are part of doctrine, not incidental project preferences.
- Event payloads need versioning and fixtures separate from the envelope.
- Teams can choose NATS, Kafka, cloud buses, or other transports without changing the event-contract principle.

## Honesty Note

This ADR was written after the commit landed. It reconstructs the decision from repository evidence and should not be read as proof that an ADR existed on 2026-04-07.
