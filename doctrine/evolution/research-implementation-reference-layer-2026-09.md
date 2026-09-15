# Research Note: Implementation Reference Layer

Date: 2026-09-14

## Question

Would a first-class implementation-reference layer make the doctrine easier to use without creating a new authority layer, and which common activities appear to justify later references?

## Evidence Boundary

This is an information-architecture and repository-usability decision, not a new portable engineering control. The evidence is therefore:

- the current repository structure and semantic routes;
- the number and role of canonical files a reader must compose for common activities;
- the supplied CI/CD composition bundle, treated as proposal material rather than executable or authoritative instruction; and
- the library's existing authority, lifecycle, and non-duplication rules.

External sources already grounding CI/CD requirements remain cited by the canonical owners. This note does not duplicate or re-admit those citations because it introduces no new CI/CD obligation.

## Repository Finding

The current corpus has strong durable owners but no layer whose explicit job is “show the normal implementation in a few minutes.” The semantic route for build and delivery currently starts with `principles/build.md` and `patterns/build-surface-model.md`, then routes to tooling and checklists; reconstructing the complete path also requires collaboration, source-of-truth, merge-path, and trunk-workflow doctrine.

Patterns consequently carry two different reader expectations:

1. explain mechanics, applicability, trade-offs, alternatives, governance, and failure modes; and
2. provide a concise composition that can be used during delivery work.

Separating the second role makes the reading path explicit while leaving authority unchanged:

```text
task intent
  -> implementation reference
  -> canonical principles and owning patterns
  -> product or estate tooling
  -> readiness checklist
```

The useful boundary is not “contains implementation detail.” Existing patterns such as idempotency across boundaries, GitOps, feature-flag governance, code review, and message-channel operations still explain mechanics and trade-offs and remain patterns.

## CI/CD Exemplar Audit

The proposed CI/CD reference composes at least six existing owners:

| Concern | Existing owner |
| --- | --- |
| Explicit quality/build/publish/deploy/verify surfaces | `principles/build.md` |
| Protected trunk, required checks, candidate promotion | `principles/collaboration.md` |
| One authority per version, policy, schema, and configuration concept | `principles/single-source-of-truth.md` |
| Binding gates, privileged pipeline trust, candidate evidence | `principles/merge-path-evidence-and-pipeline-integrity.md` |
| Delivery-unit and multi-stage surface decomposition | `patterns/build-surface-model.md` |
| Branch-to-production workflow | `patterns/trunk-workflow.md` |

The bundle's proposed pattern was therefore adapted into `impl/cicd-delivery.md`, shortened into the reference shape, and bounded explicitly for application artefacts, infrastructure plans, stateful database changes, and environment-rendered configuration. Its apply script was not executed.

## Layer Test

The layer is useful only while all four boundaries hold:

- **Against principles:** it summarises durable requirements but does not own them.
- **Against patterns:** it shows the normal composition but defers nuance, failure modes, and alternatives.
- **Against tooling:** it names capabilities and surfaces, not products or vendor syntax.
- **Against checklists:** it explains the operating shape; checklists ask whether the applicable shape was implemented and evidenced.

Canonical-owner precedence and bottom-of-file source links are necessary because composition inevitably repeats short phrases. The repetition is a derivative route, not competing authority.

## Screened Backlog

These candidates pass an initial repository-level screen: each is a common activity, has a useful flow, and spans at least three existing owners. They remain proposals. Before landing one, re-read its exact owners, check for overlap with an existing pattern, and prove the reference can stay concise without strengthening doctrine.

| Order | Candidate | Practical question | Composition surface found | Initial disposition |
| ---: | --- | --- | --- | --- |
| 1 | `service-api.md` | How should one service expose functionality to another? | API security, errors, identity, observability, versioning, idempotency | Strong candidate |
| 2 | `workload-identity-and-secrets.md` | How does an application obtain credentials safely? | Workload identity, configuration/secrets, audit, merge-path integrity | Strong candidate |
| 3 | `database-migration.md` | How is schema or data changed safely? | Data/migrations, idempotency, failure modes, reliability, observability | Strong candidate |
| 4 | `service-observability.md` | How is a service instrumented and its telemetry verified? | Observability, reliability/SLOs, incident operations, audit boundaries | Strong candidate; keep telemetry conditionality explicit |
| 5 | `application-deployment.md` | What does a production-ready application deployment look like? | Build, configuration, identity, health, recovery, observability | Strong candidate |
| 6 | `infrastructure-delivery.md` | How should infrastructure changes move through environments? | GitOps, build surfaces, merge-path integrity, collaboration, source authority | Strong candidate; do not force binary promotion semantics |
| 7 | `release-and-rollback.md` | How are releases exposed, verified, and recovered? | Candidate identity, feature flags, reliability, collaboration, release readiness | Strong candidate |
| 8 | `event-consumer.md` | How are messages consumed and failures recovered? | Event contracts, message operations, idempotency, state machines, failure modes | Strong candidate |
| 9 | `dependency-adoption.md` | Can a package, image, model, dataset, or tool be admitted? | Dependencies/supply chain, secure development, merge-path evidence | Strong candidate |
| 10 | `new-service.md` | What must exist before a new service is operationally real? | Ownership, boundary contract, delivery, identity, configuration, operability, recovery | Strong candidate; highest breadth and bloat risk |
| 11 | `privileged-automation.md` | What rules apply when automation can mutate real systems? | Merge-path integrity, workload identity, audit, run contracts, review/approval | Strong candidate; applicability must distinguish ordinary assistance from governed execution |

The first implementation sequence should favour narrow, frequently used flows before `new-service.md`, whose breadth makes it most likely to become a framework or duplicate a checklist.

## Post-Exemplar Contract Refinement

Review of the first two references exposed two predictable failure modes: broad nouns invite subject handbooks, and a useful cross-cutting reference can absorb specialist operating models that future siblings should own. The layer contract therefore gained three decisive tests:

- **Activity:** name and frame an activity engineers perform.
- **Compression:** earn the page by composing a model distributed across several owners.
- **No new doctrine:** deleting the reference removes no obligation.

“Compiled view of doctrine” is the internal mental model, not a new formal layer name. It distinguishes source semantics in principles and patterns from a derived, usability-oriented view. The testing reference remains an admitted exception to the normal size target, but its specialist explanations were compressed so its spine is evidence placement across delivery surfaces. Future infrastructure, migration, identity, and observability references should absorb their own operating detail rather than repeat it.

## Consumer Impact

Change class: **additive guidance / navigation**.

No consumer obligation changes. The new layer provides progressive disclosure and new stable entry points; canonical owner links remain the authority for edge cases, rationale, applicability, and exceptions.

## Residual Risk

The main risks are summary drift, accidental normative strengthening, and backlog-driven framework bloat. Link checking and sitemap generation address discovery only. Content review must compare each reference against its named owners, and lifecycle sweeps must treat stale references as defective derivatives.
