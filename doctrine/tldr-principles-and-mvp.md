# TL;DR And Minimum Viable Doctrine

Use this page when the library feels too large. The compact constitution is [ENGINEERING.md](../ENGINEERING.md); canonical detail lives in the linked principles and patterns. This page owns the first adoption slice, not a duplicate set of principles.

## The Shape In One Minute

- Work has an accountable purpose and owner.
- Material boundaries are explicit, versioned, and verified.
- Small changes reach a protected trunk through relevant evidence and review.
- Failure, retry, rollback, observation, and learning are designed.
- Security and governance scale with exposure, materiality, external authority, and recoverability.
- Tools and standards are scoped defaults; exceptions are explicit and expiring.
- AI assists the normal delivery path; it does not become authority or proof.

For the full ten propositions and their canonical owners, read [ENGINEERING.md](../ENGINEERING.md#core-propositions).

## Minimum Viable Doctrine

This is the smallest baseline that makes further adoption safer. It usually fits into existing repository and team records.

| Order | Establish | Evidence |
| --- | --- | --- |
| 1 | **One quality gate** — format/lint/test/contract checks in CI and one documented local command that mirrors the relevant subset. | A representative change passes locally and in CI. |
| 2 | **Protected trunk** — no routine direct mutation of the default branch; required checks and reviewed, coherent changes. | Branch policy and a merged change receipt. |
| 3 | **First-change path and ownership** — README names owner, setup, fast check, first safe change, and deeper docs. | A new contributor can reach a checked change without private instructions. |
| 4 | **One material boundary contract** — API, event, data, configuration, or policy shape with examples and validation. | Invalid examples fail the controlled path. |
| 5 | **Operability baseline** — correlated telemetry on the main path and a known place for dashboards/runbooks. | Owner can diagnose a representative failure. |
| 6 | **Recovery and learning** — rollback/containment ownership and tracked learning when change fails. | A failed change has an accountable recovery route. |

Apply [Normative Language, Applicability, And Exceptions](patterns/normative-language-applicability-and-exceptions.md) before adding profiles. Do not copy every control into every repository.

## Add Profiles When The Boundary Requires Them

- **Public or critical service:** stronger SLO, security, capacity, progressive delivery, and incident controls.
- **Sensitive or externally controlled data:** revision-pinned authority, boundary, assessment, evidence, and exception rules.
- **Platform or multi-team component:** compatibility, golden-path, ownership, and consumer migration controls.
- **AI-assisted change:** normal candidate disclosure, evidence, review, authority, and runtime observation.
- **Governed agent execution:** run contracts, least privilege, isolated workspaces, limits, receipts, and delegation controls.
- **Strategic intervention:** optional objective, measures/guardrails, intervention hypothesis, attribution, and outcome review.

Profiles compose. Use the stricter applicable control on shared scope and keep live estate decisions outside this portable library.

## Next Routes

- Adoption sequence and troubleshooting: [adoption-playbook.md](patterns/adoption-playbook.md)
- Semantic task routing: [SEMANTIC_INDEX.md](SEMANTIC_INDEX.md)
- Build and collaboration readiness: [build-readiness.md](checklists/build-readiness.md), [collaboration-readiness.md](checklists/collaboration-readiness.md)
- Developer experience: [developer-experience-scorecard.md](checklists/developer-experience-scorecard.md)
- AI-native delivery: [ai-native-software-development-lifecycle.md](patterns/ai-native-software-development-lifecycle.md), [ai-native-sdlc-readiness.md](checklists/ai-native-sdlc-readiness.md)
- External control profiles: [revision-pinned-control-profiles.md](patterns/revision-pinned-control-profiles.md)
- Terms and sources: [glossary.md](glossary.md), [REFERENCES.md](REFERENCES.md)
