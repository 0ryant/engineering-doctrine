# Build Readiness Checklist

Use this checklist when creating or reviewing a repo.

```text
[ ] The repo's build surfaces are named and documented
[ ] There is one documented local command for the quality gate
[ ] Non-trivial build logic lives in repo scripts, not repeated inline YAML
[ ] Setup or bootstrap commands are idempotent
[ ] The quality gate runs on PRs and protected branches
[ ] Supported platforms are validated in CI when the repo claims multi-platform support
[ ] Contract or schema validation exists where the repo defines contracts
[ ] Published or consumed async events use CloudEvents envelope and versioned payload schemas where applicable
[ ] Secret scanning exists before merge
[ ] Dependency and IaC scanning exist where relevant
[ ] Checked-out sibling or shared inputs are included in validation or scan scope when they influence delivery
[ ] Build caches are optional and keyed from real inputs
[ ] A build and publish surface exists if the repo ships versioned artefacts
[ ] Deploy surfaces are split by deployable unit
[ ] Scheduled execution or smoke surfaces are separate from deploy when the repo owns recurring automation or runtime checks
[ ] Path filters or scoped triggers prevent unrelated deploys
[ ] Version is sourced from one manifest
[ ] Packaging metadata is tracked under packaging/ if package-manager manifests exist
[ ] Ignored folders are used only for generated output
[ ] Side-effecting publish actions are gated behind explicit release entrypoints or parameters
[ ] Promotion reuses the same built artefact or explicit image tag where the platform allows it
[ ] Release artefacts include operator-facing docs and evidence where applicable
[ ] Execution and smoke surfaces publish evidence artefacts when they produce operational outcomes
[ ] Publish steps consume built artefacts instead of rebuilding inline
[ ] Post-deploy verification exists for each deploy surface
[ ] README documents the repo's chosen build surfaces and entrypoints
[ ] Tooling guidance is captured separately from enduring principles
```
