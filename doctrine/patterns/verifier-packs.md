# Verifier Packs

A **verifier pack** is the mandatory mirror of a skill. Every skill cited by a run contract MUST ship a sibling pack. The pack is a closed list of **binary-observable assertions** that fail loudly when the skill's declared behaviour is not actually produced. Without a paired pack, a skill is unbounded affordance — a confidence prime without an evidence discipline.

The canonical machine-readable shape lives at [../../contracts/verifier-pack.v1.schema.json](../../contracts/verifier-pack.v1.schema.json) (JSON Schema 2020-12). The pack is consumed by a run contract's `verifiers: [...]` array — see [run-contracts.md](run-contracts.md).

Relates to: [run-contracts.md](run-contracts.md) (the envelope that names which packs to run), [code-review-and-change-approval.md](code-review-and-change-approval.md) (high-risk classes and review duties), [../principles/testing-strategy.md](../principles/testing-strategy.md) (adversarial CI, mutation/property-based testing), [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) (skills as governed surfaces), [../principles/audit-logging.md](../principles/audit-logging.md) (assertion results land in the audit log), [chaos-engineering-and-game-days.md](chaos-engineering-and-game-days.md) (the tamper-class assertion kinds reuse fault-injection thinking at the unit-of-skill scale).

---

## 1. Why Verifier Packs Exist

Two evidence classes drove v1. Both share a structural cause: **skills are affordance, not assertion**.

1. **Skills can amplify confabulation when unpaired.** A skill names what an agent should know; without a paired verifier — a test the agent cannot pass without producing the promised artefact — added instructions can increase confidence without adding evidence. Treat that as a risk hypothesis to test, not as a universal measured effect.
2. **No tool catches silent-stub class failures by default.** A CLI prints *"Evidence written to: …"* and exits `0` without writing the file. Today's mainstream verdict catalogues cover missing-intent and security-sensitive-change, but not *"the declared output does not exist."*

A pack closes both by binding the skill to a non-negotiable post-run check: `test -s ${path}` (or richer) over declared artefacts. Missing artefact, loud fail. The CLI cannot lie; the agent cannot launder a lie into the audit log.

---

## 2. Pack Format

A pack declares **four required keys** (`name`, `skill`, `version`, `verifiers`) plus optional scaffolding (`description`, `fingerprint`, `schema_version`, `setup`, `teardown`). Every object level sets `additionalProperties: false`.

Each verifier item declares:

| Field | Required | Purpose |
| --- | --- | --- |
| `kind` | yes | One of the 10 canonical kinds (plus `custom` escape hatch). |
| `description` | yes | Human-readable assertion text. |
| `command` | yes | Shell-or-program invocation. |
| `expected_exit` | no | Integer 0..255 OR `null` if not asserted. |
| `expected_stdout_contains` | no | Substring match on stdout OR `null`. |
| `expected_stderr_contains` | no | Substring match on stderr OR `null`. |
| `expected_artefacts` | no | Paths that MUST exist after the verifier runs. |
| `failure_mode` | yes | `fail_loud` / `mark_untrusted` / `inconclusive`. |
| `severity` | no | `fatal` / `error` / `warning`. |
| `timeout_seconds` | no | Per-verifier wall-clock cap; exceeding returns `inconclusive`. |
| `preconditions` | no | Verifier ids that must pass before this one runs. |

---

## 3. The 11 Canonical Verifier Kinds

Each kind is a *family* of binary-observable assertions, not a single command. Packs SHOULD reuse a canonical kind; `custom` is the escape hatch and MUST justify why a standard kind would not fit.

| Kind | Asserts that |
| --- | --- |
| `cli_writes_declared_output` | The CLI writes a non-empty file at the declared path (closes silent-stub). |
| `verify_succeeds_on_valid_input` | A `verify`-style subcommand exits 0 on a freshly-produced artefact. |
| `tamper_verify_fails` | Mutating the artefact invalidates `verify`. |
| `missing_input_fails` | `verify` on a nonexistent path exits non-zero (closes fabrication class). |
| `env_canary_not_in_subprocess` | A parent-level canary env var does NOT propagate to spawned subprocesses. |
| `symlink_escape_rejected` | A symlink pointing outside the declared root is rejected. |
| `output_cap_enforced` | Oversize outputs are rejected, not silently truncated. |
| `jsonl_audit_event_emitted` | Exactly one well-formed JSONL audit event lands per CLI invocation. |
| `lockfile_generated` | Regenerating the wrapper produces a lockfile that matches the running tool fingerprint. |
| `host_registrations_generated` | Host registration files (claude/cursor/codex) exist and validate. |
| `priming_active` | The rendered system prompt contains the estate-approved priming block, content-matched to the digest declared by the run contract; this proves configuration presence, not outcome correctness (see [anti-confabulation-priming.md](anti-confabulation-priming.md)). |
| `custom` | Escape hatch — should be rare; high-friction by design. |

`priming_active` was added in schema v1.1.0 (additive minor bump). Further kinds may be added in v1.x minors. Renaming or removing a kind is a v2 break.

---

## 4. Failure Modes — Fail-Loud, Never Fail-Silent

Four verdicts per assertion; verdicts compose to a pack-level verdict.

| Verdict | Meaning | Run-level effect |
| --- | --- | --- |
| `pass` | Assertion produced its expected observation. | Continue. |
| `fail_loud` | Wrong observation (silent-stub, fabrication, tamper bypass). | **Run REJECTED**; approval queue routes to human review. |
| `mark_untrusted` | Failed in a way that downgrades trust without rejecting (e.g. size cap exceeded, lockfile drift). | Outputs marked **provisional**; audit log records the downgrade. |
| `inconclusive` | Verifier itself errored — pack-execution crash, `timeout_seconds`, or chained precondition failure. | **Loudest possible signal** — worse than `fail_loud` because the system could not determine truth. |

There is no `skip`. A precondition-failed verifier produces an *audited* skip in the JSONL log; the audit record is the loud-not-silent signal. Authors MUST NOT use preconditions to silence assertions they don't want to write.

A stub MUST NOT pass. A verifier that always returns 0 is a defect, caught at PR review the same way silent stubs in production code are caught.

---

## 5. Worked Example: `evidence-pack-mcp-verifier-pack`

This illustrative 10-assertion list for an evidence-pack skill is mapped to the v1 schema. The full YAML round-trips through [../../scripts/validate-contracts-v1.py](../../scripts/validate-contracts-v1.py).

```yaml
verifier_pack:
  name: evidence-pack-mcp-verifier-pack
  skill: evidence-pack-mcp
  version: 1.0.0
  schema_version: 1.0.0
  description: Verify evidence-pack-mcp produces a complete tamper-resistant evidence pack with bounded authority.

  setup:
    - mkdir -p ${OUTPUT_DIR} ${SCRATCH}
    - evidence-pack collect --out ${OUTPUT_DIR}/pack.json --audit ${AUDIT_LOG}
  teardown:
    - rm -rf ${SCRATCH}

  verifiers:
    - id: cli_writes_declared_output
      kind: cli_writes_declared_output
      description: evidence-pack collect writes a non-empty pack.json at the declared output path
      command: test -s ${OUTPUT_DIR}/pack.json
      expected_exit: 0
      expected_artefacts: [${OUTPUT_DIR}/pack.json]
      failure_mode: fail_loud
      severity: fatal
    # ...nine more assertions in the same shape; see scripts/validate-contracts-v1.py
    # for the complete byte-for-byte instance that validates against v1.schema.json.
```

The complete illustrative list, each with a `kind` from the canonical 10:

| # | id | kind | failure_mode | severity |
| --- | --- | --- | --- | --- |
| 1 | `cli_writes_declared_output` | `cli_writes_declared_output` | `fail_loud` | fatal |
| 2 | `verify_succeeds_on_valid_pack` | `verify_succeeds_on_valid_input` | `fail_loud` | fatal |
| 3 | `tamper_verify_fails` | `tamper_verify_fails` | `fail_loud` | fatal |
| 4 | `missing_input_fails` | `missing_input_fails` | `fail_loud` | fatal |
| 5 | `env_canary_not_in_subprocess` | `env_canary_not_in_subprocess` | `fail_loud` | fatal |
| 6 | `symlink_escape_rejected` | `symlink_escape_rejected` | `fail_loud` | fatal |
| 7 | `output_cap_enforced` | `output_cap_enforced` | `mark_untrusted` | error |
| 8 | `jsonl_audit_event_emitted` | `jsonl_audit_event_emitted` | `fail_loud` | fatal |
| 9 | `lockfile_generated` (tool-contract.lock) | `lockfile_generated` | `mark_untrusted` | error |
| 10 | `host_registrations_generated` (claude/cursor/codex) | `host_registrations_generated` | `mark_untrusted` | error |

**Seven `fail_loud` / `fatal`**, three `mark_untrusted` / `error`. A skill that cannot pass all seven fatal assertions has not earned the right to ship. The three error-level assertions downgrade trust without blocking the run — lockfile drift or missing host registration is observable in the audit log but does not reject otherwise-valid outputs.

---

## 6. Discovery And Sibling Convention

Packs live alongside the skills they mirror, or are addressable from the same estate catalog. Catalog CI fails on any registered skill without a resolvable pack.

| Skill location | Verifier-pack location |
| --- | --- |
| `<skill-root>/<skill>/SKILL.md` | `<skill-root>/<skill>/verifier-pack.yml` |
| Skill registered by an API or tool server | Pack address registered in the same catalog record |

The convention is intentionally rigid: a skill that cannot point to its pack is inadmissible.

---

## 7. Composition With Run Contracts

A run contract names which packs to run; a pack names which assertions to test. The contract's `verifiers: [...]` array holds **pack ids**, and the validator (see [run-contracts.md §7](run-contracts.md#7-validation-tooling)) checks every id resolves.

A pack runs as a post-run phase of a contract. It receives the contract fingerprint, the materialised artefact tree, and the resolved environment (so `${OUTPUT_DIR}` binds to real paths). It produces a JSONL record per assertion plus a top-level verdict. The verdict feeds the run-contract verdict, which feeds the approval queue and memory substrate.

```json
{
  "pack_id": "evidence-pack-mcp-verifier-pack",
  "skill": "evidence-pack-mcp",
  "run_contract_fingerprint": "sha256:abc...",
  "executed_at": "2026-05-19T19:00:00Z",
  "verdict": "fail_loud",
  "results": [
    {
      "id": "cli_writes_declared_output",
      "verdict": "fail_loud",
      "evidence": "file /work/out/pack.json did not exist after CLI exit",
      "severity": "fatal"
    }
  ],
  "fatal_count": 1,
  "error_count": 0,
  "warning_count": 0
}
```

---

## 8. What This Is NOT

- **NOT a unit-test framework.** Packs assert on *artefacts a real run produces*, not on internal implementation. Unit tests live in the skill's own repo ([../principles/testing-strategy.md](../principles/testing-strategy.md)); packs are integration-level smoke tests at the unit-of-skill scope.
- **NOT a model evaluator.** Packs check binary-observable artefact properties (existence, exit codes, substring matches, byte-tamper). Quality eval is a higher-level concern ([../principles/ai-ml-systems.md](../principles/ai-ml-systems.md), [rag-retrieval-baseline.md](rag-retrieval-baseline.md)).
- **NOT a security scanner.** Some assertions are security-flavoured, but packs are not a substitute for [secure-development-lifecycle](../principles/secure-development-lifecycle.md), SBOM, or supply-chain controls.
- **NOT a substitute for human review.** A passing pack is *necessary*, not sufficient. High-blast-radius runs still route through [code-review-and-change-approval.md](code-review-and-change-approval.md).
- **NOT extensible at runtime.** The 10 kinds are fixed in v1; adding one is a v1.x minor release. `custom` is the escape hatch and carries reviewer friction by design.

---

## 9. Validation Tooling

Packs are themselves validated. The reference Python validator at [../../scripts/validate-contracts-v1.py](../../scripts/validate-contracts-v1.py) round-trips the §5 example. Consumers SHOULD: run the validator in CI on every committed `verifier-pack.yml`; run a *sibling-existence* check (every skill manifest has a pack at the conventional path); fingerprint the canonicalised body (`sha256:<hex>`) and pin it from the run contract's audit log so verifiers can be reconstructed byte-for-byte.

A buggy pack is load-bearing. Mitigations: pack PRs are reviewed like any change; the canonical-kind library lets most assertions reuse vetted implementations; the pack-execution engine itself is verifiable by a meta-pack.

---

## 10. Implementation Contract

A conforming pack engine MUST implement the declared verifier-kind semantics, honour timeouts and preconditions, preserve the four verdicts, bind results to the run-contract fingerprint, and emit retrievable evidence for every assertion. A generator MAY create starter packs, but generated assertions still require review and a demonstrated negative case.

Implementations that emit or consume packs SHOULD identify the schema version and link to this pattern. No particular language, runtime, generator, or catalog is the reference implementation.

---

## 11. Honest v1 Gap

The v1 pack format does **not** address:

- **Cross-pack assertions.** A pack only asserts about its own skill. Estate-level invariants ("every contract that emitted X also emitted Y") need a higher-level meta-pack — out of scope for v1.
- **Streaming verification.** Packs run post-run; they observe artefacts the run left behind, not in-flight events. Catching a bad write *before* it lands belongs to the run-contract `hooks` map.
- **Quantitative scoring.** Each assertion is binary. Gradient scoring should be decomposed into N binary assertions or live in a separate eval framework.
- **Cross-language assertion sharing.** The schema and the declared kind semantics are authoritative. Implementations need shared conformance fixtures to resolve behavioural ambiguity; v1 does not yet publish a complete suite.
- **Pack composition / inheritance.** A pack cannot extend another. v2 may introduce composition; v1 prefers explicitness over DRY.

These gaps define the boundary of v1.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Every skill MUST have a pack | Unpaired skills net-harm weaker models; mandate is the structural close. |
| 10 fixed kinds + `custom` escape hatch | Small enumerated set is reviewable; `custom` is high-friction by design. |
| `fail_loud` / `mark_untrusted` / `inconclusive` (no `pass-silent`) | Silent-stub was the largest failure class; verdicts ARE the loud-not-silent signal. |
| Sibling-file discovery convention | Removing alternative paths removes places a pack can hide. |
| Packs validate via JSON Schema, not Rust-only | OSS-public reference must be language-neutral. |
| No `skip` verdict; audited skips only | Silencing an assertion requires explicit deletion in a reviewed PR. |

---

## Related

- [run-contracts.md](run-contracts.md) — the envelope that consumes pack ids.
- [code-review-and-change-approval.md](code-review-and-change-approval.md), [../principles/testing-strategy.md](../principles/testing-strategy.md) — review and testing discipline.
- [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md), [../principles/audit-logging.md](../principles/audit-logging.md), [chaos-engineering-and-game-days.md](chaos-engineering-and-game-days.md) — governed AI systems; audit shape; fault-injection thinking.
- [../../contracts/verifier-pack.v1.schema.json](../../contracts/verifier-pack.v1.schema.json), [../../scripts/validate-contracts-v1.py](../../scripts/validate-contracts-v1.py) — schema and reference validator.
