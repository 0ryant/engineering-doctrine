# ADR 0043: Replace Agent Co-Authorship Disclosure With A Method Record

- **Status:** Accepted
- **Decision date:** 2026-08-16
- **Recorded date:** 2026-08-16
- **Retrospective:** No
- **Amends:** [ADR 0008](0008-add-code-review-and-change-approval-pattern.md) — [code-review-and-change-approval.md](../../doctrine/patterns/code-review-and-change-approval.md) §6 row 1 (the disclosure *instrument*, not the disclosure *duty*)

## Context

[code-review-and-change-approval.md](../../doctrine/patterns/code-review-and-change-approval.md) §6 row 1 requires agent-authored PRs to **disclose in the PR** "which parts are model- or agent-generated, and what a human actually edited". The duty is sound. The instrument the ecosystem converged on to satisfy it — a `Co-Authored-By:` commit trailer naming the model — is defective in two independent ways, and the defects point in opposite directions from each other.

**Defect 1 — category error.** `Co-Authored-By:` is a Git convention that confers **authorship standing**: it is designed for pair programming and patch attribution, where the named party is a person who can hold copyright, accept accountability, be asked to defend the change under incident pressure, and be on call when it fails. A model has none of those properties. No estate writes `Co-Authored-By: rustfmt`, `Co-Authored-By: gcc`, or `Co-Authored-By: <IDE refactoring engine>`, and the reason is not that those tools contribute less — a refactoring engine can rewrite more lines than a model does. The reason is that tools do not co-author. The trailer asserts a relationship that does not exist, and the assertion is not made more accurate by the tool being probabilistic.

**Defect 2 — fidelity collapse.** Even read charitably as "a model was involved", the trailer is one undifferentiated bit spanning an enormous range: an unreviewed completion accepted verbatim at one end; at the other, output produced under an engineer's own harness, governed by that engineer's own doctrine, and materially rewritten before it landed. Those are not the same engineering act, and a marker that cannot distinguish them is a poor provenance signal in the precise sense this library already recognises elsewhere — it invites a reader to infer origin from a mechanism marker.

This library has solved defect 2 before, in this exact shape. The cohort's signing tools do not claim "signed"; their receipts **self-label a key class** (`dev` → `deployment` → `origin`) so that a mechanism demonstration cannot be misread as an origin claim, and a dev-key receipt says so on its face. The response to a low-fidelity claim was to **grade it**, not to delete it. `Co-Authored-By: <model>` is the `class=dev` of authorship.

Applying that precedent naively would produce *graded co-authorship*, which fails defect 1: it grades the wrong noun. Authorship is not a spectrum to be subdivided here, because authorship and accountability are held whole by the human who owns the code, the outcomes, and the risk. What varies between changes is not who authored them but **by what method the candidate was produced**. Those are separate facts and this library already keeps separate facts in separately addressable records ([normative-language-applicability-and-exceptions.md](../../doctrine/patterns/normative-language-applicability-and-exceptions.md) §2). The same split already exists in the cohort's supply-chain layer: an artifact has an **owner**, and a **provenance record** describes how it came to exist. Different fields, deliberately.

Deleting the trailer with no replacement is the third failure mode. It resolves both defects by removing the evidence, leaving the record silent — strictly less information than a bad signal, and it forfeits the engineer's own strongest claim (a pinned, falsifiable, reviewable production process) rather than recording it.

## Decision

1. **Authorship is singular, human, and ungraded (normative).** A non-human tool MUST NOT be named in an authorship field — `Author`, `Co-Authored-By`, `Signed-off-by`, or any successor convention that confers authorship standing or accountability. This is a **prohibition on miscasting**, not a licence to conceal: it removes an inaccurate instrument and decision 2 supplies an accurate one. The engineer named as author holds authorship, ownership, and accountability whole, and the tools used are not co-holders of any of them.

2. **The disclosure duty is discharged by a method record, not an authorship claim (normative).** §6 row 1 is amended: what MUST be recoverable for an agent-assisted change is **how the candidate was produced**, carried in a field that makes no authorship claim. The duty in row 1 is preserved and its instrument is replaced. Recording the method is the adopter's own engineering evidence about a change they already own — the same logic by which a pre-resolution gate emits a receipt for a decision the operator already owns; the receipt documents process and does not dilute ownership.

3. **Method-record schema (normative, vendor-neutral).** The record MUST carry, at minimum, a **class** and the **revision-pinned identity of any harness and governing ruleset** that shaped the output. Expressed as a Git trailer:

   ```
   Produced-With: harness=<id>@<rev>; doctrine=<id>@<rev>; class=<class>
   ```

   Per [ADR 0027](0027-keep-public-doctrine-implementation-neutral.md), this library specifies the **schema and class vocabulary only**. Concrete harness identifiers, ruleset identifiers, and transport (trailer, PR template field, or attestation) are estate bindings and MUST NOT be named in publishable doctrine. `Produced-With` is the recommended trailer key because it names tooling without implying standing; an estate MAY select another key provided it is not an authorship field (decision 1).

4. **Class vocabulary (normative).** Three classes, mirroring the graded-claim discipline of the cohort's key classes:

   | Class | Meaning |
   | --- | --- |
   | `generated` | Model or agent output accepted substantially as produced; human review was inspection, not material revision. |
   | `curated` | Model or agent output produced under a declared harness and governing ruleset, then **materially revised** by the named author, who can defend the result without reference to the tool. |
   | `authored` | Written by the named author. Ordinary tool assistance (completion, formatting, refactoring engines) does not change this class. |

   The class asserted MUST be the one the named author can defend under review. `curated` is not a courtesy upgrade from `generated`; it is a claim that the harness and ruleset were pinned and the output was materially revised, and it is falsifiable by reading the diff against the cited revisions.

5. **Applicability (scope-gated).** The method record is **MUST** in estate-governed and production delivery paths where §6 already applies, and **SHOULD** for local single-user development. `authored` changes MAY omit the record entirely — its absence is the default claim, so no adopter is obliged to stamp ordinary work. Nothing here creates a regulatory claim for adopters ([ADR 0023](0023-add-ai-adoption-control-coverage-inventory-challenge-testing-continuity-literacy.md) precedent); estates with an external transparency obligation route it through a registered control profile ([revision-pinned-control-profiles.md](../../doctrine/patterns/revision-pinned-control-profiles.md)), as [ADR 0032](0032-add-ai-act-transparency-slopsquatting-gate-and-model-dataset-admission.md) decision 1 established.

6. **Unchanged.** Every other §6 row stands: the author must explain and own the change; the same automated gates apply; dependency and lockfile diffs get explicit human review; no rubber stamps on large generated volume; separation of duties where the estate requires it; security-critical paths require the approving human to understand the diff. Decision 1 **strengthens** the "author must explain and own" row by removing the field that implied shared ownership.

7. **Style ruling (per [ADR 0028](0028-adopt-claim-level-authority-applicability-and-exceptions.md) discipline).** New normative content uses typed capitalised BCP-14 keywords, consistent with ADR 0031/0032 practice for new sections. The amended §6 row is rewritten in the table's existing register; retrofitting the remaining rows is deferred, not implied.

## Alternatives Considered

### Keep `Co-Authored-By: <model>`

Rejected on decision 1. The convention confers standing on a party that holds nothing and can be asked for nothing. Volume of contribution is not the test — a formatter may rewrite more lines than a model — so "it contributed a lot" does not repair the category error.

### Strip agent attribution entirely, with no replacement

Rejected. It resolves both defects by deleting the evidence. Silence is not neutral: it removes a reviewer's ability to know a harness was involved, and it discards the adopter's own best evidence — a pinned, falsifiable production process — in favour of an unmarked commit. It also leaves §6 row 1 with a duty and no instrument, which is the drift this ADR exists to close.

### Graded co-authorship (`Co-Authored-By` plus a class qualifier)

Rejected. It applies the right precedent (grade the claim) to the wrong noun. Grading authorship concedes that some authorship belongs to the tool; the whole point of decision 1 is that none does.

### A binary `AI-Assisted: yes/no` field

Rejected on defect 2. It is the existing trailer with the category error removed and the fidelity collapse retained, and it invites exactly the "AI built this" reading that motivated the change.

### Free-text disclosure in the PR body only

Rejected as the sole instrument. It is unparseable, absent from the commit record, and lost when a PR is squashed or the forge is migrated. It remains a valid **supplement** — §6 row 1 already asks which parts a human actually edited, and prose is the right medium for that narrative.

## Consequences

### Positive

- The record stops asserting a relationship that does not exist, and starts asserting one that does and is checkable.
- Engineers who build the harness and write the governing ruleset can finally **make that claim in the record**. Today the only available vocabulary says the opposite of the truth; `curated` with pinned revisions is a stronger, more credible claim than either an unmarked commit or a model co-author line.
- Provenance becomes falsifiable rather than declarative: a cited harness revision and ruleset revision can be read against the diff.
- Authorship and method become separately addressable records, consistent with §2 of the normative-language pattern and with the owner/provenance split the supply-chain layer already uses.
- §6 keeps its duty, so no consumer loses a control.

### Costs And Risks

- **Class inflation.** `curated` is more flattering than `generated`, and nothing mechanically prevents claiming it. The mitigation is that the claim is falsifiable against the cited revisions and is subject to the same review as any other assertion — but the library should not pretend this is enforced.
- **Revision pinning is a real cost.** Citing a harness and ruleset revision per change requires those to be versioned and reachable. Estates without that discipline will find `curated` unclaimable, which is the correct outcome but is still friction.
- **Trailer-key fragmentation.** Leaving the key to estates (per ADR 0027) means cross-estate tooling cannot assume `Produced-With`. Accepted: naming a concrete key in publishable doctrine would breach implementation neutrality.
- **This ADR does not settle external transparency obligations.** Where an estate has one, decision 5 routes it to a control profile; the method record is engineering evidence, not a compliance artifact, and must not be described as one.
- **Migration is unbounded.** Existing history carries the old trailer. This ADR is prospective; rewriting published history is out of scope and not recommended.

## Consumer Impact

**Change class:** normative for consumers on estate-governed or production agent-assisted delivery paths; additive guidance otherwise.

**Compatibility proposal:** 0.x minor. Decision 1 introduces a new `MUST NOT` on authorship fields, which is a genuine tightening — an adopter currently emitting `Co-Authored-By: <model>` becomes non-conformant and must migrate to a method record. Decision 2 replaces the instrument of an existing duty rather than adding one, and decision 5 leaves `authored` changes unmarked, so the net stamping burden on ordinary work is nil.

## Acceptance Evidence

- [x] Amended [code-review-and-change-approval.md](../../doctrine/patterns/code-review-and-change-approval.md) §6 row 1 (instrument replaced, duty preserved) and added **§6.1 The Method Record** with the class table, applicability, and the estate-binding note.
- [x] Cross-linked from [ai-ml-systems.md](../../doctrine/principles/ai-ml-systems.md) §4 ("Agents are not co-authors", with the failure-prevented clause) and [ai-adoption-controls.md](../../doctrine/patterns/ai-adoption-controls.md) §2 ("Accountability does not transfer to a tool").
- [x] Glossary entries added: **Agent co-authorship (anti-pattern)** and **Method record**, cross-referencing each other. `Produced-With` is cited as a recommended key, never a mandate.
- [x] [SITEMAP.md](../../doctrine/SITEMAP.md) regenerated via the change harness preflight.
- [x] No new external references, so [REFERENCES.md](../../doctrine/REFERENCES.md) is unchanged. The argument rests on an internal category distinction and on existing in-repo precedent (graded key classes in the cohort's signing tools), not on a new external authority.

### Honest gaps in this acceptance

- **Council review was not run.** The change harness asks for it on policy-shaping changes; this ADR was accepted by direct operator decision on 2026-08-16 instead. Recorded here rather than presented as satisfied.
- **No research note was produced.** The harness's research leg is unmet; the Context section carries the reasoning inline.
- **`Signed-off-by` is unresolved.** Decision 1's `MUST NOT` names authorship fields. `Signed-off-by` carries **DCO** semantics — a certification of the right to submit — rather than an authorship claim, so it is deliberately *not* swept in by analogy. Whether a tool may ever appear there is left open for a later ADR.
- **Class inflation remains unenforced**, as recorded under Costs And Risks. Nothing in this amendment detects a `curated` claim that the diff does not support.
