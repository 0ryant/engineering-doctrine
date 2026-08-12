# Evidence Exception Register

The single index of **evidence-floor exceptions** for this library — normative or cited content admitted below the floors of [patterns/source-authority-and-evidence-grading.md](patterns/source-authority-and-evidence-grading.md) §5–§6. Each entry is a [normative-language-applicability-and-exceptions.md](patterns/normative-language-applicability-and-exceptions.md) §5 exception in record shape: adjudicated once, **reusable while in force** by later claims citing the same source at the same level, and never permanent — a deviation that should not expire is a change to policy or profile. Entries are re-examined by every lifecycle sweep ([patterns/doctrine-content-lifecycle.md](patterns/doctrine-content-lifecycle.md) §8); this register doubles as the evidence-upgrade worklist. Decision record: [ADR 0040](../docs/adr/0040-adopt-source-authority-classes-and-evidence-weighted-citations.md).

## Active exceptions

Column mapping to the normative-language §5 minimum record: *Claim/surface* = rule and exact scope; *Source and floor* = finding and evidence state; *Justification* = rationale and residual risk (borne by this library's readers unless stated); *Approver* = authority; *Date/Expiry* = time bounds — **expiry without renewal ends the exception**: the claim loses its typed standing or the citation is removed, per that pattern's behaviour-on-expiry rule; *Upgrade path* = compensating control and remediation. Status is the table an entry sits in.

| ID | Claim / surface | Source and floor not met | Justification | Approver | Date | Expiry | Upgrade path |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EX-0001 | The August 2026 research notes' §8/§5 ledgers ([target-state](evolution/research-target-state-and-irreversible-decisions-2026-08.md), [source-authority](evolution/research-source-authority-and-evidence-weighting-2026-08.md)) | Web citations lack `archived-url` legs — the §6 admission-time-archive expectation | Archival tooling absent at admission (perma.cc bot-blocked; Robust Links domain dead); both notes landed before the pattern existed — the source-authority note records the deviation in its own caveats; the target-state note's ledger is covered by this entry's scope (its caveats predate the rule) | Operator | 2026-08-12 | 2027-02-12, or discharge at the first sweep that captures archives for still-reachable ledger rows, whichever first | Capture snapshots for reachable rows at the first lifecycle sweep once archival tooling is operable (absent at landing — the carryover is explicit); rows already degraded (ODNI, DoD primary, iso.org) are recorded unrecoverable in the source-authority note's caveats |
| EX-0002 | Context-engineering vocabulary attribution in [patterns/agentic-loop-design.md](patterns/agentic-loop-design.md) §References (Karpathy tweet, Jun 2025) | S7 source below the §5 illustrative floor (≥S6, pinned and dated) | The tweet is the canonical coinage moment of a term the pattern uses; no durable source carries the same attribution; the reference is vocabulary provenance, not claim support | Operator | 2026-08-12 | 2027-08-12, or replacement with a durable source, whichever first | Swap to an archived snapshot or a durable essay carrying the same attribution when one exists; the sweep re-checks |

## Discharged exceptions

Append-and-annotate only.

| ID | Discharged | How |
| --- | --- | --- |
| *(none yet)* | | |

An empty active table is a meaningful statement: every typed claim currently meets its evidence floor.
