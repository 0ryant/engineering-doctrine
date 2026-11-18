# ADR 0059: Apply Three Constitution Rules To Settled Inconsistencies

- **Status:** Accepted
- **Decision date:** 2026-11-18
- **Recorded date:** 2026-11-18
- **Retrospective:** No
- **Deciders:** Repository operator
- **Review provenance:** Operator-requested after reading a decision sheet that grouped the open inconsistencies by the constitution rule that settles each, and operator-accepted on 2026-11-18; drafted and reviewed by a model, no independent human or domain review recorded
- **Research:** [Applying the constitution's own rules](../../doctrine/evolution/research-apply-constitution-rules-2026-11.md); findings in the [review register](../../doctrine/evolution/review-full-doctrine-2026-11-findings.json)
- **Canonical owners:** [`ENGINEERING.md`](../../ENGINEERING.md) Core Proposition 5; [Build](../../doctrine/principles/build.md) §5; [AI And ML Systems](../../doctrine/principles/ai-ml-systems.md) §4; [Threat Modeling](../../doctrine/principles/threat-modeling-stride-lite.md) §1; [Errors And Failure Modes](../../doctrine/principles/errors-and-failure-modes.md) §4; [Configuration And Secrets](../../doctrine/principles/configuration-and-secrets.md) §2; [Privacy And Data Governance](../../doctrine/principles/privacy-and-data-governance.md) §1; [Cost And FinOps](../../doctrine/principles/cost-and-finops.md) §§2, 7.1; [Observability](../../doctrine/principles/observability.md) §7.1; [Merge Path](../../doctrine/principles/merge-path-evidence-and-pipeline-integrity.md) §§2, 4; [Testing Strategy](../../doctrine/principles/testing-strategy.md) §5; [Documentation And Knowledge](../../doctrine/principles/documentation-knowledge.md) §2; [Code Review And Change Approval](../../doctrine/patterns/code-review-and-change-approval.md) §§4, 6; [Chaos Engineering And Game Days](../../doctrine/patterns/chaos-engineering-and-game-days.md) §§1, 3
- **Derived landings:** five checklists (build, release, collaboration, platform, and AI adoption readiness); [principles at a glance](../../doctrine/tldr-principles-and-mvp.md); [glossary](../../doctrine/glossary.md) (load shedding); [semantic index](../../doctrine/SEMANTIC_INDEX.md); the Application Deployment and Service API references; the build pattern and build tooling page
- **Relationship to earlier decisions:** settles 30 of the 52 inconsistencies that the [November 2026 review](../../doctrine/evolution/review-full-doctrine-2026-11.md) left for a decision, and two findings it left open. Amends one sentence of Core Proposition 5.

## Context

The November 2026 review found 52 places where two pages of this library disagree and a choice is needed. The rules are the maintainer's, so the review chose nothing.

Three sentences already in `ENGINEERING.md` settle most of them without a new judgement:

1. "Satisfy compatible obligations together and use the stricter result where controls protect the same property." (Applicability And Profiles)
2. "Use one authority per concept." (Core Proposition 9)
3. "checklists derive review questions." (opening paragraph)

This ADR applies those three sentences and nothing else. Where settling an item needs a judgement the sentences do not supply, the item is left out and listed below.

## Decision

### D1. Where two rules protect the same property, the stricter one stands

| Topic | Before | After |
| --- | --- | --- |
| Known-exploited vulnerabilities | "Highest urgency regardless" in dependencies §2; "typically outrank" in secure development §3 | Always highest urgency. Dependencies §2 owns the rule; secure development §3 points to it. |
| Duplicate protection for agent payments | SHOULD in cost and FinOps §7.1; MUST in idempotency §1 where a duplicate causes material harm | MUST in cost and FinOps §7.1, citing idempotency §1. No new MUST: the existing one is applied to its plainest case. |
| Runtime human fallback | Person-affected decisions in AI and ML systems §4 and the checklist; person-affected or otherwise high-materiality in AI adoption controls §2 | The wider scope in all three. The contest path applies where people are affected. |
| Reference to what is promoted or deployed | "Digest or equivalent", "digest or version", and three checklists that accept a tag | A digest, or an identifier the registry or store will not re-point. A tag that can be moved is not one. Build §5 says so once; Kubernetes §3, merge path invariant 9, the GitOps pattern, and the checklists follow it. |
| Claimed platforms | Build §9: exercise each claimed target before release. Build pattern and tooling: at least one other platform | Each claimed platform is exercised. A platform with no job is not claimed. The owner is unchanged; the derived pages now match it. |
| Model-call telemetry | Section applies to production and estate-governed paths; its MUST named production calls only | The MUST covers every in-scope call, as the section's applicability line states. |
| Review latency | Critical services in collaboration §2; default-branch work in code review §4 | Default-branch work. Code review §4 owns scope, measures, and targets, as collaboration §2 already said for measures. |

**One exception, kept on purpose.** Core Proposition 5 states same-artefact promotion without condition; build §5 and collaboration §6 say "where the platform allows". The unconditional form cannot be met on a platform that forces a rebuild. The condition stays, and the hole in it is closed: where a platform cannot promote the same artefact, the limitation is recorded and each rebuild is a new candidate that needs its own evidence. Core Proposition 5 and build §5 now both say so. Three implementation references already described rebuilds this way with no owner behind them.

### D2. One authority per concept

| Concept | Owner after this ADR | What the other pages do |
| --- | --- | --- |
| When to threat-model | Threat modelling §1. A pass for a new exposed API, auth flow, data store, or message topology, and for a material trust-boundary change; recorded threat assumptions for every other new surface; "not in scope" recorded for a trivial internal tool | Secure development §1, the platform checklist, and the glance row cite it |
| Change classes that need accountable human approval | AI and ML systems §4, one list: authentication and authorisation; secrets and cryptography; tenant isolation; data and schema migration; pipeline definitions, policy, and CI or deploy privilege; internet-exposed trust boundaries; irreversible operations; person-affecting automation or decisions; estate-defined classes | Lifecycle invariant 9, code review §6, and the council row in the agentic loop pattern cite it. The list is the union of the four lists it replaces, so no class loses its gate. |
| Safety bar for fault injection in production | Chaos pattern §§1–2 | Reliability §5 keeps the intent and a pointer |
| Exercise deadlines after an architecture change | Two clocks with two owners: a game day within 60 days (chaos pattern §3) and a walk of each affected runbook within 30 days (documentation §2) | "Align with" is removed; the pattern names the shorter clock and its owner |
| Minimum cost-allocation keys | Cost and FinOps §2, five keys | Namespace labels carry the same five keys; `team` becomes `owner-team` and `product` is added |
| Pinning of third-party skills and tool servers | Merge path invariant 2 states the rule: provenance recorded, version or digest pinned | Code review §5 cites it |
| Human review of agent-authored dependency and lockfile diffs | Code review §6, typed MUST there | Dependencies §§2 and 7 already cite it. The MUST existed only in a page that deferred to this one. |
| "Tier-1" | Documentation §2: on-call pages, revenue, safety | Data and migrations and the chaos pattern cite it. The adversarial-testing tiers in testing strategy §5 become named risk classes (privileged, exposed, ordinary, docs-only), so "Tier 1" no longer means the second of four. |
| Conflicts on merge-path detail | The conflict rule in `ENGINEERING.md` | "This file wins" is removed from merge path §4. The file still owns merge-path detail; it does not outrank the constitution. |

The agentic loop pattern keeps its own list for a different concept: the classes of run-time tool action that start at "approve before irreversible". One sentence there now says the slider governs run-time actions, and that a change in a high-impact class needs human approval at every slider position.

### D3. A checklist prompt has a rule behind it

Five prompts or pointers had no owner. Four gain a rule; one is reworded.

| Prompt or pointer | Outcome | Strength |
| --- | --- | --- |
| "A secret that reached a shared remote is treated as exposed and rotated" (Git Hooks reference) | New rule in configuration and secrets §2: revoke or rotate first; rewriting history does not replace rotation | SHOULD |
| Reliability §7 pointed to the errors principle for timeouts and circuit breaking, which it did not contain | New §4 in errors and failure modes: a timeout on every remote call, with deadline propagation; retry only what can succeed; bounded retries with backoff and jitter; retry at one layer; circuit breaking; load shedding | SHOULD, production services |
| "Side-effecting publish actions are gated behind explicit release entrypoints" (build checklist) | New rule in build §5: a step with an outward side effect runs only from an explicit release entrypoint | SHOULD |
| "PII inventory … documented" (platform checklist) | New rule in privacy §1: a list per system of the categories of personal data it holds and whose they are | SHOULD |
| "OpenTelemetry or documented exception" (platform checklist) | Prompt reworded to the outcome the owner states: logs, metrics, and traces correlate through propagated trace context | No rule change |

### What changes in strength or scope

Each line can be struck on its own without affecting the others.

1. Agent payment duplicate protection: SHOULD becomes MUST in cost and FinOps §7.1.
2. Runtime human fallback: the principle and checklist widen to high-materiality decisions.
3. Model-call telemetry MUST: reaches estate-governed non-production paths.
4. Review latency: the principle's scope widens from critical services to default-branch work.
5. Deployed references: "version" and "tag" are accepted only where the registry makes them immutable.
6. High-impact change classes: AI and ML systems §4 gains pipeline policy, irreversible operations, and estate-defined classes; lifecycle invariant 9 gains secrets and internet-exposed boundaries.
7. Threat modelling §1 gains "every other new surface has its threat assumptions recorded", moved from secure development §1.
8. Namespace labels: four keys become five.
9. Same-artefact promotion: a rebuild is a new candidate. Core Proposition 5 is amended to say so.
10. Four added rules (D3), all SHOULD.
11. The testing risk tiers are renamed. No obligation changes.

## Control Cost And Lifecycle

| Decision | Failure addressed | Evidence | Operating cost | Review trigger |
| --- | --- | --- | --- | --- |
| D1 | A reader meets the weaker of two statements and follows it | One statement per property, found by search | Possible work where an estate followed the weaker text: payment duplicate handling, digests in manifests, a CI job per claimed platform | A stricter result proves unworkable on a real platform |
| D2 | Two pages drift apart again because both restate a list or threshold | One owner per concept; the others cite it | None for adopters; editors change one place | A cited owner is moved or collapsed (ADR 0047 part 3 would touch the lifecycle pattern, which is why the class list sits in the principle) |
| D3 secret exposure | A leaked credential stays live after history is rewritten | Rotation record for the exposed secret | One rotation per exposure | A platform that can prove no copy was fetched |
| D3 timeouts, retries, overload | One slow dependency becomes a wider outage through unbounded waits and multiplied retries | Client configuration showing timeouts, retry caps, and backoff; overload responses in service code | Design and configuration per call path | An incident traced to a rule here being wrong or missing |
| D3 publish entrypoint | A package or release is published as a side effect of an ordinary check run | Pipeline definition with a separate release trigger | One extra trigger or job | A platform where publish cannot be separated |
| D3 personal-data categories | Retention and erasure cannot be applied to data nobody has listed | A list per system | Upkeep when schemas change | A regime profile that supersedes it |

Retirement: each D3 rule can be removed with its checklist prompt. D1 and D2 are alignments; reversing one means restoring two statements and recording why they differ.

## Alternatives Considered

- **Leave the 52 open and decide each singly.** Open to the maintainer. These 30 follow from rules he has already written, so deciding them again adds no information.
- **Put the high-impact class list in the lifecycle pattern**, whose list was the widest. Not taken: ADR 0047 part 3, still Proposed, would collapse that pattern, and a principle is the more durable owner. The content is the same union either way.
- **Make same-artefact promotion unconditional**, the literal stricter result. Not taken: some platforms force a rebuild, and a rule that cannot be met is waived in practice. Requiring evidence for the rebuild keeps the property.
- **Reword the four ownerless prompts instead of adding rules.** Taken for the telemetry prompt, where the owner already states an outcome. Not taken for the other four: Core Proposition 6 promises timeouts and partial-failure behaviour that no detail page delivered, and the other three are stated as fact in pages already accepted.
- **Make leaked-secret rotation a MUST.** Not taken here. The evidence would support it with a recorded risk asymmetry, but the request was to apply existing rules, not to set a new strength.
- **Keep the numeric testing tiers and rename the criticality tier.** Not taken: "tier-1" for criticality appears in four files, the testing tiers in one.
- **Settle the agent-authority items in the same change.** Not taken: they turn on Core Proposition 2 and need the maintainer's judgement on what an agent may enact.

## Consumer Impact And Migration

Change class: **normative tightening** for D1 items 1 to 5 in the list above; **normative additions** at SHOULD for D3; **clarification** for D2 and the promotion exception; **editorial** for the tier rename and the reworded prompt. Compatibility: pre-1.0 minor.

Migration:

- Check that agent payment paths prevent or detect duplicates at the controlling boundary.
- Replace movable tags with digests in deployment references, or confirm the registry enforces immutability.
- Add a CI job for each claimed platform, or stop claiming it.
- Extend model-call telemetry to estate-governed non-production paths.
- Add `owner-team` and `product` to namespace labels.
- Review outbound calls for timeouts and retry policy; record categories of personal data per system; move publish steps behind a release trigger; rotate any secret that has reached a shared remote.
- Update references to "Tier 0" or "Tier 1" adversarial-testing gates to "privileged" and "exposed".

## Acceptance Criteria

- Each topic in D1 has one statement of strength and scope, and no derived page states a weaker one.
- Each concept in D2 has one owner, and the other pages cite it.
- Each D3 prompt traces to an owner rule, and each added rule carries a typed strength and cited sources.
- The register marks the 32 findings as settled, and the review note's decision count falls from 52 to 22.
- The ADR index lists this decision, and doctrine preflight passes.

## Residual Risk

- Applying "the stricter result" is mechanical; it cannot know why a weaker statement was written. Items 1 to 5 above are the ones to read with that in mind.
- The added rules were drafted and checked by a model against cited pages. The timeout and retry rules rest on one edited book and vendor guidance from three organisations; the publish-entrypoint rule on sources that support restricting and approving publication, not on its exact form.
- Not settled here: the remaining run-time question in AI-04 (may an agent take a reversible action in a high-impact class without approval), data corrections with no schema change (OPS-02), provenance for internal production artefacts (XC-28), cost-per-outcome timing (OPS-11), the meaning of "safe default" for an ops flag (DEL-10), agent authority, ownership form, the library's rules about itself, the nine disputed rules, and the held skill and contract corrections.
