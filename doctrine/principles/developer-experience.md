# Developer Experience

Durable rules for **developer experience**: reducing friction so engineers can make **safe, small, observable changes** without relying on oral tradition, heroic local setup, or hidden queues. Developer experience is not developer happiness theatre; it is the usability of the engineering system.

---

## 1. Time-To-First-Change Is A Product Signal

- A competent new contributor should be able to **clone**, understand purpose and ownership, run the local quality gate, and make a **safe small change** using documented paths.
- Repos should name the day-one route: setup, test, local run or preview, review, and release expectations.
- If a repo cannot support a quick first change, record the blocker: missing bootstrap, unclear ownership, missing fixtures, expensive credentials, or brittle local dependencies.

**Why:** Documentation and onboarding fail most often at **navigation** and hidden prerequisites, not at the absence of long-form reference material. DORA 2024 also treats documentation quality and developer independence as meaningful contributors to productivity and well-being.

---

## 2. The Local Loop Is A First-Class Interface

- The **local loop** includes setup, edit, fast validation, focused test, preview, and commit-ready checks.
- Mandatory CI gates should have local equivalents or a documented reason they are CI-only.
- Setup scripts must be **idempotent** and should fail with actionable messages, not stack traces that require maintainer interpretation.
- Slow full gates are acceptable when paired with a **fast inner loop** that catches common mistakes before review.

**Why:** Slow or mysterious local feedback increases batch size, review latency, and bypass pressure. Good local loops protect both velocity and control integrity.

---

## 3. Documentation Must Be Findable, Current, And Task-Shaped

- Put the **first answer** near the repo entry point: what this is, who owns it, how to change it, how to verify it, and where deeper docs live.
- Keep task-shaped docs separate from encyclopaedic reference. A contributor looking for “how do I ship a safe change?” should not have to read the whole doctrine tree.
- Stale docs are defects. When behaviour, commands, ownership, or contracts change, update docs in the same change or record a follow-up owner and date.

**Why:** DORA 2024 defines useful internal documentation in terms of reliability, findability, updatedness, and support. Good docs reduce cognitive load; bad docs amplify it.

---

## 4. Cognitive Load Is A Design Constraint

- Prefer **one obvious path** for routine work: setup, check, test, review, release, rollback.
- Hide accidental complexity behind scripts, templates, or golden paths; keep escape hatches explicit for unusual work.
- Use naming, file layout, generated indexes, and examples to make boundaries discoverable.
- Do not make every contributor understand every platform detail before making ordinary product changes.

**Why:** CNCF platform-engineering guidance frames self-service and golden paths as ways to reduce cognitive load while preserving higher-quality supporting services. Cognitive load is not softness; it is a capacity limit.

---

## 5. Reviews Optimise Team Flow, Not Individual Busyness

- Prefer small, focused changes with tests or evidence appropriate to the risk.
- Reviewers should respond quickly enough that authors can take useful next action, even if the first response is “split this,” “wrong reviewer,” or “I can review by tomorrow.”
- Authors should make review easy: explain intent, call out risks, separate refactors from behaviour changes, and include verification.
- Fast review does not mean weak review. Review standards stay high; unnecessary waiting is the waste.

**Why:** Google’s public engineering practices emphasise small changes and fast review response because they improve team throughput without sacrificing code health.

---

## 6. Measure The System, Not Individual Worth

- Track developer experience at the **team or repo-system** level, not as individual productivity scoring.
- Use a balanced scorecard: time-to-first-change, local-loop time, review response time, documentation findability, cognitive load, interrupted work, and satisfaction/well-being.
- Pair behavioural data with qualitative feedback. A metric without developer interviews often misreads the cause.
- Avoid single-number productivity targets such as lines of code, commit counts, ticket counts, or “utilisation.”

**Why:** SPACE shows developer productivity is multidimensional: satisfaction and well-being, performance, activity, communication and collaboration, and efficiency and flow. Single-metric productivity programmes create perverse incentives.

---

## 7. Developer Experience And Controls Are Not Opposites

- Security, compliance, and reliability controls should be shaped as **paved roads** where possible: discoverable, local-previewable, automated, and explainable.
- A control that blocks work should explain the failure, owner, remediation path, and exception path.
- Repeated exceptions are product feedback about the control or platform, not only team non-compliance.

**Why:** The best controls reduce unsafe variation while preserving independence. If governance makes the safe path slower than the unsafe path, teams will route around it.

---

## Scorecard Dimensions

Use [../checklists/developer-experience-scorecard.md](../checklists/developer-experience-scorecard.md) for a reviewable scorecard. Minimum dimensions:

| Dimension | Healthy signal |
| --- | --- |
| Time-to-first-change | New contributor can make a safe small change without maintainer hand-holding |
| Local loop | Fast check catches ordinary mistakes before PR |
| Docs findability | Entry docs answer ownership, setup, verification, and deeper links |
| Review latency | Authors get timely, actionable response |
| Cognitive load | Routine work follows a named path; exceptions are explicit |
| Developer feedback | Team-level survey/interview signal is reviewed alongside DORA metrics |

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Name DevEx as a principle | Prevents “controls first” doctrine from ignoring the human system that actually ships change. |
| Score teams/systems, not people | Aligns with SPACE and avoids productivity theatre. |
| Keep in principles | The invariant is durable; tools for portals, surveys, templates, and dashboards belong in tooling or estates. |
| Pair with DORA | DORA describes delivery outcomes; DevEx explains part of the system that creates or blocks those outcomes. |

---

## References

- ACM Queue — **The SPACE of Developer Productivity** (Forsgren et al.): https://queue.acm.org/detail.cfm?id=3454124  
- Communications of the ACM — **The SPACE of Developer Productivity**: https://cacm.acm.org/practice/the-space-of-developer-productivity/  
- DORA — **Accelerate State of DevOps Report 2024**: https://dora.dev/research/2024/dora-report  
- CNCF TAG App Delivery — **Platform Engineering Maturity Model**: https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model  
- Google Engineering Practices — **Small CLs**: https://google.github.io/eng-practices/review/developer/small-cls.html  
- Google Engineering Practices — **Speed of Code Reviews**: https://google.github.io/eng-practices/review/reviewer/speed.html  
- *Software Engineering at Google*, Chapter 9 — Code Review: https://abseil.io/resources/swe-book/html/ch09.html  
