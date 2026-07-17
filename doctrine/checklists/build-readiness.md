# Build Readiness Checklist

Use this checklist when creating or reviewing a repo.

```text
[ ] The repo's build surfaces are named and documented
[ ] There is one documented local command for the quality gate
[ ] Fast local loop documented separately from slower full gates where both exist (developer-experience.md)
[ ] Non-trivial build logic lives in repo scripts, not repeated inline YAML
[ ] Setup or bootstrap commands are idempotent
[ ] The quality gate runs on PRs and protected branches
[ ] Supported platforms are validated in CI when the repo claims multi-platform support
[ ] Contract or schema validation exists where the repo defines contracts
[ ] **GenAI, RAG, embeddings, or agents** in this repo: **tier** (A–D) and SoR rules in [principles/ai-ml-systems.md](../principles/ai-ml-systems.md); **ingestion/index** lifecycle, **eval**, and **tenant** isolation per [patterns/rag-retrieval-baseline.md](../patterns/rag-retrieval-baseline.md) and [tooling/vector-retrieval-and-embedding-illustration.md](../tooling/vector-retrieval-and-embedding-illustration.md) where applicable (skip if out of scope)
[ ] Published or consumed async events use the selected explicit envelope contract (CloudEvents by portable default, or a documented equivalent) and versioned payload schemas where applicable
[ ] Message DLQ/replay/observability addressed where the repo owns async consumers (see patterns/message-channel-operations.md)
[ ] Secret scanning exists before merge
[ ] Dependency and IaC scanning exist where relevant
[ ] Build provenance / SLSA-style attestations exist where regulators or customers require tamper-evident delivery (principles/build.md §14, principles/dependencies-supply-chain.md)
[ ] Checked-out sibling or shared inputs are included in validation or scan scope when they influence delivery
[ ] Build caches are optional and keyed from real inputs
[ ] A build and publish surface exists if the repo ships versioned artefacts
[ ] Deploy surfaces are split by deployable unit
[ ] Scheduled execution or smoke surfaces are separate from deploy when the repo owns recurring automation or runtime checks
[ ] Path filters or scoped triggers prevent unrelated deploys
[ ] Version is sourced from one manifest
[ ] Semantic version bumps follow doctrine/principles/semantic-versioning.md (or a documented exception) per publishable unit
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
