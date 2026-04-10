# Threat Modeling (STRIDE Lite)

Lightweight **systematic** review of **trust boundaries** and common attack classes. Use to **complement** concrete control checklists in [api-boundaries-and-security.md](api-boundaries-and-security.md), [kubernetes-platform-security.md](kubernetes-platform-security.md), [dependencies-supply-chain.md](dependencies-supply-chain.md), and [event-contracts.md](event-contracts.md)—not to replace them.

---

## 1. When To Use It

- **New** internet-exposed API, auth flow, data store, or message topology.
- **Material change** to trust boundaries (new integration, public surface, tenant isolation story).
- **Pre-release** or **periodic** review for high-risk systems where “OWASP checklist only” is insufficient for **architecture-level** gaps.

Skip full workshops for trivial internal tools; still record **“not in scope”** in the design note or ADR.

---

## 2. Minimal Workflow

1. **Draw** the system at **component** level: users, clients, gateways, services, data stores, queues, third parties.
2. Mark **trust boundaries** (internet ↔ app, tenant ↔ tenant, corp ↔ prod, CI ↔ runtime).
3. For each **significant flow** across a boundary, walk **STRIDE** (below) and capture **threat → mitigation → residual risk** in a short table or ADR subsection.
4. **Track** open risks (owners, deadlines); revisit after major changes.

---

## 3. STRIDE Prompts (Lite)

| Category | Question (examples) |
| --- | --- |
| **Spoofing** | Can an caller impersonate another user, service, or tenant? Weak auth, trust-on-IP, unsigned webhooks? |
| **Tampering** | Can data or config be altered in transit or at rest without detection? Missing integrity checks on events or uploads? |
| **Repudiation** | Can abuse or admin actions occur without durable, correlated audit evidence? |
| **Information disclosure** | Can secrets, PII, or cross-tenant data leak via logs, errors, caches, or overly verbose APIs? |
| **Denial of service** | Can a single actor exhaust CPU, connections, queues, or storage? Unbounded queries or fan-out? |
| **Elevation of privilege** | Can a low-privilege caller reach admin paths, escape container boundaries, or abuse CI to ship code? |

Map mitigations to practices you already mandate (rate limits, object-level auth, mTLS, least privilege, secrets rotation, Pod Security, SBOM).

---

## 4. Scope And Overlap

| Topic | Prefer |
| --- | --- |
| HTTP abuse, OWASP API | [api-boundaries-and-security.md](api-boundaries-and-security.md) |
| Cluster hardening | [kubernetes-platform-security.md](kubernetes-platform-security.md) |
| Dependency and build integrity | [dependencies-supply-chain.md](dependencies-supply-chain.md) |
| Event shape and versioning | [event-contracts.md](event-contracts.md) |

This file supplies the **structured pass** across boundaries; the others supply **specific controls**.

---

## 5. Attack Trees, Data-Flow Diagrams, And Supply-Chain Threats

- **Attack trees** — for **high-stakes** systems, decompose **attacker goals** (for example “forge webhook”, “exfiltrate tenant data”) into **steps** and map **detections** / **controls** per branch; STRIDE still applies at each edge.
- **Data-flow diagrams (DFD)** — optional tooling (**OWASP Threat Dragon**, **Microsoft Threat Modeling Tool**, draw.io) helps teams **see** forgotten trust boundaries; a **whiteboard** DFD beats no diagram.
- **Supply-chain** threats — include **CI/CD**, **package registries**, **build** provenance, and **third-party** SaaS in the model—not only runtime services; cross-check [dependencies-supply-chain.md](dependencies-supply-chain.md) and [build.md](build.md).

**Why:** STRIDE on a **single** API is insufficient when the **weakest** path is “malicious dependency” or “compromised pipeline.”

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| STRIDE over bespoke taxonomies | Widely taught, **compact**, and maps cleanly to common web/API/K8s failures. |
| “Lite” | Full tooling (data-flow diagrams in dedicated TM suites) is optional; **table + diagram sketch** is enough for many teams. |
| Principle, not estate | Threat thinking is **portable**; product-specific defensive patterns stay in tooling/estates. |
| Supply chain in scope | **CI** and **dependencies** are trust boundaries, not afterthoughts. |

---

## References

- STRIDE categories (Microsoft threat-modeling overview): https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats  
- OWASP API Security Top 10 (control cross-check): https://owasp.org/API-Security/editions/2023/en/0x11-t10/  
- OWASP **Threat Dragon** (diagram-driven threat modeling): https://owasp.org/www-project-threat-dragon/  
