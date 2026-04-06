# Collaboration And Trunk Readiness Checklist

Use when adopting or auditing trunk-based workflow, branch protection, and delivery discipline.

## Trunk And Branching

```text
[ ] Default branch is protected (no direct push, required reviews, required checks)
[ ] Topic branches are short-lived; team norm is days not weeks
[ ] Merge policy documented (squash vs merge commit; who can merge)
[ ] Linear history convention agreed if applicable
[ ] Merge queue or batching in place if concurrent merges routinely collide
[ ] Hotfix path documented (tag branch, patch, merge back to main)
```

## Pull Requests And Review

```text
[ ] PR template or norm covers what / why / how to verify
[ ] Small-PR culture reinforced; large changes need prior design note or RFC
[ ] CODEOWNERS or equivalent for critical paths
[ ] Review checks operability: migrations, flags, rollout, observability
```

## Delivery And DevOps

```text
[ ] Quality gate runs on every PR to merge path
[ ] Same quality gate runnable locally with one documented command
[ ] Path filters prevent unrelated deploys from unrelated changes
[ ] CI identities least-privilege; production deploy not default for all jobs
[ ] Artefact promotion reuses immutable build IDs or explicit image tags
[ ] Post-deploy verification exists for each deploy surface that needs it
[ ] No silent CI skips without visibility or removal
```

## Feature Flags And Safety

```text
[ ] Feature flags used for incomplete user-visible behaviour where applicable
[ ] Flag defaults safe for production; kill switches or remote config where needed
[ ] Stale flags tracked and removed on a cadence
```

## SRE And Operations

```text
[ ] Named ownership for services or deployable units
[ ] SLOs defined for user-facing paths where applicable; error budget policy understood
[ ] Runbooks or linked ops docs for deploy, rollback, common failures
[ ] Observability (logs, metrics, traces) part of definition of done for new risk
[ ] Blameless postmortems for significant incidents; actions tracked
```

## Security And Dependencies

```text
[ ] Secret scanning and dependency audit on merge path
[ ] Dependency update cadence or automation documented
[ ] Emergency change process exists without bypassing audit trail
```

## Collaboration Hygiene

```text
[ ] Decisions of record in ADR, decision log, or RFCs as appropriate
[ ] Async handoffs explicit (owner, scope, next step) in ticket or PR
```
