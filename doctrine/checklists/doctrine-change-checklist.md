# Doctrine Change Checklist

Use when **adding or substantially editing** files under `doctrine/` or the umbrella `ENGINEERING.md`.

```text
[ ] For substantive additions: follow patterns/doctrine-library-change-harness.md (research → ADR → layers → navigation)
[ ] ADR: new docs/adr/NNNN-*.md + docs/adr/README.md index row, or explicit reference to existing ADR; skip only for pure editorial (note in PR)
[ ] Research: external citations and/or doctrine/evolution/ note linked from the change or ADR when non-trivial
[ ] Research distinguishes binding external requirements, official guidance, observations, and repository synthesis; source revisions and limits are recorded where material
[ ] New citations supporting typed claims record source class, pin-or-rolling choice, and accessed date; archived copy captured where tooling permits (patterns/source-authority-and-evidence-grading.md §6)
[ ] Typed claims meet their admission floor — MUST at C1, or C2 with recorded risk asymmetry, or a registered exception in doctrine/EVIDENCE-EXCEPTIONS.md; conformance claims satisfied by their pinned norm (patterns/source-authority-and-evidence-grading.md §4–§5)
[ ] Promotion to typed standing re-admits evidence at the higher floor: re-fetch, re-grade, rolling converted to pinned, publisher status checked (patterns/doctrine-content-lifecycle.md §2)
[ ] Sweep-facing changes: reference-status leg run for the cohort (publisher status, link health, diagonal-collapse audit) and EVIDENCE-EXCEPTIONS entries re-examined (patterns/doctrine-content-lifecycle.md §8)
[ ] Change belongs in principles (durable topic authority) vs patterns (conditional operating model) vs checklists (derived review) vs tooling (illustrative) vs estates (optional supplement) — see principles/timeless-principles-and-tooling.md
[ ] Portability: no organisation-private products, portfolio tools, internal repositories, local paths, or programme artefacts appear in publishable files
[ ] If principle changed: rationale and references updated; not just opinion
[ ] Each material claim has a claim-level strength/content class, explicit applicability, expected evidence, and exception authority; no document-wide normative level is being inferred
[ ] Applicability composes baseline, named profiles, and binding external authority without making a specialised profile universal
[ ] Exception text is narrower and time-bounded, records accountable authority and compensating action, and does not turn failed, missing, or inconclusive evidence into a pass
[ ] New or expanded controls name the failure addressed, evidence, owner, operating cost, review trigger, and simplification or retirement path
[ ] If umbrella ENGINEERING.md changed: it remains a compact constitution and route map; detailed obligations have one canonical principle or pattern owner and are linked rather than copied
[ ] Cross-links added from related principles/patterns (avoid orphan pages)
[ ] Checklists derive prompts from an owning principle or pattern; no new obligation exists only in a checklist
[ ] REFERENCES.md internal map updated if new first-class doc
[ ] doctrine/SITEMAP.md regenerated: ./scripts/generate-doctrine-sitemap.sh
[ ] Skills: python scripts/validate-skills.py passes (manifest schema, priming-block hash, sibling verifier pack, governing paths, review date) and doctrine/skills/README.md register updated (patterns/agent-doctrine-consumption.md §3)
[ ] doctrine/README.md Start Here or section lists updated when files are added/removed
[ ] Checklists updated if new obligation for adopting teams
[ ] At least three materially different consumers or change classes were sampled to test applicability and evidence expectations
[ ] Duplicate or conflicting normative owners were searched for and reconciled; evolution notes are not used as operating authority
[ ] Change class labelled for consumer impact: editorial / navigation / additive guidance / normative tightening / normative replacement / estate-only / deprecation
[ ] Migration notes added for normative tightening, replacement, deprecation, or removal
[ ] Lifecycle: supersession, demotion, or retirement routed per [../patterns/doctrine-content-lifecycle.md](../patterns/doctrine-content-lifecycle.md); doctrine/DEPRECATED.md updated
[ ] evolution/moscow-review.md or decision note updated for large shifts (optional but encouraged)
[ ] evolution/honest-review-synthesis.md updated when absorbing a substantive external review of the library
[ ] For material doctrine releases: update [CHANGELOG.md](../../CHANGELOG.md) at the tag; note version or date in evolution/moscow-review.md or a short decision log entry (optional but encouraged); classify release kind using patterns/doctrine-versioning-and-consumer-compatibility.md
```
