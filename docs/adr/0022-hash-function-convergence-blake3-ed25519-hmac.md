# ADR-0022 — Hash function convergence: BLAKE3 (content) + Ed25519 (signatures) + HMAC (MAC)

**Status:** Proposed 2026-05-20
**Decision:** Operator-locked 2026-05-20
**Supersedes:** —
**Related:** ADR-0021 (audit-as-discipline applies to runner itself)

## Context

The the organisation Suite cohort uses 4 different hash families across catalog
tools today:

- **BLAKE3** — `memory-service` (hash-chained memory ledger; receipt envelopes)
- **SHA-256** — most tools (event hashes, content addresses, receipt SHAs
  in drift-control / tool-contract-generator / pipeline-authority-analyser / engineering-doctrine schemas / etc.)
- **HMAC** (over SHA-256) — `secret-broker` (audit-trail line MAC)
- **Ed25519** — `execution-sandbox` (CloudEvent signatures), `provenance-verifier`
  (artifact-egress signatures), `run-contract-composer` (decision-packet signing)

The conformance v2 matrix flagged this as cross-cutting pattern #5
("hash-function convergence") and listed it as an operator decision.

The lack of convergence costs:

1. **Cohort-wide verification scripts** can't assume one hash family;
   they must dispatch per-tool.
2. **Customer tooling that wants to verify the organisation Suite receipts** has to
   ship 2 hashing libraries (BLAKE3 + SHA-256) plus signature libs.
3. **Doctrine clarity** suffers: when a new catalog tool is added,
   "which hash should I use?" has no canonical answer.

## Decision

**Canonical hash family per use-case:**

| Use-case | Canonical algorithm | Library | Rationale |
|----------|---------------------|---------|-----------|
| Content addressing (hash chains, receipts, file content fingerprints) | **BLAKE3** | `blake3` (Rust crate, MIT/Apache-2.0) | Modern, fast (~3 GB/s single-threaded), 256-bit output, no known weaknesses. `memory-service` already canonical. |
| Digital signatures | **Ed25519** | `ed25519-dalek` (Rust crate, BSD-3) | Already canonical for `execution-sandbox`, `provenance-verifier`, `run-contract-composer`. Industry standard; small keys / signatures; constant-time. |
| Message Authentication Code (MAC over secrets) | **HMAC-SHA256** | `hmac` + `sha2` (RustCrypto) | Narrow scope — only when MAC is genuinely needed (e.g., `secret-broker` audit-trail line authentication where the receiver shares a secret). NOT a general content-addressing replacement. |

**Forbidden / deprecated:**

- **SHA-256 as a content address** (when not part of HMAC) is
  deprecated for new code. Migration: BLAKE3 replaces it.
- **MD5, SHA-1, BLAKE2** — not in scope; do not introduce.
- Re-implementing any of these from scratch — use the named crates.

## Migration

### Tools that ALREADY match canonical

- `memory-service` — BLAKE3 ✓
- `execution-sandbox` — Ed25519 ✓
- `provenance-verifier` — Ed25519 ✓
- `run-contract-composer` — Ed25519 ✓
- `secret-broker` — HMAC-SHA256 ✓ (narrow scope: audit-line MAC)

### Tools that need migration (SHA-256 content addressing → BLAKE3)

To be enumerated in a follow-up `standardisation/hash-functions/CONFORMANCE.md`
audit. Likely candidates from conformance v2 matrix:

- `tool-contract-generator` — receipt-emission pattern uses SHA-256 hashes; migrate to
  BLAKE3 for content addressing
- `drift-control` — TaskGraph hash-chained audit events use SHA-256;
  migrate to BLAKE3
- `pipeline-authority-analyser` — authority-graph fingerprints use SHA-256; migrate to BLAKE3
- `host-policy-layer` — receipt content hashes use SHA-256; migrate to BLAKE3
- `independent-review-engine` — artifact trust-graph hashes use SHA-256; migrate to BLAKE3
- `doctrine-adapter` — citation provenance hashes use SHA-256; migrate to
  BLAKE3 (priming-block SHA-256 stays SHA-256 ONLY if the priming-block
  is consumed by external verifiers that expect SHA-256; otherwise migrate)

### Migration order

1. **Phase 1**: write `ecosystem-catalog/standardisation/hash-functions/CONFORMANCE.md`
   auditing every tool's current hash usage with citations.
2. **Phase 2**: per-tool migration PRs (one PR per tool; ~5 LOC each
   for the hash constructor + tests). Bump tool minor version.
3. **Phase 3**: receipt-format ADR amendment in the relevant tool's
   ADRs noting the hash transition (consumers reading old receipts need
   a fallback during the transition).
4. **Phase 4**: customer-facing receipts format change announced in
   the bundle CHANGELOG.

## Consequences

### Positive

- One content-addressing hash across the cohort.
- Cohort-wide verifier scripts can assume BLAKE3 (single library).
- New catalog tools have a canonical answer to "which hash?"
- BLAKE3's speed is a real win for `memory-service`'s ledger and any large-file
  hashing.

### Negative

- ~5 tools need migration PRs.
- Existing receipts in customer environments may have SHA-256 hashes;
  consumers need fallback during transition.
- BLAKE3 is less widely known than SHA-256; customer-side verifier
  scripts need a BLAKE3 library (not in OS standard sets the way SHA-256
  is in `openssl`).

### Out of scope

- Choosing between BLAKE3 keyed mode and HMAC for MAC. HMAC is the
  canonical choice for the narrow MAC use-case; BLAKE3 keyed mode is
  not adopted to keep the use-case → algorithm mapping clean.
- Argon2 / scrypt / etc. (password hashing). The cohort doesn't store
  passwords. Not in scope.
- Post-quantum signatures. When the cohort adopts a post-quantum
  scheme, a successor ADR replaces Ed25519 here.

## Verification

A new `ecosystem-catalog/standardisation/hash-functions/CONFORMANCE.md`
will audit every tool's hash usage and track migration. Compliance is
binary: a tool either uses the canonical hash for each use-case or it
does not.

## References

- BLAKE3 paper + spec: https://github.com/BLAKE3-team/BLAKE3-specs
- Ed25519 RFC 8032
- HMAC RFC 2104
- Operator decision in AskUserQuestion 2026-05-20: option (a) selected
  from the portfolio-tasks §2 hash-convergence decision
- Cohort hash audit citations:
  - `memory-service/crates/memory-service-core/src/hash.rs` (BLAKE3)
  - `execution-sandbox/crates/execution-sandbox-core/src/sign.rs` (Ed25519)
  - `secret-broker/crates/secret-broker-core/src/audit.rs` (HMAC-SHA256)
