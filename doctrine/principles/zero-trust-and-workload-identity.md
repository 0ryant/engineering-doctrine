# Zero Trust And Workload Identity

Durable rules for **verifying** callers and **least privilege** between services and humans. Deepens [Core Proposition 7](../../ENGINEERING.md#7-protect-proportionately-to-risk) (Protect Proportionately To Risk) without mandating a single mesh or cloud product. Where a contract, regulation, or estate decision applies an external baseline, [Revision-Pinned External Control Profiles](../patterns/revision-pinned-control-profiles.md) binds these identity controls to its exact revision, system/data boundary, evidence, and exceptions.

For how a workload normally obtains credentials, start with [Secretless Workload Identity](../impl/secretless-workload-identity.md).

---

## 1. No Implicit Trust From Location

- **Network** presence (VPC, office VPN) is **not** sufficient proof of authorisation; every **sensitive** action still needs **identity** and **policy**.
- **Service-to-service** calls use **authenticated** identities (mTLS, signed tokens, or platform workload identity)—not shared static “service passwords” unless a documented exception exists.

**Why:** NIST **SP 800-207** (*Zero Trust Architecture*) defines zero trust as **no implicit trust** based on network location alone: https://csrc.nist.gov/publications/detail/sp/800-207/final

---

## 2. Workload Identity

- Prefer **short-lived**, **audience-scoped** credentials issued to workloads (Kubernetes service account federation, cloud workload identity, SPIFFE/SPIRE where adopted).
- **Secretless by default (MUST, estate-governed and production workloads, including CI and CD jobs):** where the target accepts federated or platform-issued workload identity, authenticate with that short-lived, audience-scoped credential rather than a stored long-lived secret. Keeping a stored secret for such a target requires a bounded exception under the [exception contract](../patterns/normative-language-applicability-and-exceptions.md#5-exception-contract). ([ADR 0051](../../docs/adr/0051-make-secretless-workload-identity-the-default.md))
- **Registered fallback (MUST, same scope):** where the target cannot accept federated identity, the stored secret is a registered fallback: record its owner, rotation cadence, blast radius, and the reason federation is unavailable wherever the estate tracks secrets. Recheck when the target or platform adds support; the secretless default then applies. Local development and human access (§3) follow their own paths.
- **Rotate** and **scope** tokens; avoid **ambient** credentials readable by every process on a host.

**Why:** **SPIFFE** provides a **vendor-neutral** identity *shape* for workloads: https://spiffe.io/. Major providers make temporary workload credentials the default and keep long-term keys for workloads that cannot use them, and OWASP ranks secret leakage and long-lived secrets as separate non-human-identity risks. Short-lived tokens can still be stolen from a compromised job, so the default narrows exposure rather than removing it. Sources and limits: [research note](../evolution/research-secretless-workload-identity-default-2026-11.md).

### 2.1 Agent Identity

Applies when a workload is an **AI agent** — a model-driven principal that plans, calls tools, and produces side effects across systems — **holding its own workload identity**: its own credentials, standing infrastructure, or unattended operation. A tool acting entirely under a human's interactive session is that human's session, governed by §3 and [ai-ml-systems.md](ai-ml-systems.md) §4, not this subsection. §2's invariants apply unchanged; this subsection **extends** them with the identity granularity that generic workload identity does not capture.

- **First-class identity type — tiered by capability and materiality.** The principal-isolation floor rides the same two axes as every other AI control ([ai-ml-systems.md](ai-ml-systems.md) §2: capability tier × materiality): **high-autonomy or material agents** (Tier D, write access to production, or unattended operation at material blast radius) MUST act under a **dedicated per-agent principal**, labeled or tagged as an agent and resolvable to its sponsor — because per-agent **revocation** (the kill switch) and non-union **least privilege** are the containment story, and no log discipline recovers them from a shared principal. **Lower-autonomy agents** (assistive, read-mostly, team pipeline context) MAY share a **team principal** — normal BAU for shared pipelines and single-lifecycle credential rotation — provided (a) every action carries a **harness-stamped per-agent identifier** in a structured claim or log field (attribution injected by the runner, never self-reported by the model), and (b) the estate records that revocation is **fleet-wide** for that principal. The anti-pattern is not sharing per se; it is **agents as generic service accounts**: shared, *unattributed*, multi-purpose principals under which agent actions are indistinguishable from deterministic services. Purpose-built agent-identity platforms are rationale, not the bar; repeated exceptions at the high tier signal the floor is set wrong and route through [exception review and, for permanent deviations, policy or profile revision](../patterns/normative-language-applicability-and-exceptions.md#5-exception-contract), not silence.
- **Named human sponsor.** Every agent identity MUST have a named human **sponsor** with a defined **lifecycle**: sponsor departure or role change triggers reassignment or decommissioning, and an **orphaned** agent — one with no current sponsor — is disabled, not left running. Sponsorship anchors on the existing named-owner control (a **role** with an escalation path, not a team alias) in [../patterns/ai-adoption-controls.md](../patterns/ai-adoption-controls.md) §§1–2; this bullet binds that owner to the identity record rather than restating the control. **Teams and sponsorship:** a team may operate the agent, and one sponsor may cover a team's whole fleet — record the sponsor as a **role** (for example team lead) whose **current holder** is always a named person, so rotation within the team is a normal lifecycle event, not a decommission trigger. A team alias alone does not satisfy this: the orphan mechanism has nothing to fire on when nobody in particular holds the record ("everyone's agent is no one's agent"). Shared **sponsorship** is fine; shared **principals** follow the tiering in the first bullet.
- **Per-interaction credentials.** Agent credentials SHOULD narrow §2's short-lived, audience-scoped rule further: issued **per interaction or per task**, scoped to that run's tools and resources, and SHOULD NOT be a standing grant over the agent's whole capability surface. Run-scoped authority composition: [../patterns/agentic-loop-design.md](../patterns/agentic-loop-design.md) §8.
- **Attribution chains.** When an agent acts **on behalf of** a human or another agent, audit records MUST preserve the full delegation chain — initiating human, sponsor, agent identity, and each hop (**on-behalf-of** / **actor-token** semantics) — so one record answers both *who asked* and *what acted*. Evidence fields and retention: [audit-logging.md](audit-logging.md).

**Standards watch** *(informative, not normative — items are pre-final or vendor-specific; any future binding routes through [../patterns/revision-pinned-control-profiles.md](../patterns/revision-pinned-control-profiles.md))*: NIST **CAISSI** SI Agent Standards Initiative, formerly the AI Agent Standards Initiative (agent authentication and identity infrastructure): https://www.nist.gov/super-intelligence/si-agent-standards-initiative — NIST NCCoE concept paper on AI agent identity and authorization (initial public draft, 2026-02): https://csrc.nist.gov/pubs/other/2026/02/05/accelerating-the-adoption-of-software-and-ai-agent/ipd — IETF OAuth **Identity Assertion JWT Authorization Grant** (draft-06, 2026-10-30, still a working-group draft; cross-app access via RFC 8693 token exchange): https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/ — Microsoft **Entra Agent ID** (GA; sponsor-lifecycle workflows, agent-specific auth flows): https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id — **A2A** v1.0 signed Agent Cards (JWS card signing): https://a2a-protocol.org/latest/specification/ — AWS Bedrock **AgentCore Identity** (per-agent workload identity gating a token vault): https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/understanding-agent-identities.html — named products are rationale, not mandated tooling.

**Why:** Composed doctrine already yields short-lived, scoped workload identity for agent runners ([ai-ml-systems.md](ai-ml-systems.md) Tier D + §§1–2 above + agentic-loop authority); the missing residue was the **agent as principal** — sponsorship, per-interaction scope, delegation attribution — now converging across NIST, IETF, and the major platforms.

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
| Secretless default with a registered fallback | A preference left no record of why a federatable target still held a stored secret. A ban would turn every static-only third-party key into a permanent exception. The default plus a registered fallback keeps each remaining secret visible and owned ([ADR 0051](../../docs/adr/0051-make-secretless-workload-identity-the-default.md)). |
| Agent identity as §2.1, not a new file | Agents inherit §2's invariants; §2.1 adds only the **granularity residue** — principal class, sponsor lifecycle, per-interaction scope, delegation attribution. Vendor mechanisms stay informative. |

---

## References

- NIST **SP 800-207**, *Zero Trust Architecture*: https://csrc.nist.gov/publications/detail/sp/800-207/final  
- **SPIFFE** / **SPIRE**: https://spiffe.io/  
- UK NCSC **Zero trust principles** (accessible summary): https://www.ncsc.gov.uk/collection/zero-trust-architecture  
- AWS IAM security best practices — workloads use temporary credentials; long-term keys only where roles cannot be used (S5, product-scoped, accessed 2026-11-15): https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html  
- Google Cloud — best practices for managing service account keys, keys "as an exception rather than the norm" (S5, product-scoped, accessed 2026-11-15): https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys
- Microsoft Entra — **workload identity federation**: a workload outside Azure exchanges a trusted token from its own identity provider for a Microsoft token, with no stored secret (S5, product-scoped, accessed 2026-11-20): https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation
- Azure Well-Architected Framework — **SE:09 application secrets**, which recommends managed identities so credentials need not be stored (S5, product-scoped, accessed 2026-11-20): https://learn.microsoft.com/en-us/azure/well-architected/security/application-secrets
- OWASP **Non-Human Identities Top 10** 2025 — NHI2 secret leakage, NHI7 long-lived secrets (S4 awareness, accessed 2026-11-15): https://owasp.github.io/www-project-non-human-identities-top-10/2025  
