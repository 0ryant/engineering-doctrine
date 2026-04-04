# Collaboration Principles

Engineering is a team sport. Collaboration doctrine exists to reduce coordination drag, improve decision quality, and keep delivery sustainable.

---

## 1. Default To Clarity

- Prefer communication that leaves an artifact others can refer back to.
- Write decisions, assumptions, and open questions down.
- Ambiguity should be reduced early, not discovered during implementation.

## 2. Work In Public

- Use issues, pull requests, ADRs, and docs to make engineering work legible.
- Important technical decisions should not live only in chat or meetings.
- If a decision changes system behavior, ownership, interfaces, or operational burden, record it.

## 3. Review Is A Shared Responsibility

- Authors are responsible for making changes easy to review.
- Reviewers are responsible for responding promptly and giving actionable feedback.
- Reviews should focus on correctness, maintainability, operability, and clarity, not personal style preferences already covered by automation.

## 4. Prefer Small, Reviewable Changes

- Small changes reduce review latency and integration risk.
- If a change is large, stage it behind flags, interfaces, or preparatory refactors.
- Large unreviewable changes are a process failure, not a badge of productivity.

## 5. Resolve Disagreement Explicitly

- Surface tradeoffs.
- Prefer documented decisions over recurring debate.
- Escalate when needed, but make the reasoning visible so the same argument does not repeat.

## 6. Collaborate Across Functions Early

- Engineering, product, design, security, and operations should align on changes before they become expensive.
- Pulling in the right partner early is cheaper than late-stage rework.

## 7. Use Synchronous Time Intentionally

- Use meetings for ambiguity reduction, decision-making, and rapid problem solving.
- Use async channels for status, documentation, proposals, and review where latency is acceptable.
- Meeting outcomes should be captured in writing.

## 8. Improve The System, Not Just The Change

- Leave docs, tests, scripts, and interfaces better than you found them where practical.
- When repeated friction appears, fix the process or tooling, not just the immediate instance.
