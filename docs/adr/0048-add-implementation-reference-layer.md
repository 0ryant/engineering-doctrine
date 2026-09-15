# 0048. Add An Implementation Reference Layer

Status: Accepted
Decision date: 2026-09-14
Recorded date: 2026-09-14
Retrospective: No

## Context

The doctrine separates durable principles, compositional patterns, replaceable tooling, verification checklists, research, and library decisions. That structure preserves authority and portability, but it leaves a common usability gap: an engineer asking how to perform a familiar activity often has to read three or more canonical files and reconstruct the normal operating model.

Patterns currently carry two cognitive roles. Some explain mechanics, trade-offs, lifecycle behaviour, governance, alternatives, and failure modes. Others are used as short composition routes that answer “what does the normal implementation look like?” Combining those roles makes patterns harder to scan and tempts quick-reference pages either to grow into full patterns or to duplicate principle-level rules.

The supplied CI/CD composition exposed the gap clearly. Its value is a concise branch-to-production reference, while the detailed authority already exists in build, collaboration, source-of-truth, merge-path, build-surface, and trunk-workflow doctrine.

## Decision

Add `doctrine/impl/` as a first-class layer between patterns and tooling:

> **`impl/` — implementation-neutral reference implementations. These documents compose canonical principles and patterns into simple engineer-facing operating models. They MAY simplify, visualise, and route existing doctrine, but MUST NOT create new normative requirements. Canonical principles and owning patterns remain authoritative on conflict.**

`doctrine/impl/README.md` defines the layer contract. An implementation reference:

- presents a concise normal flow, lifecycle, state model, or composition;
- remains independent of vendor, product, cloud, and local estate choices;
- points to canonical principles and owning patterns at the bottom;
- may route onward to tooling mappings and checklists;
- is defective when it conflicts with a canonical owner; and
- does not become a second source of truth for an underlying requirement.

The normal candidate test is a common engineering activity for which a reader needs several canonical files to recover a useful operating shape. References target roughly 500–1,500 words and a two-to-five-minute scan, with exceptions only where the implementation genuinely needs more space.

The contract was refined on 2026-09-14 after reviewing the first two references. `impl/README.md` now makes three decisive tests explicit: the file names an activity engineers perform, compresses a model distributed across canonical owners, and creates no obligation that would disappear if the reference were deleted. The internal mental model is a **compiled view of doctrine**: composition can select and simplify source semantics but cannot invent them. Traceability, variation, and practical-use tests complete the admission check.

Land `doctrine/impl/cicd-delivery.md` as the first exemplar. It composes the branch-to-production flow and distinguishes unchanged application-artefact promotion from environment-specific infrastructure plans, stateful database changes, and rendered configuration.

Tooling remains separate because products and estate bindings change independently of the operating model. Checklists remain derived verification surfaces, not rule owners. Patterns remain the correct home for trade-offs, failure modes, alternative strategies, and architectural or governance mechanics.

This decision extends the layer model adopted by [ADR 0003](0003-split-doctrine-into-principles-patterns-tooling-checklists-and-evolution.md); it does not supersede that decision.

## Alternatives Considered

### Leave composition to readers

Rejected. Reconstructing frequent operating models repeatedly increases time-to-use and interpretation drift.

### Keep short composition pages in `patterns/`

Rejected. It preserves the existing dual role and makes the difference between explanatory models and quick implementation references implicit.

### Put composition in `tooling/`

Rejected. The normal shape should survive a change of CI product, cloud, runtime, or deployment service.

### Turn checklists into implementation guides

Rejected. A verification surface is intentionally lossy and should not become the only place a reader learns the operating model.

### Create all proposed references immediately

Rejected. The layer should be reviewed through one high-value exemplar. Each later file must pass the candidate test and receive an owner audit rather than existing to fill a framework matrix.

## Consequences

Positive:

- common implementation intent gains a two-to-five-minute progressive-disclosure route;
- patterns can retain depth without also serving as quick-reference templates;
- product mappings stay replaceable;
- canonical ownership remains explicit at the point of use; and
- humans and agents can route from task intent to a normal shape before loading deeper doctrine.

Costs and risks:

- the repository gains another first-class directory and navigation surface;
- summaries can drift from their owners or accidentally strengthen them;
- “normal” can be misread as universal when applicability is omitted; and
- low-value thin references could accumulate.

Mitigations are canonical-owner precedence, mandatory bottom-of-file owner links, the contract tests, the concise document shape, normal lifecycle sweeps, and review for duplicated normative language.

## Evidence

See [research-implementation-reference-layer-2026-09.md](../../doctrine/evolution/research-implementation-reference-layer-2026-09.md). The note records the in-repository owner audit, the supplied CI/CD proposal as source material, the layer comparison, and the screened backlog.

No new external engineering control is introduced. External grounding remains with each canonical owning principle or pattern and `doctrine/REFERENCES.md`.

## Consumer Impact And Migration

Change class: **additive guidance / navigation**.

No existing consumer obligation is strengthened, weakened, relocated, deprecated, or removed. Existing links to principles and patterns remain valid. Consumers may adopt `impl/` links as progressive-disclosure entry points while retaining their pinned canonical owners and estate-specific tooling.

No migration is required.

## Acceptance Criteria

- `doctrine/impl/` is documented as a distinct first-class composition layer.
- Its inability to create normative requirements and canonical-owner precedence are explicit.
- CI/CD delivery is the first concise, implementation-neutral exemplar.
- The exemplar covers applications, infrastructure as code, database changes, and rendered configuration honestly.
- Semantic and entry-point navigation route implementation intent through the layer and onward to owners.
- The future backlog is recorded as proposal, not adopted doctrine.
- The sitemap is regenerated and doctrine preflight passes.

## Residual Risk

Documentation drift remains the primary risk. Automated link and sitemap checks can prove reachability, but they cannot prove that every summary still has identical scope and strength to its owners. Maintainer review and lifecycle sweeps remain necessary.
