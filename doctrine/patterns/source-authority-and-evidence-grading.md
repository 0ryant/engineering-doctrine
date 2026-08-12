# Source Authority And Evidence Grading

How a citation-bearing doctrine corpus grades **what it cites** and **how strongly the citations support each claim** — two separate axes, coupled to BCP-14 claim strength by admission floors. This is the canonical owner of the source-class ladder, the claim-support grades, the independence test, and the admission gate; lifecycle wiring (sweeps, source events, promotion) lives in [doctrine-content-lifecycle.md](doctrine-content-lifecycle.md), and evidence-floor exceptions live in [../EVIDENCE-EXCEPTIONS.md](../EVIDENCE-EXCEPTIONS.md).

**Activation:** estates maintaining citation-bearing normative doctrine (a corpus whose typed claims cite external sources). Estates that do not maintain such a corpus inherit nothing from this pattern. **This library is its first adopter and binds itself reflexively**, forward-only per [ADR 0040](../../docs/adr/0040-adopt-source-authority-classes-and-evidence-weighted-citations.md): the rules bind new and promoted claims; the back-catalogue routes through the lifecycle sweeps.

**Decision record:** [ADR 0040](../../docs/adr/0040-adopt-source-authority-classes-and-evidence-weighted-citations.md); **research basis:** [../evolution/research-source-authority-and-evidence-weighting-2026-08.md](../evolution/research-source-authority-and-evidence-weighting-2026-08.md) (census, cross-discipline frameworks, standards-body mechanics; council-ratified, census independently reproduced).

**Related:** [normative-language-applicability-and-exceptions.md](normative-language-applicability-and-exceptions.md) (claim strength and the exception contract this pattern's exceptions instantiate), [revision-pinned-control-profiles.md](revision-pinned-control-profiles.md) (which **takes precedence** for profile-carried sources — §7), [doctrine-library-change-harness.md](doctrine-library-change-harness.md) (authoring workflow), [../REFERENCES.md](../REFERENCES.md) (the index this pattern's metadata shape governs for new entries).

---

## 1. Two Axes, Not One

The disciplines that grade evidence at scale — intelligence (Admiralty two-axis source-reliability × information-credibility; ICD 203's likelihood/confidence separation) and medicine (GRADE's per-claim certainty, decoupled from recommendation strength) — independently landed on the same design: **what kind of source it is** and **how strongly the evidence supports this claim** are different questions, graded separately. Collapsing them is the documented failure mode: in field use, 87% of Admiralty ratings fell on the A1/B2/C3 diagonal — source prestige quietly substituted for item credibility. A doctrine corpus that grades only source prestige rebuilds that failure: a corroborated practitioner claim can never outrank an uncorroborated paper, and MUST-vs-MAY floors have nowhere to live.

So: **source class attaches to the citation** (§2); **claim support attaches to the doctrine claim** (§3); the coupling to BCP-14 strength is the admission gate (§5). The other graded literatures contribute fields, not a third instance of the core: law's scoped bindingness (a source is "mandatory" only inside its scope), software engineering's appraisal checklists with vested-interest tests, historiography's role-relativity (the same source is primary for one claim and secondary for another).

## 2. Source Classes

Each citation carries a **class**, a **scope** (what the source is authoritative *for*), and a **role** (primary/secondary *for the claim it supports*).

| Class | Definition | Hard-case rules |
| --- | --- | --- |
| **S1** | The norm itself, from its owner, in ratified form — standard, specification, statute, regulation | Release candidates and drafts are S3, flagged provisional; a grading instrument from its owning body is S1 for claims about that instrument; mirror URLs are convenience legs only — the canonical identifier (CELEX/ELI, RFC number, dated TR URI) is the citation |
| **S2** | Statutory-body or institutional guidance issued under a mandate over the domain | Interpretive, not the norm: EDPB guidelines are S2 beside GDPR's S1; NIST SPs, CISA/NCSC advisories. A body's *mandate* is the test — an edited university reference guide has none (S4) |
| **S3** | Peer-reviewed research; standards-in-progress | Preprints carry a `preprint` flag and do not inherit peer-review weight; conference/journal venue recorded |
| **S4** | Edited or reviewed artifacts: books, editor-reviewed professional magazines, foundation specifications **graded by the artifact's own review process**, disclosed-methodology research programs, edited institutional references | An editor-reviewed magazine column (IEEE Software, HBR) is S4, not peer-reviewed S3 and not bare commentary; a foundation's versioned, reviewed spec (SLSA, ASVS) is S4 while its wiki-style pages are S6; an *awareness* document supports risk-salience claims only; undisclosed-methodology consultancy content is S6/S7 |
| **S5** | Product-scoped primary documentation — the vendor's authoritative docs for its own product or protocol | **Mandatory within product scope, persuasive outside it**: for claims about the product's own behaviour, in-scope S5 is S1-equivalent (§4); cited out of scope it silently demotes |
| **S6** | Named-expert practitioner writing; vendor engineering content; first-party observations | `role=primary` for the author's own incidents, experience, and measurements; `role=secondary` for generalised advice; canonical essays remain S6 — corroboration can raise a claim's C-grade, never a source's class |
| **S7** | Community/UGC, marketing, press | Marketing is citable only as evidence *of the vendor's claim*, never of its truth; social-media posts sit here regardless of author fame |
| **X** | Cannot judge — anonymous or unattributable | A distinct state from "low", never conflated with it; X never supports normative claims. A dated, attributed first-party observation is **not** X — it is S6 with `role=primary` |

**Transcription/intermediary rule:** retrieval of the **verbatim artifact** from any host keeps the underlying class with the access path annotated; **re-keyed or transcribed content** keeps the underlying class only when corroborated across ≥2 independent transcriptions; a single uncorroborated transcription takes the **intermediary's** class.

## 3. Claim-Support Grades

Computed per material doctrine claim from its citation set — a property of the body of evidence, not of any one citation:

- **C1 — corroborated.** ≥2 **independent** in-scope sources of class S1–S4 (or S1-equivalents per §4), no credible contrary source.
- **C2 — probable.** One in-scope S1–S4 / S1-equivalent source, or ≥2 independent S5–S6 sources; no contrary evidence found after looking.
- **C3 — plausible.** A single S5–S6 source, or consistent practitioner consensus without formal backing.
- **C4 — contested/uncertain.** Credible sources conflict, or only S7/X support exists.

**The independence test** (written, because axis collapse begins here): independent means **different organisations with different incentive structures**. Two posts by one vendor are one source; a foundation spec and its own cheat-sheet are one source; a paper and its authors' blog post are one source.

**Modifiers, recorded per claim (GRADE-style):** downgrade one level for vested interest, staleness beyond the domain's clock, indirectness (evidence about a materially different context), or out-of-scope citation; upgrade one level for an unambiguous mechanism (a CVE, a mathematical argument, a reproducible benchmark) or survival across independent ecosystems.

## 4. Conformance Versus Empirical Claims

A split the gate's arithmetic needs. **Conformance claims** cite a norm *as* the norm — "conform to RFC 9110", "meet SLSA L3", "behaves as the vendor documents" — and are satisfied by **the norm itself, pinned, at the norm's own class**: S1 for de jure standards and law; **≥S4 for foundation-owned versioned specifications** (a pinned ASVS section or SLSA level — the corpus's largest bucket); for claims about a product's own behaviour, the product's authoritative documentation is **S1-equivalent within that scope**. The class is still recorded; demanding a second copy of the norm is the §8 anti-pattern. Corroboration is a test for **empirical claims**, where the source could simply be wrong; it is not a demand for two copies of a standard. Empirical claims about humans and organisations ("this practice improves that outcome") are capped at C2 on practitioner sources alone — they need S3-class evidence to reach C1.

## 5. The Admission Gate

Where this pattern is activated, admission floors couple claim strength to claim support:

- A new or promoted **MUST/MUST NOT** MUST be admitted only at **C1**, or at **C2 with an explicitly recorded risk asymmetry** (the strong-recommendation-on-moderate-evidence move — stated in the claim's section, not implied), or with a **registered evidence exception**. Conformance MUSTs are satisfied by their pinned norm (§4).
- A new or promoted **SHOULD/SHOULD NOT** SHOULD be admitted at **≥C2**; single-source support MUST be visibly flagged at the claim.
- **MAY and illustrative content** SHOULD cite ≥S6, pinned and dated. **X MUST NOT support a normative claim, and X is exception-proof**: attribution is the minimum admission ticket to the register below — if the only evidence is unattributable, the claim cannot hold a typed strength.
- Where a normative claim genuinely needs sub-floor evidence (the only description of a proprietary mechanism), it enters via [../EVIDENCE-EXCEPTIONS.md](../EVIDENCE-EXCEPTIONS.md): each entry is a [normative-language-applicability-and-exceptions.md](normative-language-applicability-and-exceptions.md) §5 exception in record shape — claim, source, justification, approver, date, **expiry** — adjudicated once and **reusable while in force** by later claims citing the same source at the same level; permanence is a change to policy or profile, never an endlessly renewed exception. The register doubles as the evidence-upgrade worklist.

**Why:** the corpus already holds "elegance is not evidence" ([doctrine-content-lifecycle.md](doctrine-content-lifecycle.md) §2); this gate is its missing companion — a vendor blog is not an RFC, and the difference is now mechanical rather than felt.

## 6. Citation Metadata And Temporal Discipline

A newly admitted citation supporting a typed claim MUST record its **class**, its **pin-or-rolling choice**, and its **accessed date**; it SHOULD capture an **archived copy** at admission — durability is created at citation time, never later (half to two-thirds of aged web citations in the legal and grey-literature studies no longer reach their cited content, one in five in the STM literature, and only ~27% had a near-publication snapshot). The archival SHOULD becomes MUST where the estate operates archival tooling; the tooling gap is a recorded watch, not a waiver of the principle. Prefer a **durable identifier** (DOI, RFC number, dated TR URI, CELEX/ELI) as the canonical leg wherever one exists.

- **Pinned (dated) is the default** — normative-claim support and any citation of a numbered sub-element (control ID, section, table) MUST be pinned, because renumbering across revisions silently retargets unpinned references. A pin creates the reciprocal duty: on amendment or revision of the pinned source, the citation MUST be reviewed — adopt the revision or re-affirm the pin, with the decision dated (the ISO dated-reference discipline).
- **Rolling (undated) is the exception**, admissible only for a whole-document reference whose *any* future change the claim survives, with a recorded `rolling-rationale` and a standing monitoring duty; claim text written to survive arbitrary change (no quoted numbers, no section IDs). If a plausible future change of the source would break the claim, it does not qualify — pin it.
- **Divergence records:** where doctrine pins revision N while the publisher supersedes to N+1, the citation carries a `deviation` — pinned revision, publisher status, owner, **expiry** — and its review fires on movement of either side. (The expiry element is this design's addition over the observed regulatory precedent, aligning divergence records with the exception contract.)
- Full field shape: class, scope, role, durable identifier, pinned-revision or rolling-rationale, accessed-date, archived-url, optional content-hash (drift detection), publisher-status, successor, deviation, supports-claims with strengths, review-trigger. [../REFERENCES.md](../REFERENCES.md) carries this shape for new entries.

## 7. Composition With Existing Machinery

- **[Revision-pinned control profiles](revision-pinned-control-profiles.md) take precedence for profile-carried sources.** Where a cited document is also a pinned control-profile baseline, supersession fires the profile pattern's migration machinery and the citation record points at the profile entry — no second pin is opened. This pattern's `deviation` field generalises the profile pattern's divergence handling to non-profile citations; it does not replace it.
- **Promotion is re-admission** at the higher floor — [doctrine-content-lifecycle.md](doctrine-content-lifecycle.md) §2 carries the wiring: re-fetch and re-verify (content drift), re-grade, rolling→pinned, publisher-status check, sub-floor exceptions called out in the promotion review.
- **Source events are sweep-anchored** — lifecycle §8 carries the reference-status leg and the event table: rescinded/disavowed sources immediate on discovery; events on MUST-supporting sources prioritised at the next sweep; calendar latency only where an estate names monitoring tooling and an owner. A Superseded doctrine file keeps its pinned citations untouched (frozen history).

## 8. Audits And Failure Modes

- **Diagonal-collapse audit** (run in each lifecycle sweep): sample graded claims and test whether class and support correlate suspiciously — many S1/C1 and S6/C3 pairs with nothing off-diagonal means the axes have collapsed into a prestige ladder and grading has become ritual. The audit's evidence is the sweep record. *(The audit mandate rests on C2 evidence with a stated risk asymmetry: it costs minutes per sweep, while the failure it guards against silently voids the entire scheme; the 87% field-collapse figure is single-source and flagged as such — it is the best available signal of how fast decay happens, not a measured constant.)*
- **Anti-patterns:** *Prestige ladder* — grading only sources, never claim support. *Two copies of the norm* — demanding corroboration for conformance claims. *Mirror as primary* — citing a transcription or unofficial mirror as the canonical leg. *Archive later* — deferring the snapshot past admission (later is too late). *Permanent downref* — an evidence exception renewed indefinitely instead of routed to policy. *Fame promotion* — raising a source's class because its author is canonical (corroboration raises C, never S). *Rolling by default* — undated references without the survivability test, delegating change control unknowingly.

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Two axes, not one | The convergent design of the two disciplines that grade at scale; single-axis schemes documented to collapse into prestige ranking |
| Written independence test | Axis collapse begins at corroboration-by-affiliates; the test is what makes C1 mean something |
| Conformance/empirical split | Removes the gate's largest false-positive class (demanding two RFCs) and grounds S5-in-scope on the legal scoping lesson |
| Floors keyed to BCP-14, not universal | A MAY does not deserve a MUST's evidence bill; proportionality per [normative-language-applicability-and-exceptions.md](normative-language-applicability-and-exceptions.md) |
| Exceptions in a register, once | RFC 3967/8067 downref economics: adjudicate once, reuse while in force, keep the upgrade worklist visible |
| Forward-only with swept back-catalogue | A 771-citation big-bang retrofit is the deferral-debt trap; sweeps give the retrofit an owner, trigger, and retirement condition |
| Archival SHOULD (not MUST) today | Typing an unmeetable MUST while archival tooling is absent would be theatre; the escalation condition is recorded |

## References

Per this pattern's own §6: all entries accessed 2026-08-12, pinned by immutable identifier where one exists; classes inline; full verification state per the research note's §8 ledger, which serves as these citations' metadata record.

- RFC 3967 / RFC 8067 (BCP 97) — downward references with registered exceptions (S1, pinned by RFC number): https://www.rfc-editor.org/rfc/rfc3967.html · https://www.rfc-editor.org/rfc/rfc8067.txt
- RFC 7322 — RFC Style Guide §4.8.6 (URI stability; dated URIs required where available) (S1, pinned by RFC number): https://www.rfc-editor.org/rfc/rfc7322.html
- ISO/IEC Directives, Part 2, ed. 9.0 (2021) — clauses 10 (normative references, dated/undated) and 15.5 (S1, pinned by edition; canonical page bot-blocks — retrieved copy per the note's M6): https://www.iso.org/sites/directives/current/part2/index.xhtml
- W3C — Normative References guidebook and URI Persistence Policy (S2, rolling with monitoring duty — living Team pages): https://www.w3.org/2013/09/normative-references · https://www.w3.org/Consortium/Persistence.html
- NIST — withdrawal practice (structured tombstones with superseding-publication identifiers) (S2, pinned example page): https://csrc.nist.gov/pubs/sp/800/171/r2/upd1/final
- Guyatt et al. — GRADE, BMJ 2008;336:924 (per-claim certainty; recommendation decoupling) (S3, pinned by citation/PMC id): https://pmc.ncbi.nlm.nih.gov/articles/PMC2335261/
- Garousi, Felderer & Mäntylä — multivocal literature review guidelines, IST 106 (2019) (S3 `preprint` of the published article, pinned by arXiv id): https://arxiv.org/pdf/1707.02553
- Zittrain, Albert & Lessig — *Perma*, 127 Harv. L. Rev. F. (2014); Klein et al., *Scholarly Context Not Found*, PLOS ONE (2014) — link rot and content drift (both S3, pinned by citation/DOI): https://harvardlawreview.org/forum/vol-127/perma-scoping-and-addressing-the-problem-of-link-and-reference-rot-in-legal-citations/ · https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0115253
- Evidence provenance and the full graded ledger: [../evolution/research-source-authority-and-evidence-weighting-2026-08.md](../evolution/research-source-authority-and-evidence-weighting-2026-08.md) §8 (Admiralty/ICD 203 rows there; the 87% diagonal and GRADE κ figures are single-source, flagged)
