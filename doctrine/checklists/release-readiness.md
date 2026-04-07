# Release Readiness Checklist

Use when cutting a **versioned** release of a publishable unit (library, service, CLI, app). Aligns with [../principles/semantic-versioning.md](../principles/semantic-versioning.md) and trunk workflow in [../patterns/trunk-workflow.md](../patterns/trunk-workflow.md).

```text
[ ] SemVer bump matches consumer impact (patch / minor / major) per semantic-versioning.md
[ ] Changelog or release notes list user-visible and operator-visible changes
[ ] Contract changes (API, CLI, schema, event type) called out; migration / upgrade steps linked
[ ] Lockfiles and reproducible build inputs updated if dependencies changed
[ ] Quality gate green on the revision that ships
[ ] Artefact is immutable (tag, digest, or build ID) before promotion to further environments
[ ] Rollback path known: revert release, feature flag, or forward fix — documented in runbook or release notes
[ ] Hotfix path understood if patching production from a tag (merge back to main per trunk pattern)
[ ] Observability: dashboards or alerts checked for new failure modes introduced by this release
```
