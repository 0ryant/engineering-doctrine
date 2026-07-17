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

### Ordering And “Exactly-Once” By Broker Class (Sketch)

| Broker / pattern | Typical ordering | “Exactly-once” reality |
| --- | --- | --- |
| **Single partition / shard** (Kafka topic partition, JetStream ordered consumer, SQS FIFO per group) | **Strong** per key when keyed correctly | Still **at-least-once** at the wire—use a duplicate-handling strategy at the controlling boundary |
| **Competing consumers** on a shared queue | **No** global order | Duplicate delivery common under redelivery |
| **Pub/sub fan-out** | Order **not** meaningful across subscribers | Each subscriber must protect material side effects from duplicate delivery |

**Why:** Vendors market **effectively-once** processing; engineering doctrine should assume **at-least-once** delivery unless **you** prove end-to-end single-commit semantics.

---

## Idempotency And Dedup

- Where at-least-once delivery applies, consumers should use the CloudEvents **`source` + `id` pair** (or an equivalent producer-scoped identity) in their duplicate-handling strategy. The controlling boundary may record the first outcome, enforce a conditional transition, deduplicate delivery, or use an idempotent effect; see [idempotency-across-boundaries.md](idempotency-across-boundaries.md).

---

## Observability

- Metrics: **depth age**, **DLQ rate**, **processing lag**, **retry count** per event type.
- Logs/traces: **correlation** from `id`, `type`, `subject` onto spans for incident triage.

---

## Relation To Other Doctrine

- **Schema / envelope** — `event-contracts.md`, `tooling/cloudevents.md`.
- **Behaviour and transitions** — `principles/state-machines-and-workflows.md`.
- **Illustrative durable broker (NATS JetStream)** — `tooling/nats-jetstream.md`; **Kafka + CloudEvents** sketch — `tooling/kafka-and-cloudevents.md`; **worked fiction** — `patterns/example-order-jetstream-workflow.md`.
- **SLOs** — if processing latency matters to users, define an SLO on **lag** or **time-to-handle**, not only API latency.

---

## References

- AWS — **dead-letter queues** (concept, widely mirrored): search vendor docs for “SQS dead-letter queue” or your broker’s equivalent.
- Azure — **Service Bus dead-lettering**: https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-dead-letter-queues  
- **Enterprise Integration Patterns** — Dead Letter Channel (conceptual): https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html  
