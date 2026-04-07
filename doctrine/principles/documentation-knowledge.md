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
- Runbooks are **tested** or **walked** periodically; stale runbooks are flagged.

**Why:** On-call time is expensive; “tribal knowledge” fails at 3am under stress.

---

## 3. README And Boundaries

- **README** states purpose, architecture sketch, **setup**, and pointers to contracts and pipelines.
- **Ownership** (team or channel) is obvious for the repo.

**Why:** Reduces **time-to-first-contribution** and misrouted incidents.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| ADRs over oral tradition | Scales with org size; supports **audit** of why systems look the way they do. |
| Runnable or reviewed runbooks | Closes the gap between **docs** and **reality**. |

---

## References

- **ADR GitHub organisation** — templates and community resources: https://adr.github.io/  
- Michael Nygard, **Documenting Architecture Decisions** (original article, archived mirrors linked from ADR community): widely cited as the start of ADR practice; see `adr.github.io` for maintained templates.  
