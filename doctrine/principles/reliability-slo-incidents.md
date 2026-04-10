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

**Why:** Severity avoids both **under-response** (quiet fires) and **over-page-everything**. Postmortems without actions repeat failures.

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

## Related

- Organisation-level **delivery** metrics (DORA / Four Keys) — [measurement-and-dora.md](measurement-and-dora.md)

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
