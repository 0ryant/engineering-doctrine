# Git Hooks And Worktrees Implementation Composition

Recorded: 2026-11-15. Repository basis: `54fd5f39383c081fc62b3ccbae44735069e31201` and the companion change.

## Question

Can local Git hooks and linked worktrees each get a short activity reference without creating doctrine, and without turning Git mechanics into authority?

The additions are [Local Checks With Git Hooks](../impl/git-hooks.md) and [Parallel Work In Git Worktrees](../impl/git-worktrees.md), requested by the maintainer. Both are governed by [ADR 0048](../../docs/adr/0048-add-implementation-reference-layer.md); neither appears in the [screened backlog](research-implementation-reference-layer-2026-09.md#screened-backlog), so this note supplies their screen.

## Layer Fit

The layer contract asks references to stay product-neutral. Both pages name Git because the library already assumes Git as its version-control baseline: trunk, topic branches, and worktrees appear in the existing [Branching And Integration](../impl/branching-and-integration.md) reference and the [collaboration tooling](../tooling/collaboration.md). The pages describe Git's documented behaviour and the operating shape around it. Commands and hook managers stay in tooling, and no hosting product, hook framework, or scanner is named. Other version-control systems with equivalent mechanisms can follow the same shape.

Both pages are named for an activity in their titles. The file names keep the mechanism (`git-hooks.md`, `git-worktrees.md`) because that is what engineers search for.

## Owner Audit: Git Hooks

| Reference material | Existing authority | Scope preserved |
| --- | --- | --- |
| Hooks are feedback, not merge enforcement | [Merge path](../principles/merge-path-evidence-and-pipeline-integrity.md) §2 invariant 1 | "Local-only scripts do not satisfy merge enforcement." |
| Same versioned scripts as CI; one documented gate command; idempotent setup | [Build](../principles/build.md) §§1–3 | Unchanged. |
| Fast inner loop; local equivalents of CI gates; bypass pressure | [Developer experience](../principles/developer-experience.md) §§1–2 | Slow full gates stay acceptable when paired with a fast inner loop. |
| Fast pre-push, full pre-merge, full gate on CI always | [Adoption playbook](../patterns/adoption-playbook.md) §8 | Troubleshooting guidance, not a mandate. |
| Same pinned tool versions | Build §3 (mirror CI semantics); [Dependencies](../principles/dependencies-supply-chain.md) §1 rationale | Composed: the pages say local and CI should mean the same thing, not that dev tooling falls under production pinning rules. |
| Secret scanning early and before merge; rotation after exposure | Build §10; [Configuration and secrets](../principles/configuration-and-secrets.md) §§2, 4 | Pre-commit scanning is an addition to, not a replacement for, the pre-merge scan. |
| Method-record trailer checks | [Code review](../patterns/code-review-and-change-approval.md) §6.1 | Transport stays an estate binding. |
| Agents face the same gates | [AI and ML-assisted systems](../principles/ai-ml-systems.md) §4; collaboration readiness | Hooks are described as early feedback for agents, not as a required control. |

Removed during the audit: a draft invariant said agents "run the same hooks". No owner requires that; the final text says agent changes face the same required checks, and hooks give them the same early feedback.

## Owner Audit: Git Worktrees

| Reference material | Existing authority | Scope preserved |
| --- | --- | --- |
| Short-lived branch from trunk; one reviewable change | [Collaboration](../principles/collaboration.md); [Trunk workflow](../patterns/trunk-workflow.md) | Unchanged. |
| One writer per mutable workspace; immutable inputs; attenuated authority; named integration | [Agentic loop design](../patterns/agentic-loop-design.md) §8.3 | Applies to parallel agents; the reference does not extend it to every human workflow as a rule. |
| Isolated workspace for agent candidates; no protected-branch mutation | [AI-native SDLC](../patterns/ai-native-software-development-lifecycle.md) §§3, 10 | Unchanged. |
| Local gate and idempotent setup per workspace | Build §3; Developer experience §2 | Unchanged. |
| Same review and required checks | Merge path §2 invariant 1; Collaboration | Worktrees create no authority. |
| Credentials and shared resources are not isolated | [Zero trust](../principles/zero-trust-and-workload-identity.md) §§2, 2.1; collaboration tooling | Per-task agent credentials remain a §2.1 SHOULD for agents holding their own identity. |
| Hotfix from the release tag, merged back | Trunk workflow | A draft also said "or from trunk"; removed because the owning pattern names the tag. |

## Git Behaviour Relied On

Both checked on the publisher's manual pages on 2026-11-15. Class S5, product-scoped primary documentation, authoritative for Git behaviour only.

| Source | Version | Behaviour used |
| --- | --- | --- |
| [githooks manual](https://git-scm.com/docs/githooks) | Last changed in 2.54.0; unchanged through 2.56.1 | Default hooks directory is `$GIT_DIR/hooks`; `core.hooksPath` changes it; pre-commit and commit-msg can be bypassed with `--no-verify`; a failing pre-push aborts the push |
| [git-worktree manual](https://git-scm.com/docs/git-worktree) | Last changed in 2.56.0 | Linked worktrees share everything except per-worktree files such as `HEAD` and the index; refs under `refs/` are shared; a branch already checked out elsewhere is refused by default; `remove`, `prune`, and `lock` behaviour; optional per-worktree configuration |

The manual does not say whether `--no-verify` skips pre-push, and the reference does not claim it. The existing tooling citation pins the worktree manual at 2.54.0; the behaviours used here are unchanged in that version.

## Compression Test

| Reference | Owners composed | Why one owner is not enough |
| --- | --- | --- |
| Git hooks | 10 | Merge path says hooks are not enforcement; build and developer experience say what local feedback is for; the playbook splits pre-push from pre-merge; secrets, pinning, and agent rules live elsewhere. |
| Git worktrees | 9 | Collaboration owns the branch lifecycle; agent workspace rules live in two AI patterns; credential isolation lives in zero trust. None describes the local mechanics that let them coexist. |

Each deletes cleanly: removing either page removes no obligation. Both stay near the 1,000-word range.

## Consumer Impact

Change class: **additive guidance / navigation**. A tooling illustration for version-controlled hooks is added beside the existing worktree commands. No obligation, exception, or enforcement setting changes.

## Residual Risk

Git behaviour can change between releases; the version notes above record what was checked. The pages are model-reviewed against their owners, with no independent human review. Hook managers and agent sandboxes evolve quickly, which is why both stay in tooling.
