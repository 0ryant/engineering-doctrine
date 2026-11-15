# Agent-Ready Application Readiness

Derived from the [Agent-Ready Application Shipping Profile](../patterns/agent-ready-application-shipping-profile.md).
Use only after an accountable estate has activated that profile. The pattern is
authoritative if this checklist diverges.

## Activation and inventory

- [ ] Profile owner, covered estate/repositories and effective release boundary are recorded.
- [ ] The manifest lists every shippable executable, app, adapter, exporter and package/install channel.
- [ ] Build/package reconciliation fails on an unlisted distributable surface.
- [ ] Added, removed or reclassified rows received profile-contract review.

## Skills

- [ ] Every row ships at least one versioned, advisory Skill for its primary workflow and limits.
- [ ] Each Skill names the shortest safe primary workflow, authority/data/side-effect limits, exact-help route and correction/recovery path where relevant.
- [ ] Skill schema parses and its version/digest match exact packaged bytes.
- [ ] Referenced commands/actions exist in the same product version.
- [ ] The exact installed/exported surface is discoverable by the declared host/user path.
- [ ] Skill text claims no approval, host precedence, execution proof or independent verification.

## Autocomplete and discovery

- [ ] Each CLI supports every declared shell with parser/schema-derived completion.
- [ ] Each graphical/API/adapter/exporter row names an actual action, field, IDE/client, exporter-CLI or host-native autocomplete mechanism; discovery text alone is insufficient.
- [ ] Public command/action drift fails generation or parity checks.
- [ ] Exact installed output passes syntax/load/discovery smoke tests.
- [ ] Static exporters are labelled and tested separately from dynamic integrations.

## Release evidence

- [ ] Every package/install channel is checked, or byte identity justifies shared evidence.
- [ ] Missing/stale assets hold release rather than receiving a per-release waiver.
- [ ] First-use documentation matches exact installed behaviour.
- [ ] Review triggers and a future profile simplification/retirement authority are recorded.
