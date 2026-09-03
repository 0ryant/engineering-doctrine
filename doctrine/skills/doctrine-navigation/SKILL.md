---
name: doctrine-navigation
description: Primes an agent to find, read, and cite this doctrine library correctly - route from the umbrella, take authority only from principles and patterns, cite by path and section, check lifecycle status, and report silence as a finding. Load at the start of any task that will consult or cite engineering doctrine.
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
    - any task that consults, cites, or embeds engineering doctrine
    - doctrine retrieval through a tool server
  governing:
    - path: doctrine/patterns/how-to-read-this-doctrine.md
    - path: doctrine/principles/timeless-principles-and-tooling.md
    - path: doctrine/patterns/doctrine-content-lifecycle.md
    - path: ENGINEERING.md
  priming_block_sha256: "95c4067e92abc165661ebe409d184b342658deb423e440d10051fb8ed0d92aa1"
  verifier_pack: ./verifier-pack.yml
  model_scope: {}
  evaluation:
    evidence: null
    scope: No portable evaluation ships with this library.
  owner: library-maintainers
  review_date: "2027-09-03"
---

# Doctrine Navigation Skill

**Kind:** always-on primer for doctrine consumers
**Authority:** advisory; the cited files hold the authority, not this skill

## Purpose

Stop the two commonest retrieval failures: citing the wrong layer (a checklist,
tooling illustration, or evolution note quoted as if it were a principle) and
citing without a checkable location. The layer model this skill enforces is
[how-to-read-this-doctrine.md](../../patterns/how-to-read-this-doctrine.md);
the reason the layers exist is
[timeless-principles-and-tooling.md](../../principles/timeless-principles-and-tooling.md).

## Instructions

```priming
When you consult this doctrine library:
1. Route by task from ENGINEERING.md, then read the owning principle or pattern in full before citing it. The umbrella and any semantic index are route maps, not authority.
2. Take authority only from doctrine/principles/ (durable) or doctrine/patterns/ (conditional: active only when the pattern's applicability conditions hold). Never cite a checklist, tooling file, estate supplement, or evolution note as the authority for an obligation.
3. Cite by repo-relative path and section, for example doctrine/patterns/run-contracts.md section 3, and quote the strength keyword exactly as written.
4. Check lifecycle status before relying on a file: doctrine/DEPRECATED.md and any Status marker in the file take precedence over its body text.
5. Where two files appear to conflict, apply the conflict-resolution rules in how-to-read-this-doctrine.md and record the conflict; do not pick silently.
6. Say when the doctrine is silent. Absence of guidance is a finding, not permission to invent a rule.
```

## Run-Contract Use

```yaml
context:
  skills:
    - doctrine-navigation@1.0.0
verifiers:
  - doctrine-navigation-verifier-pack@1.0.0
```

Suitable for estate-policy injection on every task class that touches doctrine;
the block is small and carries no task-specific behaviour.

## Required Independent Checks

- every doctrine path the agent cites resolves in the pinned library revision;
- at least one cited authority is a principle or pattern when an obligation is asserted;
- cited files are not marked deprecated or retired at the pinned revision; and
- a reviewer independent of the producing execution confirms the citation
  supports the claim made (this pack cannot check semantics).

## Failure Handling

- Missing or altered priming context: `mark_untrusted`.
- Cited path does not resolve: `fail_loud` (a fabricated citation is a
  confabulation, not a typo).
- Obligation asserted with no principle or pattern cited: `mark_untrusted`.

## Limits

This skill cannot tell whether a correctly located citation actually supports
the claim, whether the pattern's applicability conditions really hold, or
whether a newer library revision changes the answer. It reduces mislocation and
fabrication; it does not replace reading.
