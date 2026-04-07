# Supplement: Azure Container Runtimes (Example Estate)

**Scope:** Optional mapping for teams standardising on **Microsoft Azure**. This is **one** estate’s concrete choices; it does **not** override portable principles in `doctrine/principles/`. See [README.md](README.md) and [../../principles/timeless-principles-and-tooling.md](../../principles/timeless-principles-and-tooling.md).

For the vendor-neutral decision frame, see [../../principles/container-runtime-choice.md](../../principles/container-runtime-choice.md).

---

## Example Preference Within This Estate

| When | Typical choice on Azure |
| --- | --- |
| HTTP APIs, workers, event-driven workloads that fit **managed** container constraints | **Azure Container Apps** (fewer self-managed control-plane responsibilities than operating many AKS clusters) |
| Need **full Kubernetes API**, bespoke CNI/node control, or operators not satisfied above | **Azure Kubernetes Service (AKS)** — document **why** in an ADR or platform catalogue |

**Note:** Product names, SKUs, and feature boundaries change; treat this table as **starting guidance** for this estate, not immutable law.

---

## Observability (Azure)

- **Azure Monitor** is a common backend when applications export via **OpenTelemetry** to Azure-supported endpoints—see [../observability.md](../observability.md) for the general “managed ingestion” pattern.
- Current Microsoft Learn entry point: https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable

---

## Identity

- Prefer **managed identity** and **Microsoft Entra ID** integration per current Azure documentation for your workload type; avoid long-lived client secrets in application configuration.

---

## References

- Azure Container Apps overview: https://learn.microsoft.com/en-us/azure/container-apps/overview  
- AKS overview: https://learn.microsoft.com/en-us/azure/aks/intro-kubernetes  
- Container Apps logging: https://learn.microsoft.com/en-us/azure/container-apps/log-monitoring  
