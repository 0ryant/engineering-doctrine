# Skills Register

Skills are the agent-facing surface of this library: small, hash-pinned priming
artefacts that derive from named doctrine and ship with a sibling verifier
pack. The contract is [patterns/agent-doctrine-consumption.md](../patterns/agent-doctrine-consumption.md)
§3; the manifest schema is [contracts/skill.v1.schema.json](../../contracts/skill.v1.schema.json);
the validator is `scripts/validate-skills.py`. Rationale: [ADR 0044](../../docs/adr/0044-adopt-agent-facing-consumption-contract-skill-schema-and-server-boundary.md).

Layout is fixed by [patterns/verifier-packs.md §6](../patterns/verifier-packs.md):
`doctrine/skills/<name>/SKILL.md` beside `doctrine/skills/<name>/verifier-pack.yml`.
A skill without a pack is inadmissible. Skills are advisory only; authority
stays with the governing files and with independent verification.

## Tiers

| Tier | Meaning | Injection default |
| --- | --- | --- |
| 0 | Always-on primers: reading and citing the library correctly | `estate-policy` |
| 1 | Agent change-lifecycle procedures: every agent-assisted change passes through them | `estate-policy` on the producing task class |
| 2 | Readiness assessments derived from an owning checklist | `explicit-only` |
| 3 | Design-time specialists | `explicit-only` |

## Active Skills

| Skill | Version | Tier | Kind | Governing | Pack |
| --- | --- | --- | --- | --- | --- |
| [anti-confabulation](anti-confabulation/SKILL.md) | 1.1.0 | 0 | primer | [anti-confabulation-priming.md](../patterns/anti-confabulation-priming.md) | [pack](anti-confabulation/verifier-pack.yml) |
| [doctrine-navigation](doctrine-navigation/SKILL.md) | 1.0.0 | 0 | primer | [how-to-read-this-doctrine.md](../patterns/how-to-read-this-doctrine.md), [timeless-principles-and-tooling.md](../principles/timeless-principles-and-tooling.md) | [pack](doctrine-navigation/verifier-pack.yml) |
| [normative-language-reading](normative-language-reading/SKILL.md) | 1.0.0 | 0 | primer | [normative-language-applicability-and-exceptions.md](../patterns/normative-language-applicability-and-exceptions.md) | [pack](normative-language-reading/verifier-pack.yml) |
| [evidence-graded-citation](evidence-graded-citation/SKILL.md) | 1.0.0 | 0 | primer | [source-authority-and-evidence-grading.md](../patterns/source-authority-and-evidence-grading.md) | [pack](evidence-graded-citation/verifier-pack.yml) |
| [method-record-classification](method-record-classification/SKILL.md) | 1.0.0 | 1 | procedure | [code-review-and-change-approval.md §6.1](../patterns/code-review-and-change-approval.md), [ADR 0043](../../docs/adr/0043-replace-agent-coauthorship-disclosure-with-a-method-record.md) | [pack](method-record-classification/verifier-pack.yml) |

None of the active skills ships a portable evaluation; every manifest says so
(`evaluation.evidence: null`). Hosts SHOULD treat them as experimental for their
own cell until an estate evaluation exists (anti-confabulation-priming.md §6).

## Roadmap

Candidates are listed so that the derivation is visible before the file exists.
A roadmap row is not a skill: nothing here may be cited, injected, or pinned
until it has a manifest, a pack, and a green validator run. Each row names its
owning doctrine so the skill cannot drift from it.

| Tier | Candidate | Kind | Would derive from |
| --- | --- | --- | --- |
| 1 | dependency-preinstall-verification | procedure | [ai-ml-systems.md §4](../principles/ai-ml-systems.md), [dependencies-supply-chain.md §7](../principles/dependencies-supply-chain.md) |
| 1 | run-contract-compilation | procedure | [run-contracts.md](../patterns/run-contracts.md), [contracts/run-contract.v1.schema.json](../../contracts/run-contract.v1.schema.json) |
| 1 | verifier-pack-emission | procedure | [verifier-packs.md](../patterns/verifier-packs.md), [contracts/verifier-pack.v1.schema.json](../../contracts/verifier-pack.v1.schema.json) |
| 1 | agent-pr-review-readiness | procedure | [code-review-and-change-approval.md §6](../patterns/code-review-and-change-approval.md), [merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md) |
| 1 | trunk-and-branch-hygiene | procedure | [trunk-workflow.md](../patterns/trunk-workflow.md), [collaboration.md](../principles/collaboration.md) |
| 2 | build-readiness-assessment | assessment | [checklists/build-readiness.md](../checklists/build-readiness.md) via [build.md](../principles/build.md) |
| 2 | release-readiness-assessment | assessment | [checklists/release-readiness.md](../checklists/release-readiness.md) via [semantic-versioning.md](../principles/semantic-versioning.md), [feature-flag-lifecycle.md](../patterns/feature-flag-lifecycle.md) |
| 2 | platform-readiness-assessment | assessment | [checklists/platform-readiness.md](../checklists/platform-readiness.md) via [platform-engineering.md](../principles/platform-engineering.md) |
| 2 | collaboration-readiness-assessment | assessment | [checklists/collaboration-readiness.md](../checklists/collaboration-readiness.md) via [collaboration.md](../principles/collaboration.md) |
| 2 | ai-adoption-readiness-assessment | assessment | [checklists/ai-adoption-readiness.md](../checklists/ai-adoption-readiness.md) via [ai-adoption-controls.md](../patterns/ai-adoption-controls.md) |
| 2 | ai-native-sdlc-readiness-assessment | assessment | [checklists/ai-native-sdlc-readiness.md](../checklists/ai-native-sdlc-readiness.md) via [ai-native-software-development-lifecycle.md](../patterns/ai-native-software-development-lifecycle.md) |
| 2 | governance-program-readiness-assessment | assessment | [checklists/governance-program-readiness.md](../checklists/governance-program-readiness.md) via [engineering-controls-governance-program.md](../patterns/engineering-controls-governance-program.md) |
| 2 | developer-experience-scorecard | assessment | [checklists/developer-experience-scorecard.md](../checklists/developer-experience-scorecard.md) via [developer-experience.md](../principles/developer-experience.md) |
| 2 | doctrine-change-readiness | assessment | [checklists/doctrine-change-checklist.md](../checklists/doctrine-change-checklist.md) via [doctrine-library-change-harness.md](../patterns/doctrine-library-change-harness.md) |
| 3 | stride-lite-threat-model | design | [threat-modeling-stride-lite.md](../principles/threat-modeling-stride-lite.md) |
| 3 | idempotency-boundary-review | design | [idempotency-across-boundaries.md](../patterns/idempotency-across-boundaries.md) |
| 3 | event-contract-design | design | [event-contracts.md](../principles/event-contracts.md), [tooling/cloudevents.md](../tooling/cloudevents.md) |
| 3 | feature-flag-lifecycle-review | design | [feature-flag-lifecycle.md](../patterns/feature-flag-lifecycle.md) |
| 3 | state-machine-and-workflow-review | design | [state-machines-and-workflows.md](../principles/state-machines-and-workflows.md) |
| 3 | webhook-ingress-review | design | [webhook-ingress-security.md](../patterns/webhook-ingress-security.md) |

## Adding A Skill

1. Create `doctrine/skills/<name>/SKILL.md` with front matter per the schema and
   the six required body sections in order: Purpose, Instructions (containing
   exactly one ```` ```priming ```` block of at most 4096 bytes), Run-Contract
   Use, Required Independent Checks, Failure Handling, Limits.
2. Create `doctrine/skills/<name>/verifier-pack.yml` with at least a
   `priming_active` assertion whose command is
   `python ${DOCTRINE_ROOT}/scripts/validate-skills.py assert-primed --skill <name> --prompt ${RENDERED_PROMPT}`,
   plus assertions that observe the behaviour the block asks for.
3. Pin the hash: `python scripts/validate-skills.py hash --skill <name>`.
4. Run `python scripts/validate-skills.py` and the doctrine preflight; add the
   row above; follow [checklists/doctrine-change-checklist.md](../checklists/doctrine-change-checklist.md).
5. Any later byte change to the priming block bumps the version and the hash.
   Deprecation and retirement follow [patterns/doctrine-content-lifecycle.md](../patterns/doctrine-content-lifecycle.md).
