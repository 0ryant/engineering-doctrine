# Run Contracts

A **run contract** is a typed envelope that binds **trigger**, **model policy**, **context**, **capabilities**, **authority**, **hooks**, **verifiers**, and **outputs** into a single declarative shape. It is the first-class primitive of **governed execution**: every governed run authored, scheduled, or triggered in an adopting estate compiles down to a run-contract instance. There is no governed execution outside the envelope.

The canonical machine-readable shape lives at [../../contracts/run-contract.v1.schema.json](../../contracts/run-contract.v1.schema.json) (JSON Schema 2020-12). The companion verifier-pack pattern lives at [verifier-packs.md](verifier-packs.md). External licence: Apache-2.0, same as the rest of this library.

Relates to: [verifier-packs.md](verifier-packs.md) (the `verifiers` array consumes pack ids), [ai-native-software-development-lifecycle.md](ai-native-software-development-lifecycle.md) (multi-agent lineage, checkpoints, safe resume, and lifecycle authority outside the single-run envelope), [webhook-ingress-security.md](webhook-ingress-security.md) (webhook trigger hardening), [idempotency-across-boundaries.md](idempotency-across-boundaries.md) (retry semantics for non-cron triggers), [code-review-and-change-approval.md](code-review-and-change-approval.md) (manual triggers and high-risk approvals), [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) (governed AI systems), [../principles/audit-logging.md](../principles/audit-logging.md) (`outputs.audit.jsonl_path`), [../principles/single-source-of-truth.md](../principles/single-source-of-truth.md) (one envelope shape, one home).

---

## 1. Why Run Contracts Exist

Without a binding envelope, agents inherit **ambient affordance**: whatever tool, skill, network, filesystem, environment variable, subprocess, or model is in scope is implicitly available. Two evidence classes drove the v1 shape:

1. **Skill-amplified confabulation.** A skill paired with no falsification surface gives weaker models a confidence prime without an evidence discipline. The structural fix: bind the skill to a verifier pack via `context.skills` and `verifiers`.
2. **Silent-stub success.** A CLI prints *"Evidence written to: …"* and exits `0` without writing the file; an agent reads stdout, accepts success, self-scores PASS. The structural fix: declare the artefact in `outputs.required` and let a verifier check existence.

A run contract collapses both into one envelope. Trigger says **when**; model policy says **who**; context and capabilities say **with what**; authority says **inside what membrane**; hooks say **with what gates**; verifiers say **what gets proven after**; outputs say **what must exist**.

### 1.1 When A Run Is Governed

A model interaction becomes governed execution when any of these are true:

- it invokes tools or subprocesses;
- it mutates a persistent artefact or external system;
- it receives sensitive, non-public, or externally controlled data;
- it runs asynchronously, delegates, or can outlive the initiating interaction;
- it consumes a material time, token, compute, or financial budget;
- it crosses repository, service, environment, tenant, or organisational boundaries;
- its output can enter a controlled delivery or operational path without full inspection; or
- a decision-maker will rely on the result without fully inspecting the underlying work.

Autocomplete, explanation, comment rewriting, idea generation, and other ephemeral assistance may remain ordinary model interaction when a person fully inspects the result and no trigger above applies. If that output becomes part of a software candidate, the candidate still follows normal review, CI, security, authority, and release controls.

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

Trigger -> instantiate -> execute -> verify -> emit-artefacts is the only legal shape for governed execution. A governed agent running without a contract is a runtime error, not a missing-doc problem.

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

Each value is an ordered array of hook-action ids. Hook actions themselves are defined by the host runtime (host-runtime enforcement) and are out of scope for the contract schema — the contract names *what runs when*, not how the action is implemented.

### 3.4 Outputs

`outputs.required` MUST be non-empty. An explicit `required: []` is rejected at validation. Even research-only runs declare at minimum an `audit/run.jsonl` path. This is the structural close on the silent-stub class: a verifier pack runs `test -s ${path}` against every `required` entry and fails loudly if the file is absent or empty.

### 3.5 Policy-injected skills

An adopting estate MAY configure its contract compiler to inject an approved skill or prompt policy for a declared class of work. Injection is an estate control, not a universal list maintained by this library. The expanded contract MUST record the injected component, its version or digest, the policy rule that selected it, and any companion verifier.

Policy injection has four constraints:

1. **Evaluated.** The estate has measured the intervention against representative tasks and material failure modes. Prompting is not proof and does not replace independent verification.
2. **Deterministic selection.** The same declared inputs and policy version select the same components; the agent does not decide whether its own control applies.
3. **Observable.** The materialised contract and run receipt show what was injected. Silent prompt or skill mutation is inadmissible.
4. **Governed exceptions.** Bypass requires explicit, scoped authority and leaves the underlying verification obligation intact.

See [anti-confabulation-priming.md](anti-confabulation-priming.md) for one optional intervention and the evidence needed before adopting it.

---

## 4. Worked Example: `evidence-pack-build-review`

This illustrative shape describes a PR-triggered build and review contract. The YAML validates against [../../contracts/run-contract.v1.schema.json](../../contracts/run-contract.v1.schema.json):

```yaml
run_contract:
  name: evidence-pack-build-review
  schema_version: 1.0.0
  description: On every PR to example-org/evidence-pack build the evidence pack then have an LLM review it.

  trigger:
    type: repo_event
    repo: example-org/evidence-pack
    events: [pull_request_opened, pull_request_synchronize]

  model_policy:
    allowed_models: [provider/model-default, provider/model-premium]
    disallow_models: [provider/model-unqualified]
    fallback: fail

  context:
    skills: [evidence-pack-mcp, cargo-build-and-test]
    memory:
      mode: verified_only
      max_items: 32
      ceiling: RemoteSigned

  capabilities:
    tools:
      - evidence-pack.collect
      - evidence-pack.verify
      - cargo.build
      - cargo.test
      - review.claim_audit

  authority:
    filesystem:
      root: /work/evidence-pack
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
        - /usr/local/bin/evidence-pack

  hooks:
    before_tool_use: [log-tool-id, deny-out-of-scope-tools]
    after_tool_use: [record-output-hash]
    before_final_answer: [enforce-outputs-required-exists]
    on_stop: [close-audit-log, emit-run-receipt]

  verifiers:
    - evidence-pack-mcp-verifier-pack
    - cargo-build-and-test-verifier-pack
    - review-claim-audit-meta-pack

  outputs:
    required:
      - out/pack.json
      - audit/run.jsonl
      - target/release/evidence-pack
    optional:
      - "target/criterion/**"
    audit:
      jsonl_path: audit/run.jsonl
      content_addressable: true
```

Read as one sentence: *on a PR against `example-org/evidence-pack`, use an approved default or premium model (never an unqualified model), with two paired skills and five listed tools, inside the `/work/evidence-pack` root, network denied, three subprocess binaries allowed, four hook chains installed, three packs run after, and three artefacts that MUST exist at exit*. No ambient affordance escapes the envelope. The contract is harness-agnostic — any agent harness that targets the run-contract v1 schema is a valid consumer.

---

## 5. Worked Example: `nightly-evidence-pack-audit`

The same shape, cron-triggered, narrower capability surface:

```yaml
run_contract:
  name: nightly-evidence-pack-audit
  schema_version: 1.0.0
  description: Nightly at 02:00 UTC re-verify every recent evidence pack and emit an estate-health summary.

  trigger:
    type: cron
    schedule: "0 2 * * *"
    timezone: UTC
    jitter_seconds: 600

  model_policy:
    allowed_models: [provider/model-default]
    disallow_models: [provider/model-unqualified]
    fallback: fail

  context:
    skills: [evidence-pack-mcp]
    memory:
      mode: verified_only
      max_items: 16
      ceiling: RemoteSigned

  capabilities:
    tools: [evidence-pack.verify, review.claim_audit]

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
      allowed: [/usr/local/bin/evidence-pack]

  hooks:
    before_run: [acquire-nightly-lock]
    after_run: [release-nightly-lock]
    on_stop: [close-audit-log, emit-run-receipt]

  verifiers:
    - evidence-pack-mcp-verifier-pack
    - estate-health-summary-pack

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

- **NOT a workflow DAG.** A contract describes one execution unit. Multi-step orchestration belongs to a workflow engine or saga coordinator; cross-contract dependency is out of scope for v1. The coordinator still records the parent/child fingerprints, delegated scopes, dependencies, workspace ownership, checkpoints, handoffs, and integration outcome required by [ai-native-software-development-lifecycle.md](ai-native-software-development-lifecycle.md); each child has its own contract.
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

## 8. Implementation Contract

An implementation may use any language or orchestration platform. Conforming implementations MUST reject unknown fields, validate against the published schema, compute a stable fingerprint over the canonical body, enforce the declared authority independently of the model, resolve verifier-pack identifiers, and emit a receipt bound to the contract fingerprint.

Implementations that emit or consume run contracts SHOULD identify the schema version and link to this pattern. A library, generator, runtime, or review engine is a consumer of the contract; none is doctrine authority or the sole reference implementation.

---

## 9. Honest v1 Gap

The v1 envelope does **not** address:

- **Workflow DAG composition.** Multi-step orchestration ("contract A's output is contract B's input") is out of scope. Until a portable workflow primitive exists, an external coordinator owns the lineage and coordination record without mutating either contract. v2 may introduce a `dependencies: [<fingerprint>]` field or a separate workflow primitive that wraps contracts.
- **Checkpoint and resume identity.** v1 has `on_stop` and durable required outputs but no lease, checkpoint, or resume token. A stopped/expired run must not silently continue in place: the host closes its audit record and revalidates authority/context before instantiating a new run linked to the predecessor. A future workflow or contract version may type this link.
- **Cross-contract atomicity.** No transactional rollback across instances. If A succeeds and B fails, A's effects stand. Compensation belongs to a higher-level saga.
- **Live mutation.** A running contract cannot edit itself. Authors edit the source, re-validate, and the *next* instance picks it up — intentional, but it pushes some workflows (e.g. probe-then-widen-network) into multi-contract designs.
- **Streaming triggers.** Long-lived stream subscriptions (Kafka, NATS subjects, MQTT) are out of scope and need either a bridge adapter or a v2 `stream` type.
- **Per-contract budget.** No `budget` field for tokens, wall time, or dollars. For v1, a host or workflow policy owns and enforces the budget and binds its policy version and result to the run receipt; prose in a prompt is not enforcement. A later schema version may type these limits.

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
| One contract per governed execution | Multi-agent coordination composes separately fingerprinted envelopes; an orchestrator cannot widen a child by inheritance or hide delegation inside one run. |

---

## Related

- [verifier-packs.md](verifier-packs.md) — what `verifiers: [...]` resolves to.
- [webhook-ingress-security.md](webhook-ingress-security.md), [idempotency-across-boundaries.md](idempotency-across-boundaries.md) — trigger hardening and retry semantics.
- [code-review-and-change-approval.md](code-review-and-change-approval.md) — review path for high-blast-radius contracts.
- [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md), [../principles/single-source-of-truth.md](../principles/single-source-of-truth.md) — governed AI systems; canonical home.
- [../../contracts/run-contract.v1.schema.json](../../contracts/run-contract.v1.schema.json), [../../scripts/validate-contracts-v1.py](../../scripts/validate-contracts-v1.py) — schema and reference validator.
