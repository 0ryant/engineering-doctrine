# Message Channel Operations

Companion to [principles/event-contracts.md](../principles/event-contracts.md). **Contracts** define shape and semantics; **this pattern** covers **operational** behaviour for queues, topics, and buses: failure, replay, and poison messages.

---

## Intent

- Make **at-least-once** (and similar) delivery **safe** via explicit consumer design.
- Avoid **silent loss** of messages and **unbounded** poison queues.
- Align with SRE expectations: **observable** backlog, **actionable** runbooks.

---

## Dead-Letter And Poison Messages

- **Dead-letter queue (DLQ)** or **poison topic** — after **N** failures or **specific** non-retryable errors, move the message to a **separate** destination; do not retry forever.
- **Poison definition** — document what makes a message non-retryable (schema violation, oversize payload, unknown type).
- **Retention** on DLQ — bounded time or size with **alerting** before loss; align with data governance.

**Why:** Without a DLQ policy, teams either lose failures in logs or **block** partitions indefinitely.

---

## Replay And Ordering

- **Replay** is a **deliberate** operator action with **scope** (single id, batch, time window) and **risk** note (duplicate side effects if idempotency is imperfect).
- **Ordering** — if consumers assume per-key ordering, document **partition key**; replays may **violate** strict ordering—call that out.

**Why:** Replay without idempotency causes **duplicate** real-world effects; reviewers must see that contract.

---

## Idempotency And Dedup

- Consumers should treat **`CloudEvents` `id`** (or equivalent) as the **dedup** key where at-least-once applies; persist **processed ids** or use **idempotent** writes (see event-contracts semantics section).

---

## Observability

- Metrics: **depth age**, **DLQ rate**, **processing lag**, **retry count** per event type.
- Logs/traces: **correlation** from `id`, `type`, `subject` onto spans for incident triage.

---

## Relation To Other Doctrine

- **Schema / envelope** — `event-contracts.md`, `tooling/cloudevents.md`.
- **Behaviour and transitions** — `principles/state-machines-and-workflows.md`.
- **Illustrative durable broker (NATS JetStream)** — `tooling/nats-jetstream.md`.
- **SLOs** — if processing latency matters to users, define an SLO on **lag** or **time-to-handle**, not only API latency.

---

## References

- AWS — **dead-letter queues** (concept, widely mirrored): search vendor docs for “SQS dead-letter queue” or your broker’s equivalent.
- Azure — **Service Bus dead-lettering**: https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-dead-letter-queues  
- **Enterprise Integration Patterns** — Dead Letter Channel (conceptual): https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html  
