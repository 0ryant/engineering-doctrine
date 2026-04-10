# Kafka And CloudEvents (Illustrative Tooling)

**Illustrative** notes for teams using **Apache Kafka** (or compatible log brokers) with **CloudEvents**. Does not change [event-contracts.md](../principles/event-contracts.md) or [message-channel-operations.md](../patterns/message-channel-operations.md).

---

## When Kafka Fits

- High **throughput**, **durable** log retention, **replay** by offset, **consumer groups** for scale-out.
- **Ordering** per **partition** key (often entity id).

Prefer managed **PaaS** Kafka or estate-approved operators; tuning is **tooling**, not universal law.

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

## References

- Apache Kafka **documentation**: https://kafka.apache.org/documentation/  
- CloudEvents — **Kafka protocol binding**: https://github.com/cloudevents/spec/blob/main/cloudevents/bindings/kafka-protocol-binding.md  
- Confluent — **Kafka consumer lag** (operational concept): search current Confluent or Kafka docs for *consumer lag monitoring*  
