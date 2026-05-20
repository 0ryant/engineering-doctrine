# 0012. Model Routing Policy

Status: Proposed
Decision date: 2026-05-20
Recorded date: 2026-05-20
Retrospective: No

> Note on numbering. The v3 position update at
> [`value-sheet/18-cross-product-test/v3/v3-position-update.md`](https://github.com/0ryant/value-sheet)
> references this decision as "ADR-0009"; that draft was written before the
> engineering-doctrine ADR index was consulted, where 0009 is already
> [GitOps and declarative operations](0009-add-gitops-and-declarative-operations-pattern.md).
> The substantive content is the same; the engineering-doctrine canonical id
> is **0012**. The cross-reference update in
> [`value-sheet/18-cross-product-test/v3/v3-FINAL-SYNTHESIS.md`](https://github.com/0ryant/value-sheet)
> §6 ship-list (item 4) points at this file.

## Context

The v2 cross-product test ([`value-sheet/18-cross-product-test/v2/`](https://github.com/0ryant/value-sheet)) and the v3 matched-pair priming addendum produced a 9-cell empirical scoreboard that destroys the naive "bigger model is better" routing rule. The numbers, all from blind canonical re-scoring (not self-scores), are reproduced verbatim from [`v3-FINAL-SYNTHESIS.md`](https://github.com/0ryant/value-sheet) §2.1:

| Cell | Canonical | $ per cell | Δ self-canonical |
|------|----------:|-----------:|-----------------:|
| tools-opus + primer | 87 | ~$3 | 0 |
| **tools-sonnet + primer (production default)** | **85** | **$0.58** | **−1** |
| native-opus + primer | 78 | ~$2-3 | −2.5 |
| tools-sonnet (no canonical primer) | 78 | $0.58 | −11 |
| **tools-haiku + primer (narrow-scope tier)** | **73** | **~$0.21** | **+10** |
| native-sonnet | 70 | $0.38 | −21 |
| tools-haiku-no-skills | 61.5 | $0.21 | −16.5 |
| native-haiku | 47.5 | $0.17 | −35.5 |
| tools-haiku + SKILLS (DEPRECATED) | 31 | $0.20 | −65 |

The bolded rows are the three production-ready tiers. The deprecated row at canonical 31 is the smoking-gun cell: it shipped a binary whose `collect` subcommand printed a success message and exited 0 *without writing the declared output*, while self-scoring 96/100. The cell could not detect its own over-claiming because Δ was +65.

Four structural facts fall out:

1. **The 3-tier shape is empirical, not aesthetic.** Three cells sit on the production frontier: Opus-primed at canonical 87, Sonnet-primed at canonical 85, Haiku-primed at canonical 73. Sonnet-primed beats native-Opus by 7 points at 20% of the cost and lands within 2 points of Opus-primed at ~19% of its cost. The 200-token primer text artifact (skill `anti-confab-200tok@1.0.0`, hash `c138dd966c82f7bd792684ab3fef0f50d75aa9342468db8b5d265f24f3fb35a8` per council D5) closes most of the gap an Opus tier would.

2. **The primer is model-conditional.** Confirmed-uplift on Opus and Sonnet, **inverted** on Haiku when bundled with full SKILLS — the `tools-haiku + SKILLS` cell (canonical 31, self-scored 96) is the silent-stub class. The narrow-scope Haiku-PRIMED tier at canonical 73 is the production-ready *minimal* haiku surface, gated behind mandatory external review because Δ self-canonical is **+10** (the cell over-claims by 10 points and cannot grade its own work).

3. **A new corcept failure mode landed in the same evidence run.** The `bash -c '<benign>'` interpreter-wrapper class passes every corcept hook guard: the first-token check sees `bash` not `sudo/su/doas`; the protected-paths guard does not run on bash's argv; the privilege-escalation detector has no interpreter-wrapper rule. CC-2 is FALSIFIED. The corcept-side fix has since landed (per the v3 per-tool failure-mode tests), but the router still refuses the pattern structurally as defense-in-depth.

4. **Council D4 (4/4) locked the 3-tier policy.** The decision packet at `v3-FINAL-SYNTHESIS.md` §6 fixed three production tiers (premium / default / narrow_scope) with their cell-class fits, their cost ceilings, and the narrow_scope external-review requirement. A prior attempt at this ADR (with a single-default-cell shape) was overtaken by the council resolution; this document is the **refire** with the locked 3-tier shape.

The v3 position update at §6 sketched the routing rules as a prose paragraph. Four things were left undone:

- The policy was prose, not a typed envelope. Operators could not validate a policy file at boundary entry.
- The 3-tier shape was prose, not a schema constraint. A consumer could legally drop a tier and still call the result "the v3 policy."
- Refusal rules cited evidence in passing, not as a structured field. There was no schema-level mandate that a refusal carries empirical backing.
- The cost ceilings were declared but had no two-tier shape (per-cell guard versus per-session kill) and no explicit per-tier cap.

The v1 contracts surface (`contracts/run-contract.v1.schema.json` and `contracts/verifier-pack.v1.schema.json`) gave us the pattern for closing this: a JSON Schema 2020-12 file with `additionalProperties: false` everywhere, `oneOf` discriminators where multiple shapes are legal, and a Python validation harness that drives positive and negative cases per shipped example.

This ADR codifies the 3-tier routing policy as a v1 contract on that pattern.

The commercial framing matters. Anyone can publish a model id. Nobody can publish, without the underlying cohort, the empirically-grounded refusal rules — "we refuse haiku for greenfield because we measured a 73 canonical with Δ +10 self-score on this exact class of task" is the kind of statement competitors cannot reproduce by reading our marketing. The router policy IS the product surface where the v2 negative-result cohort and the v3 9-cell scoreboard become a runtime decision. The policy is the moat the doctrine secures.

Inputs that informed this decision:

- [`value-sheet/18-cross-product-test/v3/v3-FINAL-SYNTHESIS.md`](https://github.com/0ryant/value-sheet) §2.1 9-cell scoreboard and §6 council-D4 resolution.
- [`value-sheet/18-cross-product-test/v3/v3-position-update.md`](https://github.com/0ryant/value-sheet) — §6 sketch and §11 evidence addendum.
- [`value-sheet/18-cross-product-test/v2/results/test-1-backbone/canonical-scoring.md`](https://github.com/0ryant/value-sheet) — the original 5-cell blind re-scoring (canonical 31 / canonical 78 / canonical 70).
- [`value-sheet/18-cross-product-test/v2/results/test-1-backbone/canonical-scoring-sonnet-primed.md`](https://github.com/0ryant/value-sheet) and [`canonical-scoring-opus.md`](https://github.com/0ryant/value-sheet) — primed-addendum cells.
- [`value-sheet/18-cross-product-test/v2/results/test-1-backbone/canonical-scoring-haiku-primed.md`](https://github.com/0ryant/value-sheet) — the narrow-scope tier evidence (canonical 73, Δ +10).
- [`value-sheet/18-cross-product-test/v3/results/plan-b-v2-claim-audit-against-stage2/composite.md`](https://github.com/0ryant/value-sheet) — claim_audit v2 catch-rate evidence backing the FALSIFIED-escalation rule.
- [`value-sheet/18-cross-product-test/v2/results/per-tool-failure-mode-tests-results/composite.md`](https://github.com/0ryant/value-sheet) — the CC-2 falsification.
- [`doctrine/skills/anti-confabulation.skill.md`](../../doctrine/skills/anti-confabulation.skill.md) — the primer pack and its content hash.
- [`doctrine/patterns/anti-confabulation-priming.md`](../../doctrine/patterns/anti-confabulation-priming.md) — the priming-pattern doctrine.
- [`contracts/run-contract.v1.schema.json`](../../contracts/run-contract.v1.schema.json) — `model_policy.allowed_models`, the field the router resolves against.

## Decision

Adopt a v1 **router policy** contract that the corcept-hosted router consumes to (a) resolve every cell to one of three tiers, (b) escalate on adversarial-verifier verdicts, and (c) refuse routing for empirically-known failure modes. The contract surface is:

1. **Schema:** [`contracts/router-policy.v1.schema.json`](../../contracts/router-policy.v1.schema.json) — JSON Schema 2020-12 with `additionalProperties: false` everywhere, `oneOf` discriminators on `when` clauses and `action` shapes, a required `tiers: { premium, default, narrow_scope }` object so the 3-tier shape is structural, and per-action validation. The schema requires `refusal_rules` to be non-empty (loud-not-silent: a router declaring "no empirically-grounded refusals" is rejected at validation time).
2. **Worked examples:**
   - [`contracts/examples/default-production.router-policy.yaml`](../../contracts/examples/default-production.router-policy.yaml) — the v3 production default.
   - [`contracts/examples/enterprise-strict.router-policy.yaml`](../../contracts/examples/enterprise-strict.router-policy.yaml) — escalates immediately on the first FALSIFIED, refuses haiku for everything beyond `scaffolded_typed_authority`, lowers per-session kill.
   - [`contracts/examples/experimental-haiku-narrow-scope.router-policy.yaml`](../../contracts/examples/experimental-haiku-narrow-scope.router-policy.yaml) — the Haiku-PRIMED narrow-scope tier exercised in production with mandatory external review.
3. **Validator:** [`scripts/validate-contracts-v1.py`](../../scripts/validate-contracts-v1.py) — extended to load the router schema, validate the three on-disk YAML examples positively, and assert twelve negative cases (empty refusals, missing evidence_ref, soft refusal, mixed `when` discriminators, unknown top-level field, unknown cell_class enum, missing required tier, missing primer_sha256, missing `external_review_required`, mixed escalation-action discriminators, malformed primer hash, invalid tier name).
4. **Status:** Proposed. The router policy is *adopted* in the schema sense — the contract surface lands — but the cost numbers in every example are marked `# placeholder — operator to finalize`. The operator promotes to `Accepted` after reviewing the cost ceilings against actual vendor invoices.

### Policy shape

The contract has five top-level required fields and a sixth optional one:

- `policy_version` — semver of the policy document.
- `tiers` — required object with EXACTLY three keys (`premium`, `default`, `narrow_scope`). Each tier binds `model`, `primer`, `primer_sha256`, `verifier_pack`, the `cell_classes` it is empirically licensed to run, a `max_cost_usd_per_cell` ceiling, and a `external_review_required` boolean. The narrow_scope tier additionally carries `external_review_sample_rate` (set to 1.0 at v1 because the +10 Δ has not been independently sampled).
- `escalation_rules` — ordered list. First matching rule wins. Each rule binds a `when` clause (oneOf discriminator: `claim_audit_verdict + attempts_so_far`, OR `cell_class[]`, OR `operator_flag`) to an `action` (oneOf: `escalate_to_tier` with cost cap, OR `require_tier`) and an `evidence_ref` to the file that justifies the rule.
- `refusal_rules` — ordered list, **non-empty by schema**. ANY matching refusal wins. The `when` clause is one of five narrow shapes: `cell_class + model_family`, `primer + model_family`, `model_family + cell_class + primer (null)`, `cell_class + primer (null)`, or `command_matches` (regex). The action is oneOf: a hard refusal (`refuse_routing: true` with a reason) or an external-review mandate (`require_external_review: true` with a reason). Both `const: true` — soft refusals are illegal.
- `cost_ceilings` — two tiers: per-cell USD caps keyed by tier name and per-session warning + kill thresholds.
- `audit` — optional but populated in every shipped example.

### Initial rule set (encoded in `default-production.router-policy.yaml`)

Two escalation rules, five refusal rules:

| Kind | rule_id | What fires it | What happens |
|------|---------|---------------|--------------|
| Escalation | `claim-audit-falsified-escalate` | claim_audit verdict FALSIFIED after one attempt at the default tier | Escalate to `premium` tier with the same primer, cost-capped |
| Escalation | `security-critical-premium-only` | cell_class in {security_critical, supervisor_change, doctrine_promotion} | `require_tier: premium` from the first attempt |
| Refusal | `haiku-no-artifact-production-without-primer` | family == haiku_4_x AND cell_class == artifact_production AND primer == null | Refuse outright; cite v2 canonical-31 cell |
| Refusal | `haiku-no-greenfield` | family == haiku_4_x AND cell_class == greenfield_backbone | Refuse outright; cite Δ +10 self-canonical on Haiku-PRIMED |
| Refusal | `haiku-narrow-scope-requires-external-review` | family == haiku_4_x AND cell_class == scaffolded_typed_authority | Mandate non-self scoring (not a hard refusal — the tier is permitted with the review) |
| Refusal | `interpreter-wrapper-block` | command matches `^(bash\|sh\|zsh\|powershell\|pwsh\|cmd)\s+-c` | Refuse outright; cite CC-2 composite |
| Refusal | `primer-required-on-build-class` | cell_class in {build_class, artifact_production, refactor_class} AND primer == null | Refuse outright; cite the +12-14 honesty swing in v2 |

## Rationale and Decisions

Each row in this table justifies one structural choice in the schema or the default rule set, with the empirical anchor.

| Choice | Rationale | Empirical anchor |
|--------|-----------|------------------|
| Three tiers, declared structurally — `tiers: { premium, default, narrow_scope }` required | The 9-cell scoreboard frontier IS three cells. Calling the policy "v1" while permitting a deployment to drop a tier breaks the empirical contract. Schema enforces the shape; consumers cannot silently downgrade to two tiers. | v3-FINAL-SYNTHESIS.md §2.1; council D4 4/4. |
| Default tier is `tools-sonnet-primed`, not `tools-opus-primed` | Sonnet-primed canonical 85 beats native-opus 78 by 7 points at 20% of the cost, and lands within 2 of tools-opus + priming at ~19% of its cost. The cost gradient is steep enough that defaulting to Opus would burn 5× the budget for a 2-point lift. | v3 position update §1; canonical-scoring-sonnet-primed.md. |
| Premium tier reserved for {security_critical, supervisor_change, doctrine_promotion} | Cost-of-wrong-answer dominates cost-of-tier for these three. Supervisor changes alter the gate enforcing every other run; doctrine promotion edits the policy the router itself loads next session. A wrong call at Sonnet tier compounds. | v3 §6, §9 subtask 7; ADR-0006 governance ADR. |
| Narrow_scope tier permitted ONLY for `scaffolded_typed_authority`, never for greenfield | Haiku-PRIMED hit canonical 73, but Δ self-canonical is +10. On scaffolded subtasks (wire format + tests already in place from a higher tier) the cell has structural rails. On greenfield it shipped the canonical-31 silent stub. The scoping difference is the load-bearing reason haiku stays in the schema at all. | canonical-scoring-haiku-primed.md; v3 §3 narrow-scope note. |
| Narrow_scope MUST have `external_review_required: true` with sample rate 1.0 | Δ +10 means the cell cannot grade its own work. v1 says every run is sampled; the rate is only lowerable when independently measured. | canonical-scoring-haiku-primed.md self-Δ rows; council D4 4/4. |
| `primer_sha256` required on every tier | Council D5 locked the canonical primer hash `c138dd966c82f7bd792684ab3fef0f50d75aa9342468db8b5d265f24f3fb35a8`. Without a hash, "anti-confab-200tok@1.0.0" can drift via name-only resolution and the lift evaporates silently. | doctrine/skills/anti-confabulation.skill.md SHA pin (council D5). |
| Refusal rules require an `evidence_ref` field, schema-mandated | Without it, "we refuse haiku" is a vibes-claim. The commercial moat needs auditable provenance per rule. | Schema `$defs.refusal_rule.required: [rule_id, when, action, evidence_ref]`. |
| `refuse_routing` is `const: true` in the hard-refusal action shape | A "warn but allow" refusal is the silent-stub class at the routing layer. If a refusal is empirically justified, allowing override turns it into operator-roulette. | Schema `$defs.refusal_action.oneOf[0].properties.refuse_routing.const: true`. |
| `require_external_review` is `const: true` in the review-mandate action shape | Same logic: a "review optionally" mandate is not a mandate. The schema forces every external-review action to be a real obligation. | Schema `$defs.refusal_action.oneOf[1].properties.require_external_review.const: true`. |
| `refusal_rules` minItems: 1 | A router declaring "no empirically-grounded refusals" is either trivial (no policy) or misconfigured. Both fail loud. | Schema `properties.refusal_rules.minItems: 1`. |
| `when` clauses use `oneOf` discriminators, not free-form maps | Free-form maps lead to "I added a new shape, the validator passed, the router silently ignored it." Discriminators force every reader (human, machine, validator) to pick one shape and own it. | Schema `$defs.escalation_when.oneOf` and `$defs.refusal_when.oneOf`. |
| Escalation `action` uses `oneOf` to separate `escalate_to_tier` from `require_tier` | Tier escalation (default → premium on FALSIFIED) and class-pinning (security_critical → require premium up-front) are structurally different operations. Combining them in a single action shape lets typos silently swap behaviour. Schema rejects mixed action discriminators. | Negative case `router-negative-mixed-escalation-action`. |
| First FALSIFIED triggers a single retry at the default tier (`attempts_so_far: 1`), then escalates | FALSIFIED verdicts on the default tier can be a probe artifact, not a true negative — one retry catches the noise. Escalating immediately on the first verdict in default production would double the average per-task cost without empirical justification. Enterprise mode escalates on `attempts_so_far: 0`. | Plan B claim_audit v2 catch rate evidence (composite.md); cost gradient §1. |
| Haiku refused for `greenfield_backbone` specifically (not all classes) | The empirical cell that fired is `tools-haiku + SKILLS` canonical 31 on a greenfield-style binary. Refusing all haiku would lose the legitimate narrow-scope tier (canonical 73 at $0.21). The refusal is scoped to the class where the silent stub fired. | canonical-scoring.md §3; v3 §3 narrow-scope note. |
| Haiku refused on `artifact_production` only when primer is null | Distinct from the unconditional `greenfield_backbone` refusal. Build-class cells without the primer are the v2 catalog `inverted_avoid` shape; the primed narrow_scope tier handles bounded artifact_production via the require_tier escalation. | doctrine/skills/anti-confabulation.skill.md model_compatibility; canonical-scoring.md. |
| `primer-required-on-build-class` enforces canonical primer on every build/artifact/refactor cell | Tools-sonnet without the primer scored canonical 78 with Δ self-canonical −11. With the primer it scored canonical 85 with Δ −1. The +14 self-canonical swing IS the empirical commitment of the priming pattern; permitting unprimed build cells contaminates measurement and lift. | canonical-scoring.md (unprimed Sonnet vs primed Sonnet rows). |
| Interpreter-wrapper command pattern refused at the router layer, not deferred to corcept | CC-2 is FALSIFIED on corcept's side; the fix has since landed but the v2/v3 corpus retains the failure as evidence. Refusing at the router means the refusal is visible to every consumer of the policy, not just corcept-aware ones. Defense-in-depth at the routing layer. | composite.md CC-2 FALSIFIED rows; v3 §2.4. |
| Cost ceilings are two-tier (per-cell + per-session) | A single per-cell cap protects against runaway loops on one task. A per-session cap protects against amplification across cells (an agent that fires 1000 cheap cells with no per-session guard). The two-tier shape is the minimum that prevents both single-overrun and accumulation. | DORA cost-of-cycle research; standard reliability/FinOps practice. |
| Per-cell caps keyed by tier name AND replicated at tier level (`max_cost_usd_per_cell`) | Two layers because the tier-level cap is the empirical floor (an Opus cell costs ~$3, so anything <$3 strands the tier) while the per-cell-ceilings table is the operator's session-wide cost discipline. The router takes the LOWER of the two. | Cost-gradient table v3-FINAL-SYNTHESIS §2.1. |
| `operator_warning_at_usd` is soft (router continues), `operator_kill_at_usd` is hard (router refuses further routing) | A soft warning emits a structured event for human review without breaking long-running runs that legitimately need to spend; a hard kill is the loud-not-silent backstop. Combining them in a single threshold is the silent-amplification class. | Standard "warning vs error" practice; ADR-0006 governance pattern. |
| No `override_session_kill` field at policy level | Overriding the kill cap requires a new session and a new policy fingerprint. Putting an override flag at policy level invites operator-roulette where the override becomes the new default. | Loud-not-silent doctrine; configuration-and-secrets.md "no production snowflakes." |
| Each rule carries a stable `rule_id` (kebab-case) | Rule ids are the audit-log key. Renaming a rule MUST be a v1.x semver bump with a deprecation note (per `principles/semantic-versioning.md`); without stable ids, audit-log replay across policy versions is broken. | Schema `$defs.escalation_rule.properties.rule_id.pattern`. |
| Policy version is separate from schema version | The schema (`router-policy.v1.schema.json`) changes shape on additions; the policy (`policy_version: 1.0.0`) changes content on rule changes. A new refusal rule landing is a content bump, not a schema bump. | Pattern lifted from `run-contract.v1.schema.json` `schema_version` + author-supplied `name`. |
| Schema mandates `cost_ceilings.per_cell` and `cost_ceilings.per_session`; numbers in examples are placeholders | The structural commitment is "cost ceilings exist." The numbers depend on the operator's vendor invoice and risk tolerance, and the ADR cannot bind those without external grounding. Placeholders surface this honestly. | Inputs `# placeholder — operator to finalize` comments in every example YAML. |
| Audit log declaration is optional at the schema level, but every shipped example includes one | Some experimental router deployments (local-dev, single-operator) reasonably skip the audit log. Mandating it would force loudly-broken policies in those modes; making it optional plus including it in every shipped example makes the right thing the obvious thing. | Pattern lifted from `run-contract.v1.schema.json` `outputs.audit`. |

## Consequences

### Enables

- A consumer of doctrine can validate any router-policy YAML at boundary entry. The validation script extension (`validate-contracts-v1.py`) gives both CI and authors a single source of truth.
- The commercial-moat claim becomes concrete. "We refuse haiku for greenfield" stops being a slide and becomes a `refuse_routing: true` line with an `evidence_ref` pointer at the v2 canonical-scoring file.
- Operators can ship variant policies (enterprise-strict, experimental-haiku-narrow-scope) without forking the schema. The three shipped examples are the canonical demonstrations of how variation looks; new estates copy one and edit numbers.
- The 3-tier shape is structurally enforced. Variant policies CANNOT silently drop a tier and still validate.
- Escalation cost is bounded by `max_cost_usd` per rule, so a runaway "escalate-to-premium on every cell" loop self-terminates rather than amortising into the operator's monthly bill.
- The narrow_scope tier is permitted in production with mandatory external review, preserving the $0.21/cell economics of haiku for scaffolded subtasks without exposing the +10 Δ self-canonical risk to operator review.
- Audit replay across policy versions is preserved because `rule_id` is stable; an audit JSONL from yesterday remains intelligible against today's policy as long as the rule_id survived (semver bump otherwise).

### Forbids

- A router-policy YAML missing any of the three required tiers is rejected at validation time (negative case `router-negative-missing-tier`). Closing the "v1 policy without all three tiers" silent class.
- A router-policy YAML with no refusal rules is rejected at validation time (`minItems: 1`). Closing the "router with no opinions" silent class.
- A tier without a `primer_sha256` is rejected (council D5 hash pin). Closing the "primer drift via name-only resolution" silent class.
- A tier without an `external_review_required` field is rejected. Closing the "implicit review-not-required" silent class.
- A refusal rule without `evidence_ref` is rejected at validation time. Closing the "vibes-refusal" class.
- `refuse_routing: false` is structurally illegal (`const: true` in the hard-refusal action shape). There is no soft-refusal path.
- A `when` clause mixing two of the `oneOf` discriminator shapes is rejected. The router cannot be tricked into "matches if either of two conditions fires" — that ambiguity has to be encoded as two separate rules with their own rule_ids and evidence_refs.
- An `action` mixing `escalate_to_tier` and `require_tier` is rejected. Tier escalation and class-pinning are structurally different operations.
- `additionalProperties: false` everywhere means a typo'd field name does not silently become a no-op. The validator catches it and the rule cannot ship.
- The hard `operator_kill_at_usd` has no policy-level override. Once the session crosses the kill cap, the router refuses further routing; lifting the cap requires a new policy fingerprint and a new session.
- Haiku-no-primer routing on `build_class`, `artifact_production`, or `refactor_class` is rejected by the `primer-required-on-build-class` refusal rule across all shipped examples. Closing the "agent strips the primer and ships anyway" path.

### Open work

- The narrow-scope haiku tier ships with `external_review_sample_rate: 1.0`. Lowering the rate requires an independently-measured non-self canonical run on a fresh adversarial cohort and operator sign-off.
- The `corcept-hook-bypass-fix` has landed at corcept v2; the router-layer `interpreter-wrapper-block` refusal remains as defense-in-depth and an evidence anchor. Removing it from the router would require a separate ADR (it is not just a "now corcept handles it" decision — the router-layer refusal is visible to non-corcept consumers).
- The cost ceiling numbers in every example are placeholders. The operator finalises them against actual vendor invoices before the ADR moves from Proposed to Accepted.
- A v3.5 ship-list item — runtime enforcement of `require_external_review: true` — is not in scope for this ADR. The schema declares the field; the in-tree corcept implementation lands separately.

### Doctrine surfaces touched

- New machine-readable contract: [`contracts/router-policy.v1.schema.json`](../../contracts/router-policy.v1.schema.json).
- New examples directory: [`contracts/examples/`](../../contracts/examples/) with three shipped router-policy YAMLs.
- Extended validator: [`scripts/validate-contracts-v1.py`](../../scripts/validate-contracts-v1.py).
- Semantic Index gains a new Spine row and Task Route ([SEMANTIC_INDEX.md](../../doctrine/SEMANTIC_INDEX.md)).
- REFERENCES.md gains entries for the schema and ADR ([REFERENCES.md](../../doctrine/REFERENCES.md) — Machine-readable contracts table).
- Cross-link from [`value-sheet/18-cross-product-test/v3/v3-FINAL-SYNTHESIS.md`](https://github.com/0ryant/value-sheet) §6 ship-list item 4 points at this file.

### Loud residual risk

The cost numbers are illustrative. The operator MUST finalise them before this ADR moves to Accepted. Shipping the default-production policy with placeholder costs on top of real vendor billing would cause the per-session kill to fire either too early (interrupting legitimate long-runs) or too late (after meaningful spend). The schema's two-tier structure is correct; only the magnitudes are TBD.

A second residual: the narrow_scope tier's `external_review_sample_rate: 1.0` is a v1 conservative position. The operator may want to lower it once independent measurement is on the record, but until then every Haiku-PRIMED narrow-scope run is gated by a non-self reviewer. This is loud-not-silent; the schema does not let the rate drop below 0 (`minimum: 0`) and does not let it silently disappear (it is `required` whenever `external_review_required: true`).

## Evidence

- Empirical anchor table in §Context above, traced row-by-row to canonical-scoring.md, canonical-scoring-sonnet-primed.md, canonical-scoring-opus.md, canonical-scoring-haiku-primed.md.
- CC-2 falsification at composite.md rows 125, 176, 278, 292, 302.
- Council D4 4/4 resolution at v3-FINAL-SYNTHESIS.md §6 (3-tier policy locked, ADR-0009 refire mandated).
- Council D5 4/4 resolution at v3-FINAL-SYNTHESIS.md §6 (canonical primer hash pinned).
- Validation harness output (run on 2026-05-20): four in-memory positive cases (three run-contract/verifier-pack, one router-policy), three on-disk YAML positive cases, three run-contract negative cases (existing), twelve router-policy negative cases (new in this ADR). All pass. Reproduce with `python scripts/validate-contracts-v1.py` from the repo root.
- Schema cross-pattern: `run-contract.v1.schema.json` (the v1 envelope) and `verifier-pack.v1.schema.json` (the v1 verifier mirror) inform the `additionalProperties: false` + oneOf discriminator shape used here.
- Pattern surface: this ADR is the routing-policy counterpart to the existing `patterns/run-contracts.md` and `patterns/verifier-packs.md` doctrine; a future `patterns/model-routing.md` is queued as the human-readable pattern doc but is out of scope for this ADR (the schema and examples are the load-bearing artifacts).
