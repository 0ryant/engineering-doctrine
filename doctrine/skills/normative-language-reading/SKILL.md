---
name: normative-language-reading
description: Primes an agent to read and write doctrine claims at the right strength - BCP 14 keywords only when capitalised, strength per claim never per document, applicability checked before a claim is applied, exceptions recorded with authority and expiry, and missing evidence never treated as a pass. Load whenever an agent interprets, applies, or drafts normative engineering guidance.
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
    - interpreting or applying doctrine claims to a change, design, or review
    - drafting or editing normative text
  governing:
    - path: doctrine/patterns/normative-language-applicability-and-exceptions.md
    - path: doctrine/patterns/how-to-read-this-doctrine.md
    - path: doctrine/patterns/verifier-packs.md
      section: "4"
  priming_block_sha256: "b0df0b06c6fabdb03f872cf404020b500e229d62f8379afe85ae02fc0ecae3a5"
  verifier_pack: ./verifier-pack.yml
  model_scope: {}
  evaluation:
    evidence: null
    scope: No portable evaluation ships with this library.
  owner: library-maintainers
  review_date: "2027-09-03"
---

# Normative Language Reading Skill

**Kind:** always-on primer for doctrine consumers and authors
**Authority:** advisory; the strength of a claim is set by its owning file, not by this skill

## Purpose

Agents over-read and under-read normative text in predictable ways: they treat
bold or imperative prose as a rule, assign one strength to a whole document,
apply profile-scoped obligations universally, and turn missing evidence into a
pass. This skill installs the reading discipline of
[normative-language-applicability-and-exceptions.md](../../patterns/normative-language-applicability-and-exceptions.md)
so those failures are caught at the point of reading.

## Instructions

```priming
When you read or write a doctrine claim:
1. Only capitalised MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY carry BCP 14 force; CONTEXT-DEPENDENT and EXAMPLE are library content classes. Bold type, imperative tone, or a checkbox creates no obligation.
2. Read strength per claim, never per document. Report a claim as: <path> section <n>: <keyword> - <outcome preserved or failure prevented>.
3. Before applying a claim, confirm its applicability overlay: baseline, named profile, or binding external authority. A profile-scoped MUST is not universal.
4. Departure from a MUST requires a recorded exception naming the claim, the accountable authority, the compensating control, and an expiry. Departure from a SHOULD requires a recorded reason when material. Silence grants no permission.
5. Absent, failed, untrusted, or inconclusive evidence is never a pass. Say which of the four it is.
6. When two claims conflict, prefer the stricter result where both protect the same property; otherwise record the conflict for an accountable decision rather than resolving it yourself.
```

## Run-Contract Use

```yaml
context:
  skills:
    - normative-language-reading@1.0.0
verifiers:
  - normative-language-reading-verifier-pack@1.0.0
```

## Required Independent Checks

- claims the agent reports carry a per-claim strength and a locating citation;
- no report assigns a single strength to an entire document;
- every exception the agent proposes carries claim, authority, compensating
  control, and expiry; and
- a reviewer independent of the producing execution confirms the applicability
  reading, which this pack cannot check.

## Failure Handling

- Missing or altered priming context: `mark_untrusted`.
- Document-wide strength assigned: `mark_untrusted`.
- Exception proposed without expiry or authority: `fail_loud` (an open-ended
  exception is a policy change, not an exception).

## Limits

This skill cannot decide whether a profile applies, whether a stated risk
asymmetry is real, or whether an authority named in an exception actually holds
that authority in the adopting estate. Those are human, estate-bound decisions.
