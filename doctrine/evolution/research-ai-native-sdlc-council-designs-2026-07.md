# Research: AI-Native SDLC Council Designs — Session 1 Landscape, Framed Designs, And Critique (July 2026)

**Status:** non-normative council record (design-space research). **Companion:** [research-ai-native-sdlc-2026-07.md](research-ai-native-sdlc-2026-07.md) — the claim-by-claim research basis for the landed chain: [ADR 0024](../../docs/adr/0024-adopt-a-doctrine-grounded-ai-native-software-development-lifecycle.md) as amended by [ADR 0030](../../docs/adr/0030-refine-ai-native-sdlc-into-gates-records-and-applicability-overlays.md), the normative pattern [ai-native-software-development-lifecycle.md](../patterns/ai-native-software-development-lifecycle.md), and checklist [ai-native-sdlc-readiness.md](../checklists/ai-native-sdlc-readiness.md). This note preserves the session-1 council record feeding that line: landscape research across ten external frameworks/corpora, the doctrine **invariant register** used for grounding, three complete framed lifecycle designs (**verification-native**, **intent-ledger**, **fleet-charter**), the six **adversarial critiques**, and the resulting decision list.

**How to read §6–§7 against the landed chain:** the evidence-backed change kernel, seven operational gates, five record families, and the run-contract activation boundary are **landed**; the landed note's §9 records the chain's dispositions **in its own vocabulary** — it does not map D1–D17 item-by-item, and no D-id should be read as implicitly landed. Council machinery that remains **open input** for future revisions includes the sampled-lane and routing-classifier designs (D3–D5, D10), the calibration program (D8–D9, D17), model-churn recertification economics (D13), and attention-budget governance (D14). Two distinctions matter when reading the body. (1) **Direct agent merge/deploy authority** — agents *holding* merge authority — was **rejected** by the landed chain. The sampled/unsampled merge-lane designs are a different mechanism (a bounded non-model control executes the merge; agents never hold authority; see §5.1 item 1) that the landed chain neither adopted nor superseded — the underlying autonomy-threshold question is recorded as **deferred**, so D3–D5/D10 are **unadopted proposals pending a future ADR**. (2) The two "unanimous supersessions" the council proposed (§5.1 items 6 and 8; ratification proposed in D12) — the delivery-corpus-29 bounded flag-reversion carve-out and the delivery-corpus-7 disclosure-polarity inversion — target live normative text in [feature-flag-lifecycle.md](../patterns/feature-flag-lifecycle.md) and [code-review-and-change-approval.md](../patterns/code-review-and-change-approval.md) and were **never adopted**; they are likewise unadopted proposals. §7's session plan is the council's proposed schedule, not a standing commitment: subsequent work proceeded via the landed ADR 0024/0030 chain, and any future council sessions would proceed via a **new ADR against the landed pattern**, not by executing §7 as written. **Nothing in this note overrides any normative doctrine file.**

---

## 1. Purpose and method

**Goal.** Design a normative AI-native SDLC pattern for this library that survives agent-majority authorship without abandoning the doctrine's control posture. Session 1 delivers the inputs; sessions 2+ resolve decisions and draft normative text.

**Method (this session).**

1. **Landscape research**: ten frameworks/corpora researched independently (vendor lifecycles, spec-driven toolkits, multi-agent methodologies, academic syntheses, standards/measurement layers, day-2 operations). Each researcher recorded fetch failures and unverifiable claims inline; those flags are preserved below.
2. **Doctrine grounding**: consolidation of the invariants the design must honor, drawn from [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md), [../principles/merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md), [../patterns/run-contracts.md](../patterns/run-contracts.md), [../patterns/verifier-packs.md](../patterns/verifier-packs.md), and adjacent files — plus the **tension list**: places where current doctrine tacitly assumes human-authored code.
3. **Three framed designs**: independent design teams each produced a complete lifecycle from a distinct frame — verification-native (VN-SDLC), spec-as-system-of-record (IL-SDLC), and agent-workforce management (FC-SDLC).
4. **Adversarial critique**: each design was attacked through two lenses — a practicality/failure-modes lens (sceptical staff engineer under deadline pressure) and a doctrine-fidelity/governance lens (citation spot-check, undeclared supersessions, accountability termination, auditor survivability). All six critiques returned **flawed** (none returned fatal); blockers and majors are recorded per design with proposed fixes.

**What session 1 does not do**: it does not pick a winner, write normative text, or land supersession ADRs. It produces the decision list (§6) those sessions will consume.

---

## 2. Landscape map

### 2.1 Comparison table

| Framework | Phases | Autonomy model | Verification approach | Human gates | System of record | Standout idea | Key weakness |
|---|---|---|---|---|---|---|---|
| **Microsoft "AI-led SDLC"** (Azure+GitHub, Feb 2026) | Spec (Spec Kit) → coding agent → AI-assisted review → deterministic CI/CD → SRE agent ops, loop closed | "Autonomy sandwich": agentic edges, zero-agent deterministic middle; SRE agent 2×2 (identity × run mode) on Azure RBAC | Evidence-in-PR (tests, Playwright screenshots) + CodeQL/analyzers + mandatory human PR approval + per-PR ephemeral envs | Human merges everywhere; deploy rule-based; SRE Review mode admin-approved | Code + GitHub/Azure artifacts; **no unified provenance across boundary** | Agents must NOT decide deployments; ops→dev loop closure (SRE-filed issue → coding agent) | No provenance/attestation framework; no circuit breaker on the closed loop; human review is the unscaled choke point; article body **not fetchable** (verified via primary docs) |
| **AWS AI-DLC** | Inception (Mob Elaboration) → Construction (Bolts, Mob Construction) → Operations (largely "future") | Supervised AI-drives-process: AI proposes/implements only after human validation; adaptive stage skipping; FSI variant risk-gates | Structured clarification files, stage-gate approvals, per-unit build-and-test loop, audit.md decision log | Requirements, execution plan, per-unit code-gen plans, generated code | Repo-resident markdown (aidlc-docs/, audit.md, aidlc-state.md) | Clarification-questions-as-files; bolts (hours-scale cycles paced by human validation) | Enforcement is prompt-deep only; audit.md written by the agent it audits; flagship Bedrock metrics internally inconsistent; ops phase vaporware |
| **GitHub Spec Kit / SDD** | Constitution → specify → clarify → plan (Phase −1 gates) → tasks/analyze/checklist → implement | Human-steered phase-gated semi-autonomy; ~35 agent integrations | [NEEDS CLARIFICATION] markers, constitutional gates, cross-artifact /analyze, checklists as "unit tests for English", test-first | Checkpoint at every phase boundary; per-task diff review | Spec claimed; **in practice branch-scoped snapshots that rot post-merge** | Constitution with slot articles + auditable waiver ledger (Complexity Tracking) | All gates advisory/skippable; no post-merge spec-code conformance check; self-described experiment |
| **Anthropic practices + 2026 Trends** | Define success → explore/plan → implement w/ closable loop → independent judge → commit/scale → calibrate evaluator | Bounded autonomy scaled to verifiability (60% usage vs 0–20% full delegation); mechanical tiers (allowlists → classifier auto mode) | Machine-checkable criteria before code; stop-gate ladder; fresh-context/different-model judge; evidence-over-assertion | Plan edit, PR merge, BLOCKED escalation, evaluator curation | Files as coordination substrate; CLAUDE.md pruned like code | Judge/builder separation at infrastructure level; the over-review warning; 80-line learnings cap | Vendor conflict of interest; frontier-lab generalization gap; evaluator calibration admitted unsolved; "~100% AI code" claim **not supported** (calibrated: >80% merged lines) |
| **Amazon Kiro + specs.md** | Steering/hooks → requirements (EARS) → design → tasks → wave execution; specs.md adds FIRE/AI-DLC flows | Two dials: phase gates (skippable via Quick Plan) × execution supervision (Autopilot/Supervised); standing hooks | EARS traceability + phase-gate review + event hooks + context-inclusive checkpoints; no machine conformance check | Conversational confirms between phases; per-hunk review in Supervised | 3 markdown files; specs effectively **discarded after ship** | EARS as agent-facing requirements notation; steering inclusion modes as context budget; complexity-scaled checkpoints (3–26) | Gates are chat interactions, not controls; IDE lock-in (gates/traceability don't survive export); agents ignore steering; specs.md operator **unidentified** |
| **BMAD / MetaGPT / ChatDev / OpenHands** | PRD → architecture → story sharding → implement → QA gate (varies by framework) | Spectrum: BMAD human-gated per artifact; MetaGPT/ChatDev autonomous pipelines; OpenHands one generalist agent + sandbox | Typed artifact schemas (MetaGPT); communicative dehallucination (ChatDev); empirical sandbox tests (OpenHands); QA gate files (BMAD) | BMAD: every artifact; others: optional/off by default | Repo files (BMAD story files) or message pool artifacts | Context-complete story files; SOP-as-typed-interface; **negative result**: role-play decomposition doesn't help (MAST: ~37% of failures caused by multi-agent structure itself) | ChatDev 85% "executability" but 33.3% correctness (MAST); toy-app benchmarks; BMAD zero controlled evidence |
| **Academic: Bhati A-SDLC + Hymel V-Bounce** | Requirements (tests born with reqs) → design → "bounce" implementation → continuous validation → deploy → maintain | Delegated execution under human supervision; orchestrator + phase sub-agents; six-activity loop with 2 human touchpoints/phase | Continuous test creation w/ traceability by construction; paired quality-agents as checksums; behavioral KPIs | Per-phase review+approval; production promotion always human | PRD + traceability matrix + knowledge graph | Economics of attention as terminal open problem; behavioral metrics (acceptance rate, escalation quality, supervision burden) | Neither peer-reviewed (preprint + vendor whitepaper); V-Bounce zero empirical validation; human gates never operationalized |
| **Enterprise consensus (PwC/CodeRabbit/DronaHQ/Thoughtworks)** | Requirements → design (most-human) → dev → continuous testing → automated review layer → deploy/operate | Bounded/propose-only: open PRs, never merge; harness = feedforward + feedback controls | Three tiers: in-loop deterministic → AI review at generation speed → human judgment for architecture/merge | Merge + production deploy + remediation approval | Code canonical (only Tessl inverts) | "Verification tax" as the central economic problem; same-bar review invariance; cognitive debt | PwC primary **unfetchable (403)** — 96% defect-reduction stat unverifiable; no maturity model with teeth; no agent-specific SLOs |
| **Standards layer (DORA 2025/26 + NIST 800-218A + OWASP + EU AI Act)** | Policy/literacy → capability instrumentation → provenance-neutral gates → agent threat controls → measurement → ROI | Autonomy granted to generation, never acceptance; least-privilege tool scopes; OBO elevation | Uniform SSDF gates (no AI exemptions); DORA safety-net capabilities; OWASP runtime controls; rework rate as stability signal | Human-defined release criteria; privileged tool invocations | Policy artifacts + telemetry + audit store | Reviewer saturation as an attack surface (OWASP ASI T10); provenance-neutral verification; instability tax as ROI line item | DORA data predates high-volume agents (extrapolated); 218A widely miscited (it's about model dev); several primaries **not fully fetchable** |
| **Day-2 ops loop (Azure SRE agent, PagerDuty, incident.io, Argo)** | Observe/detect → investigate → mitigate (two-class) → repair via ledger → reconcile/learn | Graduated, scope-declared: autonomy per response plan, never agent-global; Review mode default; OBO elevation | Pre-execution permission gates; progressive-delivery deterministic rollback; post-fix health checks; provenance walking | Novel mutations always approved; PR review the single human step in repair loop | IaC ledger canonical; fix-through-the-ledger | Two-class mitigation taxonomy (route by **reversibility**, not severity); drift-masking anti-pattern named by the vendor itself | Provenance-aware IR is aspirational, no standard; autonomous churn under-governed; agent memory unaudited; key MS quote sourced from **snippet, not full primary** |

### 2.2 Per-framework assessments

**Microsoft AI-led SDLC.** The most architecturally instructive vendor artifact: the deterministic-CI/CD stance is genuinely contrarian and correct (keep the actuator deterministic; put AI on sensing/planning), and the ops→dev loop is real plumbing verified in primary docs. But it is "AI-executed, human-governed", not AI-led; it ships no provenance framework, no loop circuit breaker, and its cited statistics are selectively favorable — the same Atlassian paper it cites shows AI review comments resolve at 38.7% vs humans' 44.45%, and the Qodo 55%→81% figure **could not be located in the public report**. The techcommunity article body itself resisted fetching (JS-rendered); the analysis rests on the digest verified component-by-component against GitHub/Microsoft Learn docs.

**AWS AI-DLC.** Best-in-corpus mechanism design at the elicitation layer (clarification-questions-as-files; adaptive stage selection; repo-resident audit trail) wrapped around the weakest enforcement story: the whole methodology is rules files interpreted by an LLM, and audit.md is written by the agent it audits. The Bedrock evidence is internally inconsistent across AWS's own posts (30 devs/18mo vs 40/1yr baseline; 76 days vs "five months") and commit velocity is the most gameable metric in this corpus.

**GitHub Spec Kit.** The constitution-with-gates-and-waiver-ledger is a control primitive worth stealing wholesale; the [NEEDS CLARIFICATION] token and /analyze//checklist tooling treat natural language as a testable object. The fatal gap is its own: nothing ever checks merged code against the spec, gates resolve to "document an exception", and its author calls it an experiment. SDD as shipped is a very good structured prompt pipeline, not a source-of-truth inversion.

**Anthropic practices + trends report.** The most transferable single idea in the research: define a check the agent can run before it writes code, and separate judge from builder structurally (fresh context, different weights). Also the most honest self-undercutting data point: 60% AI usage but 0–20% full delegation. Caveats stand: customer metrics are vendor-supplied and unaudited; the Vantor harness is a third party's interpretation, not Anthropic primary; the "100% of Anthropic code" meme is unsupported — calibrated figures are >80% of merged production lines. The trends PDF was recovered locally after a WebFetch failure, so its content here **is** primary-source.

**Kiro + specs.md.** EARS notation and steering inclusion modes are the portable steals; Böckeler's spec-first/spec-anchored/spec-as-source taxonomy (Fowler site) is the best evaluation lens in the corpus and predicts exactly which artifacts survive outside the IDE. Kiro's gates are conversational, its specs rot after ship, and specs.md's operator and relationship to AWS branding are **unidentified** — treat as secondary quality. One Kiro docs URL 404'd; EARS details reconstructed from surviving pages plus search corroboration.

**Open-source multi-agent corpus.** The load-bearing finding is negative: MAST (1,600+ annotated traces, κ=0.88) attributes ~37% of multi-agent failures to the multi-agent structure itself, and ChatDev's 85% executability collapses to 33.3% correctness. What survives: MetaGPT's typed artifact handoffs, BMAD's context-complete story files, ChatDev's communicative dehallucination — all adoptable without role theater. OpenHands demonstrates the counterfactual the industry converged on. Several fetches were partial (MAST percentages via corroborated snippets; MetaGPT paper abstract-level only).

**Academic synthesis (Bhati, Hymel).** Neither is peer-reviewed (single-author preprint; Crowdbotics-funded whitepaper), but both independently converge on the same autonomy model — human as verifier at per-phase gates, paired quality-agents as checksums — which raises confidence in that design point. Bhati's "economics of attention" and "human-agent responsibility mapping as an auditor-verifiable artifact" name the exact problems the three designs below wrestle with. V-Bounce's numbers should not be cited; its structural insight (verification-heavy V shape when implementation is free) should be.

**Enterprise consensus.** Four independent sources agree on the same boundary — agents propose, humans merge/deploy — which makes it a defensible doctrine baseline rather than one vendor's opinion. CodeRabbit's "verification tax" and Thoughtworks' feedforward/feedback harness framing are the durable contributions. The PwC survey (74 releases/yr, 96% defect reduction) is **unverifiable** — both primary URLs returned 403 — and is uncritically recycled by DronaHQ; treat as slideware until fetched.

**Standards layer.** Composes cleanly into stackable layers with almost no internal contradiction. Three findings are doctrine-grade: NIST's provenance-neutral stance (one strong gate, no two-tier AI/human regime); OWASP ASI T10 naming reviewer saturation as an attack surface; DORA's rework-rate move (robust to denominator inflation where CFR is not). Caveats: DORA 2025 data predates high-volume autonomous agents; SP 800-218A's contribution to governing agent-written code is essentially one sentence; several primaries (capabilities-model PDF, ASI PDF, EU AI Act text) were only partially fetchable.

**Day-2 operations loop.** The two-class mitigation taxonomy (deterministic pre-declared reversals may auto-execute; novel mutations always gate) and fix-through-the-ledger are the correct control shapes, and Azure's response-plan-scoped autonomy is the most concrete published permission model for an ops agent. Provenance-aware incident response is aspirational everywhere; the drift-masking quote from Microsoft's own material is sourced from a **search snippet plus corroborating posts**, not the unfetchable primary.

---

## 3. Doctrine invariant register

Consolidated, deduplicated invariants the SDLC design must honor. IDs are the working ids used by the council; each cites its home file. (The register below lists the load-bearing invariants explicitly; contiguous ranges of the same corpus are summarized where the designs cite them uniformly, with clauses mapping positionally to ids. delivery-corpus-24 was not carried into this register by the council's doctrine reader and is not cited by any design.)

### 3.1 AI/ML and agentic systems — [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md), [../patterns/agentic-loop-design.md](../patterns/agentic-loop-design.md), [../patterns/ai-adoption-controls.md](../patterns/ai-adoption-controls.md)

| Id | Invariant |
|---|---|
| ai-corpus-1 | **Versioned repo state is the sole authoritative record**; model weights, indexes, transcripts are replaceable derivatives. |
| ai-corpus-2 / 3 | Capability **tiers A–D** and an orthogonal **materiality axis**; controls scale with the max of both. |
| ai-corpus-4 | **Governance precedes scale**: inventory before expansion; quarterly reconciliation; cheap sanctioned registration beats punitive shadow-agent detection. |
| ai-corpus-5 | **Effective challenge** (SR 11-7 shape): independent second line with incentives, competence, and influence to block; self-assessment is not challenge. |
| ai-corpus-6 | **Agents propose, CI proves, humans approve**; same merge bar regardless of author; high-risk areas keep explicit review. |
| ai-corpus-7 | **Security-critical scope** (authn/authz, secrets/crypto, tenancy, CI/deploy privilege, internet-exposed boundaries) is proposal-only until human sign-off — permanently. |
| ai-corpus-8 | Person-affecting systems: declared oversight mode, fallback, override affordance, contest path, **tested** decision-log reconstruction. |
| ai-corpus-9 | Agent plan state, active criteria, and reasoning **observable in real time**. |
| ai-corpus-10 | **Verifiability gate**: only resettable/efficient/rewardable tasks are delegable; otherwise human task with AI assistance. |
| ai-corpus-11 | **ISC** (binary, testable, state-oriented criteria) before any tool call; mandatory VERIFY scoring per criterion. |
| ai-corpus-12 | **External verifier required**; the cell cannot grade its own work; self-certified success is inadmissible. |
| ai-corpus-13 | Bounded loops: **iteration caps and budget stops** mandatory. |
| ai-corpus-14 | **Autonomy slider** (approve-every-action → … → deployed-silently) earned on evidence, demoted automatically on regression/incident; asymmetric. |
| ai-corpus-15 | **Simplest-solution escalation**: deterministic workflow before agent; agents only on demonstrated need. |
| ai-corpus-16 | **Lethal trifecta** (untrusted content + private data + write tools) → dual-path architecture with deterministic taint enforcement. |
| ai-corpus-17 | Context engineering first-class; persisted memory reopens **Tier-B retrieval governance**; verified_only admission. |
| ai-corpus-18 | Tool surfaces are **governed contracts**; tool changes are breaking changes. |
| ai-corpus-19 | Council/vote outcomes **never substitute** for CI or human approval on high-risk change. |
| ai-corpus-20 | Golden sets regression-gated; **embedding/model change = migration**. |
| ai-corpus-21 | Harm-surface test matrix; **continuous** drift monitoring against launch baseline, not change-triggered only. |
| ai-corpus-22 | **Provider continuity**: named substitute, portable evals; a silent model upgrade is a change. |
| ai-corpus-23 | Tenant/sensitivity isolation on retrieval and memory stores. |
| ai-corpus-24 | Correlation ids, actor, model/tool versions on all automation logs; **spend metering**. |
| ai-corpus-25 | Acceptable-use artifact + role-based literacy matrix. |
| ai-corpus-26 | Episode learning artifacts are **governed engineering artifacts**, not conversation residue. |

### 3.2 Merge path, review, delivery — [../principles/merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md) (canonical for merge-path conflicts until harmonised), [../patterns/code-review-and-change-approval.md](../patterns/code-review-and-change-approval.md), [../principles/testing-strategy.md](../principles/testing-strategy.md), [../patterns/feature-flag-lifecycle.md](../patterns/feature-flag-lifecycle.md), [../patterns/gitops-and-declarative-operations.md](../patterns/gitops-and-declarative-operations.md), [../principles/secure-development-lifecycle.md](../principles/secure-development-lifecycle.md), [../principles/threat-modeling-stride-lite.md](../principles/threat-modeling-stride-lite.md)

| Id | Invariant |
|---|---|
| delivery-corpus-1 | Peer review default; **four eyes must not be the same person twice**. |
| delivery-corpus-2 | PR descriptions are load-bearing. |
| delivery-corpus-3 | Approval = **"willing to be wrong with the author"** — a two-human risk-sharing contract. |
| delivery-corpus-4 / 15 | Blockers resolved or carried as **time-bounded exceptions** with owner + expiry + compensating control. |
| delivery-corpus-5 | Review latency measured; chronic delay fixed **structurally**, not by exhortation. |
| delivery-corpus-6 / 21 | **Proportional, risk-tiered** review depth; adversarial CI Tiers 0–3. |
| delivery-corpus-7 | Agent-PR disclosure; **a human author must be able to explain and own the change**. |
| delivery-corpus-8 | Approver must be able to **defend the behavior under incident pressure**. |
| delivery-corpus-9 | Escalation ladder / break-glass with retrospective. |
| delivery-corpus-10 / 11 / 12 | Server-enforced protected branches; **pipeline definitions in the same trust class as app code**; gates binding, never advisory. |
| delivery-corpus-13 | **Evidence bundle** per change: revision, workflow identity, artifacts, approvals, policy version. |
| delivery-corpus-14 / 17 / 33 | SBOM/provenance as release inputs; promotion **re-evaluates vulnerability state** at promote time; immutable digest-pinned inputs. |
| delivery-corpus-16 | Adversarial/abuse-case evidence for security-relevant scope. |
| delivery-corpus-18–20 | Test pyramid; contract tests pre-merge; **flaky tests are defects**. |
| delivery-corpus-22 | Mutation/property testing (currently optional). |
| delivery-corpus-23 | STRIDE-lite threat assumptions at design time. |
| delivery-corpus-25 | Root-cause classing (patch / process-control / architecture); recurring classes mandate structural work. |
| delivery-corpus-26–31 | Flag taxonomy/FSM/metadata contract; data-gated progressive promotion; **only humans change flag state** (29); model/prompt changes ship flagged with tested kill switch (31). |
| delivery-corpus-32 / 34 / 35 | GitOps declared-state channel; drift **detected and proposed, never auto-fixed**; control-plane changes are high-impact review. |

### 3.3 Organization, measurement, platform — [../principles/measurement-and-dora.md](../principles/measurement-and-dora.md), [../patterns/engineering-controls-governance-program.md](../patterns/engineering-controls-governance-program.md), [../principles/platform-engineering.md](../principles/platform-engineering.md), [../patterns/platform-as-product-and-golden-paths.md](../patterns/platform-as-product-and-golden-paths.md), [../principles/cost-and-finops.md](../principles/cost-and-finops.md), [../patterns/doctrine-versioning-and-consumer-compatibility.md](../patterns/doctrine-versioning-and-consumer-compatibility.md), [../principles/reliability-slo-incidents.md](../principles/reliability-slo-incidents.md), [../patterns/chaos-engineering-and-game-days.md](../patterns/chaos-engineering-and-game-days.md)

| Id | Invariant |
|---|---|
| org-corpus-1–3 | Stable metric definitions (unit of change defined once); **no individual productivity metrics**; velocity always paired with vulnerability-response SLIs. |
| org-corpus-4 | Controls as a governed programme keyed to criticality. |
| org-corpus-5 | Exception records with stable ids, a named owner, and expiry. |
| org-corpus-6 | **Control calibration** — a gate must be proven to detect what it claims to detect. |
| org-corpus-7 | Org-controlled evidence retention (links + hashes, never screenshots). |
| org-corpus-8 | **Detection without enforcement is failure.** |
| org-corpus-9–16 | Golden paths; service catalog as SoR; no silent snowflakes; repeated exceptions re-absorbed into the path; platform API contracts; Team Topologies roles. |
| org-corpus-17–19 | Cost as an NFR; unit economics = **cost per verified outcome**; spend anomaly alerting. |
| org-corpus-20 | Per-run budgets and circuit breakers. |
| org-corpus-21 | Doctrine versions like software: **change classes** on every doctrine change. |
| org-corpus-22 | Consumer pinning of doctrine versions. |
| org-corpus-23 | **Deprecation-before-removal.** |
| org-corpus-24 | SLOs on user journeys. |
| org-corpus-25 | Error-budget policy. |
| org-corpus-26 | Blameless postmortems feeding metrics. |
| org-corpus-27 | **Third-party model loss is your incident.** |
| org-corpus-28 | Rehearsed failure (game days). |

### 3.4 Execution substrate — [../patterns/run-contracts.md](../patterns/run-contracts.md), [../patterns/verifier-packs.md](../patterns/verifier-packs.md), [../patterns/anti-confabulation-priming.md](../patterns/anti-confabulation-priming.md), [../principles/state-machines-and-workflows.md](../principles/state-machines-and-workflows.md), [../principles/timeless-principles-and-tooling.md](../principles/timeless-principles-and-tooling.md)

| Id | Invariant |
|---|---|
| envelope-1–6 | Every agent execution inside a typed **run-contract envelope**; trigger→instantiate→execute→verify→emit; sha256 fingerprint; named host-registered hooks; **no mid-run self-editing of contracts**; no ambient affordance. |
| authority-1 | **Typed denial** is the default authority posture on all axes. |
| outputs-1 | `outputs.required` non-empty always — even research runs emit artifacts. |
| secrets-1 | No secret values in agent context. |
| validation-1 | Contract validation (schema, capability closure, authority coherence, verifier-pack existence, fingerprint stability) as **binding CI**. |
| verification-corpus-1–7 | Every skill ships a sibling **verifier pack**; verdicts fail-loud/no-skip; **inconclusive is louder than failure**; fixed verifier kinds; stub packs are defects; memory admission verified_only; a passing pack is **necessary, never sufficient** for high blast radius. |
| priming-1–5 | Anti-confabulation priming auto-injected for build-class runs (hash-verified); self-claim ledgers with falsifiers and non-zero prediction buffer; flagged gaps cost less than hidden ones; prompt never substitutes for structure; hashed prompt artifacts version via ADR. |
| priming-6 | **Model-conditional, evidence-gated mandates.** |
| workflow-1–7 | Lifecycle as explicit FSM; one commitment story per transition; transitions mapped to stable event types; reconciliation and projection; saga/compensation for multi-step; **dwell caps on every wait state**; human decisions as idempotent tokens in tool-assisted queues. |
| meta-1 | Vendor-agnostic principles/tooling split. |
| meta-2 | **Surface contracts.** |
| meta-3 | Standards adoption without mandating a full stack. |
| meta-4 | **Doctrine change only via human-reviewed PR + ADR.** |
| meta-5 | SSDF crosswalk retained. |

### 3.5 Tension list — where current doctrine assumes human-authored code

These are the points every design had to extend, reconcile, or supersede. They are the raw material for the session-2 supersession register.

1. **ai-corpus-6's flat "humans approve"** vs agent volume: at 10× PRs, universal human approval either queues or rubber-stamps. The corpus itself hedges ("high-risk areas keep explicit review") but never defines the routing scheme that hedge implies.
2. **delivery-corpus-3 accountability object**: "willing to be wrong with the author" has no clean referent when the author is a fleet.
3. **delivery-corpus-7 disclosure polarity**: "flag the AI-generated parts" is noise when generation is the default; the informative disclosure inverts to the human-touched surface. Its second clause (human explains and owns) is separately load-bearing and must not be silently dropped.
4. **delivery-corpus-22's optional mutation testing**: the pyramid's author/test independence assumption is dead when one actor writes both code and tests.
5. **delivery-corpus-29 humans-only flag state**: at agent-era incident tempo, a human-only kill-switch actuator is itself a reliability risk for pre-declared, tested, metric-gated reversals.
6. **ai-corpus-14 vs the merge gate**: the corpus never bridges earned runtime autonomy to review/merge depth — the slider and the static bar are unconnected.
7. **ai-corpus-2/3 tiers are product-facing**: the authoring fleet's own inventory entry and materiality classification are unresolved (all three designs rule it in-scope, Tier D, inherited max materiality).
8. **ai-corpus-1 SoR scope**: ISC records, verifier verdicts, learnings, and run audits are behavior-driving artifacts; unadmitted, they become shadow policy.
9. **delivery-corpus-13 provenance gap**: the evidence taxonomy has no agent identity, model version, contract fingerprint, or verifier-verdict fields.
10. **Run-contracts v1 declared gaps**: no per-run budget (closable via org-corpus-20), no DAG composition/cross-contract atomicity, and an undefined "higher-level compiler" for agent-authored contracts.
11. **Effective challenge (ai-corpus-5)** assumes human challengers; no test exists for when machine-briefed challenge stops being independent.
12. **Review capacity is unpriced**: no doctrine treats human attention as a saturable, attackable control with an SLO (OWASP ASI T10 does).
13. **ISC/criteria quality is unguarded**: verifier packs govern code, nothing governs the criteria themselves when agents author them.

---

## 4. The three candidate designs

All three share the substrate (run contracts, verifier packs, ISC, priming, evidence bundles) and the Microsoft-derived **autonomy sandwich** (agentic edges, deterministic actuator core). They differ in frame: what the lifecycle is *for*.

---

### 4.1 Design A — **Ledger-and-Gate: Verification-Native SDLC (VN-SDLC v1)**

**Frame.** Authoring is cheap; **justified trust is the scarce resource**. Every phase exists to cheapen or strengthen downstream verification. Human review migrates from line-reading to evidence-judging, risk-routed into three lanes; the merge bar is provenance-neutral (NIST 800-218A stance) and defined by evidence, which is identical for all authors — earned trust moves **attention allocation, never gates**.

**Summary.** Seven phases; agents author inside contract envelopes; every change carries a content-addressed evidence bundle from spec fingerprint to deploy digest. Three declared doctrine changes: ai-corpus-6 extended into three-lane routing; delivery-corpus-7 polarity inverted; delivery-corpus-29 boundedly superseded for pre-declared deterministic kill-switch actuation. Four-stage migration with pre-committed rollback triggers ("evidence production before gate relaxation").

| Phase | Purpose | Human gate |
|---|---|---|
| 1. Intent/Spec | ISC-shaped criteria before work exists; EARS lint; clarification ledger; human-owned per ai-corpus-10 | Intent owner approves; second-line challenge on high-materiality specs |
| 2. Plan | Compile spec into context-complete tasks each bound to a validated run contract; binding constitutional gates | Human approves the **contract set**; security tasks pre-flagged proposal-only |
| 3. Build | Envelope execution, stop-gate ladder, evidence-over-assertion; no human in-loop | Escalation-only (BLOCKED, fail_loud) |
| 4. Review | Three lanes: L1 line-review (Tier 0), L2 evidence-review (default), L3 sampled (earned, low-materiality); independent different-model judge, advisory + severity rules | Lane-routed; approver in L2 owns the verification regime |
| 5. Integrate/Deploy | Deterministic core; zero agent discretion; attestation chain spec→digest | Rule-based gates; human promotion at high materiality |
| 6. Operate | Two-class mitigation; fix-through-the-ledger; provenance-aware investigation; loop circuit breakers | Class-(b) mitigations; repair PRs re-enter Phase 4 |
| 7. Learn | Learnings distillation (80-line cap), judge calibration, trust ledgers; agents propose, humans ratify | All normative change human ADR-gated |

**What critics confirmed as strong.** The frame itself (authoring-cheap/trust-scarce) and the deterministic deploy core survive both critiques intact. The governance critique called its citation hygiene the best the critic had reviewed against this corpus — most of ~60 citations check out, and it correctly resolves several tensions the corpus itself names (fleet in inventory; provenance extension of delivery-corpus-13; budget gap closed via org-corpus-20; FSM-as-composition honestly flagged unproven). Also confirmed: pinned security floors; evidence-in-PR discipline adoptable standalone; the mutation-testing tightening; retiring count-denominated metrics; the bounded delivery-corpus-29 supersession ("correct call"); the **slider-moves-attention-never-gates** reconciliation ("genuinely elegant doctrine work"); reviewer-saturation back-pressure; and an unusually honest open-questions list.

**What critics broke.**

| Sev | Issue | Proposed fix |
|---|---|---|
| **Blocker** | **Stage 1 is a valley of pain**: full evidence machinery mandated while humans still line-review everything → teams fake the ceremony, poisoning the very calibration data the advance triggers need | Give Stage 1 an immediate selfish payoff (bundles auto-generate PR descriptions, measured review-time cut in sprint 1); pilot on 2–3 repos; ceremony-quality audit before triggers count |
| **Blocker** | **Brownfield unaddressed**: provenance roots at a spec fingerprint but ~95% of a real estate has no spec; "evidence coverage ~100%" generates findings on nearly every merge | Legacy on-ramp: characterization tests as substitute roots, spec-on-touch, an explicit "unspecified-legacy" provenance class, coverage ratchet not 100% target |
| **Blocker** | **Provenance-neutrality forks for human authors**: only the agent harness cheaply produces the demanded evidence; humans get a waiver class or launder changes through agents | Explicit human-authored evidence-equivalence table per lane + 2 AM break-glass path with retroactive evidence, tested before Stage 1 |
| **Blocker** (governance) | **Lane 3 removes "humans approve" without declaring supersession, and no human owns unsampled Lane-3 merges** — a deterministic gate cannot be "willing to be wrong with" anyone | Relabel as bounded normative replacement with ADR; make Lane-3 eligibility a standing org-corpus-5 risk acceptance signed by the named first-line owner, with expiry and sampling as the compensating control |
| **Blocker** (governance) | **Compounded sampling creates a fully agent-closed loop**: agent-proposed contracts (sampled countersign) × Lane-3 merges (sampled review) → changes where no human touched standard-setting or standard-checking | Forbid the intersection structurally: no Lane 3 without human-countersigned contract set — at least one human touchpoint per change; seed weak-verifier contracts into calibration |
| Major | Tier-0 scope classification is soft and gameable (planner-proposed labels; path patterns miss semantic auth changes) | Deterministic over-inclusive classifier (path + symbol + reachability), server-enforced; misses are Sev-high control failures |
| Major | Lane-2 evidence review degrades to green-checkmark clicking; throttle knobs are org-tunable | Active-act approval (identify weakest evidence; seeded challenge bundles); throttle parameters ADR-gated |
| Major | Calibration apparatus is an unfunded standing workload; stale golden PRs silently convert Lane 3 to auto-merge | Named owning team + headcount; calibration assets carry expiry; **fail closed** on stale calibration |
| Major | Inconclusive-flood alarm fatigue at estate scale | Verifier flake budgets, quarantine with owner/deadline, split infra-inconclusive from semantic-inconclusive |
| Major | No degraded mode for judge unavailability/regression | Pre-declared substitute per org-corpus-27, game-day rehearsed, alarm on judge-skip rate |
| Major (governance) | delivery-corpus-7's explain-and-own clause silently dropped in L2/L3; SoD across phases unspecified; citation gaps (ai-corpus-9, 18, 21, 23, 20-on-memory) | Name a tested "incident explainer" role per change; role-distinctness constraints enforced via platform config; add the missing invariants to phase evidence requirements |

---

### 4.2 Design B — **Intent-Ledger SDLC (IL-SDLC)**

**Frame.** **Spec-as-system-of-record**: the maintained assets are intent artifacts (constitution, per-module EARS specs, eval suites born with requirements); code is a pinned, regenerable build output. Drift between spec and shipped code is a measured, triaged defect — the GitOps drift discipline lifted one level up. Spec-as-source is **earned per module** (Böckeler's spec-first → spec-anchored → spec-as-source taxonomy), never declared globally; legacy estates may honestly stay spec-anchored forever.

**Summary.** Eight phases (0–7) in autonomy-sandwich shape. Four verification tiers V0–V3 computed from change class × materiality; a **drift oracle** binds spec↔code conformance into CI as a gate; every patch without a spec delta opens a time-bounded **spec-debt** item; sealed modules regenerate with regeneration manifests. Declares its supersessions explicitly (ai-corpus-6 partially; delivery-corpus-1/3 at V2/V3; delivery-corpus-7 polarity; delivery-corpus-18/22 tightened; delivery-corpus-29 narrowly) and deliberately extends ai-corpus-14 to move the verification tier itself — bridging the corpus's named gap.

| Phase | Purpose | Human gate |
|---|---|---|
| 0. Constitution & standing policy | Non-negotiables, fleet inventory, contract/pack catalogs before any generation | Leadership; constitution edits permanently human |
| 1. Intent & specification | EARS clauses + paired tests at authoring time; clarification files; spec deltas for brownfield | Intent owner line-reviews spec; second-line challenge high materiality |
| 2. Plan & compile | Context-complete tasks + contracts; Phase −1 gates with waiver ledger; regenerate-vs-patch ruling per module | Plan shape, waivers, any V-tier downgrade |
| 3. Build | Regenerate (sealed) or governed patch (+ spec-debt obligation); harnessed loop | Escalation-only |
| 4. Verify & review | V0 line / V1 evidence / V2 sampled / V3 auto; different-model judge; drift oracle binding; mandatory mutation gates | Tier-routed; fail_loud/inconclusive always human |
| 5. Integrate & deploy | Deterministic core; flags + kill switches for model changes | Environment approvals; error budget actuates autonomy |
| 6. Operate | Two-class mitigation; typed incident→spec issues; circuit breakers | Novel mutations; response-plan promotion on evidence |
| 7. Learn & reconcile | Spec-debt burn-down, evaluator calibration, production-to-spec feedback | All normative change human ADR-gated |

**What critics confirmed as strong.** The governance critique rated its **supersession discipline the best reviewed** — every displaced invariant declared with rationale drawn from the corpus's own tension sections, "exactly what those tensions demanded." The three-strata SoR correctly extends ai-corpus-1 and closes the shadow-policy gap; the Tier-D fleet ruling is clean; declared hard floors are faithful; envelope/verifier/priming citations all check out; error-budget-as-autonomy-actuator and reviewer-saturation-as-attack-surface are "genuine doctrinal contributions." The practicality critique confirmed the deterministic deploy core as "the strongest single decision," the V0 floors, the envelope substrate ("worth building even if the spec-as-source frame never fully lands"), the mutation-gate supersession, and the per-module maturity taxonomy's honesty.

**What critics broke.**

| Sev | Issue | Proposed fix |
|---|---|---|
| **Blocker** | **The review-capacity relief never materializes under its own rules**: model upgrades reset per-module earned autonomy (ai-corpus-22/priming-6), so at quarterly model cadence modules perpetually re-earn and nearly all volume lands at V1/V0 — where V1 degrades to checkmark clicking. The design's economic premise is refuted by its own reset rule | Design **partial-credit evidence transfer** across model versions (portable recertification suite restoring tier in days); instrument V1 with decision-time floors and sampled deep-reads; no V2 anywhere until sampling rate k is empirically sized |
| **Blocker** | **Spec-debt economics guarantee a waiver mill**: patching is always locally cheaper; the debt queue grows, expiries get bulk-extended, the drift oracle gets waivered into telemetry — the MDA/executable-UML fate | Patch pays at merge time (spec delta ships in the same PR); "reconcile later" reserved for declared incidents under a hard org-level **debt budget** that blocks new debt creation; leadership-owned created:retired tripwire |
| **Blocker** | **Saturation throttle will be politically overridden** at first deadline collision; no pre-negotiated contract, no override cost | Formal break-glass: named executive owner, time-bound, mandatory 100% retrospective audit of the override window, reported alongside SLO breaches. If leadership won't sign in Phase 0, the control does not exist |
| **Blocker** (governance) | **The V-tier routing oracle is undesigned**: nothing specifies what computes change class or how it is calibrated; agent code can move auth/tenancy behavior without touching labeled paths → V2 auto-merge; converts the declared ai-corpus-6 supersession into an **undeclared ai-corpus-7 supersession** in practice | Classifier as a first-class doctrine-grade control: deterministic, conservative-by-default (ambiguous routes UP), semantic detectors + path ownership, itself V0, calibrated with seeded misrouting PRs before V2 enables anywhere |
| Major (governance) | No **materiality ceiling**: high-materiality business logic outside ai-corpus-7 classes can earn V2 — an undeclared erosion of ai-corpus-5's blocking challenge | Cap high-materiality modules at V1 regardless of earned autonomy; state as a hard floor |
| Major (governance) | **V2 accountability does not terminate at a human** per change; open-questions honesty is not a compensating control | V2 = standing, signed, scoped, **expiring** pre-approval by the module's named first-line owner (org-corpus-5 mechanics) |
| Major (governance) | delivery-corpus-7's explain-and-own clause undeclared-dropped at V2/V3; sampling rate k shipped uncalibrated | Declare both clause dispositions; V2 structurally defined but **gated off** until a seeded-defect campaign fixes k with confidence bounds |
| Major | Inconclusive-louder-than-failure + flaky evals floods the queue; sealed modules are hostile at 3 AM (regeneration destroys bisectability; sealing ratchets down after first break-glass); spec review is the new rubber stamp (the normative surface is not actually 2 pages); eval suite carries quadruple duty and Goodharts by default; partial adoption / cross-module changes are the worst-supported common case | Flake budgets + quarantine; regeneration semantic-changelog + 3 AM forensics drill as sealing precondition + re-seal fast path; spec-review instrumentation + spec-mutation testing; independent held-out eval reserve never visible to builders; define the minimum viable subset + a change-set primitive above run contracts |
| Minor | delivery-corpus-23 uncited (threat assumptions absent from the spec schema); unsealed modules create the competing-SoT condition delivery-corpus-34 prohibits; ai-corpus-21 standing drift monitoring only half-implemented | Add STRIDE-lite section to spec schema; declare per-state precedence (unsealed: code wins; sealed: spec wins); add standing model-drift monitors + judge known-answer calibration before load-bearing use |

---

### 4.3 Design C — **Fleet Charter SDLC (FC-SDLC)**

**Frame.** **SDLC as agent-workforce management**: agents are staff. The capability gate is the hiring bar, the autonomy slider is delegation policy, review is supervision, evals are performance review, model deprecation is offboarding, the ADR-0023 inventory is the org chart. The lifecycle is a control plane letting a small number of accountable humans direct a large agent workforce. Merge bar constant for all authors; earned trust moves **who supplies the verification evidence and at what depth a human inspects it**.

**Summary.** Eight phases: a standing **Phase 0 workforce administration** (roster = inventory; capability certificates; typed-denial access; offboarding = deprecation with game days) plus intent → plan/staffing → delegated build → supervision/challenge → promotion → shift operations → performance review/doctrine evolution. Three review currencies (line / evidence / sampling) routed at **plan time**; three declared supersessions (ai-corpus-6 sampling lanes; delivery-corpus-7 polarity; delivery-corpus-29 narrow reversion carve-out); five-stage migration with per-stage triggers and a standing left-ratchet rollback rule; metrics denominated in **work orders**, not PRs.

| Phase | Purpose | Human gate |
|---|---|---|
| 0. Workforce administration | Hiring bar (harm-surface evals vs golden sets), roster/org chart, access control, offboarding | Lane owner countersigns certificates; roster mutations human-only PRs |
| 1. Intent & work-order authoring | Spec + ISC + tier/materiality + threat assumptions; verifiability-gate routing; ISC lint binding | Intent owner; oversight-mode design at spec time for person-affecting scope |
| 2. Planning & staffing | Context-complete briefs, contracts with budgets, review depth decided **before code exists** | Lead approves plan, process shape, staffing matrix, waivers |
| 3. Delegated build | Envelope + stop-gate ladder + evidence-over-assertion; human-touch disclosure manifest | Structural limits substitute; security paths auto-reroute |
| 4. Supervision & challenge | Binding gates → different-model judge (severity rules, BLOCKED) → risk-routed human depth; mandatory mutation gates in agent lanes | Line review unearnable-away for Tier-0; approver + lane owner jointly own |
| 5. Promotion | Deterministic core; promote-time vuln re-check; per-PR sandboxes | High-materiality production promotion always human |
| 6. Shift operations | Two-class mitigation; response-plan-scoped autonomy; repair via ledger with rate limits, dedup, oscillation breakers; error budget actuates on lane autonomy | Novel mutations; pattern promotion = delegation-policy PR |
| 7. Performance review & doctrine evolution | Per-lane dossiers; asymmetric re-grading; learnings distillation; accepted-justification injection | Independent human (not lane owner) approves re-grades; all doctrine via ADR |

**What critics confirmed as strong.** Both critiques confirmed the workforce metaphor maps onto corpus primitives **without distorting them**: the roster-as-inventory ruling resolves the fleet tension "exactly as the constraints demand"; the merge-bar-constant / inspection-depth-variable resolution is "the strongest single move in the design." Also confirmed: deterministic actuator core survives every attack; path-based server-enforced permanent floors; asymmetric lane-scoped autonomy; **"throttle dispatch, don't widen autonomy" called "the single best sentence in the design"**; ops-loop circuit breakers close a real industry gap; work-order-denominated metrics genuinely survive 10× inflation; instrumentation-before-delegation ordering ("provenance is unrecoverable retroactively" is the correct reason); honest open-questions register; ai-corpus-10 honestly conceding the front of the lifecycle to humans.

**What critics broke.**

| Sev | Issue | Proposed fix |
|---|---|---|
| **Blocker** | **Self-declared materiality is the master routing key and the cheapest gaming vector**: review depth, sampling eligibility, and autonomy all key off a stamp declared by the people under deadline pressure; nothing audits the declaration | Partially machine-derived materiality: path-based floors auto-escalate regardless of stamp; post-merge reconciliation of declared vs actual blast radius; under-declaration treated with shadow-agent weight; sample-audit the declarations themselves |
| **Blocker** | **The attention budget is asserted, never balanced**: humans keep ~15 duty classes; no arithmetic shows supervision-hours × 10× volume fits senior-human capacity; the bottleneck relocates to Phase 1 (spec ceremony), which has no sampling escape valve → template-copied specs poison everything downstream | Publish the budget model as an artifact (hours per work order by risk class, measured in Stage 1); throttle **intake** as well as review; spec-quality calibration (deliberately underspecified injected work orders) |
| **Blocker** | **Evidence review is structurally rubber-stamp-shaped**: a human agreeing with machine summaries of machine work at speed; calibration injection specified only for sampling lanes, never for evidence reviewers | Extend calibration to evidence-review lanes: green-bundle/wrong-change test bundles; reviewer detection rate as a control-health SLI; failing lanes demote to line review |
| **Blocker** (governance) | **The design self-authorizes its three supersessions** — never routed through meta-4 / org-corpus-21 change classes / org-corpus-23 deprecation; the canonical merge-path file "wins conflicts until harmonised" and must be harmonised, not overridden by a design doc | Gate Stage 3 on landed doctrine PRs: ADR per supersession, "normative replacement" class, deprecation markers in superseded files, version bump consumers can pin |
| **Blocker** (governance) | **No human owns unsampled sampling-lane merges**, and delivery-corpus-1 (four eyes) + delivery-corpus-7 (explain-and-own) are silently abandoned there while the citation list claims they're upheld | Lane owner solely and personally owns every unsampled merge, recorded per-merge in the evidence bundle; extend the declared supersessions to cover both clauses |
| Major (governance) | **Materiality is the wrong routing key for regulatory scope**: SOX/PCI/EU-DORA change control attaches to systems, not per-change materiality; migration triggers contain no regulatory exclusion | Add an orthogonal regulatory-scope flag; hard-pin regulated paths to evidence/line review; make the exclusion an explicit Stage-4 entry trigger |
| Major (governance) | **Calibration injection merges known defects into the protected baseline** (post-hoc sampling means the test PR lands on trunk); org-corpus-6 calibrates pre-merge gates, not merged code | Quarantine calibration: shadow branch or server-enforced promotion-blocking marker + auto-revert; calibration events in the exception ledger |
| Major (governance) | **Ops loop reopens the lethal trifecta** (attacker-controllable log content → agent-authored work orders auto-assigned to build lanes) and may bypass the Phase-1 human gate | Dual-path/taint architecture for ops agents; repair work orders are drafts requiring the same intent-owner approval as any spec |
| Major (governance) | **The fleet control plane audits itself**: platform team is first line, control author, and calibrator — an SR 11-7 SoD finding against a self-declared max-materiality system | Independent second-line challenger with block authority over stage promotions and control-plane changes; calibration audit outside the platform team |
| Major | Different-model judge doubles provider-outage surface and invites a retry lottery; migration triggers statistically unmeasurable in realistic quarters; verifier packs and capability certificates rot on model churn; legacy estates can't clear the verifiability gate while fixed platform costs accrue; injection programs decay and get fingerprinted; throttle set-points sit with the people they constrain | Judge as Tier-0 dependency (substitute + game day + rerun caps + flip-rate metric); ADR-gated stage promotion with an explicit "promoting on risk acceptance" branch + fast leading indicators; pack-diff-or-assertion CI on skill change + certificate TTLs that ratchet autonomy left on expiry (degrade loudly); per-lane estate-readiness preconditions + lane-scoped triggers; injector health SLI (no calibration → no sampling) + defects sourced from anonymized real escapes; throttle set-point changes ADR-gated with renewal-rate alarms |
| Minor | ai-corpus-14 mis-cited as authority for moving review depth (the corpus explicitly never bridges this); judge verdicts unreproducible after model deprecation; 3 AM accountability decays with per-line familiarity; mutation gates get scoped into irrelevance | Rest sampling entirely on the declared ai-corpus-6 supersession; judges/verifiers are roster members with their own golden sets retained; incident-navigability evidence as a promotion criterion; platform-owned versioned high-risk module list + diff-incremental mutation |

---

## 5. Convergence analysis

### 5.1 What all three designs agree on, regardless of frame

These survived three independent framings **and** six adversarial critiques, which makes them the likely doctrine-grade invariants of the AI-native SDLC:

1. **Deterministic actuator core / agentic edges.** Agents never merge, deploy, or exercise discretionary flag changes; CI/CD is zero-agent-discretion at every trust level. Confirmed by every critique as the control-theoretically correct placement of a stochastic component. (Extends ai-corpus-6/15, delivery-corpus-10/12/33.)
2. **Pinned, unearnable security floors.** ai-corpus-7 scope stays proposal-only-with-human-line-review forever; person-affecting floors per ai-corpus-8; intent/spec and doctrine authorship permanently human per ai-corpus-10 and meta-4. No design tried to earn these away; both critique lenses treated any classifier that could leak this scope as the top attack.
3. **The execution substrate is settled.** Run-contract envelopes with typed denial, sibling verifier packs, ISC-before-tool-call with mandatory external VERIFY, anti-confab priming, per-run budgets (closing the v1 gap via org-corpus-20), and the workflow-FSM binding of verdicts to committed transitions. All three built on it identically; no critique attacked the substrate itself.
4. **Risk-routed review depth replaces flat per-diff approval — via a declared supersession of ai-corpus-6.** All three converge on the same three-band shape (line review / evidence review / audited sampling) and on the same justification (a saturated universal gate is a fake control; OWASP ASI T10). Both governance critiques converge on the same two repair conditions: the supersession must go through the doctrine's own change protocol (ADR, change class, deprecation markers, harmonising the canonical merge-path file), and **a named human must own every unsampled merge** as a standing, expiring, signed risk acceptance.
5. **Evidence bundle extension with agent provenance.** Contract fingerprint, model identity, verifier verdicts, judge-report hash added to delivery-corpus-13; retention per org-corpus-7. Unanimous, uncontested.
6. **Disclosure polarity inversion** (delivery-corpus-7): disclose the human-touched surface. Unanimous — with the unanimous critique correction that the invariant's *explain-and-own* clause must be explicitly re-homed (a named, tested incident-explainer role), not silently dropped.
7. **Mandatory mutation/property gates where one actor class authors code and tests** (tightening delivery-corpus-22). Unanimous; critiques only added anti-scope-shrink guards.
8. **Bounded supersession of delivery-corpus-29**: pre-declared, tested, metric-gated deterministic reversion to a flag's safe default may auto-execute; forward/discretionary flag changes remain human-only. Unanimous, and route-by-reversibility (the day-2 two-class taxonomy) is the shared underlying principle.
9. **Human attention is a budgeted, saturable control**: saturation throttles agent **dispatch** rather than widening autonomy or degrading review. Unanimous in mechanism; unanimous in critique that the set-points must be ADR-gated and the override must be a formal break-glass with compensating controls, or the control is theater.
10. **Metrics that survive 10× volume**: rework rate primary; lead time re-anchored intent→verified-outcome; count-denominated metrics (PR/commit/deploy counts, raw coverage) retired as quality proxies; no individual or per-agent leaderboards (org-corpus-2); agent telemetry never feeds worker evaluation (EU AI Act Annex III trap).
11. **Autonomy is lane/task-class-scoped, earned slowly, revoked fast**, and ops autonomy attaches to pre-declared response plans, never to agents globally. Error-budget burn actuates on autonomy (extension of org-corpus-25).
12. **Fix-through-the-ledger with circuit breakers** on the closed ops loop (rate limits, dedup, oscillation detection) — closing the gap the Microsoft loop leaves open.
13. **The authoring fleet is in the ADR-0023 inventory** as a Tier-D system with materiality inherited from the max blast radius of what it can modify.
14. **Migration discipline**: instrument before delegating; calibration (org-corpus-6) before any gate relaxation; pre-committed rollback triggers; never advance on calendar or enthusiasm.
15. **Shared unsolved problems, honestly held**: ISC/criteria quality is the new unguarded surface; judge calibration is the least-calibrated component of the layer meant to replace human review; provenance attestation has no cross-vendor standard; model churn vs earned-evidence economics; the human verifier skill pipeline.

### 5.2 Where they genuinely diverge

| # | Divergence | VN-SDLC | IL-SDLC | FC-SDLC | Evidence that would settle it |
|---|---|---|---|---|---|
| 1 | **System of record** | Code canonical; specs/ISC as governed inputs | Spec stratum normative; code a derived, regenerable output (per-module, earned) | Code canonical; work orders as the unit of intent | IL's own critique supplies the test: measure spec-debt created:retired ratio, drift-oracle waiver rate, and regeneration economics on a pilot module. If spec-anchored is the empirical steady state (as the critic predicts), spec-as-source becomes an optional per-module overlay, not the frame |
| 2 | **Does earned trust move the verification tier?** | No — slider moves attention/lanes, never gates | Yes — explicit extension of ai-corpus-14 to V1↔V2 | No — merge bar constant, inspection depth varies (converges with VN) | Largely resolved 2-vs-1 toward VN/FC semantics; the residual question is terminological (whether "lane assignment" and "verification tier" are the same object). Settle by writing both as normative text and checking auditor readability |
| 3 | **Routing key for review depth** | Scope classifier (path+semantic), planner-proposed, human-checked | Computed change class × materiality (oracle undesigned — blocker) | Self-declared materiality (blocker: gameable) | All three broken the same way; the settled requirement is already visible: a **deterministic, conservative-by-default, independently owned, org-corpus-6-calibrated classifier**, with regulatory scope as an orthogonal axis. Evidence: seeded-misrouting detection rate before any sampled lane opens |
| 4 | **Maintenance model** | Patch, always, with provenance | Regenerate where sealed; patch + reconciliation obligation elsewhere | Patch via work orders | Pilot data: cost-per-verified-outcome of regeneration vs patch on a sealed candidate module, plus incident forensics drill results (bisectability substitute) |
| 5 | **Migration shape** | 4 estate-wide stages, trigger-gated | Per-module maturity ladder (A0–A3) | 5 lane-scoped stages | Critiques converge on lane/module-scoped over estate-wide (partial adoption is the permanent normal). Evidence: whether estate-wide triggers (95% provenance coverage) are reachable at all in a mixed estate — FC's critic argues no |
| 6 | **Where the human-authorship evidence question lands** | Names it (equivalence table) after critique | Implicit | Implicit | A drafted equivalence table + 2 AM break-glass path tested in a game day settles it for all three |
| 7 | **Judge posture** | Advisory + severity rules, degraded mode TBD | Binding at V1/V2 | Load-bearing in sampling lanes | Judge precision measured against an independently curated ledger, verdict flip-rate under rerun, and a provider-outage game day. If flip-rate is high, judges cannot be load-bearing (FC/IL posture fails); if precision beats the human comparator on scoped correctness, advisory-only (VN) underuses it |

### 5.3 Council reading

The convergence set (§5.1) is large enough to draft normative text from. The three frames are not actually competing lifecycles — they are **three views of one lifecycle**: VN supplies the verification economy and evidence chain, FC supplies the workforce control plane (roster, certificates, lanes, offboarding) and the governance-of-the-governors machinery, IL supplies the per-module maturity taxonomy and the drift discipline as an *optional overlay* wherever a module can earn it. Every blocker across all six critiques falls into five repairable families: (a) supersession mechanics not routed through the doctrine's own change protocol; (b) no named human owning sampled/unsampled merges; (c) an undesigned or gameable routing classifier; (d) uncalibrated or unfunded calibration; (e) missing brownfield/human-author/partial-adoption on-ramps. None of the six critiques attacked the shared premise.

---

## 6. Decisions for session 2

| Id | Decision | Options | Council leaning |
|---|---|---|---|
| **D1** | **Base frame for the normative pattern** | (a) VN backbone + FC control plane, IL maturity taxonomy as optional per-module overlay; (b) one design adopted whole; (c) new synthesis from scratch | **(a)**. §5.3 reading; no critique defended (b) for any single design |
| **D2** | **ai-corpus-6 supersession mechanics** | (a) Bounded normative replacement via ADR + change-class label + deprecation markers + harmonised merge-path canonical file; (b) keep "extension" framing | **(a)** — both governance critiques independently required it; (b) fails org-corpus-21/23 |
| **D3** | **Accountability for sampled/unsampled merges** | (a) Standing, signed, scoped, expiring risk acceptance by the named first-line owner (org-corpus-5 mechanics), recorded per-merge; (b) approver+lane-owner pair only; (c) no sampling lane at all | **(a)**; (c) retained as the regulated-scope answer (see D11) |
| **D4** | **Routing classifier design and ownership** | (a) Deterministic, over-inclusive, conservative-by-default (ambiguous routes up), path+symbol+reachability, itself Tier-0/V0, independently owned, calibrated with seeded misroutes before any sampled lane opens; (b) planner-proposed + human check; (c) self-declared with reconciliation | **(a)** — the one repair all six critiques converge on. Misses = Sev-high control failures with automatic pattern expansion |
| **D5** | **Trust-moves-what semantics** | (a) Slider moves lane assignment/sampling rate/countersign timing, never binding gates or pinned floors (VN/FC); (b) earned trust moves verification tier (IL) | **(a)** 2-of-3 + cleaner auditor story; record (b) as a rejected alternative in the ADR |
| **D6** | **Human-authored change evidence equivalence + break-glass** | (a) Explicit per-lane equivalence table + 2 AM Sev-1 path with retroactive evidence, game-day tested pre-adoption; (b) waiver class | **(a)**; (b) creates the two-tier gate NIST neutrality forbids |
| **D7** | **Brownfield on-ramp** | (a) Characterization tests as substitute provenance roots + spec-on-touch + "unspecified-legacy" provenance class + coverage ratchet; (b) require specs before agent work on legacy; (c) exclude legacy | **(a)**; per-lane estate-readiness preconditions from FC's critique folded in |
| **D8** | **Calibration program** | (a) Named owning team + headcount; every calibration asset carries expiry; **fail closed** (stale calibration closes the sampled lane); injected defects quarantined from promotion (shadow branch / server-enforced marker + auto-revert); injector health SLI; defects sourced from anonymized real escapes; (b) quarterly best-effort | **(a)** — unanimous across critiques; (b) is the documented failure mode |
| **D9** | **Judge dependency posture** | (a) Judges/verifiers are roster members: capability certificates, golden known-answer sets retained for after-the-fact control evidence, named substitute + game day, verdict caching keyed on diff hash, rerun caps with escalation, flip-rate as control-health metric; advisory until precision-calibrated, binding only per-lane after; (b) binding from day one; (c) advisory forever | **(a)** |
| **D10** | **Inconclusive-routing noise control** | (a) Split infra-inconclusive (retry/quarantine, flake budgets per pack, delivery-corpus-20 discipline) from semantic-inconclusive (human queue, still loudest); (b) route all inconclusive to humans as written | **(a)**; (b) inverts the intended semantics via alarm fatigue |
| **D11** | **Regulatory-scope axis** | (a) Orthogonal flag in inventory + work order; regulated paths pinned to evidence/line review regardless of materiality; explicit sampling exclusion as a migration trigger; (b) fold into materiality | **(a)** — FC's governance critique is decisive; regulators attach to systems, not per-change stamps |
| **D12** | **Ratify the two unanimous supersessions** | delivery-corpus-29 bounded reversion carve-out; delivery-corpus-7 polarity inversion **plus** explicit re-homing of explain-and-own to a named, tested incident-explainer role | Ratify both via the D2 mechanics; no dissent recorded |
| **D13** | **Model-churn evidence economics** | (a) Partial-credit transfer: portable per-lane/module recertification suite restoring standing in days; certificate TTLs that ratchet autonomy left on expiry (degrade loudly, never certify falsely); (b) full reset per ai-corpus-22 read literally | Leaning **(a)**, but this is the least-evidenced decision on the list — needs a costed proposal in session 3 |
| **D14** | **Attention-budget governance** | (a) Published budget model (hours per work order by risk class, measured before delegation); throttle gates intake and review; set-point changes ADR-gated; override = formal break-glass with named executive owner, time-bound, 100% retrospective audit, reported with SLO breaches; (b) SLOs only | **(a)** — all three practicality critiques independently predicted (b)'s failure |
| **D15** | **Adoption economics of Stage 1** | (a) Immediate-payoff instrumentation (evidence bundles auto-generate PR descriptions etc.), 2–3 repo pilot, ceremony-quality audits before triggers count, lane/module-scoped stages; (b) estate-wide mandate as drafted | **(a)** |
| **D16** | **Independent challenge of the control plane itself** | (a) Named second-line challenger (outside the platform team) with block authority over stage promotions and control-plane changes; calibration audited externally to its authors; (b) platform-team self-governance | **(a)** — SoD finding; also settles the SoD role-distinctness constraints from VN's critique |
| **D17** | **ISC/criteria quality control** | (a) Layered partials: ISC lint binding + different-model challenge + sampled human re-derivation on promoted lanes (divergence as the metric) + spec-mutation testing pilot; acknowledge unsolved residue in the ADR; (b) defer entirely | **(a)** — no full solution exists; the trust-inflation spiral (FC critique) makes (b) unacceptable |

---

## 7. Proposed session plan

| Session | Scope | Output |
|---|---|---|
| **2 — Frame + governance mechanics** | Resolve D1–D5, D12, D16. Draft the **supersession register**: one table per touched invariant (ai-corpus-6, delivery-corpus-1/3/7/22/29, org-corpus-25 extension, ai-corpus-1 SoR admission, delivery-corpus-13 extension) with org-corpus-21 change class, carrying ADR, and deprecation disposition. Decide harmonisation edits to [../principles/merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md) | Supersession register v1; frame ruling; accountability model text |
| **3 — Verification economy internals** | D6, D8–D10, D13, D17. Specify: the routing classifier (D4 detail), lane definitions and evidence requirements, judge admission/calibration protocol, sampling statistics approach (pre-registered sequential analysis; V2/L3 gated off until k is calibrated), calibration quarantine mechanics, human-author equivalence table, model-churn recertification suite design | Lane specification + calibration protocol drafts |
| **4 — Brownfield, operations, regulation** | D7, D11, D14–D15. Legacy on-ramp; per-lane estate-readiness preconditions; ops-loop taint architecture (lethal-trifecta closure for triage agents) and circuit-breaker thresholds; regulatory-scope overlay; attention-budget model with break-glass contract; migration stages re-cut lane/module-scoped | Migration playbook draft; ops-loop addendum |
| **5 — Metrics, artifacts, economics** | Metric definitions frozen (work-order denominators, rework rate, saturation index, provenance coverage, cost-per-verified-outcome); artifact-of-record schema list (extending meta-2 surface contracts: work order, run contract, verifier pack, evidence bundle, roster entry, waiver ledger); ledger freshness/ownership rules | Metrics annex + artifact schema annex |
| **6 — Drafting** | ADR (successor to ADR-0024/0030 line) + normative pattern file (`../patterns/` — likely revising [../patterns/ai-native-software-development-lifecycle.md](../patterns/ai-native-software-development-lifecycle.md)) + checklist updates ([../checklists/ai-native-sdlc-readiness.md](../checklists/ai-native-sdlc-readiness.md)) + edits to superseded files with deprecation markers | Draft ADR + pattern text |
| **7 — Adversarial pass + finalize** | Re-run both critique lenses against the drafts; verify every session-1 blocker has a landed repair or a recorded org-corpus-5 risk acceptance; final supersession register; release under org-corpus-21 change classes | Merge-ready PR set |

---

## 8. References

Deduplicated external sources used across the session-1 research. Flags from researchers are preserved in §2; presence here does not imply the source was fully fetchable.

**Vendor lifecycles and agents**
- https://techcommunity.microsoft.com/blog/appsonazureblog/an-ai-led-sdlc-building-an-end-to-end-agentic-software-development-lifecycle-wit/4491896 *(body not fetchable; verified via component docs)*
- https://techcommunity.microsoft.com/blog/azurepaasblog/introducing-azure-sre-agent/4414569
- https://techcommunity.microsoft.com/blog/azureinfrastructureblog/from-drift-to-self-healing-building-a-multi-repo-azure-ai-infrastructure-you-can/4515315
- https://docs.github.com/en/copilot/concepts/about-copilot-coding-agent
- https://learn.microsoft.com/en-us/azure/sre-agent/overview
- https://learn.microsoft.com/en-us/azure/sre-agent/run-modes
- https://learn.microsoft.com/en-us/azure/sre-agent/roles-permissions-overview
- https://learn.microsoft.com/en-us/azure/sre-agent/permissions
- https://devblogs.microsoft.com/all-things-azure/platform-engineering-for-the-agentic-ai-era/
- https://blog.mikehacker.net/p/agentic-devops-building-a-self-healing-software-lifecycle-with-github-copilot-and-azure-sre-agent/
- https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/
- https://aws.amazon.com/blogs/devops/building-with-ai-dlc-using-amazon-q-developer/
- https://aws.amazon.com/blogs/devops/open-sourcing-adaptive-workflows-for-ai-driven-development-life-cycle-ai-dlc/
- https://aws.amazon.com/blogs/industries/ai-driven-development-lifecycle-for-financial-services/
- https://aws.amazon.com/blogs/machine-learning/how-frontier-teams-are-reinventing-ai-native-development/
- https://github.com/awslabs/aidlc-workflows

**Spec-driven development**
- https://github.com/github/spec-kit
- https://github.com/github/spec-kit/blob/main/spec-driven.md
- https://github.github.com/spec-kit/
- https://github.com/github/spec-kit/discussions/2114
- https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/
- https://developer.microsoft.com/blog/spec-driven-development-spec-kit/
- https://developer.microsoft.com/blog/spec-driven-development-ai-native-engineering/
- https://learn.microsoft.com/en-us/training/modules/spec-driven-development-github-spec-kit-enterprise-developers/
- https://kiro.dev/docs/specs/
- https://kiro.dev/docs/specs/feature-specs/requirements-first/
- https://kiro.dev/docs/steering/
- https://kiro.dev/docs/hooks/
- https://kiro.dev/docs/chat/autopilot/
- https://specs.md/ *(operator unidentified)*
- https://specs.md/methodology/sdlc-reimagined
- https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- https://github.com/cameronsjo/spec-compare

**Anthropic practices and trends**
- https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf
- https://www.anthropic.com/engineering/building-effective-agents
- https://code.claude.com/docs/en/best-practices
- https://www.anthropic.com/institute/recursive-self-improvement
- https://vantor.com/blog/building-an-agentic-sdlc-anthropics-emerging-harness-design-patterns/ *(third-party interpretation, not Anthropic primary)*
- https://tessl.io/blog/8-trends-shaping-software-engineering-in-2026-according-to-anthropics-agentic-coding-report/
- https://venturebeat.com/technology/anthropic-says-80-of-its-new-production-code-is-now-authored-by-claude-how-your-enterprise-can-keep-up
- https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-claude-now-writes-more-than-80-percent-of-its-merged-code

**Multi-agent methodologies and evaluation**
- https://github.com/bmadcode/BMAD-METHOD
- https://github.com/FoundationAgents/MetaGPT
- https://github.com/OpenBMB/ChatDev
- https://github.com/OpenHands/OpenHands
- https://arxiv.org/abs/2308.00352 (MetaGPT)
- https://arxiv.org/abs/2307.07924 (ChatDev)
- https://arxiv.org/abs/2407.16741 (OpenHands)
- https://arxiv.org/abs/2503.13657 (MAST)
- https://sky.cs.berkeley.edu/project/mast/
- https://openreview.net/pdf?id=wM521FqPvI
- https://www.augmentcode.com/guides/bmad-method-ai-development
- https://adsantos.medium.com/you-should-bmad-part-1-63dbc45d162e

**Academic syntheses**
- https://arxiv.org/abs/2604.26275 (Bhati, A-SDLC — preprint, under review)
- https://arxiv.org/abs/2408.03416 (Hymel, V-Bounce — vendor-funded whitepaper)
- https://arxiv.org/abs/2604.23340
- https://arxiv.org/abs/2505.16339
- https://arxiv.org/abs/2601.01129 (Atlassian RovoDev)

**Enterprise/consulting**
- https://www.coderabbit.ai/guides/agentic-sdlc
- https://www.dronahq.com/agentic-sdlc-guide/
- https://www.thoughtworks.com/en-us/radar/techniques/spec-driven-development
- https://www.thoughtworks.com/about-us/news/2026/combat-ai-cognitive-debt-radar-v34
- https://www.thoughtworks.com/about-us/news/2025/thoughtworks-tech-radar-33-rapid-ai
- https://www.pwc.com/m1/en/publications/rise-of-autonomous-software-delivery.html *(HTTP 403 — unverified)*
- https://www.pwc.com/m1/en/publications/2026/docs/future-of-solutions-dev-and-delivery-in-the-rise-of-gen-ai.pdf *(HTTP 403 — unverified)*
- https://www.atlassian.com/blog/ai-at-work/developer-productivity-improved-with-rovo-dev
- https://www.qodo.ai/reports/state-of-ai-code-quality/ *(cited 55%→81% figure not located in public report)*

**Standards, measurement, governance**
- https://dora.dev/dora-report-2025/
- https://dora.dev/ai/capabilities-model/
- https://dora.dev/ai/roi/report/
- https://services.google.com/fh/files/misc/2025_dora_ai_capabilities_model.pdf *(not text-extractable)*
- https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
- https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model
- https://www.infoq.com/news/2026/05/dora-roi-ai-assisted-dev-report/
- https://redmonk.com/rstephens/2025/12/18/dora2025/
- https://csrc.nist.gov/pubs/sp/800/218/a/final
- https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218A.pdf
- https://genai.owasp.org/llm-top-10/
- https://genai.owasp.org/initiatives/agentic-security-initiative/
- https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/ *(primary PDF download-gated)*
- https://pipelab.org/learn/owasp-agentic-threats/
- https://artificialintelligenceact.eu/
- https://linuxfoundation.eu/newsroom/ai-act-explainer
- https://www.augmentcode.com/guides/eu-ai-act-2026

**Day-2 operations and provenance**
- https://www.pagerduty.com/blog/ai/new-enhancements-to-pagerdutys-sre-agent-triage-faster-without-waking-a-human/
- https://www.pagerduty.com/platform/ai-agents/sre/
- https://www.pagerduty.com/blog/product/the-path-to-autonomous-operations-pagerduty-spring-26-release/
- https://incident.io/ai-sre
- https://argo-rollouts.readthedocs.io/
- https://tldrecap.tech/posts/2026/argocon-europe/argo-rollouts-ai-integration/
- https://engineeringagents.substack.com/p/provenance-as-the-chain-of-accountability *(thought-leadership)*
- https://medium.com/toward-next-ai/ai-code-provenance-workflow-track-what-coding-agents-changed-before-it-ships-02cd387cbba3 *(thought-leadership)*
- https://nhimg.org/articles/code-provenance-is-the-missing-control-for-ai-generated-commits/ *(thought-leadership)*

---

*End of Session 1 Council Report. §7's session plan is preserved as the council's proposal; subsequent work proceeded via the landed ADR 0024/0030 chain — see the preamble.*
