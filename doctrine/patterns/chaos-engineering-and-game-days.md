# Chaos Engineering And Game Days (Pattern)

Companion to [reliability-slo-incidents.md](../principles/reliability-slo-incidents.md) §§5–6. **Principle** files state *why*; this pattern gives a **repeatable** shape for **exercises** without mandating a vendor (Gremlin, Litmus, home-grown scripts).

---

## Intent

- **Prove** (not assume) that **runbooks**, **dashboards**, **alerts**, and **dependency** behaviour work under **partial failure**.
- Build **muscle memory** for **on-call** and **incident command** in a **controlled** setting.

---

## 1. Scope And Preconditions

- **Non-production first** — inject faults in **staging** or a **dedicated** chaos environment that mirrors **production** topology enough to matter.
- **Production** experiments only with **explicit** approval, **SLO** headroom, **blast-radius** caps (single cell, single AZ, **canary** pool), **kill switch**, and **rollback** path documented.
- **Forbidden** without executive + legal review: data **corruption** tests, **privacy**-violating probes, or faults that violate **regulator** or **contract** boundaries.

---

## 2. Chaos Experiment (Minimal Template)

| Field | Content |
| --- | --- |
| **Hypothesis** | “When X fails, users still get Y within SLO” |
| **Blast radius** | Which service, region, % traffic |
| **Fault** | Latency, error rate, partition, CPU, dependency down |
| **Abort** | Metric threshold or human **stop** that ends the test |
| **Success criteria** | SLO maintained **or** graceful degradation per design |
| **Rollback** | How to return to **known-good** within **N** minutes |

Record **results** in a **short** log (wiki, ADR appendix, or ticket)—link to **dashboard** snapshots.

---

## 3. Game Day (Cross-Functional)

- **Participants:** on-call engineer, **optional** secondary, product/comms **observer**, **SRE** or platform **facilitator**.
- **Agenda (example, ~2–3 h):** review **hypothesis** → run **one** major scenario (e.g. **region** dependency loss) → **execute** runbook steps → **retro** (what broke, what to fix).
- **Frequency:** **quarterly** for **tier-1** revenue or safety paths; **after** major architecture changes within **60 days**—align with [documentation-knowledge.md](../principles/documentation-knowledge.md) runbook cadence where practical.

---

## 4. Relation To Error Budgets

- Chaos and game days **consume** **risk** budget in the sense of **engineering** time and **possible** brief degradation—schedule when **error budget** is **healthy**, not during **recovery** from a real outage unless **explicitly** justified.

---

## References

- **Principles of Chaos Engineering**: https://principlesofchaos.org/  
- Google SRE Workbook — related **disaster** and **load** testing culture: https://sre.google/sre-book/table-of-contents/  
