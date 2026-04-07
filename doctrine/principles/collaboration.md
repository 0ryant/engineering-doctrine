# Collaboration, Trunk-Based Delivery, And Operational Rigour

These rules govern how teams work together on shared code, how changes land on the default branch, and how engineering discipline extends into delivery and operations. Tooling can change. These principles should change only when the operating model changes.

Related build and release rules live in [build.md](build.md) and [../patterns/trunk-workflow.md](../patterns/trunk-workflow.md). GitHub and GitLab implementation defaults live in [../tooling/collaboration.md](../tooling/collaboration.md).

---

## 1. Trunk-Based Development Is The Default

- **Single integration branch** (usually `main`) is the source of truth for what ships. Long-lived branches are for exceptional cases, not day-to-day work.
- **Short-lived topic branches** exist only long enough to produce a reviewable change. Days, not weeks.
- **Integrate frequently** — small, incremental merges reduce merge pain and keep feedback loops tight.
- **Avoid merge queues of doom** — if a branch cannot merge within a few days, the work is probably too large; split it.
- **Release from trunk** (or from tags on trunk). Releases are not separate parallel development lines unless the product model truly requires it (and that requirement is documented).

---

## 2. Branch Protection And Merge Policy

- **Protected default branch** — no direct pushes; changes land via reviewed merge requests or pull requests.
- **Required status checks** — quality gate must pass before merge; required checks match what `main` is supposed to guarantee.
- **Required review** — at least one approval from someone who was not the sole author of the change, except for documented bot-only or emergency paths.
- **Linear history optional but valuable** — squash or rebase merges reduce noise; pick one team convention and stick to it.
- **Merge when green** — do not merge on red; do not “merge anyway” without a recorded exception process.
- **Merge queue or batching** — at scale, use a merge queue or batched merges so `main` stays green under concurrent work; the queue is part of the integration system, not a substitute for small changes.

---

## 3. Pull Requests: Small, Reviewable, Complete

- **Prefer small PRs** — easier to review, easier to revert, easier to bisect. Large changes need a design note or RFC first.
- **One concern per PR** — mixing refactors with behaviour changes makes review and rollback harder; split when practical.
- **Description answers** what, why, and how to verify. Link tickets or decision records when they exist.
- **Draft until ready** — do not request review on WIP unless explicitly seeking early direction.
- **Review for correctness, contracts, and operability** — schemas, migrations, feature flags, and rollout risk are first-class review topics.

---

## 4. Feature Flags And Controlled Rollout

- **Incomplete features do not block trunk** — ship behind flags with defaults that preserve current behaviour until intentionally enabled.
- **Flag lifecycle is owned** — temporary flags have owners and removal dates; stale flags are debt.
- **Server-side configuration** — prefer remote configuration or dynamic flags for kill switches; avoid “redeploy to turn it off” as the only option for user-visible risk.

---

## 5. Async-First Collaboration

- **Decisions live in the repo** — ADRs, short decision logs, or RFCs for significant choices. Chat is for discussion; the repo is for conclusions.
- **Disagree in writing** — summarise options, pick one, record why. Reduces repeated debates and onboarding cost.
- **Handoffs are explicit** — owner, scope, and next step documented in the ticket or PR, not only in standup.

---

## 6. Environments And Promotion

- **Environment parity in intent** — staging (or equivalent) should exercise the same deploy path and checks as production, even if scale differs.
- **Promote artefacts, not rebuilds** — same binary, image, or package version from test through prod where the platform allows (see `ENGINEERING.md` build surfaces).
- **Data and secrets** — production-like data never required for unit tests; use fixtures. Secrets never in repo; parity includes *how* secrets are injected, not their values.

---

## 7. DevOps Rigour: Delivery Pipeline Discipline

- **Pipeline as code** — reviewable, versioned, repeatable.
- **Fail fast** — lint, test, and contract checks before expensive integration steps; same order locally where possible.
- **Immutable build identifiers** — builds produce traceable artefact IDs; releases reference those IDs.
- **No silent skips** — optional steps that are skipped must be visible (or removed). “Best effort” CI that always passes teaches teams to ignore red.
- **Path-scoped automation** — triggers and permissions scoped so a doc change does not deploy infra (unless infra owns docs-as-code for that path).

---

## 8. SRE Rigour: Reliability And Operations

- **Service ownership** — each service or deployable unit has a named owner team; ownership includes on-call or escalation path where applicable.
- **SLOs where users care** — define availability and latency objectives for user-facing paths; measure them; error budgets inform release and change policy. Expanded doctrine: [reliability-slo-incidents.md](reliability-slo-incidents.md).
- **Runbooks** — operational procedures for deploy, rollback, common failures, and dashboards; stored in-repo or linked from repo README.
- **Observability** — structured logs, metrics, and traces sufficient to debug production incidents without reproducing locally; new features include observability in the definition of done. Expanded doctrine: [observability.md](observability.md), tooling: [../tooling/observability.md](../tooling/observability.md).
- **Incidents** — blameless postmortems for meaningful incidents; action items tracked to completion.
- **Change risk** — risky changes use canaries, gradual rollout, or maintenance windows per service policy; emergency changes still get a retrospective.

---

## 9. Security And Compliance In The Loop

- **Same rules as trunk** — secret scanning, dependency audit, and licence policy apply to every merge path.
- **Dependency updates** — cadence or automation for patches; breaking upgrades are planned work, not accidental drift.
- **Least privilege in CI and deploy** — pipeline identities scoped to what each pipeline needs; production deploy is not the default permission for every job.

---

## 10. Footguns To Avoid

| Footgun | Safer default |
| --- | --- |
| Long-lived “integration” branches | Trunk + small PRs + flags |
| Force-push to shared branches | Protected branches; revert commits instead |
| “Merge Friday 5pm” without rollback plan | Merge when you can watch; or defer |
| Skipping tests “just this once” | Fix or narrow the test; document rare waivers |
| Silent feature flags defaulting on in prod | Explicit defaults; staged enablement |
| One mega-PR blocking everyone | Slice work; merge skeletons behind flags |
| CI that cannot run locally | One command to reproduce the quality gate |
| Manual production edits | GitOps or reviewed automation; no snowflakes |
| Oncall without runbooks | Minimum viable runbook before paging |
| Metrics that lie (synthetic only) | Combine synthetic and real user monitoring |

---

## 11. Scaling The Model

- **CODEOWNERS or equivalent** — critical paths require the right reviewers automatically.
- **RFCs for cross-cutting change** — migrations, platform shifts, or contract breaks get design review before large code dumps.
- **Release train optional** — regular release cadence helps teams coordinate; trunk still integrates continuously.

When these principles conflict with a deadline, **narrow scope** or **add safety** (flags, canaries, rollback). Do not permanently lower the bar without recording the debt and plan to recover.
