# Example: Order Workflow On JetStream (Fiction)

**Illustrative only** — not a product standard. Shows how [state-machines-and-workflows.md](../principles/state-machines-and-workflows.md), [event-contracts.md](../principles/event-contracts.md), and [nats-jetstream.md](../tooling/nats-jetstream.md) fit together. Replace domain names, subjects, and retention with your org’s choices.

---

## 1. Behavioural Model (Excerpt)

| State | Allowed transitions | Trigger |
| --- | --- | --- |
| `draft` | → `submitted` | User confirms cart |
| `submitted` | → `paid`, `cancelled` | Payment result or timeout job |
| `paid` | → `fulfilled` | Warehouse ships |
| `fulfilled` | — | terminal |
| `cancelled` | — | terminal |

**Committed transition** = durable order row (or aggregate version) updated **and** outbound event emitted (or outboxed then published).

---

## 2. CloudEvents `type` Map (Examples)

| Transition committed | `type` (example) | `subject` (entity id) |
| --- | --- | --- |
| draft → submitted | `com.example.order.submitted.v1` | order id |
| submitted → paid | `com.example.order.paid.v1` | order id |
| submitted → cancelled | `com.example.order.cancelled.v1` | order id |
| paid → fulfilled | `com.example.order.fulfilled.v1` | order id |

Payload contracts live in repo `contracts/events/` (JSON Schema); envelope per [cloudevents.md](../tooling/cloudevents.md) and [NATS binding](https://github.com/cloudevents/spec/blob/main/cloudevents/bindings/nats-protocol-binding.md).

---

## 3. NATS Subjects And Stream (Example)

| Element | Example value | Notes |
| --- | --- | --- |
| Subject namespace | `orders.>` | Domain prefix; `>` captures hierarchy |
| Stream name | `ORDERS` | JetStream stream over `orders.>` |
| Retention | `limits` or `interest` | Team choice; document RPO for replay |
| Durable consumer (fulfilment) | `fulfilment-worker` | Pull, **AckExplicit**, **MaxDeliver** set |

**Subject examples:**

- `orders.submitted` — published when transition to `submitted` commits  
- `orders.paid` — when `paid` commits  

Routing can be one subject per `type` or a single stream subject with filtering on `ce_type` in the consumer—pick one convention per estate and document it.

---

## 4. Consumer Discipline (Sketch)

- **Idempotency:** persist processed `ce_id` (or idempotent DB write on order id + transition).
- **Poison:** after **MaxDeliver**, message remains in stream; subscribe to advisories or copy to a **poison** stream `ORDERS_POISON` with an operator runbook ([message-channel-operations.md](message-channel-operations.md)).
- **Replay:** time- or seq-based replay documented; warn that **fulfilled** may be seen again—consumer must be safe.

---

## 5. What To Copy Vs Replace

| Copy as pattern | Replace with your domain |
| --- | --- |
| FSM → event type table | Your states and `type` taxonomy |
| Subject + stream + durable name hygiene | Your naming and retention |
| Idempotency + poison + replay checklist | Your SLOs and tooling |

---

## References

- [nats-jetstream.md](../tooling/nats-jetstream.md)  
- [state-machines-and-workflows.md](../principles/state-machines-and-workflows.md)  
- [REFERENCES.md](../REFERENCES.md) — *Messaging, events, and NATS*  
