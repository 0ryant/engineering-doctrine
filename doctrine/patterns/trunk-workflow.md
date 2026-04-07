# Trunk Workflow And Delivery Surfaces

This pattern shows how trunk-based development connects to the [build surface model](build-surface-model.md) and team practices described in [principles/collaboration.md](../principles/collaboration.md). Git host defaults for branch rules and merge queues live in [../tooling/collaboration.md](../tooling/collaboration.md).

## Intent

- Keep **one integration branch** (`main`) always deployable or clearly marked otherwise.
- Land work through **short-lived branches** and **reviewed merges**.
- Use **automation** to prove quality before merge and after deploy.

## Flow (Typical)

```text
  topic branch                    main                         environments
       |                           |                                |
       +--- commit, push ---------->|                                |
       |         PR + CI            |                                |
       |         review            |                                |
       +--- merge (when green) ---->|---- quality gate on main ----->|
       |                           |     build / publish            |
       |                           |     deploy (per policy) ------>| staging
       |                           |     verify -------------------->|
       |                           |     promote ------------------->| production
```

Not every repo runs every stage; **missing stages must be explicit**, not accidental.

## Responsibilities

| Layer | Responsibility |
| --- | --- |
| **Author** | Small PR, clear description, local quality gate before push |
| **Reviewer** | Correctness, contracts, operability, security notes |
| **CI (pre-merge)** | Mandatory checks aligned with protected-branch policy |
| **CI (post-merge)** | Build, publish, deploy per path filters and ownership |
| **Runtime verification** | Smoke or synthetic checks after deploy; SLO monitoring ongoing |

## Feature Work Without Blocking Trunk

1. **Vertical slices** — mergeable increments that keep the product working.
2. **Feature flags** — default off or safe; remove flags after stabilization.
3. **Contract versioning** — additive changes first; breaking changes versioned and coordinated.

## Merge Queue (Optional, At Scale)

When many contributors land on `main`, use a **merge queue** so:

- Batches serialize against the latest `main`.
- Required checks run against the **merge result**, not only the branch tip.
- Flaky tests get fixed or quarantined; the queue is not a workaround for instability.

## Relation To Release Metadata

- Version bumps and changelog entries may happen on `main` continuously or at release tags; either way, **one source of truth** for version (see `ENGINEERING.md` distribution principles).
- **Hotfixes** branch from the tagged release, fix, tag patch, merge back to `main` so drift does not accumulate.

## Checklist Touchpoints

- [checklists/collaboration-readiness.md](../checklists/collaboration-readiness.md) — trunk and branch policy  
- [checklists/release-readiness.md](../checklists/release-readiness.md) — versioned releases and hotfix discipline  
- [patterns/message-channel-operations.md](message-channel-operations.md) — if delivery includes async consumers
