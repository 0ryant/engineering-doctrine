# Owner Gap Rules From Implementation Batch 2

Date and source access date: 2026-11-18. Repository basis: `69908f8` and the companion change.
Status: research basis for [ADR 0052](../../docs/adr/0052-close-owner-gaps-from-implementation-batch-2.md) (accepted 2026-11-18). Model research and model review; no independent human or domain review.

## Question

The [batch 2 owner audit](research-impl-backlog-batch-2-composition-2026-11.md#resolution-in-this-change) found one conflict and four missing rules that an editorial pass could not settle. The maintainer chose to resolve the conflict in favour of documented bot-only paths and to draft rules for the four gaps. What does external practice support for each, and at what strength?

## Source Ledger

Classes follow [Source Authority And Evidence Grading](../patterns/source-authority-and-evidence-grading.md) §2. Every primary page was read by the lead author on the access date (V1). No archive copies were captured.

| Source | Class and scope | Supports | Does not establish |
| --- | --- | --- | --- |
| [Apache Kafka 4.4 design: message delivery semantics](https://kafka.apache.org/44/design/design/) | S5, product-scoped; the semantics it describes are general | Saving the consumer position before processing gives at-most-once delivery on failure; processing first and then saving gives at-least-once | A rule for other brokers; acknowledgement mechanics differ per channel |
| [Google SRE Workbook, ch. 16: Canarying Releases](https://sre.google/workbook/canarying-releases/) | S4, edited book | Compare the canary with a control on defined signals before proceeding; an unhealthy canary means pause and roll back, or bring in a human; the reaction can be automated | Who decides a rollback; the chapter does not name a role |
| [Google SRE Workbook, ch. 4: Monitoring](https://sre.google/workbook/monitoring/) | S4, edited book | Monitoring and alerting code should meet the same testing standards as other code; rarely firing alerts need validation with known signals; monitoring configuration benefits from review as code | A specific post-deployment verification procedure |
| [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) | S4, reviewed guidance | Session identifiers, access tokens, credentials, keys, payment data, and sensitive personal data should be removed, masked, sanitised, hashed, or encrypted; de-identify personal data when identity is not needed | Retention periods, or a legal basis for any processing |
| [Renovate: automerge](https://docs.renovatebot.com/key-concepts/automerge/) | S5, product-scoped | Automerge waits for passing required checks; it is recommended for updates a reviewer would merge anyway, with lockfile maintenance and development dependencies as the lowest-risk classes and care for pre-1.0 packages | That any particular class is low risk in a given estate |

Internal precedents, not external grounding: feature flag governance §§4.3–4.4 (metric gates and bounded automated reversion for flags), idempotency §3 (deduplication before effects), privacy §§1–2 (minimisation and retention), and build §5 (verification closes deployment).

## Synthesis

1. **Bot updates.** The dependencies principle said "with human review", while collaboration §2 allows documented bot-only paths and the dependencies severity table itself cites a weekly or fortnightly bot merge. Tool guidance supports automerge only after required checks pass and for update classes a reviewer would accept anyway. An estate-classified low-risk path, gated by required checks, resolves the conflict without removing human review elsewhere.
2. **Acknowledgement order.** The delivery semantics follow from when the position is saved, not from the broker brand. Acknowledging after the effect is durable gives at-least-once delivery, which the library's deduplication rules already assume. Acknowledging first is legitimate only where losing the effect is acceptable, so the choice should be explicit.
3. **Deployment canaries and rollback.** The flag pattern already gates exposure on recorded metrics and bounds automated reversion. The SRE workbook applies the same logic to deployment canaries. Deployment rollback needs the same shape, and a named decider so on-call staff can act without waiting.
4. **Telemetry verification.** Build §5 says deployment is incomplete until verification proves health, but nothing says verification covers the telemetry that later detects failure. The monitoring chapter treats alerting as testable code. A SHOULD-level rule fits the evidence.
5. **Identifier minimisation.** Observability §2 encourages business identifiers on spans and logs without a minimisation bound, and the privacy rule that follows data into logs applies only to controlled-data profiles. Privacy §1 and the logging guidance support a general bound on telemetry content.

## Decision Input

| Decision | Owner | Strength proposed |
| --- | --- | --- |
| D1 bot-only update path | [Dependencies](../principles/dependencies-supply-chain.md) §2 | MAY, with required checks and an estate-defined low-risk class |
| D2 acknowledgement order | [Message channel operations](../patterns/message-channel-operations.md) | SHOULD for at-least-once consumers; MUST where losing the effect would cause material harm |
| D3 deployment canaries and rollback | [Collaboration](../principles/collaboration.md) §8.1 | SHOULD for recorded canary signals; MAY for bounded automated rollback; named decider |
| D4 telemetry verification | [Observability](../principles/observability.md) §8 | SHOULD for production services on material paths |
| D5 identifier minimisation | Observability §2, grounded in privacy §§1–2 | SHOULD |

Admission: **C2 with explicit risk asymmetry** for D2–D5. Sources are edited books, reviewed guidance, and product-scoped documentation that describe general behaviour; none is a binding standard. D1 is an internal-consistency resolution supported by tool guidance.

## Residual Risk

The rules are drafted by a model from a small set of sources. The canary and monitoring guidance comes from one provider's practice book. "Low risk" and "material harm" remain estate judgements. Acknowledgement mechanics vary by channel, so tooling has to map the rule to each product. No independent review is recorded.
