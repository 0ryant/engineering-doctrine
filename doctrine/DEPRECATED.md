# Doctrine Lifecycle Register

The single **index** of lifecycle state for this library — what is scheduled for removal, what has exited, and what the sweeps decided. Governed by [patterns/doctrine-content-lifecycle.md](patterns/doctrine-content-lifecycle.md) §6; each file's own banner is canonical for its state, and this register is the derived index over them.

## Currently Deprecated (dying table)

| Target | ADR | Deprecated since | Replacement | Earliest removal |
| --- | --- | --- | --- | --- |
| [patterns/feature-flag-lifecycle.md](patterns/feature-flag-lifecycle.md) | [ADR 0045](../docs/adr/0045-execute-the-first-lifecycle-sweep.md) | v0.5.0 | [patterns/feature-flag-governance.md](patterns/feature-flag-governance.md) | The release after v0.5.0 |
| [tooling/estates/aws-container-runtimes.md](tooling/estates/aws-container-runtimes.md) | [ADR 0045](../docs/adr/0045-execute-the-first-lifecycle-sweep.md) | v0.5.0 | [tooling/estates/TEMPLATE.md](tooling/estates/TEMPLATE.md) | The release after v0.5.0 |
| [tooling/estates/gcp-container-runtimes.md](tooling/estates/gcp-container-runtimes.md) | [ADR 0045](../docs/adr/0045-execute-the-first-lifecycle-sweep.md) | v0.5.0 | [tooling/estates/TEMPLATE.md](tooling/estates/TEMPLATE.md) | The release after v0.5.0 |

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

Nothing has yet been retired; the first removals become possible in the release after v0.5.0.
