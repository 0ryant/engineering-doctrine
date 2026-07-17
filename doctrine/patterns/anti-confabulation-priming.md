# Anti-Confabulation Priming

Use this pattern when an AI agent produces code, configuration, evidence packs,
or other material artefacts and may overstate what it created or verified.

Relates to [run-contracts.md](run-contracts.md),
[verifier-packs.md](verifier-packs.md),
[../principles/ai-ml-systems.md](../principles/ai-ml-systems.md), and
[code-review-and-change-approval.md](code-review-and-change-approval.md).

## 1. Boundary

Prompted self-critique can improve an agent's inspection behaviour, but it is not
independent evidence. The producing model remains one actor with correlated blind
spots across generation, review, and self-scoring.

Therefore:

- priming MAY make the producer more cautious and explicit;
- priming MUST NOT convert a self-score into approval authority;
- material claims still require independent, discriminating verification; and
- missing, untrusted, or inconclusive verification remains non-pass.

## 2. Portable Priming Block

An estate may version a short block with these instructions:

```text
Before reporting completion:
1. Inspect the materialised outputs, not only the plan or command exit code.
2. Re-run the checks that an independent reviewer can reproduce.
3. Name missing evidence, uncertainty, and any untested boundary.
4. Predict the strongest credible challenge to the result and test it when safe.
5. Do not claim that self-review, confidence, or fluent explanation proves the work.
```

The exact wording is replaceable. The invariant is that the producer is prompted
to distinguish assertion, materialised output, reproducible check, and independent
authority.

## 3. When To Apply

Apply only through an explicit, versioned estate policy. Good candidates are:

- artefact-producing tasks with observable required outputs;
- tasks where the agent can re-run deterministic checks safely; and
- task classes for which local evaluation shows the block improves evidence
  quality without increasing refusal or hiding uncertainty.

Do not universalise a block from one model or benchmark. Re-evaluate when the
model, prompt stack, tool surface, or task distribution changes materially.

## 4. Run-Contract Binding

When enabled, bind the priming policy in the run contract:

```yaml
context:
  skills:
    - anti-confabulation@1.0.0

verifiers:
  - anti-confabulation-verifier-pack@1.0.0
```

The contract or policy expansion record must identify:

- the priming-block version or digest;
- the task classes for which it is enabled;
- the model/provider scope of the supporting evaluation;
- the independent verifier pack; and
- the owner and review date for the policy.

### 4.1 Policy injection

A run-contract compiler MAY inject the skill for estate-defined `build-class`
tasks. Injection is not a universal doctrine default: it requires an addressable
estate policy and evaluation. The expanded contract must record the injected
skill so the run does not gain invisible context.

## 5. Verifier-Pack Pairing

Priming needs a sibling verifier that checks presence and integrity of the
rendered block; it does not score whether the model obeyed it.

```yaml
assertions:
  - id: priming-block-present
    kind: priming_active
    expected: true
    failure_mode: mark_untrusted
    severity: error
```

The verifier reads the rendered run context, isolates the versioned block, and
compares its digest with the policy record. Missing or modified context is
`mark_untrusted` or `fail_loud` according to estate materiality. If no executing
engine implements `priming_active`, the verdict is `inconclusive`; schema
declaration alone never counts as execution.

## 6. Evaluation Contract

Before enabling or widening automatic injection, measure at least:

| Measure | Why |
| --- | --- |
| Required-output existence and correctness | Detects fluent completion claims without artefacts. |
| Independent verifier pass/fail | Separates self-assessment from observable quality. |
| Self-score calibration error | Detects systematic over- or under-claiming. |
| False-refusal rate | Prevents caution prompts from suppressing valid work. |
| Token, latency, and cost delta | Makes the intervention's operational cost visible. |
| Performance by task and model class | Prevents unsafe transfer across distributions. |

Use a held-out or independently authored challenge set where feasible. Record
negative and inconclusive results, not only improvements.

## 7. Failure Modes

- Treating the priming block as proof that the outputs exist.
- Letting the producing model be the sole judge of compliance.
- Hiding injected context from the expanded run contract.
- Carrying one model's measured effect into another without evaluation.
- Optimising calibration while actual correctness or false-refusal rate worsens.
- Declaring the verifier implemented because its kind exists in a schema.
- Allowing a prompt block to replace tests, review, policy, or runtime evidence.

## 8. Consumer Impact

**Change class:** normative replacement. Automatic priming changes from a
universal named-tool rule to an estate-evaluated optional policy. Consumers must
retain independent verification and must not treat prior local measurements as
portable evidence.

## References

- [NIST AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1) — independent,
  documented measurement and accountable governance.
- [Self-Refine](https://proceedings.neurips.cc/paper_files/paper/2023/hash/91edff07232fb1b55a505a9e9f6c0ff3-Abstract-Conference.html)
  — iterative self-feedback can improve outputs in studied settings.
- [Large Language Models Cannot Self-Correct Reasoning Yet](https://proceedings.iclr.cc/paper_files/paper/2024/hash/8b4add8b0aa8749d80a34ca5d941c355-Abstract-Conference.html)
  — cautions that intrinsic self-correction is not reliably general.
- [ADR 0027](../../docs/adr/0027-keep-public-doctrine-implementation-neutral.md)
