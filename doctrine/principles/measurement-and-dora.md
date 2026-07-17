# Measurement: Delivery Performance And DORA

Link **practice** to **outcomes**. This principle sits beside [reliability-slo-incidents.md](reliability-slo-incidents.md): SLOs describe **a service’s** promises to users; **DORA-style** metrics describe **how the organisation delivers** change. Both reduce arguments from taste.

---

## 1. Software Delivery Performance Metrics

DORA's current model uses five software-delivery metrics across throughput and instability. The model evolved from the original Four Keys; use the current definitions rather than freezing an old dashboard vocabulary.

| Metric | Plain meaning |
| --- | --- |
| **Deployment frequency** | How often you ship **safely** to production |
| **Change lead time** | Time from commit to production for a typical change |
| **Failed deployment recovery time** | How long to recover from a deployment that fails and requires intervention |
| **Change fail rate** | Share of deployments requiring immediate intervention such as rollback or hotfix |
| **Deployment rework rate** | Share of deployments that are unplanned work caused by a production incident |

Exact definitions evolve with your **value stream** tooling; record **your** definitions in an internal doc and **keep them stable** quarter-to-quarter so trends mean something.

**Why:** These metrics turn “we follow the doctrine” into “delivery is getting safer/faster—or not.”

---

## 2. Map Metrics To Doctrine (Illustrative)

| Delivery signal | Doctrine touchpoints |
| --- | --- |
| **Deployment frequency** | [build.md](build.md) surfaces, [collaboration.md](collaboration.md) trunk cadence, CI that **promotes** artefacts |
| **Change lead time** | Small batches, [trunk-workflow.md](../patterns/trunk-workflow.md), automations that remove wait states |
| **Change fail rate** | [testing-strategy.md](testing-strategy.md), contract validation, [api-boundaries-and-security.md](api-boundaries-and-security.md), release discipline [semantic-versioning.md](semantic-versioning.md) |
| **Failed deployment recovery time** | [reliability-slo-incidents.md](reliability-slo-incidents.md), [observability.md](observability.md), runbooks [documentation-knowledge.md](documentation-knowledge.md) |
| **Deployment rework rate** | Small-batch correction, incident learning, [testing-strategy.md](testing-strategy.md), and prevention of repeated unplanned deployments |

Use the map in **retrospectives**: when CFR rises, investigate changed risk mix, evidence discrimination, skipped controls, ownership, release shape, and recovery conditions rather than assuming one universal cause.

---

## 2.1 Vulnerability Response And Remediation Signals (Adjacent To DORA Metrics)

**DORA delivery metrics** measure **delivery** health; **vulnerability operations** need parallel **SLIs** so “we ship often” does not mask “we never patch.” Track definitions in an internal doc and keep them stable quarter-to-quarter. Examples (rename to match your telemetry):

| SLI | Plain meaning |
| --- | --- |
| **Within remediation target** | Share (or count) of open findings resolved before the estate’s SLA clock—see [dependencies-supply-chain.md](dependencies-supply-chain.md) §2 |
| **Time to triage** | Elapsed from **first signal** (scanner, feed, report) to **prioritised** owner and disposition |
| **Known-exploited backlog** | Count and age of issues matching **weaponisation** feeds (e.g. [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)) still open |
| **Security debt beyond policy** | Findings older than the published SLA without an approved exception |

**Why:** NIST SSDF **RV** expects an ongoing vulnerability-identification and response capability. Stable response signals help an owner evaluate that capability; **DORA** throughput alone does not—pair with [dependencies-supply-chain.md](dependencies-supply-chain.md) §2 and [secure-development-lifecycle.md](secure-development-lifecycle.md) §3.

## 2.2 Delivery Metrics Are Not Company Objectives

DORA explicitly warns against setting a delivery metric as the goal, using one metric for a complex system, or comparing unlike services. Treat delivery metrics as contextual leading/lagging signals about the delivery system—not as a universal company KPI, an individual target, or a deterministic source of tasks.

For strategic or product interventions, connect stakeholder objectives to outcome measures, guardrails, intervention hypotheses, bounded work, outputs, and observed outcomes using [Outcome And Portfolio Linkage](../patterns/outcome-and-portfolio-linkage.md). Select work by testing the most material constraint or hypothesis; do not reward agents for maximising deployment count, task completion, code volume, or artefact output.

Not every change is a product intervention. Maintenance, vulnerability response, compatibility, lifecycle, operational-risk, and enabling work may be justified by the obligation, invariant, exposure, or capability they preserve. They still need an accountable mandate, but they do not need invented KPIs or causal attribution.

---

## 3. What This Document Does Not Replace

- **Product metrics** (activation, revenue) — still required for product health.
- **Security and compliance attestations** — complementary; use [dependencies-supply-chain.md](dependencies-supply-chain.md), audits, ASVS-style reviews where applicable.
- **Individual developer productivity theatre** — avoid using DORA metrics to punish people; use them to **inspect the system**.

---

## 4. SPACE: Developer Experience Beyond Throughput

- **SPACE** (Satisfaction and well-being, Performance, Activity, Communication and collaboration, Efficiency and flow) frames **developer experience** using **multiple** dimensions—not only **lines of code** or **story points**.
- Use SPACE-style surveys and **qualitative** interviews alongside DORA metrics to catch **burnout**, **tooling friction**, and **review** bottlenecks that delivery metrics can **miss**.
- Developer-experience operating rules live in [developer-experience.md](developer-experience.md); a lightweight review tool lives in [developer-experience-scorecard.md](../checklists/developer-experience-scorecard.md).

**Why:** Microsoft Research’s SPACE work shows **single-metric** productivity measures **game** behaviour and hide systemic problems.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Separate from SLO doc | SLOs are **per-service** promises; DORA metrics are **delivery system** health—both needed. |
| Reference research, don’t replicate | Definitions and benchmarks are maintained by **DORA** and secondary literature—link out. |
| SPACE complements DORA | **Throughput** without **well-being** signals misleads leadership during crunch. |

---

## References

- **DORA software delivery performance metrics** (current five-metric model and pitfalls): https://dora.dev/guides/dora-metrics/
- *Accelerate* (Forsgren, Humble, Kim) — research foundation for Four Keys  
- ACM Queue — **The SPACE of Developer Productivity** (Forsgren et al.): https://queue.acm.org/detail.cfm?id=3454124  
- [reliability-slo-incidents.md](reliability-slo-incidents.md) — SLOs, error budgets, incidents  
