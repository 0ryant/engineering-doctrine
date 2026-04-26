# Anti-Patterns And Failure Modes Gap Analysis

**Date:** 2026-04-27.  
**Question:** What public engineering handbooks, standards, and reliability/security sources say about how engineering systems fail—and where this portable doctrine is still too quiet or too scattered.

---

## Method

Compared this repository against public sources that explicitly describe **failure modes**, **anti-patterns**, **pitfalls**, or **things to avoid**:

- Public handbooks/playbooks: Google Engineering Practices, Google SRE, GitLab Engineering Handbook, Microsoft ISE Code-With Engineering Playbook, 18F de-risking and agile contracting material, thoughtbot playbook/guides, GOV.UK Technology Code of Practice, Trussworks Engineering Playbook.
- Standards/research: DORA, SPACE, SLSA, OpenSSF Scorecard, OWASP API Top 10, OWASP LLM Top 10, NIST SSDF, NIST Privacy Framework, CNCF Platform Engineering Maturity Model, Twelve-Factor App, PagerDuty and Atlassian postmortem guidance.
- Local doctrine scan: all Markdown under `doctrine/`, with emphasis on `anti-pattern`, `failure mode`, `footgun`, `pitfall`, `avoid`, `risk`, `drift`, `toil`, `lock-in`, `incident`, `support`, `AI`, and `supply chain`.

**Source verification note:** Most URLs cited below were verified with WebFetch. Some 18F and GOV.UK pages blocked direct fetch from the research environment or returned transient errors; their URLs and relevant snippets were cross-checked with WebSearch results. Treat source-specific wording here as synthesis, not a quoted control catalogue.

---

## Source Signals

| Source | Failure modes / anti-patterns emphasized |
| --- | --- |
| [Google Engineering Practices](https://google.github.io/eng-practices/review/reviewer/standard.html) | Code health erodes through small shortcuts; review nitpicks block progress; unresolved review conflicts stall; emergency merges can degrade code health. |
| [Google SRE: Eliminating Toil](https://sre.google/sre-book/eliminating-toil/) and [Dealing With Interrupts](https://sre.google/sre-book/dealing-with-interrupts/) | Manual, repetitive, automatable, tactical work consumes engineering capacity; interrupts and on-call load create burnout and prevent preventative engineering. |
| [Microsoft ISE Observability Pitfalls](https://microsoft.github.io/code-with-engineering-playbook/observability/pitfalls/) | Observability as afterthought; metric fatigue; context-poor logs; PII leakage. |
| [Microsoft ISE Reviewer Guidance](https://microsoft.github.io/code-with-engineering-playbook/code-reviews/process-guidance/reviewer-guidance/) | Reviewers not understanding code; scope creep in reviews; ego battles; tests promised "later"; complex methods and excessive arguments. |
| [GitLab AI Operating Principles](https://handbook.gitlab.com/handbook/engineering/ai/operating-principles/) | Single-review merges, pressure to approve, silent uncertainty, merging AI-generated code the author cannot explain, speed overriding stability. |
| [18F Agile Contracting Anti-Patterns](https://18f.gsa.gov/2018/09/27/antipatterns-in-agile-contracting/) and [De-risking Guide](https://guides.18f.org/derisking-government-tech/software-solutions/) | Waterfall-shaped agile contracts, vendor-pool theatre, separate contracts per release, UMOTS, poor COTS-vs-custom decisions, vendor lock-in. |
| [GOV.UK Technology Code of Practice](https://www.gov.uk/guidance/the-technology-code-of-practice) and open standards guidance | Proprietary lock-in, weak open standards posture, legacy extension without exit plan, purchasing strategies that ignore contractual limitations. |
| [thoughtbot Code Smells](https://thoughtbot.com/ruby-science/code-smells.html) and [PR smell list](https://thoughtbot.com/blog/a-smelly-list) | Smells as review heuristics, not automatic bugs; fragile tests; hidden complexity; state mutation and unchecked persistence. |
| [Trussworks Engineering Playbook](https://github.com/trussworks/Engineering-Playbook) | Mutable infrastructure, oversized IaC roots, manual deployments, environment drift, ADRs without enforcement. |
| [SLSA supply-chain threats](https://slsa.dev/spec/v1.2/threats-overview) | Source tampering, compromised build platforms, malicious artifacts, typosquatting, package unavailability, missing provenance. |
| [OpenSSF Scorecard checks](https://github.com/ossf/scorecard/blob/main/docs/checks.md) | Missing branch protection, dangerous workflows, broad workflow token permissions, unpinned dependencies, unmaintained repos, known vulnerabilities. |
| [OWASP API Top 10](https://owasp.org/API-Security/editions/2023/en/0x11-t10/) | Broken object/function authorization, unrestricted resource consumption, SSRF, improper inventory, unsafe API consumption. |
| [OWASP LLM Top 10](https://genai.owasp.org/llm-top-10/) | Prompt injection, sensitive information disclosure, model/supply-chain risk, data poisoning, improper output handling, excessive agency, system prompt leakage, vector/embedding risks, misinformation, unbounded consumption. |
| [DORA metrics guide](https://dora.dev/guides/dora-metrics/) and SPACE | Metrics-as-goals, one metric to rule them all, cross-team comparisons, siloed ownership, measuring instead of improving, productivity theatre. |
| [PagerDuty postmortems](https://www.pagerduty.com/resources/learn/incident-postmortem/) and [Atlassian postmortems](https://www.atlassian.com/incident-management/postmortem) | No postmortem owner, delayed learning, skipped write-ups, blameful review, weak timelines, action items not fed back into planning. |
| [Twelve-Factor App](https://12factor.net/) | Config in code, weak process model, dev/prod divergence, logs not treated as streams, build/release/run confusion. |
| [CNCF Platform Engineering Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/) | Platform as tool pile instead of product; weak adoption model; missing self-service, golden paths, measurement, and feedback loops. |

---

## Failure-Mode Taxonomy

| Category | Recurring anti-patterns |
| --- | --- |
| **1. Review and merge hygiene failures** | Rubber-stamp approvals; single-reviewer merges on high-risk change; oversized PRs; nitpicks blocking progress; pressure to approve quickly; "I will add tests later"; unresolved review conflict; merging code the author cannot explain. |
| **2. Speculative complexity and over-engineering** | Building for scale before validating; abstractions for imagined futures; too many arguments/god objects; maximalist infrastructure; heavy dependencies without ownership plan; nested modules no one trusts. |
| **3. Toil, interrupts, and capacity starvation** | Manual repetitive operations; on-call and project work double-booked; tickets as a gauntlet; firefighting crowding out reliability/security/dependency work; no visible capacity budget. |
| **4. Observability and feedback-loop deficits** | Instrumentation added last; metric fatigue; logs without correlation or context; PII in telemetry; no health checks; flaky/opaque CI; no user or support signal loop. |
| **5. Test quality and safety-net erosion** | Flaky tests normalized; sleeps/external APIs in unit tests; mystery fixtures; focused tests merged; hourglass suites; contract tests missing at boundaries; "green by omission." |
| **6. Supply-chain and pipeline compromise** | Unprotected default branches; dangerous workflows; over-broad tokens; unpinned dependencies; missing provenance; compromised build platforms; malicious artifacts; unmaintained packages. |
| **7. Procurement, vendor lock-in, and ownership gaps** | UMOTS; proprietary APIs without escape plan; long contracts with no exit; weak build-vs-buy analysis; supplier-owned modifications/data; no portability test; "cloud first" copied as universal law. |
| **8. Infrastructure drift and release fragility** | Manual patching; mutable environments; frightening Terraform applies; app/IaC coupling that blocks release; main not releasable; no flags/canaries/rollback evidence; dev/prod divergence. |
| **9. Security and privacy boundary failures** | Broken authorization; unsafe third-party API consumption; SSRF; improper inventory; retention not tied to data class; PII in logs/prompts; consent and DPIA as late legal paperwork. |
| **10. AI, RAG, and agentic failure modes** | Prompt injection; secrets in context; generated code merged without understanding; unbounded tool authority; data poisoning; no eval gate; RAG without retrieval quality tests; "council" as fake approval. |
| **11. Incident learning failures** | No incident owner; delayed postmortems; blameful write-ups; missing timeline; action items not owned; status/customer comms absent; recurring incidents not connected to planning. |
| **12. Knowledge and decision opacity** | Oral tradition; ADRs not enforced; research that stays in chat; stale docs; no ownership metadata; silent uncertainty; decisions hard to find six months later. |

---

## Current Doctrine Coverage Scorecard

Scale: **5 = strong and discoverable**, **4 = strong but scattered**, **3 = present but thin**, **2 = mostly implicit**, **1 = absent**.

| Failure-mode area | Score | Current coverage | Gap |
| --- | ---: | --- | --- |
| AI/RAG/agentic failure modes | 5 | `principles/ai-ml-systems.md` §8, `patterns/rag-retrieval-baseline.md`, AI research notes. | Keep current; avoid product-specific model governance in principles. |
| Supply-chain and merge-path compromise | 5 | `principles/merge-path-evidence-and-pipeline-integrity.md`, `patterns/engineering-controls-governance-program.md`, `dependencies-supply-chain.md`. | Add a single anti-pattern index pointing here. |
| Incident lifecycle and on-call | 4.5 | `patterns/incident-lifecycle-and-on-call-operations.md`, `reliability-slo-incidents.md`, `platform-readiness.md`. | Estate playbooks and tool choices remain local. |
| Observability pitfalls | 4 | `principles/observability.md`, `tooling/observability.md`, `reliability-slo-incidents.md`. | Metric fatigue / telemetry privacy could be easier to find. |
| Build, release, drift, and delivery fragility | 4 | `principles/build.md`, `patterns/build-surface-model.md`, `trunk-workflow.md`, `doctrine-versioning-and-consumer-compatibility.md`. | Release failure modes are spread across many files. |
| Review and merge hygiene | 3.5 | `principles/collaboration.md`, `patterns/trunk-workflow.md`, governance controls. | No Google-style author/reviewer anti-pattern guide or review economics page. |
| Test smells and safety-net erosion | 3.5 | `principles/testing-strategy.md` covers pyramid, hourglass, flakes, contracts, mutation/property/a11y. | Missing concrete smell taxonomy for tests and examples of bad tests. |
| Vendor lock-in / build-vs-buy | 3 | `interoperability-and-standards.md`, `container-runtime-choice.md`, estate split. | No dedicated lock-in / UMOTS / exit-strategy anti-pattern guidance. |
| Capacity starvation and toil budget | 3 | Toil appears in reliability and incident docs; prior benchmark flagged capacity allocation. | No portable capacity allocation principle. |
| Support and customer-impact comms | 3 | Incident/release docs mention comms; support is a known prior gap. | No status-page / known-issues / customer-impact pattern. |
| Data classification / handling failure modes | 3 | `privacy-and-data-governance.md`, `audit-logging.md`, AI data handling. | Missing portable classification taxonomy that drives handling requirements. |
| Knowledge opacity and decision traceability | 4 | `documentation-knowledge.md`, ADR/RFC guidance, research-publishes norm. | Anti-pattern language is not centralized; "pitfall" is not searchable. |
| Anti-pattern discoverability overall | 2.5 | Strong coverage exists, but under `avoid`, `footguns`, `risks`, `anti-patterns`, `failure modes`. | No one page says: "Here is how engineering systems fail, and where to read." |

---

## True Gaps

1. **No anti-pattern / failure-mode spine.**  
   The repo has strong local pockets (`ai-ml-systems.md` §8, `engineering-controls-governance-program.md` §5, `collaboration.md` footguns, `build-surface-model.md` "what to avoid"), but no index for failure vocabulary. A reader must know which positive principle to open before seeing the failure mode.

2. **Review economics and reviewer failure modes are thin.**  
   Public sources are unusually concrete about rubber-stamping, nitpick blocking, oversized changes, pressure to approve, piecemeal feedback, and escalation. This repo has collaboration rules, but not a focused author/reviewer anti-pattern guide.

3. **Test smell taxonomy is missing.**  
   `testing-strategy.md` gives the right testing shape, but not enough "bad test" vocabulary: mystery fixtures, sleeps, external I/O in unit tests, fragile general fixtures, test-only branches, focused tests, or green-by-omission.

4. **Build-vs-buy, UMOTS, and lock-in failure modes need portable treatment.**  
   The repo correctly avoids vendor mandates, but it does not yet say enough about how procurement and COTS customization fail: supplier-owned data, proprietary APIs, no exit plan, customization that blocks upgrades, or "cloud first" copied without estate context.

5. **Capacity starvation is still open.**  
   The prior public benchmark already flagged this. Anti-pattern research reinforces it: unbounded toil, interrupt load, security/dependency work starved by features, and reliability work treated as spare-time improvement.

6. **Support/customer-impact communication remains thin.**  
   Incident command exists, but support operating rhythm is not portable doctrine yet: status thresholds, customer-impact wording, known-issue ownership, support-to-engineering escalation, deprecation comms.

7. **Data classification is not yet the organizing control.**  
   Privacy and audit rules are good, but anti-patterns recur around PII in logs, analytics, prompts, support exports, test data, and third-party APIs. A lightweight data-classification / handling taxonomy would connect these.

8. **Failure learning is not yet managed as a portfolio.**  
   Postmortems, retrospectives, DORA, SLOs, and governance metrics exist, but there is no pattern for recurring failure-mode review: cluster incidents/near-misses/review findings, retire repeated causes, and publish learning back into doctrine.

---

## Recommendations

### Must

1. **Add a failure-mode index / anti-pattern registry.**  
   A short pattern should map common names—anti-pattern, failure mode, pitfall, smell, footgun, drift, lock-in—to the existing doctrine files. This closes discoverability without duplicating every rule.

2. **Add a capacity allocation principle.**  
   State that feature work, reliability, toil reduction, security response, dependency hygiene, platform enablement, and supportability have explicit budgets. Keep numbers estate-specific; make the allocation visible and reviewed.

3. **Add data classification and handling.**  
   Define portable classes and handling outcomes without prescribing exact labels. Use it to drive logging, telemetry, audit, support exports, AI prompt/context use, retention, and deletion.

### Should

- Add a **review anti-pattern / review economics** pattern covering rubber stamps, nitpick blocking, oversized PRs, pressure to approve, late feedback, and escalation.
- Add a **test smells** subsection or pattern linked from `testing-strategy.md`.
- Add **build-vs-buy / lock-in anti-patterns** to `interoperability-and-standards.md` or a new pattern.
- Add a **support and customer-impact communications** pattern for incidents, known issues, deprecations, status updates, and support-to-engineering loops.

### Could

- Add concrete worked examples: bad PR review, bad test, bad vendor selection, bad telemetry event.
- Add a failure-mode review cadence to `governance-program-readiness.md`.
- Add "pitfall" as a search synonym in the glossary.
- Add a small canvas / scorecard for teams to self-assess failure-mode exposure.

---

## Portable Doctrine Guardrail

Do not copy company-specific thresholds as global law. Translate failure patterns into portable invariants:

| Public-source signal | Portable doctrine translation |
| --- | --- |
| Google SRE "50% toil cap" | Toil and interrupt load are measured, visible, capped by local policy, and traded against feature work explicitly. |
| Google / GitLab reviewer rules | Review protects code health without blocking continuous improvement; escalation exists when review stalls. |
| 18F UMOTS warning | Customization that destroys upgradeability, data portability, or exit rights is a product and engineering risk. |
| GOV.UK open standards | Prefer standards and exit paths that preserve interoperability; estate exceptions require rationale. |
| OpenSSF branch/token checks | Merge and automation authority must be explicit, least-privilege, reviewable, and protected. |
| DORA pitfalls | Metrics guide improvement; they are not individual scorecards or targets to game. |
| PagerDuty / Atlassian postmortems | Incidents are not closed until learning is owned, tracked, and fed back into planning. |

---

## Suggested Gap Fill Order

1. **Failure-mode index / anti-pattern registry** — fastest, mostly cross-linking existing coverage.
2. **Capacity allocation principle** — closes a repeated human/systemic failure from both public benchmark and anti-pattern research.
3. **Data classification and handling** — unlocks clearer privacy, telemetry, AI, support, and audit guidance.
4. **Support/customer-impact communications** — complements incident lifecycle work already added.
5. **Review/test smell depth** — useful once the broader operational gaps are covered.

---

## Bottom Line

This doctrine already names many important failures, especially in **AI/RAG**, **supply chain**, **merge-path integrity**, **incident operations**, **events**, **idempotency**, and **platform drift**. The main weakness is not absence of wisdom; it is **failure-mode discoverability**. A portable doctrine should make common bad paths searchable and reviewable, not only describe the good state.
