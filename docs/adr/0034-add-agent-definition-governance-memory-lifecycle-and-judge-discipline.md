# ADR 0034: Add Agent-Definition Governance, Memory Lifecycle, And Judge Discipline

- **Status:** Accepted
- **Decision date:** 2026-08-03
- **Recorded date:** 2026-08-03
- **Retrospective:** No

## Context

Fourth closure batch from the August 2026 gap audit ([research-bleeding-edge-ai-landscape-gap-audit-2026-08.md](../../doctrine/evolution/research-bleeding-edge-ai-landscape-gap-audit-2026-08.md)) — the medium-severity trio, all adversarially verified:

- **G8 — agent-definition files as change surfaces.** Injected instructions in agent config files are code execution by another name: the "Rules File Backdoor" attack hid invisible-Unicode payloads in rules files that coding agents obeyed through fork and PR review; a wiper instruction shipped as prompt text inside an official Amazon Q Developer release (AWS-2025-019); a hallucinated package spread to 237+ repos through unreviewed AI-generated skill files. Doctrine's pipeline-definition trust class did not name these artefacts.
- **G9 — agent memory.** MINJA-class research shows agent-writable memory can be poisoned through ordinary query interaction alone, and that memory injection out-severities prompt injection once stored context is compromised. Doctrine had one retrieval-rules bullet and no lifecycle (admission/retention/relinquishment/recovery).
- **G10 — LLM-judge discipline.** Measured properties of deployed judges — kappa deflation of 33–41pp between raw agreement and chance-corrected kappa, verdict flips under trivial perturbation, master-key false positives — mean an unvalidated judge gating promotion is self-certified success at one remove. Doctrine's §8.2 evaluator-optimizer loop carried no validation duty.

Council provenance: 11-agent draft council; no blockers; 4 majors and minors resolved in landed text — notably a false canonical-ownership pointer (the no-self-review rule now lives in the merge-path invariant its pointer claimed), a managed-platform compliance branch for vendor memory stores, a minimum-viable-evidence floor for judge validation, and the confidence-gate obligation re-cut as escalation behaviour rather than calibration technique.

## Decision

1. **Agent-definition artefacts join the pipeline-definition trust class (normative).** [merge-path-evidence-and-pipeline-integrity.md](../../doctrine/principles/merge-path-evidence-and-pipeline-integrity.md) §1 defines the term (custom-agent definitions, steering/instruction files, SKILL.md-class skills, MCP server configs, delivery-wired prompt templates) with an explicit boundary: in scope when the artefact steers automation **on the merge path or holding standing credentials beyond the invoking human's session**; a solo developer's interactive-assistant instruction file is ordinary repo content. §2 invariant 2 carries the review conditions — protected paths, provenance, **no self-review** (the agent whose definition changes never approves the change), **informed reviewer**. [code-review-and-change-approval.md](../../doctrine/patterns/code-review-and-change-approval.md) §5 gains the high-risk row (illustrative; normative weight in the invariant); the AI-native SDLC pattern cross-links. Minimal viable check for the inherited adversarial-analysis gate on these paths: invisible-Unicode/bidi lint + injection-pattern scan + third-party skill/MCP digest verification — all scriptable in CI today.
2. **Agent memory lifecycle (normative, scoped to agent-writable persistent stores).** [ai-ml-systems.md](../../doctrine/principles/ai-ml-systems.md) §7: **admission** (validated, provenance-tagged writes; modes stay canonical in the run-contract `context.memory` schema and verifier-pack verdict chain — extended, not restated), **retention** (TTL defaults SHOULD; operator-initiated forget MUST; personal-data composition with privacy §2/§5.3 including derived artifacts), **relinquishment** (store closed out with the decommissioned agent, composing with zero-trust §2.1 orphan handling), **recovery** (estate-operated stores SHOULD be snapshot-restorable; poisoning suspicion MUST trigger quarantine + rebuild). **Managed-platform branch:** where the vendor exposes no write hook or snapshot, disabling memory or scope-minimisation + scheduled review-and-purge conforms, recorded once per platform. [agentic-loop-design.md](../../doctrine/patterns/agentic-loop-design.md) §5.2 adds the planted-memory persistence red-team scenario through the existing rag-retrieval-baseline §4 machinery.
3. **Judge discipline for load-bearing judges (normative, activation-gated).** agentic-loop-design §8.2: judges whose verdicts gate promotion/merges/automation are **versioned configs** (model+prompt+rubric+thresholds, regression-tested on change), validated by **chance-corrected agreement** with an **estate-set acceptance threshold** (a judge below threshold does not gate), **perturbation-tested** for position/verbosity/self-enhancement bias before binding, and **escalation-gated** (low-confidence, near-threshold, or abstained verdicts escalate; calibrated confidence where the judge exposes a signal, abstain + conservative buffer as the acceptable minimum). Drift recalibration is proportional to gate materiality. **Minimum viable evidence:** ~50–100 labeled cases, scripted kappa with bootstrap intervals, one-page protocol note. A judge is one verification mechanism outside the verifier-pack kind enum and never sole authority for high-materiality acceptance; per anti-confabulation-priming §1 an unvalidated judge verdict is untrusted verification, hence non-pass.

## Alternatives Considered

### Classify agent-definition files as ordinary source code

Rejected. Source-class review assumes the reviewer reads what executes; instruction files execute through the agent's authority, invisibly to a human skimming prose — the Rules File Backdoor survived PR review precisely because of that assumption.

### A universal per-file scope for the trust class

Rejected on council critique: read literally it pulls every solo-repo CLAUDE.md into CODEOWNERS + no-self-review, which is structurally impossible alone and erodes the mandate where it matters. The standing-credential/merge-path boundary keeps the class aimed at privileged automation.

### Restating memory admission modes in the principles file

Rejected. The run-contract schema is the canonical enum; a paraphrase would drift. The principles text extends the surface and points home.

### Numeric kappa thresholds in doctrine

Rejected. Threshold values are estate- and task-dependent; doctrine mandates the measurement discipline, the estate-recorded threshold, and the below-threshold-does-not-gate rule, keeping numbers out of portable text.

## Consequences

### Positive

- The file class that steers agent authority now carries the same protections as the CI workflows it rides on, with a CI-scriptable minimum check.
- Agent memory gets a full lifecycle with a realistic vendor-managed branch, and the persistent poisoning channel enters red-team scope.
- Judge-gated automation acquires a falsifiable evidence bar a small team can meet in an afternoon, closing the percent-agreement-theatre loophole.

### Costs And Risks

- CODEOWNERS-style ownership of agent-definition paths is new repo hygiene for estates with many agent configs.
- Memory-lifecycle duties add platform-exception records for vendor stores; deletion latency on managed platforms remains vendor-bound.
- Judge validation requires an initial labeling investment (~50–100 cases per judge) and recurring drift labels proportional to gate materiality.
- Master-key/perturbation batteries are point-in-time; new adversarial token families will require re-testing.

## Consumer Impact

**Change class:** normative for estates with agent-definition artefacts steering privileged automation (G8), agent-writable persistent memory (G9), or judges gating promotion/automation (G10); additive guidance otherwise. Estates with none of the three change nothing.

**Compatibility proposal:** 0.x minor. All mandates are activation-gated (trust-class boundary, agent-writable stores, load-bearing judges); advisory judges and interactive-assistant instruction files are explicitly out of scope.

## Acceptance Evidence

- Audit provenance: G8/G9/G10 confirmed by adversarial verification; closure recorded in the audit note §7 (rows 11, 12, 13).
- Council provenance: 11-agent council; all 4 majors and applied minors resolved in landed text; verified:false claims (ADR-context incidents: postmark-mcp malicious MCP server, ClawHub malicious-skill audit, NVIDIA NGC signing) recorded here rather than in doctrine body.
- Primary sources indexed: Pillar Security Rules File Backdoor, AWS-2025-019, Aikido skill-file propagation, GitHub secure-use/CODEOWNERS precedent; MINJA and Web3 memory-injection studies, OWASP Agent Memory Guard, Mem0 deletion APIs; MT-Bench judge biases, kappa-deflation and agreement-protocol studies, coin-flip-judge and master-key papers, Trust-or-Escalate, Anthropic and OpenAI judge-config practice.
