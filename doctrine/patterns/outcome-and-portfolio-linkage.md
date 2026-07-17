# Outcome And Portfolio Linkage

Use this optional overlay when software work is an intervention intended to change a stakeholder, customer, mission, risk, or business outcome, or when an external authority requires objective-to-measure traceability. It complements [AI-Native Software Development Lifecycle](ai-native-software-development-lifecycle.md); it is not a gate that every software change must pass.

Maintenance, vulnerability remediation, compatibility work, lifecycle replacement, operational risk reduction, and enabling work may instead use a simpler mandate that names the obligation, invariant, exposure, or future capability being preserved. Every change needs a defensible purpose and owner; not every change needs a KPI or causal product hypothesis.

---

## 1. Operating Chain

`stakeholder need → objective → outcome measures and guardrails → intervention hypothesis → bounded work → outputs → observed outcomes → continue, change, stop, or reverse`

AI may propose any link in this chain. Accountable governance accepts the objective, measure validity, priority, capacity, intervention, and portfolio decision. A measure does not authorise work, and completing an output does not prove an outcome.

| Record | Minimum content | Boundary |
| --- | --- | --- |
| **Objective** | Desired outcome; owner; scope; time horizon; non-goals. | A direction is not a task list. |
| **Measures and guardrails** | Baseline; target or acceptable range; observation window; population/unit; data source; owner; cadence; uncertainty and data-quality limits; countermetrics. | Measures test progress and harm; they are not the objective or authority. |
| **Intervention hypothesis** | Expected causal mechanism; assumptions; alternatives; dependencies; materiality; cost/capacity; review or kill date. | This is a testable bet, not a fact. |
| **Bounded work and outputs** | Tasks, governed executions where applicable, diffs, artefacts, experiments, deployments, or retired assets linked to the accepted intervention. | Activity and output volume are not value. |
| **Observed outcomes** | Measured change; guardrail effects; affected-party evidence; cost; risk; confidence; attribution limits and unintended effects. | Correlation does not silently become causation. |
| **Portfolio decision** | Continue, scale, change, stop, or reverse; owner; rationale; resource change; follow-up. | A missed target does not automatically generate more tasks. |

## 2. Activation

Apply the full overlay when at least one condition is true:

- work is funded or prioritised to change a product, customer, business, or mission outcome;
- several changes form one intervention whose value can only be assessed together;
- a material decision depends on attribution, countermetrics, or a continue/change/stop review; or
- law, contract, policy, funding governance, or another explicit authority requires the lineage.

Do not activate it merely because AI assisted the change. For non-strategic work, the mandate records the applicable justification class:

- external or standing obligation;
- vulnerability or incident response;
- compatibility or lifecycle maintenance;
- invariant preservation or operational risk reduction; or
- enabling work for an already authorised capability.

If an adopting organisation cannot explain why work belongs to one of these classes, it should not create the work merely because generation is cheap.

## 3. Measurement Contract

Use several measures with useful tension rather than a universal score. Select from outcome, delivery health, risk/quality, cost, and human impact as applicable.

Each material measure should declare:

- the question it helps answer;
- the population, unit, baseline, and target or acceptable range;
- the source/query, owner, cadence, and observation window;
- whether it is leading, lagging, diagnostic, or a guardrail;
- known uncertainty, missing data, confounders, and gaming risk; and
- what result would cause continuation, revision, stopping, or further investigation.

Delivery metrics diagnose the delivery system. They are not universal company objectives, individual productivity targets, or deterministic task generators; see [Measurement: Delivery Performance And DORA](../principles/measurement-and-dora.md).

## 4. Attribution And Shared Outcomes

One change rarely owns an outcome alone. Record concurrent interventions, external events, selection effects, and other plausible explanations. Prefer experiments where ethical and feasible; otherwise state the limits of observational evidence.

Many changes may close technically while one intervention remains under outcome review. Conversely, one change may affect several objectives; name the primary decision and material guardrails rather than claiming exact allocation without evidence.

The outcome record may be held in a product, risk, finance, service-management, or other governed system. Link it to the software-change records; do not duplicate sensitive data merely to centralise the ontology.

## 5. Closure

This overlay uses the lifecycle's three closure modes:

1. **Technical closure** — the authorised candidate was enacted and its immediate technical claims were evaluated.
2. **Operational closure** — behaviour remained within declared guardrails for the relevant observation window.
3. **Outcome review** — aggregate evidence is sufficient for the accountable owner to continue, change, stop, or reverse the intervention.

A software issue may close technically while retaining links to an operational observation or longer outcome review. Outcome review must not keep routine change records artificially open for months.

## 6. Failure Modes

- Compiling a KPI directly into tasks without a causal hypothesis, alternatives, guardrails, capacity decision, or kill criterion.
- Treating “launch”, “deploy”, task count, code volume, or generated artefact volume as a key result.
- Letting an agent create its own objective, approve its measure, fund its intervention, and declare its output successful.
- Using a single metric for a complex system or comparing unlike services and populations.
- Translating correlation into causal certainty or omitting material confounders.
- Creating unlimited initiatives because AI reduces the cost of producing candidate work while review, operation, and maintenance remain scarce.
- Requiring product-portfolio ceremony for a bounded maintenance, obligation, or incident change whose mandate is already explicit.

## 7. Measures

Review this overlay using observable decision quality rather than document completion:

- interventions stopped or changed when evidence falsifies their assumptions;
- generated-to-accepted work ratio and abandoned artefact load;
- guardrail breaches and unintended effects detected;
- outcome reviews with explicit attribution limits;
- reviewer effort required to find purpose, owner, and decision; and
- maintenance or obligation changes incorrectly forced into strategic measurement.

## Related

- [AI-Native Software Development Lifecycle](ai-native-software-development-lifecycle.md)
- [AI And ML-Assisted Systems](../principles/ai-ml-systems.md)
- [Measurement: Delivery Performance And DORA](../principles/measurement-and-dora.md)
- [AI-Native SDLC Readiness Checklist](../checklists/ai-native-sdlc-readiness.md)

## References

- **NIST AI RMF 1.0 Core** — Govern, Map, Measure, and Manage functions; organisational mission, goals, context, risks, benefits, and measures: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
- **GQM+Strategies** — links organisational goals and strategies to software goals and measurement: https://arxiv.org/abs/1402.0292
- **Goal/Question/Metric** — derives measurement from explicit goals and questions: https://drum.lib.umd.edu/items/8119803a-362b-42ec-b6ce-2311713e7236
- **COBIT 2019 goals cascade** — translates enterprise goals into alignment-goal priorities and uses enterprise goals to prioritise governance and management objectives: https://www.isaca.org/resources/news-and-trends/industry-news/2019/employing-cobit-2019-for-enterprise-governance-strategy
- **DORA metrics guidance** — delivery metrics are contextual and should not become goals or individual comparisons: https://dora.dev/guides/dora-metrics/
