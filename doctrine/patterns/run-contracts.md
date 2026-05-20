# Run Contracts

A **run contract** is a typed envelope that binds **trigger**, **model policy**, **context**, **capabilities**, **authority**, **hooks**, **verifiers**, and **outputs** into a single declarative shape. It is the **first-class primitive of agent execution**: every run authored, scheduled, or triggered in a cohort compiles down to a run-contract instance. There is no agent execution outside the envelope.

The canonical machine-readable shape lives at [../../contracts/run-contract.v1.schema.json](../../contracts/run-contract.v1.schema.json) (JSON Schema 2020-12). The companion verifier-pack pattern lives at [verifier-packs.md](verifier-packs.md). External licence: Apache-2.0, same as the rest of this library.

Relates to: [verifier-packs.md](verifier-packs.md) (the `verifiers` array consumes pack ids), [webhook-ingress-security.md](webhook-ingress-security.md) (webhook trigger hardening), [idempotency-across-boundaries.md](idempotency-across-boundaries.md) (retry semantics for non-cron triggers), [code-review-and-change-approval.md](code-review-and-change-approval.md) (manual triggers and high-risk approvals), [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) (governed AI systems), [../principles/audit-logging.md](../principles/audit-logging.md) (`outputs.audit.jsonl_path`), [../principles/single-source-of-truth.md](../principles/single-source-of-truth.md) (one envelope shape, one home).

---

## 1. Why Run Contracts Exist

Without a binding envelope, agents inherit **ambient affordance**: whatever tool, skill, network, filesystem, environment variable, subprocess, or model is in scope is implicitly available. Two evidence classes drove the v1 shape:

1. **Skill-amplified confabulation.** A skill paired with no falsification surface gives weaker models a confidence prime without an evidence discipline. The structural fix: bind the skill to a verifier pack via `context.skills` and `verifiers`.
2. **Silent-stub success.** A CLI prints *"Evidence written to: …"* and exits `0` without writing the file; an agent reads stdout, accepts success, self-scores PASS. The structural fix: declare the artefact in `outputs.required` and let a verifier check existence.

A run contract collapses both into one envelope. Trigger says **when**; model policy says **who**; context and capabilities say **with what**; authority says **inside what membrane**; hooks say **with what gates**; verifiers say **what gets proven after**; outputs say **what must exist**.

---

## 2. Lifecycle

Five phases. The body is **content-addressable**: a sha256 fingerprint anchors the audit trail.

| Phase | What happens |
| --- | --- |
| 1. Author | Operator (or higher-level compiler) writes a contract YAML/JSON. |
| 2. Validate | Schema check; fingerprint computed; verifier-pack existence check. |
| 3. Trigger | Trigger source fires; contract is instantiated; fingerprint flows forward. |
| 4. Execute | Executor enforces capabilities + authority at the membrane; emits hook events. |
| 5. Verify & emit | Packs run against `outputs.required`; verdict (pass / fail_loud / mark_untrusted / inconclusive) + audit log. |

Trigger -> instantiate -> execute -> verify -> emit-artefacts is the **only** legal execution shape. An agent running without a contract is a runtime error, not a missing-doc problem.

---

## 3. Schema Surface

The v1 schema declares **eleven top-level keys**. All object levels set `additionalProperties: false`: unknown fields are rejected loudly (the JSON Schema equivalent of `#[serde(deny_unknown_fields)]`).

| Key | Required | Purpose |
| --- | --- | --- |
| `name` | yes | Kebab-case identifier; doubles as audit-log scope. |
| `schema_version` | yes | `1.x.y` — semver of this schema. |
| `fingerprint` | generated | `sha256:<hex>` of the canonicalised body. |
| `description` | no | One-sentence summary. |
| `trigger` | yes | One of 6 trigger types (`cron`, `webhook`, `repo_event`, `file_event`, `email`, `manual`). |
| `model_policy` | yes | `allowed_models` plus explicit `disallow_models`. |
| `context` | yes | `skills` (each must have a verifier pack) and `memory` mode. |
| `capabilities` | yes | Closed `tools` set. |
| `authority` | yes | `filesystem`, `env`, `network`, `subprocess` — typed-denial defaults. |
| `hooks` | yes | Map keyed by hook name; values are ordered hook-action arrays. |
| `verifiers` | yes | Closed set of verifier-pack ids; empty array is legal but loud. |
| `outputs` | yes | `required` (non-empty), `optional`, `audit.jsonl_path`. |

### 3.1 Trigger types (6)

| Type | Discriminator fields |
| --- | --- |
| `cron` | `schedule`, optional `timezone`, `jitter_seconds` |
| `webhook` | `endpoint`, `signature_scheme` (`hmac_sha256` / `ed25519` / `none`), `shared_secret_ref` |
| `repo_event` | `repo`, `events` (PR / push / issue / release / tag), `branch_filter` |
| `file_event` | `paths`, `events` (created / modified / deleted / renamed), `debounce_ms` |
| `email` | `mailbox`, `from_allow_list`, `subject_filter` |
| `manual` | `operator_id`, `approval_required` |

`signature_scheme: none` is a typed declaration that the webhook is *intentionally* unsigned; it is not a silent omission. See [webhook-ingress-security.md](webhook-ingress-security.md) for the surrounding ingress hardening.

### 3.2 Authority axes (4)

Every axis defaults to typed denial:

- **filesystem** — `root` is required; `writable` defaults to read-only.
- **env** — `inherit: false` is the typed-denial default; `allow: [...]` is the explicit list.
- **network** — `mode` is one of `deny` or `allow_list`. There is **no `allow_all`**; that omission is intentional.
- **subprocess** — `allowed` is either a boolean or a closed list of absolute binary paths.

### 3.3 Hooks (13)

The canonical 13-hook list:

```
before_run, after_run,
before_tool_use, after_tool_use,
before_subprocess_spawn, after_subprocess_exit,
before_file_write, after_file_write,
before_network_access,
before_final_answer,
on_claim_emitted,
on_stop,
on_error
```

Each value is an ordered array of hook-action ids. Hook actions themselves are defined by the host runtime (corcept-class enforcement) and are out of scope for the contract schema — the contract names *what runs when*, not how the action is implemented.

### 3.4 Outputs

`outputs.required` MUST be non-empty. An explicit `required: []` is rejected at validation. Even research-only runs declare at minimum an `audit/run.jsonl` path. This is the structural close on the silent-stub class: a verifier pack runs `test -s ${path}` against every `required` entry and fails loudly if the file is absent or empty.

### 3.5 Auto-bundled skills

A subset of skills is **auto-bundled** by the validator at contract instantiation. If `context.skills` contains any skill tagged `kind: "build-class"` in its manifest (e.g. `pr-evidence-build`, `pr-evidence-mcp`, `mcpact-codegen`, `aegress-implementation`, `cargo-build-and-test`), the validator MUST also inject the [`anti-confabulation`](anti-confabulation-priming.md) skill into `context.skills` and the sibling `anti-confabulation-verifier-pack` into `verifiers`. Auto-bundling is **mandatory**, not opt-in.

The empirical mandate is direct: Stage 2 measurement found Sonnet 4.6's canonical score lifted from 78 to 85 (+7) and its calibration delta tightened from +11 to −1 (12-point tightening) when the cell received the canonical anti-confabulation priming block. Holding model and backbone fixed, the only changed variable was priming (`value-sheet/18-cross-product-test/v2/results/test-1-backbone/canonical-scoring-sonnet-primed.md:238-251`). The same intervention on Opus 4.7 produced delta 0 (`canonical-scoring-opus.md:52`) and delta −2.5 (line 53). The intervention costs ~200 tokens per run and the lift is reproducible.

The auto-bundle rule has three properties:

1. **Validator-enforced, not author-enforced.** Operators authoring build-class contracts MUST NOT need to remember to add `anti-confabulation`. The validator auto-injects both the skill and its sibling pack. The author MAY add them explicitly; the validator MUST NOT reject explicit duplicates.
2. **Doctrine-grade tag set.** The list of `kind: "build-class"` skills is doctrine-grade. Adding or removing a build-class tag from a skill manifest requires a doctrine PR. Operators who want priming on a non-build-class task can still add `anti-confabulation` explicitly to `context.skills`, but they cannot disable the auto-bundle by removing the explicit entry — the validator re-injects.
3. **Verifier pack is mandatory.** The bundled skill ships a sibling [`anti-confabulation-verifier-pack`](anti-confabulation-priming.md#55-verifier-pack-pairing) containing one verifier of kind `priming_active` (the 11th canonical kind in [verifier-packs.md §3](verifier-packs.md#3-the-10-canonical-verifier-kinds)). The verifier `fail_loud`s if the rendered system prompt does not contain the canonical priming block byte-for-byte, hash-matched by SHA-256.

The full pattern, including the verbatim priming block, the canonical SHA-256 (`c138dd966c82f7bd792684ab3fef0f50d75aa9342468db8b5d265f24f3fb35a8`), forces, consequences, and the honest gap list, lives at [anti-confabulation-priming.md](anti-confabulation-priming.md).

---

## 4. Worked Example: `pr-evidence-build-review`

The operator's verbatim shape for a PR-triggered build + review contract. This YAML validates byte-for-byte against [../../contracts/run-contract.v1.schema.json](../../contracts/run-contract.v1.schema.json):

```yaml
run_contract:
  name: pr-evidence-build-review
  schema_version: 1.0.0
  description: On every PR to pai-axiom/pr-evidence build the evidence pack then have an LLM review it.

  trigger:
    type: repo_event
    repo: pai-axiom/pr-evidence
    events: [pull_request_opened, pull_request_synchronize]

  model_policy:
    allowed_models: [opus, sonnet]
    disallow_models: [haiku]
    fallback: fail

  context:
    skills: [pr-evidence-mcp, cargo-build-and-test]
    memory:
      mode: verified_only
      max_items: 32
      ceiling: RemoteSigned

  capabilities:
    tools:
      - pr-evidence.collect
      - pr-evidence.verify
      - cargo.build
      - cargo.test
      - tapprove.claim_audit

  authority:
    filesystem:
      root: /work/pr-evidence
      writable: [target/, out/, audit/]
      readable: [src/, Cargo.toml, Cargo.lock]
    env:
      inherit: false
      allow: [PATH, RUSTUP_HOME, CARGO_HOME]
    network:
      mode: deny
    subprocess:
      allowed:
        - /usr/bin/cargo
        - /usr/bin/git
        - /usr/local/bin/pr-evidence

  hooks:
    before_tool_use: [log-tool-id, deny-out-of-scope-tools]
    after_tool_use: [record-output-hash]
    before_final_answer: [enforce-outputs-required-exists]
    on_stop: [close-audit-log, emit-cortex-receipt]

  verifiers:
    - pr-evidence-mcp-verifier-pack
    - cargo-build-and-test-verifier-pack
    - tapprove-claim-audit-meta-pack

  outputs:
    required:
      - out/pack.json
      - audit/run.jsonl
      - target/release/pr-evidence
    optional:
      - "target/criterion/**"
    audit:
      jsonl_path: audit/run.jsonl
      content_addressable: true
```

Read as one sentence: *on a PR against `pai-axiom/pr-evidence`, run as opus-or-sonnet (never haiku), with two paired skills and five listed tools, inside the `/work/pr-evidence` root, network denied, three subprocess binaries allowed, four hook chains installed, three packs run after, three artefacts MUST exist at exit*. No ambient affordance escapes the envelope.

---

## 5. Worked Example: `nightly-pr-evidence-audit`

The same shape, cron-triggered, narrower capability surface:

```yaml
run_contract:
  name: nightly-pr-evidence-audit
  schema_version: 1.0.0
  description: Nightly at 02:00 UTC re-verify every recent pr-evidence pack and emit a cohort-health summary.

  trigger:
    type: cron
    schedule: "0 2 * * *"
    timezone: UTC
    jitter_seconds: 600

  model_policy:
    allowed_models: [sonnet]
    disallow_models: [haiku]
    fallback: fail

  context:
    skills: [pr-evidence-mcp]
    memory:
      mode: verified_only
      max_items: 16
      ceiling: RemoteSigned

  capabilities:
    tools: [pr-evidence.verify, tapprove.claim_audit]

  authority:
    filesystem:
      root: /work/nightly-audit
      writable: [out/, audit/]
    env:
      inherit: false
      allow: [PATH]
    network:
      mode: deny
    subprocess:
      allowed: [/usr/local/bin/pr-evidence]

  hooks:
    before_run: [acquire-nightly-lock]
    after_run: [release-nightly-lock]
    on_stop: [close-audit-log, emit-cortex-receipt]

  verifiers:
    - pr-evidence-mcp-verifier-pack
    - cohort-health-summary-pack

  outputs:
    required: [out/summary.json, audit/run.jsonl]
    audit:
      jsonl_path: audit/run.jsonl
      content_addressable: true
```

The trigger swaps `repo_event` for `cron`; the rest of the envelope is structurally identical. That is the abstraction's value — six trigger types compile to one shape, and reviewers reason about one shape.

---

## 6. What This Is NOT

The shape is deliberately small. The boundary matters as much as the interior.

- **NOT a workflow DAG.** A contract describes one execution unit. Multi-step orchestration belongs to a workflow engine or saga coordinator; cross-contract dependency is out of scope for v1.
- **NOT an inline scripting language.** `hooks` and `verifiers` reference **named ids**, not embedded shell. Embedding scripts inside the envelope would re-create the ambient-affordance problem at a different layer.
- **NOT a model-controlled escape hatch.** An agent cannot rewrite its own contract mid-run. The model receives the envelope as input; it does not edit it.
- **NOT a substitute for code review.** High-blast-radius contracts still route through [code-review-and-change-approval.md](code-review-and-change-approval.md).
- **NOT a secret store.** `shared_secret_ref` holds **references** to credentials, never the credentials themselves; see [../principles/configuration-and-secrets.md](../principles/configuration-and-secrets.md).
- **NOT a deployment manifest.** The contract describes one *run*, not the long-lived deployment that hosts it; see [gitops-and-declarative-operations.md](gitops-and-declarative-operations.md).

---

## 7. Validation Tooling

Contracts are themselves validated; validators are simpler than runs.

| Validator | What it checks |
| --- | --- |
| Schema check | required fields, types, `additionalProperties: false`. |
| Capability closure | every `capabilities.tools[i]` resolves to a known MCP tool with a matching authority class. |
| Authority coherence | `network.mode: deny` is incompatible with a network-using tool in `capabilities.tools`. |
| Verifier-pack existence | every `verifiers[i]` resolves to a real pack (see [verifier-packs.md](verifier-packs.md)). |
| Fingerprint stability | same canonical body produces same `sha256`. |
| Skill-pack pairing | every `context.skills[i]` has a sibling verifier pack. |

A reference Python validator at [../../scripts/validate-contracts-v1.py](../../scripts/validate-contracts-v1.py) uses `jsonschema` against the JSON Schema 2020-12 draft. Consumers SHOULD wire it into CI.

---

## 8. Cohort Cross-Links

Run contracts are the canonical home for the abstraction per the 2026-05-19 single-source-of-truth decision. Cohort adoption surfaces:

- **`mcpact/crates/mcpact-run-contract/`** (forthcoming) — Rust crate with `serde`-typed structs and `#[serde(deny_unknown_fields)]` on every struct; same fingerprint as the JSON Schema reference path.
- **`tapprove/crates/tapprove-mcp/src/claim_audit/`** (forthcoming) — canonical post-run verifier engine; consumer of `verifiers: [tapprove.claim_audit]`.
- **Reference adopters:** `corcept.mcpact.toml` (host-side hook enforcement); `aegress` forthcoming (starter contract per generated MCP tool); `cordance-bridge` forthcoming (pure-function translator inside a contract).

Tools in the cohort that emit or consume contracts MUST link back to this file as the v1 source of truth.

---

## 9. Honest v1 Gap

The v1 envelope does **not** address:

- **Workflow DAG composition.** Multi-step orchestration ("contract A's output is contract B's input") is out of scope. v2 may introduce a `dependencies: [<fingerprint>]` field or a separate workflow primitive that wraps contracts.
- **Cross-contract atomicity.** No transactional rollback across instances. If A succeeds and B fails, A's effects stand. Compensation belongs to a higher-level saga.
- **Live mutation.** A running contract cannot edit itself. Authors edit the source, re-validate, and the *next* instance picks it up — intentional, but it pushes some workflows (e.g. probe-then-widen-network) into multi-contract designs.
- **Streaming triggers.** Long-lived stream subscriptions (Kafka, NATS subjects, MQTT) are out of scope and need either a bridge adapter or a v2 `stream` type.
- **Per-contract budget.** No `budget` field for tokens, wall time, or dollars. Budgeting is left to the host runtime and `performance-and-cost`-class observability.

These gaps are explicit — the boundary of v1, not bugs in it.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Single envelope, no shortcuts | A contract that omits a required key cannot be reviewed for what it is missing. |
| `additionalProperties: false` everywhere | Loud rejection of unknown fields closes a tamper class. |
| Network `deny` default, no `allow_all` | Removing the option removes the temptation. |
| `outputs.required` non-empty | Silent-stub class is the largest single failure mode this primitive closes. |
| 6 trigger types, no `else` branch | Each branch is reviewable; an open-ended `custom` would defeat the purpose. |
| Hooks reference ids, not embedded scripts | Pushes script surface to a named, reviewable, host-runtime registry. |

---

## Related

- [verifier-packs.md](verifier-packs.md) — what `verifiers: [...]` resolves to.
- [webhook-ingress-security.md](webhook-ingress-security.md), [idempotency-across-boundaries.md](idempotency-across-boundaries.md) — trigger hardening and retry semantics.
- [code-review-and-change-approval.md](code-review-and-change-approval.md) — review path for high-blast-radius contracts.
- [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md), [../principles/single-source-of-truth.md](../principles/single-source-of-truth.md) — governed AI systems; canonical home.
- [../../contracts/run-contract.v1.schema.json](../../contracts/run-contract.v1.schema.json), [../../scripts/validate-contracts-v1.py](../../scripts/validate-contracts-v1.py) — schema and reference validator.
