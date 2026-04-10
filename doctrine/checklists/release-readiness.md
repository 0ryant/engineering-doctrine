# Release Readiness Checklist

Use when cutting a **versioned** release of a publishable unit (library, service, CLI, app). Aligns with [../principles/semantic-versioning.md](../principles/semantic-versioning.md), [../patterns/trunk-workflow.md](../patterns/trunk-workflow.md), and [../principles/errors-and-failure-modes.md](../principles/errors-and-failure-modes.md).

## Version And Semantics

```text
[ ] SemVer bump matches consumer impact (patch / minor / major) per semantic-versioning.md
[ ] Pre-release channel (alpha/rc) or dist-tags documented if not using stable-only SemVer
[ ] Changelog or release notes list user-visible and operator-visible changes
[ ] Contract changes (API, CLI, schema, event type) called out; migration / upgrade steps linked
[ ] Deprecations in this release reference sunset timeline per semantic-versioning.md §8
```

## Build, Supply Chain, Evidence

```text
[ ] Lockfiles and reproducible build inputs updated if dependencies changed
[ ] Quality gate green on the exact revision (commit / tag) that ships
[ ] SBOM or provenance generated where organisation policy or regulators expect it (see dependencies-supply-chain.md, SLSA)
[ ] Artefact is immutable (tag, digest, or build ID) before promotion beyond first trusted environment
```

## Rollback, Flags, Hotfix

```text
[ ] Rollback path known: revert release, feature flag, or forward fix — documented in runbook or release notes
[ ] Hotfix path understood if patching production from a tag (merge back to main per trunk pattern)
[ ] Feature flags introduced in this release have owners and removal dates (collaboration.md)
```

## Communication

```text
[ ] **Internal** stakeholders notified (support, SRE, dependent teams) when behaviour or ops change
[ ] **Customer** or **public** release comms drafted when user-visible impact warrants (status page, email, in-app)
[ ] **Security** or **compliance** comms template ready if the release addresses CVEs (secure-development-lifecycle.md)
```

## Observability And Risk

```text
[ ] Dashboards or alerts updated for new failure modes introduced by this release
[ ] SLO burn risk assessed for high-change releases (reliability-slo-incidents.md)
```

## Post-Release

```text
[ ] Tag and artefacts match what was tested; no post-tag rebuild drift
[ ] DORA-style lead time / CFR can be measured for this release if the org tracks Four Keys (measurement-and-dora.md)
```
