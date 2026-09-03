# Doctrine Content Lifecycle

This pattern defines how content in this **doctrine library itself** moves through its life: how it is promoted into normative standing, demoted, superseded, retired, and — rarely — rescinded. It closes the gap the corpus has diagnosed about itself twice ([ADR 0029](../../docs/adr/0029-adopt-a-compact-non-duplicative-core-constitution.md) residual risk; the [full-corpus review](../evolution/research-full-corpus-council-review-2026-08.md)'s "house law §6" finding): without a retirement mechanism that someone is assigned to operate, a doctrine corpus only accretes.

**Applicability:** binds changes to this library (maintainers and change automation). Adopters inherit no obligations from this file — the consumer-facing meaning of each state is signalled through [doctrine-versioning-and-consumer-compatibility.md](doctrine-versioning-and-consumer-compatibility.md) §6 — but adopters MAY reuse the pattern for their own doctrine repositories. The change *process* remains [doctrine-library-change-harness.md](doctrine-library-change-harness.md); this file owns the **status vocabulary and lifecycle transitions** both of those files reference. Evidence basis: [research-doctrine-lifecycle-audit-2026-08.md](../evolution/research-doctrine-lifecycle-audit-2026-08.md).

---

## 1. Lifecycle States

Every first-class doctrine file (principles, patterns, checklists, tooling, estates) and every evolution note is in exactly one state below; ADRs use their own status vocabulary (§7: Proposed / Accepted / Rejected / Superseded / Withdrawn). **Active is the default and carries no marker** — only exceptions are stamped, so the corpus's existing files need no retro-edit.

| State | Meaning | Marker |
| --- | --- | --- |
| **Active** | Current guidance at its layer's authority. | None (implicit). |
| **Stub** | Placeholder awaiting content; carries no authority. | `**Status:** **Stub**` line (existing estate convention). |
| **Deprecated** | Still accurate at every tag in which it ships, but scheduled for supersession or retirement; signals that new adoption should not reference it. | Banner per §4. |
| **Superseded** *(exit)* | Replaced by a named successor; points forward. | Tombstone per §5. |
| **Retired** *(exit)* | No successor; the topic no longer earns doctrine. Historical value only. | Tombstone per §5. |
| **Rescinded** *(exit)* | Actively disavowed as wrong or harmful; signals consumers should stop following it even on old pins. Rare and loud. | Tombstone per §5 plus rationale in the register. |
| **Historical** *(evolution notes only)* | A dated snapshot whose currency is superseded by later notes or ADRs; retained as provenance. | One-line banner at the top of the note naming what superseded it. |

The three exit states answer different reader questions — *where did it go* (Superseded), *why is it gone* (Retired), *was it ever right* (Rescinded) — and MUST NOT be collapsed into one label. Evolution notes take only Active or Historical; **marking a note Historical is an editorial change** (notes are non-normative and create no obligations) requiring no ADR, only the banner.

**Why:** A reader landing on any file, at any pin, must learn its standing from the file itself — never by reconstructing it from changelogs.

---

## 2. Promotion

The addition path is the existing harness (research → evolution note → ADR → layered guidance → navigation → verification). This section adds the three gates the harness lacks:

- **New-file test.** A gap earns a **new first-class file** only when (a) the topic is durable and not owned by an existing file's scope, and (b) at least two existing files would cross-link it. Otherwise it lands as a **section in the existing canonical home**. The ADR MUST state which branch was taken and why.
- **Evidence expectation.** Promotion of text into normative standing (typed MUST/SHOULD claims) SHOULD cite applied experience — the change's evolution note records where the practice has been used, or explicitly records that it is **unproven adoption** (a flag the next §8 sweep re-examines). Elegance is not evidence.
- **Source-authority floor.** Promotion into typed standing is **re-admission at the higher floor** of [source-authority-and-evidence-grading.md](source-authority-and-evidence-grading.md) §5: supporting sources MUST be re-fetched and re-verified (content-drift check), re-graded, rolling references converted to pinned, and publisher status checked (superseded ⇒ re-point to the successor or record a deviation); sub-floor evidence is called out in the promotion review and registered in [../EVIDENCE-EXCEPTIONS.md](../EVIDENCE-EXCEPTIONS.md). A vendor blog is not an RFC; the difference is now part of this gate.

Layer placement follows [how-to-read-this-doctrine.md](how-to-read-this-doctrine.md); movement **up** the authority stack (tooling/evolution content becoming pattern or principle text) is a normative change and routes via ADR like any other addition.

**Why:** The corpus's promotion precedent (gap note → ADR → file) is real but uncodified; without these gates, plausible-sounding ideas reach normative standing untested and every gap tends to spawn a file.

---

## 3. Demotion And Relocation

Demotion is a **normal move, not a crisis**, and uses the same ADR mechanism as promotion:

- **Claim demotion** — a MUST softening to SHOULD, or typed text becoming informative — is a **normative loosening**; the ADR records the migration story.
- **Relocation down the stack** — principle text moving to a pattern or tooling file — preserves the vacated section number as a pointer stub where inbound references exist (the observability §6.3 pointer-stub precedent, [ADR 0036](../../docs/adr/0036-land-v050-correction-batch-from-the-corpus-review.md) decision 1), and updates the canonical-home links.
- **File demotion** — an entire file losing standing — is executed as Deprecation (§4) followed by an exit state (§5).

**Why:** The corpus review found relocation being invented ad hoc per case because no procedure existed; ad-hoc moves break anchors and canonical-home discipline.

---

## 4. Deprecation Mechanics

Deprecating any file, section, or rule requires an **ADR** that:

1. Names the target precisely (file, section, or claim).
2. Names the **Active replacement**, which MUST exist in the same release the deprecation ships in — or the ADR MUST state that none is required and why.
3. Declares the intended exit state (Superseded / Retired / Rescinded).
4. Stamps the target with the banner (template; placeholders in angle brackets):

```text
> **Status: Deprecated** (ADR <NNNN>, since v<X.Y.Z>) — superseded by <replacement link>
> (or: retired without replacement). Earliest removal: the first minor release cut at
> least 90 days after v<X.Y.Z>. This text remains accurate at every tag in which it ships.
```

The template states the pre-1.0 window; after `1.0.0` the earliest-removal line instead names the major-release condition (last paragraph of this section). For a **section-level** deprecation, the banner sits directly under the section heading with section-scoped wording ("This section…"), and the register's Target column carries `file §N`.

**Clocks are anchored to release tags, never calendar intent.** The floor composes one way: **the removal release itself satisfies the further-minor condition** — removal MAY ship in the first minor release cut at least 90 days after the deprecating tag, and MUST NOT ship earlier. The floor is a floor, not a trigger: content MAY stay Deprecated longer, but every dying-table entry past its 90-day floor MUST receive a recorded keep-or-execute verdict at each §8 sweep, so deprecations cannot become a second corpus. **Expedited path:** text that is actively harmful or insecure is rescinded immediately by ADR, with the rescission reason in the register; the floor does not apply. (This is stricter than the external precedent's shortened-window path — a doctrine sentence has no deployed-implementation base to protect.)

After `1.0.0`, removal of a normative surface additionally rides a **major** release per [doctrine-versioning-and-consumer-compatibility.md](doctrine-versioning-and-consumer-compatibility.md) §2; before `1.0.0`, the floor above is the whole gate.

**Why:** The prior removal rule (versioning §6's major-only gate, with an actively-harmful escape) was never exercised in five releases and composes unclearly with §2's 0.y.z sentence; MCP's SEP-2596 supplies the tested shape — replacement-before-deprecation, tag-anchored floors, an expedited security path.

---

## 5. Removal, Stamping, And Restoration

**Files MUST NOT be hard-deleted.** Executing an exit turns the file into a **tombstone stub**: the original path keeps resolving, containing only the exit banner (state, ADR link, successor link where one exists, and the last tag at which the full text shipped — closing the accuracy interval the deprecation banner opens). The full text remains reachable at any pinned tag. Inbound links inside the corpus MUST be repointed in the same change; external consumers' links keep working and land on the forward pointer.

Section-level removals inside a living file leave the section number as a pointer stub when any inbound reference exists (§3).

**Restoration is a normal ADR-routed move**, not a crisis: a new ADR names the tombstoned target and the reason the exit rationale no longer holds; the file is restored (revised as needed) and the tombstone row remains permanent, gaining a "restored by ADR NNNN in vX.Y.Z" annotation. Never-delete tombstoning is what makes this cheap — the full text is one pinned tag away.

**Why:** IETF and NIST retirements work because the artifact carries its own tombstone and the reader is always pointed forward; silent deletion breaks embedded links in consumers' READMEs, audit packs, and onboarding docs. W3C and MCP both make restoration first-class; a register that only buries would quietly become a presumption against ever being wrong about retiring.

---

## 6. The Register

[`doctrine/DEPRECATED.md`](../DEPRECATED.md) is the single **index** of lifecycle state — the one place to look for *what is scheduled for removal, what has exited, and what the sweeps decided*. **The file's own banner is canonical for its state; the register is a derived index** — a divergence between them is a defect, resolved by reconciling to the ADR that authorized the transition. It holds three tables:

- **Dying table** — every currently-Deprecated item: target, ADR, deprecating release, replacement (or "none required"), earliest-removal condition.
- **Tombstone table** — every executed exit: target, exit state, deprecated-since release (migrated from the dying row, which moves rather than disappears), one-line rationale ("subsumed by X", "topic no longer earns doctrine", "disavowed: reason"), ADR, exit release, and any restoration annotation. Tombstone rows are **append-and-annotate only**; any other edit to an existing row is a lifecycle defect requiring an ADR. The table is the corpus's memory against re-proposing dead ideas from amnesia.
- **Sweep ledger** — per §8: each sweep's date, record link, and per-item verdicts, so re-armed clocks and fade reconfirmations have a stored surface instead of living in git archaeology.

Every deprecation ADR and every executed exit MUST update the register in the same change. An empty register is a meaningful statement, not a missing file.

---

## 7. ADR Lifecycle

- The ADR status vocabulary gains **Superseded**: when a new ADR replaces an old decision, the old ADR's status line becomes `Superseded by [ADR NNNN](path)` and the new ADR names what it supersedes; both directions MUST be present. A decision disavowed **without** a successor is reversed the same way — the reversing ADR supersedes it and records the disavowal. Amendment-in-place (the ADR 0024/0030 precedent) remains correct for refinements that do not reverse the decision.
- The vocabulary also gains **Withdrawn**: a terminal, proposer-initiated exit for a Proposed ADR that will not proceed — distinct from Rejected (a considered refusal).
- ADRs do not get tombstone files — the status line and the index row are their lifecycle surface.
- A **Proposed ADR older than 90 days** MUST receive a recorded decision at the next §8 sweep: accept, reject, or withdraw. Proposals do not idle indefinitely.

**Why:** [documentation-knowledge.md](../principles/documentation-knowledge.md) requires of adopters that "superseded decisions are linked, not erased"; the library's own ADR index could not previously express that state.

---

## 8. Review Cadence — The Anti-Accretion Engines

Retirement fails everywhere it depends on an affirmative act nobody is assigned. Two engines make the question un-skippable, both **wired into the release checklist** (versioning §8) so skipping them is visible in release evidence:

- **Release-coupled staleness sweep.** At every minor release, files untouched for **12 months or more** each MUST receive a recorded verdict — **retain / revise / demote / deprecate** — in the sweep record. A retain verdict re-arms that file's clock via its sweep-ledger row; silence is not a verdict. A sweep MAY bound its cohort (oldest-first, at least ten files per sweep) provided every file receives a verdict within two sweeps of crossing the threshold — the corpus was created in a burst, and the first qualifying cohort (April 2027) would otherwise arrive as an unswallowable cliff that invites rubber-stamping.
- **Six-month backstop.** If no minor release occurs within six months of the last sweep, a **standalone sweep** runs anyway. This is a **maintenance obligation, not a release promise** — it neither creates nor implies a release calendar ([GOVERNANCE.md](../../GOVERNANCE.md) promises none before 1.0.0). A standalone sweep records its verdicts in the sweep record but cannot execute any verdict that requires a tag: deprecation banners take effect ("since") at the next tagged release, and removals always ship in a release.
- **The sweep record** is a dated evolution note (`evolution/sweep-YYYY-MM.md` or a section of the release's review note) holding the cohort, the verdicts with one-line reasons, fade-flag dispositions, dying-table keep-or-execute verdicts, a check that every dying-table replacement is still Active (re-targeting or reopening the ADR where one has itself been deprecated), and decisions on Proposed ADRs older than 90 days. The register's sweep ledger links every record.
- **Default-fade for informative layers.** Entries whose value is currency rather than principle — tooling illustrations, standards-watch blocks, live product-status claims, evolution-note registers — are **presumed fading**: any such entry not reconfirmed within 12 months (epoch: the entry's last edit, or the `v0.5.0` tag for pre-existing entries) is auto-flagged into the next sweep with a default verdict of demote-or-date-stamp, which the sweep MUST either execute or overturn with a recorded reason. Reconfirmation is a sweep-ledger row, not an in-file edit.
- **Reference-status leg.** Each sweep MUST re-check publisher status and link health for its cohort's citations — exhaustively for citations supporting MUST-level claims, sampled for the remainder with the sample recorded in the sweep record — run the [source-authority-and-evidence-grading.md](source-authority-and-evidence-grading.md) §8 diagonal-collapse audit, and process source events (profile-carried sources route per that pattern's §7 ADR-0026 precedence, not this table): **rescinded or disavowed sources act immediately on discovery** — supported normative claims are treated as unsupported at once; withdrawal, supersession, amendment of a pinned source, link death, content drift, vendor product sunset, and access changes are handled at the next sweep with **MUST-supporting sources prioritised ahead of cohort work**. Verdicts land in the sweep record; [../EVIDENCE-EXCEPTIONS.md](../EVIDENCE-EXCEPTIONS.md) entries are re-examined in the same pass. Calendar latency tighter than the sweep cadence exists only where the estate names monitoring tooling and an owner. A **Superseded file keeps its pinned citations untouched** — supersession points forward via the tombstone; it never rewrites the historical record.
- **The library obeys its own rules.** Deferred normative debt in this library (typing retrofits, deferred consolidations, transitional stubs) MUST carry what [normative-language-applicability-and-exceptions.md](normative-language-applicability-and-exceptions.md) §6 requires of any control: a named owner, a review trigger, and a retirement condition. An ownerless deferral is a defect, not a plan.

**Why:** IETF's mandated annual reviews died of neglect and were deleted (RFC 6410); NIST's staffed review board and the Radar's default-fade are the two designs observed to actually empty a graveyard. This section runs both, sized to a single-operator cadence, with the trigger in the release checklist and the state in the register — the two places a skipped engine becomes visible.

---

## 9. Anti-Patterns

- **Zombie deprecation** — Deprecated for releases on end with no sweep verdict; the register decays into a second corpus.
- **Deprecating onto vaporware** — killing guidance whose replacement hasn't landed; leaves a normative hole.
- **Silent removal** — deleting without tombstone or register row; breaks every embedded consumer link and erases the corpus's memory.
- **Promotion by elegance** — normative standing granted to untested prose; the §2 evidence expectation exists precisely for this.
- **Ownerless deferral** — "we'll retrofit later" with no owner or trigger; the §8 reflexive rule makes this a recorded defect.
- **Collapse of the exit states** — labelling everything "deprecated" hides whether old guidance is still safe on old pins (Superseded/Retired) or was never right (Rescinded).

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Active-by-default, stamp exceptions only | Existing files need no retro-edit; markers stay meaningful because they are rare. |
| Three exit states, not one | Different reader messages: where did it go / why is it gone / was it ever right. |
| Never hard-delete; restoration first-class | Tombstones preserve consumer links and provenance; pinned tags keep the full text, making un-retirement cheap. |
| Tag-anchored clocks with floor-not-trigger windows | Calendar intent stalls; release anchors are checkable. Floors respect pinned consumers. |
| Two anti-accretion engines, checklist-wired, register-stored | A sweep alone rots (IETF precedent); fade alone lacks judgment. The trigger lives in the release checklist and the state in the sweep ledger so neither depends on memory. |
| Same ADR rail for promotion, demotion, and restoration | Demotion must be a normal move; a separate heavier process would guarantee it never runs. |

---

## References

- IETF: [RFC 2026](https://www.rfc-editor.org/rfc/rfc2026.html) (§6.2 periodic review) and [RFC 6410](https://www.rfc-editor.org/rfc/rfc6410.html) (two-tier ladder; annual-review requirement dropped).
- MCP feature lifecycle, SEP-2596: https://modelcontextprotocol.io/community/feature-lifecycle
- W3C Process (Rescinded / Obsolete / Superseded / Restoring): https://www.w3.org/policies/process/
- NIST crypto-publication review project (periodic retain/revise/withdraw): https://csrc.nist.gov/projects/crypto-publication-review-project
- Thoughtworks Technology Radar FAQ (default-fade, production-experience gate): https://www.thoughtworks.com/radar/faq
- Full source ledger and audit evidence: [research-doctrine-lifecycle-audit-2026-08.md](../evolution/research-doctrine-lifecycle-audit-2026-08.md)

---

## Related

- [doctrine-library-change-harness.md](doctrine-library-change-harness.md) — the change process this lifecycle plugs into.
- [doctrine-versioning-and-consumer-compatibility.md](doctrine-versioning-and-consumer-compatibility.md) — change classes and the consumer-facing meaning of lifecycle states; its §6 routes here.
- [normative-language-applicability-and-exceptions.md](normative-language-applicability-and-exceptions.md) — §6 control lifecycle, applied reflexively by §8.
- [how-to-read-this-doctrine.md](how-to-read-this-doctrine.md) — the authority stack that promotion and demotion move content across.
- [../DEPRECATED.md](../DEPRECATED.md) — the register.
- [../../docs/adr/0038-adopt-a-doctrine-content-lifecycle.md](../../docs/adr/0038-adopt-a-doctrine-content-lifecycle.md) — adopting decision, with the audit evidence.
