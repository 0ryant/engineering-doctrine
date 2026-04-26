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
| **Executive / legal / customer liaison** | **Only** as required by **severity** and **regulatory** context—not every incident needs a C-suite. |

**Must not:** have **no** single IC in a **multi-team** response—**everyone** owns it means **no one** owns it.

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
- **Track** **actions** to **completion**; **reopen** the **conversation** if the **same** **failure class** recurs. **DORA** **change-failure** and **restoration** metrics improve when **this** **closes**.

**Why:** The principle file already **requires** **tracked** **actions**; this pattern **ties** them to **roles** and **cadence** so the **ritual** **sticks**.

---

## 10. Relation to SLOs, game days, and platform ownership

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

---

## Related

- [reliability-slo-incidents.md](../principles/reliability-slo-incidents.md) — SLOs, error budgets, high-level **incident** and **toil** rules
- [chaos-engineering-and-game-days.md](chaos-engineering-and-game-days.md) — **exercises** and **rehearsal**
- [documentation-knowledge.md](../principles/documentation-knowledge.md) — runbooks, **operational** **knowledge**
- [observability.md](../principles/observability.md) — **signals** that **feed** **severity** and **impact**
- [platform-as-product-and-golden-paths.md](platform-as-product-and-golden-paths.md) — **escalation** to **platform**
- [measurement-and-dora.md](../principles/measurement-and-dora.md) — **restore** **time** and **learning** **loops**

---

## References

- Google *Site Reliability Engineering* (O’Reilly) — **Managing Incidents** and **Postmortem Culture**: https://sre.google/sre-book/table-of-contents/  
- Atlassian (example **incident** **management** and **comms** vocabulary): public **ITSM** and **on-call** playbooks in product docs (verify current URLs).  
- *Practical Monitoring* / industry **on-call** practice—see [REFERENCES.md](../REFERENCES.md) for the library’s **external** index.
