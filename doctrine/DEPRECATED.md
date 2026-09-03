# Doctrine Lifecycle Register

The single **index** of lifecycle state for this library — what is scheduled for removal, what has exited, and what the sweeps decided. Governed by [patterns/doctrine-content-lifecycle.md](patterns/doctrine-content-lifecycle.md) §6; each file's own banner is canonical for its state, and this register is the derived index over them.

## Currently Deprecated (dying table)

| Target | ADR | Deprecated since | Replacement | Earliest removal |
| --- | --- | --- | --- | --- |
| [patterns/feature-flag-lifecycle.md](patterns/feature-flag-lifecycle.md) | [ADR 0045](../docs/adr/0045-execute-the-first-lifecycle-sweep.md) | Next tagged release (verdict recorded 2026-09-03, standalone sweep) | [patterns/feature-flag-governance.md](patterns/feature-flag-governance.md) | The release after the deprecating tag |
| [tooling/estates/aws-container-runtimes.md](tooling/estates/aws-container-runtimes.md) | [ADR 0045](../docs/adr/0045-execute-the-first-lifecycle-sweep.md) | Next tagged release (verdict recorded 2026-09-03) | [tooling/estates/TEMPLATE.md](tooling/estates/TEMPLATE.md) | The release after the deprecating tag |
| [tooling/estates/gcp-container-runtimes.md](tooling/estates/gcp-container-runtimes.md) | [ADR 0045](../docs/adr/0045-execute-the-first-lifecycle-sweep.md) | Next tagged release (verdict recorded 2026-09-03) | [tooling/estates/TEMPLATE.md](tooling/estates/TEMPLATE.md) | The release after the deprecating tag |

## Tombstones (executed exits)

Append-and-annotate only ([lifecycle §6](patterns/doctrine-content-lifecycle.md)).

| Target | Exit state | Deprecated since | Rationale | ADR | Exit release | Restoration |
| --- | --- | --- | --- | --- | --- | --- |
| *(none yet)* | | | | | | |

## Sweep ledger

| Sweep date | Record | Verdicts summary |
| --- | --- | --- |
| 2026-09-03 | [evolution/sweep-2026-09.md](evolution/sweep-2026-09.md) (standalone, first sweep) | ADR 0021 accepted and landed; feature-flag-lifecycle superseded by feature-flag-governance; AWS and GCP estate stubs deprecated; Azure supplement retained; cohort link health checked (2 dead links recorded); staleness and fade engines not yet armed |

Nothing has yet been retired; the first removals become possible one release after the next tagged release stamps the banners recorded above.
