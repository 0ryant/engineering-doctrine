# Build Surface Model

Use this model to design a repo's build and delivery flow without coupling the design to one CI system or one language stack.

---

## The Layers

```text
Developer tasks -> Script layer -> Quality gate -> Build/release -> Deploy -> Verify/execute
                           \-> Packaging metadata -> Release artefacts -> Evidence
```

| Layer | Audience | Purpose | Typical entrypoint |
| --- | --- | --- | --- |
| Developer tasks | Humans | Fast local invocation of common actions | `just`, `make`, `task`, `nox`, `npm run` |
| Script layer | Repo internals | Own the real logic used by local and CI surfaces | `python -m scripts ...`, `pwsh -File ...` |
| Quality gate | Merge control | Prove the repo is safe to merge or tag | `.pipelines/quality.yaml` |
| Build/release | Artefact production | Compile, package, and publish versioned outputs | `.pipelines/build-and-publish.yaml` |
| Deploy | Environment ownership | Apply infra or publish runtime and automation content | `.pipelines/deploy-*.yaml` |
| Verify / execute | Operators and schedulers | Run smoke tests, queued jobs, scheduled assurance, or post-deploy validation | `.pipelines/*execution*.yaml`, `.pipelines/*smoke*.yaml` |
| Packaging metadata | Distribution ownership | Keep installer and package-manager metadata reviewable | `packaging/` |

---

## Recommended Repo Shapes

### IaC-Only Repo

- Quality gate
- Deploy infrastructure
- No release pipeline unless the repo ships a reusable package or module artefact

### Infrastructure Plus Automation Repo

- Quality gate
- Deploy infrastructure
- Deploy automation or runbooks
- Verification after automation publish
- Shared checked-out modules or supporting repos included in validation and scan context when they influence deployment

Common lesson: infrastructure and automation publication are related, but they are not the same deployable unit.

### Application Repo

- Quality gate
- Build and publish artefacts
- Deploy runtime
- Smoke or readiness verification

### Automation Ingress Plus Execution Repo

- Quality gate
- Build and publish ingress runtime
- Deploy runtime
- Separate execution pipelines per request or automation type
- Publish completion or evidence artefacts for the execution path

Common lesson: the ingress service and the queued operational work may live in one repo, but they are not the same delivery surface.

### Scheduled Assurance Repo

- Quality gate
- Deploy infrastructure
- Scheduled execution surface
- Evidence artefact publication
- Telemetry or alert publication

Common lesson: recurring assurance work is a first-class operational product.

### Multi-Platform CLI Or Desktop Utility

- Quality gate
- Primary quality gate on one platform plus representative validation on at least one other claimed platform
- Build and publish artefacts per platform
- Packaging metadata under `packaging/`
- Generated docs included in release artefacts

Common lesson: packaging manifests are source, not output, and operator docs should ship with the release.

### Multi-Stage Runtime Promotion

- Build once
- Deploy to staging or sandbox
- Run smoke or readiness checks
- Gate promotion with approval or explicit handoff
- Promote the same artefact to production

Common lesson: the confidence step sits between staging and production, not after a silent rebuild.

---

## What To Avoid

- One giant pipeline that plans Terraform, builds binaries, publishes automation, runs recurring jobs, and deploys runtime code together just because they share a repo.
- Hidden build logic scattered across large inline YAML blocks.
- Local commands that do something materially different from CI.
- Scheduled or queued operational work buried inside deploy pipelines.
- Package-manager manifests stored in ignored output folders.
- Rebuilding for production after staging already proved a different artefact.
- Generated docs that are committed but not shipped.
- Deployments that end at "published successfully" without verifying the result.
