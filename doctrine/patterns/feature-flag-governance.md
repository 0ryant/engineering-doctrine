# Feature Flag Governance

Canonical home for the portable rules on creating, operating, reverting, and retiring feature flags. It supersedes `feature-flag-lifecycle.md`; see §10 for migration.

Flags decouple deploying code from activating it, which is what lets incomplete work land on trunk ([trunk-workflow.md](trunk-workflow.md); [principles/collaboration.md](../principles/collaboration.md) §4) and lets risky changes reach users gradually. That holds only when flags are governed as artefacts with owners, safe defaults, and removal dates.

Flag SDKs, feature-management platforms, and rollout controllers are tooling choices and belong in `doctrine/tooling/`; this file names none.

---

## 1. Applicability

- Baseline: every claim below applies to any repository that evaluates a flag at runtime, whatever the flag store.
- Stricter only under a named profile. Regulated-data: every targeting change and state transition MUST be audit-logged with actor, time, and reason ([principles/audit-logging.md](../principles/audit-logging.md)). Person-affected: the metric gates in §4.3 MUST include the harm-surface evaluation in [principles/ai-ml-systems.md](../principles/ai-ml-systems.md) §6, and the minimum dwell per tier is 24 hours.
- Numeric values are estate-tunable defaults. An estate MAY change one by recording the value and reason in its own doctrine; that is not an exception under [normative-language-applicability-and-exceptions.md](normative-language-applicability-and-exceptions.md) §5.

---

## 2. Flag Taxonomy

Every flag MUST be classified at creation. The type fixes safe default, owner, and maximum lifetime.

| Type | Purpose | Safe default | Owner | Maximum lifetime (default) |
| --- | --- | --- | --- | --- |
| Release | Gate incomplete or risky code; decouple deploy from release | `off` | Engineering team | 4 weeks after general availability (GA) |
| Experiment | Controlled comparison driving a recorded metric decision | Varies by cohort | Product and engineering | 8 weeks from activation |
| Ops | Kill switch or circuit breaker | `on` (the safe state) | Operations or SRE | Indefinite while the risk exists; reviewed quarterly |
| Permission | Gate access by role, plan, or tenant | `off` | Product and platform | Aligned to the entitlement model; reviewed annually |

Prevents: a release flag left `on` after GA (invisible debt); an ops switch defaulting `off` (production disabled). Evidence: the flag store reports a type and derived lifetime for every flag.

---

## 3. Lifecycle State Machine

### 3.1 States And Clocks

| State | Meaning | Maximum time in state (default) |
| --- | --- | --- |
| `defined` | Registered with complete metadata (§6); no production targeting | Until first deploy |
| `active` | Targeting serves traffic; promotion or experiment in progress | Type lifetime (§2) |
| `stabilize` | At 100% or decision recorded; monitoring confirms SLOs | 1 week |
| `cleanup` | Removal change opened; targeting frozen | 1 sprint |
| `removed` | Code merged, flag deleted from the store; terminal | none |

Two clocks run. The state clock bounds time in the current state. The lifetime clock is the §2 lifetime, anchored at GA for release flags and at activation for experiment flags. Stale detection (§5.2) reads both.

```text
defined --> active --> stabilize --> cleanup --> removed
              ^           |            |
              |-----------+            |   reversal (recorded reason)
              |------------------------+   incident-directed only
```

### 3.2 Legal Transitions

| From | To | Trigger | Guard | Clocks |
| --- | --- | --- | --- | --- |
| `defined` | `active` | First production targeting rule enabled | Metadata complete; promotion criteria (§4.3) recorded for release and experiment flags | Experiment lifetime starts; release lifetime armed until GA |
| `active` | `stabilize` | 100% reached, or experiment decision recorded | Guard metrics held one monitoring window at the final tier | Stabilize clock starts; release lifetime anchors at this GA date |
| `stabilize` | `cleanup` | Cleanup plan assigned; removal change opened | Stabilize clock not exceeded | Cleanup clock starts |
| `cleanup` | `removed` | Removal change merged; flag deleted from the store | Flag-variation tests removed in the same change (§7) | All clocks stop |
| `stabilize` | `active` | Reversal decided by the owner or an incident commander | Reason and `tracker_ref` recorded; targeting set to the safe default or a lower tier | Stabilize clock discarded; GA anchor cleared; re-promotion sets a new GA and restarts the stabilize clock |
| `cleanup` | `active` | Incident-directed rollback | Incident record cites the flag; removal change not yet merged | Cleanup clock discarded; re-promotion as above |
| `active` | `cleanup` | Ops or permission flag retired | Quarterly or annual review records the decision | Cleanup clock starts |

Rules:

- Every state transition MUST be performed or explicitly authorised by a human and recorded with actor and reason. Automation MUST NOT move a flag between states.
- Targeting changes inside `active` are ordinary operations; automation MAY make one only in the bounded case in §4.4.
- Targeting in `stabilize` MUST NOT change except through the reversal transition. A partial reduction not recorded as a reversal is illegal.
- Targeting in `cleanup` MUST NOT change except through the incident-directed transition.
- A second reversal of the same flag SHOULD escalate to the owning team's lead for a redesign-or-re-promote decision. Reversals MUST NOT extend a flag's life indefinitely; total age since creation stays reported (§5.3).
- Once the removal change has merged, recovery is a deployment rollback under [principles/reliability-slo-incidents.md](../principles/reliability-slo-incidents.md), not a flag transition.

### 3.3 Illegal Transitions

`removed` to anything (create a new flag); `defined` to `stabilize` or `cleanup` (a never-activated flag is deleted); `active` or `stabilize` to `removed` (cleanup is where tests and dead branches go); `cleanup` to `stabilize` (a returning flag goes to `active`); `cleanup` to `active` without an incident record.

Prevents: an operator who must undo a promoted rollout being unable to comply. Evidence: the transition log shows a reason for every backward move and no automated transitions.

---

## 4. Progressive Delivery

### 4.1 Percentage Tiers And Rings

Release flags SHOULD roll out by hashing a stable identifier (user, session, or tenant id) through default tiers `0% -> 1% -> 5% -> 10% -> 25% -> 50% -> 100%`. Minimum dwell per tier is one monitoring window: 10 to 30 minutes for web services; 24 hours for high-stakes or infrequent operations.

Rings are identity-based targeting and MAY combine with percentages. Default order: internal (employees, synthetic users); beta or opt-in; canary (1 to 5% random production slice); GA.

### 4.2 Context Targeting

Evaluation context MUST carry stable, low-cardinality attributes (user id, tenant id, plan, region, application version). Raw request paths or per-request identifiers MUST NOT be targeting attributes; they make targeting non-deterministic. The vendor-neutral OpenFeature evaluation-context shape is the SHOULD default for portability.

### 4.3 Metric Gates

Before the first tier the owner MUST record a primary metric (the SLI the feature owns) and guard metrics (SLIs it could break but does not own). Promotion MUST NOT proceed while a guard metric degrades beyond its recorded tolerance; the default tolerance is 1 to 2 standard deviations from baseline over the monitoring window. Calendar-only promotion is not conformant.

### 4.4 Automated Reversion To The Safe Default

- An ops flag MAY be tripped to its safe default by automation when the trip condition, safe default, and alert are recorded on the flag and the trip was tested before GA. The trip is a targeting change inside `active`, not a state transition.
- Automated reversion of a release or experiment flag to its safe default inside `active` on a guard-metric breach is CONTEXT-DEPENDENT: permitted only under the same pre-declaration and pre-test conditions, and only to the safe default. Every forward change and every state transition remains human.

Prevents: schedule-driven promotion shipping regressions to 100%; a kill switch only a human can pull becoming its own reliability risk. Evidence: promotion records cite metric values per tier; trip conditions are visible on the flag before GA.

---

## 5. Flag Debt And Cleanup

### 5.1 Stale Thresholds

| Type | Stale when | Default action |
| --- | --- | --- |
| Release | 4 weeks after GA | Work item opened for the owning team |
| Experiment | 8 weeks from activation | Escalate if no decision is recorded |
| Ops | Quarterly review missed | Owner confirms need or schedules retirement |
| Permission | Annual review missed | Align with the access and billing review cycle |

### 5.2 Stale Detection

A scheduled check (daily by default) SHOULD compare every flag's clocks against §3 and §5.1, open or update one work item per stale flag, and mark the flag stale where evaluating teams can see it. It MUST NOT change targeting or state.

### 5.3 Debt Measures

Report in engineering health reviews: stale flag count (target 0; alert above 10); P90 age at removal measured from GA for release flags (target 2 weeks or less); flags with no recorded owner (target 0); total age of any flag that has reversed; and code behind a flag that is compiled in, labelled so reviewers can assess risk.

Prevents: forgotten kill switches firing; experiments shaping behaviour for months. Evidence: the measures appear in the review record.

---

## 6. Metadata Contract

Every flag MUST carry: a stable key; type; owning team and a reachable owner contact; created date; expiry date (required for release and experiment flags; `null` with a recorded reason for ops and permission flags); a `tracker_ref` to the introducing work item; a description stating the safe default so on-call can act without context; and the default variation. A change introducing a flag without complete metadata MUST NOT merge. Changing the default variation of an `active` flag MUST be reviewed separately with a recorded rationale.

EXAMPLE shape (the semantic list above is the contract; field names other than `tracker_ref` are illustrative):

```json
{
  "key": "checkout-v2-rollout",
  "type": "release",
  "owner_team": "checkout",
  "owner_contact": "eng-checkout@example.com",
  "created_date": "2024-11-01",
  "expiry_date": "2024-11-29",
  "tracker_ref": "CHECKOUT-4521",
  "description": "Rolls out the new checkout flow. Safe default: off. GA target: 2024-11-15.",
  "default_variation": "off"
}
```

Prevents: on-call unable to tell what a flag does, who owns it, or which way is safe. Evidence: the merge check rejects an incomplete definition.

---

## 7. Testing With Flags

- Tests MUST set flag values through an explicit override and MUST NOT read production flag state.
- Unit tests MUST cover both variations of any flagged path; integration and contract tests MUST parameterise flag state.
- When a flag controls a schema or API contract, the two variations MUST be validated as separate contract versions ([principles/event-contracts.md](../principles/event-contracts.md) §1).
- Flag-variation tests MUST be removed in the same change as the flag code.

Prevents: CI whose result depends on what is currently rolled out. Evidence: no test fixture resolves a flag from a live store.

---

## 8. Model And Prompt Version Flags

Flags are the default mechanism for introducing a model version, prompt template, or embedding configuration without a redeploy.

- Type MUST be ops (safety switch) or experiment (quality comparison).
- A model change MUST NOT reach 100% on first deployment; roll out by tenant or user with opt-in or tiers.
- Model and prompt versions MUST be present in tracing and audit context so evaluation data isolates by variant ([principles/ai-ml-systems.md](../principles/ai-ml-systems.md) §5).
- A comparison MUST have its quality metric recorded before activation.
- The ops switch back to the previous version MUST be tested before GA.

Prevents: quality regressions accumulating across users before aggregates catch up.

---

## 9. Failure Modes

| Failure | Guard |
| --- | --- |
| Promoted rollout must be reversed but the rules forbid every move | Reversal and incident-directed transitions with recorded reasons (§3.2) |
| Repeated reversals used to dodge retirement | Second-reversal escalation; total age reported (§3.2, §5.3) |
| Ops switch cannot trip because all changes are human | Trip is a pre-declared targeting change inside `active` (§4.4) |
| Automation reverts a flag and nobody notices | Alert is part of the pre-declaration; state transitions stay human (§4.4) |
| Promotion on schedule regardless of SLOs | Metric gates recorded before tier 1 (§4.3) |
| Stale flags accumulate unseen | Daily detection, one work item per flag, debt measures (§5) |
| Orphaned flag at incident time | Owner and safe default in the metadata contract; merge check (§6) |
| Removal merged, then rollback wanted | Deployment rollback, not a flag transition (§3.2) |

---

## 10. Consumer Impact

Change class: normative replacement. This file replaces `feature-flag-lifecycle.md` as the canonical home; the old file follows the supersession mechanics in [doctrine-content-lifecycle.md](doctrine-content-lifecycle.md).

Migration note: repoint links to this path. Old §1 (taxonomy) is §2 here; old §2 (state machine) is §3; old §3 (progressive delivery) is §4, with automated reversion added as §4.4; old §4 (debt) is §5; old §5 (metadata) is §6, with the tracker-specific field renamed `tracker_ref` and `owner_email` renamed `owner_contact`; old §6 (testing) is §7; old §7 (AI flags) is §8. Every claim is now typed; consumers who relied on the old imperative wording should confirm which claims bind them under §1. No numeric default changed.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Types and lifetimes carried over unchanged | The numerics were never the defect; the untyped, self-contradictory reversal rules were. |
| Explicit `defined` state | The old "Active" entry criteria implied a pre-active state without naming it. |
| Reversal discards the state clock, re-anchors GA, keeps total age | The new rollout deserves its full stabilize window; letting reversals reset the lifetime clock would make a flag immortal. Second-reversal escalation closes that gap without a new numeric. |
| Freeze scoped to `stabilize` and `cleanup` with named escapes | A universal no-backwards rule made post-promotion rollback non-compliant. Reversal from `stabilize` and incident-directed return from `cleanup` are the two backward moves the machine needs. |
| Position on bounded automated reversion | An earlier proposal that pre-declared, tested, metric-gated reversion to the safe default may auto-execute was never adopted into doctrine. This file adopts it in bounded form: ops-flag tripping is baseline (the type is defined as a circuit breaker, so a humans-only rule contradicted the taxonomy); release and experiment auto-reversion inside `active` is CONTEXT-DEPENDENT under the same pre-declaration; automation never performs a state transition or a forward change. Estates that reject the carve-out stay conformant by pre-declaring no trip. |
| P90 age at removal measured from GA | Measured from creation, the 2-week target cannot be met once stabilize and cleanup are counted; anchoring at GA keeps it consistent with the 4-week lifetime. Clarification, not a change. |
| Neutral `tracker_ref`; JSON marked EXAMPLE | A vendor field inside a merge-gating contract is a portability leak; the semantic list is the contract. |
| Numerics are tunable defaults, not exceptions | Routing a dwell-time tweak through the exception contract would teach teams to ignore the contract. |

---

## Related

- [trunk-workflow.md](trunk-workflow.md) — flags as the mechanism for feature work that does not block trunk
- [principles/collaboration.md](../principles/collaboration.md) §4 — flag ownership and server-side kill switches
- [code-review-and-change-approval.md](code-review-and-change-approval.md) — flags and rollout risk as review topics
- [principles/state-machines-and-workflows.md](../principles/state-machines-and-workflows.md) — explicit states and guarded transitions
- [principles/reliability-slo-incidents.md](../principles/reliability-slo-incidents.md) — incident direction and rollback
- [doctrine-content-lifecycle.md](doctrine-content-lifecycle.md) — supersession mechanics for the predecessor file

---

## References

Carried over from the superseded file (link health checked 2026-09-03, [sweep-2026-09.md](../evolution/sweep-2026-09.md) §3):

- Martin Fowler — Feature Toggles (Feature Flags): https://martinfowler.com/articles/feature-toggles.html (S6, accessed 2026-09-03)
- OpenFeature — vendor-neutral feature flag standard: https://openfeature.dev/ (S4, accessed 2026-09-03)
- Trunk-based development — feature flags for incomplete work: https://trunkbaseddevelopment.com/feature-flags/ (S6, accessed 2026-09-03)

Two further citations in the superseded file (a vendor best-practices post and an observability vendor post) returned 404 at supersession and supported illustrative text only; they were not carried. The superseded file keeps them untouched, as the lifecycle pattern requires.
