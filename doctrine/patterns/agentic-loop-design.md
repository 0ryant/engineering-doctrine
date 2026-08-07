# Agentic Loop Design

Design rules and patterns for **agent harnesses** — the scaffolding that orchestrates LLM calls, tools, memory, and human oversight into a coherent, safe, and verifiable automated system.

**First-class doctrine** under [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) Tier D. The principles here apply to any agent harness regardless of framework or model provider. Framework choices (LangGraph, LangChain, plain Python) belong in `doctrine/tooling/estates/`. This file governs portable loop structure, verification discipline, injection defence, and context management.

**Research foundation:** ReAct (Yao et al., ICLR 2023), Reflexion (Shinn et al., NeurIPS 2023), PAI/ISC (Miessler, v4.0), Karpathy's verifiability and autonomy slider framing (2025), Willison + CaMeL injection defence (2023–2025), Anthropic's "Building Effective Agents" + "Multi-Agent Research System" (Dec 2024, Jun 2025), Context Engineering discourse (Karpathy, Chase, Martin, June 2025).

---

## 1. The Nested Loop Model

Agent tasks operate at **three nested time scales**. Confusing them is the most common cause of brittle harnesses.

### 1.1 Outer Loop: Goal–State Gap

```
Current state → decompose into binary testable criteria → desired state
```

- Owner: the harness or the human writing the task description.
- Input: what is true now, what must be true when done.
- Output: a set of binary YES/NO **Ideal State Criteria (ISC)** (see §3).
- The outer loop runs **once per task**. It does not re-run on every LLM call.

### 1.2 Inner Loop: Think → Act → Observe (ReAct)

```
THINK — why is this tool call needed? What state am I trying to reach?
ACT   — invoke the tool with a minimal, scoped call
OBSERVE — what did the tool return? Does it affect the plan?
```

- Every **tool call must be preceded by explicit reasoning** about why.
- Every **tool response must trigger explicit reasoning** about what it changed before the next action.
- This is not optional commentary — it is the mechanism that prevents error propagation across steps (without it, one wrong tool output silently contaminates the rest of the trajectory).
- Cap inner loop iterations explicitly (e.g., 20 steps). Budget-based stopping conditions are mandatory for Tier D: see [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) §2.

### 1.3 Episode Loop: Critique → Retry (Reflexion)

- When a task fails and the environment is **resettable**, an agent that writes a textual critique of why it failed and carries that critique into the next attempt can improve without weight updates.
- The episodic memory buffer (critiques + outcomes) is a form of test-time learning; it is the closest current equivalent to in-context adaptation.
- **Critical constraint:** the critique must be grounded by an **external grounding signal** (test suite, human rating, structured rubric — "verifier" in the pack sense is narrower: [verifier-packs.md](verifier-packs.md) §8). Pure self-evaluation is unreliable — a model can confidently misdiagnose its own failure. Self-certified success is not success.
- Store critiques alongside the task id and ISC results; they are engineering artefacts, not conversation noise.

**Why:** ReAct showed +34% task success over pure RL baselines using structural change alone — not a stronger model. Reflexion achieved 91% pass@1 on HumanEval (vs. GPT-4's 80%) through verbal critique backed by unit tests. Loop structure is higher-leverage than model choice.

---

## 2. Verifiability As The Automation Gate

> "Software 1.0 easily automates what you can specify. Software 2.0 easily automates what you can verify." — A. Karpathy

**Before committing to agent automation of any task, assess whether the environment satisfies three conditions:**

| Condition | Question | Implication if missing |
| --- | --- | --- |
| **Resettable** | Can a failed attempt be cleanly undone so another can start? | Destructive one-shot operations require human approval, not agent retry |
| **Efficient** | Can many attempts be made without prohibitive cost or latency? | Expensive tasks need tighter ISC upfront; iteration is not free |
| **Rewardable** | Can an automated process score any specific attempt? | Without this, the loop is open; no signal, no convergence |

A task that fails on any condition is a **human task with optional AI assistance** — not an autonomous agent task. Automate only what you can verify; everything else gets a human in the loop (see §6).

**Recurrence gates promotion, not existence — and never governance.** A one-off, supervised, disposable run is always legitimate — construction can cost a single prompt, though cheapness is at the prompt layer only: a one-off that invokes tools or mutates state already **requires a run contract in full** ([run-contracts.md](run-contracts.md) §§1.1–2), including its gates and ceilings (§6.1); what it lacks is standing. Demonstrated **recurrence** is the admission ticket to **standing authority and scheduling** (§6.1) — harness build-and-maintenance cost amortises only over repetition (toil is definitionally repetitive work). Anything that persists past its one-off purpose either climbs the ladder, gaining an owner, a template, and standing authority, or is deleted.

**Why:** Math and code improve explosively under AI because they are highly verifiable (compilers, test suites, automated checkers). Creative, strategic, and physical-world tasks lag because they lack cheap automated reward signals. Spending harness development effort on non-verifiable tasks produces overconfident failure rather than reliable automation.

---

## 3. Binary Testable Criteria (ISC)

Before any agent task starts, decompose the goal into **Ideal State Criteria (ISC)**: binary, testable, state-oriented success conditions.

| Rule | Good | Bad |
| --- | --- | --- |
| **State, not action** | "All unit tests pass" | "I ran unit tests" |
| **Binary testable** | Answerable YES/NO in under 2 seconds | Requires interpretation |
| **Granular** | One concern per criterion | Mixed-outcome compound checks |
| **Verifiable by the harness** | Automated assertion in VERIFY step | Requires human judgement to evaluate |

**Pattern:**

```
OBSERVE:  Reverse-engineer the request. What was explicitly asked?
          What was implied? What is definitely not wanted?
          Write ISC now, before any tool calls.

...inner loop runs...

VERIFY:   Check every ISC.
          Record: PASSED / FAILED / BLOCKED for each.
          If any FAILED: enter Episode loop (§1.3) or escalate.
          Do not proceed to next task until VERIFY runs.
```

**Why:** Without ISC, the agent is navigating without a destination and evaluating without a rubric. The VERIFY step is the convergence mechanism — skip it and the loop is open regardless of how sophisticated the inner loop is.

---

## 4. Scaffolding Over Model Intelligence

> "A well-designed system with a mediocre model will outperform a brilliant model with poor scaffolding. Every time." — D. Miessler

Invest proportionally in harness design:

| Investment | What it buys |
| --- | --- |
| **Structured loop** (§§1–3) | Prevents error propagation; enables self-correction |
| **Context engineering** (§5) | Ensures the model sees the right information at each step |
| **Tool documentation (ACI)** (§7) | Tool descriptions are the model's interface to the world; poor docs = wrong tool calls |
| **Verification mechanisms** | Closes the loop; enables Reflexion-style retry |
| **Typed state and ISC** | Forces explicit goal decomposition; creates measurable progress |

**What scaffolding cannot fix:** intrinsic motivation, curiosity, continuous learning between runs, long-horizon sparse reward tasks without human decomposition. Do not architect around capabilities current LLMs do not have. See §6 (autonomy slider) and §12 (anti-patterns).

---

## 5. Context Engineering

The **context window is the model's working memory**. The discipline of deciding what goes into it — and when — is context engineering. It is the primary optimization surface for agent reliability.

**Failure modes when context is wrong:**

| Mode | Description |
| --- | --- |
| **Poisoning** | A hallucination enters context and propagates through subsequent steps |
| **Distraction** | Too much context overwhelms the model's priors for the actual task |
| **Confusion** | Superfluous or irrelevant context corrupts the response |
| **Clash** | Parts of context contradict each other |

### 5.1 Four Context Strategies

#### Write — save context outside the window
- **Scratchpad**: tool call writes intermediate conclusions to a file or structured state field; retrieved selectively on subsequent steps.
- **Episodic memory**: on task completion or failure, auto-generate a structured summary; retrieve at start of related future tasks. This is the substrate for Reflexion-style improvement without weight updates.
- At context limit: save the current plan to external memory before spinning up new sub-agents with clean contexts; pass lightweight references, not full transcripts.

#### Select — pull the right context into the window
- **Procedural memory** (CLAUDE.md-style instruction files, `.cursor/rules/`, Copilot instruction files) — steer model behaviour across sessions without in-context instructions every time.
- **RAG**: lexical + dense retrieval, fusion, reranking. For code: combine grep, file search, and graph retrieval — embeddings alone degrade as codebases grow.
- **Tool RAG**: embed tool descriptions and retrieve only the relevant subset per step; reduces tool selection errors significantly (see §7).
- **Episodic / few-shot**: retrieve relevant past examples from episodic memory by similarity.

#### Compress — retain only required tokens
- At context limit, run a LLM-distilled summary rather than truncation: recursive summaries preserve task context that sliding-window pruning destroys — but compaction silently drops in-context constraints, so pin policy/constraints outside the window or re-inject them post-compaction (§6.1; ledger L6.1).
- Drop tool outputs after extracting the key value; the raw 10KB response rarely needs to stay in context after the model has processed it.

#### Isolate — split context across agents
- Give sub-agents narrow, focused contexts; the orchestrator handles references, not full content.
- Code agents output code to an execution sandbox; only the structured return value re-enters the LLM context (not the full stdout/stderr dump).
- Multi-agent parallelism (see §8) lets each agent work within a focused context window.

**Why:** Agent failures are increasingly context failures, not model failures. Optimising what the model sees is higher leverage per engineering hour than model upgrades or prompt rewrites.

### 5.2 Persisted-Memory Red-Teaming (ASI06)

Where an agent holds **agent-writable persistent memory** (the episodic-memory substrate of §5.1 Write), **poisoning** stops being a single-session context failure (§5 table) and becomes a **cross-session persistence channel** — **ASI06 Memory & Context Poisoning** (§11). Memory-injection research shows the store can be poisoned through **ordinary query interaction alone**, and that agents are **more vulnerable to memory injection than to prompt injection** — prompt-injection defences give limited protection once stored context is already compromised ([MINJA, arXiv 2503.03704](https://arxiv.org/abs/2503.03704); [arXiv 2503.16248](https://arxiv.org/abs/2503.16248), where memory injection on a Web3 agent produced unauthorized asset transfers).

- Where the threat model warrants red-teaming at all ([rag-retrieval-baseline.md](rag-retrieval-baseline.md) §4's condition) and memory is agent-writable, adversarial scenarios MUST include **planted-memory persistence across sessions**: a record written in session *N* alters behaviour on a **legitimate query** in session *N+1*, with no attacker present at recall time.
- Run the exercise through the **existing red-team machinery** of [rag-retrieval-baseline.md](rag-retrieval-baseline.md) §4 (adversarial and dirty documents) — a memory store is a retrieval corpus; do not build a parallel harness.
- The lifecycle controls the exercise tests — **admission, retention, relinquishment, recovery** — live in [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) §7; admission modes stay canonical in [run-contracts.md](run-contracts.md) `context.memory`.

**Why:** A poisoned memory outlives the session that planted it and is re-injected by retrieval on every related future task; red-teaming only single-session injection leaves the persistent channel untested.

---

## 6. The Autonomy Slider

There is no binary "agent on / agent off." There is a **continuum of human-in-the-loop involvement**. Good harnesses expose this slider explicitly and default conservatively. Hard-coding one setting is a design failure.

```
Fully supervised                                     Fully autonomous
      |----+--------------------+---------------+-------|
   Approve    Approve before         Review        Deployed
   every     irreversible only       results       silently
   action                           before apply
```

| Slider position | Suitable when |
| --- | --- |
| **Approve every action** | New, untested agent; novel domain; high-blast-radius tools |
| **Approve before irreversible only** | Established agent; reversible-by-default actions |
| **Review results before apply** | Mature agent; well-scoped domain; good ISC hit rate |
| **Deployed silently** | After sustained verified track record; closed loop with external verification + instant rollback |

**Rules:**
- Blast radius and verifiability (§2) determine the default starting position.
- Any **auth, tenancy, crypto, schema, money-movement, or person-affecting** action MUST start at "approve before irreversible" regardless of agent maturity — see [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) §4; agent financial authority is default-deny per [../principles/cost-and-finops.md](../principles/cost-and-finops.md) §7.1.
- The slider can move **right** (more autonomous) as empirical data accumulates from VERIFY step + ISC pass rate. It moves **left** on any ISC regression or incident.
- **Transparent plan state**: expose the agent's current plan and active ISC to operators in real time. An agent whose internals are invisible to its operators cannot be reliably supervised.

### 6.1 Build Order — How A Loop Earns Each Rung

**Gates are not a rung — they arrive with governed execution itself.** Any run that invokes tools or mutates state is governed from its first execution ([run-contracts.md](run-contracts.md) §§1.1–2) and carries the full envelope — the §3 VERIFY step and the externally enforced stop and budget ceilings of §1.2 and §8.3. The ladder orders what is *built*, under gates throughout:

1. **Run it manually first**, in a supervised session at the slider's leftmost position. A task that fails hand-run fails scheduled, only faster.
2. **Lock what worked into a reusable template** — instructions, criteria, tool list, versioned rather than living in one chat. Once that template steers scheduled automation it is an **agent-definition artefact** in the pipeline-definition trust class ([../principles/merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md) §§1–2).
3. **Harden the enforcement locus.** Stop and budget ceilings MUST be enforced outside the context window — a widening of §8.3's outside-prompt enforcement rule from multi-agent trees to every governed loop. Verification MUST bind through a mechanism outside the model's own self-report — a harness-run §3 VERIFY, a test suite, or human approval per §6; the in-context VERIFY step is necessary, not sufficient. In-context constraints demonstrably decay under ordinary compaction, and the 2025 record's marquee agent incidents — the Replit production-database deletion during an explicit code freeze, and the Amazon Q injected-prompt incident (AWS-2025-015, CVE-2025-8217) — both occurred in *interactive* sessions, not scheduled runs.
4. **Schedule last.** Standing triggers are earned by demonstrated recurrence (§2) and a verified track record, and run on the recurring-automation build surface ([build-surface-model.md](build-surface-model.md)); the worked cron example is [run-contracts.md](run-contracts.md) §5. Acquiring a standing trigger does not move the autonomy slider — a scheduled run inherits its slider position, and slider movement remains governed by the §6 observed-success rules alone.

The ladder composes with the slider: build order says when a capability exists; the slider says how much oversight it runs under. Evidence: [research-agent-loop-graph-cross-check-2026-08.md](../evolution/research-agent-loop-graph-cross-check-2026-08.md) §5 second-pass addendum (L6.1–L6.2, L4.1–L4.6).

---

## 7. Tool Design And The Agent-Computer Interface (ACI)

Tool definitions are the agent's interface to the world. Invest in them as first-class documentation.

- Write tool docstrings for a **junior developer who doesn't know your codebase** — include: purpose, when to use vs. similar tools, required and optional parameters, what errors to expect, edge cases.
- **Fewer, well-named tools beat many ambiguous ones.** Model tool selection degrades with tool soup. Keep active tool sets scoped to the task; use tool RAG (§5.1) for large tool libraries.
- **Poka-yoke where possible**: design parameters so common mistakes are structurally impossible (e.g., require an explicit `confirm: true` flag for destructive operations; use typed enums instead of free strings for action types).
- **Prefer absolute over relative paths** in file access tools — relative paths are a common root cause of cross-context path errors.
- Test tool definitions independently from the agent loop; a bad tool description sends the agent down wrong paths before the first tool call.
- **Tool changes are breaking changes**: update the ACI documentation the way you would update an API contract.

**Why:** Anthropic's production multi-agent experience: improving tool descriptions with self-diagnosing agents produced 40% faster task completion. ACI investment has a higher return than prompt iteration once the loop structure is correct.

---

## 8. Multi-Agent Patterns

Use multiple agents when tasks parallelise, exceed a single context window, or require isolated specialisation. Do not use multi-agent for tasks with heavy cross-dependencies or requiring continuous shared state.

### 8.1 Orchestrator–Worker Model
- Orchestrator (larger model) holds the plan and delegates subtasks with explicit: objective, output format, tool list, task boundaries.
- Workers (smaller or specialised models) execute with narrow focused contexts.
- Workers return typed outputs so claims, provenance, limitations, and evidence can be checked. A typed shape prevents ambiguity; it does not make the content true. The orchestrator or an independent verifier validates material worker claims before integration.

### 8.2 Evaluator–Optimizer Loop
- A separate evaluator model applies a scoring rubric to agent outputs and returns structured critique.
- Most consistent when the rubric is aligned to ISC and tested against cases with known correct answers.
- A single well-aligned judge beats a panel of poorly aligned ones; more judges is not always better.

**Judge discipline — load-bearing judges.** The rules below activate when a judge's verdicts **gate promotion, merges, or automation** (verdict-driven routing with material consequences); purely advisory critique is unaffected. Expected evidence for a compliant deployment: a chance-corrected agreement report, a versioned judge-config digest, a bias perturbation record, and an escalation-gate record (calibration record where the judge exposes a usable confidence signal). **Minimum viable evidence:** a labeled set on the order of **50–100 known-answer cases**, a scripted kappa computation with bootstrap intervals, and a one-page protocol note satisfy the measurement duty for a first deployment; estates scale sample size and cadence with the **materiality** of what the judge gates.

- **Chance-corrected agreement, not raw percent.** Before a judge becomes load-bearing, its agreement with human labels on known-answer cases MUST be measured with a chance-corrected statistic (**Cohen's kappa** for two raters, **Fleiss' kappa** for more), with raw agreement, class prevalence, confidence intervals, and the measurement protocol reported alongside. Raw percent agreement inflates on imbalanced labels: across 21 deployed judge models, **kappa deflation** (exact-match agreement minus kappa) runs 33–41 percentage points and reorders judge rankings ([arXiv 2606.19544](https://arxiv.org/abs/2606.19544)); protocol choices alone — scale, case retention, abstention handling, verdict pooling — can carry kappa across zero without changing a single verdict, so an agreement number without its protocol is not evidence ([arXiv 2606.00093](https://arxiv.org/abs/2606.00093)). The **acceptance threshold is estate-defined** and recorded with the judge config; a judge below its estate threshold does not gate.
- **The judge is a versioned config.** A load-bearing judge is model id + prompt + rubric + thresholds, **pinned and versioned like test infrastructure**. A material change MUST be regression-tested against the labeled set before deployment, and starts a new comparable series or triggers re-judging of prior outputs — verdicts from different judge versions are not comparable data. (Same-criteria-across-runs discipline: [OpenAI Evals regression cookbook](https://developers.openai.com/cookbook/examples/evaluation/use-cases/regression).)
- **Perturbation-test known biases before verdicts bind.** **Position, verbosity, and self-enhancement bias** are the canonical judge failure modes ([arXiv 2306.05685](https://arxiv.org/abs/2306.05685)). Before a judge becomes binding it MUST be stress-tested under order swaps, paraphrase, repeated trials, and adversarial probes: pairwise preferences flip ~14% of the time on mere repetition and semantically equivalent prompt templates change majority outcomes in a quarter of tested cases ([arXiv 2606.13685](https://arxiv.org/abs/2606.13685)); trivial "master key" tokens — a lone colon, a generic reasoning opener — elicit false-positive verdicts from frontier judges ([arXiv 2507.08794](https://arxiv.org/abs/2507.08794)).
- **Escalation-gated automation.** The binding obligation is the **escalation behaviour**: low-confidence, near-threshold, or **abstained** verdicts MUST escalate to a stronger judge or a human — never silently pass. Use **calibrated confidence** where the judge exposes a usable signal (logprobs, repeated sampling); an explicit abstain/"Unknown" output plus a **conservative threshold buffer** is the acceptable minimum where it does not ([Anthropic, demystifying evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)). Selective evaluation with escalation provably guarantees a target human-agreement level while keeping most verdicts automated ([arXiv 2407.18370](https://arxiv.org/abs/2407.18370)).
- **Monitor judge drift like model drift.** Recalibrate against fresh human labels **on a cadence and at a label volume proportional to what the judge gates** (estates set the schedule) and on any upstream model change; a **material kappa drop below the estate threshold** under a stable rubric is an incident for every gate the judge feeds, not a curiosity.
- **Sole-authority limit.** A judge MUST NOT be the sole authority for a high-materiality acceptance decision unless its agreement and failure modes have been independently calibrated for that use. A judge is **one verification mechanism among several** — outside the verifier-pack kind enum — downstream of the §2 verifiability gate: [verifier-packs.md](verifier-packs.md) §8 scopes packs to binary-observable artefact properties and explicitly excludes model evaluation, so judge discipline lives here. Per [anti-confabulation-priming.md](anti-confabulation-priming.md) §1, an unvalidated or uncalibrated judge verdict is **untrusted verification, hence non-pass** for load-bearing automation.

**Consumer impact:** estates whose evaluator–optimizer verdicts gate anything must produce the validation artefacts above before the gate is trusted; advisory-only critique loops require no change.

### 8.3 Production Multi-Agent Operational Rules
- **One writer or an explicit merge protocol** — each mutable workspace has one owner. Parallel writers use isolated workspaces and a named integration step.
- **Immutable inputs** — each child records the input snapshot, dependency versions, and parent contract it received. Material input change invalidates derived work until it is re-evaluated.
- **Authority attenuates** — a child receives a subset of the parent's authority. Delegation cannot widen tools, data, target, time, or budget, and an agent cannot authorise its own widening.
- **Bound the tree** — fan-out, depth, time, token/compute/cost, and retry limits MUST be enforced outside model prompts. Exhaustion stops or escalates; it does not silently relax limits.
- **Typed handoffs are claims** — handoffs carry provenance, outputs, open findings, limitations, and verifier results. They are checked before integration rather than trusted because they parse.
- **Checkpoint with identity** — persist durable state at declared boundaries. Resume revalidates input snapshot, policy version, identity, authority, lease/expiry, and target; stale work starts a linked new run or stops.
- **Propagate cancellation and revocation** — terminating or narrowing a parent recursively revokes affected child authority. Orphaned children cannot continue with cached credentials.
- **Reconcile shared state** — shared mutable state uses transactions, compare-and-set/version checks, or an explicit reconciliation owner. Non-atomic multi-contract effects declare compensation or containment.
- **Double-texting policy**: decide explicitly what happens when new input arrives while an agent is running (reject, queue, interrupt, or rollback to checkpoint). Default to **reject** for destructive agents; **queue** for retrieval agents.
- **Rainbow deployments**: when deploying a new agent version, route traffic gradually while the old version may still be mid-run. Agents, unlike stateless APIs, cannot be cut over atomically.
- **Budget guidance may appear in prompts, but enforcement belongs to the host or orchestrator policy** and is recorded in receipts. The model cannot grant itself more calls, time, compute, or spend.

**Why:** Anthropic's production research agent: multi-agent (Claude Opus 4 orchestrator + Sonnet 4 workers) outperformed single-agent Opus 4 by 90.2% on internal eval. Token cost: ~15× compared to chat, so multi-agent is not automatically preferable for cheap tasks.

### 8.4 Decomposition: Dependencies, Fan-Out, And Convergence

How to split work across agents, once §§8.1–8.3 govern the running of it. **Register note:** this subsection is design guidance at §8.3's register — untyped imperatives are design defaults; the single typed claim is marked. "Converge" here names a **graph join**, not the §§2–3 sense of a loop reaching a verified terminal state. A dependency graph is a **partial order**; any execution sequence is one linearization of it, and wall-clock time is set by the **critical path** — so deleting false ordering is the only speedup that shortens nothing else.

- **Audit every implied edge.** For each "B after A", ask: does B consume something A produces? A real data dependency keeps the edge; mere authoring order deletes it. Where ordering without data flow is genuinely required (shared-resource sequencing, an external constraint), declare it as an explicit *ordering* edge — a distinct edge type from *consumes-output-of*, never a fake data edge. Steps with no incoming edge can start immediately. **Work dependencies** (graph edges — not package dependencies, and not the pinned *dependency versions* in §8.3's input snapshots) SHOULD be **declared explicitly, with execution order derived from them** rather than hand-fixed — the invariant across orchestration systems since critical-path scheduling (1959).
- **Fan-out/converge** (scatter-gather) is the recurring shape: independent branches in parallel feeding one integration step. Two preconditions, both load-bearing: branches share **no decision surface** (reads parallelise; writes stay single-threaded or behind §8.3's merge protocol), and the converge step genuinely needs **more than one branch's contribution under its declared completeness criterion** — an all-branches converge that uses only one input is waste; quorum and first-success trade redundancy for latency deliberately.
- **The converge node is stateful, and it is a verification point** — in the §§2–3 sense, not a verifier pack ([verifier-packs.md](verifier-packs.md) §8 scopes packs to binary-observable artefact properties). It declares its **completeness criteria** (all branches / quorum / first-success), its **aggregation mode** (reduce; majority vote where outputs are comparable; judge — §8.2 discipline applies when the judge gates), and its **failure policy**. Majority vote **converges** outputs; it does not approve — §12's council-as-approval-substitute anti-pattern continues to bind for high-materiality integration. These declarations live in the external coordinator today: the run-contract v1 cannot express them ([run-contracts.md](run-contracts.md) §9 records the deferral). In the largest multi-agent failure study ([MAST, arXiv:2503.13657](https://arxiv.org/abs/2503.13657)), *incorrect* verification was roughly as common as *absent* verification — a bad judge at the converge point is not safer than none.
- **Failure policy belongs to the downstream consumer or its edge** — the cross-system default (Airflow, Argo, GitHub Actions, Prefect declare it there; dbt's `on_error` is the producer-declared exception; global fail-fast overrides everywhere). Name the choice per converge point: fail-fast-halt, skip-downstream (the common default), continue-degraded on declared partial results, or compensate-and-unwind where branches carry side effects.
- **Retry is not neutral for agent nodes.** A retried agent node is non-deterministic: it can make different implicit decisions than the attempt its completed siblings coordinated with — engines preserve *state* consistency, not *decision* consistency. Declare the re-run scope (retry the node vs re-run the subgraph from the last checkpoint) through §8.3's checkpoint-with-identity rule, and give side-effectful tools idempotency keys ([idempotency-across-boundaries.md](idempotency-across-boundaries.md)).
- **Every dynamic fan-out carries a declared cardinality bound that fails loudly at the producer** — never silent truncation — alongside §8.3's tree bounds. Unbounded fan-out is unbounded spend ([../principles/cost-and-finops.md](../principles/cost-and-finops.md) §7).
- **When not to graph.** The §8 opening triggers are the whole positive list — parallelisable work, context-window exhaustion, isolated specialisation — and §8's exclusions still bind: heavy cross-dependencies and continuous shared state stay single-agent (a graph whose critical path is near-serial after the edge audit is such a task). Check the **single-agent baseline first**: in token-matched comparisons a single agent has matched or beaten most multi-agent topologies on reasoning tasks (single study, preprint — ledger row G6.7), and the vendor record's own multi-agent cost is ~15× chat tokens (§8.3 Why). Prefer structure that can be deleted as models improve: encode coordination in contracts and checkpoints, not hand-tuned topology.

**Why:** Fan-out/converge's pedigree runs from critical-path scheduling (1959) through scatter-gather and MapReduce to every mature orchestrator, all of which derive order from declared dependencies. The agent-specific additions — converge as a verification point, decision consistency under retry, single-threaded writes — come from the 2025–2026 empirical record. Full graded source ledger: [research-agent-loop-graph-cross-check-2026-08.md](../evolution/research-agent-loop-graph-cross-check-2026-08.md) §5 including its second-pass addendum.

---

## 9. Injection Defence: Dual-Path Architecture

**The lethal trifecta**: an agent that simultaneously has (1) access to external/untrusted content, (2) access to private data, and (3) communication or write tools is a prompt injection incident waiting to happen: the "confused deputy" attack.

### 9.1 Architectural Defence Pattern

```
User prompt
  → P-LLM (Privileged)
       Only receives: user prompt
       Produces: explicit plan / structured action sequence
       Never sees: raw external content
       Has: full tool access

External content (email, document, web page, tool output)
  → Q-LLM / Quarantined processor
       Only sees: untrusted content
       Produces: typed structured values (EmailStr, Amount, etc.)
       Has: no tool access, no outbound communication
       Can be: a smaller or local model

Controller / Interpreter (regular code, not an LLM)
  → Executes P-LLM's plan step by step
  → Tracks provenance (taint) of every variable
  → At each tool call: checks whether the capability policy permits
       passing tainted data to this tool
  → Blocks or prompts user for approval when policy is violated
```

This is the architecture independently described by Willison's Dual LLM pattern (2023) and formalised with taint tracking by Google DeepMind's CaMeL paper (2025).

### 9.2 Critical Properties

- **Willison's fundamental rule**: the output of the quarantined processor (including chained outputs) **must never be forwarded verbatim as instructions** to the privileged model. Raw external content is never trusted input to the planning LLM.
- **CaMeL's improvement**: even the Dual LLM pattern is insufficient if the Q-LLM's output is used as a trusted variable by the P-LLM's plan. The answer is capability/taint tracking in the interpreter layer — a data provenance policy enforced by code, not by another probabilistic model.
- **System-level enforcement, not LLM filtering**: probabilistic LLM-based guards on injection ("99% detection is a failing grade") are not a substitute for architectural taint tracking. Enforcement must happen in deterministic code.
- **Default-deny at the interpreter**: data derived from untrusted sources requires explicit policy allowance before passing to a tool. Unknown-provenance values prompt for human approval rather than proceeding.

### 9.3 Practical Minimum (Where Full CaMeL Is Not Yet Feasible)
At minimum, before the full architecture is in place:
- Never interpolate external/retrieved text directly into the trusted system prompt.
- Structure tool outputs as typed structured data (not raw text) so the model reads values, not instructions.
- For any agent touching private data + external content + write tools: human approval gate at the communication/write step until taint tracking is implemented.

**Why:** The attack surface grows directly with agent capability. Every tool you add to a confused deputy agent is another exfiltration vector. Architectural defence is not optional for Tier D systems.

### 9.4 Adaptive Evaluation Of Deployed Defences

Deploying the §9 architecture is a **design control**, not evidence of effectiveness. An estate claiming injection or hijack resistance MUST evaluate the claim **adaptively (attacker-iterates) against its own deployment** — the testing duty routes to [../principles/testing-strategy.md](../principles/testing-strategy.md) §5 and is **not discharged by adopting this pattern**:

- **Static replay overstates every defence class measured.** Adaptive attackers (gradient methods, RL, search, human red-teaming) bypass prompting-based, adversarial-training, and detector defences that reported near-zero static attack success at **>90%** rates ([The Attacker Moves Second, arXiv:2510.09023](https://arxiv.org/abs/2510.09023)). This sharpens §9.2: a **probabilistic** component anywhere in the defence stack is presumptively bypassable, and its static benchmark numbers are not evidence.
- **The architectural layer still needs deployment-specific evaluation.** Capability policies, taint rules, tool inventories, and Q-LLM output typing are estate configuration — adaptive evaluation is what finds the permissive policy or unlisted tool path in *your* deployment. Joint US/UK AISI agent-hijack red-teaming moved success from **11%** (static corpus) to **81%** once attackers iterated, and single attempts understate risk (57% at 1 attempt vs 80% at 25) — repeat trials are part of the protocol ([AISI hijacking evaluations](https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations)).
- **Where memory is agent-writable**, the adaptive scenarios include the §5.2 planted-memory persistence exercise — same discipline, same harness, no parallel machinery.

**Why (§9.4):** the published validations of dual-path/CaMeL-class defences are static-benchmark only; an estate's claim of resistance is an empirical claim about *its* deployment, and only an iterating attacker tests it.

---

## 10. Task Routing (Full / Iteration / Minimal)

Not every input requires the full nested loop. Route intelligently:

| Mode | When | What runs |
| --- | --- | --- |
| **Full** | New problem, implementation task, complex analysis, first pass on a domain | All phases: OBSERVE (ISC), inner loop, VERIFY, LEARN |
| **Iteration** | Continuation of an existing task ("ok, now try X instead") | Inner loop only; inherit existing ISC; no re-decomposition |
| **Minimal** | Acknowledgment, clarification request, a rating, a greeting | Direct response; no tooling |

Common failure mode: running FULL on continuation tasks causes the agent to re-plan what it was already doing, fragment the work, and lose context. Recognise continuation cues and skip re-decomposition.

Anthropic's design guidance: start with the simplest possible solution (single LLM call + retrieval). Add **deterministic workflows** (predefined code paths) before agents. Add agents only when workflows demonstrably fail on task variability.

---

## 11. ASI-To-Doctrine Crosswalk (OWASP Top 10 For Agentic Applications 2026)

The **OWASP Top 10 for Agentic Applications 2026** (**ASI01–ASI10**; OWASP GenAI Security Project, Agentic Security Initiative, final release 2025-12-09) is the **agentic-layer companion** to the OWASP Top 10 for LLM Applications — **complementary, not superseding**; its entries cross-map to LLM Top 10 (2025) mitigations: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

This crosswalk is **navigational vocabulary**: it maps each ASI identifier to the existing doctrine control(s) that address it, so coverage can be demonstrated to reviewers and auditors who speak ASI vocabulary. It restates no mitigations and adds no new obligations — each linked section carries its own normative strength. Where doctrine has no control for a mitigation family, the gap is recorded honestly.

| ASI id | Risk | Doctrine control(s) |
| --- | --- | --- |
| **ASI01** | Agent Goal Hijack | §9 (untrusted content never reaches the planning model); §3 (ISC pin the goal; VERIFY detects drift from declared criteria); [run-contracts.md](run-contracts.md) (scope, authority, and outputs bound before the run); [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) §7 (retrieved/external text is untrusted input) |
| **ASI02** | Tool Misuse and Exploitation | §7 (ACI design, poka-yoke `confirm` flags, scoped tool sets); §6 (approval gates before irreversible actions); [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) §2 Tier D (per-tool least privilege, bounded loops/cost) and §7 (per-tool authorisation, rate limits, audited invocations); [run-contracts.md](run-contracts.md) capabilities; [../principles/cost-and-finops.md](../principles/cost-and-finops.md) §7.1 (financial/transaction authority default-deny, session transaction budgets, materiality-tiered approval) |
| **ASI03** | Identity and Privilege Abuse | §8.3 (authority attenuates; delegation cannot widen; resume revalidates identity, authority, lease; revocation propagates — orphaned children cannot continue with cached credentials); [../principles/zero-trust-and-workload-identity.md](../principles/zero-trust-and-workload-identity.md) §2 (workload identity for runners) and §2.1 (agent identity: sponsor lifecycle, per-interaction credentials, on-behalf-of attribution); [../principles/cost-and-finops.md](../principles/cost-and-finops.md) §7.1 (payment authority is a granted, inventory-recorded privilege — never fleet-ambient) |
| **ASI04** | Agentic Supply Chain Vulnerabilities | [../principles/dependencies-supply-chain.md](../principles/dependencies-supply-chain.md) §8 (models and datasets as dependencies: digest pinning, publisher verification, OMS/Sigstore signature + transparency-log verification, safe serialization, per-model AIBOM); [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) §4 (pre-install verification gate for AI-proposed packages) with [../principles/dependencies-supply-chain.md](../principles/dependencies-supply-chain.md) §7 (slopsquatting mitigations); [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) §7 (authenticate tool-protocol servers; track server-implementation dependencies); [ai-adoption-controls.md](ai-adoption-controls.md) §1 (vendor/embedded AI in the inventory). **No current coverage**: registry-level attestation for **agent and tool packages** (skills, MCP server distributions) — model/dataset artifact signing and AIBOM evidence now covered via the §8 link |
| **ASI05** | Unexpected Code Execution (RCE) | [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) §4 (agents propose — no direct mutation of production; CI and human gates on the change path); §5.1 Isolate (generated code runs in an execution sandbox; only typed return values re-enter context — **described practice, not a mandated control**: doctrine does not currently mandate sandboxed execution) |
| **ASI06** | Memory & Context Poisoning | §5 (poisoning as a named context failure mode; Write/Select/Compress/Isolate strategies); §5.2 (planted-memory persistence red-teaming where memory is agent-writable); [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) §7 (persisted agent memory reopens Tier B retrieval rules — ACL, eval, injection — plus memory-lifecycle rules: admission, retention, relinquishment, recovery); [rag-retrieval-baseline.md](rag-retrieval-baseline.md) (index hygiene and retrieval eval) |
| **ASI07** | Insecure Inter-Agent Communication | §8.3 (typed handoffs are claims — checked before integration, never trusted because they parse; immutable input snapshots); [../principles/zero-trust-and-workload-identity.md](../principles/zero-trust-and-workload-identity.md) §1 (mutually authenticated service-to-service identities — mTLS, signed tokens — on every hop); [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) §7 (authenticate servers and callers on tool protocols). **No current coverage**: message-level payload signing and anti-replay between agents |
| **ASI08** | Cascading Failures | §8.3 (bound the tree — fan-out, depth, time, budget; cancellation and revocation propagate; reconcile shared state); §1.2 (capped inner-loop iterations); §6 (blast radius sets the autonomy default); [verifier-packs.md](verifier-packs.md) §4 (fail-loud, never fail-silent) |
| **ASI09** | Human-Agent Trust Exploitation | §6 (transparent plan state; conservative autonomy defaults); [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) §4 (overseer authority to disregard, override, or halt; automation-bias awareness); [ai-adoption-controls.md](ai-adoption-controls.md) §2 (independent challenge) and §5 (role-based capability uplift); §8.2 judge discipline (escalation-gated automation routes low-confidence machine verdicts to humans — adjacent partial coverage on the machine-verdict side only, not human-trust calibration). **No current coverage**: adaptive trust calibration and anthropomorphism-specific countermeasures |
| **ASI10** | Rogue Agents | §8.3 (terminating or narrowing a parent recursively revokes child authority; budget enforcement outside prompts); §6 (autonomy earned from verified track record, retracted on regression or incident); [../principles/zero-trust-and-workload-identity.md](../principles/zero-trust-and-workload-identity.md) §2.1 (sponsor lifecycle; orphaned agents are disabled, not left running); [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) §4 (human halt authority) with [../principles/audit-logging.md](../principles/audit-logging.md); [ai-adoption-controls.md](ai-adoption-controls.md) §1 (inventory) and §3 (continuous drift monitoring). **No current coverage**: watchdog agents and per-agent cryptographic identity attestation |

---

## 12. Anti-Patterns

| Anti-pattern | What goes wrong |
| --- | --- |
| **Self-certified success** | The agent evaluates its own output without external verification. Reflexion only works with external signal. A closed loop without reward cannot converge. |
| **Full loop on continuation** | Re-decomposing and re-planning a task already in progress loses context, fragments work, and wastes budget. |
| **Flat injection defence** | Relying on LLM-based filters ("detect if this looks like an injection") instead of architectural separation. Probabilistic guards fail at scale. |
| **Tool soup** | All tools always present in the context regardless of task stage. Degrades tool selection accuracy; expands attack surface. |
| **Unbounded loops** | No stopping condition. Agent iterates until context limit or cost limit, not until task is done. |
| **Context poisoning via chained outputs** | One model's hallucination enters the next model's context as fact. Chain LLM outputs only via typed structured values, not raw text. |
| **Council as approval substitute** | Multiple model votes treated as equivalent to human approval or CI pass for high-risk change. Not a valid approval mechanism for auth, tenancy, schema, or person-affecting automation — see [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) §4. |
| **Missing context compression** | Raw tool outputs accumulate in context. At 95%+ context fill, model degradation is steep. Compress before you hit the limit — and pin constraints outside the window when you do: compaction silently drops them (§5.1). |
| **Autonomy hard-coded to max** | New or insufficiently verified agents deployed silently. Default conservative; earn the right to more autonomy through ISC pass-rate data. |
| **ACI neglect** | Tool descriptions written as notes to self. Treated as configuration, not documentation. Model tool misuse follows directly. |
| **Unbounded, unvalidated agent memory** | Agent-writable memory with no admission validation, no TTL, and no recovery path is an **accumulating attack surface**: every poisoned write persists and re-enters context on retrieval. Lifecycle rules: [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) §7; cross-session red-team hook: §5.2. |
| **Unvalidated load-bearing judge** | Judge verdicts gate promotion or automation with no chance-corrected agreement, no perturbation testing, no versioned config. Raw percent agreement is theatre — it inflates on imbalanced labels while kappa sits near zero. An unvalidated judge treated as ground truth is self-certified success at one remove (§8.2). |
| **Fake edges** | Authoring order encoded as dependency. Work queues behind steps it never needed and the critical path inflates for free. Audit every edge for real data flow (§8.4). |
| **Parallelised decision surfaces** | Independent branches writing to shared artefacts or making overlapping decisions. Conflicting implicit assumptions compound at the merge. Writes stay single-threaded or behind an explicit merge protocol (§§8.3–8.4). |

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Nested loop model as the baseline | ReAct and Miessler's PAI independently arrived at the same structure; it is the minimum that can converge on non-trivial tasks. |
| Verifiability gate before building automation | Karpathy: the jagged AI frontier is explained entirely by verifiability. Building agents on non-verifiable tasks produces confident failure. |
| ISC before any agent task | Without binary testable criteria, VERIFY is subjective. Subjective VERIFY = closed loop with no signal = no convergence. |
| Architectural injection defence, not probabilistic | CaMeL and Willison converge: probabilistic guards fail at scale. Taint tracking in the controller is deterministic. Effectiveness in a given estate remains an empirical claim — evidenced adaptively per §9.4, not by pattern adoption. |
| Context engineering as a first-class discipline | Anthropic production data and Karpathy both confirm: agent failures are predominantly context failures now, not model failures. |
| Autonomy slider default-conservative | Blast radius asymmetry: over-supervision wastes time; under-supervision causes incidents. Start conservative, earn autonomy from data. |
| External verifier required for Reflexion reliability | Shinn et al.'s own analysis: Reflexion gains come from external verifiers (unit tests). Self-critique without external grounding can confidently misdiagnose. |
| Scaffolding investment priority | ReAct, PAI, Anthropic: structural and scaffolding improvements outperform model upgrades per unit of engineering effort. |
| ASI crosswalk as vocabulary, not controls | Tier-D mitigations existed but were unmapped to ASI01–ASI10 identifiers, so coverage could not be demonstrated in auditor vocabulary. The crosswalk cross-links existing controls without duplicating normative content; gaps are recorded honestly. |
| Judge discipline at the pattern layer (§8.2) | Kappa deflation, verdict flipping under trivial perturbation, and master-key false positives are measured properties of deployed judges, not edge cases. A judge that gates promotion or automation is test infrastructure and gets the same rigour: pinned versioned config, regression on change, chance-corrected validation, escalation-gated automation. |

---

## References

- **ReAct**: Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models", ICLR 2023: https://arxiv.org/abs/2210.03629
- **Reflexion**: Shinn et al., "Reflexion: Language Agents with Verbal Reinforcement Learning", NeurIPS 2023: https://arxiv.org/abs/2303.11366
- **Karpathy — Verifiability** (Software 2.0 automation gate, Nov 2025): https://karpathy.bearblog.dev/verifiability/
- **Karpathy — 2025 Year in Review** (autonomy slider, context engineering, Dec 2025): https://karpathy.bearblog.dev/year-in-review-2025/
- **Karpathy — Animals vs. Ghosts** (ghost problem, limits of current LLMs, Oct 2025): https://karpathy.bearblog.dev/animals-vs-ghosts/
- **Miessler — PAI Algorithm v4.0** (ISC, 7-phase loop, scaffolding thesis): https://github.com/danielmiessler/Personal_AI_Infrastructure
- **Willison — Dual LLM Pattern** (prompt injection, confused deputy, Apr 2023): https://simonwillison.net/2023/Apr/25/dual-llm-pattern/
- **Willison — The Lethal Trifecta** (external content + private data + write tools, 2025): https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- **CaMeL** — Debenedetti et al., Google DeepMind / ETH Zurich, "Defeating Prompt Injections by Design", arXiv:2503.18813 (2025): https://arxiv.org/abs/2503.18813
- **CaMeL code** (Apache-2.0, research artifact): https://github.com/google-research/camel-prompt-injection
- **The Attacker Moves Second** — Nasr et al., adaptive attacks bypass 12 jailbreak/prompt-injection defences (prompting, adversarial-training, detector classes) at >90% vs near-zero static ASR, arXiv:2510.09023 (2025): https://arxiv.org/abs/2510.09023
- **US/UK AISI — Strengthening AI Agent Hijacking Evaluations** (AgentDojo; 11% static → 81% attacker-iterated; repeat-trial protocol, Jan 2025): https://www.nist.gov/news-events/news/2025/01/technical-blog-strengthening-ai-agent-hijacking-evaluations
- **NIST AI 100-2e2025** — Adversarial ML taxonomy (adaptive-attack evaluation requirement): https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2025.pdf
- **Anthropic — Building Effective Agents** (Dec 2024): https://www.anthropic.com/engineering/building-effective-agents
- **Anthropic — Multi-Agent Research System** (Jun 2025): https://www.anthropic.com/engineering/built-multi-agent-research-system
- **Context Engineering** (Karpathy tweet, Jun 2025): https://x.com/karpathy/status/1937902205765607626
- **LangChain — Context Engineering** (Chase, Jun 2025): https://blog.langchain.com/the-rise-of-context-engineering/
- **12 Factor Agents** (Horthy — "own your context window"): https://github.com/humanlayer/12-factor-agents
- **LangGraph** (cyclic graphs for agentic loops): https://github.com/langchain-ai/langgraph
- **OWASP Top 10 for Agentic Applications 2026** (ASI01–ASI10, Agentic Security Initiative, final release 2025-12-09): https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- **MINJA — memory injection through query interaction** (agent memory poisoned with no store access): https://arxiv.org/abs/2503.03704
- **Memory injection vs prompt injection on Web3 agents** (unauthorized asset transfers): https://arxiv.org/abs/2503.16248
- **Zheng et al. — Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena** (position, verbosity, self-enhancement bias; NeurIPS 2023): https://arxiv.org/abs/2306.05685
- **Reliability without Validity** (kappa deflation 33–41pp across 21 judge models, 2026): https://arxiv.org/abs/2606.19544
- **Agreement Metrics for LLM-as-Judge Evaluation** (measurement protocol carries kappa across zero, 2026): https://arxiv.org/abs/2606.00093
- **The Coin Flip Judge?** (verdict flipping under repetition and paraphrase, 2026): https://arxiv.org/abs/2606.13685
- **One Token to Fool LLM-as-a-Judge** (master-key adversarial tokens, 2025): https://arxiv.org/abs/2507.08794
- **Trust or Escalate** (confidence-gated selective evaluation, ICLR 2025): https://arxiv.org/abs/2407.18370
- **Anthropic — Demystifying Evals for AI Agents** (judge calibration; abstain output, Jan 2026): https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- **OpenAI Cookbook — Detecting Prompt Regressions** (pinned model-grader config): https://developers.openai.com/cookbook/examples/evaluation/use-cases/regression
