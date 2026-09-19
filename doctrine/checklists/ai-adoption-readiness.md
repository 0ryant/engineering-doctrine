# AI Adoption Readiness Checklist

Use when an organisation or team is **adopting, expanding, or reviewing** AI use (built, embedded, or vendor-supplied). Aligns with [patterns/ai-adoption-controls.md](../patterns/ai-adoption-controls.md), [principles/ai-ml-systems.md](../principles/ai-ml-systems.md), and [principles/privacy-and-data-governance.md](../principles/privacy-and-data-governance.md) §5.4 (Art 50 transparency); per-system engineering depth (retrieval, agents, change path) stays with those files. Decision record: [ADR 0023](../../docs/adr/0023-add-ai-adoption-control-coverage-inventory-challenge-testing-continuity-literacy.md).

## Inventory And Materiality

```text
[ ] AI system inventory exists and includes embedded / vendor / copilot-class AI, not only in-house builds
[ ] Every entry has a named first-line owner (role + escalation path), capability tier (A–D) AND materiality tier
[ ] High-materiality entries map to the business services they support; controls scale with max(capability, materiality)
[ ] Inventory reconciled on material change and at least quarterly; production AI absent from it is treated as a finding
[ ] Sanctioned path for registering new AI use is cheap enough that teams actually use it (shadow-AI posture: no-blame discovery)
[ ] Agent financial/transaction authority is default-deny; any grant is per-agent and inventory-recorded (grant record, approver, session caps, expiry, dedicated principal)
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
[ ] Tier-D agents: agent-hijack / tool-flow-abuse evaluation is adaptive (attacker iterates), re-run on model, defence, or agent-surface change — static replay does not count
[ ] GenAI feeding downstream systems: output validation (schema, sanitisation, groundedness); leakage probing (system prompt, training/context data, cross-tenant)
[ ] User-facing GenAI in EU AI Act scope (registered control profile): Art 50 transparency duties for the registered role verified before launch (disclosure UX / output marking for providers; notification / deepfake labelling for deployers)
[ ] Identity-verification or fraud-detection surfaces re-tested against synthetic-media attacks (deepfake voice/video, GenAI phishing, synthetic identities) on a defined cadence, not once
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

## Activated Engineering Controls

Use this routing table when the named surface exists. For each applicable row,
review the linked owner's requirements and record evidence or a scoped exception;
otherwise record why it does not apply. The owner defines strength, triggers and
exceptions. This table adds no requirement and is not a substitute for that review.

| Surface | Evidence to locate | Canonical owner |
| --- | --- | --- |
| Agents holding workload identity | Principal granularity, sponsor/orphan handling, credential scope and delegation attribution | [Zero trust §2.1](../principles/zero-trust-and-workload-identity.md#21-agent-identity) |
| Production or governed MCP pairs | Dated protocol profile, applicable authentication, server allowlist and revision-specific state handling | [AI systems §7](../principles/ai-ml-systems.md#7-retrieval-indexes-agent-context-and-tool-surfaces) |
| AI-proposed dependencies; production models/datasets | Pre-install provenance checks; digest, publisher, signing, safe loading, inventory and dataset lineage as applicable | [AI systems §4](../principles/ai-ml-systems.md#4-engineering-change-path-agents-and-humans) owns the pre-install gate; [supply chain §§7–8](../principles/dependencies-supply-chain.md) owns the adjacent dependency controls |
| Agent responders | Accountable human, predeclared action bounds, stop authority, confirmed incident conclusions and action records | [Incident operations §10](../patterns/incident-lifecycle-and-on-call-operations.md) |
| Production model-mediated calls | Required per-call telemetry, cost/correlation joins and explicitly controlled content capture | [Observability §7](../principles/observability.md) |
| Agent definitions steering privileged automation | Protected change path, provenance, informed non-self review and applicable adversarial checks | [Merge-path integrity §§1–2](../principles/merge-path-evidence-and-pipeline-integrity.md) |
| Agent-writable persistent memory | Admission, retention/forget, decommission and poisoning recovery; managed-platform compensating controls where needed | [AI systems §7](../principles/ai-ml-systems.md#7-retrieval-indexes-agent-context-and-tool-surfaces) |
| Judges gating promotion or automation | Versioned configuration, validation threshold, perturbation tests, escalation and recalibration evidence | [Agent loops §8.2](../patterns/agentic-loop-design.md) |
| Agent financial authority | Default-deny or recorded grant, scoped external budgets, applicable approval, attribution and retry-safe payment records | [Cost and FinOps §7.1](../principles/cost-and-finops.md) |
| Blocking injection/hijack defence claims | Adaptive evaluation at the owner's deployment/change/model-swap triggers; static replay is not equivalent evidence | [Testing §5](../principles/testing-strategy.md) |
| AI/agent spend | Attributable budgets, enforced limits and portable backstops; vendor limits do not remove the floor | [Cost and FinOps §7](../principles/cost-and-finops.md) |

Derivation: [ADRs 0031–0035](../../docs/adr/README.md), including ADR 0032's
amendment to the identity floor. Person-impact/transparency duties remain in the
profile-gated Harm-Surface Testing section above; the ASI mapping and extended
threat vocabulary remain navigational guidance, not extra approval gates.
