# ADR 0033: Add Agentic Threat Vocabulary, Agent Responders, And GenAI Telemetry

- **Status:** Accepted
- **Decision date:** 2026-08-03
- **Recorded date:** 2026-08-03
- **Retrospective:** No

## Context

Third closure batch from the August 2026 gap audit ([research-bleeding-edge-ai-landscape-gap-audit-2026-08.md](../../doctrine/evolution/research-bleeding-edge-ai-landscape-gap-audit-2026-08.md)), closing three adversarially verified high-severity findings. (The audit's G6 is distinct from ADR 0010's closed "G6"; identifiers here refer to the 2026-08 audit.)

- **G5 — agentic systems as threat-modeling targets.** STRIDE's fixed-role, static-boundary walk under-captures agentic attack classes: an agent is simultaneously process, data store, dataflow, and actor; goal hijack spoofs no credential and cascading multi-agent failure is not resource exhaustion. The ASI Top 10 and NIST AI 100-2e2025 supply the vocabulary; the §11 crosswalk (ADR 0031) supplies the control mapping.
- **G6 — agent responders in incident operations.** Ops agents shipped across vendors (Azure SRE Agent, PagerDuty virtual responder, incident.io AI SRE, Datadog Bits) with converged design: approval-gated by default, hypothesis-shaped RCA. Doctrine's incident pattern was all-human.
- **G7 — GenAI telemetry.** Model-mediated calls are the fastest-growing cost/audit surface; the OTel GenAI semantic conventions exist but are pre-stable (Development; main-repo `gen_ai.*` deprecated at v1.42.0 in favour of a dedicated repository). Doctrine had no per-call signal floor and no content-capture default.

Council provenance: 11-agent draft council; critique returned 1 major (the reversibility-routed remediation lane lacked a declared owner and artifact for the pre-approved action list) and minors, all resolved in landed text. Notable evidence discipline: the widely quoted ~81%-vs-11% agent-hijack statistic was **omitted** from doctrine body because the verified source is the US/UK AISI hijacking-evaluations blog, not AI 100-2e2025 as the audit had attributed; product release-status timestamps were kept out of body text.

## Decision

1. **Agentic threat vocabulary (additive guidance — no new obligations).** New §3.2 "Agentic Systems As Targets (Threat-Landscape Note)" in [threat-modeling-stride-lite.md](../../doctrine/principles/threat-modeling-stride-lite.md): when the system under review contains an agent (Tier D, or Tier B with agent-writable memory), extend the STRIDE walk with ASI01–ASI10 and AI 100-2e2025 vocabulary as auditable naming; every item routes to the owning doctrine surface (agentic-loop §11 crosswalk, ai-ml-systems §7, zero-trust §2.1); MAESTRO named as optional deeper methodology for multi-agent topologies. REFERENCES gains NIST AI 100-2e2025 (first active citation), CSA MAESTRO, and the OWASP Multi-Agentic guide — a disclosed scope extension beyond audit row 5's single-file target, mirroring the S1 precedent.
2. **Agent responders (normative, scoped to estates operating them).** New §10 in [incident-lifecycle-and-on-call-operations.md](../../doctrine/patterns/incident-lifecycle-and-on-call-operations.md) (old §10 renumbers to §11; no inbound references existed): rostered **agent responder** role with a named accountable human owner (page-steal/stop authority; never IC — command is a human accountability); remediation routed by **reversibility and blast radius** — the reversible-action list is pre-declared outside incident time by the agent's owner with the service owner, lives in the runbook/service catalogue, versioned like the severity matrix, never extended mid-incident; agent RCA enters as **ranked leads** requiring human confirmation before the postmortem record; every action in the state doc and audit trail with the §2.1 attribution chain; **circuit breaker** (rate/loop caps) on the incident→issue→coding-agent loop with the self-healing-drift-masking anti-pattern named; responder agents treated as an injection surface (agentic-loop §9). Composes with the AI-native SDLC §10/§13 authority rules rather than defining parallel autonomy.
3. **GenAI telemetry (normative minimum set; informative tooling mapping).** New §7 in [observability.md](../../doctrine/principles/observability.md): per-call minimum signal set for production model-mediated calls — model id/version (responding model as pricing key), token counts in/out, percentile latency (TTFT MUST where exposed, SHOULD where it needs custom wiring), cost-attribution key, run/session correlation id for agentic paths (joining cost-and-finops §7 budget units), tool-call identifiers, retrieval linkage; **content capture off by default** (opt-in, scoped, routed through privacy §5.3); cardinality discipline preserved. The principles text is deliberately schema-neutral; the OTel GenAI conventions mapping lands in [tooling/observability.md](../../doctrine/tooling/observability.md) with an explicit stability warning (Development; pin the adopted version; isolate `gen_ai.*` names behind a mapping layer). No single external source mandates this exact set; it is composed from the OTel instruments, vendor practice, and the library's own cost/audit requirements — this ADR is its authority.

## Alternatives Considered

### Replace STRIDE with an agentic framework (MAESTRO) for agent systems

Rejected. STRIDE remains the baseline pass every team already knows; agentic vocabulary extends it, and MAESTRO is named as optional depth — a framework swap would fork the threat-modeling discipline.

### Fold agent responders into the AI-native SDLC pattern

Rejected. The SDLC pattern owns authority/closure invariants; incident operations has residue those rules do not cover (roster semantics, reversibility routing at incident tempo, RCA handling, handoff of agent state). Composition, not duplication.

### Mandate the OTel GenAI attribute names directly

Rejected. The conventions are pre-stable and actively churning (v1.41 restructure, v1.42.0 deprecation, repository move); naming them in normative text would buy silent breakage. Schema-neutral floor in principles, versioned mapping in tooling.

## Consequences

### Positive

- Agentic threats get named in auditor vocabulary during design review, with mitigations routed to controls that already exist.
- Estates adopting ops agents inherit a complete, compose-only rulebook: ownership, kill authority, bounded auto-execution, honest RCA, full audit trail, loop caps.
- Token spend becomes attributable per call and aggregable per run/use-case; content capture becomes a governed decision instead of a silent default.

### Costs And Risks

- The reversible-action list adds a maintained artifact per agent-operating service (runbook/service-catalogue entry).
- TTFT and run-correlation instrumentation may need client-side wiring on some stacks (the MUST/SHOULD split bounds this).
- OTel GenAI convention churn will require mapping-layer updates; the §7 review trigger is the conventions' stable release.
- Vendor observations (Azure/PagerDuty/incident.io/Datadog status) will stale; they live in references and this ADR, not body text.

## Consumer Impact

**Change class:** additive guidance for G5; normative for estates operating agent responders (G6) and for production GenAI/agent call paths (G7 minimum set + content-capture default); estates with neither change nothing.

**Compatibility proposal:** 0.x minor. One section renumber in incident-lifecycle-and-on-call-operations.md (§10→§11) with no known consumers of the old number. The G7 content-capture default may require estates currently logging prompts by default to move to an explicit opt-in record — that is the intended tightening.

## Acceptance Evidence

- Audit provenance: G5/G6/G7 confirmed by adversarial verification; closure recorded in the audit note §7 (rows 5, 8, 9).
- Council provenance: 11-agent council; the major (reversible-action list ownership/artifact) and all applied minors resolved in landed text; mis-attributed statistics kept out of doctrine body.
- Primary sources indexed: NIST AI 100-2e2025, ASI Top 10, CSA MAESTRO + OWASP Multi-Agentic guide, Bishop Fox STRIDE analysis; Azure SRE Agent docs, PagerDuty/incident.io/Datadog responder observations, AKS loop write-up; OTel GenAI semantic-conventions repository.

**Review provenance:** the council review cited above was model self-review (agent critics re-reading agent drafts). No independent human or domain review of this ADR has been recorded as of 2026-09-03.
