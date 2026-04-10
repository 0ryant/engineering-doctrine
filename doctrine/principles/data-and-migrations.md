# Data, Migrations, Backups, And Recovery

Durable rules for **persisted state**: relational and document stores, object storage with lifecycle semantics, and **schema evolution** in systems that deploy continuously.

---

## 1. Schema Changes And Rolling Deploys

- **Forward-only migrations in production** — apply changes that **older running app versions** can still run against until they are fully replaced. Rolling deploys mean **N and N+1** coexist; the database must be valid for both during the overlap.
- **Expand → migrate → contract** (also called **parallel change**): add new structure first; move writers/readers; backfill; then remove old paths. This is the standard answer to “zero-downtime” schema change without heroic single-step cutovers.
- **Dangerous operations** (blocking locks, wide table rewrites, adding `NOT NULL` without a staged plan) are split into **multiple releases** with explicit checkpoints.
- **Backfills** run in **batches** with bounded row counts and pauses so replication and OLTP traffic stay healthy. **Typical starting defaults** (tune per engine and load): **1,000–50,000 rows** per batch for row-oriented OLTP, **50–500 ms** pause between batches, and **hard stop** (or halve batch size) if **replica lag** or **lock wait** exceeds team-defined thresholds—document your limits in the migration note.

**Why:** Most migration incidents are **ordering and compatibility** failures, not SQL syntax. The expand/contract sequence matches how **continuous delivery** actually works. Industry practice is widely documented under parallel change and zero-downtime migration guides.

---

## 2. Backups, Recovery, And Retention

- Define **RPO** (how much data loss is acceptable) and **RTO** (how long restore may take) per **data class** (customer data vs cache vs logs).
- **Automate backups**; **test restores** on a cadence. An untested backup is not a control.
- **Retention** follows product and legal requirements, not “keep everything forever.”

**Why:** Recovery objectives turn backup tooling into an **evidence-based** capability. Regulators and customers care about **demonstrated** restore, not checkbox backup jobs.

---

## 3. Operational Safety

- **Snapshots or PITR** (*point-in-time recovery*—see [glossary](../glossary.md)) before high-risk migrations where the platform supports it; document **rollback** as either a new forward migration or app rollback, not a fantasy “down migration” that drops data.
- **Replica lag** and **lock duration** are part of the migration review for large tables.

**Why:** Rollback stories that assume symmetric `up`/`down` SQL often **lose data** or break invariants; honest plans are easier to review.

---

## 4. Disaster Recovery, Multi-Region, And Failover Drills

- **RTO / RPO** for **regional** loss (not only single-host restore) are **explicit** where the product promises continuity; document **warm** vs **cold** standby (see [glossary](../glossary.md)) and **failover** triggers.
- **Failover drills** or **game days** exercise DNS, replication lag cutoffs, and **write** path behaviour—tabletop alone is insufficient for tier-1 data paths.
- **Backups** in §2 remain necessary but **not sufficient** for multi-region; replication **conflicts** and **split-brain** policies need written answers.

**Why:** AWS, Google, and Azure well-architected guidance all treat **DR** as distinct from backup; regulators and enterprise customers increasingly ask for **demonstrated** failover, not slide decks.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Prefer expand/contract over big-bang DDL | Matches **rolling deploys** and reduces blast radius; one step = one reviewable risk. |
| Forward-only in prod | Keeps pipeline **simple** and history **auditable**; “reverse” is often a new migration. |
| Batch backfills | Reduces lock contention and replica lag vs single massive updates. |
| Default batch / pause ranges | Gives operators a **first** knob to tune instead of inventing sizes from zero. |
| Explicit RPO/RTO | Aligns engineering with **business** risk; avoids generic “we have backups.” |
| DR beyond single restore | **Regional** failure modes need **rehearsed** paths, not only backup jobs. |

---

## References

- Martin Fowler, **ParallelChange** (parallel implementation for safe evolution): https://martinfowler.com/bliki/ParallelChange.html  
- Pramod Sadalage & Scott Ambler, *Refactoring Databases* (evolutionary database design patterns) — canonical book treatment of incremental schema change.  
- PostgreSQL and other vendors document **lock behaviour** and **concurrent** index/DDL options; always verify against your engine version.  
- James Ross Jr., “Database Migrations in Production: Zero-Downtime Strategies” (overview of safe vs unsafe DDL and expand/contract): https://www.jamesrossjr.com/blog/database-migrations-guide  
- Google Cloud — **Disaster recovery planning** (conceptual DR vs backup): https://cloud.google.com/architecture/dr-scenarios-planning-guide  
- AWS — **Disaster Recovery** whitepapers and well-architected reliability pillar (use current AWS docs for your estate)  
