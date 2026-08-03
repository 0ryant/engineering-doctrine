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
- **Agent-unit metering feeds the same scans**: where the platform meters agentic consumption in dedicated agent units—e.g. [Azure agent units](https://learn.microsoft.com/en-us/azure/sre-agent/pricing-billing), which meter LLM tokens (input, output, cache read/write) per active flow plus an always-on per-agent-hour charge—include those units in the daily anomaly scans and per-service thresholds alongside token and infrastructure spend. Agent-unit anomalies surface runaway agent loops that per-call token metrics smear across thousands of small requests. These are anomaly-signal inputs; per-run and per-use-case **budget units** remain defined in §7.

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
- **Token budget discipline**: define per-use-case token consumption targets (e.g. max input+output context per query type). Enforce via circuit breaker: if daily budget is exceeded, fall back to a cheaper model or cached response rather than pass unbounded cost to the infrastructure. Prefer **vendor- or org-level spend limits and entitlement defaults** where the platform provides them (e.g. OpenAI organisation/project spend limits, Anthropic spend limits, Bedrock service quotas — availability and hard-cap semantics vary by provider and plan; see References), and treat self-built token budgets and circuit breakers as the **backstop layer and the portable floor**: they travel across providers, catch what the platform misses, and **remain in place even where the provider enforces limits below your code** — vendor-native limits are the preferred primary, not a replacement.
- **Model selection is a cost decision**: document the latency/quality/cost trade-off when choosing between model sizes or providers. Agentic flows (Tier D) can multiply token consumption non-linearly; cost governance applies per *agent run*, not only per *API call*.
- **Vector store and embedding costs** (Tier B+): include ANN index storage, embedding re-generation costs, and reranker compute in the service cost model—not only model inference.
- **Agentic workloads in capacity planning** (Tier D): carry agent workloads through capacity planning and portfolio funding like any other growth workload—where the platform meters agentic consumption in **agent units** (e.g. [Azure agent units](https://learn.microsoft.com/en-us/azure/sre-agent/pricing-billing)), agent-unit forecasts belong in the §4 month-end projection, not only the incident channel. Budget and load baselines live in [performance-and-cost.md](performance-and-cost.md); this file governs the spend controls around them.

**Why:** AI inference is the fastest-growing cloud cost category for engineering teams in 2026. A missing token budget on one agentic workflow can exceed the monthly compute budget of the entire service.

### 7.1 Agent Financial And Transaction Authority

§7 above governs cost the estate *pays*; this subsection governs money agents *move*. It applies to any estate that grants an agent payment or transaction authority; estates that never grant such authority inherit only the first bullet.

- **Default-deny**: an agent MUST NOT hold payment instruments or transaction authority — wallets, payment credentials, transfer or purchase capability — unless explicitly granted. A grant is a **per-agent** decision recorded in the **AI inventory** ([../patterns/ai-adoption-controls.md](../patterns/ai-adoption-controls.md) §1) and attaches only to an identity satisfying [zero-trust-and-workload-identity.md](zero-trust-and-workload-identity.md) §2.1 — money movement sits on the **materiality axis** ([ai-ml-systems.md](ai-ml-systems.md) §2.1), so that means a **dedicated per-agent principal**; payment credentials are never shared fleet credentials. Default-deny is stricter than any autonomy-slider position ([../patterns/agentic-loop-design.md](../patterns/agentic-loop-design.md) §6): the authority is **absent**, not gated. Departures route through the exception contract ([../patterns/normative-language-applicability-and-exceptions.md](../patterns/normative-language-applicability-and-exceptions.md) §5) — accountable approver, compensating controls, expiry — never silent slider advancement.
- **Session and run budgets**: granted authority MUST be **session-scoped and budget-limited** — per-run/per-session transaction caps enforced **outside the prompt**, in the harness or payment plane, extending the per-run budget units and circuit-breaker enforcement §7 already requires for tokens (one budget discipline, two denominations). Composes [zero-trust-and-workload-identity.md](zero-trust-and-workload-identity.md) §2.1 per-interaction credentials and [../patterns/agentic-loop-design.md](../patterns/agentic-loop-design.md) §8.3 authority attenuation: **delegation cannot widen a payment budget**.
- **Materiality-tiered approval**: human pre-approval thresholds MUST be tiered by **transaction materiality** on the existing money-movement axis ([ai-ml-systems.md](ai-ml-systems.md) §2.1), using the applicability vocabulary of [../patterns/normative-language-applicability-and-exceptions.md](../patterns/normative-language-applicability-and-exceptions.md) §3 (**low / material / critical**; **reversible / compensatable / irreversible**) — do not invent a new materiality scale. The tier table itself is **estate-defined** (CONTEXT-DEPENDENT); the portable floor is that **irreversible or critical-value** transactions start at approve-before-execute.
- **Payment audit trails**: every agent-initiated transaction MUST carry the full **attribution chain** of [zero-trust-and-workload-identity.md](zero-trust-and-workload-identity.md) §2.1 — initiating human, sponsor, agent identity, each on-behalf-of hop — with evidence fields and retention per [audit-logging.md](audit-logging.md). Payment operations SHOULD be **idempotent** across retry boundaries ([../patterns/idempotency-across-boundaries.md](../patterns/idempotency-across-boundaries.md)): agent retry loops plus money movement is the canonical duplicate-side-effect hazard. Payment-spend anomalies alert through §4's existing channels.

**Standards watch** *(informative, not normative — items are announced, preview, or vendor-specific; any future binding routes through [../patterns/revision-pinned-control-profiles.md](../patterns/revision-pinned-control-profiles.md))*: Google-led **AP2** (Agent Payments Protocol) **mandates** — Intent and Cart mandates as cryptographically signed verifiable credentials giving non-repudiable pre-authorization — are the emerging standard direction for the pre-authorization half of this control (announced 2025-09 with 60+ payments-sector supporters): https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol — Stripe **ACP Shared Payment Tokens** (limited-authority tokens scoped to one merchant and basket total): https://stripe.com/newsroom/news/stripe-openai-instant-checkout — Mastercard **Agentic Tokens** (registered, verified agents; per-transaction authorization): https://investor.mastercard.com/investor-news/investor-news-details/2025/Mastercard-Unveils-Agent-Pay-Pioneering-Agentic-Payments-Technology-to-Power-Commerce-in-the-Age-of-AI/default.aspx — Visa **Intelligent Commerce** (spending limits, approval workflows, trusted-agent signals): https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.21366.html — named products and protocols are rationale, not mandated tooling.

**Why:** Every major payment network and agent platform shipped agent-payment rails in 2025–2026, and all converge on the shape this subsection mandates: registered per-agent identity, scoped limited-authority tokens, user-set spending limits, human approval for material transactions. An estate that lets an agent inherit a standing payment credential has skipped the one control layer the entire ecosystem agrees on.

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
| Vendor-native limits preferred; self-built breakers as backstop | Platform spend limits and entitlement defaults are enforced below application code and survive application bugs; portable self-built breakers remain the floor where the provider offers no limit. |
| Agent financial authority default-deny | Money movement is on the materiality axis by definition; absent authority beats gated authority, and per-agent grants keep revocation as the kill switch. |

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
- Microsoft Learn — **Azure SRE Agent pricing and billing** (agent units: always-on flow plus token-based active-flow metering; monthly allocation hard-stop): https://learn.microsoft.com/en-us/azure/sre-agent/pricing-billing
- Microsoft Learn — **Plan and manage costs for Microsoft Foundry** (budgets and threshold alerts; no native hard spend cap): https://learn.microsoft.com/en-us/azure/foundry/concepts/manage-costs
- AWS — **Bedrock application inference profiles** (cost-allocation tags per model/team invocation): https://docs.aws.amazon.com/bedrock/latest/userguide/cost-mgmt-application-inference-profiles.html
- AWS — **Bedrock service quotas** (token-usage quotas per model and endpoint): https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html
- OpenAI — **Spend limits** (organisation- and project-level alerts and hard limits): https://developers.openai.com/api/docs/guides/spend-limits
- Anthropic — **Spend Limits API** (per-member effective limits, overrides, increase-request workflow; Claude Enterprise organisations only): https://platform.claude.com/docs/en/manage-claude/spend-limits-api
- Google Cloud — **Agent Payments Protocol (AP2)** announcement (Intent/Cart mandates as cryptographically signed verifiable credentials; announced 2025-09 with 60+ payments-sector supporters): https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol
- OWASP — **AI Agent Security Cheat Sheet** (least-privilege tool grants; step-up authentication for payment initiation; approval bound to exact action parameters; `transfer_funds` classed CRITICAL): https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html
