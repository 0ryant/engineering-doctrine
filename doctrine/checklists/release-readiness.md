# Release Readiness Checklist

Use when cutting a **versioned** release of a publishable unit (library, service, CLI, app). Aligns with [../principles/semantic-versioning.md](../principles/semantic-versioning.md), [../patterns/trunk-workflow.md](../patterns/trunk-workflow.md), and [../principles/errors-and-failure-modes.md](../principles/errors-and-failure-modes.md).

## Version And Semantics

```text
[ ] SemVer bump matches consumer impact (patch / minor / major) per semantic-versioning.md
[ ] Pre-release channel (alpha/rc) or dist-tags documented if not using stable-only SemVer
[ ] Changelog or release notes list user-visible and operator-visible changes
[ ] Contract changes (API, CLI, schema, event type) called out; migration / upgrade steps linked
[ ] Deprecations in this release reference sunset timeline per semantic-versioning.md §9
```

## Build, Supply Chain, Evidence

```text
[ ] Lockfiles and reproducible build inputs updated if dependencies changed
[ ] Quality gate green on the exact revision (commit / tag) that ships
[ ] SBOM attached for artefacts shipped externally, to regulated environments, or where law, contract, or policy demands one; provenance per the artefact's SLSA target (dependencies-supply-chain.md §§3–4)
[ ] Artefact is identified by digest, or by an identifier its registry or store will not re-point, before promotion beyond first trusted environment (a tag that can be moved is not one)
```

## Rollback, Flags, Hotfix

```text
[ ] Recovery path known: flag reversion, rollback to the previous candidate, or forward fix — documented in runbook or release notes ([impl/release-and-rollback.md](../impl/release-and-rollback.md))
[ ] Canary or gradual rollout: judging signals and tolerance recorded before start; rollback decider named in the runbook; any automated rollback targets the previously verified candidate (principles/collaboration.md §8.1)
[ ] Hotfix path understood if patching production from a tag (merge back to main per trunk pattern)
[ ] Feature flags introduced in this release are typed, with an owner and safe default; release and experiment flags also have an expiry date (patterns/feature-flag-governance.md §§2, 6)
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
[ ] DORA-style lead time / CFR can be measured for this release if the org tracks DORA delivery metrics (measurement-and-dora.md)
```
