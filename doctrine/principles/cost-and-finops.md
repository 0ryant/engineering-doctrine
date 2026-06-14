# Cost, FinOps, And Unit Economics

Durable rules for making **cloud spend observable**, **attributable**, and **governed**—so cost is treated as a first-class non-functional requirement from day one, not an afterthought on the quarterly bill.

Complements [performance-and-cost.md](performance-and-cost.md) (budgets, load, sustainability) and [performance-and-cost.md §3](performance-and-cost.md) (tagging basics). This file provides the **governance** layer those sections reference. AI inference cost governance aligns with [ai-ml-systems.md](ai-ml-systems.md) Tier A–D risk controls.

---

## 1. FinOps Operating Model

- **Adopt the three-phase FinOps cycle**: **Inform** (allocate and measure), **Optimize** (identify and execute savings), **Operate** (establish accountability loops and repeat). Crawl before you walk; not every capability needs to be "run" maturity to be valuable.
- **FinOps is a shared-responsibility model**: Cloud engineers make the technical decisions that determine spend; finance and product own the budget; FinOps practice coordinates them. No single team "owns" cost without accountability at the point of consumption.
- **Measure before optimising**: Establish allocation coverage before committing to savings targets. Optimising unallocated spend is guesswork.

**Why:** FinOps Foundation research shows teams without an explicit operating model default to reactive, invoice-driven response—typically weeks after the spend event.

---

## 2. Cost Allocation And Tagging

- **Tag every provisioned resource** at creation time with at minimum: `environment` (prod/staging/dev), `owner-team`, `cost-centre`, `application`, and `product`. Infrastructure-as-code templates pre-populate these; resources that arrive untagged are either automatically remediated or reported to owners on a short SLA.
- **Target allocation coverage**: aim for >85% of spend traceable to a team or cost centre within 60 days of adoption; >90% at steady state. Unallocated spend >10% is a process failure, not a data problem.
- **Shared costs** (platform services, networking, centrally managed tools) are either allocated proportionally by a proxy metric (traffic, storage, requests) or held centrally with a documented rationale—never silently ignored.
- **Kubernetes and container workloads** require namespace-level labels (`application`, `team`, `cost-centre`, `environment`) as the equivalent tagging layer; aggregate these through an **OpenCost**-compatible tool or cloud-native cost visibility endpoint.

**Why:** Cost without attribution is invisible. Tagging enforcement at the IaC layer is lower friction than retroactive cleanup.

---

## 3. Unit Economics

- **Define unit metrics before launch**, not after first bill. Pick metrics that connect engineering decisions to business outcomes: cost per request, cost per tenant, cost per AI inference, cost per document processed.
- **Two tiers of metrics**: (a) *technical efficiency* — cost per GB stored, cost per vCPU-hour, cost per token; (b) *business unit* — cost per customer, cost-to-serve, cost per transaction, cost per case resolved.
- **Publish unit costs** in service dashboards and architectural review artefacts. Engineers who see the cost of a design choice at review time make different decisions than those who see it months later.
- **For AI and GenAI workloads**: establish cost-per-token baselines at Tier A and expand to cost-per-business-outcome (cost per assist, cost per agent action, cost per correctly resolved query) as the system matures—volume token spend without outcome correlation is waste signal.
- **Review definitions quarterly**; document calculation assumptions (are shared platform costs included? which cost categories?). Drift in definition makes trend analysis meaningless.

**Why:** Unit economics are the mechanism by which engineering teams make trade-offs explicit—build vs. buy, model size vs. latency, architecture cost vs. complexity.

---

## 4. Anomaly Detection And Spend Alerts

- **Alert on spend anomalies** with the same urgency as performance regressions. Alerts route to the team that owns the resource, identified by allocation tags.
- **Define alert thresholds per service**: single-resource cost ceiling (e.g. any single resource >£5k/month), percentage variance from 30-day rolling average (>15% week-on-week), and projected month-end forecast exceeding approved budget by >10%.
- **Cadence**: daily anomaly scans minimum; real-time alerting where platforms support it. Weekly or monthly is too slow.
- **Response procedure**: team categorises the anomaly (legitimate new environment, investigation needed, misconfiguration) and records root cause and remediation in the ticket. False positives are documented to refine thresholds.
- **Third-party API spend** (including model inference providers) is monitored with the same anomaly controls as first-party infrastructure—this is explicitly aligned with [OWASP API4 (Unrestricted Resource Consumption)](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/).

**Why:** Cloud spend anomalies surface misconfiguration, runaway loops, and unplanned traffic growth faster than any bill review. Catching a misconfigured autoscaler on day two costs orders of magnitude less than catching it on the invoice.

---

## 5. Rightsizing And Waste Elimination

- **Use observed utilisation, not guesses**: right-size compute after 2–4 weeks of production data. Provisioning targets are hypotheses; utilisation data is the test.
- **Default utilisation targets** (adjust with a short ADR if your workload differs): CPU 60–75% at peak, memory 50–70% at peak. Sustained CPU <30% or memory <40% is a rightsizing candidate.
- **Automation scope**: safely automate removal of *truly idle* resources (zero connections, zero CPU, zero read/write for 14+ days); automate scheduling of dev/test environments to stop overnight and on weekends. *Production* rightsizing requires owner review and testing before execution.
- **AI inference rightsizing**: apply quantisation, prompt caching, batching, and model selection *before* scaling up GPU/compute—compute optimisation upstream (in the prompt and model choice) has higher leverage than infrastructure rightsizing downstream.
- **Commitment coverage**: record the decision to purchase reserved capacity or committed use discounts in an ADR with: workload baseline, commitment term, renewal owner, and break-even threshold.

**Why:** Unused reservation and perpetually over-provisioned dev environments are the highest-value, lowest-risk optimisations in most cloud estates. Do these before fine-tuning critical-path services.

---

## 6. Showback And Chargeback

- **Showback is always on**: every team receives regular (at minimum monthly, ideally weekly) cost visibility for the resources under their ownership tags. This is non-negotiable regardless of whether formal chargeback exists.
- **Chargeback** (formal allocation to finance general ledger) is adopted only when organisational policy requires P&L separation by business unit. It carries reconciliation burden (invoice timing, credits, restatements); do not introduce it as a proxy for accountability when showback is sufficient.
- **Accountability** is the goal of both mechanisms. If teams see their cost data and still have no incentive to act, the problem is governance and product ownership—not the cost tool.

**Why:** Chargeback is not inherently more mature than showback. Distinguish the tool (reporting) from the outcome (accountability).

---

## 7. AI / Inference Cost Governance

- AI/ML workloads operating at [Tier A or above](ai-ml-systems.md) require **explicit cost controls** as part of the deployment checklist: token budgets, circuit breakers for daily spend, model selection policy, and cost-per-outcome tracking.
- **Token budget discipline**: define per-use-case token consumption targets (e.g. max input+output context per query type). Enforce via circuit breaker: if daily budget is exceeded, fall back to a cheaper model or cached response rather than pass unbounded cost to the infrastructure.
- **Model selection is a cost decision**: document the latency/quality/cost trade-off when choosing between model sizes or providers. Agentic flows (Tier D) can multiply token consumption non-linearly; cost governance applies per *agent run*, not only per *API call*.
- **Vector store and embedding costs** (Tier B+): include ANN index storage, embedding re-generation costs, and reranker compute in the service cost model—not only model inference.

**Why:** AI inference is the fastest-growing cloud cost category for engineering teams in 2026. A missing token budget on one agentic workflow can exceed the monthly compute budget of the entire service.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Three-phase FinOps cycle | Matches FinOps Foundation maturity model; avoids "optimise before you can see" failure. |
| Tagging at IaC not retroactively | Retroactive tagging campaigns fail in practice; enforcement at provisioning is permanent. |
| Unit economics at design time | Cost trade-offs made before build are cheaper than those made after deploy. |
| Daily anomaly cadence | Invoice-driven discovery loses weeks of spend; real-time is achievable with modern platforms. |
| Automate idle; human review for production sizing | Idle removal is safe; production rightsizing can break SLOs without testing. |
| Showback always; chargeback only if required | Eliminates heavyweight reconciliation for teams that only need transparency. |
| AI inference as first-class cost concern | Token spend at agentic scale dwarfs traditional cloud infra costs; requires circuit breakers, not just dashboards. |

---

## References

- FinOps Foundation — **FinOps Framework** (phases, capabilities, maturity model): https://www.finops.org/framework/
- FinOps Foundation — **Unit Economics** capability: https://www.finops.org/framework/capabilities/unit-economics/
- FinOps Foundation — **Anomaly Management** capability: https://www.finops.org/framework/capabilities/anomaly-management/
- FinOps Foundation — **Invoicing and Chargeback**: https://www.finops.org/framework/capabilities/invoicing-chargeback/
- FinOps Foundation — **Container Cost Allocation** working group: https://www.finops.org/wg/container-cost-allocation/
- FOCUS Specification — **FinOps Open Cost and Usage Specification** (billing data normalisation): https://focus.finops.org/
- OpenCost — **open-source cost monitoring for cloud-native workloads**: https://www.opencost.io/
- Green Software Foundation — **Software Carbon Intensity (SCI)** specification: https://sci.greensoftware.foundation/
- OWASP API4:2023 — **Unrestricted Resource Consumption** (includes third-party API spend): https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/
