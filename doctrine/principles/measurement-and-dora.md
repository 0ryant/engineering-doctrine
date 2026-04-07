# Measurement: Delivery Performance And DORA

Link **practice** to **outcomes**. This principle sits beside [reliability-slo-incidents.md](reliability-slo-incidents.md): SLOs describe **a service’s** promises to users; **DORA-style** metrics describe **how the organisation delivers** change. Both reduce arguments from taste.

---

## 1. The Four Keys (Conceptual)

Industry research (often summarised as **DORA** or *Accelerate*) ties software delivery performance to four headline metrics:

| Metric | Plain meaning |
| --- | --- |
| **Deployment frequency** | How often you ship **safely** to production |
| **Lead time for changes** | Time from commit to production for a typical change |
| **Change failure rate** | Share of changes causing degraded service / rollback / hotfix |
| **Time to restore** | How long to recover normal service after failure |

Exact definitions evolve with your **value stream** tooling; record **your** definitions in an internal doc and **keep them stable** quarter-to-quarter so trends mean something.

**Why:** These metrics turn “we follow the doctrine” into “delivery is getting safer/faster—or not.”

---

## 2. Map Metrics To Doctrine (Illustrative)

| Four Keys signal | Doctrine touchpoints |
| --- | --- |
| **Deployment frequency** | [build.md](build.md) surfaces, [collaboration.md](collaboration.md) trunk cadence, CI that **promotes** artefacts |
| **Lead time** | Small batches, [trunk-workflow.md](../patterns/trunk-workflow.md), automations that remove wait states |
| **Change failure rate** | [testing-strategy.md](testing-strategy.md), contract validation, [api-boundaries-and-security.md](api-boundaries-and-security.md), release discipline [semantic-versioning.md](semantic-versioning.md) |
| **Time to restore** | [reliability-slo-incidents.md](reliability-slo-incidents.md), [observability.md](observability.md), runbooks [documentation-knowledge.md](documentation-knowledge.md) |

Use the map in **retrospectives**: a rising CFR often traces to **skipped gates** or **unclear ownership**, not “bad luck.”

---

## 3. What This Document Does Not Replace

- **Product metrics** (activation, revenue) — still required for product health.
- **Security and compliance attestations** — complementary; use [dependencies-supply-chain.md](dependencies-supply-chain.md), audits, ASVS-style reviews where applicable.
- **Individual developer productivity theatre** — avoid using Four Keys to punish people; use them to **inspect the system**.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Separate from SLO doc | SLOs are **per-service** promises; DORA metrics are **delivery system** health—both needed. |
| Reference research, don’t replicate | Definitions and benchmarks are maintained by **DORA** and secondary literature—link out. |

---

## References

- **DORA** (Google Cloud DevOps Research): https://dora.dev/  
- *Accelerate* (Forsgren, Humble, Kim) — research foundation for Four Keys  
- [reliability-slo-incidents.md](reliability-slo-incidents.md) — SLOs, error budgets, incidents  
