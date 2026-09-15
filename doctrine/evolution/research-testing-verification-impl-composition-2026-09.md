# Research Note: Testing And Verification Implementation Composition

Date: 2026-09-14

## Question

How should the doctrine help engineers place tests and verification across application CI, packaging, deployment, infrastructure delivery, and scheduled assurance without creating a second testing authority?

## Evidence Boundary

This note records repository synthesis for an implementation reference. It introduces no testing control. The canonical requirements and their external grounding remain in the linked principles and owning patterns.

The supplied ZIP was treated as proposal material. Its Markdown was inspected; no bundled instruction was executed. The proposal was compared with the current repository, ADR 0048, and the owners named below before adaptation.

## Finding: A Flat Taxonomy Is Insufficient

Testing vocabulary mixes independent dimensions:

- scope, such as unit, component, integration, system, and end-to-end;
- purpose, such as regression, security, performance, resilience, migration, and recovery;
- technique, such as snapshot, property-based, fuzz, mutation, fault injection, synthetic, and canary; and
- timing, such as pre-merge, packaging, deployment, post-deploy, production, and scheduled assurance.

The same check can occupy several categories. Treating all names as siblings makes an impressive catalogue but does not answer where evidence belongs. Delivery-surface placement is the useful engineer model:

```mermaid
flowchart LR
    A["Name the claim"] --> B["Find the earliest credible surface"]
    B --> C["Run cheaper evidence first"]
    C --> D["Use deployed or scheduled evidence when reality is required"]
    D --> E["Bind the result to candidate, environment, and policy"]
```

This is a direct composition of the evidence-first rule in `principles/testing-strategy.md` and the explicit delivery surfaces in `principles/build.md`.

## Owner Audit

The reference composes existing owners rather than creating new requirements:

| Surface | Existing owners |
| --- | --- |
| Test portfolio and techniques | `principles/testing-strategy.md` |
| Quality, package, deploy, verify, and evidence surfaces | `principles/build.md`, `principles/collaboration.md`, `principles/merge-path-evidence-and-pipeline-integrity.md` |
| API, event, retry, and duplicate behaviour | `principles/api-boundaries-and-security.md`, `principles/event-contracts.md`, `principles/errors-and-failure-modes.md`, `patterns/idempotency-across-boundaries.md`, `patterns/message-channel-operations.md` |
| Migration, recovery, and failover | `principles/data-and-migrations.md`, `principles/reliability-slo-incidents.md`, `patterns/chaos-engineering-and-game-days.md` |
| Runtime evidence | `principles/observability.md`, `principles/zero-trust-and-workload-identity.md` |
| Security and supply chain | `principles/secure-development-lifecycle.md`, `principles/dependencies-supply-chain.md` |
| Performance and capacity | `principles/performance-and-cost.md` |

## Infrastructure Distinction

Application tests do not map directly onto declarative infrastructure. Static validation and a plan or what-if can show structure and intended change. An apply success shows that a control plane accepted operations. Neither proves effective connectivity, authority, policy, telemetry, or workload behaviour.

The reference therefore separates pre-apply evidence from post-apply resource, network, identity, policy, and representative-workload verification. This follows `principles/build.md` (“verify after deployment”), `patterns/idempotency-across-boundaries.md` (reviewed plan/apply and locking), and the identity, observability, reliability, and migration owners. Product commands remain outside the reference.

## Layer And Consumer Impact

[ADR 0048](../../docs/adr/0048-add-implementation-reference-layer.md) already authorises concise implementation-neutral compositions under `doctrine/impl/`, so no new ADR is required. The reference passes the layer contract tests: testing placement is a common delivery activity; no single owner supplies the cross-surface model; deleting the reference removes no obligation; and every material invariant routes to an owner.

Post-publication review found that the first version was technically strong but had begun to read like a compact testing handbook. It repeated specialist explanations, starting sets, and several secondary flows after the main evidence-placement model was already clear. The reference was therefore reduced by about one quarter, centred on the application and infrastructure delivery surfaces, and left specialist depth with canonical owners or future activity-specific references. This is the compression test operating as intended, not a change to testing doctrine.

Change class: **additive guidance / navigation**.

No existing testing requirement, applicability condition, supported-platform claim, or exception path changes. The principal residual risk is summary drift: the matrix may be mistaken for a universal checklist or outlive a changed owner. The page labels its sets and matrix as contextual, states canonical precedence, and links every subject area back to its owner.
