# ADR 0037: Land MCP Cross-Check Correction Batch

- **Status:** Accepted
- **Decision date:** 2026-08-06
- **Recorded date:** 2026-08-06
- **Retrospective:** No

## Context

A four-agent deep-research cross-check ([research-mcp-spec-cross-check-2026-08.md](../../doctrine/evolution/research-mcp-spec-cross-check-2026-08.md)) re-verified every MCP claim in the corpus against primary sources three days after ADR 0031 landed the revision-pinned baseline. **All five §7 bullets and the companion edits held.** The cross-check surfaced no invalidated rules — only a small set of factual and editorial defects, all in reference rows, research-note digests, and one script fixture. This ADR lands that **correction batch**; the cross-check's gap findings stay open in the note's §4 action list — post-session state security and extensions posture (rows 1–2) for a future ADR, the remaining rows as non-ADR additions.

Precedent for the batch shape: [ADR 0036](0036-land-v050-correction-batch-from-the-corpus-review.md). On correction style: the repo's existing precedent is **annotation with provenance** (the gap-audit's ~81% attribution correction is recorded in its §7 prose while the original §2.1 digest row stands). C4 follows that style. C1–C3 instead correct digest rows **in place** with the correction carried inline and this ADR as the provenance record — a convention this ADR explicitly establishes for verified factual defects in digest rows (a wrong date is a defect, not history). The gap-audit's ~81% row deliberately stays annotation-only: its correction is already recorded in §7 prose per ADR 0033, and re-styling it is out of this batch's scope.

Council provenance: three-critic council (doctrine fidelity / correction-class discipline; independent fact re-verification against primary sources; coherence and reader impact). The factual substance of all six corrections survived critique; 7 blockers and 13 majors against the surrounding drafts were resolved before presentation — notably the cross-check note's AgentSeal claims rewritten against their actual primary sources, a third-party quote stripped of "official position" attribution, two RFC-2119 levels corrected, the in-place-correction precedent restated honestly (above), and the companion navigation obligations enumerated (Decision 7). Council findings and resolutions are recorded in the session record; the resolved text is this ADR and the cross-check note as landed.

## Decision

1. **C1 — NSA CSI date.** The gap-audit §2.9 row asserting the NSA AISC MCP CSI at **2026-06-02** is corrected to the verified release date **2026-05-20** (NSA press release Article 4496698; doc U/OO/6030316-26), matching the date already used by the normative body and REFERENCES.md. The row keeps the media.defense.gov URL with a note that its `/2026/Jun/02/` segment is an upload path, not the release date. The **(unverified)** flag narrows: existence, date, and identity are now verified via the press release; the row's content characterization remains triangulated (the PDF bot-blocks fetchers) and keeps a content-level caveat.
2. **C2 — RC-vs-final URLs and IdP attribution.** The two gap-audit §2.9 rows citing the release-candidate blog URL — the spec row labelled "(final)" and the authorization-model row — are repointed to the final announcement (`blog.modelcontextprotocol.io/posts/2026-07-28/`). The authorization-model row's "External IdP" descriptor is removed from the spec description: the spec permits a co-hosted authorization server; external-IdP is this doctrine's own tightening ([ai-ml-systems.md](../../doctrine/principles/ai-ml-systems.md) §7 retains it on doctrine authority, unchanged).
3. **C3 — auth-change enumeration.** The unenumerated "six auth hardening changes" in the gap-audit spec row is replaced with the verifiable enumeration: RFC 9207 issuer validation (SEP-2468), DCR deprecated in favour of CIMD (PR #2858), issuer-keyed client credentials (SEP-2352), and the `application_type` registration constraint (SEP-837) — count-free phrasing, consistent with the ADR 0036 schema-fact discipline. Sources indexed in the cross-check note §5.
4. **C4 — AAIF hedge resolved.** The April note's self-flagged hedge ("verify current charter") gains a dated update: Anthropic donated MCP to the **Agentic AI Foundation** (a Linux Foundation directed fund co-founded by Anthropic, OpenAI, and Block) on **2025-12-09**, with the official announcement URL. The original hedged sentence is preserved; the update is appended, matching the annotation precedent.
5. **C5 — CIMD precision.** [ai-ml-systems.md](../../doctrine/principles/ai-ml-systems.md) §7's pin-bullet parenthetical expands the acronym on first use — **Client ID Metadata Documents (CIMD)** — and splits the citation: CIMD introduced as a recommended registration mechanism in the **2025-11-25** revision (SEP-991); DCR deprecated in its favour in **2026-07-28**. No normative change; the pin rule is untouched.
6. **C6 — fixture grammar.** `scripts/validate-contracts-v1.py` line 276: "produces an tool-contract.lock" becomes "produces a tool-contract.lock". The `tool-contract.lock` concept is recorded in the cross-check note (§4 preamble) as fixture-only with no doctrine home — a naming-only artefact, not a latent obligation; no doctrine text is added.
7. **C7 — companion navigation edits (landing checklist).** The batch lands with: a [docs/adr/README.md](README.md) index row for this ADR; CHANGELOG `[Unreleased]` entries (**Fixed** for the correction batch, **Added** for the cross-check note); a doctrine/README.md evolution-list row; SITEMAP regeneration via `./scripts/generate-doctrine-sitemap.sh`; a SEMANTIC_INDEX see-also entry beside the gap-audit's; and a REFERENCES.md internal-map row for the note. The batch does not land without them.

Scope note: the gap-audit's §8 reference block deliberately keeps the RC blog URL and the media.defense.gov PDF URL — it is a historical consulted-sources inventory, not a claims surface; only the §2.9 digest rows carry corrections.

## Consequences

**Positive:** the corpus's two conflicting NSA CSI dates converge on the verified one; the spec digest cites the final announcement rather than the RC; an unenumerable count is replaced by checkable facts; a self-flagged verification hedge is closed with a primary source; the corpus's only active-doctrine CIMD mention (ai-ml-systems.md §7) now expands its acronym.

**Costs and risks:** editing dated research notes risks obscuring the historical record; mitigated by the split convention above (in-place only for verified factual defects, with inline correction notes and this ADR as provenance; annotation style preserved where the original text was advice), and by C7's navigation record.

## Consumer Impact

**Change class:** corrective/editorial throughout. No normative claim is added, removed, retyped, or rescoped; no consumer's compliance position changes.

**Compatibility proposal:** pre-1.0 patch content; ships with `v0.5.0`.

## Acceptance Evidence

- Cross-check provenance: 4-agent deep-research verification against primary sources, recorded in [research-mcp-spec-cross-check-2026-08.md](../../doctrine/evolution/research-mcp-spec-cross-check-2026-08.md).
- Council provenance: three-critic critique with all blockers and majors resolved in the landed text (Context, ¶3).
- C1–C6 edits applied with per-edit anchor verification; C7 companion edits applied; SITEMAP regenerated.
- Contracts validation gate green after the C6 script edit.
- Operator approval of the batch recorded 2026-08-06 before landing.
