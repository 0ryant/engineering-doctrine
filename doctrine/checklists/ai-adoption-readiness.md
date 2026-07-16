# AI Adoption Readiness Checklist

Use when an organisation or team is **adopting, expanding, or reviewing** AI use (built, embedded, or vendor-supplied). Aligns with [patterns/ai-adoption-controls.md](../patterns/ai-adoption-controls.md) and [principles/ai-ml-systems.md](../principles/ai-ml-systems.md); per-system engineering depth (retrieval, agents, change path) stays with those files. Decision record: [ADR 0023](../../docs/adr/0023-add-ai-adoption-control-coverage-inventory-challenge-testing-continuity-literacy.md).

## Inventory And Materiality

```text
[ ] AI system inventory exists and includes embedded / vendor / copilot-class AI, not only in-house builds
[ ] Every entry has a named first-line owner (role + escalation path), capability tier (A–D) AND materiality tier
[ ] High-materiality entries map to the business services they support; controls scale with max(capability, materiality)
[ ] Inventory reconciled on material change and at least quarterly; production AI absent from it is treated as a finding
[ ] Sanctioned path for registering new AI use is cheap enough that teams actually use it (shadow-AI posture: no-blame discovery)
```

## Ownership And Challenge

```text
[ ] First-line owner is accountable for purpose, data inputs, acceptable use, and human-oversight mode per system
[ ] High-materiality systems get pre-launch and on-material-change review by a challenger with incentives, competence, and influence to force change (not the building team)
[ ] Person-affected automation has: designed human fallback (unavailable / low-confidence / contested), overseer override authority + affordance, and a contest path reaching a human who can reverse the decision
[ ] Per-decision logging is sufficient to reconstruct and explain a contested decision (tested, not assumed)
```

## Harm-Surface Testing

```text
[ ] Performance/accuracy regression on golden or held-out set, re-run on model / prompt / corpus change
[ ] Person-affected outputs: fairness/bias evaluation before launch and on retrain or model swap; metric choice recorded and justified per system
[ ] Production models: continuous drift monitoring (input distribution + output quality) with alert thresholds and a retrain/rollback path
[ ] GenAI: prompt-injection (direct + indirect) tests; jailbreak/guardrail-bypass red-team where safety or policy constraints exist
[ ] GenAI feeding downstream systems: output validation (schema, sanitisation, groundedness); leakage probing (system prompt, training/context data, cross-tenant)
```

## Third-Party AI Continuity

```text
[ ] Due diligence proportionate to materiality recorded per provider (data handling, subprocessors, training-on-your-data terms, audit rights or documented residual risk)
[ ] Contracts cover availability SLAs, deprecation/notice windows for model change, incident notification
[ ] Concentration assessed before contracting (how many critical systems already sit on this provider?)
[ ] High-materiality systems: exit/substitution plan with named substitute, portable eval assets, and a provider-impairment game day that has actually run
[ ] Loss-of-provider answer decided in advance (failover / queue-and-degrade / stop) and wired to the incident process
```

## Capability Uplift

```text
[ ] Acceptable-use artifact published and versioned: approved tools/uses, prohibited ones with the why, and the registration path
[ ] Literacy is role-based: builders (harm-surface classes), operators/reviewers (limits + override, automation bias), approvers (enough to challenge), users (boundaries + what never to paste)
[ ] Training/uplift tracked as evidence and refreshed on material system change
```
