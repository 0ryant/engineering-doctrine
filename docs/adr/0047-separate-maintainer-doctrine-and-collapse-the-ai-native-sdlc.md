# ADR 0047: Separate Maintainer Doctrine From The Consumer Path And Collapse The AI-Native SDLC

- **Status:** Proposed
- **Decision date:** —
- **Recorded date:** 2026-09-03
- **Retrospective:** No
- **Responds to:** the 2026-09-03 cold-truth assessment, fix 5

## Context

Two measurements from the assessment motivate this ADR. First, the library now carries roughly 111k words of ADRs and evolution notes against roughly 93k words of principles, patterns, and checklists, and four patterns in the consumer reading path exist only to govern the library itself: [doctrine-content-lifecycle.md](../../doctrine/patterns/doctrine-content-lifecycle.md), [source-authority-and-evidence-grading.md](../../doctrine/patterns/source-authority-and-evidence-grading.md), [doctrine-library-change-harness.md](../../doctrine/patterns/doctrine-library-change-harness.md), and [doctrine-versioning-and-consumer-compatibility.md](../../doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md), together with the registers [DEPRECATED.md](../../doctrine/DEPRECATED.md) and [EVIDENCE-EXCEPTIONS.md](../../doctrine/EVIDENCE-EXCEPTIONS.md). A head of engineering evaluating the library for a team has no use for any of them and, the assessment argues, is put off by meeting them first. Second, [ai-native-software-development-lifecycle.md](../../doctrine/patterns/ai-native-software-development-lifecycle.md) runs to eighteen top-level sections and about 4,000 words; the library's own retrospective already conceded its cognitive load, and the assessment names it as the single pattern a senior reader would decline.

Both are structure problems, not content problems. Nothing in the maintainer patterns is wrong; it is in the wrong place. Nothing in the SDLC is wrong; there is too much of it in one file.

## Proposed Decision

1. **A `doctrine/maintainers/` directory** holds the four maintainer patterns and the two registers. Files move with `git mv`; every inbound link is repointed in the same commit; the sitemap, semantic index, README, and REFERENCES internal map are regenerated or edited. A one-line redirect note stays at each old path for one release, then is retired through the lifecycle. The consumer path ([doctrine/README.md](../../doctrine/README.md) Start Here, [how-to-read-this-doctrine.md](../../doctrine/patterns/how-to-read-this-doctrine.md)) gains one sentence: "If you maintain this library rather than consume it, start at `maintainers/`."

2. **The versioning pattern is split.** Its consumer-facing half (change classes, release labels, upgrade policy: §§1–5) stays in the consumer path as `patterns/consuming-doctrine-releases.md`; its maintainer half (release notes minimum, maintainer checklist: §§4, §8) moves with the others. Consumers need to know how to absorb a release; they do not need to know how to cut one.

3. **The AI-native SDLC is collapsed to its seven gates.** The replacement, at the same path, keeps: scope and non-goals; the five-minute field guide; the invariants; the seven operational gates, each with its entry condition, exit evidence, and the record it produces; a one-page crosswalk to the S0–S10 references; failure modes; and consumer impact. The claim model, transition admissibility, authority model, closure and re-entry, and the lifecycle-at-a-glance diagram move to a companion note under `evolution/` as design rationale, which is what they are. Target length: at most 1,600 words and nine sections. The gate names lose the "enactment" and "mandate class" vocabulary per [ADR 0046](0046-retire-private-vocabulary-where-a-standard-term-exists.md). The readiness checklist derived from the pattern is re-derived from the collapsed version.

4. **Word-count ratio becomes a tracked measure.** The sweep record reports normative words against maintainer-and-rationale words each sweep. No threshold is set; the number is published so the drift is visible.

## Alternatives Considered

**Leave the structure and improve the README's reading order.** Rejected. Reading order is already the README's job and the assessment reader still met the maintainer layer first, because search and the semantic index do not respect reading order.

**Delete the maintainer patterns.** Rejected. They are the reason the library can retire content at all, and ADR 0045 has now exercised them once.

**Rewrite the SDLC from scratch.** Rejected. The gates and invariants are sound; the file is a design document that was landed as a pattern. Moving the design parts to evolution is the honest fix.

**Move the SDLC design sections to a second pattern file.** Rejected. Two patterns with one applicability condition is one pattern with a page break, and the second file would accrete.

## Consequences

- Consumer-visible patterns drop by three and the longest pattern shrinks by more than half.
- Every existing link to the four maintainer patterns changes; the redirect notes absorb the churn for one release.
- The SDLC readiness checklist is re-derived, which is a checklist change class in its own right.

## Consumer Impact

**Change class:** navigation for the moves; normative replacement for the SDLC collapse, with a section-number migration table in the collapsed file's Consumer Impact; checklist update for the readiness checklist.

## Acceptance Evidence (when accepted)

- `doctrine/maintainers/` exists with the six files; no link in principles, patterns, checklists, or the umbrella points at the old paths.
- The collapsed SDLC validates the "no obligation exists only in a checklist" rule against the re-derived checklist.
- The sweep record carries the word-count ratio.

## Review Note

Drafted by an agent under the owner's direction; not yet reviewed by the owner. The SDLC collapse in particular changes what consumers cite and should not be executed without the owner reading the collapsed draft.
