# 0012. Model Routing Policy

Status: Accepted
Decision date: 2026-05-20
Recorded date: 2026-05-20
Accepted date: 2026-05-20
Retrospective: No

## Context

AI models vary by task, observability, cost, latency, tool-use reliability, and
the materiality of a wrong answer. A static “largest model everywhere” rule is
wasteful, while self-assessed confidence is not authority to select a cheaper or
less challenged path. Provider model names also change faster than the control
intent.

Routing therefore needs a portable contract that binds selection to estate-owned
evidence, refuses known unsafe task/model combinations, escalates on challenge
results, and limits both individual-run and aggregate spend.

## Decision

Adopt the v1 [router-policy schema](../../contracts/router-policy.v1.schema.json)
with these invariants:

1. The policy has three capability classes: `premium`, `default`, and
   `narrow_scope`. These are control classes, not provider product names.
2. Each estate binds current model identifiers to those classes using versioned
   evaluation evidence for the task classes it permits.
3. `narrow_scope` work is bounded, strongly observable, reversible, and subject
   to independent review at the rate declared by policy. The default sample rate
   is `1.0` until estate evidence justifies a lower rate.
4. `fail`, `falsified`, `untrusted`, or `inconclusive` verifier outcomes cannot
   silently select a weaker tier. They escalate, refuse, or require accountable
   review according to an explicit rule.
5. Refusal rules are non-empty, evidence-bound, scoped to a task/model condition,
   and structurally fail closed when matched.
6. Cost controls include a per-run ceiling and an aggregate session or portfolio
   ceiling. A warning threshold does not replace a hard stop.
7. Routing policy recommends execution; it does not grant tool, merge, release,
   or production authority.

Worked YAML files under `contracts/examples/` illustrate the shape. Their model
identifiers, prices, thresholds, and evidence references are placeholders for
estate-owned values and are not doctrine defaults.

## Consequences

### Positive

- Model/provider changes do not require rewriting the portable policy shape.
- Known failure classes become explicit refusal or escalation rules.
- Cost optimisation cannot silently bypass review or task-scope constraints.
- Routing decisions are reconstructable from policy version and evidence refs.

### Negative

- Each estate must maintain representative evaluations and current pricing.
- Three classes are deliberately coarse and may need a future compatible
  extension for specialised modalities or regulated tasks.
- A schema can validate shape but cannot prove evaluation quality or runtime
  enforcement.

## Consumer Impact

**Change class:** normative replacement of implementation-specific rationale with
a provider-neutral contract. Existing consumers keep the same v1 structural
shape, but must replace inherited model identifiers, evidence links, and cost
numbers with estate-owned records.

## Verification

- Contract examples validate against the v1 schema.
- Every refusal rule has an evidence reference and a fail-closed action.
- Every narrow-scope tier declares independent review.
- No private product, repository, or programme name is part of the contract.

## References

- [NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1) — governed risk
  decisions, measurement, monitoring, and accountable roles.
- [FinOps Framework](https://www.finops.org/framework/) — contextual cost
  accountability; cost is a decision input, not the sole optimiser.
- [ADR 0027](0027-keep-public-doctrine-implementation-neutral.md) — public
  implementation-neutrality boundary.
