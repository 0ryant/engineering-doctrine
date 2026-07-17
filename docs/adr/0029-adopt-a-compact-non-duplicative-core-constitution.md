# 0029. Adopt A Compact, Non-Duplicative Core Constitution

Status: Accepted
Decision date: 2026-07-17
Recorded date: 2026-07-17
Retrospective: No

## Context

`ENGINEERING.md` began as a small umbrella and grew into more than a headline
guide. It now combines principles, architecture and security prescriptions,
tool and version examples, repository layouts, an extended document catalogue,
and a project-bootstrap checklist. Much of that content also exists in
canonical principle, pattern, tooling, and checklist files.

The current reading guidance acknowledges that the umbrella can lag and tells
readers to prefer a principle file on conflict. That makes disagreement an
expected navigation feature rather than a defect. The ten-item TL;DR spine then
adds another compressed copy of some claims.

The library needs a memorable daily entry point without discarding the depth
that makes it useful as a reference and evidence corpus. Research and source
limits are recorded in
[research-doctrine-authority-applicability-2026-07.md](../../doctrine/evolution/research-doctrine-authority-applicability-2026-07.md).

## Decision

Rebuild `ENGINEERING.md` as the compact core constitution and primary route
into the wider library.

1. The core may contain only:
   - purpose, scope, and authority boundaries;
   - the claim-level normative vocabulary adopted by ADR 0028;
   - approximately ten memorable, technology-neutral propositions;
   - entry points for applicability, exceptions, and adoption; and
   - links to canonical topic detail and semantic navigation.
2. The core is canonical for those core propositions. Topic principles are
   canonical for durable domain detail. Activated patterns own conditional
   operating models; checklists derive review questions; tooling illustrates
   replaceable implementations; evolution notes provide non-normative evidence
   and history.
3. Do not restate detailed normative blocks in the core. Technology versions,
   algorithm menus, vendor or language tables, exact file layouts, hook setup,
   pipeline filenames, and bootstrap checklists belong in their canonical
   principle, pattern, tooling, checklist, or estate surfaces.
4. A conflict between the core and a canonical detail source is a defect to
   block and repair. Readers must not be asked to choose whichever source is
   convenient.
5. Keep [tldr-principles-and-mvp.md](../../doctrine/tldr-principles-and-mvp.md)
   as the minimum-adoption route. It should link to, not duplicate, the core
   propositions.
6. Preserve the existing directory taxonomy and stable file paths. Core,
   baseline defaults, activated profiles, implementation/verification, and
   evidence/history are consumption views over those layers, not new
   directories.
7. Keep evolution material available for research, rationale, audit, and
   history, but exclude it from default operating routes unless the task asks
   for those concerns.
8. Do not use an arbitrary line limit as the acceptance test. Compactness is
   proven by singular ownership, absence of detailed duplicates, successful
   routing, and a first-pass reading suitable for normal engineering use.
9. Preserve legacy anchors where practical. Where compaction removes or
   changes a public section target, provide migration notes and update all
   in-repository references; do not silently break the documented compatibility
   surface.

This decision amends the navigation consequences of ADRs 0003, 0004, and 0011.
It does not change ADR 0003's storage-layer decision or make a route/index
authoritative over its linked sources.

## Alternatives Considered

### Keep `ENGINEERING.md` As A Compressed Mirror

Rejected. Duplicate normative detail creates drift, conflict rules, and review
work without adding a distinct authority surface.

### Delete The Reference Corpus And Keep Only Ten Rules

Rejected. Adopters still need rationale, domain constraints, implementation
patterns, checklists, external profiles, and research history.

### Make The TL;DR The Constitution And Remove The Umbrella

Rejected. `ENGINEERING.md` is already the public umbrella and compatibility
surface. The TL;DR has a distinct minimum-adoption purpose.

### Reorganise Files Into Five New Tiers

Rejected. Authority, applicability, and consumption view are separate from
storage layer. Navigation can express the views without mass moves.

### Enforce A Fixed Maximum Line Count

Rejected. A quota can reward compressed duplication or omit necessary scope
and exception semantics. Content ownership and reader task success are the
relevant tests.

## Consequences

### Positive

- A normal engineering reader gets one memorable constitution and one route to
  authoritative detail.
- Normative content has one owner instead of an umbrella copy plus a principle
  copy.
- Research depth remains available without contaminating ordinary retrieval.
- Tooling and estate choices stop appearing as timeless core law.

### Costs And Risks

- Compaction is a large semantic edit even if the resulting file is short.
- Existing external links to numbered umbrella sections may require preserved
  anchors or migration notes.
- Moving detail can reduce discoverability unless semantic routes and topic
  links are updated together.
- A concise core can become vague if its propositions are not linked to
  discriminating canonical detail.

## Consumer Impact And Migration

**Change class:** normative replacement, navigation change, and deprecation of
duplicated umbrella detail.

Consumers that copied individual umbrella sections should map them to the
linked canonical principles or patterns and review meaning changes introduced
by the claim-precision sweep. Consumers using stable file links keep the
`ENGINEERING.md` path; deep section links require the published migration map.

**Compatibility proposal:** `0.3.0`, a pre-1.0 minor containing intentional
normative movement. It is not a patch-level editorial rewrite.

## Acceptance Criteria And Measures

- Every detailed claim removed from the umbrella has one canonical owner or is
  explicitly retired with rationale.
- The core contains no implementation version, prescribed algorithm menu,
  vendor stack, repository-layout recipe, or copied project checklist.
- Reading guidance contains no rule that normalises disagreement between the
  core and canonical detail.
- The TL;DR, semantic index, README, glossary, and internal links agree with the
  new authority model.
- Representative readers or retrieval tasks can identify the core rule,
  applicable profile, exception path, and canonical detail without opening the
  complete sitemap.
- Track unresolved duplicate owners, broken legacy anchors, time to reach the
  canonical source, and material navigation failures after release.

## Residual Risks

- No source proves that approximately ten propositions is optimal; the number
  is a drafting target and must yield to clarity.
- External consumers may have copied text without retaining links, so upstream
  migration notes cannot identify every local fork.
- The reference corpus can continue to grow unless the change harness enforces
  singular ownership and control-retirement criteria.

## Related

- [ADR 0003](0003-split-doctrine-into-principles-patterns-tooling-checklists-and-evolution.md)
- [ADR 0004](0004-add-navigation-references-glossary-and-evolution-tracking.md)
- [ADR 0011](0011-add-semantic-index-for-agent-ingestion-and-topic-routing.md)
- [ADR 0028](0028-adopt-claim-level-authority-applicability-and-exceptions.md)
- [How To Read This Doctrine](../../doctrine/patterns/how-to-read-this-doctrine.md)
