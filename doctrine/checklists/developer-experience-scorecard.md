# Developer Experience Scorecard

Use this when reviewing a repo, template, platform golden path, or internal tool. It complements [../principles/developer-experience.md](../principles/developer-experience.md), [../principles/build.md](../principles/build.md), [../principles/documentation-knowledge.md](../principles/documentation-knowledge.md), and [../principles/measurement-and-dora.md](../principles/measurement-and-dora.md).

Score each dimension **0–2**:

- **0** — missing or mostly tribal knowledge
- **1** — present but inconsistent, slow, stale, or maintainer-dependent
- **2** — documented, usable by a competent contributor, and maintained

```text
[ ] Time-to-first-change: README or equivalent shows purpose, owner, setup, local check, and first safe change path
[ ] Local loop: fast local command exists for common validation; full gate is documented separately if slower
[ ] Setup health: bootstrap is idempotent and gives actionable failure messages
[ ] Docs findability: entrypoint links to architecture sketch, contracts, runbooks, ADRs/RFCs, and deeper reference
[ ] Ownership clarity: team/channel/on-call or maintainer route is obvious
[ ] Cognitive load: routine work follows one named path; exception path exists for unusual work
[ ] Review flow: expected reviewer response time, escalation path, and small-change preference are documented
[ ] Verification evidence: contributors know what evidence to include in PRs or change notes
[ ] Tooling independence: ordinary changes do not require maintainer-only local state or undocumented credentials
[ ] Feedback loop: team-level DevEx feedback or survey/interview signal is reviewed on a cadence
```

## Interpreting The Score

| Score | Meaning | Action |
| ---: | --- | --- |
| **0–7** | Friction is likely blocking contribution and increasing bypass pressure | Fix entry docs, setup, and local loop before adding new controls |
| **8–14** | Usable but uneven | Pick the lowest two dimensions and assign owners |
| **15–20** | Healthy baseline | Keep measuring; watch for stale docs and slow review queues |

## Optional Metrics

Use metrics as **team/system** signals, never as individual ranking:

```text
[ ] Median time from clone to first successful local check for a new contributor
[ ] Median local fast-check duration
[ ] Median first-review response time
[ ] % PRs with stated verification evidence
[ ] Documentation findability rating from contributor survey
[ ] Top three recurring setup or local-loop failures
```

## References

- SPACE framework: https://queue.acm.org/detail.cfm?id=3454124  
- DORA 2024 report: https://dora.dev/research/2024/dora-report  
- CNCF Platform Engineering Maturity Model: https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model  
- Google Engineering Practices — Small CLs: https://google.github.io/eng-practices/review/developer/small-cls.html  
