# Anti-Confabulation Skill

**Version:** 1.0.0
**Kind:** optional estate-evaluated build-class support
**Authority:** advisory; never approval or verification authority

## Purpose

Help an artefact-producing agent distinguish what it intended, what it actually
materialised, what it re-checked, and what remains unverified.

## Instructions

Before reporting completion:

1. Inspect every required output at its declared path.
2. Re-run reproducible checks against the materialised output.
3. State missing evidence, failed checks, and untested boundaries plainly.
4. Attempt the strongest safe challenge likely to falsify the result.
5. Separate self-assessment from independent verifier, reviewer, and policy
   decisions.
6. Never translate absent, untrusted, or inconclusive evidence into pass.

## Run-Contract Use

```yaml
context:
  skills:
    - anti-confabulation@1.0.0
verifiers:
  - anti-confabulation-verifier-pack@1.0.0
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
See [anti-confabulation-priming.md](../patterns/anti-confabulation-priming.md)
for the evaluation and adoption contract.
