# 0028. Adopt Claim-Level Authority, Applicability, And Exceptions

Status: Accepted
Decision date: 2026-07-17
Recorded date: 2026-07-17
Retrospective: No

## Context

The library distinguishes portable principles, compositional patterns,
reviewable checklists, illustrative tooling, estate supplements, and
non-normative evolution notes. That storage taxonomy is sound, but it does not
by itself distinguish:

- a non-negotiable invariant from a strong default;
- a baseline claim from one activated only by risk or external authority;
- a context-dependent decision from an example; or
- a failed control result from a separately authorised exception.

The result is inconsistent rhetorical force, fragmented applicability and
exception mechanisms, and avoidable one-size-fits-all readings. Existing AI
materiality and revision-pinned external profiles already demonstrate that
capability, impact, authority, scope, evidence, and exceptions must remain
separate.

The external grounding, repository evidence, and source limits are recorded in
[research-doctrine-authority-applicability-2026-07.md](../../doctrine/evolution/research-doctrine-authority-applicability-2026-07.md).

## Decision

Adopt [Normative Language, Applicability, And Exceptions](../../doctrine/patterns/normative-language-applicability-and-exceptions.md)
as the general pattern for interpreting and authoring doctrine claims.

1. Use capitalised `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` with
   the meanings in BCP 14, RFC 2119 and RFC 8174, when explicit normative
   strength is useful. Lower-case uses keep their ordinary English meaning.
2. Apply strength to individual claims or tightly bounded groups of claims,
   not to an entire mixed document. Normative prose without a BCP 14 keyword
   remains possible, but material obligations must not rely on typography or
   tone alone.
3. Treat `CONTEXT-DEPENDENT` and `EXAMPLE` as content classes, not BCP 14
   requirement levels. Context-dependent guidance names the decision and
   trade-offs; examples are non-normative.
4. Determine applicability before enforcing claim strength. Compose exposure,
   criticality/blast radius, data/external obligations, operational
   model/recoverability, change autonomy, consumer compatibility, and
   observability. Named profiles activate existing controls; they do not form
   a new storage layer.
5. Apply every compatible obligation from every applicable profile. Where
   controls overlap, use the stricter result. Where authorities genuinely
   conflict, record and escalate the conflict rather than selecting the
   convenient rule.
6. Record an exception separately from the rule, evidence, and finding. The
   minimum record contains identity, rule/profile and revision, exact scope,
   accountable authority, rationale and residual risk, evidence, compensating
   controls, owner and remediation, effective period, expiry, review, and
   closure or expiry detection.
7. An exception never changes `fail`, `inconclusive`, absent, or stale evidence
   into `pass`. This library cannot authorise departure from law, regulation,
   contract, or an external profile; only an authority recognised by that
   source can approve a permitted variance.
8. Adopting organisations keep live exception records in their controlled
   systems of record. This public library publishes only the portable pattern
   and record shape.
9. Every new or materially expanded control identifies the failure it
   addresses, expected evidence, operating cost, accountable owner, review
   trigger, and a condition for simplification or retirement.
10. Preserve ADR 0003's principle/pattern/tooling/checklist/evolution taxonomy.
    Do not require document-wide strength metadata or a corpus-wide metadata
    migration in this release.

## Alternatives Considered

### Continue With Imperative Prose And Bold Emphasis

Rejected. Readers cannot consistently distinguish invariants, defaults,
contextual advice, and examples.

### Assign One Requirement Level To Each Document

Rejected. Principles and patterns contain mixed claims, rationale, examples,
and conditional sections. One label would hide rather than remove ambiguity.

### Create A Universal Control Baseline

Rejected. A local utility, public service, critical platform, regulated data
system, and agent-enacted production path do not share one materiality or
authority surface.

### Create New Core, Default, Profile, And Reference Directories

Rejected. Those are useful consumption views but orthogonal to the existing
storage layers. Physical reorganisation would add compatibility cost without
solving claim semantics.

### Publish A Root `EXCEPTIONS.md` Register

Rejected. A live register would contain adopter-specific authority decisions
and could be mistaken for portable doctrine authority.

## Consequences

### Positive

- Material claims gain explicit strength and activation conditions.
- Existing AI and external-control profiles compose with one general model.
- Exceptions remain auditable without corrupting evidence results.
- Low-materiality consumers can avoid irrelevant ceremony while higher-risk
  consumers receive stronger controls.
- Control accumulation gains an explicit cost, review, and retirement test.

### Costs And Risks

- Existing prose must be reviewed claim by claim; mechanical keyword
  replacement would create false requirements.
- Applicability classification can still be wrong or gamed without accountable
  ownership and evidence.
- Overlapping profiles may expose unresolved authority conflicts.
- Exception review can become ceremonial if expiry and compensating evidence
  are not enforced.

## Consumer Impact And Migration

**Change class:** normative replacement plus normative tightening.

Consumers should classify their adopted rules and active profiles, migrate
material exceptions to the minimum record, and review existing universal
wording before importing the replacement text. Existing external profiles keep
their own authority and revision rules.

**Compatibility proposal:** `0.3.0`, a pre-1.0 minor containing intentional
normative movement. Pinned consumers must review before adoption.

## Acceptance Criteria And Measures

- The canonical pattern defines claim strength, content classes,
  applicability, composition, exception admissibility, and control lifecycle.
- At least three worked surfaces demonstrate different defensible control
  activation from the same model.
- The doctrine change harness and checklist test strength, applicability,
  evidence, exception authority, cost, and retirement.
- A waiver or variance cannot overwrite a failed, inconclusive, absent, or
  stale result in any touched canonical surface.
- Review samples track ambiguous material claims, expired exceptions,
  duplicated normative owners, and controls simplified or retired without
  hiding resulting regressions.

## Residual Risks

- No universal applicability scoring formula is adopted; consumers must define
  values and accountable classifiers appropriate to their context.
- BCP 14 improves precision but does not prove that a claim is correct,
  proportionate, or externally required.
- The pattern can reduce unnecessary process only if adopters actually review
  control cost and retirement conditions.

## Related

- [ADR 0003](0003-split-doctrine-into-principles-patterns-tooling-checklists-and-evolution.md)
- [ADR 0026](0026-adopt-revision-pinned-external-control-profiles.md)
- [ADR 0027](0027-keep-public-doctrine-implementation-neutral.md)
- [Doctrine Versioning And Consumer Compatibility](../../doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md)
