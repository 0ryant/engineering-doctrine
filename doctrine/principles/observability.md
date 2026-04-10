# Observability

Durable rules for **logs**, **metrics**, and **traces** so systems can be **understood under failure** and **SLOs** can be measured honestly.

Deployment details (Kubernetes collectors vs **managed** platform ingestion) live in [../tooling/observability.md](../tooling/observability.md). OpenTelemetry and similar specs are **interoperability choices** at boundaries—see [interoperability-and-standards.md](interoperability-and-standards.md) and [timeless-principles-and-tooling.md](timeless-principles-and-tooling.md).

---

## 1. Three Pillars, One Investigation Flow

- **Metrics** — aggregates, rates, saturation; power **SLOs** and dashboards.
- **Logs** — discrete events with context; answer **why** for a time range.
- **Traces** — request-scoped causality across services; answer **where** latency and errors sit.

**Why:** Each signal has different strengths. Metrics do not replace traces; logs without correlation IDs do not scale for distributed debugging.

---

## 2. Correlation And Context

- Propagate **distributed trace context** (W3C Trace Context) across service boundaries.
- **Structured logs** (JSON or equivalent) with **trace_id** and **span_id** aligned to OpenTelemetry so logs and traces join in backends.
- Add **business identifiers** (order id, tenant id) to spans or logs for support workflows; **do not** use high-cardinality IDs as **metric labels** (see cardinality section).

**Why:** OpenTelemetry’s logging model explicitly ties logs to spans for correlation ([OTel log correlation](https://opentelemetry.io/docs/specs/otel/logs/)). Without this, incident response devolves to **grep** and guesswork.

---

## 3. Cardinality And Cost

- **Low-cardinality** labels on metrics (service, route template, region).
- **High-cardinality** values (user id, request id) belong in **traces**, **logs**, or **exemplars**—not as Prometheus-style label sets that explode storage.

**Why:** Metric backends are optimised for aggregate queries; unbounded cardinality breaks cost and performance.

---

## 4. Alerting Philosophy

- Alert on **symptoms** tied to **SLOs** or imminent user impact, not on every threshold.
- **Pages** interrupt humans—reserve for **customer-impacting** or **security** conditions; everything else can be tickets or dashboards.

**Why:** Alert fatigue causes real outages to be ignored; Google SRE material stresses **actionable, user-symptom-based** alerting.

---

## 5. SLIs, Profiling, And Optional Deep Runtime Signals

- **SLIs** — define **quantitative** indicators for each **SLO** (for example **availability** as successful requests / total, **latency** as measured at the **user** or **edge**); keep SLI definitions **stable** so error budgets stay meaningful—see [reliability-slo-incidents.md](reliability-slo-incidents.md).
- **Profiling** — use **CPU** / **heap** profilers and **continuous profiling** products **when** latency or cost regressions are unexplained by metrics alone; run representative **load** before drawing conclusions.
- **eBPF** — optional **kernel-level** visibility for **Linux** estates; treat as **advanced** tooling with clear **ownership** and **safety** review (overhead, PII in probes).

**Why:** Metrics show **that** something is wrong; profiles show **where** hot code paths hide; SLIs tie both to **commitments** users care about.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| OpenTelemetry as the interoperability layer | **Vendor-neutral** API and OTLP reduce lock-in; industry consolidation around OTel. |
| Log–trace correlation by default | Cuts MTTR; supported by OTel SDKs and semantic conventions. |
| Strict metric cardinality discipline | Protects **cost** and **query performance** at scale. |
| Symptom-based paging | Aligns with SRE practice: humans fix what **users** experience. |
| SLI doc stays with SLO doc | Avoids **duplicate** definitions that drift between teams. |

---

## References

- OpenTelemetry project: https://opentelemetry.io/  
- OpenTelemetry **Collector deployment patterns**: https://opentelemetry.io/docs/collector/deployment/  
- OpenTelemetry **scaling** guidance: https://opentelemetry.io/docs/collector/scaling/  
- W3C **Trace Context**: https://www.w3.org/TR/trace-context/  
- OpenTelemetry **log correlation** (example, .NET): https://opentelemetry.io/docs/languages/dotnet/logs/correlation/  
- Google SRE Workbook, **Implementing SLOs** and **Alerting on SLOs**: https://sre.google/workbook/implementing-slos/  
- Google **Cloud Profiler** concepts (illustrative continuous profiling): https://cloud.google.com/profiler/docs/concepts-profiling  
