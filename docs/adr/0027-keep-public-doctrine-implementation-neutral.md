# 0027. Keep Public Doctrine Implementation-Neutral

Status: Accepted
Decision date: 2026-07-17
Recorded date: 2026-07-17
Retrospective: No

## Context

The library declares a durable split between portable principles, compositional
patterns, replaceable tooling illustrations, and organisation-specific estate
material. Some later documents violated that boundary by naming private
portfolio implementations, linking to local programme evidence, or recording
repository-specific rollout work as though it were portable guidance.

That material creates three problems:

- adopters can mistake one organisation's implementation for a required stack;
- private or unstable names become part of a public compatibility surface; and
- local completion gaps obscure the reusable rule the document should state.

External standards, public research, and vendor documentation are different:
they may be named when they ground a claim, provided their authority and limits
are explicit and they are not prescribed as the only implementation.

## Decision

1. Publishable principles, patterns, checklists, contracts, research notes, and
   ADRs must not name organisation-private products, portfolio tools, internal
   repositories, or local programme artefacts.
2. State the portable capability or control instead: for example, “CI authority
   analysis”, “tool-contract generation”, “independent review engine”, or
   “bounded memory service”.
3. Keep concrete organisation implementations in the consuming organisation's
   private estate documentation, not in this public library.
4. Permit named external standards, public frameworks, research papers, and
   vendor material only as cited grounding or clearly optional illustration.
5. Local execution records and gap registers are not library content. Keep them
   under ignored local paths.
6. Remove estate-specific proposed decisions that have no portable contract,
   generalise reusable decisions and examples, and scrub publishable Git history
   so removed implementation names are not retained in reachable refs.

## Consequences

### Positive

- Adopters can apply the doctrine without discovering or buying a particular
  private toolchain.
- Normative meaning is separated from one implementation's release backlog.
- Public history no longer acts as an accidental catalogue of private names.

### Negative

- Some historical implementation detail moves out of the public record.
- A history rewrite changes commit identities for affected descendants.
- Consumers pinned to rewritten commits must re-fetch, re-clone if necessary,
  review the replacement history, and select a new pin.

## Consumer Impact And Migration

**Change class:** normative replacement plus history repair.

The portable obligations are not tightened. References to named local tools are
replaced with capability classes, and local rollout statements are removed or
reframed as adopter-owned calibration requirements.

Because reachable history is rewritten, commit-pinned consumers must treat this
as a breaking source-control event even where document semantics are unchanged.
Fetch with pruning or re-clone, then replace old commit pins with a reviewed
commit or release tag from the rewritten history. Do not merge unrelated old and
rewritten histories.

**Release proposal:** next `0.x` minor with an explicit history-rewrite notice.

## Verification

- Current publishable files contain no prohibited organisation-private names or
  internal repository references.
- Root local work records are absent and ignored.
- All publishable branches and tags pass a full-history content, path, and commit-
  message scan after rewriting.
- Doctrine preflight, contract validation, link checks, and Markdown lint pass.
- A verified offline backup remains available outside the publishable repository.

## Related

- [ADR 0003](0003-split-doctrine-into-principles-patterns-tooling-checklists-and-evolution.md)
- [Timeless Principles And Replaceable Tooling](../../doctrine/principles/timeless-principles-and-tooling.md)
- [Doctrine Library Change Harness](../../doctrine/patterns/doctrine-library-change-harness.md)
