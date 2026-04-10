# Kafka And CloudEvents (Illustrative Tooling)

**Illustrative** mapping for teams using **Apache Kafka** (or compatible log brokers) with **CloudEvents**. This does **not** change portable rules in [../principles/event-contracts.md](../principles/event-contracts.md) or [../patterns/message-channel-operations.md](../patterns/message-channel-operations.md)—it shows **how** one stack implements them.

Companion: [cloudevents.md](cloudevents.md) (envelope baseline), [../patterns/message-channel-operations.md](../patterns/message-channel-operations.md) (DLQ, replay, observability).

Worked **fiction** — **order** workflow on JetStream (different broker, same principles): [../patterns/example-order-jetstream-workflow.md](../patterns/example-order-jetstream-workflow.md). **Saga** across services (broker-agnostic): [../patterns/example-saga-payment-workflow.md](../patterns/example-saga-payment-workflow.md).

---

## When Kafka Fits

- High **throughput**, **durable** log retention, **replay** by offset, **consumer groups** for scale-out.
- **Ordering** per **partition** key (often entity id).

Prefer managed **PaaS** Kafka or estate-approved operators; tuning is **tooling**, not universal law.

Prefer **NATS JetStream** when the org already standardised on it—see [nats-jetstream.md](nats-jetstream.md); keep the same **CloudEvents + workflow** principles.

---

## Core Concepts (Short)

| Concept | Role |
| --- | --- |
| **Topic** | Named log of records; **partitions** provide parallelism and ordering scope. |
| **Partition** | Ordered, append-only **slice** of a topic; **key** selects partition for per-key ordering. |
| **Consumer group** | Co-operative consumers sharing partition assignment; **one** consumer reads each partition at a time. |
| **Offset** | Position in a partition; **committed** offsets define **at-least-once** progress. |
| **Broker** | Kafka server; cluster **replication** and **ISR** semantics are **estate** configuration. |

Confirm options against current [Kafka documentation](https://kafka.apache.org/documentation/) (APIs and defaults evolve).

---

## CloudEvents On Kafka

- Use the **[Kafka protocol binding](https://github.com/cloudevents/spec/blob/main/cloudevents/bindings/kafka-protocol-binding.md)** where possible: **key** for partition, **value** for structured or binary event, headers for `ce_*` attributes in binary mode.
- **Topic** naming reflects **domain** boundaries; **version** breaking changes via **new** topic or **compatibility** policy on schemas (see [cloudevents.md](cloudevents.md)).

---

## Operations And Production Defaults

- **Consumer lag** — treat **max lag** (or **time-behind-latest**) per **consumer group** + **topic** as a **first-class** SLO input when async processing is user-visible; alert on **absolute** lag and **derivative** (is backlog **growing**?). See current Kafka / vendor docs for **metrics** names (`records-lag-max`, etc.).
- **Partitions and keys** — choose **partition key** to preserve needed **ordering**; **too few** partitions caps throughput; **too many** small partitions increases overhead—size for **peak** publish rate with headroom, document **repartition** as a **breaking** operational change.
- **Retention and compaction** — set **retention.ms** / **compact** policy per **topic** class (event log vs command queue); **infinite** retention has **cost** and **GDPR** implications for **PII** payloads—align with [privacy-and-data-governance.md](../principles/privacy-and-data-governance.md).
- **Producers** — configure **acks** and **idempotence** (where supported) for **critical** writes; document **failure** modes (partial ack, duplicate publish) in the service **runbook**.
- **Dead letters** — use a **dedicated** DLQ topic or **quarantine** stream plus **replay** procedure; **not** only log-and-drop. Align with [message-channel-operations.md](../patterns/message-channel-operations.md).
- **Exactly-once** — broker and client **EOS** is **bounded** by configuration and **side effects**; for **money** paths, assume **at-least-once** + **idempotent** consumers unless **you** have proven end-to-end semantics—see [idempotency-across-boundaries.md](../patterns/idempotency-across-boundaries.md).
- **AuthZ / TLS** — **SASL** / **mTLS** and **ACLs** on topics are **estate** choices; record the **pattern** in `tooling/estates/`—see [zero-trust-and-workload-identity.md](../principles/zero-trust-and-workload-identity.md).

---

## Naming Hygiene

- **Topic** names are **operational** contracts—prefix by **domain** and **environment** (`prod.orders.events` vs `dev.orders.events`) to avoid cross-talk.
- **Consumer group** ids must be **stable** per logical app; changing a group id **resets** consumption position unless you **seek** explicitly—document **migration** when renaming.
- **Schema** subjects (if using Schema Registry) should align with **event `type`** or payload versioning—see [../principles/event-contracts.md](../principles/event-contracts.md).

---

## References

- Apache Kafka **documentation**: https://kafka.apache.org/documentation/  
- CloudEvents — **Kafka protocol binding**: https://github.com/cloudevents/spec/blob/main/cloudevents/bindings/kafka-protocol-binding.md  
- CloudEvents spec (overview): https://github.com/cloudevents/spec  
- Canonical index: [../REFERENCES.md](../REFERENCES.md) — *Messaging, events, and NATS* (Kafka binding listed under standards)  
