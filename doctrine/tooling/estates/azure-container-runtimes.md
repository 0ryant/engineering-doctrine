# Supplement: Azure Container Runtimes (Example Estate)

**Scope:** Optional mapping for teams standardising on **Microsoft Azure**. This is **one** estate’s concrete choices; it does **not** override portable principles in `doctrine/principles/`. See [README.md](README.md) and [../../principles/timeless-principles-and-tooling.md](../../principles/timeless-principles-and-tooling.md).

For the vendor-neutral decision frame, see [../../principles/container-runtime-choice.md](../../principles/container-runtime-choice.md). For Microsoft's own guide across all its compute services, start from its [compute decision tree](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree).

---

## Example Preference Within This Estate

| When | Typical choice on Azure |
| --- | --- |
| HTTP APIs, workers, event-driven workloads that fit **managed** container constraints | **Azure Container Apps**: no cluster to operate |
| The Kubernetes API is needed, but the team wants Azure to choose node, scaling and security defaults | **AKS Automatic** |
| Full Kubernetes control: bespoke networking, node configuration, or operators the options above do not support | **AKS** standard cluster: Azure manages the control plane; the team owns node pools, upgrades, add-ons and cluster configuration. Document **why** in an ADR or platform catalogue |

**Note:** Product names, SKUs, and feature boundaries change; treat this table as **starting guidance** for this estate, not immutable law. Check limits and regional availability on the product pages before standardising.

---

## Observability (Azure)

- **Azure Monitor** is a common backend when applications export via **OpenTelemetry** to Azure-supported endpoints—see [../observability.md](../observability.md) for the general “managed ingestion” pattern.
- Current Microsoft Learn entry point: https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable

---

## Identity

- Use **managed identity** and **Microsoft Entra ID** integration by default, per current Azure documentation for your workload type; a long-lived client secret is a registered fallback under zero trust §2, not a configuration default.
- Workloads and pipelines outside Azure reach it through [workload identity federation](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation), which exchanges a trusted token from their own identity provider for a Microsoft token, with no stored secret.

---

## References

- Azure Architecture Center — **Choose an Azure compute service** (decision tree; accessed 2026-11-20): https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree
- Azure Container Apps overview: https://learn.microsoft.com/en-us/azure/container-apps/overview  
- AKS overview (control plane managed by the Azure platform; accessed 2026-11-20): https://learn.microsoft.com/en-us/azure/aks/what-is-aks
- AKS Automatic overview (accessed 2026-11-20): https://learn.microsoft.com/en-us/azure/aks/intro-aks-automatic
- Container Apps logging: https://learn.microsoft.com/en-us/azure/container-apps/log-monitoring  
- Microsoft Entra — **workload identity federation** (accessed 2026-11-20): https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation
