# Doctrine Lifecycle Register

The single **index** of lifecycle state for this library — what is scheduled for removal, what has exited, and what the sweeps decided. Governed by [patterns/doctrine-content-lifecycle.md](patterns/doctrine-content-lifecycle.md) §6; each file's own banner is canonical for its state, and this register is the derived index over them.

## Currently Deprecated (dying table)

| Target | ADR | Deprecated since | Replacement | Earliest removal |
| --- | --- | --- | --- | --- |
| *(none)* | | | | |

## Tombstones (executed exits)

Append-and-annotate only ([lifecycle §6](patterns/doctrine-content-lifecycle.md)).

| Target | Exit state | Deprecated since | Rationale | ADR | Exit release | Restoration |
| --- | --- | --- | --- | --- | --- | --- |
| *(none yet)* | | | | | | |

## Sweep ledger

| Sweep date | Record | Verdicts summary |
| --- | --- | --- |
| *(none yet)* | | |

An empty register is a meaningful statement: nothing is currently scheduled for removal, and nothing has yet been retired.
