# Incident Lifecycle And On-Call Operations (Pattern)

Companion to [reliability-slo-incidents.md](../principles/reliability-slo-incidents.md). That principle file states **SLOs**, **error budgets**, and **blameless learning**; this pattern is the **portable** shape for **incident response**, **command**, **on-call load**, and **post-incident action tracking** without mandating a vendor (PagerDuty, Opsgenie, Jira, status pages, war-room tooling).

**Why separate from principles:** Org size, regulatory context, and tooling differ. A portable pattern should be **adoptable** on day one (single team, single channel) and **scalable** to multi-team incidents without conflating “Google headcount” with “good process.”

---

## Intent

- Make **response** to production-impacting events **predictable**: who decides, who speaks, where truth lives, how often the world is updated, when to **escalate**, how **shifts** hand off, and how humans stay **sustainable** under interrupts.
- Keep **SLOs and severity** connected: an incident is not “any alert”—it is an **executed** response when **impact** or **risk** exceeds a defined threshold.
- **Close the loop** with **tracked** actions, not one-off postmortems in a doc graveyard.

---

## 1. Incident lifecycle (phases)

Use a **small** set of named phases; exact labels are estate-specific, but the **sequence** is stable:

| Phase | Purpose |
| --- | --- |
| **Detect / triage** | Something crosses **severity** (§2) or a human declares an incident. Confirm **impact**, start the **state doc** (§5), assign **incident command** (§3). |
| **Command / mitigate** | **Incident commander (IC)** coordinates; execution may involve **SMEs**; goal is **limit blast radius** and **restore** service to agreed definition of “recovered” (or accepted degradation). |
| **Communicate** | Per **comms cadence** (§4): internal alignment, **customer/stakeholder** updates if policy requires, **regulatory** or **legal** only when the estate demands it. |
| **Stabilize / handoff** | Work moves from **tactical** firefighting to **sustained** ownership: **on-call to dev** or to a **fix track**, with an explicit **handoff** (§7). |
| **Resolve and learn** | Formal **closure** when SLO-consistent state is restored; **blameless** review; **action items** with owners and dates (§9). |

**Must not:** skip **closure** to “it seems fine” without a written **end state** in the state doc; **must** ensure **on-call** can **sleep** after a defined **exit** (or explicit **waiver** and **relief**).

---

## 2. Severity

**Severity** maps **user impact**, **data risk**, and **immediacy** to **response shape** (who is paged, comms bar, executive involvement). **Names** (P0–P4, SEV-1, etc.) are estate-specific; the **portable** rule is:

- **A written matrix** in the runbook or service catalogue: e.g. “**P0** — customer-visible outage of paid path, no workaround” vs “**P3** — internal-only degradation with workaround.”
- **Alignment to paging:** only **some** severities require **page**; **lower** severities can be **ticket** or next-business-day, **except** when **SLO** or **regulatory** policy overrides.
- **Stability of definitions:** if severity meaning **drifts**, postmortems and metrics become **incomparable**—treat the matrix as **versioned** like a contract.
- **Escalation in severity** when impact **grows** or when **uncertainty** is high (e.g. possible **data** exposure); **de-escalate** only with **evidence** in the state doc.

**Why:** Google SRE and PagerDuty-style handbooks all converge on “severity drives **ritual**, not the reverse.”

---

## 3. Roles

**Roles** can be **one person** wearing multiple hats in a small org; the important part is that **duties** are **not left implicit** during an active incident.

| Role | Purpose |
| --- | --- |
| **Incident commander (IC)** | **Single** coordinator: priorities, timeboxes, when to **cut scope**, when to **escalate**, who is **paged**. Does **not** have to be the best debugger. |
| **Deputy / backup IC** | Optional for long incidents; **handoff** target so IC can rest (§7, §8). |
| **Communications lead (comms lead)** | **Drafts/approves** user-facing and internal comms; keeps **one voice** and cadence (§4). **Must** for customer-visible SEV-1+ in many orgs. |
| **Scribe** | Updates the **state doc** (§5) in **real time**; captures decisions, **hypotheses disproved**, **mitigations** tried. If no dedicated scribe, IC **rotates** the duty. |
| **SMEs / responders** | People who know subsystems, **infra**, or **data**; work **tactical** tasks directed by IC. |
| **Agent responder (rostered)** | Optional; only where the estate operates one. An **AI agent** on the roster working **tactical**, **pre-declared** tasks and investigation under IC direction; has a **named accountable human owner** (sponsor per [zero-trust-and-workload-identity.md](../principles/zero-trust-and-workload-identity.md) §2.1) who can **page-steal** or **stop** it at any time; **never** IC (§10). |
| **Executive / legal / customer liaison** | **Only** as required by **severity** and **regulatory** context—not every incident needs a C-suite. |

**Must not:** have **no** single IC in a **multi-team** response—**everyone** owns it means **no one** owns it; **must not** assign **incident command** to an **agent responder** (§10)—command is a **human** accountability, not a coordination capability.

**Why:** Incident command in aviation and ITIL-style command structures; portable doctrine only needs the **separation of coordination and execution**, not a certification.

---

## 4. Comms cadence

**Internal comms** keep responders aligned; **external comms** protect **trust** and **contract** obligations (SLA, **status page**, support tickets).

- **Start:** first internal update when IC is **set**; say **known impact**, **unknowns**, and **next update time**.
- **Cadence** during an active incident: **timeboxed** (e.g. “every 15 min while impact continues” for **highest** severity)—adjust to **triage** load; **no silent gaps** without stated reason in the state doc.
- **External / customer** comms: follow **estate** policy; often tied to **status page** first update within **N** minutes of **confirmed** user impact.
- **All-clear / resolved:** one **clear** message: what was wrong, what was done, what **follow-up** is planned, known **residual** risk.
- **Coordination** with **security** or **privacy** for possible **breach**-class events; **comms** may be **gated** on facts—**must not** fabricate.

**Why:** Atlassian, PagerDuty, and SRE comms playbooks all stress **predictable** updates over **ad hoc** noise.

---

## 5. State document (single source of truth)

The **incident state doc** (wiki page, **shared doc**, ticket, or **runbook** section—estate pick) is the **log of truth** for the incident:

- **Id** and **time started**; **IC**; **scope** (services, **regions**, **tenants**).
- **Current severity** and **evidence** for any **change** in severity.
- **Impact** in **user** terms; link to **SLIs** if available.
- **Hypothesis** and **timeline** of **tries**; **rejected** paths noted (saves re-triage).
- **Comms** pointer: where **external** text lives; last **public** update time.
- **Open decisions** and **escalation** requests.
- **Resolution** and **end time**; **handoff** notes for **post-incident** (§7, §9).

**Must** update when **IC** or **comms** hands off. **Why:** prevents **Slack** as the only **memory**; Slack is a **transcript**, not a **system of record** for postmortems and audit.

---

## 6. Escalation

**Escalation** = **increase** in **help**, **authority**, or **awareness** when progress stalls or impact **grows**.

- **Technical escalation:** add **SMEs**, page **deeper** on-call, involve **platform** or **vendor** support per **runbook** and **contract**.
- **Manager / leadership escalation:** for **SEV-1+**, **sustained** customer pain, or **repeated** SLO **burn**; for **resourcing** (need more people, need **deprioritization** of other work).
- **Security / legal / exec:** when **data** exfil, **fraud**, **safety**, or **regulator** may be in scope; **not** a substitute for **technical** triage—parallel tracks.

**Ladder (portable):** document **order** in the runbook: on-call **→** service owner **→** team lead **→** **domain** on-call **→** **TAM** / vendor **→** **exec**—**cut** what does not exist in the estate, **never** leave “who is next” as tribal knowledge.

**Why:** SRE and ITIL both treat **unbounded** heroics as a **smell**; **escalation** is a **resource** request, not **failure**.

---

## 7. Handoff

**Handoff** happens when the **responsible human** or **responsible team** **changes** without closing the **problem**.

- **IC handoff:** **synchronous** where possible: **old IC** to **new IC** with **verbal+written** state (what works, what does **not**, **open risks**). **Update** state doc and **paging** ownership in the **on-call** tool.
- **On-call to engineering:** after **stabilize**, a **defect** or **root-cause** track **owns** the **backlog** item; the **incident** record **links** to it.
- **Shift change:** **warm** handoff for **SEV-1+**: incoming IC **acknowledges** before outgoing **stops** (or explicit **waiver** with **liability** clear).

**Why:** NTSB-style handoff discipline is overkill for every bug, but **production** SEV-1 **without** handoff rules produces **raging** 3 a.m. **confusion**.

---

## 8. Fatigue, interrupt load, and sustainable on-call

**On-call** is a **reliability** **investment**; it is not **free** labor.

- **Primary / secondary** rotation: **primary** first responder; **secondary** for **overflow** or **SEV-1+**; **tertiary** only when **estate** truly needs it—**document** the **order**.
- **Interrupt budget (conceptual):** if **wakes** or **SEV-1s** per rotation exceed a **defined** **threshold**, **stop** and **treat** as a **reliability** or **triage** **program** problem, not a **“try harder”** problem—aligns with [reliability-slo-incidents.md](../principles/reliability-slo-incidents.md) **toil** and [measurement-and-dora.md](../principles/measurement-and-dora.md) **time to restore**.
- **Time limits:** **IC** and **SMEs** need **rest**; **long** incidents use **shifts** and **deputy** IC. **No** “heroic” **indefinite** **ownership** without **relief**—record **fatigue** as a **risk** in the state doc if the team is **understaffed**.

**Why:** DORA, SPACE, and SRE toil work all flag **sustainable** pace; **unsustainable** on-call is a **reliability** **defect**.

---

## 9. Post-incident: learning and action tracking

- **Blameless** review for **material** incidents (per estate policy, often all **P0/P1** and **any** with **data** or **security** impact).
- **Attendees** include IC, **SMEs**, **comms** if public, and **owner** of **affected** **product**; **scales** with severity.
- **Output:** **timeline**, **root cause** (or **factors** if **not** a single line), **what went well / poorly**, **action items** with **one owner** each and **date**; **link** to **tickets** or **work tracking**.
- **Architecture backlog when blast radius lied** — if the review finds that **architecture** (not only a bug) **amplified** impact, **must** open at least one **tracked** architecture or platform item—not only a hotfix ticket. **Triggers (examples):** successful **lateral movement** across an internal boundary meant to contain; **credential or secret scope** allowed exfiltration across a **trust zone**; **shared control plane** or **multi-tenant** substrate turned one defect into cross-customer impact; missing **segmentation**, **egress control**, or **kill-switch** design materially worsened outcome; **same failure class** recurs after a “patch-only” fix. **Ownership:** **product** teams for service-local trust mistakes; **platform** for shared guardrails, identity defaults, paved-road isolation; **joint** when both must change—still assign **one** accountable owner per item.
- **Track** **actions** to **completion**; **reopen** the **conversation** if the **same** **failure class** recurs. **DORA** **change-failure** and **restoration** metrics improve when **this** **closes**.

**Why:** The principle file already **requires** **tracked** **actions**; this pattern **ties** them to **roles** and **cadence** so the **ritual** **sticks**. NIST SSDF **RV.3** expects learning that reduces **recurrence**, including **system shape**.

---

## 10. Agent responders and AI-assisted investigation

**Applies only** to estates operating **agent responders** — AI agents (Azure SRE Agent-class, PagerDuty virtual responder, incident.io AI SRE) rostered into incident response. Estates without them change nothing; the all-human roles in §3 remain complete. This section adds **incident-ops-specific** rules only. Agent **autonomy** and **authority** are already governed by [ai-native-software-development-lifecycle.md](ai-native-software-development-lifecycle.md) §10 (**service/change owner** decides rollback, incident, and closure) and §13 (an operational agent cannot detect, implement, approve, and deploy its own change as one closed authority loop) — this section composes with those rules; it does **not** define a parallel autonomy framework.

- **Roster role with a named human owner.** An agent participating in response is a **roster role** in §3, not ambient tooling. It MUST have a **named accountable human owner** who can **page-steal** or **stop** it at any time. Identity, sponsorship, and lifecycle bind to existing controls — the **named human sponsor** and per-agent principal in [zero-trust-and-workload-identity.md](../principles/zero-trust-and-workload-identity.md) §2.1 and the named-owner control in [ai-adoption-controls.md](ai-adoption-controls.md) §§1–2 — and are not restated here. An agent MUST NOT serve as **IC** (§3).
- **Remediation routes by reversibility and blast radius.** Using the applicability vocabulary of [normative-language-applicability-and-exceptions.md](normative-language-applicability-and-exceptions.md) §3 (**reversible / compensatable / irreversible**; change-autonomy dimension): **pre-declared, tested, deterministic** reversible actions MAY auto-execute under a **scoped response plan**, with **notification** landing in the state doc (§5); **irreversible or production-mutating** actions — any **novel** mutation — MUST gate on human approval before execution. The **reversible-action list** is pre-declared **outside incident time** by the agent's named accountable human owner together with the service owner, lives in the **runbook or service catalogue**, is versioned like the §2 severity matrix, and changes through normal review — it is **never extended mid-incident**; the **scoped response plan** is that artifact. This is the **"approve before irreversible only"** position of the [agentic-loop-design.md](agentic-loop-design.md) §6 autonomy slider specialised to incident response; per §6 the slider moves **left** on any incident, never right mid-incident. Vendor practice converges here: Azure SRE Agent defaults to **Review** mode (agent proposes, human approves; Autonomous recommended only outside production), and PagerDuty's virtual responder executes predefined actions only **when authorized**.
- **RCA output is ranked leads, not conclusions.** Agent investigation output — hypotheses, correlations, suspected causes — enters the incident as **ranked leads with evidence** in the state doc's hypothesis log (§5). A **human** IC owns the incident **narrative** and **closure**; a lead MUST be **confirmed by a human** before it enters the postmortem record (§9) as cause. Vendor tooling is itself hypothesis-shaped (validated / invalidated / inconclusive, with evidence citations); treat un-reviewed agent RCA as **untriaged input** — the same class as an unverified SME hunch.
- **Every agent action lands in the audit trail.** Proposed, approved, and auto-executed actions and every hypothesis MUST land in the **state doc** (§5) and the incident **audit trail**, carrying the full **attribution chain** (initiating human, sponsor, agent identity, each hop) per zero-trust §2.1 and [audit-logging.md](../principles/audit-logging.md). **Handoff** (§7) includes agent state: what it is running, which approvals are pending, who owns it next.
- **Circuit breaker on the incident→issue→coding-agent loop.** Where the estate wires incidents to issue creation and **coding agents** (live mitigation paired with a tracked source fix), the loop MUST carry a **circuit breaker**: **rate caps** and **loop caps** so agents cannot open unbounded work items or re-trigger themselves. **Anti-pattern — self-healing that masks drift:** an agent that repeatedly patches **live state** (restart the pod, bump the limit) without a tracked **source/IaC** change hides the underlying defect and accumulates divergence from declared state; pair every live remediation with a source-closing item, per [gitops-and-declarative-operations.md](gitops-and-declarative-operations.md).
- **Untrusted input surface.** Responder agents read **telemetry**, **logs**, and **ticket text** — attacker-influenceable content — making them a **confused-deputy** surface during the window when change velocity is highest; apply the injection defences of [agentic-loop-design.md](agentic-loop-design.md) §9.

**Why:** Ops agents are shipping, and converged vendor design is **approval-gated by default** with **hypothesis-shaped** RCA — doctrine encodes the invariants (named owner, reversibility routing, human-owned narrative, audit trail, loop caps), not the products; release-status specifics live in the References annotations and the adopting ADR.

---

## 11. Relation to SLOs, game days, and platform ownership

- **SLOs** and **error budgets** decide **strategic** **investment**; **this pattern** is **tactical** **response** when **SLOs** are **threatened** or **breached** **now**—[reliability-slo-incidents.md](../principles/reliability-slo-incidents.md) §1–2.
- **Chaos and game days** [chaos-engineering-and-game-days.md](chaos-engineering-and-game-days.md) **rehearse** **parts** of this (roles, runbooks) **before** **production** **pain**—**link** them in **onboarding** and **on-call** checklists.
- **Platform** teams: **on-call** for **control plane**; **tenants** for **app**; **this pattern** still applies—**clarify** **which** **IC** **owns** **cross-tenant** **impact** in [platform-as-product-and-golden-paths.md](platform-as-product-and-golden-paths.md) **escalation** **posture**.

---

## Rationale and decisions

| Decision | Rationale |
| --- | --- |
| Pattern, not new principle | Keeps [reliability-slo-incidents.md](../principles/reliability-slo-incidents.md) **durable**; orgs **tune** **roles** and **SEV** **names** without forking **normative** **one-size** text. |
| One IC in multi-party incidents | **Coordination** **failure** is a top **class** of **long** **outages** in public **RCAs**. |
| State doc is mandatory concept | **Artifact** is **estate**-specific, **discipline** is **portable**. |
| Fatigue in same pattern as comms | **Human** **limits** are part of **operating** **model**, not a **soft** “culture” add-on. |
| Agent responders composed, not forked | **Identity/sponsorship**, **autonomy**, and **closed-loop** rules already live in zero-trust §2.1, agentic-loop §6, and AI-native SDLC §10/§13; §10 adds only the **incident-ops** residue (roster role, reversibility routing, ranked-leads RCA, audit trail, loop caps). |
| Reversibility routes agent remediation | Converged vendor default (Azure **Review** mode; PagerDuty authorization gate); matches the autonomy-slider position **“approve before irreversible only”** with the slider moving **left** on any incident. |

---

## Related

- [reliability-slo-incidents.md](../principles/reliability-slo-incidents.md) — SLOs, error budgets, high-level **incident** and **toil** rules
- [chaos-engineering-and-game-days.md](chaos-engineering-and-game-days.md) — **exercises** and **rehearsal**
- [documentation-knowledge.md](../principles/documentation-knowledge.md) — runbooks, **operational** **knowledge**
- [observability.md](../principles/observability.md) — **signals** that **feed** **severity** and **impact**
- [platform-as-product-and-golden-paths.md](platform-as-product-and-golden-paths.md) — **escalation** to **platform**
- [measurement-and-dora.md](../principles/measurement-and-dora.md) — **restore** **time** and **learning** **loops**
- [secure-development-lifecycle.md](../principles/secure-development-lifecycle.md) — **RV** root-cause classes (patch vs process vs **architecture**)
- [agentic-loop-design.md](agentic-loop-design.md) — **autonomy slider** (§6) and **injection defence** (§9) that §10 anchors on
- [../principles/zero-trust-and-workload-identity.md](../principles/zero-trust-and-workload-identity.md) — **agent identity**, **named human sponsor**, attribution chains (§2.1)
- [ai-native-software-development-lifecycle.md](ai-native-software-development-lifecycle.md) — **authority model** (§10) and **closure loops** (§13) governing operational agents

---

## References

- Google *Site Reliability Engineering* (O’Reilly) — **Managing Incidents** and **Postmortem Culture**: https://sre.google/sre-book/table-of-contents/  
- Atlassian (example **incident** **management** and **comms** vocabulary): public **ITSM** and **on-call** playbooks in product docs (verify current URLs).  
- *Practical Monitoring* / industry **on-call** practice—see [REFERENCES.md](../REFERENCES.md) for the library’s **external** index.
- Microsoft Learn — **Azure SRE Agent** overview / run modes / permissions (vendor observation for §10): https://learn.microsoft.com/en-us/azure/sre-agent/overview  
- PagerDuty — **SRE Agent virtual responder** (approval-gated remediation; GA 2026-03, fully autonomous mode in early access; vendor observation): https://www.pagerduty.com/blog/ai/meet-your-virtual-responder-pagerdutys-sre-agent-for-ai-driven-reliability/  
- incident.io — **AI SRE** and the self-healing drift-masking anti-pattern (vendor observation): https://incident.io/ai-sre  
- Datadog — **Bits AI SRE** (validated/invalidated/inconclusive hypothesis classification; vendor observation): https://www.datadoghq.com/blog/bits-ai-sre/  
- Microsoft — **AKS incident→issue→coding-agent loop** (vendor observation): https://techcommunity.microsoft.com/blog/appsonazureblog/autonomous-aks-incident-response-with-azure-sre-agent-from-alert-to-verified-rec/4511343  
