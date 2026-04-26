# 0007. Add Developer Experience As A First-Class Principle

Status: Accepted  
Decision date: 2026-04-27  
Recorded date: 2026-04-27  
Retrospective: No

## Context

The public benchmark gap analysis identified developer experience as present but too quiet: SPACE was referenced, onboarding and discoverability existed, but there was no named principle or scorecard for **time-to-first-change**, **local loop**, **docs findability**, **review flow**, or **cognitive load**.

Evidence:

- `doctrine/evolution/public-doctrine-benchmark-gap-analysis-2026-04.md` listed the gap explicitly.
- External sources used for the new doctrine include SPACE, DORA 2024, CNCF Platform Engineering Maturity Model, and Google Engineering Practices.

## Decision

Add developer experience as a first-class doctrine principle and add a scorecard checklist:

- `doctrine/principles/developer-experience.md`
- `doctrine/checklists/developer-experience-scorecard.md`

Developer experience is defined as the usability of the engineering system, not individual productivity scoring.

## Consequences

- Doctrine now has explicit language for safe small changes, fast local feedback, findable docs, low cognitive load, and timely review.
- Adoption and repo-readiness reviews can score developer experience directly.
- DORA and SPACE remain measurement framing; the new principle states operating expectations.
- Future platform/golden-path guidance should treat DevEx as an outcome, not only a convenience.
