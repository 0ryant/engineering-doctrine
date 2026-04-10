# Event And Message Contracts

These rules govern asynchronous integration: queues, topics, webhooks, event buses, and any other **message-shaped** boundary. They complement [build.md](build.md) and the umbrella **Contracts First** rule in `ENGINEERING.md`.

Synchronous HTTP APIs remain OpenAPI-first; **events use an explicit envelope contract plus a versioned payload contract.**

---

## 1. Events Are First-Class Contracts

- Every published event type has a **named contract** before producers ship: schema or equivalent for the payload, plus documented delivery semantics (ordering, retries, idempotency expectations).
- **Version explicitly** — additive changes preferred; breaking changes require a new event type or version suffix and a migration plan.
- **Examples and fixtures** live next to schemas; CI validates examples against schemas where the toolchain allows it.
- Contract violations at boundaries are **failures**, not best-effort logs only, unless a documented degradation path exists.

---

## 2. Standard Envelope: CloudEvents

- Use **[CloudEvents](https://github.com/cloudevents/spec)** as the **standard envelope** for event messages across services and transports, unless a platform makes that impossible and the exception is recorded.
- The envelope carries interoperability metadata: **id**, **source**, **type**, **time**, and optional **subject**, **dataschema**, and extensions as needed.
- **Payload data** remains a separate contract: define it with JSON Schema, Protobuf, or another explicit schema language; do not rely on undocumented JSON blobs.

---

## 3. Event Types And Payloads

- **`type`** (CloudEvents `type`) identifies the **semantic event** (for example `com.example.order.created.v1`). It must be **stable** and **unique** per distinct payload shape consumers rely on.
- Prefer **one schema per `type`** for a given major version; avoid overloading one `type` with incompatible payload shapes.
- **`source`** identifies the **logical producer** (URI or URN per team convention); it must be stable across deployments of the same system.
- **`id`** is unique per event instance; consumers use it for **deduplication** where delivery is at-least-once.

---

## 4. Semantics Beyond The Schema

- Document **ordering** guarantees (per partition key, per entity, or none).
- Document **delivery** semantics (at-most-once, at-least-once, effectively-once patterns) and **consumer idempotency** requirements.
- **Sensitive fields** — never put secrets in event payloads; reference correlation IDs and fetch authoritative data when needed.
- **Workflow state** — when behaviour is modelled as states and transitions, document the model and map **committed** transitions to stable event `type`s and payloads; see [state-machines-and-workflows.md](state-machines-and-workflows.md).
- **Scheduled and batch events** — when a job emits many events or fires on a schedule, document **batch boundaries**, **partial failure** semantics, and **idempotency** across replays (the same logical “run” may be retried).
- **HTTP ingress (webhooks)** — treat inbound HTTP callbacks as **untrusted** until verified: signature or mTLS, **timestamp/replay** window, **idempotency** for mutating handlers. Pattern: [../patterns/webhook-ingress-security.md](../patterns/webhook-ingress-security.md).

---

## 5. Tooling Defaults

Current CloudEvents version, bindings, and validation expectations live in [../tooling/cloudevents.md](../tooling/cloudevents.md). Update that file when the organisation upgrades spec version or default serialization.

---

## 6. Operational Handling (Queues And Buses)

Contract and schema correctness are not enough: define **dead-letter / poison** handling, **replay** rules, and **backlog observability** for production message paths. Pattern: [../patterns/message-channel-operations.md](../patterns/message-channel-operations.md).

---

## 7. When This Principle Changes

Change this document only when the operating model for cross-service events changes — for example, if the organisation standardises on a different envelope **and** migrates all producers and consumers with a recorded cutover.

---

## References

- CloudEvents specification: https://github.com/cloudevents/spec  
- CloudEvents **HTTP Protocol Binding** (webhooks, gateways): https://github.com/cloudevents/spec/blob/main/cloudevents/bindings/http-protocol-binding.md  
- OWASP **API Security** project (webhooks align with API-style risks such as authz and resource consumption): https://owasp.org/www-project-api-security/  
- Stripe — **Sign webhooks** (illustrative industry practice for HMAC verification): https://docs.stripe.com/webhooks/signatures  
