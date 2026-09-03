---
name: anti-confabulation
description: Primes an artefact-producing agent to separate what it intended, what it materialised, what it re-checked, and what remains unverified before it reports completion. Load for build-class tasks (code generation, evidence-pack emission, tool-wrapper generation, implementation work whose claims can be re-tested against artefacts).
license: Apache-2.0
doctrine:
  schema_version: "1.0.0"
  version: "1.1.0"
  kind: primer
  authority: advisory
  injection: estate-policy
  status: active
  tier: 0
  applies_to:
    - build-class tasks whose claims can be re-tested against materialised artefacts
  governing:
    - path: doctrine/patterns/anti-confabulation-priming.md
    - path: doctrine/patterns/verifier-packs.md
      section: "5"
    - path: doctrine/patterns/run-contracts.md
      section: "3"
  priming_block_sha256: "d5060d72a20abe0c394ccc46259a855ea852a3ca85d499a064dbb72abb9549e6"
  verifier_pack: ./verifier-pack.yml
  model_scope: {}
  evaluation:
    evidence: null
    scope: No portable evaluation ships with this library. Estates evaluate on representative tasks before enabling estate-policy injection (anti-confabulation-priming.md section 6).
  owner: library-maintainers
  review_date: "2027-09-03"
---

# Anti-Confabulation Skill

**Kind:** optional, estate-evaluated build-class support
**Authority:** advisory; never approval or verification authority

## Purpose

Help an artefact-producing agent distinguish what it intended, what it actually
materialised, what it re-checked, and what remains unverified.

## Instructions

The fenced block below is the priming block. Its SHA-256 is pinned in the front
matter and checked by the sibling verifier pack's `priming_active` assertion.

```priming
Before reporting completion:
1. Inspect every required output at its declared path.
2. Re-run reproducible checks against the materialised output.
3. State missing evidence, failed checks, and untested boundaries plainly.
4. Attempt the strongest safe challenge likely to falsify the result.
5. Separate self-assessment from independent verifier, reviewer, and policy decisions.
6. Never translate absent, untrusted, or inconclusive evidence into pass.
```

## Run-Contract Use

```yaml
context:
  skills:
    - anti-confabulation@1.1.0
verifiers:
  - anti-confabulation-verifier-pack@1.1.0
```

An estate may inject this skill automatically only through a versioned policy
whose supporting evaluation, model/task scope, owner, and review date are
addressable. The expanded run contract must show the injection.

## Required Independent Checks

- required artefacts exist and are non-empty where appropriate;
- declared validation commands execute with recorded inputs and versions;
- changed outputs are bound to the candidate being reviewed;
- limitations and unresolved findings are retained; and
- a verifier or reviewer independent of the producing execution evaluates the
  material claims.

## Failure Handling

- Missing or altered priming context: `mark_untrusted` or `fail_loud` according
  to estate materiality.
- No executable `priming_active` verifier: `inconclusive`.
- Output missing or behavioural check failed: use the underlying verifier's
  failure verdict; the prompt block cannot waive it.

## Limits

This skill cannot prove correctness, independence, provider reliability, or
policy compliance. Its effect may vary across models and task distributions.
See [anti-confabulation-priming.md](../../patterns/anti-confabulation-priming.md)
for the evaluation and adoption contract.

## Version Notes

- **1.1.0** — moved to the `doctrine/skills/<name>/SKILL.md` layout required by
  [verifier-packs.md §6](../../patterns/verifier-packs.md), added the machine-readable
  manifest ([contracts/skill.v1.schema.json](../../../contracts/skill.v1.schema.json)),
  delimited the priming block so its hash is reproducible, and shipped the sibling
  verifier pack that 1.0.0 referenced but never carried. The instruction text is
  unchanged from 1.0.0; the 1.0.0 hash was not reproducible from the file and is
  not carried forward ([ADR 0044](../../../docs/adr/0044-adopt-agent-facing-consumption-contract-skill-schema-and-server-boundary.md)).
