# State Machines, Workflows, And Event Emission

Portable rules for systems whose behaviour is described by **states**, **transitions**, and **asynchronous** notifications. Complements [event-contracts.md](event-contracts.md) (what crosses the wire) and [patterns/message-channel-operations.md](../patterns/message-channel-operations.md) (delivery and failure). Transport and broker choices remain **tooling**—for example [../tooling/nats-jetstream.md](../tooling/nats-jetstream.md), Kafka, or a vendor bus.

---

## 1. Make The Model Explicit

- Define **states** and **allowed transitions** (diagram, table, or formal spec)—not only a stream of event types.
- For each transition, record **who** may trigger it (user action, scheduler, compensating job, admin) and **preconditions** (data, permissions, caps).
- **Terminal** and **error** states are first-class; document **recovery** paths (retry, manual fix, cancellation).

**Why:** Event schemas without a behavioural model hide **illegal** transitions and double-application bugs.

---

## 2. One Commitment Story Per Transition

- A transition is **committed** when durable state matches the new state and **downstream effects** are defined—either applied, **scheduled**, or **outboxed** with a clear idempotency story.
- **At-least-once** delivery means the **same** transition may be **observed** more than once; consumers must not assume “once per real-world act” unless the producer **dedupes** or the consumer is **idempotent**.

**Why:** Aligns with semantics in [event-contracts.md](event-contracts.md) (ordering, delivery, dedup via `id`).

---

## 3. Map Transitions To Event Types

- Each **committed** transition that other systems care about should correspond to **stable** CloudEvents `type` values (or a documented equivalent) and **versioned** payloads—see [event-contracts.md](event-contracts.md).
- Avoid reusing one `type` for **different** transitions or payload shapes; add a version or new type when consumers would break.

**Why:** Reviewers and contract tests can trace **FSM edge → event type → schema**.

---

## 4. Reconciliation And Projection

- If state is **derived** from events (projection, read model), document **ordering** assumptions and **lag** tolerance.
- Provide a path to **rebuild** or **reconcile** state from history or from an authoritative store when projections drift.

**Why:** Replay and backlog processing (see [message-channel-operations.md](../patterns/message-channel-operations.md)) routinely **re-deliver** old events.

---

## 5. Scope

| In scope | Out of scope (tooling or product docs) |
| --- | --- |
| States, transitions, idempotency, event-type mapping | Specific broker config, stream names, consumer SDKs |
| Correlation across saga-like flows | Vendor workflow engines as mandatory standard |

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Principle, not a pattern only | Behavioural contracts are **as durable** as payload schemas; they belong beside **event-contracts**. |
| Transport-agnostic | JetStream, Kafka, and SaaS buses all need the same **transition + dedup** discipline. |

---

## References

- Enterprise Integration Patterns — **Message**, **Idempotent Receiver**: https://www.enterpriseintegrationpatterns.com/patterns/messaging/  
- CloudEvents (envelope at boundaries): https://github.com/cloudevents/spec  
