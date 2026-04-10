# Container Runtime Choice: Managed Platforms Vs Kubernetes

Durable rules for **where** containerised workloads run. The goal is **operational sobriety**: fewer self-managed control planes unless capabilities or constraints genuinely require them—**regardless of cloud**.

---

## 1. Prefer Managed Application Runtimes When They Fit

- When a **vendor-managed** application platform meets security, networking, compliance, and scaling needs, prefer it over operating **your own** Kubernetes cluster for that workload.
- Maintain an **estate catalogue** (or platform decision record) that names **your** organisation’s blessed managed path per environment—not every reader shares the same vendor.

**Why:** Self-managed **Kubernetes** multiplies responsibilities: control plane lifecycle, node pools, CNI, add-ons, cluster RBAC, and platform security baselines. Teams often accumulate **too many** clusters with **too little** platform engineering capacity; managed runtimes narrow the surface **you** own.

---

## 2. When Kubernetes Is Justified

- Choose **Kubernetes** (any certified distribution—cloud-managed control plane or on-prem) when you need **full cluster semantics**: deep node/OS control, bespoke networking or policy at node boundary, large operator ecosystems, or features **not** exposed by your managed application platform.
- The decision is **documented** (ADR or platform catalogue), not habitual.

**Why:** Kubernetes is **powerful** and **expensive** to operate well; it should be a **deliberate** trade when requirements exceed what a managed application layer offers.

---

## 3. Same Discipline Regardless Of Runtime

- **Images** stay minimal, non-root by default, scanned in CI (aligned with `ENGINEERING.md` container strategy).
- **Secrets** are not baked into images; prefer **short-lived** credentials and **workload identity** where the platform supports it.
- **Observability** and **contracts** do not change—only the **plumbing** does.

---

## 4. Security Posture When On Kubernetes

- If the estate runs Kubernetes, apply **[kubernetes-platform-security.md](kubernetes-platform-security.md)**.

---

## 5. Edge, Windows, And Device Runtimes

- **Edge / IoT** — constrained devices may use **lightweight** runtimes (for example **containerd**-class, **micro-VMs**, or **static** binaries) instead of full clusters; record **update**, **observability**, and **SBOM** expectations per fleet.
- **Windows containers** — viable for **.NET** and Windows-only dependencies; image **size** and **patch** cadence differ from Linux—capture the **estate** choice in `tooling/estates/` when Windows Server / Azure Windows paths are in play.

**Why:** The same **managed vs self-operated** trade applies at the **edge**; pretending every workload is Linux-on-Kubernetes creates **hidden** platform teams.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Managed-first **when fit** | Reduces **undifferentiated** ops and blast radius; not every team should be a mini-platform org. |
| K8s when semantics require | Avoids **fighting** a managed layer with requirements it cannot satisfy. |
| Catalogue in estate docs | Keeps principles **agnostic** while giving each org a **single** place for named products. |
| Edge/Windows explicit | Avoids **silent** exclusion of non-Linux estates from doctrine. |

---

## References

- **Kubernetes** — project overview (what “full cluster” implies): https://kubernetes.io/docs/concepts/overview/  
- **KEDA** — event-driven autoscaling (often used **with** Kubernetes; some managed products embed similar patterns): https://keda.sh/  
- Vendor **managed container** and **Kubernetes** offerings — use **your** cloud’s documentation for comparative tables; do not copy product picks into portable principles.  
- Microsoft Learn — **Windows containers** overview (when evaluating Windows hosts): https://learn.microsoft.com/en-us/virtualization/windowscontainers/about/  
