---
name: anti-confabulation
version: 1.0.0
schema_version: 1.0.0
applies_to: build-class tasks (code generation, evidence-pack emission, MCP wrapper generation, implementation work whose claims can be re-tested against artefacts)
required_for:
  - model-balanced-4.6
  - model-balanced-4.7
optional_for:
  - model-high-capability-4.7
experimental_for:
  - narrow-scope model-4.7
verifier_pack: anti-confabulation-verifier-pack
priming_block_sha256: c138dd966c82f7bd792684ab3fef0f50d75aa9342468db8b5d265f24f3fb35a8
priming_block_bytes: 1444
priming_block_words: 231
licence: Apache-2.0
related:
  - doctrine/patterns/anti-confabulation-priming.md
  - doctrine/patterns/run-contracts.md
  - doctrine/patterns/verifier-packs.md
  - contracts/verifier-pack.v1.schema.json
---

# Skill: anti-confabulation

> Anti-confabulation priming. A fixed ~200-token meta-cognitive block that
> lifts build-class-task calibration delta from +11 to −1 (12-point
> tightening) on model-balanced 4.6, holding model and backbone fixed. Empirical
> basis: `evidence-workbook/18-cross-product-test/v2/results/test-1-backbone/`.

## When to reach for this skill

Reach for `anti-confabulation` whenever an agent is about to perform a
**build-class task** — code generation, evidence-pack emission, MCP wrapper
generation, implementation work whose self-claims can be re-tested by a
hostile re-scorer against materialised artefacts. Do **not** reach for this
skill on pure-reasoning tasks (Q&A, analysis, summarisation without artefact
emission) — untested in the Stage 2 measurement and bundling would inflict the
~200-token cost without an observed lift.

The skill is **auto-bundled** by run contracts whose `context.skills` array
contains any build-class skill (per
[doctrine/patterns/run-contracts.md §3.5](../patterns/run-contracts.md#35-auto-bundled-skills)).
Operators MUST NOT need to add this skill explicitly when authoring a
build-class contract; the validator handles it.

## When this skill is required

Per the model class:

- **model-balanced 4.6 / 4.7:** REQUIRED for any build-class contract. Empirical lift
  +7 canonical points / 12-point delta tightening
  (`canonical-scoring-model-balanced-primed.md:238-251`).
- **model-high-capability 4.7:** OPTIONAL but recommended. Empirical delta floor 0 to −2.5
  (`canonical-scoring-model-high-capability.md:50-58`). The model-high-capability lift is small but the
  intervention is cheap.
- **narrow-scope model 4.7:** EXPERIMENTAL. Unmeasured with priming in Stage 2; the
  unprimed Tools-narrow-scope model cell over-claimed by 65 points
  (`canonical-scoring.md:39-43`). Whether priming would help is an open
  empirical question.

## The canonical priming block

The text below is the canonical, hashable, immutable artefact for v1.0.0. Any
run contract auto-bundling this skill MUST inject this exact text into the
cell's system prompt. The verifier pack
[`anti-confabulation-verifier-pack`](#verifier-pack-reference) asserts
presence by SHA-256 match.

```
# Anti-confabulation priming

You are about to perform a build-class task. Stage 2 measurement found that
unprimed cells over-claimed their canonical score by 11 to 65 points across 5
of 7 cells, with the worst single failure being a CLI that printed "Evidence
written to: <path>" and exited 0 without writing the file. The cell
self-scored PASS. A hostile re-scorer then re-ran every binary check on real
artefacts and found the silent stub.

Assume the same hostile re-scorer will audit your work line by line, re-run
every assertion you make against real artefacts, and reject any claim that
does not survive blind binary verification. They have no access to your
internal reasoning; they only read what you produced and what the artefacts
actually do.

Before you self-score:

1. List the load-bearing claims your output makes that a hostile judge would
   re-test (e.g. ".env_clear() is wired", "verify fails on tampered input",
   "the declared output file exists and is non-empty").
2. For each claim, name the binary observation that would falsify it.
3. Predict the canonical (hostile-judge) score you will receive. Build a
   prediction buffer: if your self-score is S, your predicted hostile score
   should be S minus the magnitude of the gaps you cannot close in this run.
4. If your prediction buffer is zero, you have not looked hard enough.

Loud-not-silent: declare gaps explicitly. Unflagged gaps cost more than
flagged ones.
```

**Canonical fingerprint:**
`sha256:c138dd966c82f7bd792684ab3fef0f50d75aa9342468db8b5d265f24f3fb35a8`

The hash is computed over the verbatim 1444 bytes of the block above with
**LF line endings only** (no CRLF, no BOM, 231 words). Implementations on
Windows-checkout repositories MUST normalise CRLF to LF before hashing (the
canonical Git object-store representation of this file is LF-only; see the
project's `core.autocrlf=true` convention). Operators verifying their consumer
pipeline can reproduce the hash with:

```bash
# Extract the priming block region between the triple-backtick fences above,
# normalise to LF, and pipe through sha256sum. The expected output is the
# canonical hash.
git cat-file -p HEAD:doctrine/skills/anti-confabulation.skill.md \
  | awk '/^```$/{c++; if (c==1) {p=1; next} else if (c==2) {p=0}} p' \
  | sha256sum
# Expected: c138dd966c82f7bd792684ab3fef0f50d75aa9342468db8b5d265f24f3fb35a8
```

Any change to the block produces a new hash and requires a new ADR documenting
why the prior block was insufficient (per
[doctrine/patterns/anti-confabulation-priming.md §5.6](../patterns/anti-confabulation-priming.md#56-versioning)).

## How (golden invocation)

The skill is consumed declaratively by listing it in a run contract's
`context.skills` array:

```yaml
run_contract:
  name: evidence-pack-build-review
  schema_version: 1.0.0
  context:
    skills:
      - evidence-pack-mcp        # build-class skill; triggers auto-bundle
      - anti-confabulation     # auto-added by validator if absent
      - cargo-build-and-test
    memory: { mode: verified_only, ceiling: RemoteSigned }
  verifiers:
    - evidence-pack-mcp-verifier-pack
    - anti-confabulation-verifier-pack   # sibling pack; mandatory
    - cargo-build-and-test-verifier-pack
  # ... rest of contract
```

The validator MUST:

1. Detect any `context.skills[i]` with `kind: build-class` in its skill
   manifest.
2. Auto-inject `anti-confabulation` into `context.skills` if absent.
3. Auto-inject `anti-confabulation-verifier-pack` into `verifiers` if absent.
4. Render the priming block into the cell's system prompt at contract
   instantiation time.

## Expected output

Per the agent's response:

- The cell SHOULD list load-bearing claims and their binary falsifiers before
  self-scoring (priming ingredient 1-2).
- The cell SHOULD report a numeric hostile-judge prediction with a non-zero
  buffer (priming ingredient 3-4).
- The cell SHOULD declare gaps explicitly in a "voluntary deductions" or
  equivalent section.

Per the verifier pack:

- The `priming_active` assertion passes when the rendered system prompt
  contains the canonical block byte-for-byte, hash-matched.
- The assertion `fail_loud`s if the block is missing, mangled, or replaced
  with an older version.
- The assertion is `inconclusive` if the executing engine
  (`review.claim_audit`) has not yet shipped the `priming_active` kind
  implementation.

## Common pitfalls

- **Skipping the auto-bundle by removing the build-class tag from a skill
  manifest.** This is a doctrine PR — the tag is the affordance. Removing it
  to silence priming is not a per-contract opt-out; it is a doctrine change.
- **Pasting a paraphrased priming block.** The hash is over the verbatim
  bytes. A paraphrased block has a different hash; the verifier `fail_loud`s.
  Use the verbatim text.
- **Double-priming.** A skill whose own SKILL.md cites the silent-stub
  failure mode in similar terms may stack interventions when `context.skills`
  includes both. The Stage 2 measurement did not control for double-priming;
  reviewers SHOULD watch for the pattern at PR time.
- **Treating priming as a substitute for the verifier pack.** Priming
  tightens self-score deltas; the structural envelope catches outputs. Both
  are mandatory.
- **Applying priming to narrow-scope model without measurement.** The `required_for`
  semantics mark narrow-scope model experimental for a reason — priming may be net-neutral
  or net-harmful on a model without sufficient meta-cognitive capacity. Run
  per-model measurement before promoting narrow-scope model from `experimental_for` to
  `required_for`.

## Verifier-pack reference

The sibling verifier pack is `anti-confabulation-verifier-pack` and ships
alongside this file at `doctrine/skills/anti-confabulation.verifier-pack.yml`
(forthcoming; until shipped, the pack body is reproduced inline in
[doctrine/patterns/anti-confabulation-priming.md §5.5](../patterns/anti-confabulation-priming.md#55-verifier-pack-pairing)).

The pack contains exactly one verifier of kind `priming_active`. The kind is
the 11th canonical verifier kind in
[contracts/verifier-pack.v1.schema.json](../../contracts/verifier-pack.v1.schema.json)
(added in this commit; see
[doctrine/patterns/verifier-packs.md §3 "Canonical kinds"](../patterns/verifier-packs.md#3-the-10-canonical-verifier-kinds)).

## Empirical basis (links into measurement files)

Run-contract authors and reviewers can audit the measurement basis at:

- `evidence-workbook/18-cross-product-test/v2/results/test-1-backbone/canonical-scoring.md`
  — 5-cell unprimed baseline; Tools-narrow-scope model silent-stub at lines 39-43.
- `evidence-workbook/18-cross-product-test/v2/results/test-1-backbone/canonical-scoring-model-high-capability.md`
  — 2-cell model-high-capability pass with priming; Tools-model-high-capability delta 0 at line 52;
  Native-model-high-capability delta −2.5 at line 53.
- `evidence-workbook/18-cross-product-test/v2/results/test-1-backbone/canonical-scoring-model-balanced-primed.md`
  — apples-to-apples control; +7 lift / 12-point delta tightening at lines
  238-251; downstream `deny_unknown_fields` surfacing at lines 300-319;
  commercial cost-effectiveness ordering at lines 281-291.

See [doctrine/patterns/anti-confabulation-priming.md §3 "Rationale"](../patterns/anti-confabulation-priming.md#3-rationale)
for the full evidence walkthrough.

## See also

- [doctrine/patterns/anti-confabulation-priming.md](../patterns/anti-confabulation-priming.md)
  — the canonical pattern document. Read this for full rationale, forces,
  consequences, and the honest gap list.
- [doctrine/patterns/run-contracts.md §3.5](../patterns/run-contracts.md#35-auto-bundled-skills)
  — the run-contract auto-bundle rule that injects this skill.
- [doctrine/patterns/verifier-packs.md §3](../patterns/verifier-packs.md#3-the-10-canonical-verifier-kinds)
  — the `priming_active` verifier kind (the 11th canonical kind).
- [contracts/verifier-pack.v1.schema.json](../../contracts/verifier-pack.v1.schema.json)
  — the machine-readable schema with `priming_active` in the kind enum.
