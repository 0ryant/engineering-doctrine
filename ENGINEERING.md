# Engineering Doctrine

This is the compact constitution for the library: durable propositions, adoption rules, and routes to canonical detail. It applies to software, services, data and infrastructure changes, automation, and AI-assisted delivery. It does not make every control applicable to every system.

Use [doctrine/SEMANTIC_INDEX.md](doctrine/SEMANTIC_INDEX.md) to find the canonical source for a task. Topic principles own detailed obligations and trade-offs; patterns own conditional operating models; checklists derive review questions; tooling and estate files are replaceable implementation guidance. Research under `doctrine/evolution/` is evidence and history, not adopted doctrine by itself.

---

## Normative Language

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY**, when written in capitals, use the meanings in [BCP 14](https://www.rfc-editor.org/info/bcp14) ([RFC 2119](https://www.rfc-editor.org/rfc/rfc2119), [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174)). Use them at claim level and sparingly:

- **MUST/MUST NOT** — required to prevent unacceptable harm or preserve an activated contract, authority, or interoperability boundary.
- **SHOULD/SHOULD NOT** — the portable default; deviation requires understanding the consequences and recording a reason when material.
- **MAY** — a recognised option, not a requirement.
- **Contextual guidance** — requires an explicit trade-off; it is not an additional RFC keyword.
- **Example** — illustrates one implementation and is non-normative.

Applicability and exception mechanics are defined in [Normative Language, Applicability, And Exceptions](doctrine/patterns/normative-language-applicability-and-exceptions.md). An external law, contract, regulator, or policy can impose stricter requirements than this library; this library cannot waive them.

## Core Propositions

### 1. Optimise For Outcomes And Explicit Purpose

Engineering activity is not value by itself. Every material change has an accountable purpose and owner. Strategic work measures stakeholder outcomes and guardrails; maintenance, obligations, incidents, compatibility, and risk reduction use the mandate appropriate to their class. See [measurement-and-dora.md](doctrine/principles/measurement-and-dora.md), [documentation-knowledge.md](doctrine/principles/documentation-knowledge.md), and [outcome-and-portfolio-linkage.md](doctrine/patterns/outcome-and-portfolio-linkage.md).

### 2. Make Ownership, Authority, And Accountability Explicit

Know who owns the system, who may request and produce change, what evidence is required, who may authorise it, and which identity enacts it. Advice, implementation, verification, authorisation, and enactment are distinct duties even when one platform supports several. See [collaboration.md](doctrine/principles/collaboration.md), [code-review-and-change-approval.md](doctrine/patterns/code-review-and-change-approval.md), and [merge-path-evidence-and-pipeline-integrity.md](doctrine/principles/merge-path-evidence-and-pipeline-integrity.md).

### 3. Keep Changes Reviewable, Reversible, And Observable

Prefer small, coherent changes through a protected integration path. Make rollout, containment, rollback or forward recovery, and runtime observation proportionate to blast radius. See [collaboration.md](doctrine/principles/collaboration.md), [trunk-workflow.md](doctrine/patterns/trunk-workflow.md), and [reliability-slo-incidents.md](doctrine/principles/reliability-slo-incidents.md).

### 4. Define And Verify Material Boundaries

Version and validate contracts at consumer, service, event, data, policy, and artefact boundaries. Select a stable interoperable shape that fits the boundary; avoid undocumented payloads and accidental compatibility promises. See [event-contracts.md](doctrine/principles/event-contracts.md), [api-boundaries-and-security.md](doctrine/principles/api-boundaries-and-security.md), and [semantic-versioning.md](doctrine/principles/semantic-versioning.md).

### 5. Automate Discriminating Evidence On The Controlled Change Path

Local and CI checks SHOULD agree on the relevant properties. Passing automation proves only what its tests can discriminate; high-impact change adds domain, security, policy, or human challenge where required. Promote the immutable artefact that was tested and approved. See [build.md](doctrine/principles/build.md), [testing-strategy.md](doctrine/principles/testing-strategy.md), and [merge-path-evidence-and-pipeline-integrity.md](doctrine/principles/merge-path-evidence-and-pipeline-integrity.md).

### 6. Design Failure, Retry, Recovery, And Reconciliation

Externally retried or redelivered commands need an idempotency or duplicate-handling strategy; the underlying domain transition need not itself be idempotent. Define timeouts, partial-failure behaviour, compensation, recovery, and reconciliation before they are needed. See [errors-and-failure-modes.md](doctrine/principles/errors-and-failure-modes.md), [idempotency-across-boundaries.md](doctrine/patterns/idempotency-across-boundaries.md), and [data-and-migrations.md](doctrine/principles/data-and-migrations.md).

### 7. Protect Proportionately To Risk

Protect identities, data, dependencies, build and deployment systems, runtime boundaries, and sensitive operations using least privilege and maintained security mechanisms. Applicability follows exposure, materiality, data class, external authority, and recoverability—not a universal algorithm or product menu. See [secure-development-lifecycle.md](doctrine/principles/secure-development-lifecycle.md), [dependencies-supply-chain.md](doctrine/principles/dependencies-supply-chain.md), [privacy-and-data-governance.md](doctrine/principles/privacy-and-data-governance.md), and [revision-pinned-control-profiles.md](doctrine/patterns/revision-pinned-control-profiles.md).

### 8. Preserve Operability And Learn From Incidents

Material paths have useful telemetry, ownership, runbooks, service objectives where appropriate, and tested recovery. Security-sensitive and materially consequential actions leave durable audit evidence without turning all telemetry into surveillance. Incidents produce accountable learning and tracked change. See [observability.md](doctrine/principles/observability.md), [audit-logging.md](doctrine/principles/audit-logging.md), [reliability-slo-incidents.md](doctrine/principles/reliability-slo-incidents.md), and [incident-lifecycle-and-on-call-operations.md](doctrine/patterns/incident-lifecycle-and-on-call-operations.md).

### 9. Prefer Simple, Replaceable Designs With Controlled Coupling

Separate domain decisions from infrastructure concerns where that improves changeability and testing. I/O belongs in components whose explicit responsibility is I/O; there is no universal four-layer architecture. Use one authority per concept, allow intentional replication with reconciliation, and refactor existing modules when that yields a more coherent design. See [modularity-and-ports-adapters.md](doctrine/principles/modularity-and-ports-adapters.md), [single-source-of-truth.md](doctrine/principles/single-source-of-truth.md), and [timeless-principles-and-tooling.md](doctrine/principles/timeless-principles-and-tooling.md).

### 10. Govern AI-Assisted Change Without Creating A Second Delivery Path

AI may analyse, design, implement, review, and recommend; policy and accountable people authorise. Governed executions are bounded by run contracts, material claims receive discriminating challenge, and production observation closes the loop. Incidental assistance remains lightweight, but its output receives the same candidate controls when it enters delivery. See [ai-ml-systems.md](doctrine/principles/ai-ml-systems.md), [ai-native-software-development-lifecycle.md](doctrine/patterns/ai-native-software-development-lifecycle.md), and [run-contracts.md](doctrine/patterns/run-contracts.md).

## Applicability And Profiles

Apply controls by composing the relevant dimensions rather than assigning one permanent tier to a repository:

- exposure and consumer reach;
- criticality, blast radius, and reversibility;
- data sensitivity and external obligations;
- operating model and recovery needs;
- change autonomy and observability; and
- compatibility scope.

Start with the baseline that makes further change safe, then activate public-service, critical-production, regulated-data, platform, AI-assisted, governed-agent, or other profiles as the system requires. Satisfy compatible obligations together and use the stricter result where controls protect the same property. When methods or authorities genuinely conflict, record the conflict and obtain an accountable decision; this library cannot override governing external authority.

## Exceptions And Control Health

A material exception identifies the rule, scope, reason and residual risk, authority, owner, compensating control, evidence/detection, effective date, expiry, and remediation or replacement. Expiry without renewal ends the exception; it does not create permanent precedent. See [normative-language-applicability-and-exceptions.md](doctrine/patterns/normative-language-applicability-and-exceptions.md).

Every material control SHOULD identify the failure it addresses, evidence that it works, operating cost, owner, review trigger, and simplify/retire condition. Controls may be retained, tuned, replaced, or retired through accountable evidence; activity count is not proof of effectiveness. See [engineering-controls-governance-program.md](doctrine/patterns/engineering-controls-governance-program.md).

## Minimum Viable Adoption

For a team starting from little shared doctrine, establish these foundations first:

1. one local-and-CI quality gate;
2. a protected default branch and reviewed small changes;
3. a documented first-change path and named ownership;
4. one material boundary contract with examples and validation;
5. correlated telemetry on the main path; and
6. rollback/learning ownership when change fails.

Use [TL;DR And Minimum Viable Doctrine](doctrine/tldr-principles-and-mvp.md), [adoption-playbook.md](doctrine/patterns/adoption-playbook.md), and the relevant readiness checklists. Do not copy the whole reference tree into a team's daily checklist.

## Canonical Topic Routes

| Need | Start here |
| --- | --- |
| Build, CI, artefacts, delivery | [build.md](doctrine/principles/build.md), [build-surface-model.md](doctrine/patterns/build-surface-model.md) |
| Branching, review, approval | [collaboration.md](doctrine/principles/collaboration.md), [code-review-and-change-approval.md](doctrine/patterns/code-review-and-change-approval.md) |
| Security, vulnerabilities, supply chain | [secure-development-lifecycle.md](doctrine/principles/secure-development-lifecycle.md), [dependencies-supply-chain.md](doctrine/principles/dependencies-supply-chain.md) |
| External controls and regulatory profiles | [revision-pinned-control-profiles.md](doctrine/patterns/revision-pinned-control-profiles.md) |
| APIs, events, retries, workflows | [api-boundaries-and-security.md](doctrine/principles/api-boundaries-and-security.md), [event-contracts.md](doctrine/principles/event-contracts.md), [idempotency-across-boundaries.md](doctrine/patterns/idempotency-across-boundaries.md) |
| Data, privacy, migrations | [data-and-migrations.md](doctrine/principles/data-and-migrations.md), [privacy-and-data-governance.md](doctrine/principles/privacy-and-data-governance.md) |
| Observability, reliability, incidents | [observability.md](doctrine/principles/observability.md), [reliability-slo-incidents.md](doctrine/principles/reliability-slo-incidents.md) |
| Platforms, developer experience, measurement | [platform-engineering.md](doctrine/principles/platform-engineering.md), [developer-experience.md](doctrine/principles/developer-experience.md), [measurement-and-dora.md](doctrine/principles/measurement-and-dora.md) |
| AI, RAG, agents, AI-native delivery | [ai-ml-systems.md](doctrine/principles/ai-ml-systems.md), [ai-native-software-development-lifecycle.md](doctrine/patterns/ai-native-software-development-lifecycle.md) |
| Full task routing and research evidence | [SEMANTIC_INDEX.md](doctrine/SEMANTIC_INDEX.md), [REFERENCES.md](doctrine/REFERENCES.md) |

## Compatibility Note For `v0.3.0`

This version replaces the previous detailed umbrella and its deep section anchors with this compact constitution. Consumers that link to an old umbrella subsection SHOULD link to the canonical principle or pattern named above. The underlying topic files remain the stable source of detailed guidance; no directory taxonomy has changed.
