# Platform, SRE, And Extended Readiness Checklist

Use when adopting or auditing **data**, **observability**, **reliability**, **API security**, and **supply-chain** doctrine beyond core build/trunk.

```text
[ ] SLOs defined for user-facing paths; error budget policy agreed (reliability-slo-incidents.md)
[ ] Incident response and on-call: severity matrix, incident state doc, comms/escalation **habits**, and post-incident action tracking aligned with patterns/incident-lifecycle-and-on-call-operations.md (scale **roles** to org size; avoid silent “no IC” in multi-team incidents)
[ ] OpenTelemetry or documented exception; logs correlate with traces (observability.md + tooling/observability.md)
[ ] Production runtime chosen per container-runtime-choice.md; concrete products recorded in estate catalogue or tooling/estates/
[ ] Multi-team / platform slice: golden paths, self-service guardrails, and service-catalog metadata aligned with patterns/platform-as-product-and-golden-paths.md (ownership, interfaces, runbooks/SLO pointers)
[ ] If Kubernetes in use: kubernetes-platform-security.md baseline applied
[ ] Database migrations follow expand/contract or documented maintenance window (data-and-migrations.md)
[ ] Backup RPO/RTO documented; restore tested on cadence (data-and-migrations.md)
[ ] API limits: pagination, payload size, rate limits on auth routes (api-boundaries-and-security.md)
[ ] OWASP API Top 10 risks reviewed for public APIs (api-boundaries-and-security.md)
[ ] If using **GenAI**, **RAG**, **fine-tuning**, or **agentic** automation: **tier** (A–D) and SoR rules in [principles/ai-ml-systems.md](../principles/ai-ml-systems.md) (§§6–7 eval, retrieval, MCP-class tools; §8 anti-patterns); RAG eval + isolation per [patterns/rag-retrieval-baseline.md](../patterns/rag-retrieval-baseline.md); pipeline ownership per [tooling/vector-retrieval-and-embedding-illustration.md](../tooling/vector-retrieval-and-embedding-illustration.md) where applicable; [glossary.md](../glossary.md) **GenAIOps** for ops vocabulary
[ ] STRIDE-lite threat-modeling pass for internet-facing or high-impact surfaces (threat-modeling-stride-lite.md); residual risks tracked
[ ] PII inventory and retention periods documented (privacy-and-data-governance.md)
[ ] Dependency automation enabled (Renovate or Dependabot per dependency-automation.md)
[ ] SBOM policy matches what you ship (dependencies-supply-chain.md)
[ ] CI abstract surfaces mapped to real host (ci-platform-mapping.md)
[ ] Test pyramid healthy; flaky tests have owners (testing-strategy.md)
[ ] Published or consumed async events use the selected explicit envelope contract (CloudEvents by portable default, or a documented equivalent) and versioned payload schemas where applicable (event-contracts.md)
[ ] Event-backed workflows document states/transitions and map commits to stable event types where applicable (state-machines-and-workflows.md)
[ ] Message channels have DLQ/poison, replay posture, and backlog metrics per patterns/message-channel-operations.md (if the system uses queues/topics)
[ ] Delivery performance trended using stable definitions (measurement-and-dora.md) where org tracks Four Keys or equivalents
[ ] Chaos engineering or game days exercised for high-blast-radius systems on a cadence (principles/reliability-slo-incidents.md §5; pattern: patterns/chaos-engineering-and-game-days.md)
[ ] DR / failover drills and multi-region assumptions validated where data-and-migrations.md §4 applies
[ ] Webhook ingress hardened where third-party HTTP callbacks are accepted (patterns/webhook-ingress-security.md)
[ ] ADRs or decision log for major architectural forks (documentation-knowledge.md)
[ ] Customer-facing web: WCAG target documented (user-facing-quality.md)
```
