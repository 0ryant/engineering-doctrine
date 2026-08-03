# ADR 0031: Add Agent Identity, MCP Revision Pinning, And ASI Crosswalk Coverage

- **Status:** Accepted
- **Decision date:** 2026-08-03
- **Recorded date:** 2026-08-03
- **Retrospective:** No

## Context

The August 2026 landscape sweep and gap audit ([research-bleeding-edge-ai-landscape-gap-audit-2026-08.md](../../doctrine/evolution/research-bleeding-edge-ai-landscape-gap-audit-2026-08.md)) confirmed, with adversarial verification, three high-severity findings this ADR closes as one batch (precedent: ADR 0023's A1–A8 batch):

- **G1 — agent identity.** Doctrine had generic workload identity but no first-class notion of the **agent as principal**: no sponsor lifecycle, no orphan handling, no per-interaction credential narrowing, no on-behalf-of attribution. Two independent standards tracks (NIST CAISI agent-identity concept paper; IETF identity-assertion JWT grant draft) and every major platform (Entra Agent ID, A2A signed Agent Cards, AWS AgentCore Identity) converged on agent-specific identity in 2026; "agents as generic service accounts" is now an identifiable anti-pattern.
- **S1 — ASI vocabulary absence.** The OWASP Top 10 for Agentic Applications 2026 (ASI01–ASI10, final 2025-12-09) became the auditor vocabulary for agentic risk; doctrine's Tier-D and agentic-loop controls existed but were unmapped to ASI identifiers, so coverage could not be demonstrated.
- **S2 — MCP under-specification.** Doctrine treated MCP as generic RPC hygiene while the protocol became revision-sensitive: the 2025-06-18 revision established the OAuth 2.1 resource-server model with RFC 8707 resource indicators, and the 2026-07-28 revision introduced a stateless core (removing `Mcp-Session-Id`), an extensions framework, and a twelve-month deprecation policy. Host/server pairs that do not declare a revision silently diverge on auth and transport semantics.

Council provenance: drafted and adversarially critiqued by an 11-agent council (per-item prep readers, primary-source verifiers, drafters; doctrine-fidelity and practicality critics). All critique blockers and majors were resolved before landing — notably scoping the MCP pin mandate to estate-governed/production pairs, downgrading external hardening documents from "apply" to informative, and moving the gateway/session rule into its canonical section.

## Decision

1. **Agent identity (normative).** New §2.1 in [zero-trust-and-workload-identity.md](../../doctrine/principles/zero-trust-and-workload-identity.md): agents holding their own workload identity MUST act under a distinct, agent-labeled principal resolvable to a **named human sponsor** (orphaned agents are disabled); credentials SHOULD be per-interaction and SHOULD NOT be standing grants; on-behalf-of delegation chains MUST be preserved in audit records. Scope excludes tools acting entirely under a human's interactive session. The compliance floor is a dedicated, labeled per-agent principal — purpose-built identity platforms are rationale, not the bar. A standards-watch block (CAISI, IETF draft, Entra Agent ID, A2A, AgentCore) is informative; any future binding routes through [revision-pinned-control-profiles.md](../../doctrine/patterns/revision-pinned-control-profiles.md). Companion edits: ai-ml-systems.md Tier D row; run-contracts.md honest-gap note recording the missing `actor` field as a v2 candidate.
2. **MCP baseline (normative).** [ai-ml-systems.md](../../doctrine/principles/ai-ml-systems.md) §7 gains an MCP-specific baseline: estate-governed/production host/server pairs MUST pin a dated spec revision via a Revision-Pinned External Control Profile (ADR 0026 mechanism; one estate-level profile enumerating pairs suffices); remote/multi-tenant servers MUST use external-IdP OAuth 2.1 with RFC 8707 resource indicators (local single-user servers MAY omit, SHOULD least-privilege); hosts SHOULD restrict to a curated allowlist (a documented estate list is conforming — no registry product required); gateways serving 2026-07-28+ pairs MUST NOT key auth/rate-limiting/session state on `Mcp-Session-Id`; NSA AISC MCP CSI and the OWASP secure-MCP guide are cited as informative hardening baselines. Companion edits: api-boundaries-and-security.md Related pointer, dependencies-supply-chain.md protocol-deprecation cadence bullet, glossary MCP refresh.
3. **ASI crosswalk (additive guidance, recorded here for provenance).** New §11 in [agentic-loop-design.md](../../doctrine/patterns/agentic-loop-design.md) mapping ASI01–ASI10 to existing doctrine controls, with honest no-coverage cells (agent/tool registry attestation, message-level inter-agent signing and anti-replay, adaptive trust calibration, watchdog agents); Anti-Patterns renumbers §11→§12 (no inbound references existed). ai-ml-systems.md §5 cites the ASI Top 10 as the complementary agentic-layer checklist.

## Alternatives Considered

### A dedicated agent-identity principle file

Rejected. Agents inherit §2's invariants; only the granularity residue (principal class, sponsor, per-interaction scope, attribution) is new. A separate file would duplicate normative identity text and drift.

### Pinning MCP guidance to prose in ai-ml-systems.md without the profile mechanism

Rejected. ADR 0026 exists precisely so external revisioned baselines carry owner, authority source, boundary, and migration state; a second ad-hoc mechanism would fork the discipline.

### Universal (unscoped) MCP revision-pin mandate

Rejected on council critique: it lands hardest on the lightest contexts (a solo developer with several stdio dev servers). Scoped to estate-governed/production pairs; local development servers get SHOULD-level guidance.

### Embedding ASI mitigations as new normative text

Rejected. The mitigations already exist in doctrine controls; the crosswalk is navigational vocabulary and adds no obligations, keeping single-home normativity.

## Consequences

### Positive

- Agent actions become attributable (sponsor, principal, delegation chain) with a floor small teams can meet.
- MCP auth/transport divergence becomes a controlled, evidence-carrying change instead of a silent upgrade.
- Agentic-risk coverage is demonstrable in ASI vocabulary, with genuine gaps recorded honestly as future work.

### Costs And Risks

- Estates operating agents must stand up sponsor records and per-agent principals; platforms without agent principal classes rely on labeling conventions.
- MCP profile records add registry upkeep; the twelve-month deprecation window requires scheduled migrations.
- The ASI crosswalk's no-coverage cells are public admissions; consumers may press for closure (tracked as future audit actions).
- Standards-watch items (CAISI, IETF draft) are pre-final and will need revisiting.

## Consumer Impact

**Change class:** normative for consumers operating agents with their own workload identity or estate-governed/production MCP pairs; additive guidance otherwise (crosswalk, references, glossary).

**Compatibility proposal:** 0.x minor. New MUST/SHOULD claims activate only for the scoped contexts above; consumers without agents or MCP estates inherit no new obligations. One section renumber in agentic-loop-design.md (§11→§12 Anti-Patterns) with no known consumers of the old number.

## Acceptance Evidence

- Audit provenance: gaps G1/S2 and stale S1 confirmed by adversarial verification in the August 2026 gap audit; closure recorded in its §7 action list (rows 1, 4, 6).
- Council provenance: 11-agent draft council; 1 blocker and 5 majors from the critique phase resolved in the landed text.
- Primary sources indexed in REFERENCES.md: MCP 2025-06-18 and 2026-07-28 changelogs, MCP Registry posture, NSA AISC MCP CSI, OWASP secure-MCP guide and ASI Top 10, NIST CAISI/NCCoE, IETF identity-assertion draft, Entra Agent ID, A2A v1.0, AWS AgentCore Identity.
