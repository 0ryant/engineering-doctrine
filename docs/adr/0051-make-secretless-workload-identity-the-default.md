# ADR 0051: Make Secretless Workload Identity The Default

- **Status:** Accepted
- **Decision date:** 2026-11-15
- **Recorded date:** 2026-11-15
- **Retrospective:** No
- **Deciders:** Repository operator
- **Review provenance:** Operator-directed and operator-accepted on 2026-11-15; drafted and reviewed by a model, no independent human or domain review recorded
- **Research:** [Secretless workload identity as the default](../../doctrine/evolution/research-secretless-workload-identity-default-2026-11.md)
- **Canonical owner:** [Zero Trust And Workload Identity](../../doctrine/principles/zero-trust-and-workload-identity.md) §2
- **Derived landings:** [Configuration And Secrets](../../doctrine/principles/configuration-and-secrets.md) §§1, 4 (pointers); [Build Readiness](../../doctrine/checklists/build-readiness.md); [Platform Readiness](../../doctrine/checklists/platform-readiness.md); [Secretless Workload Identity](../../doctrine/impl/secretless-workload-identity.md); [glossary](../../doctrine/glossary.md)

The owner and landing edits land in the same change as this ADR.

## Context

Zero trust §2 prefers short-lived, audience-scoped workload credentials, and configuration and secrets §4 asks for CI federation "where possible". Preference leaves the common failure untouched: stored long-lived secrets accumulate in CI settings, environment files, and secret stores for targets that would accept federated identity, with no record of why. The operator asked for secretless access to be the library's stance.

Provider guidance converges on temporary workload credentials as the default and keeps long-term keys for workloads that cannot use them. IETF work on workload identity practices points the same way but is still a draft. The evidence is in the [research note](../../doctrine/evolution/research-secretless-workload-identity-default-2026-11.md).

## Decision

Zero trust §2 becomes the canonical owner of a **secretless default**:

1. **MUST (estate-governed and production workloads, including CI and CD jobs):** where the target accepts federated or platform-issued workload identity, authenticate with that short-lived, audience-scoped credential rather than a stored long-lived secret. Keeping a stored secret for such a target requires a bounded exception under the [exception contract](../../doctrine/patterns/normative-language-applicability-and-exceptions.md#5-exception-contract).
2. **MUST (same scope):** where the target cannot accept federated identity, the stored secret is a registered fallback. Record its owner, rotation cadence, blast radius, and the reason federation is unavailable wherever the estate tracks secrets. Recheck when the target or platform adds support; rule 1 then applies.
3. **Unchanged:** local development, human and break-glass access (§3), and the agent-specific rules in §2.1, which inherit this default for agents holding their own identity.

Configuration and secrets §§1 and 4 point to the owner instead of restating the rule. The checklists gain one derived prompt each. The implementation reference describes the default and its fallback.

## Control Cost And Lifecycle

| Field | Value |
| --- | --- |
| Failure addressed | Long-lived credentials that are leaked, over-shared, or never rotated, for targets that did not need them |
| Expected evidence | For each production or CI target: federated identity in configuration, a registered fallback with the four fields, or a bounded exception |
| Accountable owner | The workload's service owner; the platform team owns the federation capability |
| Operating cost | Federation setup per platform and target; keeping the fallback register current |
| Review trigger | WIMSE workload identity practices published as an RFC; evidence that runtime token theft dominates incidents; a fallback register that stays large |
| Simplification or retirement | If platforms make federation universal, the fallback register collapses; if most targets remain fallbacks, narrow the scope or return to a preference |

## Alternatives Considered

### Keep the preference

Rejected by the operator. A preference leaves no record of why a federatable target still holds a stored secret.

### Ban stored secrets outright

Rejected. Many third-party APIs, webhook senders, and legacy targets accept only static keys. Every such key would become a permanent exception, which the exception contract treats as evidence the rule is wrong.

### Also forbid environment-variable delivery

Deferred. The source is an IETF draft. Revisit when it is published.

### Put the rule in configuration and secrets

Rejected. The rule concerns how a workload proves its identity, which zero trust §2 owns. Configuration and secrets keeps secret-handling rules and points to the owner.

## Consumer Impact And Migration

Change class: **normative tightening**, scoped to estate-governed and production workloads, including CI and CD jobs. Local development, human access, and non-production experiments are unaffected.

Compatibility: pre-1.0 minor.

Migration:

1. Inventory the credentials each production workload and pipeline holds.
2. Move every target that accepts federated or platform identity to the secretless path.
3. Register the remaining stored secrets as fallbacks with the four required fields.
4. Where a federatable target cannot move yet, record a bounded exception with an owner and expiry chosen by the estate.

No fixed calendar deadline is imposed. The exception expiry carries the migration clock.

## Acceptance Criteria

- Zero trust §2 states both MUST rules with their scope.
- Configuration and secrets §§1 and 4 route to the owner without restating it.
- Build and platform readiness each carry one derived prompt linked to the owner.
- The implementation reference and glossary describe the default and its fallback.
- The ADR index lists this decision, and doctrine preflight passes.

## Residual Risk

The rule rests on convergent provider guidance and risk asymmetry, not a ratified standard or measured incident reduction. Short-lived tokens can still be stolen from a compromised job, so pipeline integrity and provenance verification remain necessary. "Accepts federated identity" can be argued case by case; the fallback register makes those judgements visible but does not settle them. Model review only; no independent human or domain review is recorded.
