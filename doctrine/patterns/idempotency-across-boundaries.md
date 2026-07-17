# Idempotency Across Boundaries

Defines safe-retry strategies for **HTTP**, **messages**, **infrastructure**, and data work. The retry or redelivery boundary is the control surface; the underlying domain transition does not have to be idempotent. Complements [api-boundaries-and-security.md](../principles/api-boundaries-and-security.md), [event-contracts.md](../principles/event-contracts.md), and [state-machines-and-workflows.md](../principles/state-machines-and-workflows.md).

---

## 1. Retry Boundary And Domain Effect

- An externally retried or redelivered mutating command **SHOULD** declare how duplicate, ambiguous, and partially completed attempts are handled.
- Idempotency concerns the **intended effect** of applying the same command more than once. Request logs, metrics, and other incidental effects may still differ between attempts.
- When the domain action is inherently non-idempotent and a duplicate could cause material harm, the controlling boundary **MUST** prevent or detect duplicate business effects. Suitable mechanisms include an idempotency key, a business-unique transaction identifier, a conditional state transition, or a durable record of the first outcome.
- Do not infer business-level exactly-once behaviour from a transport or broker claim. State the duplicate and recovery invariant that the application actually enforces.

**Why:** Retrying a command is a delivery concern; incrementing a counter, appending a ledger entry, allocating scarce inventory, or initiating an external action may remain intentionally non-idempotent inside that boundary. HTTP defines idempotency in terms of the requested intended effect, not every server-side side effect.

---

## 2. HTTP Mutations

- Accept **idempotency keys** (header or body) for payments, provisioning, and other **high-cost** duplicates; **persist** key → outcome mapping for the documented **retry window**.
- Use **PUT** and **DELETE** semantics where the intended effect follows their idempotent HTTP semantics. Document **POST** retry behaviour explicitly; the method name alone neither supplies nor prohibits an application-level deduplication strategy.

**Why:** [RFC 9110 §9.2.2](https://www.rfc-editor.org/rfc/rfc9110.html#name-idempotent-methods) defines PUT, DELETE, and safe methods as idempotent and cautions against automatically retrying a non-idempotent method without knowledge or detection of the original effect. Idempotency keys are one implementation pattern for ambiguous POST outcomes.

---

## 3. Messages And Events

- Where **at-least-once** delivery applies, use a stable event identity as a deduplication key. For CloudEvents, the identity is the **`source` + `id` pair**, not `id` alone; for another envelope or broker, document the equivalent scope.
- **Outbox** pattern: commit business state and **outbound** event in one transaction; publisher **retries** from outbox—consumers still dedupe.
- Apply deduplication before an irreversible or non-idempotent consumer effect, and retain the first disposition for the redelivery window when the effect is material.

**Why:** Enterprise Integration Patterns — **Idempotent Receiver**: https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html

---

## 4. Infrastructure And Data

- **Plan → apply** with reviewed diffs; **state** backends with locking where concurrent applies occur.
- **Migrations** — prefer forward-only steps that tolerate **re-run** or **no-op** where feasible. Otherwise define a checkpoint, restart, repair, or forward-recovery procedure before execution; do not label a destructive transition idempotent merely because the migration runner can be invoked again.

**Why:** Aligns retry safety with the recovery and migration obligations in [data-and-migrations.md](../principles/data-and-migrations.md).

---

## References

- *Enterprise Integration Patterns* — **Idempotent Receiver**: https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html  
- IETF **RFC 9110 §9.2.2** — idempotent HTTP method semantics: https://www.rfc-editor.org/rfc/rfc9110.html#name-idempotent-methods
- CloudEvents v1.0.2 core specification — uniqueness of the `source` + `id` pair: https://github.com/cloudevents/spec/blob/ce%40v1.0.2/cloudevents/spec.md#id-1
- Stripe API — **Idempotency**: https://stripe.com/docs/api/idempotent_requests  
- Martin Fowler — **ParallelChange** (related to safe repeated deploys): https://martinfowler.com/bliki/ParallelChange.html  
