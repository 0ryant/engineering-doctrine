# TL;DR And Minimum Viable Doctrine

Use this page when the library feels too large. The compact constitution is [ENGINEERING.md](../ENGINEERING.md); canonical detail lives in the linked principles and patterns. This page owns two things: the first adoption slice, and a one-line human-readable glance at every principle file (at the end of this page). It owns no obligation; every line here is a signpost to the file that does.

## The Shape In One Minute

- Work has an accountable purpose and owner.
- Material boundaries are explicit, versioned, and verified.
- Small changes reach a protected trunk through relevant evidence and review.
- Failure, retry, rollback, observation, and learning are designed.
- Security and governance scale with exposure, materiality, external authority, and recoverability.
- Tools and standards are scoped defaults; exceptions are explicit and expiring.
- AI assists the normal delivery path; it does not become authority or proof.

For the full ten propositions and their canonical owners, read [ENGINEERING.md](../ENGINEERING.md#core-propositions).

## Minimum Viable Doctrine

This is the smallest baseline that makes further adoption safer. It usually fits into existing repository and team records.

| Order | Establish | Evidence |
| --- | --- | --- |
| 1 | **One quality gate** — format/lint/test/contract checks in CI and one documented local command that mirrors the relevant subset. | A representative change passes locally and in CI. |
| 2 | **Protected trunk** — no routine direct mutation of the default branch; required checks and reviewed, coherent changes. | Branch policy and a merged change receipt. |
| 3 | **First-change path and ownership** — README names owner, setup, fast check, first safe change, and deeper docs. | A new contributor can reach a checked change without private instructions. |
| 4 | **One material boundary contract** — API, event, data, configuration, or policy shape with examples and validation. | Invalid examples fail the controlled path. |
| 5 | **Operability baseline** — correlated telemetry on the main path and a known place for dashboards/runbooks. | Owner can diagnose a representative failure. |
| 6 | **Recovery and learning** — rollback/containment ownership and tracked learning when change fails. | A failed change has an accountable recovery route. |

Apply [Normative Language, Applicability, And Exceptions](patterns/normative-language-applicability-and-exceptions.md) before adding profiles. Do not copy every control into every repository.

## Add Profiles When The Boundary Requires Them

- **Public or critical service:** stronger SLO, security, capacity, progressive delivery, and incident controls.
- **Sensitive or externally controlled data:** revision-pinned authority, boundary, assessment, evidence, and exception rules.
- **Platform or multi-team component:** compatibility, golden-path, ownership, and consumer migration controls.
- **AI-assisted change:** normal candidate disclosure, evidence, review, authority, and runtime observation.
- **Governed agent execution:** run contracts, least privilege, isolated workspaces, limits, receipts, and delegation controls.
- **Strategic intervention:** optional objective, measures/guardrails, intervention hypothesis, attribution, and outcome review.

Profiles compose. Use the stricter applicable control on shared scope and keep live estate decisions outside this portable library.

## Next Routes

- Adoption sequence and troubleshooting: [adoption-playbook.md](patterns/adoption-playbook.md)
- Semantic task routing: [SEMANTIC_INDEX.md](SEMANTIC_INDEX.md)
- Build and collaboration readiness: [build-readiness.md](checklists/build-readiness.md), [collaboration-readiness.md](checklists/collaboration-readiness.md)
- Developer experience: [developer-experience-scorecard.md](checklists/developer-experience-scorecard.md)
- AI-native delivery: [ai-native-software-development-lifecycle.md](patterns/ai-native-software-development-lifecycle.md), [ai-native-sdlc-readiness.md](checklists/ai-native-sdlc-readiness.md)
- External control profiles: [revision-pinned-control-profiles.md](patterns/revision-pinned-control-profiles.md)
- Terms and sources: [glossary.md](glossary.md), [REFERENCES.md](REFERENCES.md)

## Every Principle At A Glance

One line per principle file, written for a human deciding what to open. These lines are signposts, not rules: they carry no normative strength, and where a line and its file disagree the file wins and the line is a defect to fix. Each link uses the file's own title. Every active file under `principles/` appears here exactly once; a file carrying a deprecation or supersession banner drops out, and `scripts/check-principles-glance.sh` enforces both.

Start with [Timeless Principles And Replaceable Tooling](principles/timeless-principles-and-tooling.md). It explains the split the rest of the library assumes: principles say what must stay true, tooling shows one way to do it today.

### How Change Lands

| Principle | In one line |
| --- | --- |
| [Collaboration, Trunk-Based Delivery, And Operational Rigour](principles/collaboration.md) | One protected trunk, short-lived branches, small reviewed changes, async by default, and flags for risky rollout, with delivery and operations rigour built in. |
| [Build Principles](principles/build.md) | Name each build surface, keep local and CI checks in agreement, promote the same artefact where the platform allows, and keep build evidence beyond the session. |
| [Merge Path Evidence And Pipeline Integrity](principles/merge-path-evidence-and-pipeline-integrity.md) | The default-branch merge path is a controlled channel: gates bind rather than advise, evidence can be checked later, and pipeline definitions, including agent definitions that steer privileged automation, are security-relevant. |
| [Testing Strategy](principles/testing-strategy.md) | Pick evidence that can tell success from failure: a pyramid by default, contract tests at boundaries, flakes fixed or quarantined with an owner and a deadline, and depth scaled to risk. |
| [Semantic Versioning Policy](principles/semantic-versioning.md) | One version line per publishable unit, and the number says how risky the upgrade is; HTTP API versioning is separate; deprecate with a sunset, never silently. |

### Boundaries And Contracts

| Principle | In one line |
| --- | --- |
| [API Boundaries, HTTP Semantics, And API Security](principles/api-boundaries-and-security.md) | Exposed HTTP and RPC surfaces are inventoried; protected routes authenticate and authorise per object; rate limits, safe retries, and outbound-fetch defences apply; the OWASP API Top 10 is the checklist. |
| [Event And Message Contracts](principles/event-contracts.md) | Every event has a named, versioned contract before producers ship; CloudEvents is the portable envelope default; delivery semantics are written down, not assumed. |
| [Errors And Failure Modes](principles/errors-and-failure-modes.md) | Machine-readable errors at boundaries; CLIs document exit codes and keep errors on stderr; retryable and permanent failures stay distinct; safe retries are documented, and costly duplicates get idempotency or duplicate detection. |
| [State Machines, Workflows, And Event Emission](principles/state-machines-and-workflows.md) | Write the states and transitions down, give each transition one commitment story, map transitions to event types, and design sagas with compensation, timeouts, and human steps. |
| [Interoperability, Standards, And Vendor Reality](principles/interoperability-and-standards.md) | Adopt a standard's wire shape at the boundary where it fits; that is not a vote for the whole ecosystem around it. |
| [Authoritative Sources And Intentional Duplication](principles/single-source-of-truth.md) | One identified authority per concept; derivatives are regenerated or reconciled by a declared process; duplication can be intentional, and a wrong abstraction is worse than a copy. |
| [Modularity, Ports, Adapters, And Layering](principles/modularity-and-ports-adapters.md) | Let core rules depend on abstractions where that improves testing or replacement, make dependency direction explicit, and expect no mandatory layer count. |
| [Naming And Repository Layout](principles/naming-and-repo-layout.md) | Predictable homes for contracts, tests, and tooling entrypoints; consistent names; monorepo and polyrepo each carry their own ownership and versioning duties. |

### Operating It

| Principle | In one line |
| --- | --- |
| [Observability](principles/observability.md) | Logs, metrics, and traces in one correlated investigation flow; cardinality costs money; alert on symptoms and burn rate; GenAI and agent calls get a minimum telemetry floor. |
| [Reliability: SLOs, Error Budgets, And Incidents](principles/reliability-slo-incidents.md) | A few SLOs tied to user journeys, error budgets that govern velocity, incidents that produce learning, measured toil, and continuity plans for critical dependencies. |
| [Performance, Load, And Cost](principles/performance-and-cost.md) | Latency and throughput budgets on critical paths; regressions block release unless accepted with a reason; major launches are load-tested; cost is observable, and carbon where reporting requires it. |
| [Cost, FinOps, And Unit Economics](principles/cost-and-finops.md) | The governance layer over cost: spend is attributable, alerted, rightsized, and shown back; AI inference gets token budgets and circuit breakers; agents get default-deny financial authority. |
| [Container Runtime Choice: Managed Platforms Vs Kubernetes](principles/container-runtime-choice.md) | Prefer a managed application runtime when it fits; run Kubernetes only when the capabilities require it; the same delivery discipline applies either way. |

### Security

| Principle | In one line |
| --- | --- |
| [Secure Development Lifecycle And Vulnerability Response](principles/secure-development-lifecycle.md) | Design review, implementation discipline, vulnerability response, and training, mapped to NIST SSDF; a recurring failure class means process or architecture work, not only another ticket. |
| [Threat Modeling](principles/threat-modeling-stride-lite.md) | When a trust boundary changes, walk the STRIDE prompts and answer the blast-radius questions; a complement to control checklists, not a replacement. |
| [Zero Trust And Workload Identity](principles/zero-trust-and-workload-identity.md) | Network location is not authorisation; services authenticate with workload identity, short-lived by preference; agents holding their own identity get a named human sponsor; break-glass is rare, monitored, and reviewed. |
| [Configuration And Secrets](principles/configuration-and-secrets.md) | Configuration and secrets are different things; secrets live in secret stores, managed identity, or short-lived tokens and rotate; real secrets are never committed. |
| [Dependencies And Supply Chain](principles/dependencies-supply-chain.md) | Lock resolution, update on a cadence, produce SBOMs and provenance, sign artefacts, know your licences, verify AI-proposed packages before install, and treat models and datasets as dependencies. |
| [Kubernetes Platform Security](principles/kubernetes-platform-security.md) | Only when you run Kubernetes: least-privilege RBAC, default-deny network policy, restricted pods, externally sourced secrets, verified workloads, and audit switched on. |
| [Audit Logging](principles/audit-logging.md) | Privileged, security-sensitive, policy-relevant, financially material, and externally consequential actions leave protected, structured, retained audit records, distinct from operational logs. |

### Data And Privacy

| Principle | In one line |
| --- | --- |
| [Data, Migrations, Backups, And Recovery](principles/data-and-migrations.md) | Expand, migrate, contract; forward-only migrations that old and new versions can both run against; batched backfills; tested backups, retention, and disaster-recovery drills. |
| [Privacy And Data Governance](principles/privacy-and-data-governance.md) | Collect only what you need, delete on schedule, know where data lives and who processes it, and keep analytics apart from audit; impact assessments when risk to individuals is high, AI transparency only under a registered profile. |

### People, Platform, And Measurement

| Principle | In one line |
| --- | --- |
| [Developer Experience](principles/developer-experience.md) | Time-to-first-change is a product signal, the local loop is an interface, documentation is task-shaped, cognitive load is a design constraint; measure the system, not the person. |
| [Platform Engineering](principles/platform-engineering.md) | Treat the platform as a product for stream-aligned teams: the thinnest viable platform, golden paths, self-service, and cognitive load as the metric. |
| [Documentation And Organisational Knowledge](principles/documentation-knowledge.md) | Decisions in writing, runbooks for on-call, READMEs that state boundaries and ownership, and onboarding material people can find. |
| [Measurement: Delivery Performance And DORA](principles/measurement-and-dora.md) | DORA delivery metrics link practice to outcomes but are not company objectives; SPACE covers the human side of the system. |
| [User-Facing Quality: Accessibility And Internationalisation](principles/user-facing-quality.md) | When there is a user interface: accessibility is quality, not decoration; plan internationalisation early when multiple locales matter; mobile, voice, and document surfaces count. |

### AI Systems And Agents

| Principle | In one line |
| --- | --- |
| [AI And ML-Assisted Systems](principles/ai-ml-systems.md) | AI features, retrieval, and agents are ordinary governed systems: owned, risk-tiered, evaluated, audited, and changed through the same path as everything else. |
