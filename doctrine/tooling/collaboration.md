# Collaboration Tooling

**Example** mappings for implementing [../principles/collaboration.md](../principles/collaboration.md) on common Git hosts. Outcomes are durable (protected `main`, required checks, review); **how** your host enforces them is estate-specific—see [../principles/timeless-principles-and-tooling.md](../principles/timeless-principles-and-tooling.md).

---

## Platform Defaults At A Glance

| Outcome | GitHub (typical) | GitLab (typical) |
| --- | --- | --- |
| Block direct push to default branch | Branch protection: **Restrict who can push** (admins included if policy requires) | Protected branch: **Allowed to merge** via MR only; **Allowed to push** denied for developers |
| Require CI before merge | Branch protection: **Require status checks to pass**; select the checks that define your quality gate | **Pipelines must succeed** on MR; only merge when latest pipeline green |
| Require human review | Branch protection: **Require pull request reviews** (count per policy); optional **Require review from Code Owners** | **Approval rules** on project or merge requests; **CODEOWNERS** for path ownership |
| Keep `main` serial under load | **Merge queue** (merge group) with required checks on the **tested merge commit** | **Merge trains** (merge request pipelines on serialized merges) |
| Enforce one integration branch | Protection rules on `main` (and release branches if used); default branch setting | Protected `main`; release branches protected with stricter rules if needed |
| Emergency bypass | Documented break-glass (admin merge or rule override) with **post-incident review** | Maintainer bypass with same audit expectation |

---

## GitHub

### Branch protection (default branch)

- Enable **Require a pull request before merging** with minimum approvals per org policy (often one for small teams, two for regulated teams).
- Enable **Require status checks to pass** and mark checks as **required** only if they are reliable (fix or remove flaky jobs).
- Enable **Require branches to be up to date before merging** *or* use a **merge queue** so integration is validated against the latest base without manual rebases at high churn.
- Prefer **Require conversation resolution before merging** when review threads must be explicitly cleared.
- **Do not** allow force pushes or branch deletion on protected branches unless a documented exception process exists.

### Merge queue

- Use when multiple contributors merge to `main` daily and concurrent merges cause red builds.
- Configure the queue to run the same (or stricter) checks as the PR, against the **merge group** result.
- Keep batches small enough that failures are diagnosable; fix flaky tests rather than raising timeouts indefinitely.

### CODEOWNERS

- Place `CODEOWNERS` in `.github/` (or repo root per GitHub docs) and require owner review for sensitive paths (infra, security, migrations).

### Pull request settings

- Choose **squash** or **merge** consistently; squash keeps history linear and review units clear; merge preserves per-commit history when that matters.
- Disable **allow merge commits** if the team standardises on squash-only, or the inverse—avoid three equally valid merge styles that confuse contributors.

---

## GitLab

### Protected branches

- Protect `main`: **Allowed to merge** by maintainers or developers via MR; **Allowed to push** denied for roles that should not bypass review.
- **Merge only if pipeline succeeds** on the MR target branch workflow.

### Merge trains

- Enable **merge trains** when high concurrency causes “green MR, red `main`” after merge.
- Trains run pipelines on the **prospective merged result**; same discipline as GitHub merge queue—flaky pipelines undermine the feature.

### Approvals and CODEOWNERS

- Use **approval rules** (per branch, per file pattern) aligned with [CODEOWNERS](https://docs.gitlab.com/ee/user/project/code_owners/) for critical areas.
- Optional **approval rules** for security or compliance roles on infra and release paths.

### Merge method

- Prefer **merge commit** vs **fast-forward** vs **squash** per team convention; document in the project README. Squash mirrors GitHub’s common trunk hygiene.

---

## Cross-Platform Practices

- **Required checks** should map 1:1 to the repo’s documented quality gate (see [build.md](build.md)); avoid listing redundant or experimental jobs as required.
- **Bots**: If release bots or renovate open PRs, policy should still require review or auto-merge only where checks and ownership rules allow it.
- **Infrastructure as code**: When branch rules are codified (e.g. Terraform `github_branch_protection`, GitLab `gitlab_branch_protection`), treat changes like production changes: review, plan, apply.
- **Auditing**: Enable audit logs at the org level where available; break-glass merges should be rare and traceable.

---

## When To Revise This Doc

Update this file when the organisation changes Git host features, renames default checks, or adopts a different merge policy—**before** teams drift into undocumented local workarounds.
