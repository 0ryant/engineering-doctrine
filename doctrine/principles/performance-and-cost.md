# Performance, Load, And Cost

Durable rules for **non-functional requirements**: latency budgets, **load validation**, and **cloud cost** discipline so performance and spend stay **observable and owned**.

---

## 1. Performance Budgets

- Define **latency** and **throughput** expectations for **critical paths** (for example p95/p99 API latency, job completion time).
- Regressions beyond budget are **release blockers** unless explicitly accepted with rationale.

**Why:** Without budgets, optimisations are arbitrary and regressions repeat until users complain.

---

## 2. Load And Capacity

- **Load tests** run before major launches or **order-of-magnitude** traffic changes; scenarios reflect **realistic** mixes (not only peak RPS).
- **Capacity** plans connect traffic forecasts to **autoscaling** limits, quotas, and **database** headroom.

**Why:** Synthetic tests miss reality, but **no** load testing misses obvious bottlenecks before they hit production.

---

## 3. FinOps And Cost Observability

- **Tag** cloud resources (team, service, environment, cost centre) consistently.
- **Alerts** on **spend anomalies** and **third-party API** bills where spend is material.
- **Right-size** after observing **utilisation**, not upfront guesses alone.

**Why:** OWASP API **API4** includes uncontrolled **spend** via third-party APIs; internal cost surprises are **operational** incidents for many teams.

---

## 4. Sustainability And Carbon Awareness

- **Measure** energy and emissions **where** your cloud or hosting provider exposes **carbon** or **grid** signals; tag workloads for **attribution** the same way as cost.
- **Optimise** **meaningfully**—**empty** clusters, **over-provisioned** dev estates, and **always-on** sandboxes often dominate **embodied** waste before micro-optimising code paths.
- **Software Carbon Intensity (SCI)** and related **Green Software Foundation** guidance provide a **normalised** framing when customers ask for **sustainability** evidence—adopt **metrics** that match your **reporting** obligations.

**Why:** Enterprise RFPs and **CSRD**-class reporting increasingly ask for **digital** sustainability posture; FinOps and **carbon** budgets are converging for large estates.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Budgets on critical paths only | Avoids bureaucracy on low-impact surfaces while protecting **user trust**. |
| Load test major changes | Cheaper than **firefighting** at launch. |
| Tagging + anomaly alerts | Makes cost **actionable**; untagged spend is not attributable. |
| Carbon as NFR where required | Avoids **greenwashing**—tie claims to **provider** data and **bounded** SCI-style metrics when reporting. |

---

## References

- OWASP **API4:2023** — Unrestricted Resource Consumption (includes provider spend): https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/  
- FinOps Foundation — **FinOps Definition** and principles: https://www.finops.org/introduction/what-is-finops/  
- Google SRE Book — **Handling Overload** (conceptual framing for capacity and graceful degradation): https://sre.google/sre-book/handling-overload/  
- Green Software Foundation — **Software Carbon Intensity (SCI)** specification: https://sci.greensoftware.foundation/  
