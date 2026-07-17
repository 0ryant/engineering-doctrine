# Reliability: SLOs, Error Budgets, And Incidents

Durable rules for **service level objectives**, **error budgets**, and **incident response** so reliability is a **product and engineering contract**, not an aspiration.

---

## 1. Service Level Objectives (SLOs)

- Define **a focused set** of SLOs tied to **user-visible** journeys (availability, latency, success rate of critical operations). **Typical default:** **3–5** SLOs **per service** (or per **clearly bounded** user-facing product); fewer is better than many. Add **only** when a journey is **independently** owned, **measured**, and **actionable**—not one metric per dashboard tile.
- SLOs are **agreed** between engineering, product, and stakeholders; they are not secretly chosen for easy green dashboards.

**Why:** Google’s SRE books position SLOs as the **translation layer** between user happiness and measurable metrics. Too many SLOs dilute focus; unrealistic SLOs burn teams without improving trust.

---

## 2. Error Budgets

- **Error budget** = allowed unreliability (conceptually `100% − SLO` over a window).
- **Policy** defines what happens when budget is exhausted or nearly exhausted: slow feature work, freeze risky deploys, prioritise reliability fixes—**exceptions** documented for security or severe customer impact.

**Why:** [Google’s example error budget policy](https://sre.google/workbook/error-budget-policy/) ties budget exhaustion to **halted releases** (except P0/security) until the service is back within SLO—this encodes **trade-offs** explicitly instead of arguing every incident.

---

## 3. Incident Response

- **Severity** levels drive response (who joins, comms cadence, executive escalation).
- **Blameless postmortems** for material incidents with **tracked action items** and owners.
- **Customer-facing status** and comms for user-visible outages per organisational policy.
- A suspected exposure, loss of control, supplier event, recovery action, or notification affecting a declared external profile links the incident to that profile's authority, exact revision, system/data boundary, assessment evidence, and exception/remediation records; see [Revision-Pinned External Control Profiles](../patterns/revision-pinned-control-profiles.md).
- For **adoptable** **depth** on **incident command**, **roles**, **comms cadence**, **incident state docs**, **escalation**, **on-call handoff**, **sustainable** **interrupt load**, and **post-incident** **action** **tracking**, use [../patterns/incident-lifecycle-and-on-call-operations.md](../patterns/incident-lifecycle-and-on-call-operations.md) (portable pattern; not every team needs every **role** on day one).

**Why:** Severity avoids both **under-response** (quiet fires) and **over-page-everything**. Postmortems without actions repeat failures. A **separate** pattern keeps the **principle** file stable while the **ritual** can **scale** with the org.

---

## 4. Error Budget And Feature Velocity

- Budget **not** consumed can mean SLOs are too loose or release velocity is too conservative—review periodically.

**Why:** Error budgets are a **two-way** negotiation: starving innovation is also a failure mode.

---

## 5. Chaos Engineering And Game Days

- **Inject** controlled faults (latency, error rates, dependency loss) in **non-prod** first, then **limited** prod experiments with **blast radius** caps and **abort** criteria.
- **Game days** cross-functionally validate runbooks, dashboards, and **on-call** muscle memory—not only automated chaos.

**Why:** *Chaos Engineering* (Netflix **Chaos Monkey** lineage) and Google SRE **disaster** testing culture both argue that **rehearsed** failure teaches more than optimistic architecture diagrams. See **Principles of Chaos Engineering**: https://principlesofchaos.org/

---

## 6. Toil And Operational Load

- Track **toil** — repetitive, manual, interrupt-driven work that does not improve the system—and **budget** reduction alongside feature work.
- **Post-incident** action items feed **DORA** change-failure and restore-time learning—see [measurement-and-dora.md](measurement-and-dora.md).

**Why:** Google SRE book — **Eliminating Toil**: https://sre.google/sre-book/eliminating-toil/

---

## 7. Critical Dependency Continuity

When a **third-party service** (payment API, identity provider, **external model API**) sits inside a critical user journey, its loss is **your** incident:

- **Runtime posture per dependency** — explicit **timeouts**, **circuit breaking**, and a **designed degraded mode** (queue-and-retry, cached/stale answers, reduced feature, or **degrade to human handling**) chosen **in advance**, not improvised mid-outage ([errors-and-failure-modes.md](errors-and-failure-modes.md)); dependency error budgets feed the same policy machinery as §2.
- **Substitution readiness scales with criticality** — for dependencies whose loss breaches SLOs: a named **substitute** (alternate provider, alternate implementation, or manual process), the assets required to switch (data exports, config, **portable eval sets** for model APIs), and a **game day** that exercises the switch (§5) — an exit plan that has never run is a hypothesis.
- **Concentration is assessed, not discovered** — know how many critical journeys share one provider **before** contracting the next one (vocabulary: DORA Art 29 "not easily substitutable"); record it where the estate tracks dependencies.
- **Provider change is change** — deprecations, silent model upgrades, and SLA shifts trigger the same regression and review path as your own releases.

**Why:** [ai-ml-systems.md](ai-ml-systems.md) §6 treats external model APIs as critical dependencies; this section holds the mechanics that promise relies on. AI-specific procurement/exit detail: [../patterns/ai-adoption-controls.md](../patterns/ai-adoption-controls.md) §4.

---

## Related

- Organisation-level **delivery** metrics (DORA / Four Keys) — [measurement-and-dora.md](measurement-and-dora.md)
- **AI provider continuity** (due diligence, concentration, exit/substitution) — [../patterns/ai-adoption-controls.md](../patterns/ai-adoption-controls.md) §4
- **Chaos experiments and game days** (pattern) — [../patterns/chaos-engineering-and-game-days.md](../patterns/chaos-engineering-and-game-days.md)
- **Incident lifecycle, on-call, escalation, comms, handoff, and post-incident** **actions** (pattern) — [../patterns/incident-lifecycle-and-on-call-operations.md](../patterns/incident-lifecycle-and-on-call-operations.md)

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Tie policy to budget state | Makes reliability **actionable**—not just dashboards. |
| ~3–5 SLOs per service (typical) | Enough to cover **critical** journeys without **diluting** focus or error-budget debate. |
| Documented exceptions | Security and existential risk cannot wait for budget recovery—**process** replaces panic. |
| Blameless culture | Improves **signal quality** in postmortems; fear hides defects. |

---

## References

- Google SRE Workbook — **Error Budget Policy**: https://sre.google/workbook/error-budget-policy/  
- Google SRE Workbook — **Implementing SLOs**: https://sre.google/workbook/implementing-slos/  
- *Site Reliability Engineering* (O’Reilly, Google) — **Monitoring Distributed Systems** and **Eliminating Toil** (foundational context): https://sre.google/sre-book/table-of-contents/  
- **Principles of Chaos Engineering** (community): https://principlesofchaos.org/  
