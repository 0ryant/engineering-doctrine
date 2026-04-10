# Interoperability, Standards, And Vendor Reality

This doctrine may cite **open specifications** (for example **CloudEvents**, **OpenTelemetry**) that are often published through **vendor-neutral** foundations. That is an **interoperability** choice at **boundaries**—not a requirement to adopt any particular **full** product stack or to run **Kubernetes** everywhere.

---

## 1. Standards Are Wire And Contract Shapes

- **CloudEvents** — portable **event envelope** for queues, buses, and HTTP callbacks; avoids bespoke headers per team.
- **OpenTelemetry** — portable **instrumentation** and **OTLP**-style export where used; backends may be **vendor SaaS**, **cloud observability suites**, or **self-hosted**.

**Why:** Managed runtimes and **PaaS** still require **stable contracts** between services. Vendor-neutral specs at the **contract** layer reduce lock-in while letting each org pick **runtime and backend** freely.

---

## 2. Managed Platforms And Operational Sprawl

- Prefer **managed application platforms** when they meet security, networking, and compliance needs and **materially reduce** self-operated control planes—see [container-runtime-choice.md](container-runtime-choice.md).
- **Kubernetes** is appropriate when **cluster-level** capabilities are required; concrete product names belong in **estate** supplements (`doctrine/tooling/estates/`), not in portable principles.

**Why:** Outcomes (small blast radius, clear ownership) matter more than a uniform **CNCF** footprint.

---

## 3. Observability Without “Cluster Orthodoxy”

- The **three signals** (logs, metrics, traces) and **correlation** are invariant.
- **How** telemetry is collected (daemonset, sidecar, agent, or **platform-managed** ingestion) is **tooling**—see [../tooling/observability.md](../tooling/observability.md).

**Why:** Basing observability doctrine only on **self-managed cluster** patterns would exclude common **enterprise** deployments.

---

## 4. gRPC And Protobuf As First-Class Alternatives

- Where **strong typing**, **streaming**, or **efficient** on-the-wire representation matter, **gRPC** over **HTTP/2** with **Protocol Buffers** is a valid **contract-first** choice alongside REST + JSON + OpenAPI.
- Treat `.proto` files and **package** / **version** conventions as **source of truth**; generate stubs in CI with pinned **protoc** / plugins for reproducibility.
- **Interoperability** with browsers or third parties that cannot speak gRPC may require a **gateway** (for example gRPC-Web, JSON transcoding)—document that boundary explicitly.

**Why:** Many internal service meshes standardise on gRPC; portable doctrine should not **assume** JSON-only HTTP.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Cite specs, not stacks | Teams may use **zero** projects from a foundation’s landscape and still use **OTel + CloudEvents**. |
| Estate-specific names in `tooling/estates/` | Keeps principles **readable** outside one cloud. |
| Minimum standard surface | Avoids standards creep. |
| gRPC / Protobuf optional parity | **JSON + OpenAPI** and **gRPC + proto** are both valid **contracts-first** stacks; pick per boundary and record gateways where needed. |

---

## References

- CNCF landscape (informational only): https://landscape.cncf.io/  
- CNCF home: https://www.cncf.io/  
- **gRPC** — A high-performance, open-source universal RPC framework: https://grpc.io/  
- **Protocol Buffers** — Language-neutral, platform-neutral extensible mechanisms for serialising structured data: https://protobuf.dev/  
