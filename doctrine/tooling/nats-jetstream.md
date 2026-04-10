# NATS And JetStream (Illustrative Tooling)

**Illustrative** mapping for teams using **[NATS.io](https://nats.io/)** with **[JetStream](https://docs.nats.io/nats-concepts/jetstream)** for durable streaming and work queues. This does **not** change portable rules in [../principles/event-contracts.md](../principles/event-contracts.md) or [../principles/state-machines-and-workflows.md](../principles/state-machines-and-workflows.md)—it shows **how** one stack implements them.

Companion: [cloudevents.md](cloudevents.md) (envelope baseline), [../patterns/message-channel-operations.md](../patterns/message-channel-operations.md) (DLQ, replay, observability).

Worked **fiction** tying FSM → `type` → subjects/consumers: [../patterns/example-order-jetstream-workflow.md](../patterns/example-order-jetstream-workflow.md). **Saga** (broker-agnostic): [../patterns/example-saga-payment-workflow.md](../patterns/example-saga-payment-workflow.md).

---

## When This Stack Fits

- **Fan-out** and **many consumers** with light operational overhead.
- **Durable** interest: JetStream **streams** retain messages with limits; **consumers** track delivery position.
- **Work-queue** patterns (competing consumers) or **ordered** stream consumption per subject key.

Prefer another broker when the org has already standardised on Kafka, Pulsar, or a managed cloud bus—keep the same **CloudEvents + workflow** principles.

---

## Core Concepts (Short)

| Concept | Role |
| --- | --- |
| **Subject** | Address string for messages; hierarchy with `.` (for example `orders.created`). |
| **Stream** | JetStream storage + retention policy over a **subject set**. |
| **Consumer** | Named pull or push subscription with **durable** cursor, **ack** model, **max deliveries**, optional **replay**. |
| **Core NATS** | Fire-and-forget without JetStream—no persistence; not a substitute for durability requirements. |

Confirm options against current NATS/JetStream docs (APIs and defaults evolve).

---

## CloudEvents On NATS

- Prefer the **[NATS protocol binding for CloudEvents](https://github.com/cloudevents/spec/blob/main/cloudevents/bindings/nats-protocol-binding.md)** when interop matters: **structured** mode (JSON event in body) or **binary** mode (attributes in NATS headers on server **2.2+**, payload = `data`).
- If you intentionally deviate, document the mapping; still set `id`, `type`, `source`, and `time` consistently so traces align with [cloudevents.md](cloudevents.md).
- Use **`subject`** for routing; align **`ce_subject`** (or payload field) with partition **entity id** when ordering per entity matters—see [../principles/event-contracts.md](../principles/event-contracts.md).

---

## Operational Alignment (JetStream)

- **At-least-once** — configure **MaxAckPending**, **MaxDeliver**, and **AckWait** / **Backoff** per current [consumer](https://docs.nats.io/nats-concepts/jetstream/consumers) docs. Note: **Backoff** applies to ack **timeout** redelivery; **NAK** is immediate unless the client supports **NAK with delay**—design retries accordingly.
- When **MaxDeliver** is exhausted, messages typically **remain in the stream** until handled (e.g. terminal ack, delete, or operator process)—plan **poison** handling explicitly; JetStream has no single “DLQ checkbox”; patterns use **advisories**, **mirror streams**, or app-level dead letters. Align with [message-channel-operations.md](../patterns/message-channel-operations.md).
- **Replay** — by sequence or time; document impact on **idempotent** consumers and workflow state—see [state-machines-and-workflows.md](../principles/state-machines-and-workflows.md).
- **Observability** — export stream **lag**, **pending**, **redelivery** counts; tie **`ce_id`** to traces (OpenTelemetry) where used.

---

## Naming Hygiene

- Stream and durable consumer names are **operational** identifiers—document **ownership** and **environments** (dev/stage/prod) to avoid cross-talk.
- Subject taxonomy should reflect **domain** boundaries, not only infrastructure layers.

---

## References

- NATS documentation: https://docs.nats.io/  
- JetStream concepts: https://docs.nats.io/nats-concepts/jetstream  
- JetStream consumers: https://docs.nats.io/nats-concepts/jetstream/consumers  
- CloudEvents — NATS protocol binding: https://github.com/cloudevents/spec/blob/main/cloudevents/bindings/nats-protocol-binding.md  
- CloudEvents spec (overview): https://github.com/cloudevents/spec  
- Canonical index: [../REFERENCES.md](../REFERENCES.md) — *Messaging, events, and NATS*  
