# Reliability: SLOs, Error Budgets, And Incidents

Durable rules for service level objectives, error budgets, and incident response so reliability is a product and engineering contract, not an aspiration.

---

## 1. Service Level Objectives (SLOs)

- Define a focused set of SLOs tied to user-visible journeys (availability, latency, success rate of critical operations). Typical default: 3–5 SLOs per service (or per clearly bounded user-facing product); fewer is better than many. Add only when a journey is independently owned, measured, and actionable—not one metric per dashboard tile.
- SLOs are agreed between engineering, product, and stakeholders; they are not secretly chosen for easy green dashboards.

**Why:** Google’s SRE books position SLOs as the translation layer between user happiness and measurable metrics. Too many SLOs dilute focus; unrealistic SLOs burn teams without improving trust.

---

## 2. Error Budgets

- Error budget = allowed unreliability (conceptually `100% − SLO` over a window).
- Policy defines what happens when budget is exhausted or nearly exhausted: slow feature work, freeze risky deploys, prioritise reliability fixes—exceptions documented for security or severe customer impact.

**Why:** [Google’s example error budget policy](https://sre.google/workbook/error-budget-policy/) ties budget exhaustion to halted releases (except P0/security) until the service is back within SLO—this encodes trade-offs explicitly instead of arguing every incident.

---

## 3. Incident Response

- Severity levels drive response (who joins, comms cadence, executive escalation).
- Blameless postmortems for material incidents with tracked action items and owners.
- Customer-facing status and comms for user-visible outages per organisational policy.
- A suspected exposure, loss of control, supplier event, recovery action, or notification affecting a declared external profile links the incident to that profile's authority, exact revision, system/data boundary, assessment evidence, and exception/remediation records; see [Revision-Pinned External Control Profiles](../patterns/revision-pinned-control-profiles.md).
- For adoptable depth on incident command, roles, comms cadence, incident state docs, escalation, on-call handoff, sustainable interrupt load, and post-incident action tracking, use [../patterns/incident-lifecycle-and-on-call-operations.md](../patterns/incident-lifecycle-and-on-call-operations.md) (portable pattern; not every team needs every role on day one).
- Estates operating agent responders — AI agents rostered into incident response — additionally apply that pattern §10: a roster role with a named accountable human owner (never IC), remediation routed by reversibility, agent RCA as ranked leads requiring human confirmation, and every agent action in the audit trail; see [../patterns/incident-lifecycle-and-on-call-operations.md](../patterns/incident-lifecycle-and-on-call-operations.md) §10.

**Why:** Severity avoids both under-response (quiet fires) and over-page-everything. Postmortems without actions repeat failures. A separate pattern keeps the principle file stable while the ritual can scale with the org.

---

## 4. Error Budget And Feature Velocity

- Budget not consumed can mean SLOs are too loose or release velocity is too conservative—review periodically.

**Why:** Error budgets are a two-way negotiation: starving innovation is also a failure mode.

---

## 5. Chaos Engineering And Game Days

- Inject controlled faults (latency, error rates, dependency loss) in non-prod first, then limited production experiments under the preconditions and abort criteria that [../patterns/chaos-engineering-and-game-days.md](../patterns/chaos-engineering-and-game-days.md) §§1–2 own.
- Game days cross-functionally validate runbooks, dashboards, and on-call muscle memory—not only automated chaos.

**Why:** *Chaos Engineering* (Netflix Chaos Monkey lineage) and Google SRE disaster testing culture both argue that rehearsed failure teaches more than optimistic architecture diagrams. See Principles of Chaos Engineering: https://principlesofchaos.org/

---

## 6. Toil And Operational Load

- Track toil — repetitive, manual, interrupt-driven work that does not improve the system—and budget reduction alongside feature work.
- Post-incident action items feed DORA change-fail-rate and failed-deployment-recovery-time learning—see [measurement-and-dora.md](measurement-and-dora.md).

**Why:** Google SRE book — Eliminating Toil: https://sre.google/sre-book/eliminating-toil/

---

## 7. Critical Dependency Continuity

When a third-party service (payment API, identity provider, external model API) sits inside a critical user journey, its loss is your incident:

- **Runtime posture per dependency** — explicit timeouts, circuit breaking, and a designed degraded mode (queue-and-retry, cached/stale answers, reduced feature, or degrade to human handling) chosen in advance, not improvised mid-outage ([errors-and-failure-modes.md](errors-and-failure-modes.md) §4 owns timeout, retry, and overload behaviour); dependency error budgets feed the same policy machinery as §2.
- **Substitution readiness scales with criticality** — for dependencies whose loss breaches SLOs: a named substitute (alternate provider, alternate implementation, or manual process), the assets required to switch (data exports, config, portable eval sets for model APIs), and a game day that exercises the switch (§5) — an exit plan that has never run is a hypothesis.
- **Concentration is assessed, not discovered** — know how many critical journeys share one provider before contracting the next one (vocabulary: EU Digital Operational Resilience Act, DORA Art 29, "not easily substitutable"); record it where the estate tracks dependencies. This is the regulatory use of DORA, not the delivery-research programme cited in §6.
- **Provider change is change** — deprecations, silent model upgrades, and SLA shifts trigger the same regression and review path as your own releases.

**Why:** [ai-ml-systems.md](ai-ml-systems.md) §6 treats external model APIs as critical dependencies; this section holds the mechanics that promise relies on. AI-specific procurement/exit detail: [../patterns/ai-adoption-controls.md](../patterns/ai-adoption-controls.md) §4.

---

## 8. Workload Runtime Shape

Applies to production services. Where a managed platform provides one of these properties, the duty is to confirm and configure it, not to rebuild it ([container-runtime-choice.md](container-runtime-choice.md) §1).

- **SHOULD: health signals the platform can act on.** A workload signals whether it is **alive** and whether it is **ready** for traffic as separate questions, and traffic is withheld until it is ready, including during slow start-up. Keep the checks cheap and local: a check that fails when a shared dependency is slow can remove every instance at once.
- **SHOULD: graceful stop, and tolerance of abrupt stop.** On a termination signal a workload reports itself not ready and keeps serving until the platform has stopped routing to it, or for a short configured delay where the platform gives no such signal, because routing can stop at the same moment as the signal and not before it. It then finishes or returns in-flight work and exits within the platform's grace period. It also tolerates being killed without notice, so correctness never depends on a clean shutdown.
- **SHOULD (services with an availability objective, §1): redundancy matched to the objective.** Run more than one instance across the failure domains the platform offers, with enough capacity to lose one, and bound how many instances planned maintenance removes at once. A single instance is a legitimate, recorded choice where the objective allows downtime.
- **SHOULD: declared resource needs.** A workload declares the compute and memory it needs and a memory bound, in the platform's terms, so it is scheduled against real capacity and cannot exhaust its neighbours ([performance-and-cost.md](performance-and-cost.md) §2). Whether to cap CPU is a platform policy choice.

**Why:** without these, a deploy drops requests, a restart sends traffic to an instance that cannot serve, and one failed machine becomes an outage. Evidence note: the properties are supported by documentation from four platform publishers and an edited practitioner book; those sources disagree on what a readiness check may depend on and on CPU caps, so the details stay with tooling ([ADR 0057](../../docs/adr/0057-close-owner-gaps-from-implementation-batch-3.md)).

---

## Related

- Delivery metrics (DORA) — [measurement-and-dora.md](measurement-and-dora.md)
- **AI provider continuity** (due diligence, concentration, exit/substitution) — [../patterns/ai-adoption-controls.md](../patterns/ai-adoption-controls.md) §4
- **Chaos experiments and game days** (pattern) — [../patterns/chaos-engineering-and-game-days.md](../patterns/chaos-engineering-and-game-days.md)
- Incident lifecycle, on-call, escalation, comms, handoff, and post-incident actions (pattern) — [../patterns/incident-lifecycle-and-on-call-operations.md](../patterns/incident-lifecycle-and-on-call-operations.md)

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Tie policy to budget state | Makes reliability actionable—not just dashboards. |
| ~3–5 SLOs per service (typical) | Enough to cover critical journeys without diluting focus or error-budget debate. |
| Documented exceptions | Security and existential risk cannot wait for budget recovery—process replaces panic. |
| Blameless culture | Improves signal quality in postmortems; fear hides defects. |
| Workload runtime shape (§8) | Health signals, graceful stop, redundancy, and declared resources are what make deploys and single failures uneventful; stated as properties because platforms differ in mechanism ([ADR 0057](../../docs/adr/0057-close-owner-gaps-from-implementation-batch-3.md)). The stop wording was sharpened so a workload keeps serving until routing stops ([ADR 0058](../../docs/adr/0058-sharpen-four-rules-after-the-november-2026-review.md)). |

---

## References

- Google SRE Workbook — Error Budget Policy: https://sre.google/workbook/error-budget-policy/  
- Google SRE Workbook — Implementing SLOs: https://sre.google/workbook/implementing-slos/  
- *Site Reliability Engineering* (O’Reilly, Google) — Monitoring Distributed Systems and Eliminating Toil (foundational context): https://sre.google/sre-book/table-of-contents/  
- **Principles of Chaos Engineering** (community): https://principlesofchaos.org/  
- Kubernetes documentation — **probes**, **pod termination**, **disruptions**, and **resource management** (S5, product-scoped; accessed 2026-11-18): https://kubernetes.io/docs/concepts/workloads/pods/probes/  
- AWS Well-Architected Framework — **REL10-BP01** multiple locations, **REL11-BP02** fail over to healthy resources (S5; accessed 2026-11-18): https://docs.aws.amazon.com/wellarchitected/latest/framework/rel10-bp01.html  
- Azure Architecture Center — **Health Endpoint Monitoring** pattern (S5; 2026-09-24; accessed 2026-11-18): https://learn.microsoft.com/en-us/azure/architecture/patterns/health-endpoint-monitoring  
- Google SRE Book — **Load Balancing in the Datacenter** (ch. 20; draining and health states) (S4; accessed 2026-11-18): https://sre.google/sre-book/load-balancing-datacenter/  
- *The Twelve-Factor App* — **Disposability** (S6; accessed 2026-11-18): https://12factor.net/disposability  
- Kubernetes documentation — **Termination of Pods** (endpoint removal runs alongside graceful shutdown) (S5, product-scoped; accessed 2026-11-18): https://kubernetes.io/docs/concepts/workloads/pods/pod-termination/  
