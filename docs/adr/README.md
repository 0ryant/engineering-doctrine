# Architecture Decision Records

This directory records decisions about the **engineering-doctrine** library itself.

## Honesty Rule For Retrospective ADRs

Some ADRs were reconstructed from git history after the decision had already been made.
Those files include:

- `Decision date` — when the repository history shows the decision landed.
- `Recorded date` — when the ADR was written.
- `Retrospective: Yes` — a reminder that the ADR is evidence-based reconstruction, not proof the decision was documented at the time.
- `Evidence` — commit hashes, file paths, or contemporaneous decision records that support the reconstruction.

Do not rewrite retrospective ADRs to make the process look cleaner than it was.

## Status Vocabulary

Beyond `Proposed`, `Accepted`, and `Rejected`, two exit statuses are defined:

- **Superseded** — a later ADR replaced this decision. The superseded ADR's status line reads `Superseded by [ADR NNNN](path)` and the superseding ADR names what it supersedes; both directions are required. A decision disavowed without a successor is reversed the same way — the reversing ADR supersedes it and records the disavowal. Amendment-in-place remains correct for refinements that do not reverse a decision.
- **Withdrawn** — a terminal, proposer-initiated exit for a Proposed ADR that will not proceed; distinct from Rejected (a considered refusal). A Proposed ADR older than 90 days receives a recorded accept/reject/withdraw decision at the next lifecycle sweep ([doctrine-content-lifecycle.md](../../doctrine/patterns/doctrine-content-lifecycle.md) §7).

Numbers 0013–0020 were never assigned in any reachable history; the gap is recorded here so it is not misread as deleted decisions.

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
| [0012](0012-model-routing-policy.md) | Accepted | 2026-05-20 | Portable model-routing contract: evidence-bound tiers, escalation, refusal, review, and cost ceilings |
| [0021](0021-audit-as-discipline-applies-to-runner-itself.md) | Proposed | 2026-05-20 | Verification discipline applies recursively to measurement runners |
| [0022](0022-hash-function-convergence-blake3-ed25519-hmac.md) | Rejected | 2026-05-20 | Reject a fixed portable cryptographic algorithm menu; use maintained applicable profiles |
| [0023](0023-add-ai-adoption-control-coverage-inventory-challenge-testing-continuity-literacy.md) | Accepted | 2026-07-16 | Add AI adoption-control coverage: inventory & materiality, independent challenge, harm-surface testing, provider continuity, literacy |
| [0024](0024-adopt-a-doctrine-grounded-ai-native-software-development-lifecycle.md) | Accepted (amended by 0030) | 2026-07-17 | Adopt the evidence-and-authority kernel for an AI-native SDLC; operating model refined by ADR 0030 |
| [0025](0025-restore-apache-2.0-as-project-license.md) | Accepted | 2026-07-17 | Restore Apache-2.0 as the adoption-first project licence and supersede the AGPL default-branch experiment |
| [0026](0026-adopt-revision-pinned-external-control-profiles.md) | Accepted | 2026-07-17 | Adopt revision-pinned external control profiles; use NIST SP 800-171 as the worked CUI profile without making it a universal baseline |
| [0027](0027-keep-public-doctrine-implementation-neutral.md) | Accepted | 2026-07-17 | Keep publishable doctrine implementation-neutral and remove organisation-private product names and local work records |
| [0028](0028-adopt-claim-level-authority-applicability-and-exceptions.md) | Accepted | 2026-07-17 | Adopt claim-level normative strength, composable applicability, bounded exceptions, and control lifecycle |
| [0029](0029-adopt-a-compact-non-duplicative-core-constitution.md) | Accepted | 2026-07-17 | Rebuild the umbrella as a compact core constitution and route map |
| [0030](0030-refine-ai-native-sdlc-into-gates-records-and-applicability-overlays.md) | Accepted | 2026-07-17 | Refine AI-native delivery into seven gates, five record families, governed execution, typed claims, and three closure modes |
| [0031](0031-add-agent-identity-mcp-revision-pinning-and-asi-crosswalk-coverage.md) | Accepted | 2026-08-03 | Add first-class agent identity (§2.1), a revision-pinned MCP baseline, and the ASI01–ASI10 crosswalk — closes gap-audit items G1, S1, S2 |
| [0032](0032-add-ai-act-transparency-slopsquatting-gate-and-model-dataset-admission.md) | Accepted | 2026-08-03 | Add profile-gated EU AI Act Art 50 transparency (§5.4), the slopsquatting pre-install gate, and model/dataset admission (§8); amends ADR 0031 with the tiered agent-principal floor — closes gap-audit items G2, G3, G4 |
| [0033](0033-add-agentic-threat-vocabulary-agent-responders-and-genai-telemetry.md) | Accepted | 2026-08-03 | Add agentic threat vocabulary (§3.2), the agent-responder incident role (§10), and the GenAI per-call telemetry floor (§7) — closes gap-audit items G5, G6, G7 |
| [0034](0034-add-agent-definition-governance-memory-lifecycle-and-judge-discipline.md) | Accepted | 2026-08-03 | Add agent-definition artefacts to the pipeline trust class, the agent memory lifecycle, and load-bearing-judge discipline — closes gap-audit items G8, G9, G10 |
| [0035](0035-add-agent-financial-authority-adaptive-evaluation-and-spend-governance.md) | Accepted | 2026-08-03 | Add agent financial authority default-deny (§7.1), adaptive defence evaluation (§5/§9.4), and vendor-native spend governance — closes gap-audit items G11, S3, S4, S5; all high- and medium-severity audit findings now closed, with low-severity G12–G13 (rows 16–17) and crosswalk residues (rows 19–22) tracked open |
| [0036](0036-land-v050-correction-batch-from-the-corpus-review.md) | Accepted | 2026-08-03 | Land the v0.5.0 correction batch from the full-corpus review — B2/M20/M21 observability fix+move+typing, B1 interim FSM repair, M7–M9 schema-fact repairs, M15 umbrella-reference sweep, M3/M4/M6 checklist/inventory reconciliation |
| [0037](0037-land-mcp-cross-check-correction-batch.md) | Accepted | 2026-08-06 | Land the MCP cross-check correction batch — NSA CSI date, RC-vs-final URLs, auth-change enumeration, AAIF hedge resolution, CIMD precision, fixture grammar; establishes in-place correction of verified factual defects in research-note digest rows |
| [0038](0038-adopt-a-doctrine-content-lifecycle.md) | Accepted | 2026-08-06 | Adopt a doctrine content lifecycle — status vocabulary with three exit states, promotion gates, ADR-routed demotion/supersession/restoration, the DEPRECATED.md register, checklist-wired staleness sweep and default-fade; Superseded/Withdrawn ADR statuses |
| [0039](0039-add-agent-loop-graph-decomposition-guidance.md) | Accepted | 2026-08-07 | Add graph-decomposition guidance (§8.4 fan-out/converge with converge-as-verification-point), the §6.1 build-order ladder with split enforcement MUSTs, loop economics, recurrence-gates-promotion, agent/graph glossary entries, and a lifecycle-compliant run-contracts v2 DAG deferral |
| [0040](0040-adopt-source-authority-classes-and-evidence-weighted-citations.md) | Accepted | 2026-08-12 | Adopt source-authority classes and evidence-weighted citations — S1–S7+X × C1–C4 two-axis scheme with the conformance/empirical split, BCP-14 admission floors, citation metadata with admission-time archiving, sweep-anchored source-event reviews, the EVIDENCE-EXCEPTIONS register, and forward-only adoption with a sweep-routed back-catalogue |
| [0043](0043-replace-agent-coauthorship-disclosure-with-a-method-record.md) | Accepted | 2026-08-16 | Replace agent co-authorship disclosure with a method record — a tool MUST NOT be named in an authorship field; §6 row 1's duty is preserved and its instrument replaced by a class-graded (`generated`/`curated`/`authored`), revision-pinned record of how the candidate was produced. Numbers 0041–0042 are reserved for routed-but-unlanded work |

## Candidate Considered But Not Recorded

Commit `8a32a6b` (`2026-04-10`, "Doctrine: concrete defaults, rationale tables, split multi-topic sections") was reviewed and **not** given a standalone ADR. It appears to be a broad refinement of already accepted doctrine mechanics rather than a distinct architectural fork. Its substance is covered by ADR 0003 and ADR 0004.
