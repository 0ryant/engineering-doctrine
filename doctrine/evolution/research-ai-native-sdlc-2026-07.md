# Research: A Doctrine-Grounded AI-Native Software Development Lifecycle (July 2026)

**Purpose:** Evaluate the operator-supplied *AI-Native Software Authority Lifecycle — Council Session 1*, reconcile it with this library and current primary sources, and record why the adopted lifecycle is an evidence-backed state-transition system rather than a vendor workflow or an autonomous-agent release path.

**Decision record:** [ADR 0024](../../docs/adr/0024-adopt-a-doctrine-grounded-ai-native-software-development-lifecycle.md).
**Normative landing:** [AI-Native Software Development Lifecycle](../patterns/ai-native-software-development-lifecycle.md).
**Review surface:** [AI-Native SDLC Readiness Checklist](../checklists/ai-native-sdlc-readiness.md).

---

## 1. Trigger, Provenance, And Source Limits

The trigger was the operator-supplied `ai-native-software-authority-lifecycle-council-session-1.docx` on 2026-07-17. The document calls itself a non-binding council draft. It contains a coherent original synthesis, vendor landscape notes, an eleven-state lifecycle, transition admissibility fields, authority roles, evidence classes, materiality tiers, adoption stages, measures, and open decisions for a later council.

The source is **proposal evidence**, not doctrine authority. No named council members, empirical pilot, public review record, or validated transition schema accompany it. Its vendor sources show product direction and practitioner hypotheses; they do not prove that the proposed lifecycle improves safety, quality, or flow.

The source was structurally inspected before amendment: 234 paragraphs, 23 tables, one section, no comments, and no tracked insertions/deletions. All 13 rendered pages were reviewed. Two presentation defects were found (numbered lists restarting at 8 and 17), and one research statement was stale: the cited Anthropic report is publicly accessible as a PDF at the time of this review.

## 2. Existing Doctrine Baseline

The proposal does not replace this library's existing control model. The following were already authoritative:

| Concern | Existing doctrine | Constraint on the lifecycle |
| --- | --- | --- |
| Source of truth | [single-source-of-truth.md](../principles/single-source-of-truth.md), [ai-ml-systems.md](../principles/ai-ml-systems.md) §1 | Repository and durable operational records govern; chat/model state does not. |
| Build and promotion | [build.md](../principles/build.md) | Explicit, reproducible build surfaces; promote the same immutable artefact. |
| Merge-path authority | [merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md), [code-review-and-change-approval.md](../patterns/code-review-and-change-approval.md) | Binding CI, protected branches, authenticatable/scoped/retrievable evidence, accountable approval. |
| Agent execution | [run-contracts.md](../patterns/run-contracts.md) | **Every agent execution** compiles to a run contract. This is not an open threshold decision. |
| Agent verification | [verifier-packs.md](../patterns/verifier-packs.md) | Every skill has a bounded verifier mirror; `pass`, `fail_loud`, `mark_untrusted`, `inconclusive`; no silent skip. |
| AI risk | [ai-ml-systems.md](../principles/ai-ml-systems.md), [ai-adoption-controls.md](../patterns/ai-adoption-controls.md) | Capability and materiality are separate axes; higher-impact action receives stronger oversight, testing, and runtime control. |
| Secure lifecycle | [secure-development-lifecycle.md](../principles/secure-development-lifecycle.md), [testing-strategy.md](../principles/testing-strategy.md) | Security is prepared, protected, produced, and responded to throughout the lifecycle; risk-based testing remains mandatory. |
| Runtime accountability | [reliability-slo-incidents.md](../principles/reliability-slo-incidents.md), [measurement-and-dora.md](../principles/measurement-and-dora.md) | Enactment is not success; SLO, incident, change-failure, and flow evidence close the loop. |

## 3. Primary And Authoritative External Grounding

Verified 2026-07-17. These sources support parts of the control model; none mandates this library's eleven states.

| Source | What it supports | Boundary / non-claim |
| --- | --- | --- |
| **NIST SP 800-218, SSDF 1.1** | A risk-based secure development framework spanning Prepare, Protect, Produce, and Respond; practices integrate into each SDLC implementation. | It is an outcome/practice framework, not this transition model. [NIST](https://csrc.nist.gov/pubs/sp/800/218/final) |
| **NIST SP 800-218A** | AI model producers and system producers/acquirers apply AI-specific secure practices throughout the SDLC in addition to SSDF 1.1. | It does not replace SSDF or prescribe agent authority. [NIST](https://csrc.nist.gov/pubs/sp/800/218/a/final) |
| **NCSC/CISA et al., Guidelines for Secure AI System Development** | Secure design, development, deployment, and operation/maintenance; ownership of security outcomes across the lifecycle. | Guidance, not proof that a particular agentic process works. [NCSC](https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development/guidelines) |
| **ISO/IEC 5338:2023** | Defines and manages AI system lifecycle processes, using established systems/software lifecycle foundations and allowing organisation-specific lifecycle models. | The standard's full normative text is paywalled; this review relies on ISO's official abstract, not invented clauses. [ISO](https://www.iso.org/standard/81118.html) |
| **NIST AI RMF 1.0** | GOVERN is cross-cutting; MAP, MEASURE, and MANAGE operate continuously and iteratively. MAP 1.3–1.6 and MAP 2.1 connect organisational mission/goals, business value, risk tolerance, requirements, and supported tasks; MAP 3 connects benefits and costs. | Voluntary risk framework; functions are not a linear release checklist or a company strategy method. [NIST AIRC](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) |
| **COBIT 2019 goals cascade** | Translates stakeholder needs and enterprise goals into prioritised alignment goals and governance/management objectives, aligning I&T strategy to enterprise strategy. | It supports strategic lineage, not automatic decomposition into software tasks. [ISACA](https://www.isaca.org/resources/news-and-trends/industry-news/2019/employing-cobit-2019-for-enterprise-governance-strategy) |
| **GQM and GQM+Strategies** | Derives questions and measures from explicit goals; extends this to link business strategies and organisational goals to operational software goals and measurement. | It structures goal-oriented measurement; it does not prove a selected intervention caused an observed outcome. [GQM+Strategies](https://arxiv.org/abs/1402.0292), [UMD GQM report](https://drum.lib.umd.edu/items/8119803a-362b-42ec-b6ce-2311713e7236) |
| **DORA software delivery metrics** | Measures delivery-process outcomes using throughput and instability signals, with context-specific leading/lagging interpretation. It warns against setting a metric as the goal or using one metric for a complex system. | DORA metrics diagnose delivery-system health; they are not enterprise objectives or universal team targets. [DORA](https://dora.dev/guides/dora-metrics/) |
| **SLSA v1.2** | Build provenance records how, where, and with what inputs an artefact was produced; source/build tracks support immutable candidate identity and supply-chain integrity. | Provenance does not establish semantic correctness or business approval. [SLSA](https://slsa.dev/spec/v1.2/) |
| **EU AI Act, Regulation (EU) 2024/1689** | For in-scope high-risk AI: lifecycle risk management, human oversight including override/stop, accuracy/robustness/cybersecurity, and post-market monitoring. | Legal applicability is estate- and use-case-specific. The doctrine uses these as rationale, not as a claim that every consumer is regulated. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) |

### Version Honesty

NIST published an Initial Public Draft of SP 800-218 Revision 1 (SSDF 1.2) in December 2025. This research does not silently promote a draft to final authority: SSDF 1.1 and its final AI community profile SP 800-218A remain the cited final baseline. [NIST project page](https://csrc.nist.gov/projects/ssdf)

## 4. Vendor And Practitioner Observations

Vendor material is useful for landscape awareness and implementation ideas, not as normative authority or independent effectiveness evidence. The three sources were re-reviewed at the operator's request on 2026-07-17.

| Observation | Useful signal | Limit |
| --- | --- | --- |
| **AWS AI-DLC** describes a repeated plan → clarify → human-validate → implement loop across inception, construction, and operations. It persists requirements, plans, and designs in the repository, concentrates humans on critical decisions, and proposes short collaborative work cycles. | Durable intent, explicit clarification before execution, and rapid human decision points are stronger than a one-shot prompt. Repository persistence aligns with the doctrine source-of-truth boundary. | The assertion that AI-assisted and autonomous approaches are suboptimal, the quality/velocity benefits, and the renamed rituals are vendor claims. “Mob” collaboration and “bolts” are optional team practices, not portable controls. [AWS](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/) |
| **Microsoft AI-led SDLC** demonstrates spec-first decomposition into tasks, a coding agent working on a branch/PR, agent-assisted review, an isolated preview environment, deterministic CI/CD promotion, and an SRE agent opening a new issue from runtime evidence. It also exposes agent actions and workflow runs for inspection. | This gives concrete handoffs for S1/S2 → S4, supports treating executable candidates as untrusted until isolated evaluation, reinforces deterministic enactment, and shows runtime observations feeding a new S0. Action receipts are useful evidence. | A weather-dashboard demonstration does not establish safety or scalability for material systems. Product-specific components, reported third-party review statistics, and visibility into purported model “thinking” are not portable proof; doctrine records observable actions and outcomes, not private chain-of-thought. [Microsoft](https://techcommunity.microsoft.com/blog/appsonazureblog/an-ai-led-sdlc-building-an-end-to-end-agentic-software-development-lifecycle-wit/4491896) |
| **GitHub Spec Kit** evolves specification, plan, tasks, and implementation with flow-back when discovery changes upstream artefacts. | Specs are living, versioned records; material change must invalidate and rebind derived work. | A specification is not verification, approval, or runtime evidence. [GitHub](https://github.github.com/spec-kit/guides/evolving-specs.html) |
| **Google OKR playbook** distinguishes objectives from measurable key results, rejects activity-only KRs and “launch X” without user/economic benefit, and requires credible evidence. | Supports outcome-oriented goals and cross-team commitments rather than task-count scorecards. | Reprinted practitioner guidance, not a standard; OKR vocabulary and scoring are optional. [What Matters, reprinted with Google permission](https://www.whatmatters.com/resources/google-okr-playbook) |
| **Anthropic 2026 Agentic Coding Trends Report** predicts multi-agent coordination, days-long task horizons, exception-focused human oversight, agentic creation by non-engineers, increased output volume, and dual-use security pressure. Its own framing says high-stakes work still needs active supervision and validation. | Multi-agent lineage/workspace ownership, checkpoints and safe resume, human-attention measures, equal controls for domain-expert-created software, and security-first isolation are credible design pressures. | These are vendor-authored predictions, self-reported studies, and case studies—not a portable governance standard, audited comparative evidence, or proof of the numeric productivity claims. [Anthropic](https://resources.anthropic.com/2026-agentic-coding-trends-report) |

### Vendor Decision Pass

| Finding | Decision | Doctrine landing or reason |
| --- | --- | --- |
| Persist intent, claims, plans, and clarifications in versioned repository records; flow material changes back through derived work. | **Take** | S1/S2 now require versioned records; changed intent/claims invalidate downstream contracts, candidates, evidence, and approvals until rebound. |
| Compile multi-agent work into explicit parent/child scopes, dependencies, owned workspaces, handoffs, and integration responsibility. | **Take** | S4, transition admissibility, the readiness checklist, and ADR 0024 now make coordination evidence explicit. Every child remains a distinct agent execution with its own run contract. |
| Make long-running work checkpointable, expiring, cancellable, and safely resumable. | **Take** | Added to the invariant, run-contract surface, checklist, tooling illustration, and pilot acceptance criteria. A stale run cannot silently resume. |
| Execute agent-produced code in an isolated preview/test environment before promotion. | **Take** | Added as a portable control; no vendor sandbox product is prescribed. Isolation does not replace independent tests, review, or deterministic promotion. |
| Observe agent actions, tool calls, outputs, and workflow receipts. | **Take with privacy boundary** | These are evidence; private chain-of-thought is neither required nor treated as proof. Prompt/secret retention remains minimised. |
| Let operational agents turn runtime signals into new work. | **Take with authority boundary** | An agent may register S0 and propose remediation; it may not detect, implement, approve, and deploy its own change as one closed loop. |
| Focus scarce human attention on novelty, ambiguity, material impact, and exceptions. | **Take as calibrated routing** | Existing capability × materiality gates remain authoritative. Automated review can prioritise attention but cannot remove accountable approval for high-risk change or make the producer its sole challenger. |
| Allow domain experts and non-engineers to create executable tools with agents. | **Take under the same controls** | Originator job title does not waive ownership, inventory, repository, privacy, security, review, operability, or retirement obligations. |
| Treat output volume and speed as evidence of success. | **Investigate, do not adopt** | Pilot measures now include accepted outcomes, human attention, abandoned artefacts, induced backlog, quality, and runtime results. Vendor numeric claims are not baselines. |
| Adopt vendor product stacks, AWS ritual names, a one-prompt-to-production flow, or autonomous closed-loop remediation. | **Reject as doctrine** | These either belong in an estate ADR or violate the evidence and authority model. |

## 5. Council Proposal: Findings And Amendments

### Findings Preserved

1. **State transitions are a stronger control model than phase labels.** They expose what changed, which evidence applies, who authorised it, and what invalidates the decision.
2. **Intent, executable artefacts, authority, evidence, and observed runtime state must remain distinct.** Conflating them creates self-approval and stale-evidence failure modes.
3. **Runtime reconciliation is first-class.** Delivery completion without observed outcome encourages premature success claims.
4. **Deterministic and agentic surfaces should be separated.** Model discretion can assist ambiguous work; policy, artefact addressing, promotion, rollback, and receipts require deterministic enforcement.
5. **Brownfield adoption should be staged.** Existing systems can carry the record; a new lifecycle platform is not a prerequisite.

### Corrections And Tightening

| Council question or claim | Doctrine-grounded resolution |
| --- | --- |
| Should every action have a run contract, or only those above a threshold? | Every **agent execution** has a run contract. Deterministic CI/deployment jobs use their normal manifests, immutable inputs, identities, policy, and receipts; do not relabel all automation as agentic. |
| Can verifier packs implement the verification layer? | They implement bounded execution assertions. They are composed with domain/semantic, security, supply-chain, human/policy, and runtime evidence; they cannot prove whole-system correctness. |
| Can an agent authorise a transition after evaluating it? | No. Agents may recommend. Protected-branch/release policy and accountable approvers hold authority; the producer is not the sole challenger. |
| Is a transition bundle a new central database? | Not necessarily. It is a reconstructable record whose fields may live in linked issue, repository, CI/CD, artefact, policy, and observability systems. |
| Should the universal schema be standardised now? | No. First pilot one real change and its failure/inconclusive path; use the evidence to decide which fields merit a portable contract. |
| Are `PASS`, `FAIL`, `WAIVED`, and similar one global verdict catalogue? | No. Verifier-pack verdicts remain their adopted four-state model. A waiver is a separate policy decision that leaves the original evidence intact. |
| May high-confidence agents receive more autonomy? | Confidence is not authority evidence. Increase autonomy from task observability, reversibility, discriminating verification, sampled review, rollback results, and incident history. |

## 6. Adopted Synthesis

For a company-wide AI-native operating model, the lifecycle is preceded and closed by an objective-to-outcome chain:

`stakeholder need → objective or standing obligation → outcome measures and guardrails → intervention hypothesis → tasks/run contracts → outputs → observed outcomes → portfolio decision`

This chain is externally grounded by COBIT's goal cascade, GQM+Strategies, NIST AI RMF, and DORA's metric cautions. The exact record shape and its composition with S0–S10 are this library's synthesis. It deliberately rejects a direct KPI-to-task compiler: measures do not authorise work, interventions are causal hypotheses, and outputs do not prove outcomes.

The adopted lifecycle has eleven control states:

1. S0 observed need;
2. S1 intent registered;
3. S2 claims specified;
4. S3 transition designed;
5. S4 work compiled;
6. S5 candidate produced;
7. S6 candidate challenged;
8. S7 transition authorised;
9. S8 transition enacted;
10. S9 runtime evaluated; and
11. S10 reconciled.

This ordering is **our synthesis**. External sources justify lifecycle-wide risk, security, provenance, oversight, and monitoring. Existing doctrine supplies repository authority, run contracts, verifier packs, protected merge paths, deterministic promotion, materiality, reliability, and review. The state names and transition-record composition are the library's own integration decision.

## 7. Evidence Classes And Authority Boundaries

The council's verification ladder is retained but made compositional:

- E0 intent;
- E1 run/task contract;
- E2 structural;
- E3 behavioural;
- E4 semantic and harm;
- E5 security and supply chain;
- E6 human and policy; and
- E7 enactment and runtime.

No layer inherits authority from another. In particular:

- valid structure does not prove behaviour;
- passing tests do not establish all semantic or person-impact claims;
- provenance does not establish approval;
- human approval does not turn failed evidence into passed evidence; and
- successful deployment does not establish acceptable runtime outcomes.

## 8. Brownfield Pilot And Metrics

The first pilot should be a moderate-materiality, reversible, observable change with a real consumer outcome. It must:

1. reconstruct S0–S10 using existing systems;
2. compile a parent run and at least one delegated child run with separate contracts, workspaces, checkpoints, and verifier packs;
3. stop and safely resume one long-running execution without accepting stale authority or context;
4. execute the candidate in an isolated preview/test environment without production credentials;
5. bind a candidate digest to evidence and approval;
6. deliberately exercise one failed or inconclusive challenge;
7. deploy deterministically with a rollback path;
8. let an operational signal originate a new S0 record without bypassing the normal authority path; and
9. reconcile runtime signals to the original claims.

Record:

- lead time and rework by state;
- required-evidence completeness and stale/unbound rejection;
- human corrections, verifier inconclusive/false result samples, and agent cost per accepted outcome;
- overlapping-write conflicts, orphaned/deadlocked runs, failed resumes, escalation quality, and human review time per accepted outcome;
- generated-to-accepted change ratio, abandoned artefacts, and induced maintenance/backlog load;
- approval invalidations, waiver age, direct-authority violations;
- change failure and rollback/containment outcomes; and
- percentage/time of release-to-runtime reconciliation.

Success is not simply faster delivery. The pilot should show that accountability, safety, and operability are maintained or improved without creating hidden manual control debt.

### Pilot Tasking

These tasks convert the vendor-source review into executable adoption work. Named people and estate-specific file paths are assigned when the pilot is approved.

| Accountable role | Objective and owned surface | Acceptance and verification evidence | Stop condition |
| --- | --- | --- | --- |
| **Lifecycle/product owner** | Version stakeholder need, objective/obligation, measurement and guardrail contract, intervention hypothesis, intent, claims, clarifications, and task graph in the existing strategy/portfolio, issue/spec, and PR path. | One change reconstructs objective → measures → intervention → S0–S5; changing a material objective, measure, or claim invalidates or rebinds derived contracts and approvals. | Stop if durable upward lineage, measure provenance, or decision ownership requires manual inference. |
| **Agent-platform owner** | Implement parent/child run identifiers, delegated scopes, dependency/workspace ownership, checkpoints, cancellation, expiry, and safe resume. | Two agents work in non-overlapping workspaces; a forced stop/resume emits receipts; stale authority blocks; integration ownership is explicit. | Stop on overlapping writes, orphaned/deadlocked runs, undeclared delegation, or resume without contract revalidation. |
| **Platform/security owner** | Provide disposable preview/test isolation for agent-produced executable content. | Policy evidence shows no standing production credential, bounded data/egress, disposable state, and deterministic promotion of the approved digest. | Stop if isolation or credential boundaries cannot be demonstrated. |
| **Service/SRE owner** | Route a synthetic or real operational finding into a new S0 record and normal challenge/authorisation path. | Runtime evidence, triage owner, proposed remediation, independent challenge, approval, deployment receipt, and reconciliation are linked. | Stop if the detecting agent can self-authorise or directly deploy the remediation. |
| **Measurement owner** | Establish a baseline and pilot scorecard for flow, accepted outcomes, quality, attention, coordination, demand amplification, cost, and recovery. | Before/after definitions, sample method, evidence source, and review cadence are recorded; vendor case-study figures are excluded as local baselines. | Stop expansion if speed/output rises while accepted quality, safety, recovery, review load, or maintainability worsens. |

## 9. Decisions Landed, Deferred, And Rejected

| Topic | Result | Reason |
| --- | --- | --- |
| State-transition lifecycle | **Landed** | Makes evidence and authority invalidation explicit while allowing existing phase language as a view. |
| Objective-to-outcome operating chain | **Landed** | External goal-cascade and measurement sources support explicit strategic lineage; separating measures, interventions, tasks, outputs, and outcomes prevents activity from masquerading as value. |
| Run contract for every agent execution | **Landed / already doctrine** | A threshold would reintroduce unbounded agent work and conflict with the existing pattern. |
| Layered evidence model | **Landed** | Prevents execution-local verification from being mistaken for global correctness. |
| Deterministic enactment | **Landed** | Keeps non-deterministic model discretion away from the production authority boundary. |
| Multi-agent lineage and workspace ownership | **Landed** | Parallel context and output increase integration risk; each execution remains separately bounded and traceable. |
| Long-running checkpoints, expiry, cancellation, and safe resume | **Landed** | Extended duration increases stale-context and stale-authority risk. |
| Isolated preview/test plus action-level receipts | **Landed** | Agent-produced code is untrusted until challenged; observable actions are evidence, private reasoning is not. |
| Operations-originated S0 feedback | **Landed with authority boundary** | Agents may detect and propose, but cannot close the request/produce/approve/enact loop themselves. |
| Agentic creation by domain experts/non-engineers | **Landed under existing controls** | Wider access increases the need for inventory, ownership, repository, security, review, operability, and retirement controls; job title is not a waiver. |
| Vendor productivity and quality figures | **Investigate locally** | Self-reported/vendor studies can motivate measures but cannot establish this estate's baseline or causal benefit. |
| Universal transition-record schema | **Deferred** | Requires pilot evidence and compatibility analysis. |
| Global autonomy thresholds | **Deferred** | Must be calibrated by task class, estate, materiality, and observed evidence. |
| New central lifecycle platform | **Rejected as prerequisite** | Existing linked systems can implement the control model; premature centralisation adds lock-in and ceremony. |
| Direct agent merge/deploy authority | **Rejected** | Conflicts with protected merge paths, separation of duties, and deterministic authorisation. |
| Vendor ritual names, one-prompt flow, and prescribed product stack | **Rejected as doctrine** | Team practices and products are estate choices; the portable contract is evidence, authority, isolation, and reconciliation. |

## 10. Consumer Impact And Residual Risk

**Change class:** normative tightening for consumers that use AI or agents across software delivery. The compatibility proposal is a **0.x minor** increment; pinned consumers must review before upgrading. Migration follows P0–P5 in the pattern. The minimum new obligations are objective/obligation-to-outcome lineage, measurement and guardrail contracts, an explicit intervention hypothesis, traceable intent/claims, run contracts for every agent execution, explicit coordination and safe resume for multi-agent/long-running work, isolated execution of untrusted candidates, evidence-bound authorisation, deterministic enactment of the authorised artefact, and runtime/portfolio reconciliation.

Residual risks:

- the eleven-state granularity has not yet been empirically compared with simpler alternatives;
- durable cross-system evidence links and approval invalidation may require platform work;
- evidence retention, prompt/privacy boundaries, and legally mandated oversight are estate-specific;
- the market landscape is changing quickly; these vendor-authored predictions, statistics, and case studies are not independently audited comparative evidence and may overstate maturity;
- exception-focused oversight could become rubber-stamping if escalation recall and sampled human review are weak;
- wider non-engineering creation can produce shadow systems and maintenance debt faster than governance and platform capacity expand; and
- objectives and KPIs can create false precision, gaming, priority cascades, or spurious causal claims when data quality, countermetrics, intervention assumptions, and opportunity cost are weak; and
- no pilot evidence yet establishes an autonomy threshold or transition schema.

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
- SLSA, [Specification v1.2](https://slsa.dev/spec/v1.2/).
- European Union, [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj).
- AWS, [AI-Driven Development Life Cycle](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/).
- Microsoft, [An AI-led SDLC](https://techcommunity.microsoft.com/blog/appsonazureblog/an-ai-led-sdlc-building-an-end-to-end-agentic-software-development-lifecycle-wit/4491896).
- GitHub, [Spec Kit: Evolving specifications](https://github.github.com/spec-kit/guides/evolving-specs.html).
- Anthropic, [2026 Agentic Coding Trends Report](https://resources.anthropic.com/2026-agentic-coding-trends-report) (landing page linking the report reviewed here).
