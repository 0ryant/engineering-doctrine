# CI Platform Mapping (Examples)

Illustrative mappings from **abstract delivery surfaces** in `ENGINEERING.md` (quality gate, build/publish, deploy, verify) to **example** CI products. Paths such as `.pipelines/*.yaml` are **one** convention among many.

The **invariants** are the surfaces themselves, not the vendor.

---

## Abstract Surfaces (Invariant)

| Surface | Responsibility |
| --- | --- |
| **Quality gate** | fmt, lint, type-check, test, contracts, secret scan |
| **Build & publish** | Immutable artefact + version metadata |
| **Deploy** | Per deployable unit; plan/apply where IaC |
| **Execute / smoke** | Scheduled or manual verification with evidence |

**Why a mapping doc:** Teams on **GitHub Actions**, **GitLab CI**, or **Azure Pipelines** implement the same **contract** with different YAML entrypoints; duplicating doctrine per vendor fragments truth.

---

## GitHub Actions (typical mapping)

| Abstract file | Typical GHA equivalent |
| --- | --- |
| `.pipelines/quality.yaml` | `.github/workflows/quality.yml` — `pull_request` + `push` to default branch |
| `.pipelines/build-and-publish.yaml` | workflow on `release` tags or `workflow_dispatch` with approval |
| `.pipelines/deploy-infrastructure.yaml` | dedicated workflow with **OIDC** to cloud, Terraform in repo scripts |
| Variables | GitHub **Environments**, **secrets**, **vars**, **reusable workflows** |

References: GitHub **Workflow syntax** and **Reusable workflows**: https://docs.github.com/en/actions/using-workflows

---

## GitLab CI (typical mapping)

| Abstract file | Typical GitLab equivalent |
| --- | --- |
| `.pipelines/quality.yaml` | `.gitlab-ci.yml` **include** or `stages: [quality]` with `rules` for MR pipelines |
| Build / publish | stage with **release** or container registry push |
| Deploy | stage with protected environments, optional manual jobs |
| Variables | GitLab **CI/CD variables**, **protected** and **masked** |

References: GitLab **CI/CD YAML reference**: https://docs.gitlab.com/ee/ci/yaml/

---

## Azure Pipelines (typical mapping)

| Abstract file | Typical Azure equivalent |
| --- | --- |
| `.pipelines/quality.yaml` | `azure-pipelines.yml` or pipeline in `.pipelines/` referenced by Azure DevOps |
| Templates | **YAML templates** for reuse across repos |
| Variables | **Variable groups**, **Key Vault** linkage |

References: Azure Pipelines **YAML schema**: https://learn.microsoft.com/en-us/azure/devops/pipelines/yaml-schema/

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Keep abstract names in umbrella doc | Template repos stay **portable**; only this tooling file is vendor-specific. |
| OIDC over long-lived cloud keys | Aligns with `ENGINEERING.md` **managed identity / OIDC** preference. |
| One quality workflow per repo minimum | Matches **trunk** discipline: every merge path runs the same gate. |

---

## References

- GitHub Actions documentation: https://docs.github.com/en/actions  
- GitLab CI/CD documentation: https://docs.gitlab.com/ee/ci/  
- Azure Pipelines: https://learn.microsoft.com/en-us/azure/devops/pipelines/  
- **OpenID Connect** for cloud deploy from CI (pattern): major clouds document “OIDC from GitHub Actions” / GitLab JWT — use provider docs when implementing.  
