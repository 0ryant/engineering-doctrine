# State Machines, Workflows, And Event Emission

Portable rules for systems whose behaviour is described by **states**, **transitions**, and **asynchronous** notifications. Complements [event-contracts.md](event-contracts.md) (what crosses the wire) and [patterns/message-channel-operations.md](../patterns/message-channel-operations.md) (delivery and failure). Transport and broker choices remain **tooling**—for example [../tooling/nats-jetstream.md](../tooling/nats-jetstream.md), Kafka, or a vendor bus.

End-to-end **illustration** (order lifecycle + JetStream): [../patterns/example-order-jetstream-workflow.md](../patterns/example-order-jetstream-workflow.md).

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

## 5. Sagas, Compensation, Timeouts, And Human Steps

Requirements are **tiered** so teams can adopt **timeouts** before full **saga** documentation, etc.

### 5.1 Saga And Compensation (Multi-Service Flows)

- **Must** for **any** workflow that spans **multiple** transactional boundaries with **partial failure**: document **forward** recovery and/or **compensating** actions per step, and behaviour when a downstream step **fails** after earlier steps **committed**.
- **N/A** for **single-service** transactions with ordinary **ACID** semantics—do not force saga notation where there is no **distributed** commit problem.

**Why:** *Enterprise Integration Patterns* and **saga** literature exist because **distributed** systems lack one global **ACID** transaction.

### 5.2 Timeouts And Wait States

- **Must:** every **wait** state has a **maximum** dwell time and a **defined** next state (retry with cap, **escalate** to human, **cancel**, or **dead-letter**).
- **Should:** publish **metrics** on dwell time so stuck workflows surface before users open tickets.

**Why:** Indefinite **pending** is a **reliability** and **support** sink.

### 5.3 Human-In-The-Loop

- **Must** when humans **approve** or **remediate**: transitions are **audited** (who/when/what); **re-posted** approvals remain **idempotent** (same decision token does not **double** effect).
- **Should:** tool-assisted **queues** for work items rather than ad-hoc email-only flows.

**Why:** Manual steps without **audit** and **idempotency** fail under **replay** and compliance review.

---

## 6. Scope

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
| Sagas explicit | **Long-running** flows need **compensation** / timeout semantics—not pretend two-phase commit across HTTP. |
| Timeouts mandatory | **Wait** states without caps become **silent** incidents. |
| Human steps audited | **Replay**-safe approvals satisfy **compliance** and idempotency. |

---

## References

- Enterprise Integration Patterns — **Message**, **Idempotent Receiver**, **Dead Letter Channel**: https://www.enterpriseintegrationpatterns.com/patterns/messaging/  
- CloudEvents (envelope at boundaries): https://github.com/cloudevents/spec  
- Martin Fowler — **Event Sourcing** (state from history, optimistic concurrency, rebuild): https://martinfowler.com/eaaDev/EventSourcing.html  
- Martin Fowler — **Saga** pattern: https://martinfowler.com/bliki/Saga.html  
- Canonical index: [../REFERENCES.md](../REFERENCES.md) — *Messaging, events, and NATS*  
