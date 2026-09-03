---
name: method-record-classification
description: Primes an agent to keep tools out of authorship fields and to classify a change candidate honestly as generated, curated, or authored, recording the revision-pinned harness and ruleset in a method-record field that makes no authorship claim. Load before an agent finalises a commit, PR, or other change candidate in an estate-governed or production delivery path.
license: Apache-2.0
doctrine:
  schema_version: "1.0.0"
  version: "1.0.0"
  kind: procedure
  authority: advisory
  injection: estate-policy
  status: active
  tier: 1
  applies_to:
    - finalising a commit, pull request, or change candidate that a model or agent helped produce
  governing:
    - path: doctrine/patterns/code-review-and-change-approval.md
      section: "6.1"
    - path: doctrine/principles/ai-ml-systems.md
      section: "4"
    - path: docs/adr/0043-replace-agent-coauthorship-disclosure-with-a-method-record.md
  priming_block_sha256: "b8740a8f26ed1d0f06a63dbd12b4b98da742a36c8bf1234e97a1aa8fc3f8d767"
  verifier_pack: ./verifier-pack.yml
  model_scope: {}
  evaluation:
    evidence: null
    scope: No portable evaluation ships with this library.
  owner: library-maintainers
  review_date: "2027-09-03"
---

# Method-Record Classification Skill

**Kind:** change-lifecycle procedure
**Authority:** advisory; the named human author owns the class asserted

## Purpose

Discharge the disclosure duty in
[code-review-and-change-approval.md §6](../../patterns/code-review-and-change-approval.md)
the way [ADR 0043](../../../docs/adr/0043-replace-agent-coauthorship-disclosure-with-a-method-record.md)
requires: a tool is never a co-author, and how the candidate was produced is
recorded in a separately addressable, falsifiable field. The class vocabulary
is defined in §6.1 of the pattern; this skill only makes an agent apply it
before the candidate leaves its hands.

## Instructions

```priming
Before you finalise a commit or change candidate:
1. Never write a non-human tool into an authorship field: Author, Co-Authored-By, Signed-off-by, or any successor that confers standing. The named human holds authorship, ownership, and accountability whole.
2. Classify the candidate honestly. generated: accepted substantially as produced, review was inspection. curated: produced under a declared, revision-pinned harness and ruleset, then materially revised by the named author. authored: written by the author; ordinary tool assistance does not change this.
3. Record the class with the revision-pinned harness and ruleset in a field that makes no authorship claim. Recommended trailer: Produced-With: harness=<id>@<rev>; doctrine=<id>@<rev>; class=<class>. An authored change MAY omit the record.
4. Claim curated only when both revisions are pinned and the material revision is visible in the diff. curated is falsifiable and is not a courtesy upgrade from generated.
5. The record is required in estate-governed and production paths and a strong default elsewhere. If the estate binds a different key, use it. If it binds an authorship field, refuse and flag the binding.
6. If you cannot determine the class, say so and leave the decision to the named author rather than guessing.
```

## Run-Contract Use

```yaml
context:
  skills:
    - method-record-classification@1.0.0
verifiers:
  - method-record-classification-verifier-pack@1.0.0
```

Estates normally bind this skill to the task class that produces commits or
PRs, and the sibling pack runs against the candidate checkout.

## Required Independent Checks

- no authorship field on the candidate names anything outside the estate's
  human-identity allowlist;
- if a method record is present it is well-formed and its class is in the
  vocabulary;
- a `curated` record pins both harness and ruleset revisions; and
- the named author confirms the asserted class at review (the pack cannot judge
  whether revision was material).

## Failure Handling

- Missing or altered priming context: `mark_untrusted`.
- Tool named in an authorship field: `fail_loud` (a category error, not a
  formatting issue).
- Malformed method record: `fail_loud`.
- `curated` without pinned revisions: `fail_loud`.

## Limits

The pack checks the record's form and the authorship fields. Whether the
revision was material, and therefore whether `curated` is honest, is decided by
the named author and their reviewer. The allowlist of human identities is an
estate binding and is deliberately not defined here.
