# Observability Tooling

Illustrative patterns for [../principles/observability.md](../principles/observability.md). Backends, agents, and collectors are **estate choices**—see [../principles/timeless-principles-and-tooling.md](../principles/timeless-principles-and-tooling.md). **Preserve** correlation IDs, structured logs, and cardinality discipline regardless of vendor.

**Not Kubernetes-only:** Many estates use **vendor-managed** application platforms with **platform-managed** telemetry ingestion. Self-managed Collector **DaemonSets** are **one** pattern when you operate clusters—not a universal mandate—see [interoperability-and-standards.md](../principles/interoperability-and-standards.md).

---

## Default Stack (Instrumentation)

| Concern | Default | Swappable alternatives |
| --- | --- | --- |
| **Instrumentation API** | **OpenTelemetry** language SDKs | Vendor-native agents where OTel is impossible (document exception) |
| **Wire protocol** | **OTLP** (gRPC `4317`, HTTP `4318`) when exporting to a collector or compatible backend | Vendor-native export when the backend only accepts a proprietary protocol (prefer OTel bridges where available) |
| **Backend** | Organisation-chosen (cloud provider suite, SaaS APM, self-hosted) | Must still support **trace–log correlation** in practice |

---

## Managed And Non-Kubernetes Deployments

When workloads run on **PaaS**, **serverless containers**, or **vendor-managed** environments without node-level agents:

- Instrument apps with **OTel SDKs** and export via **OTLP to a managed gateway** or use your **vendor’s** supported OpenTelemetry ingestion path (consult current vendor docs).
- Prefer **one** blessed export path per environment; avoid duplicate agents (OTel + legacy agent) unless the vendor requires a transition plan.
- **Logs**: structured logs with `trace_id` / `span_id`; ingest via your platform’s logging pipeline—correlation fields must survive ingestion mapping.

**Why:** CNCF Collector patterns were written for clusters; **enterprise** platforms often ingest telemetry **without** you operating a DaemonSet. The **invariant** is correlated signals, not a specific CNCF deployment topology.

---

Estate example (Azure-oriented): [estates/azure-container-runtimes.md](estates/azure-container-runtimes.md).

---

## Collector Deployment (Kubernetes — When You Run Clusters)

When the organisation **does** operate Kubernetes, use Collector patterns from the OpenTelemetry project:

Follow OpenTelemetry’s documented **deployment patterns** (supplemental to managed-PaaS paths above):

- **Agent** — per-node collection, local OTLP receive, forward to gateway.
- **Gateway** — centralised processing, tail sampling (if used), export to backends.
- Use **gRPC-aware** load balancing when scaling gateway replicas (L4 balancers can pin connections and negate scale-out).

Official guidance: [Deploy the Collector](https://opentelemetry.io/docs/collector/deployment/), [Scaling the Collector](https://opentelemetry.io/docs/collector/scaling/).

**Why these defaults:** The Collector is **vendor-neutral**, supports **batching** and **tail sampling** at the right tier, and avoids N×direct-to-vendor exporters from every pod at large N.

---

## Log Pipeline

- Prefer **structured logs** with **trace_id** / **span_id** fields populated from the active span ([OTel log correlation model](https://opentelemetry.io/docs/specs/otel/logs/)).
- Ship logs via **OTLP logs** or file tailing into the Collector — **one** blessed path per cluster.

**Why:** Duplicated ad-hoc log shippers create **different schemas** and break correlation.

---

## Metrics And Labels

- Use **OTel semantic conventions** and **Prometheus-compatible** exposition where metrics backends expect it.
- Enforce **label allowlists** in CI or policy-as-code for custom metrics.

**Why:** Prevents cardinality explosions discovered only after production deploy.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| OTel + OTLP as default | Industry **convergence**; reduces bespoke instrumentation. |
| Managed-first export where no cluster | **Managed** runtimes often ingest telemetry without node agents—avoid assuming **self-managed** Kubernetes in docs or designs. |
| Collector tier **when on K8s** | Offloads **batching**, **retry**, and **PII scrubbing** (if configured) from app processes at scale. |
| Gateway for tail sampling (cluster pattern) | Sampling needs **complete trace** views; DaemonSet-only sampling is **incorrect** for cross-node traces. |
| Semantic conventions | Makes dashboards and alerts **portable** across services. |

---

## References

- OpenTelemetry — **Deploy the Collector**: https://opentelemetry.io/docs/collector/deployment/  
- OpenTelemetry — **Scaling the Collector**: https://opentelemetry.io/docs/collector/scaling/  
- OpenTelemetry — **Collector hosting best practices** (security): https://opentelemetry.io/docs/security/collector-hosting/  
- OpenTelemetry — **Semantic Conventions**: https://opentelemetry.io/docs/specs/semconv/  
