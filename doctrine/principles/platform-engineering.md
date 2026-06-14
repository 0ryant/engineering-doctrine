# Platform Engineering

Durable rules for **building and operating internal developer platforms** that reduce **cognitive load** on stream-aligned teams and accelerate **safe delivery**.

Platform engineering is an intentional discipline rooted in [Team Topologies](https://teamtopologies.com/book) thinking. It is not "DevOps renamed", not "a shared ops team", and not "self-service for its own sake". The goal is deliberate reduction of extraneous cognitive complexity so stream-aligned teams can focus on their domain.

Implementation guidance (Backstage, Port, specific IDP tooling) lives in `doctrine/tooling/`. This file holds portable intent.

---

## 1. Team Types And Interaction Modes

Understand which team type each team in the estate represents and design interactions explicitly.

### 1.1 Four Team Topologies

| Team type | Primary job | Typical outputs |
| --- | --- | --- |
| **Stream-aligned** | Deliver a flow of change tied to a product domain | Features, bug fixes, operational improvements |
| **Platform** | Reduce cognitive load for stream-aligned teams | Paved paths, internal APIs, tooling, documentation |
| **Enabling** | Amplify capability in stream-aligned or platform teams | Training, coaching, discovery, short-lived embeds |
| **Complicated-subsystem** | Operate a high-specialist component (e.g., ML pipeline, real-time engine) | Versioned services with clear APIs away from domain pressure |

### 1.2 Three Interaction Modes

| Mode | When to use it | Characteristics |
| --- | --- | --- |
| **Collaboration** | Discovery, new platform capability, short-term unblocking | Both teams working together; high-bandwidth; time-boxed |
| **X-as-a-Service** | Steady-state platform delivery | Platform exposes a well-defined API; stream-aligned team self-serves |
| **Facilitating** | Enabling teams coaching | Non-prescriptive; builds capability, then steps back |

**Why:** Naming team types and interaction modes turns organisational friction into an explicit design choice. Unacknowledged collaboration across all team pairs scales poorly and burns both parties.

---

## 2. Platform-As-A-Product

The platform is a product consumed by internal teams. Apply product management discipline.

- Treat **stream-aligned teams as customers**; platform team as the product team.
- Maintain a **platform backlog** with prioritised roadmap, not just reactive tickets.
- Measure **adoption**, **DORA metrics** of platform consumers, **time to first production deployment** for new teams, and **cognitive load surveys** — not just uptime.
- Publish a **changelog** for every breaking or significant platform change; version platform APIs (see `doctrine/principles/semantic-versioning.md`).
- Run **regular feedback loops**: office hours, usage instrumentation, quarterly consumer surveys.
- Do not add platform features ahead of demonstrated demand. Thinnest viable platform (see §3) applies.

**Why:** Platforms built without product thinking accumulate shelfware, break consumers silently, and lose trust. The Google infrastructure teams' experience and CNCF Platforms Whitepaper both confirm product-thinking is the differentiating practice.

---

## 3. Thinnest Viable Platform (TVP)

Build the minimum platform that genuinely reduces cognitive load. Resist premature capitalisation.

- Start with **three to five highest-friction capabilities** for stream-aligned teams (commonly: container build and push pipeline, secret injection, observability baseline, PR-to-deploy flow, RBAC-scoped service accounts).
- Add new capabilities **only when multiple stream-aligned teams demonstrate the same unmet need**.
- Prefer **open-source or managed services** under the platform API. The platform team's value is the integration and paved path — not building infrastructure from scratch.
- Document **what the platform does NOT cover**. An explicit out-of-scope list prevents scope creep and resets expectations.
- Re-evaluate scope **quarterly**. Remove capabilities with zero adoption; fold specialised components back into consuming teams if the complexity does not justify central operation.

**Why:** Over-built platforms produce "golden cages" — high initial productivity but brittle, slow-to-change foundations. The Thinnest Viable Platform principle (Team Topologies) keeps investment proportional to proven value.

---

## 4. Platform Team Formation And Staffing

- **Staffing ratio:** a platform team of 6–10 engineers can sustain a well-scoped platform for 15–30 stream-aligned teams. Beyond this, either split the platform by domain or grow the platform team proportionally.
- Platform engineers must have **product, operations, and software delivery fluency** — not just infrastructure depth.
- Platform teams should include at least one **enabling function** (SRE, DevEx, or embedded tooling engineer) to drive adoption, not just build features.
- Avoid the **ops-dump antipattern**: forming a platform team by absorbing all infrastructure tasks from product teams without redesigning the interaction model. This reproduces a siloed ops structure under a new name.
- When the platform team is too small, use **collaboration mode** with stream-aligned teams to co-build initial capabilities, then shift to **X-as-a-service** once patterns are stable.

**Why:** Platform teams that are understaffed for their scope are slower than the teams they serve — which destroys trust and drives shadow IT.

---

## 5. Self-Service And Golden Paths

Golden paths are the preferred, low-friction routes to common outcomes. They are well-supported and well-documented — not mandatory rails.

- A golden path must include: **a working example**, **a one-command bootstrap or template**, **docs for common failure modes**, and **an escalation path**.
- Publish golden paths through a **service catalogue or developer portal** (Backstage, Port, or equivalent). The catalogue is the platform's storefront — keep it current or it misleads.
- Golden paths should be **composable**: a team that needs 80% of a standard path and 20% customisation should be able to do so without forking the entire template.
- Track **path adoption** and **deviation reasons**. High deviation signals either path friction or legitimate innovation — distinguish between them.
- Deprecate golden paths that are no longer maintained rather than leaving them as stale traps.

**Why:** Paved roads reduce accidents, not freedoms. The Netflix, Spotify, and GitHub platform models emphasise enabling autonomy within a supported structure — not enforcing uniformity.

---

## 6. Cognitive Load As A Metric

Cognitive load is the primary outcome the platform must reduce. Measure it deliberately.

- **Intrinsic** cognitive load (essential domain complexity) cannot be removed — only unneeded complexity can.
- **Extraneous** cognitive load (tooling complexity, unclear process, toil) is the platform's target. Reduce it by absorbing or automating.
- Measure via:
  - **Developer productivity surveys** (SPACE framework dimensions: Satisfaction, Performance, Activity, Communication, Efficiency) — see `doctrine/principles/measurement-and-dora.md`.
  - **Time-on-undifferentiated-work** ratio (hours on toil vs product-domain work — target: <20% toil).
  - **Onboarding time** (time from day-0 to first PR merged and deployed to staging — target: ≤1 day with golden path).
  - **DORA Four Keys** of platform consumers (deployment frequency, lead time, MTTR, change failure rate).
- Report cognitive load metrics to platform customers (stream-aligned team leads) on the same cadence as uptime metrics.

**Why:** Platform teams that do not measure consumer outcomes optimise for the wrong thing — shipping platform features that do not reduce team pain.

---

## 7. Platform Documentation And Contracts

Platform APIs are first-class contracts. Apply the same discipline as any other public API.

- **Every platform capability** has: a written purpose, an API contract (OpenAPI, Backstage entity schema, Terraform variable definition, or equivalent), example inputs/outputs, and documented error modes.
- Breaking changes follow **semantic versioning** and require **migration guides** with deprecation windows (minimum one sprint; major changes require one release cycle advance notice).
- The platform team owns documentation currency. Stale docs erode trust faster than missing features.
- **Use the platform to document the platform**: if the catalogue cannot describe platform services, the catalogue is broken.
- **Internal ADRs** for platform architecture decisions are public within the org. Teams consuming the platform deserve to understand why it works the way it does — see `doctrine/principles/documentation-knowledge.md`.

**Why:** Documentation is the delivery contract. A platform that cannot be used without ad-hoc Slack questions is not self-service.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Team Topologies as the reference model | Provides explicit vocabulary for team interactions. Avoids "DevOps" ambiguity. Widely adopted and well-evidenced. |
| Platform-as-a-product orientation | Platforms that lack product discipline drift toward shelfware or shadow IT. Consumer NPS is a leading indicator of platform health. |
| Thinnest viable platform | Over-built platforms are slower to change than no platform. Real production needs drive capability; build-ahead investment rarely lands correctly. |
| Separate platform team from enabling team function | Mixing sustained platform ops with short-term coaching produces neither outcome well. Enabling should be time-boxed by design. |
| Cognitive load as the primary metric | It is actionable, consumer-facing, and connects infrastructure decisions to developer experience outcomes better than adoption count alone. |
| ADRs for platform architecture, public in org | Trust requires transparency; consumers cannot safely integrate with a black box. |

---

## References

- Team Topologies (Skelton & Pais, 2019): https://teamtopologies.com/book
- CNCF Platforms Whitepaper: https://tag-app-delivery.cncf.io/whitepapers/platforms/
- Platform engineering glossary and community: https://platformengineering.org/
- Backstage — open-source developer portal: https://backstage.io/
- SPACE framework for developer productivity: https://queue.acm.org/detail.cfm?id=3454124
- Google SRE — Eliminating Toil: https://sre.google/sre-book/eliminating-toil/
- Gartner — Platform Engineering (2023 hype cycle reference): https://www.gartner.com/en/articles/what-is-platform-engineering
