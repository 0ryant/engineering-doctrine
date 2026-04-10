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

## Operations (Sketch)

- **Consumer lag** is a primary SRE metric; alert on **age** and **rate** of growth.
- **Dead letters** — use **DLQ topic** or **quarantine** stream + tooling per estate; align with [message-channel-operations.md](../patterns/message-channel-operations.md).
- **Exactly-once** claims are **bounded** by producer/consumer semantics—document **effective** guarantees for finance-grade flows.

---

## References

- Apache Kafka **documentation**: https://kafka.apache.org/documentation/  
- CloudEvents — **Kafka protocol binding**: https://github.com/cloudevents/spec/blob/main/cloudevents/bindings/kafka-protocol-binding.md  
- Confluent — **Kafka consumer lag** (operational concept): search current Confluent or Kafka docs for *consumer lag monitoring*  
