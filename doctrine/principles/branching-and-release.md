# Branching And Release Principles

These principles define how code moves from idea to production. The objective is fast integration, low merge friction, high confidence, and reversible delivery.

---

## 1. Prefer Trunk-Based Development

- `main` is the primary integration branch and should remain releasable.
- Engineers should integrate to `main` frequently.
- Feature branches are temporary integration aids, not long-lived working areas.
- Long-lived parallel branches increase merge risk, delay feedback, and hide integration problems.

## 2. Keep Feature Branches Short-Lived

- A feature branch should usually live for hours to a few days, not weeks.
- Break large work into smaller vertical slices that can merge independently.
- If work cannot be merged safely yet, hide it behind a feature flag or other release control.
- The longer a branch lives, the more expensive it becomes.

## 3. Small Changes Move Faster And Safer

- Prefer small pull requests with one clear purpose.
- Reviewability is a quality attribute.
- A pull request that is difficult to review is too large or too mixed in concern.
- Separate refactors, behavior changes, and release metadata updates where practical.

## 4. Integrate Continuously

- Every merge to `main` should pass the quality gate.
- Merge conflicts should be resolved while context is still fresh.
- Teams should optimize for frequent integration rather than infrequent “big bang” merges.
- Delayed integration is hidden risk.

## 5. Deploy And Release Are Different Decisions

- Deployment is moving code to an environment.
- Release is exposing behavior to users or downstream systems.
- Use feature flags, configuration, entitlement checks, or controlled activation to separate deploy from release where needed.
- Incomplete work may be deployed if it is safely dark.

## 6. Promote The Same Artefact

- Build once when the platform allows.
- Promote the same immutable artifact through test, staging, and production environments.
- Confidence should increase through validation, not through rebuilding.
- Environment-specific behavior should come from configuration and secrets, not from environment-specific branches.

## 7. Avoid Environment Branching

- Do not maintain separate long-lived branches per environment such as `dev`, `test`, or `prod`.
- Environments represent stages of validation and promotion, not divergent code lines.
- If different environments require different values, use configuration, variables, or managed settings.

## 8. Release Branches Are The Exception

- Prefer release from `main`.
- Create release branches only when there is a documented operational reason, such as supporting multiple active versions or a regulated validation window.
- If release branches exist, define:
  - who owns them
  - how fixes are forward-merged
  - how long they live
  - when they are retired

## 9. Hotfixes Must Rejoin The Mainline

- Urgent production fixes may take an expedited path.
- Every hotfix must merge back into `main` immediately after stabilisation.
- No fix should live only in a patch branch.

## 10. History Should Support Understanding

- Use clear commit messages in imperative mood.
- Prefer a history that explains intent and supports audit and rollback.
- Branch and PR names should describe the change being made, not just the ticket number.