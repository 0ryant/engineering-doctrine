# Kubernetes Platform Security (When You Run K8s)

Apply this document **only when** the organisation runs **Kubernetes** (cloud-managed control plane such as EKS/AKS/GKE, or on-prem). It does **not** negate [container-runtime-choice.md](container-runtime-choice.md)—if a **managed application platform** removes the need for a cluster, prefer that path when it meets requirements.

---

## 1. Cluster Baseline

- **RBAC** — least privilege for humans and CI; no permanent **cluster-admin** bindings for day-to-day roles.
- **Network policy** — default **deny** between namespaces unless explicitly allowed; ingress/egress documented.
- **Pod security** — restrict privileged pods, host namespaces, and dangerous capabilities; align with current Kubernetes **Pod Security** mechanisms for your version.
- **Secrets** — prefer **CSI drivers** / external secret stores over long-lived static kubeconfigs in CI; rotate service account tokens per platform guidance.

**Why:** Most cluster compromises spread **laterally** through over-permissive RBAC and flat networks.

---

## 2. Supply Chain For Workloads

- **Image policy** — allow only trusted registries; scan images in CI; pin digests or tags per [dependencies-supply-chain.md](dependencies-supply-chain.md).
- **Admission control** — validate signed images (**Sigstore** / policy where adopted), required labels, resource limits.

**Why:** “Bad image in cluster” is a **supply-chain** incident, not an app bug.

---

## 3. Observability And Audit

- **Audit logs** for API server actions where the cloud or platform provides them (enable per vendor guidance).
- **Platform metrics** for etcd, API latency, scheduler — not only pod CPU.

**Why:** Debugging **cluster** health requires **control plane** visibility, not only app metrics.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Explicit “when K8s” scope | Avoids implying **every** team must carry cluster security burden when **managed** runtimes suffice. |
| Default-deny networking | **Cheapest** control for lateral movement inside the cluster. |
| Admission + signing | Implements **shift left** on images at the last gate before run. |

---

## References

- Kubernetes **Pod Security Admission**: https://kubernetes.io/docs/concepts/security/pod-security-admission/  
- Kubernetes **Network Policies**: https://kubernetes.io/docs/concepts/services-networking/network-policies/  
- NSA / CISA **Kubernetes Hardening Guide** (baseline checklist): https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF (PDF) — summary pages widely mirrored if you prefer HTML digests.  
- Your **Kubernetes provider’s** security baseline (EKS, GKE, AKS, or distribution vendor) — use current vendor docs for control-plane audit and managed integrations.  
