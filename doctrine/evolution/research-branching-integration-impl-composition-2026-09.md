# Branching And Integration Implementation Composition

Recorded: 2026-09-19. Repository basis: `1c5c59a01a6214f3a9287a63ce2a2ebce8666a8f` and the companion change.

## Question

Can an engineer choose a workspace, branch base, integration target, and release path without reconstructing the model from several doctrine files?

The supplied branching discussion is proposal material, not authority. The addition is [Branching And Integration](../impl/branching-and-integration.md), an activity reference governed by [ADR 0048](../../docs/adr/0048-add-implementation-reference-layer.md). [ADR 0002](../../docs/adr/0002-adopt-trunk-workflow-and-cloudevents-as-portable-defaults.md) already establishes trunk as the default. Neither decision needs replacement.

## Evidence Boundary

The reference composes existing owners. External material below checks terminology, contextual limits, and optional Git mechanics; it introduces no control and does not re-admit the existing trunk policy at a stronger level.

“Trunk is superior in every way” is not adopted. Branch strategy, artefact promotion, release cadence, and deployed-state evidence are different concerns. A branch-heavy workflow can still promote an unchanged artefact; a trunk workflow can still rebuild incorrectly for production.

## Owner Audit

| Reference material | Existing authority | Scope preserved |
| --- | --- | --- |
| Trunk, short-lived branches, small PRs | [Collaboration](../principles/collaboration.md) §§1–3; [Trunk Workflow](../patterns/trunk-workflow.md) | Days, not weeks; existing PR guidance and exceptions. No new branch count or hours limit. |
| Protected review and merge checks | Collaboration §2; [Merge Path Evidence](../principles/merge-path-evidence-and-pipeline-integrity.md) §2; [Code Review](../patterns/code-review-and-change-approval.md) | Local hooks cannot replace server-enforced gates. Existing bot and emergency paths remain. |
| Local feedback and optional workspaces | [Build](../principles/build.md) §§2–3; [Developer Experience](../principles/developer-experience.md) §§1–4 | Discoverable local loop. Worktrees, clones, and prefixes are illustrations, not obligations. |
| Revision, candidate, and environment state | Build §§4–5, 12; Collaboration §§6–7; [Authoritative Sources](../principles/single-source-of-truth.md) §§1–2 | Authority is per concept, not one global branch for every state. Multiple deployable units remain possible. |
| Incomplete features | Collaboration §4; Trunk Workflow; [Feature Flag Governance](../patterns/feature-flag-governance.md); [Data And Migrations](../principles/data-and-migrations.md) | Compatible increments and applicable flag lifecycle; flags do not erase stateful migration risk. |
| Hotfixes and support lines | Trunk Workflow, release metadata and LTS sections; Collaboration §§1–2 | Tag-first hotfix, patch, merge back to main; documented support EOL and security/legal exception authority. |
| Environment layouts and IaC | [GitOps](../patterns/gitops-and-declarative-operations.md) §§4–5; Build | Paths, overlays, or desired-state branches remain legitimate; environment-specific plans are not universally promotable binaries. |
| Adoption | [Adoption Playbook](../patterns/adoption-playbook.md) §§3, 5 | Quality-gate-first pilot; no branch-deletion programme. |

The collaboration principle's phrase “source of truth for what ships” is clarified to identify active integration state. Its existing build and promotion rules already distinguish that state from a deployed candidate. The clarification changes no release, review, or support obligation.

## Compression Test

The trunk pattern supplies integration mechanics and exceptions; build supplies candidate identity and deployable surfaces; source-of-truth supplies per-concept authority; GitOps supplies desired-versus-observed state. None alone answers the workspace-to-deployment identity question.

The reference keeps one flow, a daily sequence, and a concept table. It routes full delivery and test placement to the existing sibling references. Removing it would remove no obligation. Commands and naming examples stay in tooling; strategy comparisons stay out of the onboarding page.

## Source Limits

- DORA supports frequent integration and small batches in its delivery-performance guidance. This is research-program guidance, not universal causal proof. Its numerical goals, direct-push discussion, and synchronous-review preference do not replace this repository's branch, protection, or async-collaboration policies.
- Vincent Driessen's 2020 reflection recommends a simpler flow for continuous delivery and retains context for versioned products supporting multiple installed versions. That is the model author's contextual advice, not comparative experimental evidence.
- The trunk-based-development practitioner guide accommodates release branches but generally prefers fixing trunk first and backporting. This library's owning pattern says to branch from the release tag and merge the patch back. The difference is recorded, not silently resolved through an `impl/` summary.
- Git's manual supports multiple working trees and their shared repository data. It does not establish which branching strategy performs best or make worktrees a credential sandbox.

## Source Ledger

All four primary publisher pages were retrieved and the relevant passages checked on 2026-09-19. Classes follow [Source Authority And Evidence Grading](../patterns/source-authority-and-evidence-grading.md), separately from claim support. These are contextual/illustrative citations, not new typed obligations.

| Source | Class, scope, and role | Pin and verification |
| --- | --- | --- |
| [DORA: Trunk-Based Development](https://dora.dev/capabilities/trunk-based-development/) | S4 research-program guidance; primary for DORA's stated practices and analysis summary. | Retrieved HTML capture pinned by SHA-256 below; relevant guidance and its cited report years inspected, underlying datasets not reanalysed. |
| [Driessen: A Successful Git Branching Model](https://nvie.com/posts/a-successful-git-branching-model/) | S6 named practitioner; primary for his model and reflection. | 2010 article with 2020-03-05 reflection; retrieved HTML capture pinned by SHA-256 below. Reflection and model checked. |
| [Trunk Based Development: Branch For Release](https://trunkbaseddevelopment.com/branch-for-release/) | S6 named practitioner writing; primary for the presented workflow, secondary as general advice. | Page reports published SHA `742e4124d06f2b74c1496ffd8bfee7a4346864f0`; retrieved HTML capture pinned below. Release and fix-direction passages checked. |
| [Git: Worktree Manual](https://git-scm.com/docs/git-worktree/2.54.0) | S5 product-scoped primary; authoritative for Git worktree behaviour only. | Version 2.54.0; description, `add -b`, and `list` inspected. Latest manual page reports 2.55.0 has no changes to this manual. |

Capture hashes (SHA-256 of downloaded HTML bytes):

```text
DORA      5652a26a93bb55acf8e715be8a8bc6ef3c2abd4a11eafaad18e5975203014f04
Driessen  d2b8ec7691b7f5576af81284de5cfd925fe5ecff95476d16c1522fcd0e51003f
TBD       620a7f423be79fb6d7683f6964e8cf7d786fa0f85c2bb03c06d3c68391df9c5d
Git       4a610af6002ac15deb902bebbc00184156366d63d5a8145dbba4ffe79064ab07
```

Archive status: local admission captures retained; no public archival URL was established. The hashes identify the admitted bytes but do not make them publicly retrievable. Access dates alone are not revision pins. No withdrawal notice was observed on the retrieved pages; that is not a comprehensive publisher-status audit. Review these contextual citations when the reference or tooling examples change, or a source event is discovered, through the normal library lifecycle.

## Consumer Impact

Change classes: **additive guidance / navigation**, plus **editorial clarification** of integration versus deployed state. No new obligation, exception change, migration, enforcement setting, or release is introduced. ADR 0002 and ADR 0048 cover the existing decisions.

Review cases are an ordinary service with concurrent contributors; a supported older release; an urgent patch while main is ahead; a GitOps desired-state repository; environment-specific IaC; and developers using clones or different prefixes. In each case, applicability stays with the named owners. Checklists, glossary, and the doctrine's compact core require no new rule or term.

## Residual Risk

Summaries can drift or make exceptional support look routine. Owner links, explicit scope, and the no-new-doctrine test address that risk but cannot eliminate it mechanically. A future change to hotfix direction belongs in its canonical owner with consumer-impact review, not in this reference. Public archive availability remains a citation-durability limitation.
