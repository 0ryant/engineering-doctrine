# ADR 0036: Land v0.5.0 Correction Batch From The Corpus Review

- **Status:** Accepted
- **Decision date:** 2026-08-03
- **Recorded date:** 2026-08-03
- **Retrospective:** No

## Context

The [full-corpus council review at v0.4.0](../../doctrine/evolution/research-full-corpus-council-review-2026-08.md) confirmed 2 blockers and 20 majors. Its §6 routes most majors to forward-plan lanes (V41 typing retrofit, canonical-home consolidation ADR, V45/D12 flag supersession, machine-verdict precedence ADR). This ADR lands the **correction batch** — the subset that is corrective rather than structural: both blockers (one interim), the schema-derived-fact repairs, the umbrella-reference sweep, and the checklist/inventory reconciliation, satisfying v0.5.0 acceptance criteria 1 (interim half) and 2 as recorded in the [forward plan](../../doctrine/evolution/post-v0.3.0-external-review-decisions-and-v0.4.0-plan-2026-07.md).

Council provenance: 5-item draft council (prep + draft per item), two critics (fidelity/correction-class discipline; coherence/reader impact) — zero blockers or majors in critique; 9 minors, all applied. The M9 replacement example was schema-validated three times: by the drafter, independently by the fidelity critic, and in situ after application.

## Decision

1. **B2 + M20 + M21 (observability).** The burn-rate YAML is corrected (recording rules authored for **all four** alert windows; every aggregation `sum by (job)`, fixing the naming prefix and empty `$labels.job`) and moved wholesale to [tooling/observability.md](../../doctrine/tooling/observability.md) as "Burn-Rate Alerting (Prometheus-Compatible Backends)" with an explicit missing-rules trap warning. The principle keeps §§6.1–6.4 backend-neutral; §6.3 becomes a pointer stub so §6.4 keeps its number (ratified reading of "move wholesale": content moves, slot preserved). §6 gains typed applicability — production services with SLOs **SHOULD** use multi-window burn rate; low-traffic services **MAY** use a single tier with recorded reason — and the threshold table is EXAMPLE class.
2. **B1 interim (feature-flag FSM).** The unresolvable instruction set is repaired minimally: `stabilize → active` is the one permitted reversal (recorded reason; stabilize clock restarts on re-promotion); the targeting freeze narrows to `cleanup` with an incident-review escape; the unqualified no-backwards sentence and the new-flag remedy are deleted; the ASCII diagram gains a reversal caption. Deliberately **untyped**, matching the file's register — full typing, canonical-home wiring, and de-vendoring remain with the V45/D12 supersession ADR, now cross-linked from the file.
3. **M7 + M8 + M9 (schema-derived facts).** Verifier-kind counts become count-free everywhere except §3, which names the schema enum as authoritative; run-contracts' "eleven top-level keys" statements are removed in favour of count-free phrasing; the anti-confabulation §5 example is replaced with a pack that validates against `verifier-pack.v1.schema.json` (Draft 2020-12). Noted for V47: the §4 run-contract *fragment* (pre-existing, deliberately partial) will need a fragment-marking convention before example validation is mechanised in CI, and README/REFERENCES rows that hardcode "11 canonical kinds" join the same recurrence class.
4. **M15 (+ sweep).** Twelve references into vanished umbrella ENGINEERING.md content are repointed to current canonical homes (the nine known-rotted files plus three sweep additions ratified by the council: trunk-workflow, adoption-playbook, timeless-principles-and-tooling); ENGINEERING.md's compatibility note is updated for v0.4.0. The CI anchor check remains the V48 deliverable.
5. **M3 + M4 + M6 + navigation (reconciliation).** The AI inventory gains a **Financial / transaction authority** row (default none; grant record, approver, caps, expiry, dedicated principal); ai-adoption-readiness gains the default-deny, agent-hijack adaptive-evaluation (trigger wording matched to testing-strategy §5), and synthetic-media re-test items; ai-native-sdlc-readiness gains the composite memory-lifecycle overlay item; README lists the four previously omitted first-class files; SEMANTIC_INDEX gains a cost-governance route reaching cost-and-finops §7/§7.1. M4 drift provenance corrected per the review: ADR 0035 (245249d) and the ADR 0023 audit-fix (7f107cc), not ADR 0033.

## Consequences

**Positive:** copy-pasted burn-rate alerting now fires; the corpus's only unresolvable instruction set is resolved; schema-fact drift is eliminated at its current instances; a Tier-D team following published routes now reaches the financial default-deny, memory-lifecycle, and adaptive-evaluation duties.

**Costs and risks:** the §6.3 pointer stub and B1 interim text are transitional shapes that V45/D12 and the M20 follow-through will supersede; the M7/M8 recurrence class is fixed by hand pending V47 mechanisation.

## Consumer Impact

**Change class:** corrective/editorial for the majority; two scoped normative deltas — the §6 burn-rate SHOULD/MAY typing (an obligation-clarification, previously untyped prose) and the B1 interim transition rule (replaces contradictory text; permissive relative to the impossible prior state). No consumer becomes newly non-compliant.

**Compatibility proposal:** pre-1.0 minor content, ships with `v0.5.0`.

## Acceptance Evidence

- All 42 council edits applied with per-edit anchor assertions; 6 insert-seam defects caught and repaired during application; both critics' 9 minors applied.
- Contracts validation gate green post-application; the M9 example validates in situ against the pack schema.
- Corpus-review tasks B1(interim)/B2/M3/M4/M6/M7/M8/M9/M15/M20/M21 tracked to completion in the session task register; remaining majors stay open under their routed lanes.

**Review provenance:** the council review cited above was model self-review (agent critics re-reading agent drafts). No independent human or domain review of this ADR has been recorded as of 2026-09-03.
