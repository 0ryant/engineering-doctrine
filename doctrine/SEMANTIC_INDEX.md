# Semantic Index

Purpose: help humans and agents choose the right doctrine files for a task. This page is a routing index, not a new doctrine layer. When a route points to a principle, pattern, tooling page, checklist, ADR, or evolution note, the linked source remains authoritative.

Use this with [SITEMAP.md](SITEMAP.md): the sitemap lists every Markdown file; this index explains what to ingest and why.

---

## Critical Agent Context

Before substantive analysis, edits, or generated guidance in this repository, ingest this minimum set:

1. [../AGENTS.md](../AGENTS.md) - repo-specific agent instructions and the doctrine change harness requirement.
2. [tldr-principles-and-mvp.md](tldr-principles-and-mvp.md) - compact doctrine spine and minimum viable doctrine.
3. [patterns/how-to-read-this-doctrine.md](patterns/how-to-read-this-doctrine.md) - authority order, reading paths, and conflict resolution.
4. This file - semantic routes by task and topic.
5. The topic route below that matches the request.

If editing [doctrine/](.), [../docs/adr/](../docs/adr/), or [../ENGINEERING.md](../ENGINEERING.md), also ingest:

- [patterns/doctrine-library-change-harness.md](patterns/doctrine-library-change-harness.md) - research, ADR, layering, navigation, verification.
- [checklists/doctrine-change-checklist.md](checklists/doctrine-change-checklist.md) - pre-merge coverage list.
- [patterns/doctrine-versioning-and-consumer-compatibility.md](patterns/doctrine-versioning-and-consumer-compatibility.md) - change class and consumer impact.
- [../docs/adr/README.md](../docs/adr/README.md) - ADR format and index.

Agent rule of thumb: summarize from this index only for routing. For claims, quote or paraphrase the canonical source doc that the route names.

---

## Authority Order

| Layer | Use for | Notes |
| --- | --- | --- |
| [../AGENTS.md](../AGENTS.md) | Agent behavior while editing this repo | Always-on contributor instructions. |
| [../ENGINEERING.md](../ENGINEERING.md) | Umbrella engineering guide | Good headline index; principle files win on detail. |
| [principles/](principles/) | Durable, portable doctrine | Cite these for obligations and stable intent. |
| [patterns/](patterns/) | How principles compose in real repos | Use for workflow, adoption, and operational shape. |
| [tooling/](tooling/) | Replaceable implementation illustrations | Do not treat product examples as global law. |
| [tooling/estates/](tooling/estates/) | Org/cloud-specific supplements | Optional, local to an estate. |
| [checklists/](checklists/) | Reviewable execution | Use when assessing readiness or PR completeness. |
| [evolution/](evolution/) | Research, audits, and gap notes | Evidence and context, not always adopted doctrine. |
| [../docs/adr/](../docs/adr/) | Decisions about this library | Structural and policy-shaping repo decisions. |
| [REFERENCES.md](REFERENCES.md) | External authorities and internal map | Audit and navigation index. |
| [SITEMAP.md](SITEMAP.md) | Complete generated file list | Regenerate after doctrine Markdown add/remove/rename. |

---

## Semantic Spine

These are the high-signal concepts agents should keep in working memory while reading the rest of the corpus.

| Concept | Canonical files | Compress to |
| --- | --- | --- |
| Truth in repo | [principles/ai-ml-systems.md](principles/ai-ml-systems.md), [principles/documentation-knowledge.md](principles/documentation-knowledge.md) | Git, ADRs, contracts, and merged docs are authoritative; chats, indexes, embeddings, and prompts are derivatives. |
| Principles vs tooling | [principles/timeless-principles-and-tooling.md](principles/timeless-principles-and-tooling.md) | Durable intent lives in principles; replaceable examples and vendor choices live in tooling or estates. |
| Minimum viable doctrine | [tldr-principles-and-mvp.md](tldr-principles-and-mvp.md), [patterns/adoption-playbook.md](patterns/adoption-playbook.md) | Start with quality gate, protected trunk, first-change path, one boundary contract, observability, ownership. |
| Contracts first | [../ENGINEERING.md](../ENGINEERING.md), [principles/event-contracts.md](principles/event-contracts.md), [principles/semantic-versioning.md](principles/semantic-versioning.md) | Boundary shapes are versioned, validated, and treated as build failures when broken. |
| Explicit build surfaces | [principles/build.md](principles/build.md), [patterns/build-surface-model.md](patterns/build-surface-model.md), [tooling/build.md](tooling/build.md) | Quality, build/publish, deploy, verify, and execution surfaces are named and reproducible. |
| Trunk and small change | [principles/collaboration.md](principles/collaboration.md), [patterns/trunk-workflow.md](patterns/trunk-workflow.md), [patterns/code-review-and-change-approval.md](patterns/code-review-and-change-approval.md) | Short-lived branches, reviewed merges, green main, small PRs, explicit high-risk review. |
| Merge path integrity | [principles/merge-path-evidence-and-pipeline-integrity.md](principles/merge-path-evidence-and-pipeline-integrity.md), [patterns/engineering-controls-governance-program.md](patterns/engineering-controls-governance-program.md), [tooling/merge-path-and-pipeline-control-suite.md](tooling/merge-path-and-pipeline-control-suite.md) | The merge path and pipeline definitions are controlled surfaces with evidence, gates, waivers, and audit consumption. |
| Security in the loop | [principles/secure-development-lifecycle.md](principles/secure-development-lifecycle.md), [principles/api-boundaries-and-security.md](principles/api-boundaries-and-security.md), [principles/dependencies-supply-chain.md](principles/dependencies-supply-chain.md), [principles/threat-modeling-stride-lite.md](principles/threat-modeling-stride-lite.md) | Security is designed, tested, reviewed, scanned, and governed before production. |
| Operability | [principles/observability.md](principles/observability.md), [principles/reliability-slo-incidents.md](principles/reliability-slo-incidents.md), [patterns/incident-lifecycle-and-on-call-operations.md](patterns/incident-lifecycle-and-on-call-operations.md) | Logs, metrics, traces, runbooks, SLOs, incidents, and post-incident actions are connected. |
| AI, RAG, and agents | [principles/ai-ml-systems.md](principles/ai-ml-systems.md), [patterns/rag-retrieval-baseline.md](patterns/rag-retrieval-baseline.md), [tooling/vector-retrieval-and-embedding-illustration.md](tooling/vector-retrieval-and-embedding-illustration.md) | AI systems are governed systems; retrieval indexes and agent tools have ownership, eval, migration, ACL, audit, and merge-gate discipline. |
| Run contracts and verifier packs | [patterns/run-contracts.md](patterns/run-contracts.md), [patterns/verifier-packs.md](patterns/verifier-packs.md) | Every agent run compiles to one typed envelope; every skill ships a sibling pack. Stage-2 silent-stub and skill-amplification classes are closed structurally at the post-run gate. |
| Model routing policy | [../docs/adr/0012-model-routing-policy.md](../docs/adr/0012-model-routing-policy.md), [../contracts/router-policy.v1.schema.json](../contracts/router-policy.v1.schema.json) | The router policy is a v1 contract with a structural 3-tier shape: `tiers: { premium, default, narrow_scope }`. Escalation rules, refusal rules (non-empty, evidence-backed), two-tier cost ceilings. Refuse-routing is `const: true` — no soft refusals. narrow_scope (Haiku-PRIMED, canonical 73, Δ +10 self-canonical) carries mandatory external review at sample rate 1.0. The empirical refusal cohort (canonical-31 haiku, +10 self-canonical greenfield Δ, CC-2 interpreter wrapper) IS the commercial moat. |
| Developer experience | [principles/developer-experience.md](principles/developer-experience.md), [checklists/developer-experience-scorecard.md](checklists/developer-experience-scorecard.md), [principles/measurement-and-dora.md](principles/measurement-and-dora.md) | Safe change should be easy: fast local loop, findable docs, clear ownership, low cognitive load, timely review. |

---

## Task Routes

Use the left column as intent matching. Ingest the route before answering or editing.

| Task or user intent | Read first | Then read |
| --- | --- | --- |
| Edit doctrine, ADRs, or the umbrella guide | [patterns/doctrine-library-change-harness.md](patterns/doctrine-library-change-harness.md), [checklists/doctrine-change-checklist.md](checklists/doctrine-change-checklist.md) | [patterns/doctrine-versioning-and-consumer-compatibility.md](patterns/doctrine-versioning-and-consumer-compatibility.md), [../docs/adr/README.md](../docs/adr/README.md), [REFERENCES.md](REFERENCES.md), [SITEMAP.md](SITEMAP.md) |
| Decide where new content belongs | [principles/timeless-principles-and-tooling.md](principles/timeless-principles-and-tooling.md), [patterns/doctrine-library-change-harness.md](patterns/doctrine-library-change-harness.md) | [doctrine/README.md](README.md), [REFERENCES.md](REFERENCES.md), related principle or pattern route |
| Onboard to the library quickly | [tldr-principles-and-mvp.md](tldr-principles-and-mvp.md), [patterns/how-to-read-this-doctrine.md](patterns/how-to-read-this-doctrine.md) | [glossary.md](glossary.md), [../ENGINEERING.md](../ENGINEERING.md), [patterns/adoption-playbook.md](patterns/adoption-playbook.md) |
| Adopt doctrine in a team or org | [patterns/adoption-playbook.md](patterns/adoption-playbook.md), [tooling/estates/minimum-viable-doctrine.template.md](tooling/estates/minimum-viable-doctrine.template.md) | [checklists/build-readiness.md](checklists/build-readiness.md), [checklists/collaboration-readiness.md](checklists/collaboration-readiness.md), [checklists/developer-experience-scorecard.md](checklists/developer-experience-scorecard.md) |
| Build, CI, package, release, or delivery graph | [principles/build.md](principles/build.md), [patterns/build-surface-model.md](patterns/build-surface-model.md) | [tooling/build.md](tooling/build.md), [tooling/ci-platform-mapping.md](tooling/ci-platform-mapping.md), [checklists/build-readiness.md](checklists/build-readiness.md), [checklists/release-readiness.md](checklists/release-readiness.md) |
| Branching, PRs, review, agent-authored diffs | [principles/collaboration.md](principles/collaboration.md), [patterns/code-review-and-change-approval.md](patterns/code-review-and-change-approval.md) | [patterns/trunk-workflow.md](patterns/trunk-workflow.md), [tooling/collaboration.md](tooling/collaboration.md), [checklists/collaboration-readiness.md](checklists/collaboration-readiness.md) |
| Governance, assurance, pipeline controls, audit packs | [principles/merge-path-evidence-and-pipeline-integrity.md](principles/merge-path-evidence-and-pipeline-integrity.md), [patterns/engineering-controls-governance-program.md](patterns/engineering-controls-governance-program.md) | [tooling/merge-path-and-pipeline-control-suite.md](tooling/merge-path-and-pipeline-control-suite.md), [checklists/governance-program-readiness.md](checklists/governance-program-readiness.md), [docs/adr/0006-add-governance-and-assurance-navigation-and-adopt-adrs.md](../docs/adr/0006-add-governance-and-assurance-navigation-and-adopt-adrs.md) |
| Security, vulnerability response, supply chain | [principles/secure-development-lifecycle.md](principles/secure-development-lifecycle.md), [principles/dependencies-supply-chain.md](principles/dependencies-supply-chain.md) | [principles/threat-modeling-stride-lite.md](principles/threat-modeling-stride-lite.md), [principles/merge-path-evidence-and-pipeline-integrity.md](principles/merge-path-evidence-and-pipeline-integrity.md), [evolution/mythos-era-engineering-principles-research-2026-04-28.md](evolution/mythos-era-engineering-principles-research-2026-04-28.md) |
| APIs, HTTP boundaries, service calls, SSRF, browser controls | [principles/api-boundaries-and-security.md](principles/api-boundaries-and-security.md), [principles/errors-and-failure-modes.md](principles/errors-and-failure-modes.md) | [principles/zero-trust-and-workload-identity.md](principles/zero-trust-and-workload-identity.md), [patterns/webhook-ingress-security.md](patterns/webhook-ingress-security.md), [patterns/idempotency-across-boundaries.md](patterns/idempotency-across-boundaries.md) |
| Events, messaging, workflows, sagas | [principles/event-contracts.md](principles/event-contracts.md), [principles/state-machines-and-workflows.md](principles/state-machines-and-workflows.md) | [patterns/message-channel-operations.md](patterns/message-channel-operations.md), [tooling/cloudevents.md](tooling/cloudevents.md), [patterns/example-order-jetstream-workflow.md](patterns/example-order-jetstream-workflow.md), [patterns/example-saga-payment-workflow.md](patterns/example-saga-payment-workflow.md) |
| Idempotency, retries, duplicate delivery | [patterns/idempotency-across-boundaries.md](patterns/idempotency-across-boundaries.md), [principles/errors-and-failure-modes.md](principles/errors-and-failure-modes.md) | [patterns/message-channel-operations.md](patterns/message-channel-operations.md), [principles/event-contracts.md](principles/event-contracts.md), [principles/data-and-migrations.md](principles/data-and-migrations.md) |
| Data migrations, backup, recovery, retention | [principles/data-and-migrations.md](principles/data-and-migrations.md), [principles/privacy-and-data-governance.md](principles/privacy-and-data-governance.md) | [patterns/idempotency-across-boundaries.md](patterns/idempotency-across-boundaries.md), [principles/reliability-slo-incidents.md](principles/reliability-slo-incidents.md) |
| Observability, SLOs, incidents, on-call | [principles/observability.md](principles/observability.md), [principles/reliability-slo-incidents.md](principles/reliability-slo-incidents.md) | [patterns/incident-lifecycle-and-on-call-operations.md](patterns/incident-lifecycle-and-on-call-operations.md), [patterns/chaos-engineering-and-game-days.md](patterns/chaos-engineering-and-game-days.md), [tooling/observability.md](tooling/observability.md) |
| Platform engineering, golden paths, service catalog | [patterns/platform-as-product-and-golden-paths.md](patterns/platform-as-product-and-golden-paths.md), [principles/developer-experience.md](principles/developer-experience.md) | [principles/measurement-and-dora.md](principles/measurement-and-dora.md), [checklists/platform-readiness.md](checklists/platform-readiness.md), [checklists/developer-experience-scorecard.md](checklists/developer-experience-scorecard.md) |
| Runtime choice, Kubernetes, container platforms | [principles/container-runtime-choice.md](principles/container-runtime-choice.md), [principles/kubernetes-platform-security.md](principles/kubernetes-platform-security.md) | [principles/interoperability-and-standards.md](principles/interoperability-and-standards.md), [tooling/estates/README.md](tooling/estates/README.md), estate supplement if present |
| GitOps, declarative operations, drift | [patterns/gitops-and-declarative-operations.md](patterns/gitops-and-declarative-operations.md), [principles/single-source-of-truth.md](principles/single-source-of-truth.md) | [principles/build.md](principles/build.md), [principles/collaboration.md](principles/collaboration.md), [principles/configuration-and-secrets.md](principles/configuration-and-secrets.md) |
| AI systems, RAG, embeddings, model operations | [principles/ai-ml-systems.md](principles/ai-ml-systems.md), [patterns/rag-retrieval-baseline.md](patterns/rag-retrieval-baseline.md) | [tooling/vector-retrieval-and-embedding-illustration.md](tooling/vector-retrieval-and-embedding-illustration.md), [evolution/research-ai-ml-ops-landscape-2026-04.md](evolution/research-ai-ml-ops-landscape-2026-04.md), [evolution/research-enterprise-rag-agents-indexing-2026-04.md](evolution/research-enterprise-rag-agents-indexing-2026-04.md) |
| Internal AI agents, knowledge factory, MCP, handoffs | [principles/ai-ml-systems.md](principles/ai-ml-systems.md), [evolution/research-internal-ai-knowledge-factory-governance-2026-04.md](evolution/research-internal-ai-knowledge-factory-governance-2026-04.md) | [patterns/code-review-and-change-approval.md](patterns/code-review-and-change-approval.md), [principles/audit-logging.md](principles/audit-logging.md), [tooling/ai-assisted-development.md](tooling/ai-assisted-development.md), [evolution/research-enterprise-rag-agents-indexing-2026-04.md](evolution/research-enterprise-rag-agents-indexing-2026-04.md) |
| Agent run contracts and verifier packs (typed envelope of execution) | [patterns/run-contracts.md](patterns/run-contracts.md), [patterns/verifier-packs.md](patterns/verifier-packs.md) | [../contracts/run-contract.v1.schema.json](../contracts/run-contract.v1.schema.json), [../contracts/verifier-pack.v1.schema.json](../contracts/verifier-pack.v1.schema.json), [patterns/anti-confabulation-priming.md](patterns/anti-confabulation-priming.md), [principles/ai-ml-systems.md](principles/ai-ml-systems.md), [principles/audit-logging.md](principles/audit-logging.md), [patterns/code-review-and-change-approval.md](patterns/code-review-and-change-approval.md) |
| Anti-confabulation priming, self-score calibration for build-class agents | [patterns/anti-confabulation-priming.md](patterns/anti-confabulation-priming.md), [skills/anti-confabulation.skill.md](skills/anti-confabulation.skill.md) | [patterns/run-contracts.md](patterns/run-contracts.md) (§3.5 auto-bundle), [patterns/verifier-packs.md](patterns/verifier-packs.md) (`priming_active` kind), [../contracts/verifier-pack.v1.schema.json](../contracts/verifier-pack.v1.schema.json), [principles/ai-ml-systems.md](principles/ai-ml-systems.md) |
| Choose model + escalate on FALSIFIED + refuse known failure modes | [../docs/adr/0012-model-routing-policy.md](../docs/adr/0012-model-routing-policy.md), [../contracts/router-policy.v1.schema.json](../contracts/router-policy.v1.schema.json) | [../contracts/examples/default-production.router-policy.yaml](../contracts/examples/default-production.router-policy.yaml), [../contracts/examples/enterprise-strict.router-policy.yaml](../contracts/examples/enterprise-strict.router-policy.yaml), [../contracts/examples/experimental-haiku-narrow-scope.router-policy.yaml](../contracts/examples/experimental-haiku-narrow-scope.router-policy.yaml), [patterns/anti-confabulation-priming.md](patterns/anti-confabulation-priming.md), [../scripts/validate-contracts-v1.py](../scripts/validate-contracts-v1.py) |
| Documentation, ADRs, runbooks, onboarding | [principles/documentation-knowledge.md](principles/documentation-knowledge.md), [../docs/adr/README.md](../docs/adr/README.md) | [patterns/how-to-read-this-doctrine.md](patterns/how-to-read-this-doctrine.md), [glossary.md](glossary.md), [REFERENCES.md](REFERENCES.md) |
| Metrics, DORA, DevEx measurement | [principles/measurement-and-dora.md](principles/measurement-and-dora.md), [principles/developer-experience.md](principles/developer-experience.md) | [checklists/developer-experience-scorecard.md](checklists/developer-experience-scorecard.md), [patterns/platform-as-product-and-golden-paths.md](patterns/platform-as-product-and-golden-paths.md) |
| User-facing quality, accessibility, i18n | [principles/user-facing-quality.md](principles/user-facing-quality.md) | [principles/api-boundaries-and-security.md](principles/api-boundaries-and-security.md), [principles/testing-strategy.md](principles/testing-strategy.md) |
| Naming, repo layout, modular architecture | [principles/naming-and-repo-layout.md](principles/naming-and-repo-layout.md), [principles/modularity-and-ports-adapters.md](principles/modularity-and-ports-adapters.md) | [principles/single-source-of-truth.md](principles/single-source-of-truth.md), [patterns/build-surface-model.md](patterns/build-surface-model.md) |

---

## Research And Evidence Routes

Use evolution notes when a task asks why the library moved, what gaps remain, or what external landscape informed the doctrine.

| Question | Evidence route |
| --- | --- |
| What does external review say about the library? | [evolution/honest-review-synthesis.md](evolution/honest-review-synthesis.md), [evolution/public-doctrine-benchmark-gap-analysis-2026-04.md](evolution/public-doctrine-benchmark-gap-analysis-2026-04.md), [evolution/public-doctrine-taxonomy-scorecard-and-choice-2026-04-27.md](evolution/public-doctrine-taxonomy-scorecard-and-choice-2026-04-27.md) |
| What gaps or thin areas were known? | [evolution/moscow-review.md](evolution/moscow-review.md), [evolution/deep-research-section-gaps.md](evolution/deep-research-section-gaps.md), [evolution/anti-patterns-and-failure-modes-gap-analysis-2026-04.md](evolution/anti-patterns-and-failure-modes-gap-analysis-2026-04.md) |
| Why are AI/RAG/agents first-class? | [docs/adr/0005-treat-ai-ml-rag-and-agentic-workflows-as-first-class-governed-systems.md](../docs/adr/0005-treat-ai-ml-rag-and-agentic-workflows-as-first-class-governed-systems.md), [evolution/research-ai-ml-ops-landscape-2026-04.md](evolution/research-ai-ml-ops-landscape-2026-04.md), [evolution/research-enterprise-rag-agents-indexing-2026-04.md](evolution/research-enterprise-rag-agents-indexing-2026-04.md) |
| Why the vulnerability-storm / Mythos-era additions? | [evolution/mythos-era-engineering-principles-research-2026-04-28.md](evolution/mythos-era-engineering-principles-research-2026-04-28.md), [docs/adr/0010-record-mythos-era-vulnerability-storm-research-and-doctrine-gaps.md](../docs/adr/0010-record-mythos-era-vulnerability-storm-research-and-doctrine-gaps.md) |
| What is the authoritative external-source index? | [REFERENCES.md](REFERENCES.md) |

---

## Agent Ingestion Protocol

1. Classify the request: edit, review, explain, adopt, research, or route.
2. Read the Critical Agent Context section above.
3. Read the matching Task Route. If multiple routes match, prefer the highest-risk route first: security, merge path, privacy, AI/agents, data, release.
4. For edits, run the doctrine change harness: research basis, ADR when structural or policy-shaping, layered placement, cross-links, navigation, verification.
5. For answers, cite the canonical file route in the response rather than this index unless the question is specifically about navigation.
6. Treat [SITEMAP.md](SITEMAP.md) as completeness, [REFERENCES.md](REFERENCES.md) as audit/navigation, and this file as semantic intent.

Residual risk: this index is hand-curated. When adding or removing first-class doctrine, update this file alongside [README.md](README.md), [REFERENCES.md](REFERENCES.md), and generated [SITEMAP.md](SITEMAP.md) if the route changes.
