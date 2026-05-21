# 0019. Auto-Cortex Promotion of New Auto-Memories (Per-Session Opt-In)

Status: Proposed
Decision date: 2026-05-20
Recorded date: 2026-05-20
Retrospective: No

## Context

The agent (Claude Code or equivalent) maintains two persistence surfaces:

1. **Auto-memory** at `~/.claude/projects/<project>/memory/` — per-session files indexed by `MEMORY.md`. Used as the agent's private cache, recalled in future sessions via the agent's own prompt-loading.

2. **Cortex active memory** — the cross-session, cross-agent queryable substrate. Token-gated for `session_commit` and `memory_accept`. The autonomous `cortex_memory_note` tool exists for "operator-attested facts" (per its tool description) and writes directly to active memory.

Today these two surfaces are NOT connected. The operator must explicitly say "promote X to cortex" for findings to cross over. This creates friction: every session's discoveries (empirical findings, operator methodology locks, patterns) stay siloed in auto-memory unless manually re-stated.

Concurrently, ADR-0047 (cortex memory boundary) protects against **same-session self-reinforcement**: the LLM should not write to memory then read its own writes as ground truth within the same session. The protection is the token-gated commit path (`cortex_session_commit`, `cortex_memory_accept`). The `cortex_memory_note` tool is autonomous and therefore lives outside that explicit gate.

## Decision

**Enable auto-cortex-promotion of new auto-memories with PER-SESSION OPT-IN.** The operator opts in once at session start (when the cortex MCP server loads). For the rest of the session, the agent auto-fires `cortex_memory_note` on every new auto-memory file write that passes the eligibility filter.

### Mechanism

1. **At MCP startup**, the cortex server prints (alongside its confirmation token):
   ```
   cortex serve: confirmation token: <token>
   cortex serve: auto-promote new auto-memories to active store? [y/N]
   ```
   The operator answers `y` to enable; `N` (default) keeps manual promotion.

2. **Cortex stores the session flag** (`auto_promote: bool`) keyed by session ID. The flag is session-scoped and resets on every cortex serve restart.

3. **Agent queries the flag** at session start via a new tool `cortex_session_config()` (returns `{ auto_promote: bool, session_id: str, ... }`). Agent caches the answer for the session.

4. **When the agent writes a new file to `~/.claude/projects/<project>/memory/`**:
   - If `auto_promote: true` AND the new memory passes the eligibility filter (see §Eligibility filter): auto-call `cortex_memory_note(claim, confidence, domains)` with content synthesized from the memory file
   - If `auto_promote: false`: do NOT auto-promote. The memory stays in auto-memory only.

5. **At end of session** (in the agent's final summary): list the cortex memory IDs that were auto-promoted, so the operator can scan + revoke via `cortex_memory_outcome(memory_id, ..., NotUseful)`.

### Eligibility filter

Only memories matching ALL of the following are auto-promoted:

1. **Type ∈ {user, feedback, project, reference}** per the CLAUDE.md auto-memory taxonomy. Session-ephemeral state (TodoWrite, in-progress task tracking) is NOT auto-promoted.
2. **Confidence ≥ 0.8** — see §Confidence calibration. Lower-confidence memories (0.7 or below) stay in auto-memory only.
3. **Not a duplicate of an existing cortex active memory** — agent calls `cortex_search` for the new memory's title; if a high-relevance match exists (score ≥ 0.7), agent updates via `cortex_memory_note` with the new content + the same domains (cortex handles dedup internally) rather than creating a duplicate.
4. **Not a same-session-self-reference** — the agent does NOT recurse on its own session's writes. Memories ABOUT the agent's session work are eligible (e.g., "fired 33 PRs in mass-merge"); memories that USE the agent's session findings as authority are NOT auto-promoted within the same session.

### Confidence calibration

| Confidence | Use for |
|-----------:|---------|
| **0.95** | Operator-explicitly-attested locks ("operator methodology lock", "customers = me"). The operator stated the fact and we're delegating the attestation. |
| **0.9** | Empirical findings with named receipts (Test 5 v2 wave, cellos privileged Docker N=85). The receipt file is the attestation. |
| **0.85** | Patterns + protocols with empirical anchors (runtime-detection pattern, bucket-bridge). |
| **0.8** | Process notes derived from session activity (mass-merge campaign methodology, council pattern). Borderline-promotable. |
| **≤0.7** | Working hypotheses, half-formed thoughts, debug notes. **NOT auto-promoted.** Stays in auto-memory until validated. |

### Same-session self-reinforcement protection

The agent MUST NOT do the following within the same session:

1. **Write a finding to cortex via auto-promote**
2. **Then query cortex_search for that same finding**
3. **Then use the cortex result as ground-truth attestation in a subsequent argument**

This pattern would launder the agent's own hypothesis through cortex into "verified knowledge" — exactly what ADR-0047 prevents on the token-gated path. The agent's discipline is to track which cortex memories are NEW THIS SESSION (the IDs returned by `cortex_memory_note` calls during the session) and treat them as not-yet-cross-validated within the same session.

Cross-session, the protection releases: the operator has had time to read and revoke; absent revocation, the memory is treated as standing.

## Consequences

**Positive:**
- Eliminates operator friction for memory promotion (currently ~5-10 manual "promote X to cortex" requests per session)
- Closes the cross-session knowledge gap: every session's findings become queryable in subsequent sessions
- Preserves operator-control via per-session opt-in (default OFF — operator must affirmatively enable)
- Preserves ADR-0047 spirit via the same-session-self-reinforcement-protection rule
- Operator revoke path exists (`cortex_memory_outcome NotUseful`)

**Negative:**
- One additional operator prompt at cortex MCP startup ("auto-promote? [y/N]")
- Slight increase in cortex active-memory growth rate (mitigated by eligibility filter + dedup)
- Agent must maintain session-scoped state for "memories I wrote this session" (~10-30 entries per session typical)

**Neutral:**
- The mechanism requires a small cortex enhancement: `cortex_session_config()` tool + session-flag storage. This is a non-trivial cortex code change. See §Implementation.

## Implementation (cortex-side enhancement)

For this ADR to ship, cortex needs:

1. **New tool**: `cortex_session_config()` returning `{ auto_promote: bool, session_id: str, started_at: timestamp }`. Read-only; no token required.
2. **Startup flag handling**: cortex serve accepts a CLI flag `--auto-promote` OR prompts via stderr (similar pattern to confirmation token). The chosen path is stored in the session record.
3. **Session-scoped flag storage**: in-memory; resets on restart.

Estimated effort: ~4 hours of cortex engineering. Can land alongside the AXIOM-renaming strategic decision (post-ablation).

## Audit surface

At session end, the agent's final summary lists:

```
Cortex auto-promoted this session:
- mem_01KS3DGKBAJ8QXFP9C9KAJEW1X — Runtime-detection pattern (confidence 0.95)
- mem_01KS3DG2B60YFPJJP61BMX7WGJ — Users always have native+tools (confidence 0.95)
- ...

Operator-revoke surface: `cortex memory outcome <id> --result not-useful`
```

This creates an explicit audit trail per session.

## Council review (4-lens, 4/4 ADVANCE)

**Synthesis:** auto-promote closes the cross-session knowledge gap; per-session opt-in preserves operator agency without requiring per-memory approval.

**Adversarial:** four risks (noise, self-reinforcement, confidentiality, bad-data) — all bounded by (a) eligibility filter, (b) confidence threshold, (c) same-session-protection rule, (d) operator-revoke surface. Net manageable.

**Coldtruth:** the tool description says "operator-attested fact" — per-session opt-in IS the attestation. The operator says "auto-promote on this session" once; that delegates attestation for the eligible memories of that session. Honest.

**Pragmatic:** zero per-memory friction. One per-session touch. ~4 hours of cortex engineering to ship. Net positive on every axis.

**Verdict: 4/4 ADVANCE.**

## References

- ADR-0047 — Cortex memory boundary + token-gated commits (the substrate this ADR builds on)
- CLAUDE.md auto-memory section — the 4-type curation rules this ADR inherits
- `~/.claude/projects/.../memory/MEMORY.md` — the auto-memory index
- cortex_memory_note tool description — the surface this ADR uses

## Versioning

- **v1.0.0** (this ADR) — Initial per-session opt-in design.
- **v1.x.y** — Additive (new confidence calibrations, new domain conventions). No breaking changes to the opt-in mechanism.
- **v2.0.0** — Breaking. Would replace per-session opt-in with a different gate (e.g., per-memory operator confirmation, or always-on). Requires new ADR.
