# 0008. Add Code Review And Change Approval Pattern

Status: Accepted  
Decision date: 2026-04-27  
Recorded date: 2026-04-27  
Retrospective: No

## Context

[Collaboration.md](../../doctrine/principles/collaboration.md) already defines trunk, branch protection, PR sizing, and a one-line review-latency expectation. The public [anti-patterns gap analysis](../../doctrine/evolution/anti-patterns-and-failure-modes-gap-analysis-2026-04.md) called out **review economics** and **reviewer/author failure modes** as a thin area. Teams need a **portable pattern** for:

- author vs reviewer **duties**,
- **blocker** vs **non-blocker** comments,
- **review latency** targets (as examples, estate-tunable),
- **high-risk** change classes (security, infra, schema, API),
- **agent-authored** / LLM-sourced diffs, and
- **escalation** when review stalls or disagreement is sharp,

without defaulting to ITIL **Change Advisory** ceremony for normal software work.

## Decision

Add [doctrine/patterns/code-review-and-change-approval.md](../../doctrine/patterns/code-review-and-change-approval.md) as **additive guidance** in `patterns/`, cross-linked from collaboration and navigation indexes.

## Consequences

- Review expectations are easier to find and cite than from collaboration alone.
- The pattern explicitly rejects CAB-for-every-deploy while allowing proportional scrutiny for high-risk change.
- Future edits should follow [doctrine-library-change-harness.md](../../doctrine/patterns/doctrine-library-change-harness.md): navigation (sitemap, glossary, REFERENCES), and ADR index update (this file).

## Evidence

- Working tree: new pattern file; ADR 0008; index and reference updates in the same change.
