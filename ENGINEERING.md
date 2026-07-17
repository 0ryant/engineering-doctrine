# Engineering Principles

These principles govern how code, infrastructure, and tooling is designed and built.
They are intentionally durable. Apply them from the first commit, not retroactively.

Build and delivery guidance is split deliberately:

- Durable rules live in `doctrine/principles/`.
- Current implementation defaults live in `doctrine/tooling/`.
- Repo-shape guidance and checklists live in `doctrine/patterns/` and `doctrine/checklists/`.

When tooling changes, update the tooling docs first. Change the principles only when the operating model itself has changed.

**AI and ML-assisted systems** are **first-class**: `doctrine/principles/ai-ml-systems.md` (tiers A–D, retrieval lifecycle, agents, MCP-class tools) applies whenever you ship GenAI, RAG, custom training, or agentic automation—alongside `doctrine/patterns/rag-retrieval-baseline.md` and `doctrine/tooling/vector-retrieval-and-embedding-illustration.md` where retrieval is in scope. The **adoption operating model** (inventory & materiality, ownership & independent challenge, harm-surface testing, AI provider continuity, capability uplift) is `doctrine/patterns/ai-adoption-controls.md` + `doctrine/checklists/ai-adoption-readiness.md`. When AI participates across software delivery, use `doctrine/patterns/ai-native-software-development-lifecycle.md`: stakeholder need, objective and guardrailed outcome measures, intervention hypothesis, bounded work, executable change, authority, evidence, enactment, and observed outcome advance as explicit, reconciled transitions. Tasks and outputs are never substitutes for outcomes.

**Principles vs tooling:** Portable **intent** lives in `doctrine/principles/`; replaceable **examples and estate notes** live in `doctrine/tooling/` (including `tooling/estates/`). See `doctrine/principles/timeless-principles-and-tooling.md`.

**TL;DR + minimum viable doctrine (MVP) synthesis:** `doctrine/tldr-principles-and-mvp.md`.

**Glossary (terms and acronyms):** `doctrine/glossary.md`.

**Contributing, license, and security (this repository’s meta policy):** root `README.md` (License and project governance), `CONTRIBUTING.md`, `SECURITY.md`, and `GOVERNANCE.md`.

---

## 1. Contracts First

- Define data schemas before writing implementation code. JSON Schema, OpenAPI, Protobuf, or Terraform variable definitions are all valid depending on context.
- Version all schemas explicitly. Never mutate a versioned schema; create a new version.
- Keep example and fixture files alongside every schema. They serve as documentation and test inputs.
- Validate contracts in CI as a mandatory quality gate. A schema that cannot be validated against its examples is broken code.
- Contract violations are build failures, not warnings.
- **Asynchronous and event-shaped boundaries** — use **[CloudEvents](https://github.com/cloudevents/spec)** as the standard **envelope** for events (queues, topics, webhooks, buses), plus a **versioned payload** schema for `data`. Event types (`type`) and producers (`source`) are stable identifiers; event `id` supports deduplication under at-least-once delivery.
- Full rules: `doctrine/principles/event-contracts.md`. Current CloudEvents defaults: `doctrine/tooling/cloudevents.md`. Workflow state and transition → event mapping: `doctrine/principles/state-machines-and-workflows.md`. Optional NATS/JetStream illustration: `doctrine/tooling/nats-jetstream.md`. Worked fiction (order FSM + subjects): `doctrine/patterns/example-order-jetstream-workflow.md`.

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
- Nuance (duplication vs wrong abstraction, generated code): `doctrine/principles/single-source-of-truth.md`.

---

## 4. Idempotency

- Every operation that modifies state must be safe to run multiple times with the same inputs and produce the same result.
- Prefer `set` and `upsert` orientation. `create` operations check for existence first and return a distinct, catchable error if the resource already exists.
- Infrastructure changes use plan, review, then apply. Never mutate live infrastructure without a diff step.
- Use atomic writes for every file modification: write to a temp file, then rename.
- Cross-boundary idempotency (HTTP, messages, infra): `doctrine/patterns/idempotency-across-boundaries.md`.
- RAG retrieval baseline (hybrid search, eval, privacy): `doctrine/patterns/rag-retrieval-baseline.md`.

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
- Secure development lifecycle (design review, vuln response, training): `doctrine/principles/secure-development-lifecycle.md`.
- AI-assisted engineering, RAG, fine-tuning, and agentic automation (governance, truth in repo, tiers): `doctrine/principles/ai-ml-systems.md`; illustrative tooling categories: `doctrine/tooling/ai-assisted-development.md`; retrieval baseline: `doctrine/patterns/rag-retrieval-baseline.md`; agent harness loop design (ReAct, verifiability gate, ISC, dual-path injection defence, context engineering, verbal RL): `doctrine/patterns/agentic-loop-design.md`.

---

## 6. Right Tool For The Job

Choose the language, runtime, and tooling that best fit the problem. Avoid dogmatic single-language codebases. Prefer tools that match the team's strengths and the project's operational constraints.

The table below is **illustrative** for templates and brownfield guidance—not mandatory estate law. Standardise **organisation-wide** stacks in `doctrine/tooling/estates/` when you need one agreed answer.

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
- Ports-and-adapters / hexagonal nuance: `doctrine/principles/modularity-and-ports-adapters.md`.

---

## 8. Zero Trust

- Never assume a caller is trusted without verifying credentials at the point of access.
- No implicit ambient auth from environment alone; verify explicitly every time.
- Vault and secret access should re-validate through a challenge or equivalent proof on every open.
- Least privilege applies to every service identity.
- Applications do not store master credentials locally in plaintext under any circumstances.
- Deeper pattern (workload identity, SPIFFE, service-to-service): `doctrine/principles/zero-trust-and-workload-identity.md`.

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
- Field-level guidance, immutability, retention: `doctrine/principles/audit-logging.md`.
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

- **Workstation container engine** (Podman, Docker, Colima, etc.) is an **estate** decision—record the team default in `doctrine/tooling/estates/` when it matters; the principle is **reproducible** definitions and **least surprise**, not a single vendor SKU. Prefer Podman **where licensing or workstation constraints** make it the better default **for that estate**.
- **Production runtime** — prefer **vendor-managed application platforms** when they meet requirements and reduce **self-managed control-plane sprawl**. Use **Kubernetes** when **cluster-level** capabilities are required; record the decision in your **platform catalogue** or ADRs. See `doctrine/principles/container-runtime-choice.md`. When you **do** run Kubernetes, apply `doctrine/principles/kubernetes-platform-security.md`. **Concrete product mappings** (for example Azure vs AWS vs GCP) belong in `doctrine/tooling/estates/` supplements, not in portable principles.
- **Interoperability specs** — **CloudEvents** and **OpenTelemetry** name **portable shapes** at boundaries; they do **not** mandate any **full** vendor or foundation stack. See `doctrine/principles/interoperability-and-standards.md` and `doctrine/principles/timeless-principles-and-tooling.md`.
- Every service should have **tracked** container build definitions: **production** and **development** images (exact filenames are template-level—`Dockerfile`, `Dockerfile.dev`, `Containerfile`, or generator equivalents are all valid if documented).
- Use **Compose** or equivalent when local multi-container orchestration is part of the workflow.
- Use non-root users in final images unless there is a documented exception.
- Use named volumes for dependency and build caches when local containers need them.

---

## 12. Build And Delivery Surfaces

Every project must define the build and delivery surfaces it actually owns. Not every repo needs every surface, but every surface that exists must be explicit, documented, and reviewable.

The **example paths** below (`.pipelines/...`) are **one** template layout—your CI host may use different filenames; keep the **meaning** of each surface.

| Surface | Example path | Responsibility |
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
- Materialise CI variables and secret references using your estate’s pattern (directory layout is not prescribed here).

See `doctrine/principles/build.md` and `doctrine/patterns/build-surface-model.md` for the operating model behind this structure.

---

## 13. Collaboration And Trunk-Based Workflow

- **Trunk as default** — one integration branch (`main`) is the source of truth; integrate frequently via short-lived topic branches and reviewed merges.
- **Protected branch** — no direct pushes to the default branch; required status checks and review before merge; merge only when checks pass.
- **Small pull requests** — one concern per change where practical; large or risky work gets a design note or RFC first.
- **Feature flags** — incomplete capabilities ship behind flags with safe defaults; flags have owners and removal plans.
- **Promotion** — promote immutable artefacts through environments; same build ID or image tag from test to prod where the platform allows.
- **GitOps and declarative operations** — when infrastructure and platform config are managed as *declarative* desired state in version control and reconciled (or push-equivalently) with *visible drift*—not manual snowflakes. Pattern: `doctrine/patterns/gitops-and-declarative-operations.md`.
- **Operational rigour** — named service ownership, runbooks for deploy and rollback, observability for new risk, blameless postmortems with tracked actions, SLOs and error budgets where user-facing reliability matters.
- **Footguns to avoid** — long-lived integration branches, force-push to shared branches, merging red, Friday merges without rollback, CI that cannot run locally, manual production drift.

Full doctrine: `doctrine/principles/collaboration.md`. Pattern: `doctrine/patterns/trunk-workflow.md`; code review and merge path: `doctrine/patterns/code-review-and-change-approval.md`; GitOps (declarative / reconciled desired state): `doctrine/patterns/gitops-and-declarative-operations.md`. Checklist: `doctrine/checklists/collaboration-readiness.md`. Platform defaults (GitHub/GitLab): `doctrine/tooling/collaboration.md`.

### Git Hooks And Local Hygiene

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
- **Semantic versioning** applies per **publishable unit** (package, service, CLI, versioned API, image, app, or other independently upgraded artefact). Use the smallest honest **major / minor / patch** bump; bump only units that changed. Full policy: `doctrine/principles/semantic-versioning.md`.
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
- HTTP Problem Details, CLI exit codes, retries: `doctrine/principles/errors-and-failure-modes.md`.

---

## 16. Configuration And Secrets

- Never commit secrets, tokens, connection strings, or credentials to source control.
- Provide `.env.example` documenting every required environment variable with placeholder values and a one-line description.
- Local development should inject secrets through ignored local files or a dedicated secrets launcher, not hardcoded values.
- CI should inject secrets from variable groups, secure stores, or vault-backed variables.
- Production should use a managed secret store and workload identity where the platform supports it.
- Password prompts in CLIs use masked input. Passwords are never echoed or logged.
- Config vs secrets, rotation, dynamic config: `doctrine/principles/configuration-and-secrets.md`.

---

## 17. Naming And Project Structure Conventions

- Choose an org-wide repo naming convention and apply it consistently.
- Layout, monorepo vs polyrepo, CODEOWNERS: `doctrine/principles/naming-and-repo-layout.md`.
- Use `doctrine/` at template roots when the repo is intended to teach repeatable engineering patterns.
- Script directories should be grouped by responsibility such as `scripts/quality/`, `scripts/setup/`, `scripts/build/`, and `scripts/infra/`.
- Pipeline definitions live in your estate’s chosen location (for example `.pipelines/`, `.github/workflows/`, or `.gitlab-ci.yml`).
- IaC lives under `terraform/` or `infra/`.
- `packaging/` is for tracked package-manager manifests. `dist/` is generated output only.
- Contracts live under `contracts/` with schemas and examples side by side. Event payload contracts and examples sit with synchronous API contracts; use a clear subdirectory or naming convention for event types (for example `contracts/events/`).
- Use strict modes and fail-fast defaults in shell scripts.

---

## 18. Platform Operations, Observability, And Extended Principles

The following **principle** documents extend build/trunk doctrine with **SRE, data, API security, and governance** expectations. Each file includes **rationale** (why we chose this) and **references** to authoritative sources. **Vendor-specific** examples live under `doctrine/tooling/estates/`—see `doctrine/principles/timeless-principles-and-tooling.md`.

**Timeless vs tooling** — `doctrine/principles/timeless-principles-and-tooling.md` (includes an **illustrative NIST SSDF PO/PS/PW/RV** cross-walk in §6).

**Umbrella-aligned depth (also in §§3–17 above)** — `doctrine/principles/single-source-of-truth.md`, `configuration-and-secrets.md`, `audit-logging.md`, `errors-and-failure-modes.md`, `naming-and-repo-layout.md`, `modularity-and-ports-adapters.md`, `zero-trust-and-workload-identity.md`, `secure-development-lifecycle.md`, `ai-ml-systems.md`.

**Data and persistence** — `doctrine/principles/data-and-migrations.md` (expand/contract migrations, backups, RPO/RTO).

**Observability** — `doctrine/principles/observability.md`; illustrative tooling: `doctrine/tooling/observability.md`.

**Testing strategy** — `doctrine/principles/testing-strategy.md` (pyramid, contract tests, flakiness, adversarial / abuse-case testing on the merge path).

**State machines and workflows (event-backed)** — `doctrine/principles/state-machines-and-workflows.md` (transitions, idempotency, event-type mapping).

**API boundaries and API security** — `doctrine/principles/api-boundaries-and-security.md` (limits, authz, OWASP API alignment).

**AI and ML-assisted systems** — `doctrine/principles/ai-ml-systems.md` (governance, tiers A–D + materiality axis, merge path, OWASP LLM); adoption controls: `doctrine/patterns/ai-adoption-controls.md`; **AI-native delivery lifecycle** (objective → guardrailed outcome measures → intervention → bounded work → outputs → observed outcomes; S0 observed need → S10 reconciled; transition records, layered evidence, deterministic enactment): `doctrine/patterns/ai-native-software-development-lifecycle.md` + `doctrine/checklists/ai-native-sdlc-readiness.md`; **agentic loop design** (nested loop, verifiability gate, ISC, autonomy slider, dual-path injection defence, context engineering, verbal RL): `doctrine/patterns/agentic-loop-design.md`; illustrative tooling: `doctrine/tooling/ai-assisted-development.md`.

**Threat modeling (STRIDE lite)** — `doctrine/principles/threat-modeling-stride-lite.md` (trust boundaries; complements API and platform security).

**Privacy and data governance** — `doctrine/principles/privacy-and-data-governance.md`.

**Reliability: SLOs, error budgets, incidents** — `doctrine/principles/reliability-slo-incidents.md`.

**Delivery measurement (DORA metrics)** — `doctrine/principles/measurement-and-dora.md` (delivery-system signals, not company objectives; **SPACE** developer-experience framing in §4).

**Developer experience** — `doctrine/principles/developer-experience.md` (time-to-first-change, local loop, docs findability, cognitive load, review flow); scorecard: `doctrine/checklists/developer-experience-scorecard.md`.

**Performance, load, and cost** — `doctrine/principles/performance-and-cost.md`.

**FinOps and cloud cost governance** — `doctrine/principles/cost-and-finops.md` (tagging strategy, unit economics, anomaly SLAs, AI inference budgets).

**Platform engineering and team topologies** — `doctrine/principles/platform-engineering.md` (team types, interaction modes, golden paths, cognitive load metrics, TVP).

**Documentation and knowledge** — `doctrine/principles/documentation-knowledge.md` (ADRs, runbooks).

**Dependencies and supply chain** — `doctrine/principles/dependencies-supply-chain.md`; illustrative automation options: `doctrine/tooling/dependency-automation.md`.

**Merge path, pipeline integrity, and evidence** — `doctrine/principles/merge-path-evidence-and-pipeline-integrity.md` (controlled merge channel; pipeline definitions as security artefacts; binding gates; SBOM and provenance when stakeholders require them).

**Governance programme for engineering controls** — `doctrine/patterns/engineering-controls-governance-program.md` (ownership, exceptions, metrics, audit consumption); readiness checklist `doctrine/checklists/governance-program-readiness.md`; illustrative control categories `doctrine/tooling/merge-path-and-pipeline-control-suite.md`.

**User-facing quality** — `doctrine/principles/user-facing-quality.md` (accessibility, internationalisation).

**CI platform mapping** — `doctrine/tooling/ci-platform-mapping.md` (abstract surfaces vs example CI products).

**Canonical reference index** — `doctrine/REFERENCES.md`.

**Checklist** — `doctrine/checklists/platform-readiness.md`.

**Platform as product, golden paths, service catalog** — `doctrine/patterns/platform-as-product-and-golden-paths.md` (self-service guardrails, catalog metadata, exceptions—portable; no mandated portal product).

**Interoperability and standards posture** — `doctrine/principles/interoperability-and-standards.md`.

**Container runtime choice (managed vs Kubernetes)** — `doctrine/principles/container-runtime-choice.md`.

**Kubernetes security (only when running K8s)** — `doctrine/principles/kubernetes-platform-security.md`.

**Estate-specific tooling supplements** — `doctrine/tooling/estates/` (optional mappings; example Azure: `estates/azure-container-runtimes.md`; empty stubs: `estates/aws-container-runtimes.md`, `estates/gcp-container-runtimes.md`).

**How to read this doctrine** — `doctrine/patterns/how-to-read-this-doctrine.md`.

**Feature flag lifecycle and progressive delivery** — `doctrine/patterns/feature-flag-lifecycle.md` (flag taxonomy, lifecycle FSM, data-gated rollout, flag debt, OpenFeature).

**Message channels (DLQ, replay)** — `doctrine/patterns/message-channel-operations.md`. Illustrative brokers: `doctrine/tooling/nats-jetstream.md`, `doctrine/tooling/kafka-and-cloudevents.md`.

**Webhook ingress** — `doctrine/patterns/webhook-ingress-security.md`.

**Idempotency across boundaries** — `doctrine/patterns/idempotency-across-boundaries.md`.

**RAG retrieval baseline** — `doctrine/patterns/rag-retrieval-baseline.md` (hybrid retrieval, eval, privacy/security).

**Vector / embedding pipeline (illustrative tooling)** — `doctrine/tooling/vector-retrieval-and-embedding-illustration.md`.

**Enterprise RAG, indexing, agents (research)** — `doctrine/evolution/research-enterprise-rag-agents-indexing-2026-04.md`.

**Mythos-era / AI vulnerability storm (research + corpus closure)** — `doctrine/evolution/mythos-era-engineering-principles-research-2026-04-28.md`; ADR `docs/adr/0010-record-mythos-era-vulnerability-storm-research-and-doctrine-gaps.md` (G1–G6 **closed** in principles/patterns—see ADR table).

**Chaos engineering and game days** — `doctrine/patterns/chaos-engineering-and-game-days.md` (extends `doctrine/principles/reliability-slo-incidents.md`).

**Worked fiction — saga (payment + inventory)** — `doctrine/patterns/example-saga-payment-workflow.md` (with `example-order-jetstream-workflow.md` for JetStream).

**Release checklist** — `doctrine/checklists/release-readiness.md`.

**Doctrine maintenance** — `doctrine/checklists/doctrine-change-checklist.md`, audit log `doctrine/evolution/moscow-review.md`.

**Doctrine file index** — `doctrine/SITEMAP.md` (regenerate: `scripts/generate-doctrine-sitemap.sh`).

**Team adoption / migration** — `doctrine/patterns/adoption-playbook.md`; one-page pitch template: `doctrine/tooling/estates/minimum-viable-doctrine.template.md`.

**External review synthesis** — `doctrine/evolution/honest-review-synthesis.md`.

---

## Quick-Start Checklist For A New Project

Copy this list to the project README under `## Setup` and tick items off:

```text
[ ] Schema or contract files defined and example docs created
[ ] Contract validation script written and passing
[ ] Event producers/consumers: CloudEvents envelope, versioned payload schema, examples, validation (if the repo uses async events)
[ ] .env.example with all required variables documented
[ ] Local task runner or one documented command mirrors the quality gate
[ ] .gitignore covers secrets, build outputs, Terraform state, OS files, and IDE files
[ ] Setup script is idempotent and documented
[ ] .githooks/pre-commit and pre-push written
[ ] git config core.hooksPath .githooks added to setup script
[ ] Quality gate pipeline triggers on PRs and protected branches (path per estate; `.pipelines/quality.yaml` is one example)
[ ] Multi-platform validation exists when the repo claims support beyond one platform
[ ] Build and publish surface exists if the repo ships versioned artefacts
[ ] Deploy surface exists for each deployable unit the repo owns
[ ] Scheduled execution or smoke surfaces exist when the repo owns recurring automation or runtime checks
[ ] Shared checked-out inputs are included in validation or scan context when they influence delivery
[ ] Infrastructure deploy workflow exists with plan, apply, and destroy when the repo owns infrastructure
[ ] packaging/ manifests tracked if the repo ships through package managers
[ ] Publish parameters or separate release entrypoints are documented for side-effecting release actions
[ ] Promotion reuses the same built artefact or explicit image tag where the platform allows it
[ ] SemVer policy understood per publishable unit (see doctrine/principles/semantic-versioning.md) or exception documented
[ ] Generated docs, completions, or man pages included in release artefacts where applicable
[ ] Execution and smoke surfaces publish evidence artefacts where they produce operational outcomes
[ ] Production and development container build definitions exist and are documented if the repo ships containers
[ ] compose.yaml or docker-compose.yml works for local container workflows where needed
[ ] Terraform provider pinned and backend configured if the repo owns infrastructure
[ ] README includes what it does, architecture, setup, and interface reference
[ ] Repo-level AI or editor guidance added if the organisation standardises it
[ ] Default branch protected; required checks and review match trunk policy
[ ] Collaboration and trunk readiness reviewed using doctrine/checklists/collaboration-readiness.md where teams adopt full doctrine
[ ] Platform / SRE extended readiness reviewed using doctrine/checklists/platform-readiness.md where teams adopt full doctrine
[ ] Versioned releases use doctrine/checklists/release-readiness.md where applicable
```
