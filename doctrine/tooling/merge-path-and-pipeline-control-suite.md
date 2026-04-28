# Merge Path And Pipeline Control Suite (Illustrative)

**Illustrative only** — maps **control classes** from [merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md) to **categories** of tools and integration patterns. Swap products freely; keep **binding enforcement**, **evidence retention**, and **pipeline-in-scope** semantics.

---

## 1. Control Classes And Typical Tool Categories

| Control class | Typical intent | Example tool **categories** (non-exhaustive) |
| --- | --- | --- |
| **Secret exposure in VCS** | Block credentials, keys, tokens in commits | Secret scanners for git history and staged files; host-native secret scanning when available |
| **Dependency vulnerability (SCA)** | Fail on known CVEs above policy severity | Language-native advisory consumers; multi-ecosystem scanners |
| **Licence / policy** | Enforce allowlist for distribution | Licence scanners, policy engines on dependency graphs |
| **Container / filesystem posture** | Known vulns and misconfigs in images and repos | OCI/filesystem scanners with policy-as-code exit codes |
| **IaC / cloud config** | Misconfiguration before deploy | Static analysers for Terraform, Kubernetes manifests, cloud policy-as-code |
| **Pipeline static analysis** | Dangerous workflow patterns, excessive permissions, injection | Workflow linters, dedicated CI security analysers, custom Open Policy Agent (OPA) on YAML |
| **Provenance / SBOM emission** | Attest builds; publish SBOM with releases | SBOM generators (SPDX, CycloneDX), SLSA-style generators, Sigstore cosign signing |
| **Post-merge assurance** | Runtime verification separate from merge | Smoke jobs, synthetic probes (see execution surfaces in your build model) |
| **Adversarial / abuse-case analysis** | Negative-security testing on security-relevant diffs; optional deeper scheduled scans | SAST with chaining, policy-driven fuzz/DAST, LLM-assisted review bots—**estate** picks products; principle: [merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md) §2 invariants 8–9, [testing-strategy.md](../principles/testing-strategy.md) §5 |

---

## 2. Integration Pattern (Merge Gate)

1. **Single orchestration entry** per repo (workflow file, pipeline template, or bot) invokes **scripts** that implement the gate.  
2. **Required check** enforced at **host** for default branch; same script runnable **locally** for fast feedback.  
3. **Publish artefacts** (SARIF, SBOM, test reports) to durable storage when policy requires—not only console logs.  
4. **Pin** third-party automation references where the ecosystem allows **immutable** references (commit SHA for reusable actions, digest-pinned containers).  
5. **Short-lived credentials** to clouds via **OIDC federation** where supported—avoid long-lived cloud keys in repository secrets when alternatives exist.

---

## 3. Host-Specific Notes (Examples Only)

| Host | Official hardening / OIDC references |
| --- | --- |
| **GitHub Actions** | Security hardening overview: https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions — OIDC to cloud: https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect |
| **GitLab CI** | CI/CD variables, protected environments, and job token scope: https://docs.gitlab.com/ee/ci/ |
| **Azure Pipelines** | OIDC with Microsoft Entra workload identity: https://learn.microsoft.com/en-us/azure/devops/pipelines/library/connect-to-azure |

---

## 4. Static Analysis Of Pipelines (Why A Separate Row)

OWASP’s CI/CD risk work and field surveys (e.g. Filippo Valsorda’s 2024/2025 compromise survey) show **workflow definition abuse** (`pull_request_target`-class patterns, malicious third-party steps, over-scoped tokens) as **recurring** root causes. Treat **pipeline YAML** (or equivalent) as an input to **policy-enforcing** static analysis, not only app source.

**Reference:** https://owasp.org/www-project-top-10-ci-cd-security-risks/ and https://words.filippo.io/compromise-survey/

---

## References (External)

- OWASP — **Top 10 CI/CD Security Risks**: https://owasp.org/www-project-top-10-ci-cd-security-risks/  
- **Filippo Valsorda** — compromise survey: https://words.filippo.io/compromise-survey/  
- **SLSA** — Build track: https://slsa.dev/spec/v1.2/  
- **Sigstore** — **cosign** signing: https://docs.sigstore.dev/cosign/overview/  
- **SPDX** / **CycloneDX** — SBOM interchange: https://spdx.dev/ , https://cyclonedx.org/  
- **CISA SBOM** hub: https://www.cisa.gov/sbom  
- **OpenSSF Scorecard** (automation health signals for OSS repos—illustrative metrics source): https://scorecard.dev/  

---

*Introduced: 2026-04-26.*
