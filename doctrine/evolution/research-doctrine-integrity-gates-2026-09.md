# Doctrine Integrity Gates — September 2026

Date: 2026-09-19
Status: Repository investigation and implementation basis; not normative authority.
Decision: [ADR 0049](../../docs/adr/0049-add-doctrine-integrity-gates-and-obligation-routing.md).

## Evidence And Limits

Inspection started at commit `c82af3b3ee76b6888ca0787b2edcfff65b1f8181`.
The [August review](research-full-corpus-council-review-2026-08.md) is a model
review, not proof that its historical findings still apply. The
[v0.6.0 roadmap](post-v0.3.0-external-review-decisions-and-v0.4.0-plan-2026-07.md)
retains the release acceptance criteria; this note does not waive them.

Observed repository evidence:

- ADR 0036 records earlier repairs, but the preflight and CI did not validate
  Markdown link targets or the YAML examples embedded in doctrine pages.
- The contract harness constructs schema examples independently of Markdown.
  Its passing result cannot prove that a reader's copied example parses.
- Financial-authority and synthetic-media items in AI adoption readiness, and
  the agent-memory item in AI-native SDLC readiness, were concatenated onto
  preceding checklist lines. Their intended owner links existed but their
  presentation obscured separate checks.
- Readiness lacked a single route across the controls introduced in ADRs
  0031–0035. A derived activation table can expose them without copying rules.

This is internal primary evidence for a maintenance decision. Source support for
existing consumer controls remains with their canonical owners and original
decision records. The new maintainer obligation has its separate admission below.

## Source Admission For The Maintainer Gate

Claim: obligation-changing ADRs identify their canonical owner and derived
landings, or explain why none is needed. Support is **C2**, capped at practitioner
evidence: two independently maintained documentation guides support the narrower
mechanism of relevant cross-links, one source of truth and discoverable entry
points. They do not prescribe this ADR field or prove a measured reduction in
missed obligations. The precise gate is this library's synthesis, corroborated
by its observed routing defects, not presented as an industry mandate.

**Risk asymmetry:** the cost is a short map checked during existing review; a
missing route can hide an applicable obligation from consumers without failing
syntax checks. Scope is only this library's obligation-changing ADRs, with an
explicit no-derived-landing rationale available. Review at the next lifecycle
sweep, or earlier if the map becomes duplicative; maintainer owns simplification.

| Primary source | Class, scope and pin | Supports / limits |
| --- | --- | --- |
| [Google developer documentation: cross-references](https://developers.google.com/style/cross-references) | S6 practitioner guidance, primary for its documentation practice; snapshot accessed/pinned 2026-09-19, SHA-256 `855487835614255b3c6c96b87c49bd0d389dcc0599dac9e90ec82f5bab9afc0d` | Select relevant destinations and explain link purpose; cautions against indiscriminate links. Does not require an ADR map. |
| [GitLab documentation: folder structure](https://docs.gitlab.com/development/documentation/site_architecture/folder_structure/) | S6 practitioner guidance, primary for its documentation practice; snapshot accessed/pinned 2026-09-19, SHA-256 `8fcb9ad0e36c1e2ba8cfde5878711ec8281f9998859c266f08f1db622436c1e0` | Link to one authoritative source; connect new/renamed pages from indexes and related pages. Does not establish consumer policy strength. |

These are different organisations, not two copies of one guide. Publisher pages
were accessible at admission; dated HTML captures are retained in maintainer
evidence. No durable public archive URL was obtained. Archive availability is a
maintainer follow-up at the next sweep, not a claim that the live URLs are immutable.

## Obligation-To-Readiness Map

The added **Activated Engineering Controls** table in
[AI adoption readiness](../checklists/ai-adoption-readiness.md) is a route, not an
adoption mandate. Its activation conditions and links preserve the owners below.

| Decision | Existing canonical owners | Derived landing |
| --- | --- | --- |
| ADR 0031, amended by 0032 | Zero trust §2.1: agent identity; AI/ML §7: MCP revision and tool surfaces | Identity and governed/production MCP rows; ASI crosswalk stays threat navigation |
| ADR 0032 | AI/ML §4: pre-install package gate; dependencies §7–8: adjacent package/model/dataset controls; privacy and data governance §5.4: activated transparency profile | Dependency row and existing profile-gated person-impact checks |
| ADR 0033 | Incident lifecycle §10: agent responders; observability §7: GenAI telemetry | Responder and telemetry rows; threat vocabulary stays navigational |
| ADR 0034 | Merge-path integrity §1–2: agent definitions; AI/ML §7: memory; agentic loop §8.2: binding judges | Definitions, memory and judge rows; repaired memory checklist item |
| ADR 0035 | Cost §7/7.1: spend and financial authority; testing §5: adaptive evaluation | Spend, authority and adaptive-evaluation rows; repaired financial and synthetic-media items |

Delete the derived route and the obligation still exists at its owner. A route
does not change a `SHOULD` into a `MUST` or activate a control outside its scope.

## Verification Boundaries

| Check | Can establish | Cannot establish |
| --- | --- | --- |
| Local Markdown targets | Referenced tracked-document targets exist; umbrella fragments resolve | Other-file fragments, external URL health, meaning of the destination |
| Embedded YAML parsing | The printed YAML parses; owned complete instances fit their declared schema | Runtime operations, effectiveness of a control, completeness of an excerpt |
| Existing contract/skill harnesses | Their schema, negative and consistency cases pass | All prose agrees with its canonical owners |
| Model reader/reviewer | Defects noticed by that model under a recorded scenario | Human comprehension, elapsed reader time, independent domain approval |

Human cold-reader verification remains explicitly open. The operator elected
to use model walkthroughs to find defects, not to relabel them as human evidence.

## Follow-Up

Run direct example and link gates alongside existing harnesses. Keep release
closeout, semantic challenge, canonical-owner consolidation and human usability
separate from this integrity decision. Passing these checks alone is not a
v0.6.0 release verdict.
