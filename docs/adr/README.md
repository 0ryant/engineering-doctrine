# Architecture Decision Records

This directory records decisions about the **engineering-doctrine** library itself.

## Honesty Rule For Retrospective ADRs

Some ADRs were reconstructed from git history after the decision had already been made.
Those files include:

- `Decision date` — when the repository history shows the decision landed.
- `Recorded date` — when the ADR was written.
- `Retrospective: Yes` — a reminder that the ADR is evidence-based reconstruction, not proof the decision was documented at the time.
- `Evidence` — commit hashes, file paths, or council notes that support the reconstruction.

Do not rewrite retrospective ADRs to make the process look cleaner than it was.

## Index

| ADR | Status | Decision date | Topic |
| --- | --- | --- | --- |
| [0001](0001-establish-versioned-engineering-doctrine-library.md) | Accepted (retrospective) | 2026-04-04 | Establish a versioned engineering-doctrine library |
| [0002](0002-adopt-trunk-workflow-and-cloudevents-as-portable-defaults.md) | Accepted (retrospective) | 2026-04-07 | Adopt trunk workflow and CloudEvents as portable defaults |
| [0003](0003-split-doctrine-into-principles-patterns-tooling-checklists-and-evolution.md) | Accepted (retrospective) | 2026-04-07 | Split doctrine into durable layers |
| [0004](0004-add-navigation-references-glossary-and-evolution-tracking.md) | Accepted (retrospective) | 2026-04-10 | Add navigation, references, glossary, and evolution tracking |
| [0005](0005-treat-ai-ml-rag-and-agentic-workflows-as-first-class-governed-systems.md) | Accepted (retrospective) | 2026-04-10 | Treat AI/ML, RAG, and agentic workflows as governed systems |
| [0006](0006-add-governance-and-assurance-navigation-and-adopt-adrs.md) | Accepted | 2026-04-26 | Add Governance & Assurance navigation and adopt ADRs |
| [0007](0007-add-developer-experience-as-a-first-class-principle.md) | Accepted | 2026-04-27 | Add Developer Experience as a first-class principle |
| [0008](0008-add-code-review-and-change-approval-pattern.md) | Accepted | 2026-04-27 | Add code review and change approval pattern (DevOps-native) |
| [0009](0009-add-gitops-and-declarative-operations-pattern.md) | Accepted | 2026-04-27 | Add GitOps and declarative operations pattern |
| [0010](0010-record-mythos-era-vulnerability-storm-research-and-doctrine-gaps.md) | Accepted | 2026-04-28 | Record Mythos-era / AI vulnerability storm research; **G1–G6 closed** in corpus (2026-04-28 synthesis) |
| [0011](0011-add-semantic-index-for-agent-ingestion-and-topic-routing.md) | Accepted | 2026-05-09 | Add semantic index for agent ingestion and topic routing |
| [0012](0012-model-routing-policy.md) | Proposed | 2026-05-20 | Model routing policy v1 contract — 3-tier (premium/default/narrow_scope) + empirical refusal rules + escalation + cost ceilings |
| [0019](0019-auto-cortex-promotion-with-per-session-opt-in.md) | Proposed | 2026-05-20 | Auto-Cortex promotion of new auto-memories (per-session opt-in) |
| [0021](0021-audit-as-discipline-applies-to-runner-itself.md) | Proposed | 2026-05-20 | Audit-as-discipline applies to the runner itself |
| [0022](0022-hash-function-convergence-blake3-ed25519-hmac.md) | Proposed | 2026-05-20 | Hash function convergence: BLAKE3 (content) + Ed25519 (signatures) + HMAC (MAC) |
| [0023](0023-add-ai-adoption-control-coverage-inventory-challenge-testing-continuity-literacy.md) | Accepted | 2026-07-16 | Add AI adoption-control coverage: inventory & materiality, independent challenge, harm-surface testing, provider continuity, literacy |
| [0024](0024-adopt-a-doctrine-grounded-ai-native-software-development-lifecycle.md) | Accepted | 2026-07-17 | Adopt an objective-to-outcome, evidence-backed AI-native SDLC with explicit authority, layered verification, deterministic enactment, and runtime reconciliation |
| [0025](0025-restore-apache-2.0-as-project-license.md) | Accepted | 2026-07-17 | Restore Apache-2.0 as the adoption-first project licence and supersede the AGPL default-branch experiment |

## Candidate Considered But Not Recorded

Commit `8a32a6b` (`2026-04-10`, "Doctrine: concrete defaults, rationale tables, split multi-topic sections") was reviewed and **not** given a standalone ADR. It appears to be a broad refinement of already accepted doctrine mechanics rather than a distinct architectural fork. Its substance is covered by ADR 0003 and ADR 0004.
