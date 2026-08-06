# Research: Doctrine Content Lifecycle Audit And External Models (August 2026)

**Status:** research note (non-normative). **Date:** 2026-08-06. **Method:** 3-agent audit — (1) internal lifecycle-machinery extraction over the full corpus and git history, (2) consolidated open-backlog and drop-candidate sweep, (3) external standards-lifecycle research across eight models with primary sources — followed by a three-critic council over the resulting drafts. Proposals route via ADR per repo convention; the adopting decision is [ADR 0038](../../docs/adr/0038-adopt-a-doctrine-content-lifecycle.md).

---

## 1. Purpose

The operator's question: *does the library have a solid promotion harness — a defined path to a new principle — and a demotion process; how do we supersede and retire out-of-fashion or obsolete content?* This note records the evidence: what lifecycle machinery exists, what is absent, what mature standards ecosystems do about the same problem, and which mechanics transfer to a single-operator, pre-1.0 doctrine repo.

---

## 2. Internal audit — what exists, what is absent

### 2.1 Exists and works: the addition path

Research → evolution note → ADR → layered guidance → navigation → verification, codified in [doctrine-library-change-harness.md](../patterns/doctrine-library-change-harness.md) (§§1–5) and mirrored in CONTRIBUTING.md, the change checklist, and the preflight script. Worked precedents: ADR 0007 (developer-experience principle from a named gap-note finding plus external sources), ADRs 0008, 0009, 0023, 0024/0030, 0026, 0028. The de-facto promotion criterion — "a gap note named it, an ADR created it" — is real but written nowhere, and no text states when a gap earns a **new file** versus a **section**, nor any evidence expectation beyond "researched basis".

### 2.2 Absent in practice: the retirement half

Verified at HEAD (2026-08-06):

- **Strictly monotonic corpus.** `git log --diff-filter=D` and `--diff-filter=R` over `doctrine/` and `docs/`: zero deletions, zero renames in all reachable history, across five releases (v0.1.0 … v0.4.0). Every doctrine file ever created still exists at its original path. (Caveat: history was rewritten under ADR 0027; pre-repair deletions would not appear.)
- **The Deprecation change class has never been used.** Defined in [doctrine-versioning-and-consumer-compatibility.md](../patterns/doctrine-versioning-and-consumer-compatibility.md) §3 since v0.1.0; no release in CHANGELOG.md has ever declared it.
- **No ADR has ever been superseded**, and no `Superseded` status exists in the index vocabulary — while [documentation-knowledge.md](../principles/documentation-knowledge.md) requires of adopters that "superseded decisions are **linked**, not erased". ADR 0021 has sat at Proposed since 2026-05-20 with no staleness trigger.
- **The ordinary removal gate composes unclearly pre-1.0.** Versioning §6 permits removal only in a major release (with an actively-harmful escape), while §2's 0.y.z sentence allows intentional normative movement in minors; the composition was never exercised or clarified.
- **No file-level status vocabulary** (only the two estate stubs carry `**Status:** **Stub**`), no review cadence, no deprecation register, no tombstone convention.
- **Self-diagnosed, twice, unclosed.** ADR 0029 residual risk: "The reference corpus can continue to grow unless the change harness enforces singular ownership and control-retirement criteria." The [full-corpus review](research-full-corpus-council-review-2026-08.md)'s "house law §6" finding: the control-lifecycle rule (owner, review trigger, retirement condition — [normative-language-applicability-and-exceptions.md](../patterns/normative-language-applicability-and-exceptions.md) §6) is demanded of adopters' controls and not applied to the library's own normative debt (the ADR 0032 typing-retrofit deferral being the cited instance).
- **Stuck test case.** [feature-flag-lifecycle.md](../patterns/feature-flag-lifecycle.md): orphaned from the normative link graph, untyped, previously self-contradictory (B1, interim-repaired by ADR 0036) — with no mechanism able to mark, demote, or retire it.
- **The lifecycle-vocabulary owner is itself stale.** The versioning pattern is a single-commit file, unrevised since v0.1.0 (2026-04-27) through four subsequent tags — one of six patterns never revised since first landing (three date to 2026-04-10).
- **ADR numbers 0013–0020 were never assigned** in any reachable history; no record explains the gap.

### 2.3 Staleness tail and disposition candidates (input to ADR 0038 decision 7)

The April 2026 cohort dominates the untouched tail: most of `doctrine/tooling/` (including both estate stubs, single-commit since 2026-04-07), several single-commit patterns (webhook-ingress-security, the two example workflows, 2026-04-10), and [platform-engineering.md](../principles/platform-engineering.md) (single-commit principle, untyped, Gartner-2023-cited, overlapping the newer platform-as-product pattern — the review names it the area's structural risk). Candidate Historical set among evolution notes: the mythos-era note (its ADR 0010 gaps closed), the two 2026-04 landscape/RAG notes (currency superseded by the 2026-08 audit and ADRs 0031/0037; two still live-cited from tooling files — repoint at execution), the knowledge-factory note, deep-research-section-gaps (line-count table wildly stale), the benchmark/taxonomy pair, scorecard-vs-mainstream, and moscow-review. The consolidated open backlog is otherwise almost fully routed to the forward plan's v0.5.0 lanes; the unowned items are the V41 owner assignment, the platform-engineering disposition, and the dormant 2026-04 gap registers.

---

## 3. External models — source ledger

| Model | Mechanics relevant here | What it does / does not establish | Source |
|---|---|---|---|
| IETF (RFC 2026 / RFC 6410) | Immutable RFCs + metadata overlay; bidirectional Obsoletes/Updates graph; Historic status; RFC 6410 cut three standards tiers to two and **deleted the mandated annual review** ("the annual review … has not taken place … the requirement for this review is dropped") | Establishes: never-edit-always-stamp works at scale; unstaffed periodic review dies of neglect. Does not establish: a promotion evidence bar transferable below "two independent interoperating implementations" | https://www.rfc-editor.org/rfc/rfc2026.html · https://www.rfc-editor.org/rfc/rfc6410.html |
| NIST (CSRC / SP series) | Withdrawn status with superseded-by pointers and tombstone cover sheets on the archived PDF; ~1-year supersession sunset (SP 800-53 r4 withdrawn one year after r5); crypto-publication review board on a ~5-year cycle with forced retain/revise/withdraw decisions | Establishes: retirement ≠ deletion; a clock that forces the question plus evidence that answers it | https://csrc.nist.gov/pubs/sp/800/53/r4/upd3/final · https://csrc.nist.gov/projects/crypto-publication-review-project |
| W3C Process | Three-way exit vocabulary — Rescinded (defective) / Obsolete (stale, restorable) / Superseded (replaced); restoration is first-class via the same review weight as demotion | Establishes: the exits answer different reader questions and restoration must be a normal move | https://www.w3.org/policies/process/ |
| CNCF | Sandbox→Incubating→Graduated→Archived; adopter-interview evidence; archival via health review + supermajority; reactivation path | Establishes: evidence-typed promotion; committee-shaped — the ladder itself does not transfer to n=1 | https://github.com/cncf/toc/blob/main/process/README.md · …/process/archiving.md |
| TC39 | Stage 0–4 consensus gating; regression to an earlier stage is first-class; `inactive-proposals.md` tombstone table with per-item rationale ("no interested champions" is a recorded death cause) | Establishes: the tombstone-with-rationale table; champion loss as retirement trigger | https://tc39.es/process-document/ · https://github.com/tc39/proposals/blob/main/inactive-proposals.md |
| MCP (SEP-2596) | Active/Deprecated/Removed; replacement MUST be Active in the deprecating revision (or none-required stated); ≥12-month floor **anchored to revision release, not decision date**; floor-not-trigger; expedited path (≥90 days) only for active security risk; single deprecated-features registry page | Establishes: the tested modern shape for replacement-gated, tag-anchored deprecation and the one-registry reader experience | https://modelcontextprotocol.io/community/feature-lifecycle |
| OWASP projects | Incubator/Lab/Production + Flagship; 1-release/year activity floor; Inactive → reactivate-or-dissolve | Establishes: an activity floor needs an enforcement clock (OWASP lacks one — its graveyard mechanics are the weakest of the eight) | https://owasp.org/www-committee-project/ · https://policy.owasp.org/operational/projects |
| Thoughtworks Radar | Adopt/Trial/Assess/Hold-now-Caution; Trial requires production experience; **default-fade** — blips drop off after one edition unless they move or are re-affirmed; archived blips frozen with an outdated-advice flag | Establishes: retention-requires-signal is the only observed self-filling graveyard; production-experience gate against promotion-by-elegance | https://www.thoughtworks.com/radar/faq |

Synthesis carried into the pattern: minimal status set (Active default / Stub / Deprecated flag; exits Superseded / Retired / Rescinded; Historical for notes), never-delete-always-stamp, one register, replacement-before-deprecation, tag-anchored floor-not-trigger windows, restoration as a normal move, and **two** anti-accretion engines (a staffed sweep and default-fade) because each alone has an observed failure mode. Known failure modes designed against: retirement-as-unassigned-act (IETF), zombie deprecation (floor with no eviction verdict), deprecating onto vaporware, silent removal, promotion by elegance, clock ambiguity (window anchored to decision dates rather than releases).

---

## 4. Disposition

[ADR 0038](../../docs/adr/0038-adopt-a-doctrine-content-lifecycle.md) adopts the pattern ([doctrine-content-lifecycle.md](../patterns/doctrine-content-lifecycle.md)), creates the register ([DEPRECATED.md](../DEPRECATED.md)), revises the versioning pattern's §6, extends the ADR status vocabulary, and routes the inaugural applications (V45/D12 supersession, Historical banners, estate-stub and platform-engineering dispositions, first sweeps). Council record: three critics (fidelity, consistency/source verification, design); 5 blockers and 15 majors resolved in the landed drafts, including this note's own existence (the drafts initially shipped without their harness-required research note — an irony the council did not let stand).
