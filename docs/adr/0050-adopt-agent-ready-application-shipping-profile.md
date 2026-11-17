# ADR 0050: Adopt an agent-ready application shipping profile

- **Status:** Accepted
- **Decision date:** 2026-11-15
- **Deciders:** Repository operator
- **Review provenance:** Operator-directed; drafted with agent council review, no independent human/domain review recorded
- **Research:** [Agent-ready application discovery](../../doctrine/evolution/research-agent-ready-application-discovery-2026-11.md)
- **Canonical owner:** [Agent-ready application shipping profile](../../doctrine/patterns/agent-ready-application-shipping-profile.md)
- **Derived checklist:** [Agent-ready application readiness](../../doctrine/checklists/agent-ready-application-readiness.md)

## Context

Agent-facing instructions and autocomplete are often treated as optional
documentation. That allows them to exist in source but disappear from packages,
installers, host adapters or static exporters. It also makes “all applications
support this” impossible to test because the application set is open-ended.

The operator selected a forward shipping rule: applications in the owned estate
must ship with Skills and autocomplete. This library is portable, so an
estate-specific selection cannot become a universal baseline for every
consumer. It needs a named profile whose activation, inventory and evidence are
explicit.

## Decision

Add the optional **agent-ready application shipping profile**. When an
accountable estate activates it:

1. It maintains an exhaustive manifest of every executable, application,
   adapter, exporter and package path distributed outside build/test
   automation, including preview/beta surfaces.
2. Every row **MUST** ship at least one versioned, advisory, machine-
   discoverable Skill covering its primary workflow and limits.
3. Every row **MUST** ship autocomplete appropriate to its primary interaction
   surface: generated shell completion, command/action completion or palette,
   schema-backed IDE/client completion, or a named exporter/host autocomplete
   mechanism. Discovery prose alone is insufficient.
4. Exact packaged and installed artefacts **MUST** prove both surfaces are
   present, current and discoverable. Source-tree tests alone do not pass.
5. Adding, removing or reclassifying a shippable row is a profile-contract
   change reviewed before release. A packaging channel cannot evade the gate.

The pattern is the canonical owner. The checklist derives review prompts. The
semantic index, doctrine README, references map and sitemap make the profile
discoverable.

Skills remain advisory. They cannot approve actions, override host/user
instructions, establish trust or substitute for runtime verification.

## Alternatives considered

| Alternative | Disposition | Reason |
| --- | --- | --- |
| Make the rule a universal baseline for every doctrine consumer | Reject | External sources describe mechanisms, not a universal need; estates differ. |
| Require Skills but not autocomplete | Reject | Agent guidance does not make commands discoverable to people or tools at the interaction point. |
| Require autocomplete but not Skills | Reject | Completion exposes syntax, not product intent, safety limits or recovery paths. |
| Check only the source tree | Reject | Packaging omission and command drift are the target failure modes. |
| Allow unmanifested “internal” apps | Reject inside an activated profile | An open census makes the rule non-falsifiable. Non-shippable components remain outside scope. |

## Consumer impact and migration

**Change class:** additive guidance for the portable library; normative
tightening only for estates that activate the profile.

Existing consumers are unchanged until they activate it. An adopting estate
must inventory shippable surfaces, name the accountable profile owner, add
Skill/autocomplete assets and exact-artifact checks, then gate later releases.
Existing releases need not be rewritten, but the next release after activation
must either pass or remain held. Removing the profile is a recorded policy
change, not a per-release waiver.

## Acceptance

- The pattern declares applicability, evidence, failure, cost, owner, review
  trigger and retirement path.
- The checklist contains no obligation absent from the pattern.
- Navigation reaches the pattern from the semantic index, README, references
  map and generated sitemap.
- The doctrine preflight passes.
- Three sample consumers—CLI, graphical app and static host adapter—can map to
  a concrete Skill and autocomplete/discovery mechanism without changing the
  profile wording.

## Consequences and residual risk

Activated estates gain a finite, testable app census and make agent/human
discoverability part of release evidence. They also accept permanent packaging
and compatibility-test cost.

The profile does not prove a Skill is useful, an agent follows it, suggestions
are well ranked, or every host supports one standard. Those remain product and
estate evaluation responsibilities. The external references are rolling and no
archival copy was captured in this change; future source movement needs review.
