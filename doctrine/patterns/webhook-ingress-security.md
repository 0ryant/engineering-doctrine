# Webhook Ingress Security

Companion to [principles/event-contracts.md](../principles/event-contracts.md) for **HTTP callbacks** from third parties (payments, Git hosting, SaaS integrations). **Contracts** define payload shape; **this pattern** covers **authentication**, **integrity**, and **replay** resistance.

---

## 1. Authenticate The Sender

- **HMAC** or **asymmetric** signatures over a **canonical** representation of the payload (raw body, not re-serialised JSON) with a **shared secret** or **public key** per integration.
- **Rotate** signing secrets; support **overlapping** verification windows during rotation.

**Why:** OWASP **API Security** guidance and common vendor patterns stress **authenticity** and **integrity** for inbound callbacks; treat unsigned webhooks as **spoofable**. See OWASP API Security project: https://owasp.org/www-project-api-security/

---

## 2. Timestamp And Replay Window

- Require a **timestamp** or **monotonic** event id from the sender; **reject** events outside a **short** clock-skew window (for example 5 minutes) unless using idempotent dedup only.
- Store **processed** delivery ids (`ce_id`, provider id) for **deduplication**—see [message-channel-operations.md](message-channel-operations.md).

**Why:** Signed payloads without **freshness** checks allow **replay** attacks.

---

## 3. Idempotency And Ordering

- Handlers must tolerate **duplicate** deliveries; document **at-least-once** semantics.
- If ordering matters, define **per-entity** serialisation or **version** fields in the payload.

**Why:** Providers **retry** on timeouts; your handler will see duplicates.

---

## 4. Ingress Hardening

- **TLS** only; pin **allowlisted** source IPs only as **defence in depth** (not sole auth).
- **Rate limit** and **size limit** ingress endpoints—align with [api-boundaries-and-security.md](../principles/api-boundaries-and-security.md).

---

## References

- OWASP — **API Security** project (webhook endpoints share many API risks): https://owasp.org/www-project-api-security/  
- Stripe — **Webhook signatures** (industry example of HMAC + timestamp): https://docs.stripe.com/webhooks/signatures  
- CloudEvents — HTTP **binding** when mapping provider payloads to envelopes: https://github.com/cloudevents/spec/blob/main/cloudevents/bindings/http-protocol-binding.md  
