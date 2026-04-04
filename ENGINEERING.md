# Engineering Principles

These principles govern how code, infrastructure, and tooling is designed and built.
They are intentionally durable. Apply them from the first commit, not retroactively.

Build and delivery guidance is split deliberately:

- Durable rules live in `doctrine/principles/`.
- Current implementation defaults live in `doctrine/tooling/`.
- Repo-shape guidance and checklists live in `doctrine/patterns/` and `doctrine/checklists/`.

When tooling changes, update the tooling docs first. Change the principles only when the operating model itself has changed.

---

## 1. Contracts First

- Define data schemas before writing implementation code. JSON Schema, OpenAPI, Protobuf, or Terraform variable definitions are all valid depending on context.
- Version all schemas explicitly. Never mutate a versioned schema; create a new version.
- Keep example and fixture files alongside every schema. They serve as documentation and test inputs.
- Validate contracts in CI as a mandatory quality gate. A schema that cannot be validated against its examples is broken code.
- Contract violations are build failures, not warnings.

---

## 2. Test-Driven Development

- Write tests before or alongside implementation. Tests written only after the fact are pre-commit insurance, not TDD.
- Every public API surface such as a library function, CLI command, or REST endpoint needs at minimum:
  - One test for the happy path.
  - One test for the principal failure path.
- Use environment variable overrides for all path resolution to enable CI isolation without mocking global state.
- Integration tests live in a `tests/` directory alongside the code, not buried in CI scripts.
- Tests are documentation. A test name should describe the behaviour, not the implementation.

---

## 3. DRY - Single Source Of Truth

- Centralise shared dependency versions in one place such as a Cargo workspace, `pyproject.toml`, or workspace root manifest.
- Never duplicate a version string. Source it once and derive it everywhere else.
- One schema file, one secret store, one version string. If you find yourself copy-pasting a constant, it belongs in a shared module.

---

## 4. Idempotency

- Every operation that modifies state must be safe to run multiple times with the same inputs and produce the same result.
- Prefer `set` and `upsert` orientation. `create` operations check for existence first and return a distinct, catchable error if the resource already exists.
- Infrastructure changes use plan, review, then apply. Never mutate live infrastructure without a diff step.
- Use atomic writes for every file modification: write to a temp file, then rename.

---

## 5. Shift Security Left

- Security is a first-class requirement from day one, never bolted on.
- Sensitive types such as keys, passwords, and tokens must be handled with language-appropriate zeroization or protected-memory patterns.
- Encryption at rest must use modern AEAD schemes such as XChaCha20-Poly1305 or AES-256-GCM.
- Password-derived keys should use Argon2id where possible, or bcrypt or scrypt when constraints require them.
- Nonces and IVs must be random per operation from a cryptographically secure source and never reused.
- Every state-changing operation writes a structured audit entry.
- Pre-commit hooks block secrets from being committed, enforce formatting, and run linting.
- Secret scanning in CI is required, not optional.
- Fail closed, not open. Default deny.
- Prefer managed identity or OIDC over static credentials wherever supported.

---

## 6. Right Tool For The Job

Choose the language, runtime, and tooling that best fit the problem. Avoid dogmatic single-language codebases. Prefer tools that match the team's strengths and the project's operational constraints.

| Category | Tool | When to reach for it |
| --- | --- | --- |
| **Languages** | Rust | Systems programming, crypto, static binaries, CLI tools |
| | Go | Network services, CLIs, lightweight microservices |
| | Python 3.12+ | Data pipelines, scripting, ML, API prototyping |
| | TypeScript | Web frontends, VS Code extensions, Node.js backends |
| | .NET (C#) | Enterprise integrations, Windows-native tooling, Azure-heavy estates |
| **Ops / Automation** | PowerShell 7 | Windows automation, CI helper scripts, Azure operations |
| | Bash / sh | Linux and container entrypoints where PowerShell is unavailable |
| | YAML pipelines | CI orchestration only; logic belongs in repo scripts |
| **Infrastructure** | Terraform >= 1.5 | Cloud provisioning with reviewable plans and reusable modules |
| | Podman + Compose | Container workflows without Docker Desktop licensing constraints |

- Write idiomatic code for the chosen language.
- A tool is chosen for a reason; document it once in the README and resist unnecessary stack churn.
- When multiple tools are equally valid, prefer the one already in use in the project or team.
- If the estate standardises on one IaC tool, treat that as the default unless there is an explicit exception.

---

## 7. Lego Extensibility

- Every component is designed to be replaceable and composable without breaking its neighbours.
- Libraries have no I/O. They accept inputs and return typed outputs. I/O belongs at the edges.
- Architect in explicit layers:

  ```
  IaC / Platform
       |
  Distribution
       |
  Application
       |
  Quality gates
  ```

- Extension points are explicit typed contracts such as interfaces, traits, or abstract base classes.
- New features add new modules. They do not mutate stable existing ones unless fixing a bug.
- Prefer feature flags or conditional compilation over repository forks.

---

## 8. Zero Trust

- Never assume a caller is trusted without verifying credentials at the point of access.
- No implicit ambient auth from environment alone; verify explicitly every time.
- Vault and secret access should re-validate through a challenge or equivalent proof on every open.
- Least privilege applies to every service identity.
- Applications do not store master credentials locally in plaintext under any circumstances.

---

## 9. Layered Architecture

Apply this consistently. Each layer has exactly one responsibility and communicates through well-defined interfaces:

```text
+-------------------------------------------------+
| IaC / Platform layer                            |
+-------------------------------------------------+
| Distribution layer                              |
+-------------------------------------------------+
| Interface layer                                 |
+-------------------------------------------------+
| Core library layer                              |
+-------------------------------------------------+
```

- The core library is tested in isolation with no mocking of external systems.
- The interface layer is thin: parse input, call core, format output.
- The IaC layer should align with the same environment variable names and runtime assumptions used by the app layer.

---

## 10. Audit Everything

- Every state-changing operation writes a structured audit entry.
- Audit records are append-only.
- Minimum fields per entry:
  - `id` - UUID v4
  - `timestamp` - ISO-8601 UTC
  - `actor` - who or what performed the operation
  - `operation` - what was done
  - `resource` - what was acted on
  - `status` - `success` or `failure`
  - `message` - optional human-readable context, required on failure
- Preferred format: JSONL.
- Audit logs outlive the session. They are queryable and archivable.

---

## 11. Container Strategy

- Prefer Podman where licensing or workstation constraints make it the better default.
- Every service should have:
  - `Dockerfile.build` for the production image
  - `Dockerfile.dev` for local development
  - `docker-compose.yml` or `compose.yaml` when local orchestration is part of the workflow
- Use non-root users in final images unless there is a documented exception.
- Use named volumes for dependency and build caches when local containers need them.

---

## 12. Build And Delivery Surfaces

Every project must define the build and delivery surfaces it actually owns. Not every repo needs every surface, but every surface that exists must be explicit, documented, and reviewable.

| Surface | Default file | Responsibility |
| --- | --- | --- |
| **Quality gate** | `.pipelines/quality.yaml` | fmt, lint, type-check, test, contract validation, secret scan |
| **Build & Publish** | `.pipelines/build-and-publish.yaml` | compile, package, and publish versioned artefacts |
| **Deploy Infrastructure** | `.pipelines/deploy-infrastructure.yaml` | Terraform plan, apply, destroy |
| **Deploy Runtime / Automation** | `.pipelines/deploy-*.yaml` | publish apps, jobs, runbooks, or data assets by deployable unit |
| **Execute / Smoke** | `.pipelines/*execution*.yaml`, `.pipelines/*smoke*.yaml` | scheduled automation, queued operations, smoke tests, and evidence publication |

Rules:

- Every repo has a quality gate.
- Add a build and publish surface only if the repo emits versioned artefacts.
- Split deploy surfaces by deployable unit. Infrastructure, runtime, automation, and data promotion are separate concerns even when they share a repo.
- Scheduled or manually queued execution surfaces stay separate from deploy when they run on their own cadence, permissions, or evidence contract.
- Prefer path filters or scoped triggers so a change only runs the surfaces it can affect.
- If the repo claims multi-platform support, validate at least one non-primary supported platform before release and package on the target platform when packaging semantics differ.
- If deploy or release logic consumes checked-out sibling or shared repo content, that content is part of the delivery graph and must be scanned or validated too.
- CI orchestrates. Repo scripts implement.
- Local task runners should mirror the quality gate and primary build actions closely enough for pre-push reproduction.
- Promote the same built artefact through staging, smoke, and production where the platform allows it.
- Pipeline variable files live in `.pipelines/variables/` alongside the pipeline that uses them.

See `doctrine/principles/build.md` and `doctrine/patterns/build-surface-model.md` for the operating model behind this structure.

---

## 13. Git Workflow

- Keep `.githooks/` in the repo root. Do not rely on developers configuring hooks manually.
- `git config core.hooksPath .githooks` belongs in the setup script.
- `pre-commit` should stay fast and focus on format and contract validation.
- `pre-push` can be slower and run the full lint and test suite.
- Setup scripts must be idempotent.
- Commit messages use imperative mood and present tense.

---

## 14. Distribution And Release Metadata

- Release metadata is source code. Track installer and package-manager manifests under `packaging/` or an equivalent reviewed directory.
- Ignored output folders such as `dist/`, `target/`, or staging directories are for generated artefacts only.
- Version is sourced from one manifest and derived everywhere else.
- Publish steps consume previously built artefacts. They do not invent metadata inline or silently rebuild during publish.
- Promotion flows should reuse immutable build outputs or explicit image tags across environments where the platform allows it.
- Expensive platform builds or side-effecting publish steps should be explicit, parameterised entrypoints rather than implicit on every merge.
- Release artefacts should include operator-facing outputs that are part of the product contract: installers, archives, docs, man pages, shell completions, schema examples, SBOMs, checksums, or migration notes as applicable.
- Feed URLs, API keys, and publish endpoints come from environment variables or variable groups. Never hardcode them in code or pipeline YAML.

---

## 15. Error Handling

- Library code returns typed results or raises typed exceptions.
- Avoid panics, unchecked unwraps, and silent exception swallowing in library code.
- Use typed error enums or hierarchies that callers can match on.
- Error messages are actionable: they explain what went wrong and what the operator should do next.
- Never swallow errors silently. Log with context at the callsite before propagating upward.
- The boundary layer such as a CLI, API, or UI translates internal errors into user-facing messages and exit codes.

---

## 16. Configuration And Secrets

- Never commit secrets, tokens, connection strings, or credentials to source control.
- Provide `.env.example` documenting every required environment variable with placeholder values and a one-line description.
- Local development should inject secrets through ignored local files or a dedicated secrets launcher, not hardcoded values.
- CI should inject secrets from variable groups, secure stores, or vault-backed variables.
- Production should use a managed secret store and workload identity where the platform supports it.
- Password prompts in CLIs use masked input. Passwords are never echoed or logged.

---

## 17. Naming And Project Structure Conventions

- Choose an org-wide repo naming convention and apply it consistently.
- Use `doctrine/` at template roots when the repo is intended to teach repeatable engineering patterns.
- Script directories should be grouped by responsibility such as `scripts/quality/`, `scripts/setup/`, `scripts/build/`, and `scripts/infra/`.
- Pipeline files live under `.pipelines/` with a `variables/` subdirectory where needed.
- IaC lives under `terraform/` or `infra/`.
- `packaging/` is for tracked package-manager manifests. `dist/` is generated output only.
- Contracts live under `contracts/` with schemas and examples side by side.
- Use strict modes and fail-fast defaults in shell scripts.

---

## Quick-Start Checklist For A New Project

Copy this list to the project README under `## Setup` and tick items off:

```text
[ ] Schema or contract files defined and example docs created
[ ] Contract validation script written and passing
[ ] .env.example with all required variables documented
[ ] Local task runner or one documented command mirrors the quality gate
[ ] .gitignore covers secrets, build outputs, Terraform state, OS files, and IDE files
[ ] Setup script is idempotent and documented
[ ] .githooks/pre-commit and pre-push written
[ ] git config core.hooksPath .githooks added to setup script
[ ] .pipelines/quality.yaml triggers on PRs and protected branches
[ ] Multi-platform validation exists when the repo claims support beyond one platform
[ ] Build and publish surface exists if the repo ships versioned artefacts
[ ] Deploy surface exists for each deployable unit the repo owns
[ ] Scheduled execution or smoke surfaces exist when the repo owns recurring automation or runtime checks
[ ] Shared checked-out inputs are included in validation or scan context when they influence delivery
[ ] .pipelines/deploy-infrastructure.yaml with plan, apply, and destroy when the repo owns infrastructure
[ ] packaging/ manifests tracked if the repo ships through package managers
[ ] Publish parameters or separate release entrypoints are documented for side-effecting release actions
[ ] Promotion reuses the same built artefact or explicit image tag where the platform allows it
[ ] Generated docs, completions, or man pages included in release artefacts where applicable
[ ] Execution and smoke surfaces publish evidence artefacts where they produce operational outcomes
[ ] Dockerfile.build and Dockerfile.dev exist if the repo ships containers
[ ] compose.yaml or docker-compose.yml works for local container workflows where needed
[ ] Terraform provider pinned and backend configured if the repo owns infrastructure
[ ] README includes what it does, architecture, setup, and interface reference
[ ] Repo-level AI or editor guidance added if the organisation standardises it
```
