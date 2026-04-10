# Idempotency Across Boundaries

Unifies **idempotent** design for **HTTP**, **messages**, and **infrastructure** so retries and replays are safe. Complements umbrella **Idempotency** in `ENGINEERING.md`, [api-boundaries-and-security.md](../principles/api-boundaries-and-security.md), [event-contracts.md](../principles/event-contracts.md), and [state-machines-and-workflows.md](../principles/state-machines-and-workflows.md).

---

## 1. HTTP Mutations

- Accept **idempotency keys** (header or body) for payments, provisioning, and other **high-cost** duplicates; **persist** key → outcome mapping for the **retry window**.
- Use **PUT** and **DELETE** semantics where they truly are idempotent; document **POST** behaviour explicitly when not.

**Why:** Stripe and other APIs popularised idempotency keys; Open Banking and payment rails expect them.

---

## 2. Messages And Events

- Treat **CloudEvents `id`** (or broker message id) as **dedup** key where **at-least-once** delivery applies.
- **Outbox** pattern: commit business state and **outbound** event in one transaction; publisher **retries** from outbox—consumers still dedupe.

**Why:** Enterprise Integration Patterns — **Idempotent Receiver**: https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html

---

## 3. Infrastructure And Data

- **Plan → apply** with reviewed diffs; **state** backends with locking where concurrent applies occur.
- **Migrations** — forward-only steps that tolerate **re-run** or **no-op** where platforms allow (document exceptions).

**Why:** Aligns with `ENGINEERING.md` idempotency bullets and [data-and-migrations.md](../principles/data-and-migrations.md).

---

## References

- *Enterprise Integration Patterns* — **Idempotent Receiver**: https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html  
- Stripe API — **Idempotency**: https://stripe.com/docs/api/idempotent_requests  
- Martin Fowler — **ParallelChange** (related to safe repeated deploys): https://martinfowler.com/bliki/ParallelChange.html  
