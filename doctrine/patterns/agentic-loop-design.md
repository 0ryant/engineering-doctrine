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
- **Critical constraint:** the critique must be grounded by an **external verifier** (test suite, human rating, structured rubric). Pure self-evaluation is unreliable — a model can confidently misdiagnose its own failure. Self-certified success is not success.
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

**What scaffolding cannot fix:** intrinsic motivation, curiosity, continuous learning between runs, long-horizon sparse reward tasks without human decomposition. Do not architect around capabilities current LLMs do not have. See §6 (autonomy slider) and §9 (anti-patterns).

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
- At context limit, run a LLM-distilled summary rather than truncation: recursive summaries preserve task context that sliding-window pruning destroys.
- Drop tool outputs after extracting the key value; the raw 10KB response rarely needs to stay in context after the model has processed it.

#### Isolate — split context across agents
- Give sub-agents narrow, focused contexts; the orchestrator handles references, not full content.
- Code agents output code to an execution sandbox; only the structured return value re-enters the LLM context (not the full stdout/stderr dump).
- Multi-agent parallelism (see §8) lets each agent work within a focused context window.

**Why:** Agent failures are increasingly context failures, not model failures. Optimising what the model sees is higher leverage per engineering hour than model upgrades or prompt rewrites.

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
- Any **auth, tenancy, crypto, schema, or person-affecting** action must start at "approve before irreversible" regardless of agent maturity — see [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) §4.
- The slider can move **right** (more autonomous) as empirical data accumulates from VERIFY step + ISC pass rate. It moves **left** on any ISC regression or incident.
- **Transparent plan state**: expose the agent's current plan and active ISC to operators in real time. An agent whose internals are invisible to its operators cannot be reliably supervised.

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
- Orchestrator never re-derives what a worker reported; it trusts the typed output schema.

### 8.2 Evaluator–Optimizer Loop
- A separate evaluator model applies a scoring rubric to agent outputs and returns structured critique.
- Most consistent when the rubric is aligned to ISC and tested against cases with known correct answers.
- A single well-aligned judge beats a panel of poorly aligned ones; more judges is not always better.

### 8.3 Production Multi-Agent Operational Rules
- **Checkpoint every step** — durable state persistence, not in-memory only. On failure, resume from last checkpoint rather than full restart.
- **Double-texting policy**: decide explicitly what happens when new input arrives while an agent is running (reject, queue, interrupt, or rollback to checkpoint). Default to **reject** for destructive agents; **queue** for retrieval agents.
- **Rainbow deployments**: when deploying a new agent version, route traffic gradually while the old version may still be mid-run. Agents, unlike stateless APIs, cannot be cut over atomically.
- **Effort budgets in prompts**: explicitly instruct the orchestrator how many sub-agents and calls are appropriate for different query complexities.

**Why:** Anthropic's production research agent: multi-agent (Claude Opus 4 orchestrator + Sonnet 4 workers) outperformed single-agent Opus 4 by 90.2% on internal eval. Token cost: ~15× compared to chat, so multi-agent is not automatically preferable for cheap tasks.

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

---

## 10. Task Routing (Full / Iteration / Minimal)

Not every input requires the full nested loop. Route intelligently:

| Mode | When | What runs |
| --- | --- | --- |
| **Full** | New problem, implementation task, complex analysis, first pass on a domain | All phases: OBSERVE (ISC), inner loop, VERIFY, LEARN |
| **Iteration** | Continuation of an existing task ("ok, now try X instead") | Inner loop only; inherit existing ISC; no re-decomposition |
| **Minimal** | Acknowledgment, clarification request, a rating, a greeting | Direct response; no tooling |

Common failure mode: running FULL on continuation tasks causes the agent to re-plan what it was already doing, fragment the work, and lose context. Recognise continuation cues and skip re-decomposition.

Anthropic's design guidance: start with the simplest possible solution (single LLM call + retrieval). Add workflows before agents. Add agents only when workflows demonstrably fail on task variability.

---

## 11. Anti-Patterns

| Anti-pattern | What goes wrong |
| --- | --- |
| **Self-certified success** | The agent evaluates its own output without external verification. Reflexion only works with external signal. A closed loop without reward cannot converge. |
| **Full loop on continuation** | Re-decomposing and re-planning a task already in progress loses context, fragments work, and wastes budget. |
| **Flat injection defence** | Relying on LLM-based filters ("detect if this looks like an injection") instead of architectural separation. Probabilistic guards fail at scale. |
| **Tool soup** | All tools always present in the context regardless of task stage. Degrades tool selection accuracy; expands attack surface. |
| **Unbounded loops** | No stopping condition. Agent iterates until context limit or cost limit, not until task is done. |
| **Context poisoning via chained outputs** | One model's hallucination enters the next model's context as fact. Chain LLM outputs only via typed structured values, not raw text. |
| **Council as approval substitute** | Multiple model votes treated as equivalent to human approval or CI pass for high-risk change. Not a valid approval mechanism for auth, tenancy, schema, or person-affecting automation — see [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) §4. |
| **Missing context compression** | Raw tool outputs accumulate in context. At 95%+ context fill, model degradation is steep. Compress before you hit the limit. |
| **Autonomy hard-coded to max** | New or insufficiently verified agents deployed silently. Default conservative; earn the right to more autonomy through ISC pass-rate data. |
| **ACI neglect** | Tool descriptions written as notes to self. Treated as configuration, not documentation. Model tool misuse follows directly. |

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Nested loop model as the baseline | ReAct and Miessler's PAI independently arrived at the same structure; it is the minimum that can converge on non-trivial tasks. |
| Verifiability gate before building automation | Karpathy: the jagged AI frontier is explained entirely by verifiability. Building agents on non-verifiable tasks produces confident failure. |
| ISC before any agent task | Without binary testable criteria, VERIFY is subjective. Subjective VERIFY = closed loop with no signal = no convergence. |
| Architectural injection defence, not probabilistic | CaMeL and Willison converge: probabilistic guards fail at scale. Taint tracking in the controller is deterministic. |
| Context engineering as a first-class discipline | Anthropic production data and Karpathy both confirm: agent failures are predominantly context failures now, not model failures. |
| Autonomy slider default-conservative | Blast radius asymmetry: over-supervision wastes time; under-supervision causes incidents. Start conservative, earn autonomy from data. |
| External verifier required for Reflexion reliability | Shinn et al.'s own analysis: Reflexion gains come from external verifiers (unit tests). Self-critique without external grounding can confidently misdiagnose. |
| Scaffolding investment priority | ReAct, PAI, Anthropic: structural and scaffolding improvements outperform model upgrades per unit of engineering effort. |

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
- **Anthropic — Building Effective Agents** (Dec 2024): https://www.anthropic.com/engineering/building-effective-agents
- **Anthropic — Multi-Agent Research System** (Jun 2025): https://www.anthropic.com/engineering/built-multi-agent-research-system
- **Context Engineering** (Karpathy tweet, Jun 2025): https://x.com/karpathy/status/1937902205765607626
- **LangChain — Context Engineering** (Chase, Jun 2025): https://blog.langchain.com/the-rise-of-context-engineering/
- **12 Factor Agents** (Horthy — "own your context window"): https://github.com/humanlayer/12-factor-agents
- **LangGraph** (cyclic graphs for agentic loops): https://github.com/langchain-ai/langgraph
