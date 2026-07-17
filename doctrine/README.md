# Doctrine

This folder captures durable engineering doctrine for scaffolds and templates.

**This repository (license, how to contribute, security):** see root [README.md](../README.md#license), [CONTRIBUTING.md](../CONTRIBUTING.md), and [GOVERNANCE.md](../GOVERNANCE.md).

It is split intentionally:

- **`principles/`** — **Timeless intent**: platform-agnostic outcomes, constraints, and trade-offs. Change rarely; cite **rationale** and **references** when you do.
- **`tooling/`** — **Illustrative implementation**: example stacks, filenames, and bots that **one** estate might use. Change often; keep **surface contracts** stable (see `principles/build.md`).
- **`tooling/estates/`** — **Optional supplements**: concrete product mappings for a **specific** organisation or cloud—never global law.
- **`patterns/`** — how surfaces fit together in real repositories.
- **`checklists/`** — reviewable execution.
- **`evolution/`** — audits, MoSCoW backlogs, and notes on **why** large changes happened.

Read **[principles/timeless-principles-and-tooling.md](principles/timeless-principles-and-tooling.md)** first for how this split works.

## Start Here

### Meta (how to read this repo)

- **[SEMANTIC_INDEX.md](SEMANTIC_INDEX.md)** — **semantic route map** for humans and agents: critical ingestion set, topic routes, and evidence paths
- **[tldr-principles-and-mvp.md](tldr-principles-and-mvp.md)** — **TL;DR** spine + **minimum viable doctrine** (read this if the tree feels too large)
- **[glossary.md](glossary.md)** — terms and acronyms used across doctrine (orientation only)
- [patterns/doctrine-library-change-harness.md](patterns/doctrine-library-change-harness.md) — **maintainer workflow** for library edits (research, ADR, layers, sitemap, glossary, references)
- [patterns/how-to-read-this-doctrine.md](patterns/how-to-read-this-doctrine.md) — navigation and conflict resolution
- [patterns/doctrine-versioning-and-consumer-compatibility.md](patterns/doctrine-versioning-and-consumer-compatibility.md) — how this library labels releases and downstream compatibility impact
- [principles/timeless-principles-and-tooling.md](principles/timeless-principles-and-tooling.md) — principles vs tooling vs estate supplements

### Governance & Assurance

This is a **navigation section**, not a new doctrine layer. Files stay under `principles/`, `patterns/`, `tooling/`, and `checklists/`.

- [principles/merge-path-evidence-and-pipeline-integrity.md](principles/merge-path-evidence-and-pipeline-integrity.md) — **merge path & pipeline integrity** (binding gates, evidence, SBOM/provenance expectations; NIST / CISA / SLSA–cited)
- [patterns/engineering-controls-governance-program.md](patterns/engineering-controls-governance-program.md) — **engineering controls governance programme** (ownership, waivers, metrics, audit consumption; CSF 2.0–aligned)
- [patterns/normative-language-applicability-and-exceptions.md](patterns/normative-language-applicability-and-exceptions.md) — claim-level normative strength, composable applicability profiles, bounded exceptions, and control retirement
- [patterns/revision-pinned-control-profiles.md](patterns/revision-pinned-control-profiles.md) — **external control profiles** (governing authority, exact revision, bounded applicability, parameter/tailoring decisions, assessment evidence, exceptions, and migration; NIST SP 800-171 CUI worked profile)
- [tooling/merge-path-and-pipeline-control-suite.md](tooling/merge-path-and-pipeline-control-suite.md) — illustrative **control suite** for merge paths and pipelines
- [checklists/governance-program-readiness.md](checklists/governance-program-readiness.md) — **governance programme** readiness checklist (org-level)
- [patterns/ai-adoption-controls.md](patterns/ai-adoption-controls.md) — **AI adoption controls** (inventory & materiality, ownership & effective challenge, harm-surface testing, provider continuity, capability uplift)
- [checklists/ai-adoption-readiness.md](checklists/ai-adoption-readiness.md) — **AI adoption** readiness checklist (org/team-level)
- [patterns/ai-native-software-development-lifecycle.md](patterns/ai-native-software-development-lifecycle.md) — **AI-native delivery lifecycle** (seven gates, five record families, governed execution, typed claims, authority separation, and three closure modes)
- [patterns/outcome-and-portfolio-linkage.md](patterns/outcome-and-portfolio-linkage.md) — optional objective-to-outcome overlay for strategic/product interventions and externally required lineage
- [checklists/ai-native-sdlc-readiness.md](checklists/ai-native-sdlc-readiness.md) — profile-based lifecycle readiness for incidental assistance, governed execution, multi-agent work, high materiality, and strategic outcomes

### Adoption And Worked Examples

- [patterns/adoption-playbook.md](patterns/adoption-playbook.md) — how teams migrate toward this doctrine
- [patterns/example-order-jetstream-workflow.md](patterns/example-order-jetstream-workflow.md) — worked **fiction**: state machine + CloudEvents + JetStream
- [patterns/example-saga-payment-workflow.md](patterns/example-saga-payment-workflow.md) — worked **fiction**: saga, compensation, timeouts
- [patterns/chaos-engineering-and-game-days.md](patterns/chaos-engineering-and-game-days.md) — chaos experiments and game day pattern
- [patterns/incident-lifecycle-and-on-call-operations.md](patterns/incident-lifecycle-and-on-call-operations.md) — **incident command**, on-call, escalation, comms, handoff, post-incident actions

### Core principles

- [principles/build.md](principles/build.md) — enduring build and delivery rules
- [principles/event-contracts.md](principles/event-contracts.md) — event and message contracts (CloudEvents + versioned payloads)
- [principles/state-machines-and-workflows.md](principles/state-machines-and-workflows.md) — states, transitions, and emitted event types
- [principles/collaboration.md](principles/collaboration.md) — trunk-based workflow, collaboration, SRE rigour
- [principles/semantic-versioning.md](principles/semantic-versioning.md) — SemVer per publishable unit
- [principles/interoperability-and-standards.md](principles/interoperability-and-standards.md) — portable specs vs full stacks
- [principles/container-runtime-choice.md](principles/container-runtime-choice.md) — managed platforms vs Kubernetes
- [principles/kubernetes-platform-security.md](principles/kubernetes-platform-security.md) — when clusters are in scope
- [principles/single-source-of-truth.md](principles/single-source-of-truth.md) — DRY vs wrong abstraction
- [principles/configuration-and-secrets.md](principles/configuration-and-secrets.md) — config vs secrets, rotation
- [principles/audit-logging.md](principles/audit-logging.md) — audit fields, immutability, retention
- [principles/errors-and-failure-modes.md](principles/errors-and-failure-modes.md) — HTTP, CLI, retries
- [principles/naming-and-repo-layout.md](principles/naming-and-repo-layout.md) — repo layout, monorepo vs polyrepo
- [principles/modularity-and-ports-adapters.md](principles/modularity-and-ports-adapters.md) — ports and adapters / hexagonal boundaries
- [principles/zero-trust-and-workload-identity.md](principles/zero-trust-and-workload-identity.md) — workload identity, SPIFFE pointer
- [principles/secure-development-lifecycle.md](principles/secure-development-lifecycle.md) — SDL, vuln response, training (NIST SSDF alignment)
- [principles/ai-ml-systems.md](principles/ai-ml-systems.md) — **First-class** GenAI / RAG / agents: governance, tiers A–D, retrieval lifecycle, truth in repo
- [principles/developer-experience.md](principles/developer-experience.md) — **Developer experience**: time-to-first-change, local loop, docs findability, cognitive load, review flow

### Patterns

- [patterns/how-to-read-this-doctrine.md](patterns/how-to-read-this-doctrine.md)
- [patterns/normative-language-applicability-and-exceptions.md](patterns/normative-language-applicability-and-exceptions.md) — claim strength, activation profiles, exception records, and control lifecycle
- [patterns/doctrine-versioning-and-consumer-compatibility.md](patterns/doctrine-versioning-and-consumer-compatibility.md) — doctrine release labels, change classes, and consumer pinning guidance
- [patterns/code-review-and-change-approval.md](patterns/code-review-and-change-approval.md) — code review and merge approval (duties, blockers, latency, high-risk, **agent**-authored diffs, escalation)
- [patterns/gitops-and-declarative-operations.md](patterns/gitops-and-declarative-operations.md) — **GitOps** (declarative desired state, **reconciliation**, **drift**, **secrets** boundaries); touches build, **SSOT**, **merge** path, collaboration
- [patterns/build-surface-model.md](patterns/build-surface-model.md)
- [patterns/trunk-workflow.md](patterns/trunk-workflow.md)
- [patterns/message-channel-operations.md](patterns/message-channel-operations.md)
- [patterns/adoption-playbook.md](patterns/adoption-playbook.md)
- [patterns/example-order-jetstream-workflow.md](patterns/example-order-jetstream-workflow.md) — example order FSM + JetStream (fiction)
- [patterns/example-saga-payment-workflow.md](patterns/example-saga-payment-workflow.md) — saga payment + inventory (fiction)
- [patterns/chaos-engineering-and-game-days.md](patterns/chaos-engineering-and-game-days.md) — chaos / game days
- [patterns/incident-lifecycle-and-on-call-operations.md](patterns/incident-lifecycle-and-on-call-operations.md) — incident lifecycle, IC, on-call, escalation, comms, handoff, post-incident actions
- [patterns/webhook-ingress-security.md](patterns/webhook-ingress-security.md) — signed webhooks, replay windows, idempotency
- [patterns/idempotency-across-boundaries.md](patterns/idempotency-across-boundaries.md) — HTTP, messages, infra idempotency
- [patterns/rag-retrieval-baseline.md](patterns/rag-retrieval-baseline.md) — RAG retrieval (hybrid, eval, privacy)
- [patterns/platform-as-product-and-golden-paths.md](patterns/platform-as-product-and-golden-paths.md) — platform-as-product, golden paths, self-service, service catalog
- [patterns/run-contracts.md](patterns/run-contracts.md) — governed-execution **run contracts** (v1 envelope binding trigger, model, context, capabilities, authority, hooks, verifiers, outputs)
- [patterns/verifier-packs.md](patterns/verifier-packs.md) — **verifier packs** (mandatory mirror of every skill; 11 canonical kinds plus `custom`)
- [patterns/anti-confabulation-priming.md](patterns/anti-confabulation-priming.md) — optional **anti-confabulation priming** pattern; adopters evaluate it on representative tasks and pair it with independent verification
- [patterns/ai-adoption-controls.md](patterns/ai-adoption-controls.md) — **AI adoption controls**: inventory & materiality, ownership & independent challenge, harm-surface test matrix, third-party AI continuity, role-based capability uplift
- [patterns/ai-native-software-development-lifecycle.md](patterns/ai-native-software-development-lifecycle.md) — **AI-native SDLC**: seven gates, five record families, typed claims, governed execution, candidate-bound authority, enactment, and closure
- [patterns/outcome-and-portfolio-linkage.md](patterns/outcome-and-portfolio-linkage.md) — optional outcome/portfolio linkage for strategic work; does not invent KPIs for routine maintenance or obligations
- [patterns/revision-pinned-control-profiles.md](patterns/revision-pinned-control-profiles.md) — **revision-pinned external control profiles**: apply contractual/regulatory baselines without copying them into universal principles; NIST SP 800-171 CUI worked profile

### Skills

- [skills/anti-confabulation.skill.md](skills/anti-confabulation.skill.md) — auto-bundled into build-class run contracts; ships the verbatim priming block (SHA-256 `c138dd96…`) and the `priming_active` verifier-pack reference

### Checklists

- [checklists/build-readiness.md](checklists/build-readiness.md)
- [checklists/collaboration-readiness.md](checklists/collaboration-readiness.md)
- [checklists/platform-readiness.md](checklists/platform-readiness.md)
- [checklists/release-readiness.md](checklists/release-readiness.md)
- [checklists/developer-experience-scorecard.md](checklists/developer-experience-scorecard.md)
- [checklists/doctrine-change-checklist.md](checklists/doctrine-change-checklist.md)
- [checklists/ai-adoption-readiness.md](checklists/ai-adoption-readiness.md) — inventory/materiality, challenge, harm-surface tests, provider continuity, uplift
- [checklists/ai-native-sdlc-readiness.md](checklists/ai-native-sdlc-readiness.md) — applicability-profiled mandate, governed-execution, evidence, authority, enactment, and closure checks

### Illustrative tooling (replace with your estate’s choices)

- [tooling/build.md](tooling/build.md) — example task runners, scripts, pipeline layout
- [tooling/cloudevents.md](tooling/cloudevents.md) — CloudEvents baseline (spec evolves—verify vendor support)
- [tooling/nats-jetstream.md](tooling/nats-jetstream.md) — illustrative NATS / JetStream + CloudEvents
- [tooling/kafka-and-cloudevents.md](tooling/kafka-and-cloudevents.md) — illustrative Kafka + CloudEvents sketch
- [tooling/collaboration.md](tooling/collaboration.md) — example Git host branch rules
- [tooling/observability.md](tooling/observability.md) — example OTel and collector patterns
- [tooling/ci-platform-mapping.md](tooling/ci-platform-mapping.md) — abstract CI surfaces vs example products
- [tooling/dependency-automation.md](tooling/dependency-automation.md) — example dependency bots
- [tooling/ai-assisted-development.md](tooling/ai-assisted-development.md) — illustrative **categories** of AI-assisted dev tooling (estate picks products)
- [tooling/vector-retrieval-and-embedding-illustration.md](tooling/vector-retrieval-and-embedding-illustration.md) — illustrative **ingest → lexical → vector → rerank** stack layers

### Estate supplements (optional)

- [tooling/estates/README.md](tooling/estates/README.md)
- [tooling/estates/TEMPLATE.md](tooling/estates/TEMPLATE.md) — scaffold for a new estate
- [tooling/estates/minimum-viable-doctrine.template.md](tooling/estates/minimum-viable-doctrine.template.md) — **one-page** team pitch (5–7 principles + links)
- [tooling/estates/azure-container-runtimes.md](tooling/estates/azure-container-runtimes.md) — **example** Azure mapping only
- [tooling/estates/aws-container-runtimes.md](tooling/estates/aws-container-runtimes.md) — **stub** (no product picks)
- [tooling/estates/gcp-container-runtimes.md](tooling/estates/gcp-container-runtimes.md) — **stub** (no product picks)

### Platform, SRE, and governance principles

- [principles/ai-ml-systems.md](principles/ai-ml-systems.md) — GenAI, RAG, agents (**first-class** delivery + governance)
- [principles/data-and-migrations.md](principles/data-and-migrations.md)
- [principles/observability.md](principles/observability.md)
- [principles/testing-strategy.md](principles/testing-strategy.md)
- [principles/api-boundaries-and-security.md](principles/api-boundaries-and-security.md)
- [principles/threat-modeling-stride-lite.md](principles/threat-modeling-stride-lite.md) — STRIDE-lite trust-boundary review
- [principles/privacy-and-data-governance.md](principles/privacy-and-data-governance.md)
- [principles/reliability-slo-incidents.md](principles/reliability-slo-incidents.md) — SLOs, error budgets, incidents; **tactical** response: [patterns/incident-lifecycle-and-on-call-operations.md](patterns/incident-lifecycle-and-on-call-operations.md)
- [principles/measurement-and-dora.md](principles/measurement-and-dora.md) — current DORA delivery metrics, metric pitfalls, and the boundary between delivery signals and company objectives
- [principles/developer-experience.md](principles/developer-experience.md) — SPACE, local loop, docs findability, cognitive load
- [principles/performance-and-cost.md](principles/performance-and-cost.md)
- [principles/documentation-knowledge.md](principles/documentation-knowledge.md)
- [principles/dependencies-supply-chain.md](principles/dependencies-supply-chain.md)
- [principles/user-facing-quality.md](principles/user-facing-quality.md) — A11y, i18n, **§0 scope** (headless vs UI surfaces)

### Reference index

- [REFERENCES.md](REFERENCES.md)
- [SEMANTIC_INDEX.md](SEMANTIC_INDEX.md) — task and topic route map for ingestion
- [SITEMAP.md](SITEMAP.md) — machine-friendly file list (regenerate via `scripts/generate-doctrine-sitemap.sh`)

### Research And Evolution (Rationale, Not Operating Authority)

Use these records to understand source grounding, decisions, audits, and known gaps. Follow their linked adopted principles, patterns, and ADRs for current operating doctrine.

- [evolution/honest-review-synthesis.md](evolution/honest-review-synthesis.md) — disposition of substantive external review feedback
- [evolution/post-v0.3.0-external-review-decisions-and-v0.4.0-plan-2026-07.md](evolution/post-v0.3.0-external-review-decisions-and-v0.4.0-plan-2026-07.md) — retrospective `v0.3.0` decision register, `v0.3.1` corrections, and executable `v0.4.0` tasks
- [evolution/research-doctrine-authority-applicability-2026-07.md](evolution/research-doctrine-authority-applicability-2026-07.md) — primary-source ledger for normative language, applicability, exceptions, and control lifecycle
- [evolution/research-ai-native-sdlc-2026-07.md](evolution/research-ai-native-sdlc-2026-07.md) — primary-source and vendor-observation ledger for the AI-native SDLC
- [evolution/research-nist-sp-800-171-control-profiles-2026-07.md](evolution/research-nist-sp-800-171-control-profiles-2026-07.md) — NIST SP 800-171 revision migration and wider-doctrine applicability analysis
- [evolution/research-ai-adoption-control-gaps-2026-07.md](evolution/research-ai-adoption-control-gaps-2026-07.md) — AI adoption-control gap audit and source ledger
- [evolution/moscow-review.md](evolution/moscow-review.md), [evolution/deep-research-section-gaps.md](evolution/deep-research-section-gaps.md), and [evolution/anti-patterns-and-failure-modes-gap-analysis-2026-04.md](evolution/anti-patterns-and-failure-modes-gap-analysis-2026-04.md) — backlog and gap analyses
- [evolution/public-doctrine-benchmark-gap-analysis-2026-04.md](evolution/public-doctrine-benchmark-gap-analysis-2026-04.md) and [evolution/public-doctrine-taxonomy-scorecard-and-choice-2026-04-27.md](evolution/public-doctrine-taxonomy-scorecard-and-choice-2026-04-27.md) — public-doctrine benchmark and source-selection context
- [evolution/research-ai-ml-ops-landscape-2026-04.md](evolution/research-ai-ml-ops-landscape-2026-04.md), [evolution/research-enterprise-rag-agents-indexing-2026-04.md](evolution/research-enterprise-rag-agents-indexing-2026-04.md), and [evolution/research-internal-ai-knowledge-factory-governance-2026-04.md](evolution/research-internal-ai-knowledge-factory-governance-2026-04.md) — historical AI/ML landscape research
- [evolution/mythos-era-engineering-principles-research-2026-04-28.md](evolution/mythos-era-engineering-principles-research-2026-04-28.md) — AI-accelerated vulnerability research and adopted gap map
- [evolution/v0.3.0-release-plan.md](evolution/v0.3.0-release-plan.md) — `v0.3.0` decision register, task plan, and release gates
