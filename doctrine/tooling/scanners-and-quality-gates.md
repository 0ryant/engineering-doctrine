# Scanners And Quality Gates (Illustrative)

**Illustrative only.** [merge-path-and-pipeline-control-suite.md](merge-path-and-pipeline-control-suite.md) §1 maps control classes to categories of tool. This page names open-source tools for those categories, across the languages an enterprise estate commonly holds. It adds no obligation: the rules sit with the owners named in §1.

**Selection rule** ([ADR 0060](../../docs/adr/0060-name-only-open-source-gate-tools-usable-without-a-paid-plan.md)). A tool is offered here only if it carries an open-source licence and can run on a private, commercial codebase without a paid plan or a licence key. Tools under Apache-2.0 or MIT come first (§§2–3). Tools under other open-source licences are listed apart, with the licence named (§4), so an organisation can apply its own licence policy. This page does not interpret licence obligations.

**Dated facts.** Licences were read from each project's own repository, and plan terms from each publisher's own pages, on 2026-11-18. Both change. Check before adopting. The per-tool record is in the [research note](../evolution/research-scanner-tooling-map-2026-11.md).

---

## 1. What Each Class Catches

| Class | What it catches | Rule it serves |
| --- | --- | --- |
| Secrets in commits | Credentials in history or in staged changes | [build](../principles/build.md) §10; [dependencies](../principles/dependencies-supply-chain.md) §3; [configuration and secrets](../principles/configuration-and-secrets.md) §§2, 4 |
| Dependency vulnerabilities | Known vulnerabilities in what ships, at merge and again on a schedule | [dependencies](../principles/dependencies-supply-chain.md) §§2–3; [merge path](../principles/merge-path-evidence-and-pipeline-integrity.md) §2 invariant 9 |
| Dependency policy | Disallowed licences, banned packages, unexpected sources | [dependencies](../principles/dependencies-supply-chain.md) §§6–7 |
| Container images | Vulnerable packages and unsafe image configuration | [Kubernetes platform security](../principles/kubernetes-platform-security.md) §3; [build](../principles/build.md) §10 |
| Infrastructure and cluster configuration | Misconfiguration before it deploys | [build](../principles/build.md) §10; [GitOps](../patterns/gitops-and-declarative-operations.md) §4 |
| Pipeline definitions | Injection paths, over-scoped tokens, unpinned third-party steps | [merge path](../principles/merge-path-evidence-and-pipeline-integrity.md) §2 invariant 2 |
| SBOM | A record of what an artefact contains | [dependencies](../principles/dependencies-supply-chain.md) §3 |
| Signing and provenance | Who built an artefact, and from what | [dependencies](../principles/dependencies-supply-chain.md) §§4–5 |
| Static analysis | Defect and vulnerability patterns in source | [testing strategy](../principles/testing-strategy.md) §5; [merge path](../principles/merge-path-evidence-and-pipeline-integrity.md) §2 invariant 8 |
| Test strength | Tests that cannot fail, and inputs never tried | [testing strategy](../principles/testing-strategy.md) §6 |
| Contract change | Breaking changes to an API or schema | [semantic versioning](../principles/semantic-versioning.md); [event contracts](../principles/event-contracts.md) |
| Dynamic scanning | Flaws visible only in a running system | [testing strategy](../principles/testing-strategy.md) §5 |

---

## 2. Cross-Language Tools Under Apache-2.0 Or MIT

Start here. One tool per class covers most languages in a mixed estate.

| Class | Tools |
| --- | --- |
| Secrets in commits | [Gitleaks](https://github.com/gitleaks/gitleaks), [detect-secrets](https://github.com/Yelp/detect-secrets) |
| Dependency vulnerabilities | [Trivy](https://github.com/aquasecurity/trivy), [Grype](https://github.com/anchore/grype), [OSV-Scanner](https://github.com/google/osv-scanner), [OWASP Dependency-Check](https://github.com/dependency-check/DependencyCheck), [OWASP dep-scan](https://github.com/owasp-dep-scan/dep-scan) |
| Dependency policy and licences | [OSS Review Toolkit](https://github.com/oss-review-toolkit/ort), [Trivy](https://github.com/aquasecurity/trivy) |
| Container images | [Trivy](https://github.com/aquasecurity/trivy), [Grype](https://github.com/anchore/grype), [Dockle](https://github.com/goodwithtech/dockle) |
| Infrastructure and cluster configuration | [Checkov](https://github.com/bridgecrewio/checkov), [KICS](https://github.com/Checkmarx/kics), [Trivy](https://github.com/aquasecurity/trivy), [cfn-lint](https://github.com/aws-cloudformation/cfn-lint), [Bicep linter](https://github.com/Azure/bicep), [Helm lint](https://github.com/helm/helm), [KubeLinter](https://github.com/stackrox/kube-linter), [kubeconform](https://github.com/yannh/kubeconform), [Kubescape](https://github.com/kubescape/kubescape), [Polaris](https://github.com/FairwindsOps/polaris), [Conftest](https://github.com/open-policy-agent/conftest), [Kyverno](https://github.com/kyverno/kyverno) |
| Pipeline definitions | [actionlint](https://github.com/rhysd/actionlint), [zizmor](https://github.com/zizmorcore/zizmor), [OpenSSF Scorecard](https://github.com/ossf/scorecard), [taudit](https://github.com/0ryant/taudit) |
| SBOM | [Syft](https://github.com/anchore/syft), [cdxgen](https://github.com/cdxgen/cdxgen), [Trivy](https://github.com/aquasecurity/trivy), [SBOM Tool](https://github.com/microsoft/sbom-tool) |
| Signing and provenance | [cosign](https://github.com/sigstore/cosign); for GitHub-hosted builds, artifact attestations (see host features below), which the [SLSA GitHub generator](https://github.com/slsa-framework/slsa-github-generator), now no longer actively maintained, points to |
| Static analysis across languages | [Infer](https://github.com/facebook/infer) |
| Fuzzing infrastructure | [OSS-Fuzz](https://github.com/google/oss-fuzz), [ClusterFuzzLite](https://github.com/google/clusterfuzzlite) |
| Contract change | [Spectral](https://github.com/stoplightio/spectral), [oasdiff](https://github.com/oasdiff/oasdiff), [Buf](https://github.com/bufbuild/buf) |
| Dynamic scanning | [ZAP](https://github.com/zaproxy/zaproxy), [Nuclei](https://github.com/projectdiscovery/nuclei) |
| Hygiene: prose, links, SQL, commits | [markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2), [typos](https://github.com/crate-ci/typos), [lychee](https://github.com/lycheeverse/lychee), [SQLFluff](https://github.com/sqlfluff/sqlfluff), [commitlint](https://github.com/conventional-changelog/commitlint) |
| Hook and lint runners | [pre-commit](https://github.com/pre-commit/pre-commit), [Lefthook](https://github.com/evilmartians/lefthook), [Super-Linter](https://github.com/super-linter/super-linter) |
| Dependency updates | [Dependabot core](https://github.com/dependabot/dependabot-core) |

Trivy appears in several rows because one binary scans dependencies, images, configuration, and licences, and can emit an SBOM. cfn-lint carries MIT-0, the no-attribution form of MIT.

**Disclosure.** taudit, which scans the authority CI/CD pipelines hold (secrets, identities, trust boundaries), is written by the maintainer of this library. It is listed under the same rule as every other tool, and it is the only tool here with that connection ([ADR 0060](../../docs/adr/0060-name-only-open-source-gate-tools-usable-without-a-paid-plan.md) D6). It was relicensed from AGPL-3.0-or-later to MIT on 2026-11-18.

---

## 3. Per-Language Tools Under Apache-2.0 Or MIT

Add these where the estate holds that language. An empty cell means no tool under these two licences was found; check §4 and the cross-language row before concluding there is none.

| Language | Lint and static analysis | Security analysis | Dependency audit | Coverage, mutation, fuzzing | SBOM |
| --- | --- | --- | --- | --- | --- |
| Rust | [Clippy](https://github.com/rust-lang/rust-clippy), [cargo-semver-checks](https://github.com/obi1kenobi/cargo-semver-checks) | — | [cargo-audit](https://github.com/rustsec/rustsec), [cargo-deny](https://github.com/EmbarkStudios/cargo-deny), [cargo-vet](https://github.com/mozilla/cargo-vet) | [cargo-llvm-cov](https://github.com/taiki-e/cargo-llvm-cov), [cargo-mutants](https://github.com/sourcefrog/cargo-mutants), [cargo-fuzz](https://github.com/rust-fuzz/cargo-fuzz) | [cargo-cyclonedx](https://github.com/CycloneDX/cyclonedx-rust-cargo) |
| Java and Kotlin | [Error Prone](https://github.com/google/error-prone), [NullAway](https://github.com/uber/NullAway), [Infer](https://github.com/facebook/infer), [detekt](https://github.com/detekt/detekt), [ktlint](https://github.com/pinterest/ktlint), [Spotless](https://github.com/diffplug/spotless) | — | [OWASP Dependency-Check](https://github.com/dependency-check/DependencyCheck) | [PIT](https://github.com/hcoles/pitest), [Jazzer](https://github.com/CodeIntelligenceTesting/jazzer) | [CycloneDX Maven plugin](https://github.com/CycloneDX/cyclonedx-maven-plugin), [CycloneDX Gradle plugin](https://github.com/CycloneDX/cyclonedx-gradle-plugin) |
| JavaScript and TypeScript | [ESLint](https://github.com/eslint/eslint), [typescript-eslint](https://github.com/typescript-eslint/typescript-eslint), [Biome](https://github.com/biomejs/biome), [Prettier](https://github.com/prettier/prettier), [TypeScript compiler](https://github.com/microsoft/TypeScript) | [eslint-plugin-security](https://github.com/eslint-community/eslint-plugin-security) | [audit-ci](https://github.com/IBM/audit-ci), [Retire.js](https://github.com/RetireJS/retire.js) | [Vitest](https://github.com/vitest-dev/vitest), [StrykerJS](https://github.com/stryker-mutator/stryker-js), [Jazzer.js](https://github.com/CodeIntelligenceTesting/jazzer.js) | [cyclonedx-node-npm](https://github.com/CycloneDX/cyclonedx-node-npm) |
| Python | [Ruff](https://github.com/astral-sh/ruff), [mypy](https://github.com/python/mypy), [Pyright](https://github.com/microsoft/pyright) | [Bandit](https://github.com/PyCQA/bandit) | [pip-audit](https://github.com/pypa/pip-audit), [pip-licenses](https://github.com/raimon49/pip-licenses) | [pytest](https://github.com/pytest-dev/pytest), [coverage.py](https://github.com/nedbat/coveragepy), [Atheris](https://github.com/google/atheris) | [cyclonedx-python](https://github.com/CycloneDX/cyclonedx-python) |
| Go | [Staticcheck](https://github.com/dominikh/go-tools) | [gosec](https://github.com/securego/gosec) | [go-licenses](https://github.com/google/go-licenses) | — | [cyclonedx-gomod](https://github.com/CycloneDX/cyclonedx-gomod) |
| C# and .NET | [.NET SDK analyzers](https://github.com/dotnet/sdk), [Roslynator](https://github.com/dotnet/roslynator) | — | [`dotnet package list --vulnerable`](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-package-list) (the older `dotnet list package` form still works) | [coverlet](https://github.com/coverlet-coverage/coverlet), [Stryker.NET](https://github.com/stryker-mutator/stryker-net), [SharpFuzz](https://github.com/Metalnem/sharpfuzz) | [cyclonedx-dotnet](https://github.com/CycloneDX/cyclonedx-dotnet) |
| C and C++ | [clang-tidy and the Clang static analyzer](https://github.com/llvm/llvm-project), [Infer](https://github.com/facebook/infer) | [the LLVM sanitizers](https://github.com/llvm/llvm-project) | — | [libFuzzer](https://github.com/llvm/llvm-project), [OSS-Fuzz](https://github.com/google/oss-fuzz) | — |
| Ruby | [RuboCop](https://github.com/rubocop/rubocop) | — | — | [SimpleCov](https://github.com/simplecov-ruby/simplecov) | — |
| PHP | [PHPStan](https://github.com/phpstan/phpstan), [Psalm](https://github.com/vimeo/psalm) | [Psalm](https://github.com/vimeo/psalm) | [`composer audit`](https://github.com/composer/composer) | — | — |
| Swift | [SwiftLint](https://github.com/realm/SwiftLint) | — | — | — | — |

Shell, SQL, YAML, Dockerfile, and infrastructure formats are covered by §2 and §4. The LLVM tools carry Apache-2.0 with the LLVM exceptions.

---

## 4. Tools Under Other Open-Source Licences

All are open source. They are listed apart because many organisations treat these licence families differently from Apache-2.0 and MIT. The family label is a common classification, not advice.

| Licences | Family | Tools and what each is for |
| --- | --- | --- |
| BSD-3-Clause, BSD-style, ISC, Artistic-2.0 | Permissive | [govulncheck](https://github.com/golang/vuln) (BSD-3-Clause): Go dependency vulnerabilities; [the Go toolchain (`go vet`, native fuzzing, coverage)](https://github.com/golang/go) (BSD-3-Clause): Go static checks and test strength; [shfmt](https://github.com/mvdan/sh) (BSD-3-Clause): shell formatting; [mutmut](https://github.com/boxed/mutmut) (BSD-3-Clause): Python mutation testing; [Infection](https://github.com/infection/infection) (BSD-3-Clause): PHP mutation testing; [PHP_CodeSniffer](https://github.com/PHPCSStandards/PHP_CodeSniffer) (BSD-3-Clause): PHP style; [Scalafix](https://github.com/scalacenter/scalafix) (BSD-3-Clause): Scala lint; [PMD](https://github.com/pmd/pmd) (BSD-style): static analysis for Java and other languages; [the npm CLI (`npm audit`)](https://github.com/npm/cli) (Artistic-2.0): JavaScript dependency vulnerabilities; [Knip](https://github.com/webpro-nl/knip) (ISC): unused JavaScript dependencies |
| MPL-2.0, EPL-2.0, LGPL-2.1, LGPL-3.0 | Weak copyleft | [TFLint](https://github.com/terraform-linters/tflint) (MPL-2.0): Terraform lint; [OpenTofu (`tofu validate`, `tofu fmt`)](https://github.com/opentofu/opentofu) (MPL-2.0): infrastructure syntax and format; [Hypothesis](https://github.com/HypothesisWorks/hypothesis) (MPL-2.0): Python property-based testing; [JaCoCo](https://github.com/jacoco/jacoco) (EPL-2.0): JVM coverage; [Semgrep Community Edition](https://github.com/semgrep/semgrep) (LGPL-2.1): static analysis across languages; [Opengrep](https://github.com/opengrep/opengrep) (LGPL-2.1): static analysis across languages; [SpotBugs](https://github.com/spotbugs/spotbugs) (LGPL-2.1): Java static analysis; [Checkstyle](https://github.com/checkstyle/checkstyle) (LGPL-2.1): Java style; [Find Security Bugs](https://github.com/find-sec-bugs/find-sec-bugs) (LGPL-3.0): Java security analysis; [SonarQube Community Build](https://github.com/SonarSource/sonarqube) (LGPL-3.0): static analysis across languages |
| GPL-2.0, GPL-3.0 | Strong copyleft | [ShellCheck](https://github.com/koalaman/shellcheck) (GPL-3.0): shell static analysis; [yamllint](https://github.com/adrienverge/yamllint) (GPL-3.0): YAML lint; [Hadolint](https://github.com/hadolint/hadolint) (GPL-3.0): Dockerfile lint; [Cppcheck](https://github.com/danmar/cppcheck) (GPL-3.0): C and C++ static analysis; [Flawfinder](https://github.com/david-a-wheeler/flawfinder) (GPL-2.0): C and C++ security patterns; [golangci-lint](https://github.com/golangci/golangci-lint) (GPL-3.0): Go linter runner; [bundler-audit](https://github.com/rubysec/bundler-audit) (GPL-3.0): Ruby dependency vulnerabilities; [ansible-lint](https://github.com/ansible/ansible-lint) (GPL-3.0): Ansible lint; [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) (GPL-3.0): mobile application analysis |
| AGPL-3.0 | Network copyleft | [TruffleHog](https://github.com/trufflesecurity/trufflehog) (AGPL-3.0): secrets, with verification of live credentials; [Renovate](https://github.com/renovatebot/renovate) (AGPL-3.0): dependency updates; [AFL++](https://github.com/AFLplusplus/AFLplusplus) (AGPL-3.0): fuzzing; [MegaLinter](https://github.com/oxsecurity/megalinter) (AGPL-3.0): runner for many linters |
| Apache-2.0 with CC-BY-4.0 data | Mixed | [ScanCode Toolkit](https://github.com/aboutcode-org/scancode-toolkit) (Apache-2.0 AND CC-BY-4.0): licence and copyright detection |

---

## 5. Where A Paid Plan Or Other Terms Appear

An open-source tool can have a companion that is not free for private code. These were checked on the publishers' pages; other hosts and vendors were not checked.

| Tool or feature | Open-source part | What needs a plan or carries other terms |
| --- | --- | --- |
| Gitleaks GitHub Action | The Gitleaks CLI (MIT) | The action wrapper has had its own licence since version 2 and asks organisations for a licence key. Run the CLI directly. |
| CodeQL and host code scanning | The query libraries (MIT) | The CLI is under vendor terms. On GitHub, code scanning in private repositories needs a paid Code Security licence. |
| Dependency review action | The action (MIT) | On GitHub, private repositories need Code Security or Advanced Security. |
| Host-native secret scanning | None | On GitHub's Free plan it covers public repositories only; private repositories need a paid plan or add-on. |
| Artifact attestations | The [`actions/attest`](https://github.com/actions/attest) action (MIT); `attest-build-provenance` is now a wrapper on it | On GitHub's Free and Team plans, public repositories only; private repositories need the Enterprise plan. |
| Harden-Runner | The action (Apache-2.0) | The free tier covers public repositories on hosted runners. Private repositories and self-hosted runners need the paid tier. |
| Semgrep rules | The Semgrep Community Edition engine (LGPL-2.1) | The publisher's own rules carry a separate licence that allows internal business use and bars use in competing products. |
| taudit GitHub Action | taudit (MIT) | The action's repository carries no licence file at the date above, so the wrapper is not offered. |
| Renovate hosted app | The Renovate CLI and images (AGPL-3.0) | The hosted app is a vendor service under its own terms, which were not checked. The open-source route is to run it yourself. |

---

## 6. Not Offered

- **Not open source:** the CodeQL CLI (vendor terms), Brakeman (Brakeman Public Use License), Bearer CLI (Elastic License 2.0), and the Terraform CLI (Business Source License; OpenTofu is in §4).
- **Retired by the publisher:** Terrascan is archived, and tfsec's publisher directs users to Trivy.
- **Little recent activity at the date above:** cfn_nag, LicenseFinder, Security Code Scan, and Horusec.

---

## 7. Wiring A Scanner As A Gate

- **Make it binding.** A scanner step whose failure is discarded reports; it does not gate ([merge path](../principles/merge-path-evidence-and-pipeline-integrity.md) §2).
- **Pin the scanner.** It runs with the pipeline's privileges, so pin its version or digest and verify what is downloaded ([dependencies](../principles/dependencies-supply-chain.md) §1).
- **Run the same command locally and in CI** ([build](../principles/build.md) §3).
- **Scan on a schedule as well as at merge.** New advisories arrive for code that has not changed ([dependencies](../principles/dependencies-supply-chain.md) §3).
- **Keep the findings.** Results and SBOMs go to storage the organisation controls, not only the CI console ([build](../principles/build.md) §12).
- **Prove it can fail.** Plant a known finding and confirm the gate stops it ([engineering controls governance programme](../patterns/engineering-controls-governance-program.md) §2).

---

## References

Each tool name above links to the project's own repository, where its licence was read (S5, product-scoped; accessed 2026-11-18). Plan terms:

- GitHub — **Pricing** (plan comparison: attestations, secret scanning, code scanning) (S5; accessed 2026-11-18): https://github.com/pricing  
- GitHub Docs — **About code scanning** (S5; accessed 2026-11-18): https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning  
- GitHub Docs — **About dependency review** (S5; accessed 2026-11-18): https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review  
- gitleaks-action — **README**, licence key and licence change (S5; accessed 2026-11-18): https://github.com/gitleaks/gitleaks-action  
- Harden-Runner — **README**, pricing tiers (S5; accessed 2026-11-18): https://github.com/step-security/harden-runner  
- Semgrep — **Licensing** (S5; accessed 2026-11-18): https://docs.semgrep.dev/licensing  
- Renovate — **Documentation home**, licence and ways to run (S5; accessed 2026-11-18): https://docs.renovatebot.com/  
