# Research: A Doctrine-Grounded AI-Native Software Development Lifecycle (July 2026)

**Purpose:** Evaluate proposed AI-native software delivery controls against this library and current primary sources, distinguish external support from library synthesis, and record why the operational model uses evidence-backed gates and records rather than a vendor workflow or autonomous release path.

**Decision records:** [ADR 0024](../../docs/adr/0024-adopt-a-doctrine-grounded-ai-native-software-development-lifecycle.md), as amended by [ADR 0030](../../docs/adr/0030-refine-ai-native-sdlc-into-gates-records-and-applicability-overlays.md).
**Normative landing:** [AI-Native Software Development Lifecycle](../patterns/ai-native-software-development-lifecycle.md).
**Review surface:** [AI-Native SDLC Readiness Checklist](../checklists/ai-native-sdlc-readiness.md).

---

## 1. Trigger, Provenance, And Source Limits

Initial working material proposed an eleven-state lifecycle, transition-admissibility fields, authority roles, evidence classes, materiality tiers, adoption stages, and measures. A later external review challenged its operational complexity, mandatory strategy linkage, universal run-contract wording, deterministic-control language, verifier-independence model, source-of-truth boundary, closure model, and multi-agent coordination detail. Both inputs are non-binding review evidence: portable doctrine claims below are retained only where they can be grounded in retrievable external sources or are clearly labelled as this library's synthesis.

Those materials are **proposal and review evidence**, not doctrine authority. They provide neither cross-organisation comparative evidence nor a validated transition schema. Their vendor sources show product direction and practitioner hypotheses; they do not prove that the proposed lifecycle improves safety, quality, or flow.

## 2. Existing Doctrine Baseline

The proposal does not replace this library's existing control model. The following were already authoritative:

| Concern | Existing doctrine | Constraint on the lifecycle |
| --- | --- | --- |
| Source of truth | [single-source-of-truth.md](../principles/single-source-of-truth.md), [ai-ml-systems.md](../principles/ai-ml-systems.md) §1 | Authoritative, versioned records govern the surfaces they own; chat/model state does not. Repository state is preferred where executable intent can be represented as code, but operational authority may be federated. |
| Build and promotion | [build.md](../principles/build.md) | Explicit, reproducible build surfaces; promote the same immutable artefact. |
| Merge-path authority | [merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md), [code-review-and-change-approval.md](../patterns/code-review-and-change-approval.md) | Binding CI, protected branches, authenticatable/scoped/retrievable evidence, accountable approval. |
| Agent execution | [run-contracts.md](../patterns/run-contracts.md) | Every **governed execution** compiles to a run contract. Incidental, ephemeral, fully inspected assistance does not gain agent authority merely because a model was used; output entering delivery still follows normal candidate controls. |
| Agent verification | [verifier-packs.md](../patterns/verifier-packs.md) | Every skill has a bounded verifier mirror; `pass`, `fail_loud`, `mark_untrusted`, `inconclusive`; no silent skip. |
| AI risk | [ai-ml-systems.md](../principles/ai-ml-systems.md), [ai-adoption-controls.md](../patterns/ai-adoption-controls.md) | Capability and materiality are separate axes; higher-impact action receives stronger oversight, testing, and runtime control. |
| Secure lifecycle | [secure-development-lifecycle.md](../principles/secure-development-lifecycle.md), [testing-strategy.md](../principles/testing-strategy.md) | Security is prepared, protected, produced, and responded to throughout the lifecycle; risk-based testing remains mandatory. |
| Runtime accountability | [reliability-slo-incidents.md](../principles/reliability-slo-incidents.md), [measurement-and-dora.md](../principles/measurement-and-dora.md) | Enactment is not success; SLO, incident, change-failure, and flow evidence close the loop. |

## 3. Primary And Authoritative External Grounding

Verified again 2026-07-17. These sources support parts of the control model; none mandates this library's seven gates, five record families, S0-S10 crosswalk, run-contract activation rule, claim taxonomy, or closure modes.

| Source | Class | What it supports | Boundary / non-claim |
| --- | --- | --- | --- |
| **NIST SP 800-218, SSDF 1.1** | External guidance | A risk-based secure development framework spanning Prepare, Protect, Produce, and Respond; its high-level practices integrate into each SDLC implementation. | It is an outcome/practice framework, not this transition model. [NIST](https://csrc.nist.gov/pubs/sp/800/218/final) |
| **NIST SP 800-218A** | External guidance | AI model producers, AI-system producers, and acquirers apply AI-specific secure practices throughout the SDLC in conjunction with SSDF 1.1. | It does not prescribe agent authority, gates, records, or run contracts. [NIST](https://csrc.nist.gov/pubs/sp/800/218/a/final) |
| **NCSC/CISA et al., Guidelines for Secure AI System Development** | External guidance | Secure design, development, deployment, and operation/maintenance across the AI-system lifecycle, including responsible release and runtime monitoring. | It does not prove that a particular agentic process or state model is effective. [NCSC](https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development/guidelines) |
| **ISO/IEC 5338:2023** | External standard | Defines processes supporting the definition, control, management, execution, and improvement of AI systems over their lifecycle, based on established system/software lifecycle foundations and usable within an organisation or project. | The full normative text is paywalled; this review relies on ISO's official abstract and does not infer clauses. [ISO](https://www.iso.org/standard/81118.html) |
| **NIST AI RMF 1.0** | External guidance | GOVERN is cross-cutting; MAP, MEASURE, and MANAGE are continuous, iterative, context-tailored functions. Organisational mission, goals, value, risk tolerance, benefits, costs, and supported tasks are relevant when governing an AI system. | The voluntary functions are not an ordered release checklist, a universal company strategy method, or support for mandatory KPI lineage on every software change. [NIST AIRC](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) |
| **COBIT 2019 goals cascade** | External governance guidance | Translates enterprise goals into alignment-goal priorities and uses enterprise goals to prioritise governance and management objectives. | It supports contextual strategic lineage when that context applies, not automatic compilation from stakeholder needs into software tasks. [ISACA](https://www.isaca.org/resources/news-and-trends/industry-news/2019/employing-cobit-2019-for-enterprise-governance-strategy) |
| **GQM and GQM+Strategies** | External measurement method | Derives questions and measures from explicit goals and can link business strategies to operational software goals and measurement. | It does not prove that a selected intervention caused an observed outcome or require product-style measurement for maintenance work. [GQM+Strategies](https://arxiv.org/abs/1402.0292), [UMD GQM report](https://drum.lib.umd.edu/items/8119803a-362b-42ec-b6ce-2311713e7236) |
| **DORA software delivery metrics** | External practitioner research/guidance | Measures delivery-process outcomes using throughput and instability signals, with contextual leading/lagging interpretation; warns against goals built from the metric, single-metric reduction, and unlike comparisons. | DORA metrics diagnose delivery-system health; they are not enterprise objectives, individual targets, or proof of product impact. [DORA](https://dora.dev/guides/dora-metrics/) |
| **SLSA v1.2** | External specification | Provenance is verifiable information describing where, when, and how an artefact was produced; build and source tracks support candidate identity and supply-chain reconstruction. | Provenance does not establish semantic correctness, policy authority, or business approval. [SLSA](https://slsa.dev/spec/v1.2/provenance) |
| **EU AI Act, Regulation (EU) 2024/1689** | External legal requirement where applicable | For in-scope high-risk AI: lifecycle risk management, human oversight including override/stop, accuracy/robustness/cybersecurity, and post-market monitoring. | Applicability is use-case- and jurisdiction-specific. The doctrine uses these provisions as rationale, not as a claim that every consumer is regulated. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) |

### Version Honesty

NIST published an Initial Public Draft of SP 800-218 Revision 1 (SSDF 1.2) in December 2025. This research does not silently promote a draft to final authority: SSDF 1.1 and its final AI community profile SP 800-218A remain the cited final baseline. [NIST project page](https://csrc.nist.gov/projects/ssdf)

## 4. Vendor And Practitioner Observations

Vendor material is useful for landscape awareness and implementation ideas, not as normative authority or independent effectiveness evidence. The linked public surfaces were re-reviewed on 2026-07-17.

| Observation | Useful signal | Limit |
| --- | --- | --- |
| **AWS AI-DLC** describes a repeated plan → clarify → human-validate → implement loop across inception, construction, and operations. It persists requirements, plans, and designs in the repository, concentrates humans on critical decisions, and proposes short collaborative work cycles. | Durable intent, explicit clarification before execution, and rapid human decision points are stronger than a one-shot prompt. Repository persistence aligns with the doctrine source-of-truth boundary. | The assertion that AI-assisted and autonomous approaches are suboptimal, the quality/velocity benefits, and the renamed rituals are vendor claims. “Mob” collaboration and “bolts” are optional team practices, not portable controls. [AWS](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/) |
| **Microsoft AI-led SDLC** demonstrates spec-first decomposition into tasks, a coding agent working on a branch/PR, agent-assisted review, an isolated preview environment, configured CI/CD promotion, and an SRE agent opening a new issue from runtime evidence. It also exposes agent actions and workflow runs for inspection. | This gives concrete examples of durable specification/work handoffs, supports treating executable candidates as untrusted until isolated evaluation, illustrates bounded non-model enactment, and shows runtime observations feeding new work. Action receipts are useful evidence. | A weather-dashboard demonstration does not establish safety or scalability for material systems. Product-specific components, reported third-party review statistics, and visibility into purported model “thinking” are not portable proof; doctrine records observable actions and outcomes, not private chain-of-thought. [Microsoft](https://techcommunity.microsoft.com/blog/appsonazureblog/an-ai-led-sdlc-building-an-end-to-end-agentic-software-development-lifecycle-wit/4491896) |
| **GitHub Spec Kit** evolves specification, plan, tasks, and implementation with flow-back when discovery changes upstream artefacts. | Specs are living, versioned records; material change must invalidate and rebind derived work. | A specification is not verification, approval, or runtime evidence. [GitHub](https://github.github.com/spec-kit/guides/evolving-specs.html) |
| **Google OKR playbook** distinguishes objectives from measurable key results, rejects activity-only KRs and “launch X” without user/economic benefit, and requires credible evidence. | Supports outcome-oriented goals and cross-team commitments rather than task-count scorecards. | Reprinted practitioner guidance, not a standard; OKR vocabulary and scoring are optional. [What Matters, reprinted with Google permission](https://www.whatmatters.com/resources/google-okr-playbook) |
| **Anthropic 2026 Agentic Coding Trends Report landing page** identifies shifting engineering roles, multi-agent coordination, human–AI collaboration, scaling agentic coding beyond engineering, and the continuing need for active human judgment. | Multi-agent lineage, explicit coordination, human-attention measures, and equal software controls regardless of the originator are credible design pressures. | The public page is vendor-authored and exposes headline topics, not the full report evidence without a gated submission. It is not a portable governance standard, audited comparison, or support for body-only numeric claims. [Anthropic](https://resources.anthropic.com/2026-agentic-coding-trends-report) |

### Vendor Decision Pass

| Finding | Decision | Doctrine landing or reason |
| --- | --- | --- |
| Persist intent, claims, plans, and clarifications in identified, versioned records; flow material changes back through derived work. | **Take as portable capability** | Repository records are preferred when the surface is representable as code. The authoritative record may be federated, but ownership, version, links, and reconciliation stay explicit. |
| Compile multi-agent work into explicit parent/child scopes, dependencies, owned workspaces, handoffs, and integration responsibility. | **Take as library synthesis** | Coordination invariants govern multi-agent work; vendor diagrams do not define the authority model. Every governed child execution remains separately bounded. |
| Make long-running work checkpointable, expiring, cancellable, and safely resumable. | **Take as library synthesis** | Resume revalidates inputs, policy, identity, and authority. The current sources show the pressure for long-running coordination but do not validate one checkpoint protocol. |
| Execute agent-produced code in an isolated preview/test environment before promotion. | **Take as externally aligned control** | Secure lifecycle guidance supports protected development/deployment; vendor demonstrations illustrate isolation. Isolation does not replace discriminating tests, review, or promotion of the authorised artefact. |
| Observe agent actions, tool calls, outputs, and workflow receipts. | **Take with privacy boundary** | These are evidence; private chain-of-thought is neither required nor treated as proof. Prompt/secret retention remains minimised. |
| Let operational agents turn runtime signals into new work. | **Take with authority boundary** | An agent may propose a new mandate and remediation; it may not detect, implement, approve, and enact its own change as one closed loop. |
| Focus scarce human attention on novelty, ambiguity, material impact, and exceptions. | **Take as calibrated routing** | Existing capability × materiality gates remain authoritative. Automated review can prioritise attention but cannot remove accountable approval for high-risk change or make the producer its sole challenger. |
| Allow domain experts and non-engineers to create executable tools with agents. | **Take under the same controls** | Originator job title does not waive ownership, inventory, repository, privacy, security, review, operability, or retirement obligations. |
| Treat output volume and speed as evidence of success. | **Investigate, do not adopt** | Adoption measures include accepted outcomes, human attention, abandoned artefacts, induced backlog, quality, and runtime results. Vendor numeric claims are not baselines. |
| Adopt vendor product stacks, AWS ritual names, a one-prompt-to-production flow, or autonomous closed-loop remediation. | **Reject as doctrine** | These either belong in an estate ADR or violate the evidence and authority model. |

## 5. External Review Decision Ledger

The second review correctly identified that the first synthesis fused agent execution, software change control, and product/portfolio governance. The useful kernel is retained:

> Intent is not implementation. Implementation is not evidence. Evidence is not authority. Authority is not enactment. Enactment is not outcome.

The following pass separates source support from design decisions:

| Topic | Decision | Classification and basis |
| --- | --- | --- |
| Seven operational gates | **Take** | **Library synthesis.** SSDF, NCSC, AI RMF, and SLSA support lifecycle-wide practices and traceable evidence, but no source validates seven gates. Seven is chosen instead of the review's six so challenge and authorisation remain separate. |
| S0-S10 | **Retain as reference crosswalk** | **Library synthesis.** The eleven states remain useful for diagnosis and invalidation, but no cited source validates them as mandatory workflow statuses. |
| Five record families | **Take** | **Library synthesis aligned with external guidance.** SLSA supports provenance, SSDF/NCSC support lifecycle records, and AI RMF supports documentation and accountability; the five-family grouping is this library's composition. |
| Governed-execution activation | **Take** | **Library synthesis.** External guidance supports proportional, risk-based controls; the exact activation conditions and run-contract envelope are not externally mandated. |
| Typed claims | **Take** | **Library synthesis aligned with evidence methods.** Structural, functional, quantitative, compatibility, safety, operational, and causal claims require different falsification surfaces; no source prescribes this exact taxonomy. |
| Evidence diversity by failure mode | **Take** | **Library synthesis.** Deterministic tests, independent review, policy checks, adversarial evaluation, and runtime observation can fail differently. Actor or model count alone is not a valid independence measure. |
| Bounded control execution | **Take; replace strict determinism** | **External alignment plus synthesis.** SLSA supports reconstructable provenance; SSDF and NCSC support controlled lifecycle mechanisms. Final authority must use configured, bounded, inspectable, reconstructable controls rather than open-ended model discretion. Statistical inputs do not invalidate that boundary. |
| Federated systems of record | **Take** | **Library synthesis.** Identified, versioned records remain authoritative for the surfaces they own. Repository state is preferred when representable as code; external state is linked and reconciled. |
| Three closure modes | **Take** | **Library synthesis aligned with lifecycle monitoring.** NCSC and AI RMF support operation and monitoring, but do not prescribe technical, operational, and outcome closure. |
| Objective-to-outcome linkage | **Take as optional overlay** | **External guidance in strategic contexts.** COBIT, GQM+Strategies, AI RMF, and DORA support goal-oriented, contextual measurement. They do not require a KPI or causal product hypothesis for every maintenance, vulnerability, compatibility, migration, risk-reduction, or enabling change. |
| Multi-agent coordination invariants | **Take** | **Library synthesis; vendor pressure signal only.** Vendor sources show multi-agent coordination as a growing concern but do not establish one safe protocol. |
| One central lifecycle platform or universal schema | **Defer / reject as prerequisite** | Existing linked records can satisfy the control model. Standardisation needs interoperability and consumer evidence; platform centralisation is not a doctrine obligation. |
| Vendor productivity figures, ritual names, and product stacks | **Reject as doctrine; investigate locally** | Vendor observation only. These claims do not establish comparative effectiveness or portable controls. |

## 6. Adopted Synthesis

### Seven Operational Gates

1. **Admit mandate** — establish justification class, owner, materiality, scope, and non-goals.
2. **Specify claims** — state what must be true and what evidence could discriminate it.
3. **Bound governed execution** — apply a run contract when model/agent authority, persistence, data, delegation, cost, scope, or uninspected reliance crosses the activation boundary.
4. **Produce candidate** — create an addressable change and disclose limitations.
5. **Challenge candidate** — gather claim-appropriate evidence with sufficiently different failure modes.
6. **Authorise transition** — policy and accountable people decide for the exact candidate.
7. **Enact, observe, and close** — promote the authorised candidate, emit receipts, evaluate runtime claims, and select the appropriate closure mode.

The detailed state crosswalk remains:

| Operational gate | Reference states |
| --- | --- |
| Admit mandate | S0 observed need; S1 intent registered |
| Specify claims | S2 claims specified |
| Bound governed execution | S3 transition designed; S4 work compiled |
| Produce candidate | S5 candidate produced |
| Challenge candidate | S6 candidate challenged |
| Authorise transition | S7 transition authorised |
| Enact, observe, and close | S8 transition enacted; S9 runtime evaluated; S10 reconciled |

### Five Record Families

1. **Mandate** — justification class, owner, materiality, scope, non-goals, and optional strategic linkage.
2. **Governed execution** — authority envelope, inputs, allowed tools/data, outputs, limits, delegation, stop/escalation conditions, and receipts.
3. **Candidate claim set** — immutable candidate identity, typed claims, limitations, affected surfaces, and required evidence.
4. **Challenge and decision** — separately addressable evidence and findings, policy verdict, authority, approvals, and waivers.
5. **Enactment and observation** — separately addressable deployment receipt, immediate technical verdict, operational observation, rollback/containment state, and optional outcome-review link.

The records may be distributed across existing issue, repository, CI/CD, artefact, policy, deployment, and observability systems. The grouping does not create a central database or allow evidence, authority, and enactment to collapse into one undifferentiated status.

### Governed Execution And Optional Strategy

A run contract activates when model-mediated work can invoke tools, mutate persistent artefacts, access sensitive data, operate asynchronously, delegate, consume material budget, cross controlled systems, enter a delivery path without full inspection, or materially influence a decision whose basis will not be fully inspected. Incidental, ephemeral, low-risk assistance remains governed by the host product's data/use policy and by ordinary candidate controls when a human adopts its output.

Every change needs a mandate. The full chain below activates only for strategic/product interventions or an applicable external obligation:

`stakeholder need → objective → outcome measures and guardrails → intervention hypothesis → bounded work → outputs → observed outcomes → continue, change, or stop`

Other mandate classes include external obligation, vulnerability/incident response, compatibility/lifecycle, risk reduction, and enabling work. They require relevant success claims, not invented business KPIs or causal product hypotheses.

## 7. Claims, Evidence, And Authority Boundaries

Claims are typed so that "evidence-backed" remains discriminating:

| Claim type | Example | Suitable evidence surfaces |
| --- | --- | --- |
| Structural | Required schema exists and validates | Schema/build validation |
| Functional | Unauthorised requests are rejected | Behavioural tests plus security checks |
| Quantitative | p95 latency remains below a threshold | Controlled benchmark and/or runtime telemetry |
| Compatibility | Supported consumers continue to work | Contract, replay, migration, and consumer tests |
| Safety/security | Cross-tenant disclosure is prevented | Threat analysis, adversarial tests, permission checks, runtime detection |
| Operational | Rollback restores the intended service state | Deployment exercise, receipt, recovery observation |
| Causal/outcome | An intervention reduces abandonment | Experiment or bounded observational evidence with attribution limits |

Evidence remains layered from intent/contract through structural, behavioural, semantic/harm, security/supply-chain, policy, enactment, and runtime surfaces. First-party deterministic tests are valid evidence; they become insufficient when they can share a material failure mode with production or when the claim's materiality requires stronger challenge. A second model is not independent merely because it is a second actor.

No evidence class inherits authority from another:

- valid structure does not prove behaviour;
- passing tests do not establish every semantic, security, or person-impact claim;
- provenance does not establish approval;
- approval does not turn failed or inconclusive evidence into passed evidence;
- a waiver records accepted residual risk and does not rewrite the technical verdict; and
- successful enactment does not prove acceptable operational or stakeholder outcomes.

Final authority and enactment use explicitly configured, bounded, inspectable, reconstructable non-model controls. Their inputs, policy/configuration version, identity, target, candidate, and output remain addressable. This admits statistical telemetry and human judgement without granting a model open-ended merge or production authority.

## 8. Adoption Evidence And Measures

Before widening agent authority or standardising a record schema, an adopting organisation should demonstrate the model on representative work and at least one blocked, failed, or inconclusive path. The demonstration should include:

- a routine maintenance change that does not invent a KPI;
- a strategic intervention that activates the optional outcome overlay;
- a candidate whose changed digest invalidates earlier evidence and approval;
- a governed multi-agent execution with owned workspaces, bounded delegation, cancellation, and resume revalidation;
- isolated execution without standing production credentials;
- separate challenge and authorisation; and
- technical closure, operational closure, and an optional longer-term outcome-review link.

Useful measures include:

- gate lead time, rework, and review wait by materiality;
- required-evidence completeness and stale/unbound rejection;
- verifier false-result and inconclusive samples;
- shared-failure-mode findings missed by nominally independent reviewers;
- human correction and review time per accepted outcome;
- overlapping-write conflicts, orphaned/deadlocked runs, cancellation/resume failures, and poisoned-handoff findings;
- generated-to-accepted change ratio, abandoned artefacts, and induced maintenance/backlog load;
- approval invalidations, waiver age, and direct-authority violations;
- change failure and rollback/containment outcomes; and
- technical and operational closure coverage, plus outcome-review completion where the overlay applies.

Success is not simply faster output. Evidence should show that accepted quality, safety, recoverability, operability, and review cost remain acceptable without hidden manual control debt.

## 9. Decisions Landed, Deferred, And Rejected

| Topic | Result | Reason |
| --- | --- | --- |
| Evidence-backed change kernel | **Landed / preserved** | Keeps intent, implementation, evidence, authority, enactment, and outcome distinct. |
| Seven operational gates | **Landed as synthesis** | Reduces operational vocabulary while preserving separate challenge and authorisation. |
| S0-S10 | **Retained as reference** | Useful diagnostic detail; not externally validated as mandatory workflow state. |
| Five record families | **Landed as synthesis** | Fits normal engineering records while preserving separately addressable evidence, decisions, receipts, and observations. |
| Governed-execution run contracts | **Landed with activation boundary** | Prevents ambient authority without imposing the full envelope on incidental assistance. |
| Typed claims and failure-mode evidence diversity | **Landed** | Makes evidence proportionate to what is asserted and avoids model-count theatre. |
| Bounded, inspectable control execution | **Landed; replaces strict determinism** | Preserves final non-model authority while admitting statistical inputs and fallible environments. |
| Federated authoritative records | **Landed** | Reflects real delivery surfaces while preferring code/repository records where feasible. |
| Technical, operational, and outcome closure | **Landed** | Routine work can close without waiting for portfolio attribution; deployment alone still proves nothing beyond enactment. |
| Objective-to-outcome operating chain | **Landed as optional overlay** | Strong for strategic/product interventions; false precision for many maintenance and obligation classes. |
| Multi-agent coordination invariants | **Landed as synthesis** | Parallel work raises authority, shared-state, cancellation, handoff, and recovery risks. |
| Vendor productivity and quality figures | **Investigate locally** | Vendor-reported results cannot establish a consumer baseline or causal benefit. |
| Universal record schema and global autonomy thresholds | **Deferred** | Require compatibility analysis and evidence segmented by task and materiality. |
| New central lifecycle platform | **Rejected as prerequisite** | Existing linked systems can implement the controls. |
| Direct agent merge/deploy authority | **Rejected** | Conflicts with evidence/authority separation and bounded non-model control execution. |
| Vendor rituals, one-prompt flow, and prescribed product stack | **Rejected as doctrine** | Optional implementation observations are not portable controls. |

## 10. Consumer Impact And Residual Risk

**Change class:** normative replacement and clarification for consumers using AI or agents across software delivery. The compatibility proposal is a **0.x minor** increment; pinned consumers should review before upgrading.

Migration preserves the existing control kernel while changing its operating surface. Consumers should map S0-S10 to the seven gates, group existing linked records into the five families, apply run contracts to governed executions, type material claims, assess verifier diversity by failure mode, identify authoritative systems of record, and choose technical, operational, or outcome closure explicitly. Strategic objective/measure/intervention lineage becomes conditional rather than universally required.

Residual risks:

- seven gates and five record families are library synthesis and have not been established as optimal across organisations;
- the governed-execution threshold can drift or be gamed unless representative fixtures and policy ownership keep it calibrated;
- durable cross-system links and automatic evidence/approval invalidation may require delivery-platform work;
- evidence retention, prompt/privacy boundaries, and legally mandated oversight remain context-specific;
- bounded control mechanisms can still act on incomplete or noisy inputs; reconstructability is not correctness;
- evidence diversity can become ceremonial unless shared failure modes are sampled and challenged;
- vendor-authored predictions, statistics, and case studies are not independently audited comparative evidence;
- wider non-engineering creation can produce shadow systems and maintenance debt faster than governance capacity expands; and
- none of the cited sources establishes a universal autonomy threshold or validates one portable record schema.

## 11. References

- NIST, [Secure Software Development Framework (SSDF) Version 1.1, SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final).
- NIST, [Secure Software Development Practices for Generative AI and Dual-Use Foundation Models, SP 800-218A](https://csrc.nist.gov/pubs/sp/800/218/a/final).
- NIST, [AI Risk Management Framework 1.0](https://airc.nist.gov/airmf-resources/airmf/).
- ISACA, [COBIT 2019 Goals Cascade](https://www.isaca.org/resources/news-and-trends/industry-news/2019/employing-cobit-2019-for-enterprise-governance-strategy).
- Basili et al., [GQM+Strategies](https://arxiv.org/abs/1402.0292); University of Maryland, [Goal/Question/Metric technical report](https://drum.lib.umd.edu/items/8119803a-362b-42ec-b6ce-2311713e7236).
- DORA, [Software delivery performance metrics](https://dora.dev/guides/dora-metrics/).
- Google, [OKR playbook (reprinted with permission)](https://www.whatmatters.com/resources/google-okr-playbook).
- NCSC and international partners, [Guidelines for Secure AI System Development](https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development/guidelines).
- ISO, [ISO/IEC 5338:2023 — AI system life cycle processes](https://www.iso.org/standard/81118.html).
- SLSA, [Provenance v1.2](https://slsa.dev/spec/v1.2/provenance).
- European Union, [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj).
- AWS, [AI-Driven Development Life Cycle](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/).
- Microsoft, [An AI-led SDLC](https://techcommunity.microsoft.com/blog/appsonazureblog/an-ai-led-sdlc-building-an-end-to-end-agentic-software-development-lifecycle-wit/4491896).
- GitHub, [Spec Kit: Evolving specifications](https://github.github.com/spec-kit/guides/evolving-specs.html).
- Anthropic, [2026 Agentic Coding Trends Report](https://resources.anthropic.com/2026-agentic-coding-trends-report) (public landing page; only claims visible there are relied upon).
