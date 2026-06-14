# Feature Flag Lifecycle

Durable rules for **creating, operating, and retiring feature flags** so progressive delivery is safe, observable, and free of technical debt.

Feature flags (also called feature toggles) allow code changes to ship to production decoupled from their activation. This enables trunk-based development (see `doctrine/principles/collaboration.md`), safe rollouts, and controlled experiments — but only if flags are governed as first-class engineering artefacts, not throwaway conditionals.

Flag evaluation SDKs and feature management platforms belong in `doctrine/tooling/`. This file holds the portable lifecycle and governance rules.

---

## 1. Flag Taxonomy

Every flag must be classified at creation. Classification drives ownership, default behaviour, and maximum permitted lifetime.

| Type | Purpose | Default | Owner | Max lifetime |
| --- | --- | --- | --- | --- |
| **Release** | Gate incomplete or risky code during rollout; decouple deploy from release | `off` | Engineering team | 4 weeks after GA |
| **Experiment** | A/B test or controlled rollout for learning; drives a metric decision | Varies by cohort | Product + Engineering | 8 weeks from activation |
| **Ops** | Runtime kill switch or circuit breaker; operational safety valve | `on` (safe state) | Ops / SRE | Indefinite while the risk exists; reviewed quarterly |
| **Permission** | Gate access to a feature by user role, plan, or tenant | `off` | Product + Platform | Aligned to entitlement model; reviewed annually |

**Why:** Conflating flag types causes wrong defaults (a release flag left `on` after GA is invisible debt; an ops kill switch defaulting `off` disables production). Named types make expectations explicit in code review.

---

## 2. Lifecycle State Machine

All flags progress through defined states. Flags that stagnate in any state past their time limit trigger automated cleanup reminders.

```
create ──► active ──► stabilize ──► cleanup ──► removed
              │                          ▲
              └── (experiment) ──────────┘
                   decision deadline
```

| State | Entry criteria | Exit criteria | Max time in state |
| --- | --- | --- | --- |
| **Active** | Flag created, targeting rules set, code deployed | Feature rolled out to 100% or decision made | Type-dependent (see §1) |
| **Stabilize** | Rollout complete; monitoring shows stable SLOs | Cleanup plan written and assigned | 1 week |
| **Cleanup** | PR opened to remove flag code and conditional branches | Flag removed from codebase and platform | 1 sprint |
| **Removed** | Code merged, flag deleted from flag store | — | — |

- Flags do **not** move backwards. If a rollout is reversed, the flag returns to `active` with a lower percentage — it does not revert to a previous lifecycle state.
- A flag in **stabilize** or **cleanup** must not have its targeting changed. If a new risk is discovered, create a new ops flag.

**Why:** Without a lifecycle state machine, "we'll clean it up later" never happens. The FSM creates explicit handoffs and sprint-sized cleanup tasks.

---

## 3. Progressive Delivery

Safe rollout patterns reduce blast radius and enable evidence-based promotion.

### 3.1 Percentage Rollout

Roll out to a random percentage of the target population by hashing a stable identifier (user id, session id, tenant id). Increase incrementally:

```
0% → 1% → 5% → 10% → 25% → 50% → 100%
```

- Minimum dwell at each tier: **one monitoring window** (typically 10–30 minutes for web services; 24 hours for high-stakes or infrequent operations).
- Define **promotion criteria** before starting: which SLI or metric must hold at tier N before advancing to tier N+1.

### 3.2 Ring Deployment

Target populations in priority order:

1. **Internal** (employees, synthetic test users)
2. **Beta / opt-in** (consenting early adopters)
3. **Canary** (small random production slice, e.g., 1–5%)
4. **General availability**

Rings are not percentages — they are identity-based targeting rules. Both can be active simultaneously (ring 3 at 5%).

### 3.3 Context Targeting

Evaluation context must carry stable, low-cardinality identifiers for targeting rules:

```json
{
  "user_id": "u-123",
  "tenant_id": "t-acme",
  "plan": "enterprise",
  "region": "eu-west-1",
  "app_version": "2.4.1"
}
```

- Do **not** pass raw UUIDs or request paths as targeting attributes — they produce non-deterministic targeting.
- Follow the [OpenFeature](https://openfeature.dev/) evaluation context schema for portability.

### 3.4 Metric Gates

Define which metric confirms the flag is safe to advance:

- **Primary metric:** the SLI the feature owns (e.g., `checkout_completion_rate`, `p99_latency_ms`).
- **Guard metrics:** SLIs the team does not own but could break (e.g., `error_rate`, `cart_session_duration`).
- Promotion is blocked if any guard metric degrades beyond the pre-defined tolerance (typically ±1–2 standard deviations from baseline over the monitoring window).

**Why:** Arbitrary promotion schedules produce rollout-induced incidents. Data-gated progression aligns with the Netflix chaos principle: understand what normal looks like before advancing.

---

## 4. Flag Debt And Cleanup

### 4.1 Age Thresholds

| Flag type | Stale threshold | Action |
| --- | --- | --- |
| Release | 4 weeks post-GA | Automated ticket to owning team |
| Experiment | 8 weeks from activation | Escalate if no decision recorded |
| Ops | Quarterly review | Owner confirms still needed or schedules removal |
| Permission | Annual entitlement review | Align with IAM/billing review cycle |

### 4.2 Automated Stale Detection

Run a daily CI job or scheduled script against the flag store:

- Query all flags with `status == active` and `updated_at < (now - max_lifetime)`.
- Open or update a tracking ticket in the issue tracker (one ticket per flag).
- Tag the flag with `stale` in the flag platform to warn evaluating teams.
- Do **not** automatically disable stale flags — only humans should change flag state.

### 4.3 Flag Debt Metrics

Report these in engineering health reviews:

- **Stale flag count** (age > threshold): target 0; alert at >10.
- **P90 flag age** at removal: target ≤ 2 weeks for release flags.
- **Flags with no recorded owner**: target 0.
- **Flags blocking a merge** (code behind flag, not compiled out): label explicitly so reviewers can assess risk.

**Why:** Flag debt is invisible until it causes an incident — either a forgotten kill switch that fires, or an experiment running for months and accidentally shaping user behaviour. Measurement makes debt visible.

---

## 5. Governance And Flag Metadata Schema

Every flag must carry this metadata at creation:

```json
{
  "key": "checkout-v2-rollout",
  "type": "release",
  "owner_email": "eng-checkout@example.com",
  "owner_team": "checkout",
  "created_date": "2024-11-01",
  "expiry_date": "2024-11-29",
  "jira_ticket": "CHECKOUT-4521",
  "description": "Rolls out the new checkout flow. Safe default: off. GA target: 2024-11-15.",
  "default_variation": "off"
}
```

Rules:

- `owner_email` and `owner_team` are **required** — no orphaned flags.
- `expiry_date` must be set for all release and experiment flags; ops flags set `null` with a reason.
- `description` must explain the **safe default state** so on-call can act without context.
- Flags without full metadata fail the PR check (contract violation — see `doctrine/principles/event-contracts.md` §1).
- Changes to `default_variation` on an active flag require a separate review with documented rationale.

**Why:** Flags are silent configuration. When something breaks at 3 AM, the on-call engineer needs to know what the flag does, who owns it, and what the safe state is — instantly.

---

## 6. Testing With Flags

- **Never test against production flag state.** Tests must explicitly set flag values via the SDK's testing API or environment-variable override.
- Unit tests must cover **both** flag variations for any code path touched by a flag.
- Integration and contract tests must parameterize the flag state, not assume it.
- If a flag controls a schema change or API contract, treat the flag-off and flag-on states as **separate contract versions** — validate both.
- Remove flag-variation tests at the same time as the flag code. Flag-specific tests left in place after removal are dead code.

**Why:** Tests that silently read production flag values produce non-deterministic CI — the same code can pass and fail depending on what is currently rolled out. Explicit override is a CI hygiene requirement.

---

## 7. AI And Model Version Flags

Flags are the correct mechanism to introduce new model versions, prompt templates, or embedding configurations without redeploying:

- Type: **ops** (for safety switches) or **experiment** (for quality comparisons).
- Target by tenant or user with explicit opt-in or gradual rollout — never roll out a model change at 100% on first deployment.
- Capture **model variant** in tracing context (correlation ID enriched with `model_version`, `prompt_template_version`) to isolate evaluation data — see `doctrine/principles/ai-ml-systems.md` §5.
- A/B comparison between model versions **requires a defined quality metric** before activation, not retrospective analysis.
- Rollback path: ops kill switch returning to previous model version must be documented and tested before GA.

**Why:** Model changes can degrade quality subtly across thousands of users before aggregates catch up. Progressive rollout with metric gates applies here even more than for UI changes.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Four named flag types with different lifetimes | Conflated types produce wrong defaults and unclear ownership. Naming types forces an explicit contract. |
| Lifecycle FSM with defined exit criteria | Without it, cleanup debt accumulates silently. The FSM makes cleanup a sprint-sized task with clear handoff. |
| Data-gated promotion, not calendar-gated | Calendar gates promote regardless of SLO stability; data gates catch regressions before they reach 100%. |
| Flag metadata as a required contract | On-call engineers need owner + safe default instantly. Missing metadata is a safety gap, not a convenience gap. |
| No automatic flag disablement | Silent state changes by automation are a safety incident waiting to happen. Humans change flag state; automation alerts. |
| Tests override flag state explicitly | Non-deterministic CI (tests inherit production state) undermines confidence in every CI run after that flag changes. |
| AI/model version flags as ops/experiment type | Model quality regressions are slow and invisible. Progressive rollout is as important here as for functional changes. |

---

## References

- Martin Fowler — **Feature Toggles (Feature Flags)**: https://martinfowler.com/articles/feature-toggles.html
- **OpenFeature** — vendor-neutral feature flag standard: https://openfeature.dev/
- LaunchDarkly — **Feature Flag Best Practices**: https://launchdarkly.com/blog/feature-flag-best-practices/
- Trunk-based development — **feature flags for incomplete work**: https://trunkbaseddevelopment.com/feature-flags/
- Honeycomb — **Flags and observability in progressive delivery**: https://www.honeycomb.io/blog/feature-flags-observability
