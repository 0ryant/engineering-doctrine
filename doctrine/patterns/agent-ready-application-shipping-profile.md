# Agent-Ready Application Shipping Profile

Use this named profile when an accountable estate decides that every
application it ships must be immediately discoverable to both people and
software agents. It composes [Build Principles](../principles/build.md),
[Developer Experience](../principles/developer-experience.md),
[Agent Doctrine Consumption](agent-doctrine-consumption.md) and
[Doctrine Versioning](doctrine-versioning-and-consumer-compatibility.md).
The decision and evidence basis are [ADR 0050](../../docs/adr/0050-adopt-agent-ready-application-shipping-profile.md)
and the [research note](../evolution/research-agent-ready-application-discovery-2026-11.md).

## 1. Applicability and owner

This is an optional portable profile, not the universal doctrine baseline. It
activates only when an estate authority names:

- the repositories/products covered;
- the accountable profile owner;
- the effective release boundary; and
- the manifest location and review cadence.

Once activated, it applies to every **shippable surface** in that manifest: a
user-facing executable, application, agent/host adapter, static exporter or
package path distributed outside build/test automation. Preview, beta and
experimental distributions remain rows with that support state; calling their
recipients unsupported does not remove them. Libraries and internal components
that are never independently distributed are not separate rows, but their
public entry points must remain reachable through the owning row.

## 2. Closed surface manifest

The profile owner **MUST** keep an exhaustive, versioned manifest. Each row
names:

- surface identity, kind and owning repository;
- every packaging/install channel;
- supported interaction/host surfaces;
- Skill bundle identity, version and digest;
- autocomplete/discovery mechanism and source schema;
- exact package/install checks; and
- support/lifecycle state.

Adding, removing, splitting, merging or reclassifying a row is a profile-
contract change reviewed before release. “Internal”, “experimental”, “static
exporter” or a second package channel is not an escape after the surface is
distributed outside build/test automation.

Failure addressed: an open inventory lets a new application evade a universal
release statement by changing its label after the fact. Evidence is a manifest-
to-build/package reconciliation that fails on unlisted distributable surfaces.

## 3. Skill requirement

“Skill” here is the product/host-declared Skill form. The stricter schema,
priming-block hash and sibling verifier-pack rules in
[Agent Doctrine Consumption](agent-doctrine-consumption.md) govern this
library's own doctrine Skills only. A product Skill uses its declared host or
product schema, while retaining this profile's advisory-authority,
version/digest, validation and exact-package requirements.

Every manifest row **MUST** ship at least one versioned, advisory,
machine-discoverable Skill that covers:

1. the primary user job and shortest safe workflow;
2. authority, data and side-effect limits;
3. correction, recovery or rollback where relevant; and
4. how to obtain exact help/current schema rather than guessing.

The Skill **MUST** be bound to the commands/actions and product version it
describes. A digest or signature proves byte identity, not correctness or
authority. A Skill **MUST NOT** approve an action, override host/user
instructions, promote retrieved material, or claim that an agent followed it.
Where a host implements a published Skill standard, use the conforming metadata
and discovery surface; a file hidden only in repository docs does not pass.

Evidence: parse/schema tests, digest manifest, referenced-command/action
resolution and a package/install discovery test on every declared channel.

## 4. Autocomplete requirement

Every manifest row **MUST** provide autocomplete appropriate to its primary
interaction surface:

| Surface | Required autocomplete/discovery outcome |
| --- | --- |
| CLI | Generated completion for every supported shell, derived from the live command parser/schema and syntax-smoke tested. |
| Graphical application | Command/action palette or field/action autocomplete covering supported primary workflows and reflecting current permissions/state. |
| API/SDK-first application | Versioned schema-backed IDE/client completion plus discoverable examples for primary operations. |
| Agent/host adapter or static exporter | Completion for the exporter CLI, host-native action/command completion, or another named autocomplete mechanism, plus discoverable configuration and the relevant Skill; static support must not be described as a dynamic integration. |

Autocomplete is not only a generated file. The exact installed surface must
load or expose it through the documented path. Adding/removing a public action
without regenerating the corresponding completion **MUST** fail the release
gate.

Evidence: schema/command parity, generation reproducibility, syntax/load smoke,
permission/state negatives where dynamic and exact installed discovery.

## 5. Exact-artifact release gate

Source-tree success is necessary and insufficient. Before each release under
the profile, the release owner **MUST** reconcile the surface manifest against:

- built package/archive/installer contents;
- fresh installation or static export output;
- Skill inventory, versions and digests;
- completion/action inventory derived from the runtime schema; and
- the documented first-use path.

Missing, stale, unparsable, undiscoverable or unlisted surfaces hold the
affected release. A packaging channel cannot borrow evidence from another
channel unless the bytes and installation result are identical and bound by
the release evidence.

## 6. Exceptions, review and retirement

Inside an activated profile, a shippable row has no per-release waiver from the
two-surface requirement. The profile authority may instead make a recorded
policy change that removes the row from the supported shipment, delays the
release, narrows the profile prospectively, or deactivates the profile for a
named future boundary. That decision cannot relabel failed/missing evidence as
a pass.

Review the profile when the app inventory, supported hosts/shells, packaging
graph, public command schema or Skill standard changes. The operating cost is
asset maintenance, packaging size, host compatibility checks and release time.
Simplify by generating both surfaces from canonical schemas and sharing
validators; retire the profile only when the accountable estate no longer
requires agent-ready shipment, through an explicit compatibility-impact
decision.

## 7. Failure modes

| Failure | Guard |
| --- | --- |
| Skill exists in source but not package | Exact package/install inventory and digest check |
| Completion is stale after a command change | Parser/schema-derived generation and command-drift test |
| A static exporter is marketed as a live adapter | Manifest support kind and separate static matrix |
| Skill text becomes hidden authority | Advisory-only contract and host/user precedence |
| New app evades the rule as “internal” | Closed distributable-surface reconciliation |
| One package channel silently omits assets | Per-channel exact-artifact gate |
| Profile becomes permanent bureaucracy without value | Named owner, review triggers, generation/shared validators and explicit retirement decision |

## 8. Consumer impact

**Change class:** additive guidance until activated; normative tightening for an
adopting estate. Activation should be versioned like any other policy-sensitive
dependency. Existing releases remain historical; the next declared release
boundary must pass the profile or hold.

Use the derived [agent-ready application readiness checklist](../checklists/agent-ready-application-readiness.md)
for review. The pattern is the canonical owner if checklist wording diverges.
