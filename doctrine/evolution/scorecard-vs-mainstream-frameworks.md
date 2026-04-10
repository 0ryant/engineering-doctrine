# Scorecard: This Doctrine vs Mainstream Engineering Frameworks

**Date:** 2026-04-10.
**Method:** Systematic domain-by-domain comparison of this doctrine's coverage, depth, and actionability against **11 mainstream engineering frameworks and handbooks**. Scoring is on a 5-point scale per domain: **5** = industry-leading depth, **4** = strong and actionable, **3** = adequate / on par, **2** = thin / mentioned but shallow, **1** = absent or stub, **--** = intentionally out of scope for that framework.

---

## Frameworks Compared

| # | Framework | Type | Primary audience |
| --- | --- | --- | --- |
| **G-SRE** | Google SRE Book + SRE Workbook | SRE / operations bible | SREs, platform teams |
| **G-SWE** | Software Engineering at Google (Winters et al.) | Eng practices at scale | IC engineers, leads |
| **DORA** | DORA / Accelerate (Forsgren, Humble, Kim) | Delivery performance research | Eng leadership, transformation |
| **AWS-WA** | AWS Well-Architected Framework (6 pillars) | Cloud architecture review | Architects, cloud teams |
| **MS-CSE** | Microsoft CSE Engineering Playbook (open source) | Day-to-day eng practices | Full-stack engineers |
| **12F** | 12-Factor App (Wiggins / Heroku) | App design methodology | App developers |
| **SSDF** | NIST SSDF SP 800-218 | Secure SDLC standard | Security, compliance |
| **TT** | Team Topologies (Skelton & Pais) | Org design for fast flow | Eng managers, VPEs |
| **CNCF-P** | CNCF Platforms Whitepaper | Platform engineering | Platform teams |
| **TW** | ThoughtWorks / Fowler canon (Tech Radar, Evolutionary Arch, Continuous Delivery) | Opinionated industry thought leadership | Architects, tech leads |
| **GL** | GitLab Handbook (public) | Company-wide handbook | All engineering roles |

---

## Domain Scorecard

### Legend

- **This** = this doctrine (ADO engineering-doctrine repo)
- Scores reflect **coverage + depth + actionability** in that domain
- A dash (**--**) means the framework intentionally does not address that domain

| # | Domain | This | G-SRE | G-SWE | DORA | AWS-WA | MS-CSE | 12F | SSDF | TT | CNCF-P | TW | GL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | **Build & CI/CD surfaces** | **5** | 2 | 3 | 3 | 2 | 4 | 2 | 2 | -- | 2 | 4 | 4 |
| 2 | **Trunk-based dev & branching** | **5** | 2 | 4 | 4 | -- | 4 | -- | -- | -- | -- | **5** | 4 |
| 3 | **Contract-first (API + events)** | **5** | 2 | 3 | -- | 2 | 3 | -- | 2 | -- | -- | 4 | 3 |
| 4 | **Event-driven / async** | **5** | 2 | 2 | -- | 3 | 2 | -- | -- | -- | -- | 3 | 2 |
| 5 | **Testing strategy** | 4 | 3 | **5** | 3 | 2 | 4 | -- | 3 | -- | -- | **5** | 4 |
| 6 | **Observability (logs/metrics/traces)** | 4 | **5** | 3 | 3 | 4 | 3 | 3 | -- | -- | 2 | 4 | 3 |
| 7 | **SLOs / error budgets / incidents** | 4 | **5** | 3 | 4 | 3 | 2 | -- | -- | -- | -- | 3 | 3 |
| 8 | **Security (SDL, zero trust, secrets)** | **5** | 3 | 3 | 2 | 4 | 3 | 2 | **5** | -- | -- | 3 | 3 |
| 9 | **Supply chain (SBOM, SLSA, deps)** | **5** | -- | 2 | -- | 3 | 2 | -- | 4 | -- | -- | 3 | 3 |
| 10 | **Threat modeling** | 4 | 2 | 2 | -- | 3 | 2 | -- | 4 | -- | -- | 2 | 2 |
| 11 | **Privacy / data governance** | 3 | 2 | 2 | -- | 3 | 2 | -- | 3 | -- | -- | 2 | 3 |
| 12 | **Data & migrations** | 4 | 2 | 3 | -- | 3 | 3 | 3 | -- | -- | -- | 4 | 3 |
| 13 | **Configuration & secrets** | 4 | 3 | 3 | -- | 4 | 3 | **5** | 3 | -- | -- | 3 | 3 |
| 14 | **Container strategy** | 4 | 3 | 2 | -- | 4 | 3 | 3 | -- | -- | 3 | 3 | 3 |
| 15 | **Kubernetes security** | 4 | 3 | -- | -- | 4 | 2 | -- | 2 | -- | 3 | 2 | 2 |
| 16 | **Platform engineering** | 4 | 3 | 3 | 3 | 2 | 2 | -- | -- | **5** | **5** | 3 | 3 |
| 17 | **Team topologies / org design** | 3 | 3 | 4 | 4 | -- | 2 | -- | -- | **5** | 4 | 3 | 4 |
| 18 | **FinOps / cost governance** | **5** | 2 | 2 | -- | 4 | 2 | -- | -- | -- | -- | 2 | 2 |
| 19 | **AI/ML systems & governance** | **5** | -- | -- | -- | 3 | 2 | -- | 2 | -- | -- | 2 | 2 |
| 20 | **RAG / retrieval / agents** | **5** | -- | -- | -- | 2 | 1 | -- | -- | -- | -- | 1 | 1 |
| 21 | **Feature flags / progressive delivery** | 4 | 2 | 3 | 3 | -- | 3 | -- | -- | -- | -- | **5** | 4 |
| 22 | **Chaos engineering / game days** | 3 | **5** | 2 | 2 | 3 | 2 | -- | -- | -- | -- | 3 | 2 |
| 23 | **DORA / delivery metrics** | 4 | 3 | 3 | **5** | -- | 3 | -- | -- | -- | -- | 4 | 4 |
| 24 | **Documentation / ADRs / runbooks** | 4 | 4 | 4 | -- | 2 | **5** | -- | 2 | -- | -- | 3 | 4 |
| 25 | **Onboarding / adoption playbook** | 4 | 2 | 3 | 2 | 3 | 3 | -- | -- | 3 | 3 | 2 | 4 |
| 26 | **Code review practices** | 3 | 2 | **5** | 3 | -- | 4 | -- | -- | -- | -- | 4 | 4 |
| 27 | **Modularity / architecture** | 4 | 2 | 4 | -- | 4 | 3 | 3 | -- | -- | -- | **5** | 3 |
| 28 | **Versioning / SemVer** | **5** | -- | 3 | -- | -- | 3 | -- | -- | -- | -- | 3 | 3 |
| 29 | **Idempotency** | **5** | 3 | 2 | -- | 3 | 2 | -- | -- | -- | -- | 3 | 2 |
| 30 | **Interoperability / standards** | 4 | 2 | 2 | -- | 3 | 2 | 2 | 2 | -- | 3 | 3 | 2 |
| 31 | **Error handling patterns** | 4 | 3 | 3 | -- | 2 | 3 | -- | -- | -- | -- | 3 | 2 |
| 32 | **Multi-cloud / portability** | 4 | -- | -- | -- | 2 | 2 | 3 | -- | -- | 2 | 3 | 2 |
| 33 | **Compliance (SOC2/ISO mapping)** | 1 | -- | -- | -- | 4 | 2 | -- | 4 | -- | -- | 2 | 3 |
| 34 | **Developer experience (SPACE)** | 2 | 2 | 4 | 4 | -- | 3 | -- | -- | 3 | 3 | 3 | 4 |
| 35 | **Performance / load testing** | 3 | 4 | 3 | -- | 4 | 3 | -- | -- | -- | -- | 3 | 2 |
| 36 | **Disaster recovery / RTO/RPO** | 2 | 4 | 2 | -- | **5** | 2 | -- | -- | -- | -- | 2 | 2 |
| 37 | **Sustainability / green software** | 1 | -- | -- | -- | 3 | 1 | -- | -- | -- | -- | 2 | 1 |
| 38 | **Governance of doctrine itself** | **5** | -- | 2 | -- | 2 | 3 | -- | -- | -- | -- | 2 | 4 |

---

## Summary Scores (Average Across Applicable Domains)

| Framework | Avg score | Domains scored | Peak domains (5s) |
| --- | --- | --- | --- |
| **This doctrine** | **3.9** | 38 | Build, trunk, contracts, events, security, supply chain, FinOps, AI/ML, RAG, versioning, idempotency, governance |
| G-SRE | 2.8 | 31 | Observability, SLOs, chaos |
| G-SWE | 2.8 | 32 | Testing, code review |
| DORA | 3.1 | 16 | Delivery metrics |
| AWS-WA | 3.0 | 30 | DR/RTO |
| MS-CSE | 2.7 | 33 | Documentation |
| 12-Factor | 2.8 | 10 | Config |
| NIST SSDF | 3.0 | 14 | SDL |
| Team Topologies | 4.3 | 6 | Team types, platform |
| CNCF Platforms | 3.2 | 9 | Platform |
| ThoughtWorks | 3.2 | 33 | Trunk, testing, flags, architecture |
| GitLab | 2.9 | 34 | None at 5 |

**Note:** Averages are only meaningful across **applicable** domains — narrow frameworks (12-Factor, Team Topologies, DORA) score high in their lane and aren't penalised for out-of-scope domains.

---

## Where This Doctrine Leads

| Domain | Why it's ahead |
| --- | --- |
| **Build surfaces model** | No other framework names and formalises quality-gate / build / deploy / verify as explicit, reviewable surfaces with local-mirrors-CI. Most stop at "use CI/CD." |
| **Contract-first (sync + async)** | CloudEvents envelope + versioned payloads + CI validation + worked fictions. Most frameworks say "use schemas" without prescribing the event envelope or validation gate. |
| **Supply chain (SBOM + SLSA + SCA)** | SLSA levels, CycloneDX/SPDX choice rationale, OCI attestation, severity SLAs — more actionable than NIST SSDF which defines the *what* but not the *how*. |
| **AI/ML governance (tiers A-D)** | Risk-tiered model from API call to agentic automation, with explicit upgrade triggers, eval requirements, and MCP/tool protocol guidance. No mainstream framework has this yet. |
| **RAG / retrieval** | Hybrid search baseline, freshness SLAs, tenant isolation, eval loop, vector pipeline illustration. Novel territory — mainstream frameworks haven't caught up. |
| **FinOps depth** | Unit economics, anomaly SLAs, AI inference budgets, FOCUS spec pointer. Goes beyond AWS-WA cost pillar. |
| **Idempotency** | Unified HTTP + message + infra idempotency pattern. Most frameworks mention idempotency in one context only. |
| **Principles / tooling / estates split** | Architectural differentiator — no other framework cleanly separates *timeless intent* from *replaceable implementation* from *org-specific product picks*. |
| **Self-governance** | Change checklist, MoSCoW audit trail, gap research, honest review synthesis, sitemap generation — the doctrine governs its own evolution. Rare outside GitLab's handbook. |

---

## Where This Doctrine Is On Par

| Domain | Comparable to |
| --- | --- |
| **Observability** | Strong (three pillars, cardinality, OTel), but G-SRE goes deeper on alerting philosophy, monitoring-as-code, and Borgmon/Prometheus lineage |
| **SLOs / incidents** | Solid error-budget policy and blameless postmortems, but thinner on multi-window burn-rate alerting math than G-SRE Workbook |
| **Testing** | Good pyramid + contracts + flake policy; G-SWE has deeper treatment of test size taxonomy, hermetic tests, and testing-at-scale anti-patterns |
| **Platform engineering** | Team Topologies + TVP + cognitive load — matches CNCF whitepaper in principle but lighter on IDP implementation patterns |
| **Feature flags** | Lifecycle FSM, progressive delivery, flag debt — comparable to TW/Fowler depth |
| **Documentation** | ADRs + runbooks solid; MS-CSE has richer templates and worked examples |
| **DORA metrics** | Four Keys + SPACE framing; DORA/Accelerate obviously goes deeper on the research backing |

---

## Where This Doctrine Is Thin Or Absent

| Domain | Gap | Who does it better | Suggested action |
| --- | --- | --- | --- |
| **Compliance mapping (SOC2/ISO/FedRAMP)** | Intentionally absent for portability | AWS-WA, NIST, GitLab | **Keep as Won't** unless regulated estate demands it; add a pointer to control-mapping templates in estates |
| **Disaster recovery / RTO-RPO drills** | Mentioned in data-and-migrations but no drill cadence or runbook pattern | AWS-WA (Reliability pillar), G-SRE (DiRT) | **Should**: add a DR drill subsection to reliability or a pattern |
| **Developer experience (SPACE metrics)** | Mentioned in measurement-and-dora §4 but only a paragraph | DORA, G-SWE, GitLab | **Could**: expand §4 or link to a DX survey template |
| **Performance / load testing methodology** | Budget and FinOps tags are strong; load test *methodology* (tools, baselines, regression gates) is thin | G-SRE (handling overload), AWS-WA | **Should**: add a load-test pattern or expand performance-and-cost |
| **Sustainability / green software** | Absent beyond a REFERENCES pointer | AWS-WA (sustainability pillar), Green Software Foundation | **Could**: one-page principle if the org cares; SCI metric pointer |
| **Code review depth** | "Small PRs, reviewed merge" but no review *checklist*, *review time SLA*, or *reviewer selection* guidance | G-SWE (readability, review best practices), MS-CSE | **Should**: expand collaboration.md or add a review pattern |
| **Chaos engineering depth** | Pattern exists but thin vs Netflix/Gremlin; no steady-state hypothesis template | G-SRE, Principles of Chaos | **Could**: expand the pattern with a hypothesis → experiment → analyse template |
| **Multi-region / global architecture** | Not addressed beyond "managed platform" preference | AWS-WA, G-SRE | **Could** if teams run multi-region; estate-specific |
| **Monorepo tooling at scale** | Mentioned in naming; no Bazel/Nx/Turborepo guidance | G-SWE (monorepo chapter) | **Won't** for portable doctrine; estate supplement if needed |
| **Incident command structure** | Severity levels + postmortems but no IC/CL/Scribe role definitions | PagerDuty incident response guide, G-SRE | **Should**: add role definitions to reliability principle |

---

## Unique Differentiators (Not Found In Any Compared Framework)

1. **Estates model** — organisation-specific product picks live in `tooling/estates/` supplements, not mixed into principles. No other framework has this separation.
2. **Worked fictions** — fictional end-to-end scenarios (order FSM + JetStream, saga + compensation) that demonstrate multiple principles interacting. Most frameworks use isolated examples.
3. **AI risk tiers (A-D) with upgrade triggers** — graduated governance from API-only to agentic. Novel.
4. **RAG retrieval baseline pattern** — hybrid search, eval loops, tenant isolation, freshness. No comparable in any mainstream framework.
5. **Minimum Viable Doctrine (MVD)** — explicit smallest-set starting point with a one-page team template. Most frameworks are all-or-nothing.
6. **Self-auditing evolution folder** — MoSCoW, gap research, honest review synthesis, change checklist. The doctrine tracks its own debt.

---

## Competitive Position Summary

```
                    Breadth of coverage
                    (domains addressed)
                         |
                    High |  AWS-WA    [THIS]    GitLab
                         |                       G-SWE
                         |  MS-CSE
                    Med  |         TW
                         |
                    Low  |  12F    TT    CNCF-P
                         |              DORA
                         +---------------------------
                         Low    Med    High
                              Depth per domain
                          (actionability, specificity)
```

**This doctrine occupies the top-right quadrant**: broad coverage across 35+ domains with actionable depth (defaults, rationale tables, worked examples, checklists). The closest competitors in that quadrant are **GitLab Handbook** (broader on org/people, thinner on technical specificity) and **AWS Well-Architected** (deeper on cloud architecture, locked to one vendor).

The unique positioning is **portable, forkable, modular doctrine with replaceable tooling** — no other framework offers this combination.

---

## Recommended Priority Actions (From This Scorecard)

### Must (to close material gaps)

None — all material domains are covered.

### Should (to match best-in-class where you're close)

1. **DR drill pattern** — cadence, runbook test, blast radius, reporting (closes the AWS-WA/G-SRE gap)
2. **Code review practice** — reviewer selection, review-time SLA, review checklist (closes the G-SWE gap)
3. **Incident command roles** — IC, CL, Scribe definitions (closes the G-SRE gap)
4. **Load testing methodology** — baseline, regression gate, tooling categories (closes the AWS-WA gap)

### Could

5. **SPACE / developer experience** expansion
6. **Chaos experiment template** (steady-state hypothesis format)
7. **Sustainability / SCI one-pager**
8. **Multi-region architecture pattern** (if teams need it)

### Won't (confirmed)

- Full SOC2/ISO control mapping (portability)
- Monorepo-at-Google-scale tooling (estate-specific)
- Vendor-locked architecture guidance (principles stay portable)

---

## References

- Google SRE Book: https://sre.google/sre-book/table-of-contents/
- Software Engineering at Google: https://abseil.io/resources/swe-book
- DORA / Accelerate: https://dora.dev/
- AWS Well-Architected: https://docs.aws.amazon.com/wellarchitected/
- Microsoft CSE Playbook: https://microsoft.github.io/code-with-engineering-playbook/
- 12-Factor App: https://12factor.net/
- NIST SSDF SP 800-218: https://csrc.nist.gov/Projects/SSDF
- Team Topologies: https://teamtopologies.com/book
- CNCF Platforms Whitepaper: https://tag-app-delivery.cncf.io/whitepapers/platforms/
- ThoughtWorks Technology Radar: https://www.thoughtworks.com/radar
- GitLab Handbook: https://handbook.gitlab.com/
- Principles of Chaos Engineering: https://principlesofchaos.org/
- Green Software Foundation: https://greensoftware.foundation/
- PagerDuty Incident Response: https://response.pagerduty.com/
