# Doctrine

This folder captures durable engineering doctrine for scaffolds and templates.

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

- [patterns/how-to-read-this-doctrine.md](patterns/how-to-read-this-doctrine.md) — navigation and conflict resolution
- [principles/timeless-principles-and-tooling.md](principles/timeless-principles-and-tooling.md) — principles vs tooling vs estate supplements
- [evolution/moscow-review.md](evolution/moscow-review.md) — latest **thin-area / audit / MoSCoW** snapshot
- [evolution/honest-review-synthesis.md](evolution/honest-review-synthesis.md) — condensed **external review** signal
- [patterns/adoption-playbook.md](patterns/adoption-playbook.md) — how teams migrate toward this doctrine

### Core principles

- [principles/build.md](principles/build.md) — enduring build and delivery rules
- [principles/event-contracts.md](principles/event-contracts.md) — event and message contracts (CloudEvents + versioned payloads)
- [principles/state-machines-and-workflows.md](principles/state-machines-and-workflows.md) — states, transitions, and emitted event types
- [principles/collaboration.md](principles/collaboration.md) — trunk-based workflow, collaboration, SRE rigour
- [principles/semantic-versioning.md](principles/semantic-versioning.md) — SemVer per publishable unit
- [principles/interoperability-and-standards.md](principles/interoperability-and-standards.md) — portable specs vs full stacks
- [principles/container-runtime-choice.md](principles/container-runtime-choice.md) — managed platforms vs Kubernetes
- [principles/kubernetes-platform-security.md](principles/kubernetes-platform-security.md) — when clusters are in scope

### Patterns

- [patterns/how-to-read-this-doctrine.md](patterns/how-to-read-this-doctrine.md)
- [patterns/build-surface-model.md](patterns/build-surface-model.md)
- [patterns/trunk-workflow.md](patterns/trunk-workflow.md)
- [patterns/message-channel-operations.md](patterns/message-channel-operations.md)
- [patterns/adoption-playbook.md](patterns/adoption-playbook.md)

### Checklists

- [checklists/build-readiness.md](checklists/build-readiness.md)
- [checklists/collaboration-readiness.md](checklists/collaboration-readiness.md)
- [checklists/platform-readiness.md](checklists/platform-readiness.md)
- [checklists/release-readiness.md](checklists/release-readiness.md)
- [checklists/doctrine-change-checklist.md](checklists/doctrine-change-checklist.md)

### Illustrative tooling (replace with your estate’s choices)

- [tooling/build.md](tooling/build.md) — example task runners, scripts, pipeline layout
- [tooling/cloudevents.md](tooling/cloudevents.md) — CloudEvents baseline (spec evolves—verify vendor support)
- [tooling/nats-jetstream.md](tooling/nats-jetstream.md) — illustrative NATS / JetStream + CloudEvents
- [tooling/collaboration.md](tooling/collaboration.md) — example Git host branch rules
- [tooling/observability.md](tooling/observability.md) — example OTel and collector patterns
- [tooling/ci-platform-mapping.md](tooling/ci-platform-mapping.md) — abstract CI surfaces vs example products
- [tooling/dependency-automation.md](tooling/dependency-automation.md) — example dependency bots

### Estate supplements (optional)

- [tooling/estates/README.md](tooling/estates/README.md)
- [tooling/estates/TEMPLATE.md](tooling/estates/TEMPLATE.md) — scaffold for a new estate
- [tooling/estates/minimum-viable-doctrine.template.md](tooling/estates/minimum-viable-doctrine.template.md) — **one-page** team pitch (5–7 principles + links)
- [tooling/estates/azure-container-runtimes.md](tooling/estates/azure-container-runtimes.md) — **example** Azure mapping only
- [tooling/estates/aws-container-runtimes.md](tooling/estates/aws-container-runtimes.md) — **stub** (no product picks)
- [tooling/estates/gcp-container-runtimes.md](tooling/estates/gcp-container-runtimes.md) — **stub** (no product picks)

### Platform, SRE, and governance principles

- [principles/data-and-migrations.md](principles/data-and-migrations.md)
- [principles/observability.md](principles/observability.md)
- [principles/testing-strategy.md](principles/testing-strategy.md)
- [principles/api-boundaries-and-security.md](principles/api-boundaries-and-security.md)
- [principles/threat-modeling-stride-lite.md](principles/threat-modeling-stride-lite.md) — STRIDE-lite trust-boundary review
- [principles/privacy-and-data-governance.md](principles/privacy-and-data-governance.md)
- [principles/reliability-slo-incidents.md](principles/reliability-slo-incidents.md)
- [principles/measurement-and-dora.md](principles/measurement-and-dora.md) — DORA / Four Keys vs doctrine
- [principles/performance-and-cost.md](principles/performance-and-cost.md)
- [principles/documentation-knowledge.md](principles/documentation-knowledge.md)
- [principles/dependencies-supply-chain.md](principles/dependencies-supply-chain.md)
- [principles/user-facing-quality.md](principles/user-facing-quality.md) — A11y, i18n, **§0 scope** (headless vs UI surfaces)

### Reference index

- [REFERENCES.md](REFERENCES.md)
- [SITEMAP.md](SITEMAP.md) — machine-friendly file list (regenerate via `scripts/generate-doctrine-sitemap.sh`)
