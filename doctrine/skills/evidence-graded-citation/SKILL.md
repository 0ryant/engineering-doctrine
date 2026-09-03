---
name: evidence-graded-citation
description: Primes an agent to cite sources with a source-authority class and a claim-support grade, record accessed dates and pinned revisions, hunt for disconfirming sources, and respect the admission floors for MUST and SHOULD claims. Load whenever an agent supports a claim with external evidence - research notes, ADR context, doctrine drafting, or a recommendation the reader will act on.
license: Apache-2.0
doctrine:
  schema_version: "1.0.0"
  version: "1.0.0"
  kind: primer
  authority: advisory
  injection: estate-policy
  status: active
  tier: 0
  applies_to:
    - research notes and evidence ledgers
    - ADR context and rationale sections
    - drafting or promoting typed doctrine claims
    - recommendations that cite external sources
  governing:
    - path: doctrine/patterns/source-authority-and-evidence-grading.md
    - path: doctrine/patterns/doctrine-content-lifecycle.md
      section: "2"
    - path: doctrine/EVIDENCE-EXCEPTIONS.md
  priming_block_sha256: "c868ebaa18063b530cb918749bc2e929c5e6c2ea400a4b6e867e3a8d97d27676"
  verifier_pack: ./verifier-pack.yml
  model_scope: {}
  evaluation:
    evidence: null
    scope: No portable evaluation ships with this library.
  owner: library-maintainers
  review_date: "2027-09-03"
---

# Evidence-Graded Citation Skill

**Kind:** always-on primer for any evidence-bearing output
**Authority:** advisory; grades are the author's claim and are reviewable

## Purpose

Make the two-axis scheme of
[source-authority-and-evidence-grading.md](../../patterns/source-authority-and-evidence-grading.md)
mechanical at the point of writing: every citation says what kind of source it
is, every claim says how well it is supported, and the admission floors for
normative strength are applied before a MUST is written rather than discovered
at review.

## Instructions

```priming
When you cite a source to support a claim:
1. Tag every citation with its source-authority class S1 to S7 or X, record the accessed date, and pin the revision where the source is versioned.
2. Grade the claim, not the citation. C1 needs two independent S1-S4 sources with no credible contrary source; C2 needs one S1-S4 source or two independent S5-S6 sources; C3 is a single S5-S6 source or practitioner consensus; C4 is conflicting evidence or X-only support. Independent means different organisations with different incentives.
3. A MUST needs C1, or C2 with a stated risk asymmetry, or a registered entry in doctrine/EVIDENCE-EXCEPTIONS.md. A SHOULD needs C2, and single-source support must be flagged at the claim. X supports no normative claim.
4. Conformance claims are satisfied by the pinned norm itself; do not demand a second copy of a standard. Empirical claims about people and organisations cap at C2 on practitioner sources alone.
5. Look for disconfirming sources before grading. "No contrary evidence found after looking" is a statement you must be able to defend by saying where you looked.
6. Write the grade beside the claim as [S<n> C<n>, accessed YYYY-MM-DD]. A citation you cannot classify is X.
```

## Run-Contract Use

```yaml
context:
  skills:
    - evidence-graded-citation@1.0.0
verifiers:
  - evidence-graded-citation-verifier-pack@1.0.0
```

## Required Independent Checks

- every external citation carries a source class and an accessed date;
- every graded claim carries a support grade consistent with its citation set;
- no MUST-level claim is graded below C2, and C2 MUSTs state a risk asymmetry
  or cite an EVIDENCE-EXCEPTIONS entry; and
- a reviewer independent of the producing execution spot-checks that the cited
  source says what the claim needs (this pack cannot read sources).

## Failure Handling

- Missing or altered priming context: `mark_untrusted`.
- Citation without class or date: `mark_untrusted`.
- MUST claim graded C3 or C4: `fail_loud` (below the admission floor).

## Limits

The pack checks form, not truth. It cannot tell whether a source was read,
whether two sources are really independent, or whether a stated risk asymmetry
is credible. Those remain review judgements.
