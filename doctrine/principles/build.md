# Build Principles

These are the durable rules for how repositories should build, package, release, deploy, execute, and verify. Tooling can change. These principles should change only when we learn something structural. How this differs from `tooling/` examples: [timeless-principles-and-tooling.md](timeless-principles-and-tooling.md).

Async **event and message** contracts are covered in [event-contracts.md](event-contracts.md).

**Data stores, migrations, backups** — [data-and-migrations.md](data-and-migrations.md).

---

## 1. Build Surfaces Must Be Explicit

- Define the build surfaces a repo actually owns: local developer entrypoint, script layer, quality gate, release surface, deploy surface, execution surface, and verification surface.
- Not every repo needs every surface. Hidden surfaces are the problem, not missing ones.
- Every surface must have a name, a purpose, and an obvious entrypoint.

## 2. CI Orchestrates; Scripts Implement

- Pipeline YAML should handle checkout, authentication, caching, environment wiring, and script invocation.
- Build logic belongs in versioned scripts or task runners inside the repo.
- If logic is repeated across pipelines, environments, or repos, it belongs in a script, not inline YAML.

## 3. Local And CI Must Agree

- Every mandatory CI gate should be runnable locally with one documented command.
- Local task runners should mirror CI semantics closely enough that failures are reproducible before push.
- Setup scripts must be idempotent so a contributor can repair or re-run their environment safely.

## 4. Separate By Deployable Unit

- Infrastructure, application runtime, automation and runbooks, package publishing, scheduled assurance, and data promotion are different deployable units.
- Different deployable units should have separate delivery surfaces even when they live in one repo.
- Path filters and scoped triggers should reflect deployable ownership, not repo convenience.

## 5. Validate Before Packaging; Verify After Deployment

- The minimum order is: validate -> build -> package -> publish -> deploy -> verify.
- Never publish from a state that did not pass the quality gate.
- When the platform allows, promote the same built artefact through staging and production rather than rebuilding per environment.
- Deployment is incomplete until verification proves the deployed thing is healthy enough for its intended use.

## 6. Release Metadata Is Source Code

- Version, package names, installer metadata, package-manager manifests, and release note inputs are source, not output.
- Keep release metadata in tracked directories such as `packaging/`, not in ignored output folders such as `dist/`.
- Build outputs may be regenerated. Release metadata must remain reviewable and diffable.
- Semantic version increments follow [semantic-versioning.md](semantic-versioning.md) per publishable unit.

## 7. Release Artefacts Include Operational Usefulness

- A release is not just the executable or deployment bundle.
- If users or operators need man pages, shell completions, schema examples, SBOMs, checksums, migration notes, or verification reports, those are release artefacts too.
- Generated docs should derive from the live source of truth so they cannot silently drift.

## 8. Execution And Assurance Surfaces Are First-Class

- Scheduled scans, queued automation, smoke tests, and recurring operational runbooks are delivery surfaces in their own right.
- Give execution surfaces explicit entrypoints, permissions, contracts, and evidence outputs.
- Do not hide recurring operational behaviour inside deployment pipelines just because it uses the same repo.

## 9. Supported Platform Claims Must Be Verified

- If a repo claims support for an OS, architecture, shell, or runtime, the build model must exercise that target before release.
- Use a primary platform for deep quality gates and representative validation jobs for secondary supported platforms.
- Package on the target platform when packaging semantics differ materially by platform.

## 10. Security Gates Must Cover The Real Delivery Graph

- Scan the dependencies, scripts, shared modules, and referenced assets that actually ship or influence deployment.
- If a pipeline checks out sibling or shared repos or copies modules into a deployment context, those inputs are part of the delivery graph and must be scanned or validated too.
- Secret scanning, contract validation, dependency audit, and IaC scanning belong in the build model, not as optional afterthoughts.
- Allowlists must be explicit, documented, and reviewed periodically.

## 11. Caches Are Accelerators, Not Dependencies

- Builds must still work when caches are cold or absent.
- Cache keys should be tied to real inputs such as lockfiles, platform, or toolchain.
- A cache miss may slow the build. It must not change correctness.

## 12. Build Evidence Matters

- Produce durable evidence for what happened: plans, SBOMs, published artefact names, test results, verification output, and audit-friendly metadata.
- Execution results, smoke evidence, and callback or completion payloads count as durable evidence when they are part of the operating model.
- Evidence should outlive the terminal session and be retrievable after the fact.
- Prefer additive evidence over hand-written change summaries.

## 13. Tooling Is Replaceable; Contracts Are Not

- Task runners, script languages, CI systems, packaging tools, deployment tasks, and smoke frameworks may change over time.
- The contract of each build surface should remain stable even if the implementation is replaced.
- When tooling changes, update the tooling guidance first. Only change the principles if the operating model itself has changed.
