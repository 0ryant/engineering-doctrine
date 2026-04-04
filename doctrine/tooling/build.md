# Build Tooling

This is the current default tooling guidance that implements the build principles for a Terraform-first, automation-friendly engineering estate.

These choices are defaults, not laws. Replace them when the repo context changes, but preserve the surface contracts described in [../principles/build.md](../principles/build.md).

---

## Current Default Stack

| Surface | Current default | Why it works well | Swappable alternatives |
| --- | --- | --- | --- |
| Local task entrypoint | `justfile` | Simple, readable, maps well to CI verbs | `make`, `task`, `nox`, `tox`, `npm scripts` |
| Script implementation | Python `python -m scripts ...` | Cross-platform glue, easy to test, easy to reuse from CI | Go, C#, Bash, PowerShell, Rust utilities |
| Windows and Azure automation | PowerShell 7 | Strong fit for Azure control planes and Windows operations | C#, Python, Bash where appropriate |
| Quality orchestration | `.pipelines/quality.yaml` | Clear merge-gate boundary | GitHub Actions, reusable pipeline templates |
| Infrastructure deploy | `.pipelines/deploy-infrastructure.yaml` | Explicit Terraform plan, apply, destroy surface | Reusable Terraform pipeline templates |
| Runtime and automation deploy | Separate deploy pipeline per unit | Matches ownership and change scope | Workload-specific deploy pipelines |
| Execution and smoke surface | Separate `.pipelines/*execution*.yaml` or `.pipelines/*smoke*.yaml` | Keeps recurring automation and runtime validation explicit | Scheduler-owned jobs, workflow engines, runbook schedulers |
| Package metadata | `packaging/` | Tracked, reviewable, not hidden under ignored outputs | Ecosystem-native tracked folders with the same property |
| Generated output | `dist/`, `target/`, staging directories | Disposable and reproducible | Any ignored output tree |
| Build cache | Pipeline cache plus language-native cache and `sccache` where valuable | Speeds builds without redefining them | Any cache that is input-keyed and optional |
| Supply-chain checks | Secret scan, contract validation, dependency audit, IaC scan, SBOM | Catches drift across code, config, and release layers | Equivalent scanners that cover the same risks |

---

## Current Recommendations

### Local Build Surface

- Prefer a single human-facing task runner with verbs like `check`, `test`, `release`, `setup`, and `publish`.
- Keep local task names close to CI stage names.
- Make the task runner a convenience layer, not the only way to invoke the logic.

### Script Layer

- Put non-trivial build logic in `scripts/`.
- Group by responsibility such as `scripts/build/`, `scripts/setup/`, `scripts/quality/`, `scripts/proget/`, or `scripts/infra/`.
- Use a single script entrypoint when the repo benefits from discoverability, for example `python -m scripts`.

### Pipeline Layout

- Always keep a quality pipeline.
- Add a build and publish pipeline only when the repo emits versioned artefacts.
- Keep quality automatic. Make expensive platform builds or side-effecting publish steps explicit through parameters, tags, or separate manual entrypoints.
- Split deploy pipelines by deployable unit:
  - infrastructure
  - runtime or application
  - automation or runbooks
  - data or content promotion where needed
- Add separate execution or smoke pipelines when scheduled automation or runtime validation has its own cadence, permissions, or evidence contract.

### Platform Support

- Choose one primary CI platform for the deepest quality gate.
- Add at least one secondary-platform validation job when the repo claims cross-platform support.
- Produce platform-specific installers or archive layouts on the target platform when packaging semantics differ.

### Variable Materialization

- Generate transient tfvars or env files from variable groups and secret stores at runtime when the deployment model needs resolved values.
- Keep the generator script in the repo and the resolved file out of source control.
- Review the generator as build logic, not as a one-off convenience script.

### Promotion And Runtime Validation

- Build once, then promote the same image tag or packaged artefact through staging, smoke, and production where the platform allows it.
- When runtime risk is non-trivial, add an explicit smoke or readiness surface instead of hiding the checks inside deployment-only logic.
- Use environment approvals or promotion boundaries where the operating model needs a human gate.

### Packaging And Distribution

- Keep package-manager manifests in `packaging/`.
- Treat `dist/` as generated output only.
- Derive version strings from one manifest.
- Publish from previously built artefacts instead of rebuilding during the publish step.

### Docs As Artefacts

- Generate CLI docs, man pages, completions, schema examples, or similar artefacts from the live source tree where possible.
- Include those artefacts in release packages when they are part of the user contract.

### Verification And Evidence

- After deployment, verify the deployed unit directly:
  - syntax or parse validation for scripts and runbooks
  - publication state checks
  - smoke tests
  - connectivity or control-plane probes
- Publish the resulting evidence when the run changes or validates real state.

---

## Why These Defaults Hold Up Well

- A task-runner layer gives local and CI parity without forcing developers to remember raw script paths.
- Repo-owned scripts keep logic reviewable, testable, and reusable across pipelines.
- Separate deploy surfaces reduce blast radius and clarify ownership.
- Separate execution and smoke surfaces model recurring automation as a real product surface, not a hidden side effect.
- Tracked packaging manifests prevent release drift.
- Build-once-and-promote improves confidence and reduces environment-specific rebuild surprises.
