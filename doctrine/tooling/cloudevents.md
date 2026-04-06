# CloudEvents Tooling

This is the current default for implementing [../principles/event-contracts.md](../principles/event-contracts.md): **CloudEvents** as the standard event envelope for asynchronous integration.

These choices are defaults. Replace them when a platform mandates a different wire format, but **preserve** explicit payload schemas and versioned event types.

---

## Specification Baseline

| Item | Current default | Notes |
| --- | --- | --- |
| **Spec** | [CloudEvents](https://github.com/cloudevents/spec) **1.0** | Track patch releases; breaking spec upgrades require org-wide migration planning. |
| **Structured mode (JSON)** | Default for HTTP and many brokers | Single JSON object with `specversion`, `id`, `source`, `type`, optional `time`, `data`, `dataschema`, `subject`. |
| **Binary mode** | Use when the broker separates metadata headers from body | Map CloudEvents attributes to protocol headers per [HTTP Protocol Binding](https://github.com/cloudevents/spec/blob/main/cloudevents/bindings/http-protocol-binding.md) or the binding for your broker. |
| **Payload (`data`)** | JSON with **JSON Schema** for the payload document | Other encodings (Protobuf, Avro) are valid when the repo documents `datacontenttype` and schema location. |

---

## Required Attributes (Minimum Interop)

Producers should set at minimum:

- `specversion`: `1.0`
- `id`: unique string for this occurrence (UUID recommended)
- `source`: URI-reference identifying the logical producer
- `type`: dotted reverse-DNS or equivalent stable identifier including **version** (for example `com.example.service.entity.verb.v1`)

Also set when applicable:

- `time`: RFC 3339 timestamp in UTC
- `subject`: fine-grained routing or partitioning key (for example entity id)
- `dataschema`: URI for the JSON Schema (or other schema) of `data`

---

## Bindings And Transports

| Transport | Default approach |
| --- | --- |
| **HTTP** (webhooks, gateways) | `Content-Type: application/cloudevents+json` for structured; or binary mode with `ce-*` headers per HTTP binding |
| **Kafka / NATS / AMQP / etc.** | Use the **official CloudEvents binding** for that protocol where available; otherwise structured JSON in the message value with documented header mapping |
| **Cloud vendor event grids** | Map vendor envelopes **to** CloudEvents at the boundary if the native format differs; keep conversion in one thin adapter layer |

---

## Validation

- Validate **envelope** shape (required attributes present and well-formed) in tests and at ingress where performance allows.
- Validate **payload** against the registered JSON Schema (or Protobuf decode) in the consumer’s boundary layer or shared SDK.
- Contract tests between producer and consumer fixtures catch drift before deploy.

---

## SDKs And Libraries

Prefer **maintained CloudEvents SDKs** in the implementation language over ad-hoc JSON construction. If the stack has no SDK, centralise envelope creation in one module and test it.

---

## Versioning This Doc

Bump the **spec baseline** table when the organisation adopts a new CloudEvents minor/patch line or changes the default binding. Keep [../principles/event-contracts.md](../principles/event-contracts.md) aligned only if the **operating model** changes, not on every SDK upgrade.
