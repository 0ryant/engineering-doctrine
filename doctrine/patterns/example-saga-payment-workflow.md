# Example: Payment Saga Across Services (Fiction)

**Illustrative only** — not a product standard. Shows how [state-machines-and-workflows.md](../principles/state-machines-and-workflows.md) §5 (**sagas**, **compensation**, **timeouts**) applies when **no** single database transaction spans **payment**, **inventory**, and **notification** services. For **transport** detail with Kafka or NATS, see [../tooling/kafka-and-cloudevents.md](../tooling/kafka-and-cloudevents.md) or [../tooling/nats-jetstream.md](../tooling/nats-jetstream.md).

---

## 1. Behavioural Model (Excerpt)

| State | Meaning | Next states |
| --- | --- | --- |
| `initiated` | Payment id reserved; no money captured | → `funded`, `failed` |
| `funded` | Ledger shows capture | → `inventory_reserved`, `compensating` |
| `inventory_reserved` | Stock held for order | → `completed`, `compensating` |
| `completed` | Customer notified; terminal | — |
| `compensating` | Undo prior steps in order | → `failed` |
| `failed` | Terminal; user sees decline | — |

**Timeout:** if `funded` but inventory does not reach `inventory_reserved` within **T** (for example **30 s**), transition to **`compensating`** (release capture, release any soft hold).

---

## 2. Forward Steps And Compensation

| Step | Forward action | On failure / saga abort |
| --- | --- | --- |
| 1 | **Authorize** or **capture** payment (idempotent on `payment_id`) | Void / refund if capture succeeded |
| 2 | **Reserve** inventory (idempotent on `reservation_id`) | Release reservation |
| 3 | **Emit** `order.completed` (or notify) | Best-effort **cancel** email if already sent |

Each step uses an **idempotency key** shared with the remote system so **retries** do not double-charge or double-reserve—see [idempotency-across-boundaries.md](idempotency-across-boundaries.md).

---

## 3. Events (CloudEvents Shapes — Examples)

| Transition committed | `type` (example) | `subject` |
| --- | --- | --- |
| → `funded` | `com.example.payment.captured.v1` | order id |
| → `inventory_reserved` | `com.example.inventory.reserved.v1` | order id |
| → `completed` | `com.example.order.completed.v1` | order id |
| → `compensating` | `com.example.saga.compensating.v1` | order id |

Payloads are **versioned** JSON Schema; envelope per [event-contracts.md](../principles/event-contracts.md).

---

## 4. Human-In-The-Loop (Optional)

If **fraud** holds the payment: state **`awaiting_review`** with **SLA** (for example **24 h**) before auto-decline or escalate; **same** approval token must not **complete** the saga twice (idempotent approval handler).

---

## 5. What This Example Does Not Decide

- **Orchestration** vs **choreography** (single saga coordinator vs event collaboration)—either works if **state** and **compensation** are explicit.
- **Message broker** choice—principle-level rules live in [message-channel-operations.md](message-channel-operations.md).

---

## References

- Martin Fowler — **Saga**: https://martinfowler.com/bliki/Saga.html  
- [reliability-slo-incidents.md](../principles/reliability-slo-incidents.md) — operational learning from failure  
