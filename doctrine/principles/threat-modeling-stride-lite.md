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

### 3.1 GenAI-Era Attacker Uplift (Threat-Landscape Note)

Generative AI **collapses the cost** of convincing impersonation: fluent **phishing** without tells, **voice cloning**, live **video deepfakes**, and **synthetic identities** assembled from harvested data (NCSC assesses the largest near-term uplift is in **social engineering**; FinCEN and Europol document deepfakes defeating identity-verification and authorising fraudulent transfers). When walking **Spoofing** and **Repudiation**, treat any control that assumes *a human can recognise a counterpart* — voice approval, video verification, email instruction from a known sender, "call back to confirm" — as a **trust boundary under active attack**, and include **synthetic-media scenarios** in the analysis. Mitigations follow existing doctrine shape: **phishing-resistant** MFA and out-of-band verification over recognition, **signed** machine-to-machine instructions ([../patterns/webhook-ingress-security.md](../patterns/webhook-ingress-security.md)), and re-testing identity/fraud controls against synthetic media on a cadence, not once ([../patterns/ai-adoption-controls.md](../patterns/ai-adoption-controls.md) §3). The **vulnerability-side** acceleration (AI-assisted exploit development) is covered in [../evolution/mythos-era-engineering-principles-research-2026-04-28.md](../evolution/mythos-era-engineering-principles-research-2026-04-28.md).

### 3.2 Agentic Systems As Targets (Threat-Landscape Note)

§3.1 covers AI as **attacker uplift**; this note covers the other direction — the **AI system itself as target**. When the system under review **contains an agent** — capability Tier **D**, or Tier **B** with **agent-writable memory**, per [ai-ml-systems.md](ai-ml-systems.md) §2 and §7 — extend the STRIDE walk with the **agentic attack vocabulary** as **auditable naming, not new controls**: the **OWASP Top 10 for Agentic Applications 2026** (**ASI01–ASI10**) and the **NIST AI 100-2e2025** adversarial-ML taxonomy — notably **direct prompting** (attacker controls the query interface), **indirect prompt injection** (attacker plants instructions in documents, web pages, or retrieval corpora ingested into context at runtime), **poisoning**, and **agent hijacking** (tool use turns injected instructions into code execution or data exfiltration; AI 100-2 §3.5). Classic STRIDE **under-captures** these classes because an agent is simultaneously **process, data store, dataflow, and actor**, breaking the fixed-role, static-boundary assumptions the category walk relies on (Bishop Fox): **goal hijack** (ASI01) turns the agent's *legitimate* capabilities against its principal — no credential is spoofed and no data is tampered at rest — and **cascading multi-agent failure** (ASI08) propagates through delegation, not through one actor exhausting a resource. Keep the STRIDE pass; add the vocabulary so these threats get **named** rather than forced into the nearest letter.

Each vocabulary item routes to the doctrine surface that **owns** its mitigation — this section restates none. The **ASI-to-doctrine crosswalk** at [../patterns/agentic-loop-design.md](../patterns/agentic-loop-design.md) §11 maps every ASI identifier to its controlling section (each linked section carries its own normative strength; residual gaps — for example inter-agent message signing and anti-replay — are recorded there honestly). **Injection and poisoning** handling of retrieved/external content routes through [ai-ml-systems.md](ai-ml-systems.md) §7 and the context-isolation patterns of [../patterns/agentic-loop-design.md](../patterns/agentic-loop-design.md) §5/§9; **agent identity and delegation trust** through [zero-trust-and-workload-identity.md](zero-trust-and-workload-identity.md) §2.1. For multi-agent topologies where a per-flow STRIDE table strains, **MAESTRO** (see References) is an optional deeper methodology; STRIDE remains this file's baseline pass.

---

## 4. Blast-Radius Acceptance (Testable Prompts)

**Goal:** reviewers can answer *what escapes if this node is compromised* without relying on slogans (“least privilege”, “internal only”) that skip **evidence**.

For each **trust-boundary** crossing and each **high-value** component, capture:

- **Reach in five minutes** — If this **identity** or **component** is stolen, what **reads, writes, deletes, impersonation, or egress** become possible **next** (data stores, queues, admin APIs, metadata services, **CI/CD**, outbound internet, adjacent tenants)?
- **Highest-value asset without an independent control** — If the answer is **production data**, **credential minting**, or **broad egress**, add mitigation or **explicit** risk acceptance with owner.
- **What actually stops lateral movement** — Network “private” labels are **not** controls by themselves; name **identity**, **policy**, **segmentation**, or **deny-by-default** enforcement that still applies after compromise.
- **Irreversible or bulk actions** — Call out exports, tenant-wide reads, queue fan-out, destructive admin paths, unrestricted outbound fetch.
- **Proof, not vocabulary** — Point to **negative** tests, blocked egress checks, scoped service accounts, or route-level policy checks that would **fail** if the boundary regressed.

**Acceptance bar (portable):** for each critical asset, the reviewer can name **which single-component compromise is contained** and **which is not**. If they cannot, the design is not yet reviewed.

**Cross-checks:** [api-boundaries-and-security.md](api-boundaries-and-security.md) (BOLA/BOPLA, rate limits, SSRF), [zero-trust-and-workload-identity.md](zero-trust-and-workload-identity.md) (workload identity, no location-only trust). **Theater** = listing controls without **failure consequences**, ignoring machine identities and CI, or “defense in depth” while **one** shared credential still reaches the crown jewels.

---

## 5. Scope And Overlap

| Topic | Prefer |
| --- | --- |
| HTTP abuse, OWASP API | [api-boundaries-and-security.md](api-boundaries-and-security.md) |
| Cluster hardening | [kubernetes-platform-security.md](kubernetes-platform-security.md) |
| Dependency and build integrity | [dependencies-supply-chain.md](dependencies-supply-chain.md) |
| Event shape and versioning | [event-contracts.md](event-contracts.md) |
| Agentic mitigation controls, ASI crosswalk | [../patterns/agentic-loop-design.md](../patterns/agentic-loop-design.md) §11 |

This file supplies the **structured pass** across boundaries; the others supply **specific controls**.

---

## 6. Attack Trees, Data-Flow Diagrams, And Supply-Chain Threats

- **Attack trees** — for **high-stakes** systems, decompose **attacker goals** (for example “forge webhook”, “exfiltrate tenant data”) into **steps** and map **detections** / **controls** per branch; STRIDE still applies at each edge.
- **Data-flow diagrams (DFD)** — optional tooling (**OWASP Threat Dragon**, **Microsoft Threat Modeling Tool**, draw.io) helps teams **see** forgotten trust boundaries; a **whiteboard** DFD beats no diagram.
- **Supply-chain** threats — include **CI/CD**, **package registries**, **build** provenance, and **third-party** SaaS in the model—not only runtime services; cross-check [dependencies-supply-chain.md](dependencies-supply-chain.md) and [build.md](build.md).

**Why:** STRIDE on a **single** API is insufficient when the **weakest** path is “malicious dependency” or “compromised pipeline.”

---

## 7. Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| STRIDE over bespoke taxonomies | Widely taught, **compact**, and maps cleanly to common web/API/K8s failures. |
| “Lite” | Full tooling (data-flow diagrams in dedicated TM suites) is optional; **table + diagram sketch** is enough for many teams. |
| Principle, not estate | Threat thinking is **portable**; product-specific defensive patterns stay in tooling/estates. |
| Supply chain in scope | **CI** and **dependencies** are trust boundaries, not afterthoughts. |
| Blast-radius prompts | Separates **falsifiable** containment claims from **security vocabulary** theater. |

---

## References

- STRIDE categories (Microsoft threat-modeling overview): https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats  
- OWASP API Security Top 10 (control cross-check): https://owasp.org/API-Security/editions/2023/en/0x11-t10/  
- OWASP **Threat Dragon** (diagram-driven threat modeling): https://owasp.org/www-project-threat-dragon/  
- OWASP **Secure by Design Framework** (design-time security): https://owasp.org/www-project-secure-by-design-framework/  
- NIST **Zero Trust Architecture** (SP 800-207): https://csrc.nist.gov/publications/detail/sp/800-207/final  
- NCSC — **Impact of AI on the cyber threat** (social-engineering uplift): https://www.ncsc.gov.uk/report/impact-of-ai-on-cyber-threat  
- FinCEN **FIN-2024-Alert004** — deepfake media targeting financial institutions: https://www.fincen.gov/system/files/shared/FinCEN-Alert-DeepFakes-Alert508FINAL.pdf  
- Europol — **Facing Reality? Law enforcement and the challenge of deepfakes**: https://www.europol.europa.eu/publications-events/publications/facing-reality-law-enforcement-and-challenge-of-deepfakes  
- NIST **AI 100-2e2025** — Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations: https://csrc.nist.gov/pubs/ai/100/2/e2025/final  
- OWASP **Top 10 for Agentic Applications 2026** (ASI01–ASI10): https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/  
- CSA — **MAESTRO** agentic threat-modeling framework: https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro  
- OWASP — **Multi-Agentic System Threat Modeling Guide v1.0** (landing page; primary PDF is download-gated): https://genai.owasp.org/resource/multi-agentic-system-threat-modeling-guide-v1-0/  
- Bishop Fox — **Taking MAESTRO in Stride** (STRIDE with agentic frameworks): https://bishopfox.com/blog/taking-maestro-in-stride-ai-threat-modeling-frameworks  
