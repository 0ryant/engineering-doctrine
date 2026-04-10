# Glossary

Short definitions for terms used across this doctrine. **Normative detail** lives in linked principles, patterns, and external specs—this page is for **orientation** only.

See also: **[tldr-principles-and-mvp.md](tldr-principles-and-mvp.md)** (spine + MVP), **[REFERENCES.md](REFERENCES.md)** (external authorities).

---

## A

**Acceptance (of messages)** — Consumer tells the broker it finished processing; behaviour (single vs cumulative ack, redelivery) is **broker-specific**. See [message-channel-operations.md](patterns/message-channel-operations.md).

**ADR (Architecture Decision Record)** — In-repo note: context, decision, consequences; superseded decisions stay linked. See [documentation-knowledge.md](principles/documentation-knowledge.md).

**Artefact / artifact** — Versioned output of a build (binary, image, package, chart). This library often uses **artefact** (British spelling); tools and US docs may say **artifact**. See [build.md](principles/build.md).

**At-least-once delivery** — A message or request may arrive **more than once**; handlers must be **idempotent** or **dedupe** explicitly. See [event-contracts.md](principles/event-contracts.md), [idempotency-across-boundaries.md](patterns/idempotency-across-boundaries.md).

**Audit log** — Append-oriented record of **who** did **what** to **which** resource, for security and compliance—not the same as product analytics. See [audit-logging.md](principles/audit-logging.md).

---

## B

**Blameless postmortem** — Incident review focused on **system** and **process** fixes, not individual fault; actions tracked to completion. See [reliability-slo-incidents.md](principles/reliability-slo-incidents.md), [collaboration.md](principles/collaboration.md).

**BOLA / BOPLA** — *Broken object (and property) level authorisation*: access control bugs where callers reach others’ objects or fields. Top theme in OWASP API Top 10. See [api-boundaries-and-security.md](principles/api-boundaries-and-security.md).

**Build surface** — Named entrypoint in the delivery model (quality gate, build/publish, deploy, verify, etc.). See [build.md](principles/build.md), [build-surface-model.md](patterns/build-surface-model.md).

---

## C

**Canary / gradual rollout** — Release to a **small** slice first, expand if healthy; limits blast radius. See [collaboration.md](principles/collaboration.md).

**Chaos engineering** — **Controlled** fault injection and game days to validate resilience **before** production surprises. See [reliability-slo-incidents.md](principles/reliability-slo-incidents.md).

**CloudEvents** — Vendor-neutral **envelope** for events (`id`, `source`, `type`, `time`, …) over HTTP, Kafka, NATS, etc.; **payload** still needs its own schema. See [event-contracts.md](principles/event-contracts.md), [tooling/cloudevents.md](tooling/cloudevents.md).

**CODEOWNERS** — Git host file mapping **paths** to **required reviewers** (teams or individuals). See [collaboration.md](principles/collaboration.md), [naming-and-repo-layout.md](principles/naming-and-repo-layout.md).

**Contract** — Explicit, versioned **shape** and rules at a boundary (schema, OpenAPI, proto, migration contract). Violations are **build or runtime failures** per policy—not informal JSON. See [ENGINEERING.md](../ENGINEERING.md) §1.

**CORS / CSP** — *Cross-Origin Resource Sharing* and *Content Security Policy*: browser-facing controls for APIs and pages. See [api-boundaries-and-security.md](principles/api-boundaries-and-security.md).

---

## D

**Dead letter queue (DLQ)** — Destination for messages that **failed** processing after policy limits; avoids infinite retry loops. See [message-channel-operations.md](patterns/message-channel-operations.md).

**Deployable unit** — Thing you **ship or operate** with its own lifecycle (app, infra module, automation package, etc.); often maps to **separate** deploy surfaces. See [build.md](principles/build.md).

**DORA (Four Keys)** — *Deployment frequency*, *lead time for changes*, *change failure rate*, *time to restore*—delivery **outcomes**, not lines of code. See [measurement-and-dora.md](principles/measurement-and-dora.md).

**DPIA / PIA** — *Data protection* or *privacy* **impact assessment** for high-risk processing. See [privacy-and-data-governance.md](principles/privacy-and-data-governance.md).

---

## E

**Error budget** — Allowed **unreliability** derived from an SLO; spending it signals **slow down or invest** in reliability. See [reliability-slo-incidents.md](principles/reliability-slo-incidents.md).

**Estate** — In this repo: a **specific** organisation, cloud, or region whose **named** product choices live under `tooling/estates/`—not global law. See [timeless-principles-and-tooling.md](principles/timeless-principles-and-tooling.md).

**Exactly-once (illusion)** — True end-to-end **exactly-once side effects** are rare; most systems are **at-least-once** plus **idempotent** design. See [message-channel-operations.md](patterns/message-channel-operations.md).

---

## F

**Feature flag** — Toggle for **incomplete** or **risky** behaviour; safe defaults and **removal** discipline required. See [collaboration.md](principles/collaboration.md).

**FinOps** — Cost **visibility**, allocation, and governance for cloud spend. See [performance-and-cost.md](principles/performance-and-cost.md).

---

## G

**Golden path** — Org’s **blessed** default way to build/run a service (often part of an internal platform—not fully specified in portable doctrine).

---

## H

**Hermetic build** — Build with **declared** inputs only (pinned toolchains, lockfiles) so outputs are **reproducible** and auditable. See [build.md](principles/build.md) §14.

**Hexagonal / ports and adapters** — Core domain isolated from I/O via **interfaces**; adapters implement DB, HTTP, queues. See [modularity-and-ports-adapters.md](principles/modularity-and-ports-adapters.md).

---

## I

**Idempotency** — Repeating an operation with the **same intent** does not **compound** harm (safe retries, dedupe keys). See [ENGINEERING.md](../ENGINEERING.md) §4, [idempotency-across-boundaries.md](patterns/idempotency-across-boundaries.md).

**IDOR** — *Insecure direct object reference*—often overlaps **BOLA**. See [api-boundaries-and-security.md](principles/api-boundaries-and-security.md).

---

## L

**LTS (long-term support) branch** — Exceptional **parallel** line for extended patch support; document EOL. See [trunk-workflow.md](patterns/trunk-workflow.md).

---

## M

**Merge queue** — Serialises merges to `main` by testing the **merged** result; reduces “green branch, red main.” See [collaboration.md](principles/collaboration.md), [trunk-workflow.md](patterns/trunk-workflow.md).

**Minimum viable doctrine (MVP)** — Smallest practice set that makes **further** adoption safe; team-specific one-pager in [minimum-viable-doctrine.template.md](tooling/estates/minimum-viable-doctrine.template.md). See [tldr-principles-and-mvp.md](tldr-principles-and-mvp.md).

**mTLS** — *Mutual TLS*: both parties present certificates; common for **service-to-service** identity. See [api-boundaries-and-security.md](principles/api-boundaries-and-security.md), [zero-trust-and-workload-identity.md](principles/zero-trust-and-workload-identity.md).

**Mutation testing** — Changes code under test to see if tests **fail**; surviving mutants imply weak assertions. See [testing-strategy.md](principles/testing-strategy.md).

---

## O

**Observability** — Logs, metrics, traces (and **correlation**) sufficient to debug **unknown-unknown** failures. See [observability.md](principles/observability.md).

**OIDC** — *OpenID Connect*: identity layer on OAuth 2.0; common for **human** and sometimes **workload** flows. See [zero-trust-and-workload-identity.md](principles/zero-trust-and-workload-identity.md).

**OpenTelemetry (OTel)** — Vendor-neutral telemetry APIs and **OTLP** export. See [interoperability-and-standards.md](principles/interoperability-and-standards.md), [tooling/observability.md](tooling/observability.md).

**Outbox** — Pattern to **atomically** persist business state and an **outbound** message descriptor so publishers don’t double-send under crash. Related to idempotency; see [idempotency-across-boundaries.md](patterns/idempotency-across-boundaries.md).

---

## P

**PII** — *Personally identifiable information*; minimise, segregate from analytics, define retention. See [privacy-and-data-governance.md](principles/privacy-and-data-governance.md).

**Principle** — In this repo: **durable intent** under `principles/`—**not** tied to one vendor SKU. See [timeless-principles-and-tooling.md](principles/timeless-principles-and-tooling.md).

**Problem Details** — `application/problem+json` (RFC 9457) for **machine-readable** HTTP errors. See [errors-and-failure-modes.md](principles/errors-and-failure-modes.md), [api-boundaries-and-security.md](principles/api-boundaries-and-security.md).

**Promotion** — Moving a **built** artefact through environments **without** rebuilding for each hop (where the platform allows). See [build.md](principles/build.md).

**Publishable unit** — Thing consumers pin versions on (package, image, API product, CLI); gets its **own** SemVer line. See [semantic-versioning.md](principles/semantic-versioning.md).

---

## Q

**Quality gate** — Mandatory checks (fmt, lint, test, contracts, scans) before merge or tag. See [build.md](principles/build.md).

---

## R

**Replay** — Re-deliver or re-process messages from history or DLQ **deliberately**; needs **idempotency** and scope. See [message-channel-operations.md](patterns/message-channel-operations.md).

**RFC (design)** — *Request for comments*: **pre-decision** exploration; outcomes land in ADRs when decided. See [documentation-knowledge.md](principles/documentation-knowledge.md).

**RPO / RTO** — *Recovery point* / *time* **objectives**: how much data loss and downtime are acceptable in DR. See [data-and-migrations.md](principles/data-and-migrations.md).

**Runbook** — Step-by-step **operator** procedure (deploy, rollback, common failures). See [documentation-knowledge.md](principles/documentation-knowledge.md).

---

## S

**Saga** — Multi-step **distributed** workflow with **forward** recovery or **compensating** actions; not one ACID transaction across services. See [state-machines-and-workflows.md](principles/state-machines-and-workflows.md).

**SBOM** — *Software bill of materials*: inventory of components in a build (often SPDX/CycloneDX). See [dependencies-supply-chain.md](principles/dependencies-supply-chain.md).

**SCA** — *Software composition analysis*: dependency + vuln + sometimes **licence** scanning. See [dependencies-supply-chain.md](principles/dependencies-supply-chain.md).

**SDL** — *Secure development lifecycle*: design review, implementation norms, **vulnerability response**. See [secure-development-lifecycle.md](principles/secure-development-lifecycle.md).

**SemVer** — *Semantic versioning* `MAJOR.MINOR.PATCH` per **publishable unit**. See [semantic-versioning.md](principles/semantic-versioning.md).

**Shift left** — Move security, quality, and validation **earlier** in the lifecycle (design, CI), not only pre-release. See [ENGINEERING.md](../ENGINEERING.md) §5.

**SLA** — *Service level **agreement***: **contractual** promise to a customer (often stricter or broader than internal SLOs).

**SLI** — *Service level **indicator***: measured metric backing an SLO (e.g. successful requests ÷ total).

**SLO** — *Service level **objective***: internal target for reliability/latency derived from user needs; pairs with **error budget**. See [reliability-slo-incidents.md](principles/reliability-slo-incidents.md).

**SLSA** — *Supply-chain levels for software artifacts*: framework for **build integrity** and **provenance**. See [build.md](principles/build.md) §14, [dependencies-supply-chain.md](principles/dependencies-supply-chain.md).

**SPACE** — Framework for **developer experience** (satisfaction, performance, activity, collaboration, flow)—complements DORA. See [measurement-and-dora.md](principles/measurement-and-dora.md).

**SPIFFE / SPIRE** — *Secure production identity framework for everyone* and common implementation: **workload identities** and SVIDs. See [zero-trust-and-workload-identity.md](principles/zero-trust-and-workload-identity.md).

**SSDF** — NIST *Secure Software Development Framework* (SP 800-218): practices grouped **Prepare, Protect, Produce, Respond**. See [timeless-principles-and-tooling.md](principles/timeless-principles-and-tooling.md) §6.

**STRIDE** — *Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege*—threat-model **prompts**. See [threat-modeling-stride-lite.md](principles/threat-modeling-stride-lite.md).

---

## T

**Telemetry (three pillars)** — **Metrics**, **logs**, **traces**—each answers different questions under failure. See [observability.md](principles/observability.md).

**Threat modeling** — Structured identification of threats at **trust boundaries** (often STRIDE). See [threat-modeling-stride-lite.md](principles/threat-modeling-stride-lite.md).

**Toil** — Manual, repetitive operational work that does not **improve** the system long-term; budget its reduction. See [reliability-slo-incidents.md](principles/reliability-slo-incidents.md).

**Tooling** — In this repo: **illustrative** stacks under `tooling/` and `tooling/estates/`—swappable if **surface contracts** stay stable. See [timeless-principles-and-tooling.md](principles/timeless-principles-and-tooling.md).

**Trunk-based development** — Integrate frequently to a **single** default branch (`main`); short-lived topic branches. See [collaboration.md](principles/collaboration.md).

---

## W

**Webhook** — HTTP **callback** from a provider; verify signatures, bound replay windows, **idempotent** handlers. See [webhook-ingress-security.md](patterns/webhook-ingress-security.md).

**Workload identity** — Runtime identity for **services** (tokens, certs, SPIFFE) distinct from **human** logins. See [zero-trust-and-workload-identity.md](principles/zero-trust-and-workload-identity.md).

---

## Z

**Zero Trust** — No implicit trust from **network location** alone; verify **per request** with least privilege. See [ENGINEERING.md](../ENGINEERING.md) §8, [zero-trust-and-workload-identity.md](principles/zero-trust-and-workload-identity.md).

---

## Maintenance

Add or tighten entries when a term appears in **multiple** principle files without a single definition. Prefer **links** over long prose here.
