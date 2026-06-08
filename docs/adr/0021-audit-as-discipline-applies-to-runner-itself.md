# 0021. Audit-As-Discipline Applies to the Runner Itself

Status: Proposed
Decision date: 2026-05-20
Recorded date: 2026-05-20
Retrospective: No

## Context

The 2026-05-20 model-balanced/model-high-capability ablation against the agent-authority framework bundle (matrix
`canonical-test/matrices/claude-code-3x5-bundle-on.yaml`) ran 15 cells.
Three of those cells were declared as `condition: E` ("full agent-authority framework stack:
the organisation-tools + primer + skills blurb"). They claimed they would exercise
the full 7-server the organisation MCP cohort: `host-policy-layer`, `tool-contract-generator`, `independent-review-engine`,
`doctrine-adapter`, `memory-service`, `context-supply-service`, `secret-broker`.

Empirically, only one server connected. `receipts/ablation-model-balanced-model-high-capability-cccli-2026-05-20/cells/cc-narrow-scope model-E/transcript.jsonl`
line 1 shows:

```
"mcp_servers": [
  {"name":"host-policy-layer","status":"failed"},
  {"name":"tool-contract-generator","status":"failed"},
  {"name":"independent-review-engine","status":"failed"},
  {"name":"doctrine-adapter","status":"failed"},
  {"name":"memory-service","status":"connected"},
  {"name":"context-supply-service","status":"failed"},
  {"name":"secret-broker","status":"failed"}
]
```

The runner's invocation pattern for six of seven binaries was wrong
(e.g. `host-policy-layer mcp` — there is no such subcommand; the actual MCP
server is the separate `host-policy-layer-mcp` binary; `context-supply-service mcp` should be
`context-supply-service serve`; `tool-contract-generator serve` doesn't exist because tool-contract-generator is a
compiler, not an MCP server; `independent-review-engine` isn't installed at all).
Every server with a wrong invocation failed silently and the runner
treated `final_status: COMPLETED` as success.

Three E-cells were scored by a downstream model-high-capability 4.7 blind judge for
~$4.24 — measuring "D + memory-service-only" while claiming to measure "D +
full the organisation cohort". The measurement is structurally invalid.

This failure is doctrinally diagnostic. The agent-authority framework stack's central
principle is *audit-as-discipline*: every claim must be backed by a
typed evidence envelope; declared-but-unverified surfaces fail closed.
The runner that MEASURES the agent-authority framework stack failed to apply this
discipline to itself. It accepted a declared cohort and ran without
verifying any of it actually connected. The doctrine framework Dx14
("agent-authority framework v3.4 declared-but-not-wired-fails-closed") emerged from
exactly this kind of measurement collapse — but Dx14 had been
applied only to product surfaces, not to the runner that audits them.

## Decision

**The audit-as-discipline principle applies recursively. Any tool that
MEASURES agent-authority framework-shaped surfaces MUST itself apply agent-authority framework principles.**

Concretely: when a measurement runner declares its expected
substrate, it must fail closed on declared-but-not-wired conditions
at the runner level, BEFORE any expensive measurement begins.

The minimum mechanism, codified in this ADR for use by every
present + future measurement runner in the bundle:

1. **Declarative cohort contract.** Each measurement cell (or
   matrix row) declares the substrate it requires. For the
   canonical-test runner this is the new `expected_mcp_tools` field
   on the cell spec.

2. **Pre-execution gate.** At cell startup, the runner parses
   whatever introspection signal the host provides (for Claude Code
   it is the stream-json `system.init` event's `mcp_servers` array)
   and computes the gap: declared - registered. Any non-empty gap
   triggers the fail-closed path.

3. **Distinct terminal state.** The cell ends in a NEW terminal
   state — `FAILED_PREFLIGHT` in the canonical-test ledger — distinct
   from `FAILED_EMPTY` (model ran, produced nothing) and `COMPLETED`
   (model ran, produced artefacts). The state name carries the
   diagnosis.

4. **Zero LLM spend.** The kill happens BEFORE the runner forwards
   any prompt to the model. Zero tokens, zero dollars.

5. **Typed diagnostic receipt.** The runner emits
   `<cell_dir>/preflight-failure.json` with the cell_id, declared
   cohort, actually-registered cohort, the missing set, doctrine
   pointer, and remediation hint. The receipt is the typed evidence
   envelope this ADR demands.

6. **Opt-in, backward-compatible.** Cells that omit the cohort
   declaration are NOT gated. Matrices written before Dx14 keep
   running. The gate fires only when a cell explicitly opts in by
   declaring what must be there.

The principle generalises beyond MCP cohorts:
- Whatever a runner DECLARES it depends on, it MUST validate at
  startup, fail closed on absence, and emit a typed receipt.
- The validator must run before the expensive step (LLM tokens,
  scoring time, network spend).
- The validator's own output must be auditable (receipt on disk,
  ledger entry).

## Mechanism: the worked example

`the organisation-bundle/canonical-test/harness-free-runner/claude_code_runner.py`
(branch `claude/dx14-fail-closed-gate-2026-05-20`) is the canonical
worked example. Key pieces:

- **Cell-spec field.** `CellSpec.expected_mcp_tools: list[str]`
  (default `[]`). Schema in `matrix.v1.schema.json` accepts an
  optional `expected_mcp_tools: [...]` per cell.

- **Telemetry surface.** `ClaudeCodeCellTelemetry` carries
  `expected_mcp_tools`, `registered_mcp_tools`, `missing_mcp_tools`,
  and `preflight_gate_active`. Every cell — gated or not — records
  these so post-hoc analysis can detect a silent failure pattern.

- **Inline gate.** Inside the stream-json read loop, the runner
  watches for the `system.init` event (always the first event CC
  emits). If the cell declared a cohort AND any declared server is
  not in the `connected` set, the runner:
  1. records `missing_mcp_tools` on the telemetry,
  2. sets `final_status = "FAILED_PREFLIGHT"`,
  3. emits the diagnostic receipt at `<cell_dir>/preflight-failure.json`,
  4. kills the CC subprocess before LLM exchange.

- **Ledger schema.** `FAILED_PREFLIGHT` is added to the recoverable
  state set (operator fixes the cohort, re-fires). Distinct from
  `FAILED_EMPTY` (permanent — re-run won't help) and `COMPLETED`.

- **MCP-cohort startup map.**
  `the organisation-bundle/canonical-test/harness-free-runner/mcp-cohort-startup-map.md`
  is the canonical reference for how every the organisation cohort tool starts
  its MCP server. The runner uses these invocations by default.

- **Tests.** Eight new tests in
  `tests/test_claude_code_runner.py` lock in: the gate fires on a
  partial cohort, doesn't fire on a clean cohort, doesn't fire when
  no cohort is declared, the matrix loader accepts the new field, a
  bad type for the field is rejected, the receipt is well-formed,
  and the cell-config relays the spec field.

## Consequences

### Positive

- **Measurement integrity.** No more silent failures from
  declared-but-unwired substrate. Every E-cell that claims "full
  agent-authority framework stack" can be VERIFIED to have full stack at start.
- **~$4 saved per invalidated cell.** The 2026-05-20 incident burned
  ~$4.24 on three structurally-invalid cells; the gate prevents that
  class of waste at zero LLM cost (it kills before the first token).
- **Diagnostic specificity.** `FAILED_PREFLIGHT` + the receipt's
  `missing_mcp_tools` field tells operators exactly which dependency
  needs fixing. Previous failure mode: "the bundle seems to add
  surprisingly little value over primer-alone" (which the operator
  cannot debug from the receipts alone).
- **Doctrine integrity.** agent-authority framework doctrine claims to apply audit-as-
  discipline. This ADR enforces that claim recursively, including
  on the runners that measure the doctrine itself. Dogfooding.

### Negative

- **Backward-compat surface.** All existing matrices keep working
  because the field is opt-in. But any operator who copy-pastes the
  prior E-cell config WITHOUT adding the `expected_mcp_tools` line
  will silently re-introduce the bug. Mitigation:
  `mcp-cohort-startup-map.md` is the single source of truth that the
  matrices should reference; the next Dx-numbered doctrine extension
  could make `expected_mcp_tools` mandatory for any cell with
  `tools: true` AND `bundle: ON`. Out of scope for this ADR.
- **Per-host invocation drift.** The gate validates that
  declared-name X registered. It does NOT validate that the
  registered server is the RIGHT version. A stale binary that
  registers a stale tool surface would pass the gate. Mitigation
  (future doctrine): tool-surface SHA pinning per cohort entry.

### Cost / dollars saved per future invalidated cell

The 2026-05-20 incident gives the empirical anchor: 3 cells at
canonical-scoring + bundling-wave cost ~$4.24 = ~$1.41 per
invalidated cell. The gate kills at zero LLM tokens, so each future
prevented cell saves ~$1.41 in canonical scoring + whatever the
runtime spend would have been (~$0.10-$2.20 per cell depending on
model class). Conservative envelope: ~$2-4 per prevented invalid
cell.

## Council 4-lens review

### Synthesis lens

What is this REALLY about? "Don't measure things you didn't actually
wire up". This is the same principle that says: a unit test that
import-fails should be a test failure, not a silent pass. The
runner is a measurement contract; the contract has preconditions;
preconditions must be checked. The wider point — applicable beyond
this ADR — is that agent-authority framework's load-bearing doctrine claim
(audit-as-discipline) must be self-applied. Any tool, harness, or
scorer that AUDITS the agent-authority framework bundle inherits the discipline.

### Adversarial lens

Where could this still fail?

1. **The gate trusts the registered-status signal.** If CC's
   `system.init` event is malformed or absent, `registered_mcp_tools`
   is empty and EVERY cell with a declared cohort fails preflight.
   Mitigation: the cell records the raw signal in telemetry so
   debugging the runner-vs-CC contract is possible.
2. **Operators may circumvent the gate by omitting `expected_mcp_tools`.**
   If your matrix-author skips the declaration, the gate is silent.
   This is intentional (backward compat) but means doctrine drift is
   possible. A future doctrine update could fail the matrix loader
   if a cell has `tools: true` AND `bundle: ON` AND no
   `expected_mcp_tools` — out of scope for this ADR.
3. **Wrapper scripts hide complexity.** host-policy-layer-mcp needs a
   wrapper-cmd that `cd`s before exec because CC's MCP config
   ignores `cwd`. The wrapper is per-host. If the host's host-policy-layer-mcp
   binary moves, the wrapper breaks silently. Mitigation: env vars
   in the wrapper + the startup-map documents where it should live.

### Cold-truth lens

The 2026-05-20 ablation burned ~$4.24 measuring an invalidated
cohort. That's not catastrophic — but the same class of failure on
a 3x5x5 matrix at model-high-capability rates would burn ~$200 and require operator
embarrassment to admit the receipts are invalid. This ADR is
correcting a small problem before it scales. The honest framing:
"we shipped a measurement runner that didn't apply our own central
doctrine to itself, found out empirically, and are now patching".
The doctrine generalises beyond this one runner — every agent-authority framework tool
that audits agent-authority framework-shaped surfaces should be evaluated against this
lens before its next release.

### Pragmatic lens

Implementation cost: ~1 hour for the runner change, ~30 min for the
tests, ~30 min for the matrix + ADR + cohort-startup-map docs.
Ongoing maintenance: zero — the gate is purely structural. The
runtime overhead is bounded by reading one extra JSON line at cell
start (the `system.init` event was already being parsed; we just
added a set-subtract). The wrapper script for host-policy-layer-mcp is a per-
host artefact that lives in the runner repo, so it ships in version
control.

Verdict: low cost, high diagnostic value, structurally aligned with
the doctrine the runner exists to measure. Adopt.

## References

- `the organisation-bundle/canonical-test/harness-free-runner/mcp-cohort-startup-map.md`
  — the canonical cohort startup invocations (post-Dx14 audit).
- `the organisation-bundle/canonical-test/harness-free-runner/claude_code_runner.py`
  — the gate implementation (branch `claude/dx14-fail-closed-gate-2026-05-20`).
- `the organisation-bundle/canonical-test/matrices/claude-code-3x5-bundle-on-dx14-refire.yaml`
  — first matrix using the gate (re-fire of the three invalid E cells).
- `the organisation-bundle/receipts/ablation-model-balanced-model-high-capability-cccli-2026-05-20/cells/cc-*-E/transcript.jsonl`
  — empirical evidence: six of seven mcp_servers status=failed.
- `the organisation-bundle/receipts/ablation-dx14-refire-2026-05-20/`
  — post-fix evidence: same three E cells re-fired with the gate active.
- agent-authority framework v3.4 algorithm Dx14: "declared-but-not-wired-fails-closed"
  doctrine. This ADR is its application to the runner itself.
