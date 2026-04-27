# 0009. Add GitOps And Declarative Operations Pattern

Status: Accepted  
Decision date: 2026-04-27  
Recorded date: 2026-04-27  
Retrospective: No

## Context

The library already encodes **promotion of immutable artefacts**, **single source of truth**, **no manual production snowflakes**, and **merge-path scrutiny for IaC** across several principles. **GitOps** (declarative desired state, reconciliation, drift visibility) is a **named practice** in industry ([OpenGitOps](https://opengitops.dev/)) but was **not** a first-class page—contributors and adopters had to **reconstruct** the shape from [build.md](../../doctrine/principles/build.md), [collaboration.md](../../doctrine/principles/collaboration.md), and [merge-path…](../../doctrine/principles/merge-path-evidence-and-pipeline-integrity.md) alone.

## Decision

Add [doctrine/patterns/gitops-and-declarative-operations.md](../../doctrine/patterns/gitops-and-declarative-operations.md) as a **portable pattern**: definitions, **invariants**, what GitOps is **not**, and links to principles—**no** new vendor mandates in `principles/`. Estate-specific Argo, Flux, or cloud wiring remains in `tooling/estates/` or org supplements.

## Consequences

- **Navigation** and **citability** improve for a common delivery model.
- **Overclaiming** is avoided: the pattern is explicit that **label** without **reconciliation** **discipline** is not sufficient.
- Future changes follow [doctrine-library-change-harness.md](../../doctrine/patterns/doctrine-library-change-harness.md) (sitemap, REFERENCES, glossary).

## Evidence

- Pattern and ADR added in the same change; contemporaneous review discussion was not treated as the system of record.
