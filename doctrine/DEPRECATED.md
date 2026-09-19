# Doctrine Lifecycle Register

The single **index** of lifecycle state for this library — what is scheduled for removal, what has exited, and what the sweeps decided. Governed by [patterns/doctrine-content-lifecycle.md](patterns/doctrine-content-lifecycle.md) §6; each file's own banner is canonical for its state, and this register is the derived index over them.

## Currently Deprecated (dying table)

| Target | ADR | Deprecated since | Replacement | Earliest removal |
| --- | --- | --- | --- | --- |
| [patterns/feature-flag-lifecycle.md](patterns/feature-flag-lifecycle.md) | [ADR 0045](../docs/adr/0045-execute-the-first-lifecycle-sweep.md) | v0.5.0 | [patterns/feature-flag-governance.md](patterns/feature-flag-governance.md) | First minor release cut at least 90 days after v0.5.0 ([lifecycle §4](patterns/doctrine-content-lifecycle.md#4-deprecation-mechanics)) |
| [tooling/estates/aws-container-runtimes.md](tooling/estates/aws-container-runtimes.md) | [ADR 0045](../docs/adr/0045-execute-the-first-lifecycle-sweep.md) | v0.5.0 | [tooling/estates/TEMPLATE.md](tooling/estates/TEMPLATE.md) | First minor release cut at least 90 days after v0.5.0 ([lifecycle §4](patterns/doctrine-content-lifecycle.md#4-deprecation-mechanics)) |
| [tooling/estates/gcp-container-runtimes.md](tooling/estates/gcp-container-runtimes.md) | [ADR 0045](../docs/adr/0045-execute-the-first-lifecycle-sweep.md) | v0.5.0 | [tooling/estates/TEMPLATE.md](tooling/estates/TEMPLATE.md) | First minor release cut at least 90 days after v0.5.0 ([lifecycle §4](patterns/doctrine-content-lifecycle.md#4-deprecation-mechanics)) |

## Tombstones (executed exits)

Append-and-annotate only ([lifecycle §6](patterns/doctrine-content-lifecycle.md)).

| Target | Exit state | Deprecated since | Rationale | ADR | Exit release | Restoration |
| --- | --- | --- | --- | --- | --- | --- |
| *(none yet)* | | | | | | |

## Sweep ledger

| Sweep date | Record | Verdicts summary |
| --- | --- | --- |
| 2026-09-03 | [evolution/sweep-2026-09.md](evolution/sweep-2026-09.md) (standalone, first sweep) | ADR 0021 accepted and landed; feature-flag-lifecycle superseded by feature-flag-governance; AWS and GCP estate stubs deprecated; Azure supplement retained; cohort link health checked (2 dead links recorded); staleness and fade engines not yet armed |
| 2026-09-14 | [evolution/sweep-2026-09.md §7](evolution/sweep-2026-09.md#7-v050-release-coupled-follow-up-2026-09-14) (v0.5.0 release-coupled follow-up) | Three scheduled deprecations activated; replacements confirmed active; 34 principle summaries re-read; Proposed ADR and evidence-exception clocks checked; full reference-status leg completed and active rot repaired |

Nothing has yet been retired. The v0.5.0 tag was cut on 2026-09-15, so the
90-day floor falls on 2026-12-14; removal is eligible only in a minor release
cut at or after that floor, not automatically on that date. See the
[dated clarification in ADR 0045](../docs/adr/0045-execute-the-first-lifecycle-sweep.md#clarification-2026-09-19-removal-floor)
for the tag timestamp and the reconciliation to the already-adopted rule.
