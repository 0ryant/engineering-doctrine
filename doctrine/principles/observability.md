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

Tiers separate **mandatory** SLO plumbing from **optional** deep diagnostics.

### 5.1 SLIs (Required When SLOs Exist)

- **Must** when the service has **SLOs**: each SLO has **one or more** **SLIs** with a **written** definition (numerator, denominator, window, and **where** measured—edge vs service). Keep definitions **stable** across quarters unless the SLO itself changes—see [reliability-slo-incidents.md](reliability-slo-incidents.md).

**Why:** Error budgets are meaningless if the **SLI formula** drifts silently.

### 5.2 Profiling (When Metrics Are Insufficient)

- **Should** when latency or CPU **regressions** are unexplained after checking **SLOs**, **deploys**, and **dependency** changes: run **CPU** / **heap** profiles under **representative** load (see [performance-and-cost.md](performance-and-cost.md)).
- **Optional** as a **continuous** product in mature estates—not a day-one gate for every service.

**Why:** Profiles locate **hot paths** metrics aggregate away.

### 5.3 eBPF And Kernel-Level Probes (Advanced)

- **Optional** for **Linux** estates with **platform** support: use only with **documented** owners, **overhead** limits, and **PII** review on captured data.

**Why:** Power without **governance** risks **privacy** and **stability** incidents.

---

## 6. Multi-Window Burn-Rate Alerting

Alert on **how fast the error budget is being consumed**, not just on instantaneous error rate. A single-window alert on raw error rate misses slow leaks and floods on spikes that resolved quickly.

### 6.1 Burn-Rate Definition

```
burn_rate = current_error_rate / SLO_error_budget_rate
```

Where `SLO_error_budget_rate = 1 − SLO_target`. For a 99.9% availability SLO, the error budget rate is `0.001` (0.1%). A burn rate of 1 means the budget is being consumed at exactly the sustainable pace for the window. A burn rate of 14.4 for one hour means the entire monthly budget would be gone in ~2 days.

### 6.2 Multi-Window Model

Use **paired windows** (long + short) to filter out transient spikes. An alert fires only when **both** windows show elevated burn. This suppresses false pages from momentary errors and prevents delayed detection of slow burns.

| Burn-rate threshold | Long window | Short window | Budget fraction consumed | Routing |
| --- | --- | --- | --- | --- |
| **14.4×** | 1 hour | 5 minutes | ~2% in 1h | **Page** (fast burn) |
| **6×** | 6 hours | 30 minutes | ~5% in 6h | **Page** (fast burn) |
| **1×** | 3 days | 6 hours | ~10% in 3d | **Ticket** (slow burn) |

- Fast burn (14.4× or 6×) → immediate page; the budget will exhaust within hours if unchecked.
- Slow burn (1×) → ticket for the responsible team; budget is leaking but not critically.
- Reset pages when burn rate drops below threshold in the short window.

### 6.3 PromQL Patterns

Define recording rules first to avoid query duplication and reduce evaluation load:

```yaml
# Recording rule — error ratio over window
- record: job:request_error_ratio:rate1h
  expr: |
    sum(rate(http_requests_total{status=~"5.."}[1h]))
    / sum(rate(http_requests_total[1h]))

- record: job:request_error_ratio:rate5m
  expr: |
    sum(rate(http_requests_total{status=~"5.."}[5m]))
    / sum(rate(http_requests_total[5m]))
```

```yaml
# Alerting rule — fast burn (1h + 5m paired windows)
- alert: ErrorBudgetBurnFast
  expr: |
    job:request_error_ratio:rate1h > (14.4 * 0.001)
    and
    job:request_error_ratio:rate5m > (14.4 * 0.001)
  for: 2m
  labels:
    severity: page
  annotations:
    summary: "Fast error budget burn — {{ $labels.job }}"
    description: "Burn rate >14.4× on 1h+5m windows. ~2% monthly budget at risk."

# Alerting rule — slow burn (3d + 6h paired windows)
- alert: ErrorBudgetBurnSlow
  expr: |
    job:request_error_ratio:rate3d > (1 * 0.001)
    and
    job:request_error_ratio:rate6h > (1 * 0.001)
  for: 1h
  labels:
    severity: ticket
  annotations:
    summary: "Slow error budget burn — {{ $labels.job }}"
    description: "Burn rate ≥1× sustained over 3d+6h. Review before budget exhaustion."
```

Replace `0.001` with `1 − SLO_target` for your service. Replace `http_requests_total` with your service's request counter metric.

### 6.4 Common Failure Modes

| Failure mode | Symptom | Fix |
| --- | --- | --- |
| **Single-window alert** | Pages on transient spikes; misses slow leaks | Add the paired short window `and` clause |
| **Alert on raw error rate, not burn rate** | Fires equally at low and high traffic; meaningless at night | Compute error ratio, then multiply by burn-rate threshold |
| **Threshold copied from a different SLO** | Wrong budget fraction for service's actual SLO | Derive threshold from `(1 − SLO_target)` explicitly |
| **No slow-burn alert** | Budget silently exhausts over days; incident surprised | Add the 3d+6h tier routed to ticket/work queue |
| **Page fatigue from 14.4× tier alone** | On-call desensitised; slow fires silently | Use all three tiers; route slow burn to ticket not page |

**Why:** The Google SRE Workbook multi-burn-rate model is the industry standard for SLO-based alerting. Single-threshold or raw-rate alerts produce either excessive noise or silent budget exhaustion — both degrade on-call health and SLO reliability.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| OpenTelemetry as the interoperability layer | **Vendor-neutral** API and OTLP reduce lock-in; industry consolidation around OTel. |
| Log–trace correlation by default | Cuts MTTR; supported by OTel SDKs and semantic conventions. |
| Strict metric cardinality discipline | Protects **cost** and **query performance** at scale. |
| Symptom-based paging | Aligns with SRE practice: humans fix what **users** experience. |
| SLI doc stays with SLO doc | Avoids **duplicate** definitions that drift between teams. |
| Tiered §5 | **SLIs** are mandatory with SLOs; profiling/eBPF stay **optional** power tools. |
| Multi-window burn-rate alerting (§6) | Prevents both false pages (single window) and silent budget exhaustion (no slow-burn tier). Model from Google SRE Workbook. |

---

## References

- OpenTelemetry project: https://opentelemetry.io/
- OpenTelemetry **Collector deployment patterns**: https://opentelemetry.io/docs/collector/deployment/
- OpenTelemetry **scaling** guidance: https://opentelemetry.io/docs/collector/scaling/
- W3C **Trace Context**: https://www.w3.org/TR/trace-context/
- OpenTelemetry **log correlation** (example, .NET): https://opentelemetry.io/docs/languages/dotnet/logs/correlation/
- Google SRE Workbook, **Implementing SLOs**: https://sre.google/workbook/implementing-slos/
- Google SRE Workbook, **Alerting on SLOs** (multi-burn-rate model): https://sre.google/workbook/alerting-on-slos/
- Google **Cloud Profiler** concepts (illustrative continuous profiling): https://cloud.google.com/profiler/docs/concepts-profiling
