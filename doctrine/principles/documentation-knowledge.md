# Documentation And Organisational Knowledge

Durable rules for **decisions**, **operations**, and **onboarding** so intent survives turnover and chat scrollback.

---

## 1. Decisions In Writing

- **Significant** technical choices use **ADRs** (Architecture Decision Records), short RFCs, or an equivalent **decision log** in-repo.
- Each record captures **context**, **decision**, and **consequences**; superseded decisions are **linked**, not erased.

**Why:** Async collaboration (already in `collaboration.md`) requires a **system of record**. ADR templates are widely used for exactly this.

---

## 2. Runbooks And On-Call

- **Runbooks** exist for deploy, rollback, common failures, and **data fixes** that recur.
- Runbooks are **tested** or **walked** on a **defined cadence**: **at least quarterly** for **tier-1** paths (on-call pages, revenue, safety), and **within 30 days** after **material** changes to architecture, deploy path, or dependencies for any runbook **affected**. Record **last exercised** date in the runbook header or adjacent index. Tie to **game days** or **drills** where your org runs them ([reliability-slo-incidents.md](reliability-slo-incidents.md)).

**Why:** On-call time is expensive; “tribal knowledge” fails at 3am under stress.

---

## 3. README And Boundaries

- **README** states purpose, architecture sketch, **setup**, and pointers to contracts and pipelines.
- **Ownership** (team or channel) is obvious for the repo.

**Why:** Reduces **time-to-first-contribution** and misrouted incidents.

---

## 4. RFC Lifecycle Versus ADRs

- Use **RFCs** (or design docs) for **pre-decision** exploration: options, trade-offs, and **review** before commitment—especially when multiple teams must align.
- Promote outcomes to **ADRs** once a decision is **made**; link the RFC in the ADR’s **context** section.
- **Stale** RFCs should be **closed** or **superseded** so search results do not contradict shipped reality.

**Why:** ADRs record **what** was chosen; RFCs record **how** you got there—mixing both in one format confuses readers.

---

## 5. Onboarding Curricula And Discoverability

- Maintain a **short** onboarding path (day-one tasks, repo map, “how we ship”) separate from **encyclopaedic** doctrine.
- Prefer a **single** internal **portal** or **search** index that lists **golden paths**, service catalog links, and **runbooks**—even if the underlying content lives in Git.

**Why:** *Software Engineering at Google* emphasises **discoverable** engineering knowledge; new hires fail on **navigation**, not lack of Markdown files.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| ADRs over oral tradition | Scales with org size; supports **audit** of why systems look the way they do. |
| Runnable or reviewed runbooks | Closes the gap between **docs** and **reality**. |
| Quarterly + post-change exercise | Prevents **stale** procedures without over-burdening small teams. |
| RFC before ADR for big bets | Separates **exploration** noise from **decision** record. |

---

## References

- **ADR GitHub organisation** — templates and community resources: https://adr.github.io/  
- Michael Nygard, **Documenting Architecture Decisions** (original article, archived mirrors linked from ADR community): widely cited as the start of ADR practice; see `adr.github.io` for maintained templates.  
- *Software Engineering at Google*, Chapter 3 — **Knowledge Sharing**: https://abseil.io/resources/swe-book/html/ch03.html  
