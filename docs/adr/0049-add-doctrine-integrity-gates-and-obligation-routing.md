# 0049. Add Doctrine Integrity Gates And Obligation Routing

Status: Accepted
Decision date: 2026-09-19
Recorded date: 2026-09-19
Retrospective: No
Review provenance: Agent-assisted implementation and model review; not independent human or domain review.

## Context

The corpus review found broken umbrella anchors, executable-looking YAML that
was not validated, hand-maintained schema counts, and controls with incomplete
checklist routes. ADR 0036 repaired individual instances, but did not install
all the regression gates. Some checklist additions also landed concatenated
onto preceding items. Passing the existing contract harness did not establish
that the examples printed in Markdown were valid: that harness primarily
constructs its own examples.

These are library integrity and discoverability defects. They do not justify
inventing new controls for consuming systems.

## Decision

Implement the V46–V48 integrity work from the
[release roadmap](../../doctrine/evolution/post-v0.3.0-external-review-decisions-and-v0.4.0-plan-2026-07.md):

1. Check rendered local Markdown link targets and `ENGINEERING.md` anchors in
   preflight and CI. Ignore example code and external URLs; do not report
   network health or arbitrary-file fragment validity as checked.
2. Parse the YAML examples printed in doctrine Markdown. Complete examples
   owned by a repository schema receive schema validation. Partial excerpts
   and externally owned formats are explicitly identified, with the narrower
   syntax-only assurance stated. Nothing in this check executes a command,
   queries a live service, or proves runtime semantics.
3. Route the activated controls introduced by ADRs 0031–0035 from AI adoption
   readiness to their existing canonical owners. Repair malformed checklist
   entries. The owner's strength, scope and exception path remain authoritative.
4. Make future ADRs that change typed obligations identify canonical ownership
   and derived checklist/navigation landings, or explain why none is needed.
   The canonical maintainer requirement lives in the change harness §3; the
   doctrine-change checklist is its verification surface.

Prefer links to actual schemas over hand-counted summaries of schema members.
Keep the existing contract and skill validators: direct documentation checks
complement their semantic cases rather than replacing them.

## Control Cost And Lifecycle

The PR author maintains the ownership map; the reviewer checks it against the
diff. Automated gates run locally and in CI. Their cost is a small dependency
set and bounded repository parsing, with no network sweep. Revisit the gates
when rendering syntax, schema ownership or repository layout changes. Remove
a derived checklist prompt when its owning obligation is retired; simplify a
gate when a maintained equivalent proves the same property.

## Alternatives Considered

- **One-off repairs only:** rejected; they leave the demonstrated drift path open.
- **Validate separately constructed examples only:** retained for semantic tests,
  rejected as evidence about the examples readers actually copy.
- **Treat every snippet as a complete contract:** rejected; excerpts are useful
  but must not masquerade as complete schema-conforming instances.
- **Duplicate controls in checklists:** rejected; discoverability must not create
  another normative owner.
- **Check all external URLs on each PR:** deferred; network availability and
  source support require different evidence from deterministic internal links.

## Evidence

The [integrity investigation](../../doctrine/evolution/research-doctrine-integrity-gates-2026-09.md)
records the repository evidence, routing map and verification limits. The
[August corpus review](../../doctrine/evolution/research-full-corpus-council-review-2026-08.md)
and [ADR 0036](0036-land-v050-correction-batch-from-the-corpus-review.md)
provide the historical findings. The research note also records the new
maintainer gate's **C2 admission with risk asymmetry**, independently sourced
documentation guidance, dated captures and limits. This is a repository-specific
maintenance decision, not a new portable engineering control justified by
repository precedent.

## Consumer Impact And Migration

Change class: **editorial corrections / navigation / maintainer-process tightening**.

Consuming applications gain no new obligations. Existing AI controls become
easier to find without changing applicability. Maintainers install the declared
Python requirements, classify YAML examples, fix invalid links/examples, and
include an ownership/landing map in obligation-changing ADRs. No content is
retired or moved by this decision.

## Acceptance Criteria

- Negative fixtures demonstrate that broken paths, umbrella anchors and invalid
  YAML/schema examples fail the corresponding checks.
- Current tracked documentation passes those checks locally and in CI.
- ADRs 0031–0035 have explicit, owner-linked readiness coverage without making
  conditional or profile-specific controls universal.
- Preflight runs the new gates and the generated sitemap is current.
- The maintainer ownership requirement and its derived checklist route agree.

## Residual Risk

Reachability is not semantic correctness; valid YAML is not a working runtime.
Model review is not independent domain review or human usability evidence.
These gates do not close the remaining v0.6.0 release criteria or authorise a tag.
