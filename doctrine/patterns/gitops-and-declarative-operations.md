# GitOps And Declarative Operations

**Portable intent:** This pattern explains how **this library** uses the term *GitOps* and *declarative operations*: **published community standards and external research first** (OpenGitOps, OWASP, NIST pointers, Twelve-Factor), then a **short map** to in-repo principles. It is not an exercise in self-referential doctrine.

**Estate** choices (Argo CD, Flux, cloud services, push-based tools) live under `doctrine/tooling/estates/` or your org catalogue.

---

## 1. OpenGitOps: canonical principles (v1.0.0)

The [OpenGitOps](https://opengitops.dev/) project publishes versioned GitOps principles under the [CNCF GitOps Working Group](https://github.com/cncf/tag-app-delivery). The **authoritative** text is in the [open-gitops/documents](https://github.com/open-gitops/documents) repository. The table below is a **faithful summary** of [GitOps Principles v1.0.0](https://raw.githubusercontent.com/open-gitops/documents/v1.0.0/PRINCIPLES.md)—read the source for normative wording.

| # | Principle | Core requirement (from the standard) |
| --- | --- | --- |
| 1 | **Declarative** | A GitOps-managed *system* must express *desired state* **declaratively**. |
| 2 | **Versioned and Immutable** | Desired state is *stored* so that **immutability**, **versioning**, and a **full history** are enforced. |
| 3 | **Pulled Automatically** | Software agents **pull** desired-state declarations from the source. |
| 4 | **Continuously Reconciled** | Agents **continuously** observe *actual* state and **reconcile** toward *desired* state. |

**Push-based delivery** (e.g. CI applies Terraform or manifests from a **known commit** on each change) is common. OpenGitOps *as written* emphasises *pull* reconcilers. Many teams use a **governed, idempotent push** with the same VCS review, evidence, and promotion discipline as pull-based flows; vendor-neutral discussions of *GitOps without a pull reconciler* exist (e.g. [Puppet — What is GitOps?](https://www.puppet.com/blog/what-is-gitops)). The **invariants in §4** are written so **either** model can pass if review, **immutability of declared inputs**, and **drift visibility** are real.

**Formal terms** (*desired state*, *reconciliation*, *state store*): [OpenGitOps GLOSSARY v1.0.0](https://github.com/open-gitops/documents/blob/v1.0.0/GLOSSARY.md).

---

## 2. External research: security, risk, and config discipline

| Source | Relevance to GitOps / declarative operations |
| --- | --- |
| [OWASP Top 10 CI/CD Security Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/) (v1.0, 2022) | Community **research** on CI/CD as an attack surface: e.g. insufficient **flow control** (CICD-SEC-1), **poisoned pipeline execution** (CICD-SEC-4), **pipeline-based access** (CICD-SEC-5), **credential hygiene** (CICD-SEC-6), **insecure system configuration** (CICD-SEC-7), **artifact integrity** (CICD-SEC-9), **visibility** (CICD-SEC-10). GitOps does **not** make these disappear; it **centralises** *who* can change *production shape* in VCS, reconcilers, and automation that must be **governed** with the same evidence mindset as application pipelines. Complements [merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md). |
| NIST *Secure Software Development Framework* (SSDF), e.g. [SP 800-218](https://csrc.nist.gov/publications/detail/sp/800-218/final) | Activities under **Protect Software (PS)** and **Produce Well-Secured Software (PO)** expect build pipelines and environments to be **hardened and verifiable**; versioned declarative IaC in git is a **common** way to get **reviewable** infrastructure change. Cite NIST in **estate** compliance packs, not in portable principles here. |
| [Twelve-Factor App — Config](https://12factor.net/config) | Config **belongs in the environment**; **contrast** with putting **secrets** in the repo. Aligns with [configuration-and-secrets.md](../principles/configuration-and-secrets.md) and with secret patterns (sealed secrets, ESO, cloud refs) in mature GitOps estates. |
| [OpenGitOps](https://opengitops.dev/) (community) | **Interoperable vocabulary** and education; §1 is the **spine** of this file. |

**Historical note (orientation, not normative):** the term *GitOps* spread in the **Kubernetes** ecosystem (Weaveworks and industry write-ups, roughly 2017–2018) and has since broadened to **cloud and non-K8s** targets. [OpenGitops.dev](https://opengitops.dev/) quotes practitioners (e.g. [Kelsey Hightower on declarative config at scale](https://opengitops.dev/)) in support of the movement—not as a normative law for this file.

---

## 3. How OpenGitOps maps to our invariants

| OpenGitOps principle (§1) | What we require in §4 |
| --- | --- |
| **Declarative** | Default change is **not** tribal console or SSH habit. |
| **Versioned and Immutable** | VCS merge path (or governed import) + **defensible** references to what runs in production (e.g. image digest or lock). |
| **Pulled Automatically** (or **practical** equivalent) | Reconciler **or** documented push that **replays a known revision**; no routine mystery deploys. |
| **Continuously Reconciled** | **Drift** is visible; break-glass is **rare** and followed by return to **declared** state. |

---

## 4. Invariants (portable, this library)

1. **Reviewed changes** to material cluster- or account-level *desired state* through the VCS path, or a governed import with an audit trail.

2. **Reconciliation loop** or **push equivalent**: every material apply is tied to a **known** revision; no unreviewed *surprise* applies as culture.

3. **Immutable deployment inputs** for application payloads: e.g. container **digest** or equivalent where images are in play; using `latest` in production is a **red flag** unless policy allows it and it is **auditable**.

4. **Secrets** not in clear text in git; use [configuration-and-secrets.md](../principles/configuration-and-secrets.md) and estate patterns (sealed secrets, ESO, cloud secret refs).

5. **Drift** is measured and triaged; if break-glass is frequent, treat it as a **governance or automation** gap, not only heroics.

6. **Blast radius** of shared control planes: treat IaC and orchestrator changes as **high-impact** review, aligned with [code-review-and-change-approval.md](code-review-and-change-approval.md) §5 and OWASP CI/CD risk *themes* (§2).

---

## 5. Environments, overlays, promotion

- Overlays, paths, and branches: **estate** design. Document **precedence** and one clear **promotion** story (how the artefact or reconciler target moves).

- Databases and migrations: [data-and-migrations.md](../principles/data-and-migrations.md). Not all *state* belongs in git.

---

## 6. What “GitOps” is not (aligned with OpenGitOps + common failure research)

| Anti-pattern | Contrast |
| --- | --- |
| “GitOps” = ad-hoc `kubectl` as **culture** | Fails *declarative* + *reconciliation* intent; at best a one-off, at worst **invisible drift** |
| Secrets in **tickets** or **chat** to unblock deploy | Undermines *versioned, reviewable* governance; see OWASP **credential hygiene** (CICD-SEC-6) themes and NIST/estate secret handling |
| Three competing *sources of truth* (e.g. Helm + raw YAML + click-ops) | Undermines a **single** declared stack; **reconcile to one** hierarchy or document **waiver and owner** |

---

## 7. In-repo alignment (secondary)

These internal files support the same outcomes; they **do not** replace **§1–2** for evidence of what GitOps *means* externally.

- [build.md](../principles/build.md) (immutable artefact promotion)  
- [single-source-of-truth.md](../principles/single-source-of-truth.md)  
- [collaboration.md](../principles/collaboration.md) (no production snowflakes)  
- [merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md)  
- [code-review-and-change-approval.md](code-review-and-change-approval.md)  
- [naming-and-repo-layout.md](../principles/naming-and-repo-layout.md) (IaC naming/tags)  
- [kubernetes-platform-security.md](../principles/kubernetes-platform-security.md) (when clusters are in scope)  
- [adoption-playbook.md](adoption-playbook.md)  
- [engineering-controls-governance-program.md](engineering-controls-governance-program.md)  

---

## 8. Authoring note: estate pages

Estate supplements should name: reconciler (if any), where secrets are materialised, per-environment layout, revert/rollback path, and which **external** frameworks the estate maps to for audits (e.g. **OpenGitOps** invariants + **OWASP CI/CD** top risks).

**Primary external bibliography for this pattern:** [PRINCIPLES.md (v1.0.0)](https://raw.githubusercontent.com/open-gitops/documents/v1.0.0/PRINCIPLES.md), [OpenGitOps](https://opengitops.dev/), [OWASP Top 10 CI/CD Security Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/).
