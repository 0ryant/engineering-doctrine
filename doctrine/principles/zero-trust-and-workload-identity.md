# Zero Trust And Workload Identity

Durable rules for **verifying** callers and **least privilege** between services and humans. Deepens umbrella **Zero Trust** without mandating a single mesh or cloud product. Where a contract, regulation, or estate decision applies an external baseline, [Revision-Pinned External Control Profiles](../patterns/revision-pinned-control-profiles.md) binds these identity controls to its exact revision, system/data boundary, evidence, and exceptions.

---

## 1. No Implicit Trust From Location

- **Network** presence (VPC, office VPN) is **not** sufficient proof of authorisation; every **sensitive** action still needs **identity** and **policy**.
- **Service-to-service** calls use **authenticated** identities (mTLS, signed tokens, or platform workload identity)—not shared static “service passwords” unless a documented exception exists.

**Why:** NIST **SP 800-207** (*Zero Trust Architecture*) defines zero trust as **no implicit trust** based on network location alone: https://csrc.nist.gov/publications/detail/sp/800-207/final

---

## 2. Workload Identity

- Prefer **short-lived**, **audience-scoped** credentials issued to workloads (Kubernetes service account federation, cloud workload identity, SPIFFE/SPIRE where adopted).
- **Rotate** and **scope** tokens; avoid **ambient** credentials readable by every process on a host.

**Why:** **SPIFFE** provides a **vendor-neutral** identity *shape* for workloads: https://spiffe.io/

---

## 3. Human And Break-Glass

- **Human** access to production uses **MFA** and **just-in-time** elevation where the estate supports it.
- **Break-glass** accounts are **rare**, **monitored**, and **reviewed**.

**Why:** Zero trust applies to **operators** as well as services.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Principle, not mesh SKU | Service mesh is **tooling**; invariant is **verified identity** at each hop. |
| Links to API doctrine | [api-boundaries-and-security.md](api-boundaries-and-security.md) covers **authorisation** semantics at HTTP boundaries. |

---

## References

- NIST **SP 800-207**, *Zero Trust Architecture*: https://csrc.nist.gov/publications/detail/sp/800-207/final  
- **SPIFFE** / **SPIRE**: https://spiffe.io/  
- UK NCSC **Zero trust principles** (accessible summary): https://www.ncsc.gov.uk/collection/zero-trust-architecture  
