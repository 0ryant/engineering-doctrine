# Code Review And Change Approval (DevOps-Native)

**Portable intent:** Peer review and automation on the same merge path are the default way software changes are scrutinised and approved—not a separate ITIL Change Advisory ceremony for every deploy. This pattern spells out author and reviewer **duties**, **blockers vs nits**, **review latency** expectations, **high-risk** change classes, **agent-authored** work, and **escalation** when reviewers and authors disagree.

**Applies to** teams using protected trunk, PR/MR review, and policy-as-code gates. **Complements** [collaboration.md](../principles/collaboration.md) and [merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md). It does **not** replace [engineering-controls-governance-program.md](engineering-controls-governance-program.md) for org-wide waivers and audit when law or policy require approvals beyond the merge path.

**Not this:** a standing CAB for routine application work; tickets for their own sake; “four eyes” that are the same person twice. **This:** clear roles, explicit risk, and measurable review health.

---

## 1. Author duties

- **Size for review** — Prefer one concern per PR and the [concrete size bounds in collaboration.md §3](../principles/collaboration.md); split work or use feature flags and thin vertical slices when the change is large.
- **Description is load-bearing** — State what changed, why, and how to verify (tests, flags, environment). Link tickets, ADRs, or RFCs when the change implements a prior decision.
- **Self-review before request** — Read the full diff; run the same quality gate you expect in CI; catch obvious issues so reviewers spend time on judgment, not syntax.
- **Call out review hotspots** in the body—migrations, auth, cryptography, new dependencies, pipeline or workflow edits, agent-definition or steering edits, public API or schema changes—so the right people look first.
- **Respond to review** — Answer questions, push fixes, or explain trade-offs; resolve or re-open threads per team convention. Stalled author responses are a throughput problem, not only a reviewer problem.
- **No surprise generated bulk** — If a significant slice is LLM- or tool-authored, follow §6; reviewers should not have to guess what is unverified.

---

## 2. Reviewer duties

- **Timeliness** — First response within team latency norms (§4). Chronic unavailability of review is a delivery risk: escalate per §7 and [measurement-and-dora.md](../principles/measurement-and-dora.md).
- **Read with intent to merge** — Assume good faith; look for correctness, security, operability, contract impact, and revertability.
- **Approve only when you are willing to be wrong with the author** — You share post-merge ownership of outcomes for the scope you approved, within team norms.
- **Distinguish blockers from nits** — Use §3; do not conflate preference with safety or correctness.
- **CODEOWNERS and security paths** — If you are a required reviewer for a path, treat that responsibility like an on-call slice for that merge: defer or reassign if you cannot meaningfully review in time.
- **Ask questions** when uncertain — A clarifying question is not a personal attack; a drive-by approval on high-risk change is negligence when the diff deserved scrutiny.

---

## 3. Blocker vs non-blocker (merge policy)

| Class | Treat as | Examples (typical) |
| --- | --- | --- |
| **Merge-blocking** (request changes) | Must be resolved before merge, or a **time-bounded exception** is recorded (owner, expiry, compensating control); align with [merge-path §2 invariant 7](../principles/merge-path-evidence-and-pipeline-integrity.md) for gate waivers | Wrong or untested core logic; security flaw; breaks API contract or migration safety; pipeline change that weakens or bypasses gates; missing rollback story for a high-risk deploy; unmet regulatory obligation. |
| **Non-blocking (nit, suggestion, follow-up)** | May merge if author and team accept follow-up debt; prefer a **tracked issue** for substantive “later” work | Naming, style (where not auto-fixed), micro-optimisations, optional observability, documentation nits. |
| **Editorial** | Bot or owner can fix in a follow-up if policy allows | Typos, formatting only. |

**Rules that reduce review fights:** (a) Let required checks own mechanical quality (lint, format) so review is not a linter substitute. (b) Nits default to **comments**, not “request changes,” unless the team explicitly distinguishes comment vs block in the tool. (c) If a nit is held as blocking, the reviewer states why it is safety- or contract-relevant; otherwise it is a false blocker.

---

## 4. Review latency expectations

- **Measure** at least time-to-first-review and time-to-merge for default-branch work; align with DORA and [measurement-and-dora.md](../principles/measurement-and-dora.md). Chronic delay is a **bottleneck** to fix (capacity, spreading ownership, smaller PRs), not only the author’s fault.
- **Set explicit targets** per estate. Examples only—tune to your org:

| Urgency / risk | Indicative first-review target (business hours) | Notes |
| --- | --- | --- |
| Standard product change | Under one business day | Smaller PRs make this believable. |
| High-risk (§5) | Under four business hours, or a dedicated on-call / security review rotation for hot paths | May need a reviewer pool, not a single hero. |
| Hotfix or sev-impacting | Minutes to an hour, with the right on-call or duty holder | Not the same bar as optional tech-debt review; post-merge review or retro if break-glass was used. |

- **Nights and weekends** — Do not treat informal response times as SLOs unless on-call or compensation covers that class of work.
- If review latency breaks delivery, treat it like any constraint: WIP limits, more reviewers, smaller batches, or escalation (§7)—not only backlog resentment.

---

## 5. Security, infra, schema, and high-risk change classes

These changes deserve **extra clarity** in the PR body, **often more than one** informed reviewer, and stricter **blocker discipline**—**proportional** governance, not a Change Advisory Board for every line of application code.

| Class | What to expect (illustrative) | Doctrine links |
| --- | --- | --- |
| **Security** (authZ, secrets, crypto, new internet-exposed surface) | Threat and abuse notes; security or champion review; no rubber stamps on privilege and data handling | [api-boundaries-and-security.md](../principles/api-boundaries-and-security.md), [threat-modeling-stride-lite.md](../principles/threat-modeling-stride-lite.md), [secure-development-lifecycle.md](../principles/secure-development-lifecycle.md) |
| **Infra / pipeline** (IaC, wide Kubernetes or cloud scope, CI that holds secrets or deploy rights) | Plan or diff reviewed; treat automation edits as high trust per merge-path pipeline rules | [merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md), [tooling/collaboration.md](../tooling/collaboration.md) |
| **Agent-definition / steering** (custom-agent files, steering or instruction files, `SKILL.md`-class skill packs, MCP server configs, prompt templates wired into delivery — in the merge-path §1 scope, i.e. steering merge-path or standing-credential automation) | Protected paths with **CODEOWNERS-style ownership**; **no self-review** and an **informed reviewer** per merge-path §2 invariant 2 (the canonical owner of both rules); **provenance and version/digest pinning** for third-party skills and MCP servers; §6 rows apply transitively when the diff is agent-authored | [merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md), [dependencies-supply-chain.md](../principles/dependencies-supply-chain.md), [run-contracts.md](run-contracts.md) §3.5, [verifier-packs.md](verifier-packs.md) §6 |
| **Schema and migrations** | Forwards and backwards compatibility story; rollback or reversible steps; data volume and lock risk | [data-and-migrations.md](../principles/data-and-migrations.md) |
| **Public API and contracts** | Versioning; consumer impact; deprecation path if breaking | [semantic-versioning.md](../principles/semantic-versioning.md), [event-contracts.md](../principles/event-contracts.md) |
| **Feature flags with safety implications** | Default off; owner; staged rollout | [collaboration.md §4](../principles/collaboration.md) |

Regulated sectors or customer contracts may add approvals **outside** the PR—record them in governance and evidence systems, not as vague “CAB said no” without a retrievable record.

---

## 6. Agent-authored PRs (LLM and coding agents)

**When** code, configuration, or substantial text in the PR was produced or heavily edited by an LLM or an autonomous agent (including Copilot-sized chunks that **are** the core of the change), treat review as a **governance** concern as well as a craft concern. **Aligns** with [ai-ml-systems.md](../principles/ai-ml-systems.md).

| Rule | Rationale |
| --- | --- |
| **Record the method, not a co-author** | A non-human tool **MUST NOT** be named in an authorship field (`Author`, `Co-Authored-By`, or any successor conferring authorship standing): authorship, ownership, and accountability are held whole by the human author, and a tool holds none of them. What **MUST** be recoverable instead is **how the candidate was produced** — see §6.1. “I used help” is not enough for audit or teaching, and neither is a co-author line. |
| **Author must explain and own the change** | Merge implies a human can defend behaviour under incident pressure. Mystery diffs are higher risk than honest unfamiliarity. |
| **Same automated gates as any other PR** | Tests, scans, and policies apply; no blanket waiver because “AI wrote it.” |
| **Dependency and lockfile diffs reviewed explicitly** | Agent-added dependencies are the **slopsquatting** surface; every added or changed package passes the pre-install verification gate ([ai-ml-systems.md §4](../principles/ai-ml-systems.md)) and lockfile-diff review per [dependencies-supply-chain.md §7](../principles/dependencies-supply-chain.md). |
| **No rubber stamps on large generated volume** | Spurious green CI on weak tests is worse when generation is fast; reviewers sample and request targeted proof (property-based, contract, or scenario tests). |
| **Separation of duties (where your estate requires it)** | The same person should not be the only check when an agent touches production credentials, protected paths, or control bypass—match enterprise SoD policy. |
| **Security-critical path: human must understand the diff** | For authn/authz, secrets/crypto, tenancy, schema safety, **CI/CD** privilege, or internet-exposed boundaries, the **approving human** must be able to **defend behaviour under incident pressure**; targeted **abuse-case** or adversarial evidence is expected when generation touched those paths ([testing-strategy.md](../principles/testing-strategy.md) §5, [merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md) §2). |

**VCS “agents”** (Renovate, release bots) follow [collaboration.md](../principles/collaboration.md) and [tooling/collaboration.md](../tooling/collaboration.md) (bot accounts, auto-merge where allowed). This section is about **LLM- and agent-generated content in the diff**, not about dependency bots alone.

### 6.1 The Method Record

A **method record** states how a change candidate was produced. It makes **no authorship claim**: authorship names who is accountable, the method record describes process, and they are separately addressable facts ([normative-language-applicability-and-exceptions.md](normative-language-applicability-and-exceptions.md) §2). Recording the method is the author's own engineering evidence about a change they already own — it does not dilute ownership any more than a build attestation dilutes it.

The record **MUST** carry a **class** and the **revision-pinned identity** of any harness and governing ruleset that shaped the output:

| Class | Meaning |
| --- | --- |
| `generated` | Model or agent output accepted substantially as produced; human review was inspection, not material revision. |
| `curated` | Model or agent output produced under a **declared harness and governing ruleset**, then **materially revised** by the named author, who can defend the result without reference to the tool. |
| `authored` | Written by the named author. Ordinary tool assistance (completion, formatting, refactoring engines) does not change this class. |

The class asserted **MUST** be the one the author can defend under review. `curated` is not a courtesy upgrade from `generated`; it claims the harness and ruleset were pinned and the output materially revised, and it is falsifiable by reading the diff against the cited revisions.

Applicability: **MUST** in estate-governed and production delivery paths where this section already applies; **SHOULD** for local single-user development. `authored` changes **MAY** omit the record — its absence is the default claim, so ordinary work carries no stamping burden.

This library specifies the **schema and class vocabulary only**. Concrete harness identifiers, ruleset identifiers, and transport (commit trailer, PR template field, or signed attestation) are estate bindings and are deliberately unnamed here ([ADR 0027](../../docs/adr/0027-keep-public-doctrine-implementation-neutral.md)). A commit-trailer binding might read:

```
Produced-With: harness=<id>@<rev>; doctrine=<id>@<rev>; class=curated
```

`Produced-With` is a recommended key because it names tooling without implying standing; an estate **MAY** choose another, provided it is not an authorship field. Estates with an external **transparency obligation** route that duty through a registered control profile ([revision-pinned-control-profiles.md](revision-pinned-control-profiles.md)) rather than through this record — a method record is engineering evidence, not a compliance artifact ([privacy-and-data-governance.md](../principles/privacy-and-data-governance.md) §5.4).

Rationale and rejected alternatives: [ADR 0043](../../docs/adr/0043-replace-agent-coauthorship-disclosure-with-a-method-record.md). An agent producing the candidate can be primed to apply this section with the [`method-record-classification` skill](../skills/method-record-classification/SKILL.md), whose sibling pack checks authorship fields and record form on the candidate commit.

---

## 7. Escalation: reviewer is wrong, or author is sure the reviewer is

Disagreement is normal; **indefinite stall** and silent resentment are failure modes. Assume good faith first; escalate with **links and rationale**, not drama.

1. **Clarify in thread** — Quote the objection; state your model of correctness or risk; ask a concrete question (for example: “If we merge this, what fails at runtime?”).
2. **Get a second opinion early** on high-risk work (§5)—do not spend days in a two-person deadlock when a third engineer or security champion can break symmetry.
3. **Tie-break using a named team norm**—for example: area code owner, tech lead, on-call with post-merge revert authority for emergencies, or engineering management for cross-team conflict. This library does not mandate a single job title; it mandates that **the tie-break path exists before week two of argument**.
4. If the reviewer cannot state a **blocker** in terms of safety, correctness, or contract (§3), treat the feedback as a non-blocker or escalate to step 3—not an unlimited veto on style.
5. If you are the **reviewer** and you may be wrong, say so; ask for a test or spec pointer; **approve** with explicit assumptions, or **downgrade** to a non-blocking suggestion when appropriate.

**Culturally unacceptable:** threats; merging with no response to substantive security feedback; bypassing required review except documented break-glass with a retrospective.

---

## 8. References and related doctrine

- [collaboration.md](../principles/collaboration.md) — trunk, PR size, feature flags, review latency
- [merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md) — gates, evidence, pipeline as security surface
- [measurement-and-dora.md](../principles/measurement-and-dora.md) — lead time, flow
- [ai-ml-systems.md](../principles/ai-ml-systems.md) — governed GenAI and agents
- [checklists/collaboration-readiness.md](../checklists/collaboration-readiness.md), [tooling/collaboration.md](../tooling/collaboration.md) — host mechanics
- [engineering-controls-governance-program.md](engineering-controls-governance-program.md) — when org-level change policy overlays the merge path

**External (orientation):** [Google’s code review intro](https://google.github.io/eng-practices/review/) (expectations and standards); your estate may adopt stricter or looser norms with written rationale.
