# Scanner Tooling Map: Licences, Cost, And Coverage

Date and source access date: 2026-11-18. Repository basis: `8bd0c70`.
Status: research basis for [ADR 0060](../../docs/adr/0060-name-only-open-source-gate-tools-usable-without-a-paid-plan.md) (accepted 2026-11-18). Model research and model review; no independent human or domain review.

## Question

The library names scanner classes and maps them to categories of tool. Which concrete tools can it name under three conditions set by the maintainer: open source and usable in an enterprise without cost; Apache-2.0 and MIT listed first, other open-source licences apart; and coverage of the languages an enterprise estate is likely to hold, not only the maintainer's own?

## Method

1. **Candidates.** The list started from the quality gates configured in the maintainer's own repositories, read from their pipeline and hook definitions. That inventory is private and is not reproduced here. It was Rust-heavy, so the common tools for nine other language ecosystems and for infrastructure formats were added.
2. **Licence.** For each candidate, the licence detected on the project's own repository was read through the host's API. Where detection returned no answer, the licence file or the package manifest in the repository was read.
3. **Cost.** For tools with a known companion service or hosted feature, the publisher's own README, documentation, or pricing page was read for what a private repository needs.
4. **Purpose.** What each tool is for is taken from the project's own one-line description.

Classes follow [Source Authority And Evidence Grading](../patterns/source-authority-and-evidence-grading.md) §2. Every source is S5: a project or vendor describing its own product, in scope for its own licence and terms. No archive copies were captured.

## Findings

1. **The gap is real.** Before this change no active page named a secret scanner, a vulnerability scanner, an infrastructure scanner, or a workflow linter.
2. **Most candidates pass the first test.** Of 140 entries across 137 repositories, 106 carry Apache-2.0 or MIT (including dual licences, MIT-0, and the LLVM exceptions) and 34 carry another open-source licence.
3. **Recall is not a safe source for licences.** One widely used fuzzer's repository now carries AGPL-3.0, with Apache-2.0 and commercial licence files beside it. A Rails security scanner carries a public-use licence that is not open source. A code scanner carries the Elastic License 2.0. The best-known infrastructure CLI carries the Business Source License. Each would have been listed wrongly from memory.
4. **Some classes have no Apache-2.0 or MIT tool.** Shell and YAML linting, Dockerfile linting, Ruby dependency auditing, and general multi-language static analysis are served only by copyleft tools. Ruby security analysis has no open-source option among the candidates.
5. **Open-source tools ship with companions that are not free for private code.** Eight were confirmed; the table below records them.
6. **One candidate is the maintainer's own.** taudit, a CI/CD authority scanner, is public. Its maintainer relicensed it from AGPL-3.0-or-later to MIT on 2026-11-18, and its published repository carries MIT. It meets the selection rule and is listed in the first table under a disclosed exception (ADR 0060 D6). Its GitHub Action repository has no licence file, so the wrapper is not offered.
7. **Several projects are fading.** Two are archived by their publishers, one publisher directs users to a successor, and four show little recent activity.

## Plan Terms Checked

| Tool or feature | What the publisher's page says | Source |
| --- | --- | --- |
| Gitleaks GitHub Action | From version 2 the action's licence changed from MIT; organisation accounts need a licence key, personal accounts do not. The key was described as free | [gitleaks-action README](https://github.com/gitleaks/gitleaks-action) |
| Code scanning | Code scanning on private repositories needs a GitHub Code Security licence | [About code scanning](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning) |
| CodeQL CLI | Distributed under GitHub CodeQL Terms and Conditions; the query repository is MIT | [codeql-cli-binaries licence](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md) |
| Dependency review action | Available for public repositories, and for private repositories with Code Security or Advanced Security enabled | [About dependency review](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review) |
| Secret scanning, artifact attestations | Free plan: public repositories only for both. Attestations: Team plan public only, Enterprise included | [Pricing](https://github.com/pricing) |
| Harden-Runner | Community tier free for public repositories on hosted runners; private repositories and self-hosted runners need the Enterprise tier | [harden-runner README](https://github.com/step-security/harden-runner) |
| Semgrep | Engine is LGPL 2.1. Publisher-maintained rules are under the Semgrep Rules License v1.0: internal business use allowed, use in competing products or services not | [Semgrep licensing](https://docs.semgrep.dev/licensing) |
| taudit GitHub Action | The action's repository has no licence file | [taudit-action repository](https://github.com/0ryant/taudit-action) |
| Renovate | AGPL-3.0-only; runs as an open-source package or image, or as an app hosted by a vendor. The hosted app's pricing is not stated on the page read | [Renovate documentation](https://docs.renovatebot.com/) |

Not checked: plan terms on hosts other than GitHub; edition limits of SonarQube Community Build; the terms of the vulnerability databases that scanners download.

## Licence Ledger

As read on 2026-11-18. "Apache-2.0" may stand for a dual Apache-2.0 and MIT project where the host reports one of the two.

| Tool | Repository | Licence as read |
| --- | --- | --- |
| Atheris | [google/atheris](https://github.com/google/atheris) | Apache-2.0 |
| audit-ci | [IBM/audit-ci](https://github.com/IBM/audit-ci) | Apache-2.0 |
| Bandit | [PyCQA/bandit](https://github.com/PyCQA/bandit) | Apache-2.0 |
| Buf | [bufbuild/buf](https://github.com/bufbuild/buf) | Apache-2.0 |
| cargo-cyclonedx | [CycloneDX/cyclonedx-rust-cargo](https://github.com/CycloneDX/cyclonedx-rust-cargo) | Apache-2.0 |
| cargo-deny | [EmbarkStudios/cargo-deny](https://github.com/EmbarkStudios/cargo-deny) | Apache-2.0 |
| cargo-fuzz | [rust-fuzz/cargo-fuzz](https://github.com/rust-fuzz/cargo-fuzz) | Apache-2.0 |
| cargo-llvm-cov | [taiki-e/cargo-llvm-cov](https://github.com/taiki-e/cargo-llvm-cov) | Apache-2.0 |
| cargo-semver-checks | [obi1kenobi/cargo-semver-checks](https://github.com/obi1kenobi/cargo-semver-checks) | Apache-2.0 |
| cargo-vet | [mozilla/cargo-vet](https://github.com/mozilla/cargo-vet) | Apache-2.0 |
| cdxgen | [cdxgen/cdxgen](https://github.com/cdxgen/cdxgen) | Apache-2.0 |
| Checkov | [bridgecrewio/checkov](https://github.com/bridgecrewio/checkov) | Apache-2.0 |
| Clippy | [rust-lang/rust-clippy](https://github.com/rust-lang/rust-clippy) | Apache-2.0 |
| ClusterFuzzLite | [google/clusterfuzzlite](https://github.com/google/clusterfuzzlite) | Apache-2.0 |
| Conftest | [open-policy-agent/conftest](https://github.com/open-policy-agent/conftest) | Apache-2.0 |
| cosign | [sigstore/cosign](https://github.com/sigstore/cosign) | Apache-2.0 |
| coverage.py | [nedbat/coveragepy](https://github.com/nedbat/coveragepy) | Apache-2.0 |
| CycloneDX Gradle plugin | [CycloneDX/cyclonedx-gradle-plugin](https://github.com/CycloneDX/cyclonedx-gradle-plugin) | Apache-2.0 |
| CycloneDX Maven plugin | [CycloneDX/cyclonedx-maven-plugin](https://github.com/CycloneDX/cyclonedx-maven-plugin) | Apache-2.0 |
| cyclonedx-dotnet | [CycloneDX/cyclonedx-dotnet](https://github.com/CycloneDX/cyclonedx-dotnet) | Apache-2.0 |
| cyclonedx-gomod | [CycloneDX/cyclonedx-gomod](https://github.com/CycloneDX/cyclonedx-gomod) | Apache-2.0 |
| cyclonedx-node-npm | [CycloneDX/cyclonedx-node-npm](https://github.com/CycloneDX/cyclonedx-node-npm) | Apache-2.0 |
| cyclonedx-python | [CycloneDX/cyclonedx-python](https://github.com/CycloneDX/cyclonedx-python) | Apache-2.0 |
| detect-secrets | [Yelp/detect-secrets](https://github.com/Yelp/detect-secrets) | Apache-2.0 |
| detekt | [detekt/detekt](https://github.com/detekt/detekt) | Apache-2.0 |
| Dockle | [goodwithtech/dockle](https://github.com/goodwithtech/dockle) | Apache-2.0 |
| Error Prone | [google/error-prone](https://github.com/google/error-prone) | Apache-2.0 |
| eslint-plugin-security | [eslint-community/eslint-plugin-security](https://github.com/eslint-community/eslint-plugin-security) | Apache-2.0 |
| go-licenses | [google/go-licenses](https://github.com/google/go-licenses) | Apache-2.0 |
| gosec | [securego/gosec](https://github.com/securego/gosec) | Apache-2.0 |
| Grype | [anchore/grype](https://github.com/anchore/grype) | Apache-2.0 |
| Helm lint | [helm/helm](https://github.com/helm/helm) | Apache-2.0 |
| Jazzer | [CodeIntelligenceTesting/jazzer](https://github.com/CodeIntelligenceTesting/jazzer) | Apache-2.0 |
| Jazzer.js | [CodeIntelligenceTesting/jazzer.js](https://github.com/CodeIntelligenceTesting/jazzer.js) | Apache-2.0 |
| KICS | [Checkmarx/kics](https://github.com/Checkmarx/kics) | Apache-2.0 |
| kubeconform | [yannh/kubeconform](https://github.com/yannh/kubeconform) | Apache-2.0 |
| KubeLinter | [stackrox/kube-linter](https://github.com/stackrox/kube-linter) | Apache-2.0 |
| Kubescape | [kubescape/kubescape](https://github.com/kubescape/kubescape) | Apache-2.0 |
| Kyverno | [kyverno/kyverno](https://github.com/kyverno/kyverno) | Apache-2.0 |
| lychee | [lycheeverse/lychee](https://github.com/lycheeverse/lychee) | Apache-2.0 |
| oasdiff | [oasdiff/oasdiff](https://github.com/oasdiff/oasdiff) | Apache-2.0 |
| OpenSSF Scorecard | [ossf/scorecard](https://github.com/ossf/scorecard) | Apache-2.0 |
| OSS Review Toolkit | [oss-review-toolkit/ort](https://github.com/oss-review-toolkit/ort) | Apache-2.0 |
| OSS-Fuzz | [google/oss-fuzz](https://github.com/google/oss-fuzz) | Apache-2.0 |
| OSV-Scanner | [google/osv-scanner](https://github.com/google/osv-scanner) | Apache-2.0 |
| OWASP Dependency-Check | [dependency-check/DependencyCheck](https://github.com/dependency-check/DependencyCheck) | Apache-2.0 |
| pip-audit | [pypa/pip-audit](https://github.com/pypa/pip-audit) | Apache-2.0 |
| PIT | [hcoles/pitest](https://github.com/hcoles/pitest) | Apache-2.0 |
| Polaris | [FairwindsOps/polaris](https://github.com/FairwindsOps/polaris) | Apache-2.0 |
| Retire.js | [RetireJS/retire.js](https://github.com/RetireJS/retire.js) | Apache-2.0 |
| Roslynator | [dotnet/roslynator](https://github.com/dotnet/roslynator) | Apache-2.0 |
| SLSA GitHub generator | [slsa-framework/slsa-github-generator](https://github.com/slsa-framework/slsa-github-generator) | Apache-2.0 |
| Spectral | [stoplightio/spectral](https://github.com/stoplightio/spectral) | Apache-2.0 |
| Spotless | [diffplug/spotless](https://github.com/diffplug/spotless) | Apache-2.0 |
| Stryker.NET | [stryker-mutator/stryker-net](https://github.com/stryker-mutator/stryker-net) | Apache-2.0 |
| StrykerJS | [stryker-mutator/stryker-js](https://github.com/stryker-mutator/stryker-js) | Apache-2.0 |
| Syft | [anchore/syft](https://github.com/anchore/syft) | Apache-2.0 |
| Trivy | [aquasecurity/trivy](https://github.com/aquasecurity/trivy) | Apache-2.0 |
| TypeScript compiler | [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | Apache-2.0 |
| ZAP | [zaproxy/zaproxy](https://github.com/zaproxy/zaproxy) | Apache-2.0 |
| cargo-audit | [rustsec/rustsec](https://github.com/rustsec/rustsec) | Apache-2.0 OR MIT |
| clang-tidy and the Clang static analyzer | [llvm/llvm-project](https://github.com/llvm/llvm-project) | Apache-2.0 WITH LLVM-exception |
| libFuzzer | [llvm/llvm-project](https://github.com/llvm/llvm-project) | Apache-2.0 WITH LLVM-exception |
| the LLVM sanitizers | [llvm/llvm-project](https://github.com/llvm/llvm-project) | Apache-2.0 WITH LLVM-exception |
| .NET SDK analyzers | [dotnet/sdk](https://github.com/dotnet/sdk) | MIT |
| composer audit | [composer/composer](https://github.com/composer/composer) | MIT |
| dotnet list package --vulnerable | [dotnet/sdk](https://github.com/dotnet/sdk) | MIT |
| actionlint | [rhysd/actionlint](https://github.com/rhysd/actionlint) | MIT |
| Bicep linter | [Azure/bicep](https://github.com/Azure/bicep) | MIT |
| cargo-mutants | [sourcefrog/cargo-mutants](https://github.com/sourcefrog/cargo-mutants) | MIT |
| commitlint | [conventional-changelog/commitlint](https://github.com/conventional-changelog/commitlint) | MIT |
| coverlet | [coverlet-coverage/coverlet](https://github.com/coverlet-coverage/coverlet) | MIT |
| Dependabot core | [dependabot/dependabot-core](https://github.com/dependabot/dependabot-core) | MIT |
| ESLint | [eslint/eslint](https://github.com/eslint/eslint) | MIT |
| Gitleaks | [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks) | MIT |
| Infer | [facebook/infer](https://github.com/facebook/infer) | MIT |
| ktlint | [pinterest/ktlint](https://github.com/pinterest/ktlint) | MIT |
| Lefthook | [evilmartians/lefthook](https://github.com/evilmartians/lefthook) | MIT |
| markdownlint-cli2 | [DavidAnson/markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2) | MIT |
| mypy | [python/mypy](https://github.com/python/mypy) | MIT |
| Nuclei | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei) | MIT |
| NullAway | [uber/NullAway](https://github.com/uber/NullAway) | MIT |
| OWASP dep-scan | [owasp-dep-scan/dep-scan](https://github.com/owasp-dep-scan/dep-scan) | MIT |
| PHPStan | [phpstan/phpstan](https://github.com/phpstan/phpstan) | MIT |
| pip-licenses | [raimon49/pip-licenses](https://github.com/raimon49/pip-licenses) | MIT |
| pre-commit | [pre-commit/pre-commit](https://github.com/pre-commit/pre-commit) | MIT |
| Prettier | [prettier/prettier](https://github.com/prettier/prettier) | MIT |
| Psalm | [vimeo/psalm](https://github.com/vimeo/psalm) | MIT |
| Pyright | [microsoft/pyright](https://github.com/microsoft/pyright) | MIT |
| pytest | [pytest-dev/pytest](https://github.com/pytest-dev/pytest) | MIT |
| RuboCop | [rubocop/rubocop](https://github.com/rubocop/rubocop) | MIT |
| Ruff | [astral-sh/ruff](https://github.com/astral-sh/ruff) | MIT |
| SBOM Tool | [microsoft/sbom-tool](https://github.com/microsoft/sbom-tool) | MIT |
| SharpFuzz | [Metalnem/sharpfuzz](https://github.com/Metalnem/sharpfuzz) | MIT |
| SimpleCov | [simplecov-ruby/simplecov](https://github.com/simplecov-ruby/simplecov) | MIT |
| SQLFluff | [sqlfluff/sqlfluff](https://github.com/sqlfluff/sqlfluff) | MIT |
| Staticcheck | [dominikh/go-tools](https://github.com/dominikh/go-tools) | MIT |
| Super-Linter | [super-linter/super-linter](https://github.com/super-linter/super-linter) | MIT |
| SwiftLint | [realm/SwiftLint](https://github.com/realm/SwiftLint) | MIT |
| taudit | [0ryant/taudit](https://github.com/0ryant/taudit) | MIT |
| typescript-eslint | [typescript-eslint/typescript-eslint](https://github.com/typescript-eslint/typescript-eslint) | MIT |
| Vitest | [vitest-dev/vitest](https://github.com/vitest-dev/vitest) | MIT |
| zizmor | [zizmorcore/zizmor](https://github.com/zizmorcore/zizmor) | MIT |
| Biome | [biomejs/biome](https://github.com/biomejs/biome) | MIT OR Apache-2.0 |
| typos | [crate-ci/typos](https://github.com/crate-ci/typos) | MIT OR Apache-2.0 |
| cfn-lint | [aws-cloudformation/cfn-lint](https://github.com/aws-cloudformation/cfn-lint) | MIT-0 |
| AFL++ | [AFLplusplus/AFLplusplus](https://github.com/AFLplusplus/AFLplusplus) | AGPL-3.0 |
| MegaLinter | [oxsecurity/megalinter](https://github.com/oxsecurity/megalinter) | AGPL-3.0 |
| Renovate | [renovatebot/renovate](https://github.com/renovatebot/renovate) | AGPL-3.0 |
| TruffleHog | [trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog) | AGPL-3.0 |
| ScanCode Toolkit | [aboutcode-org/scancode-toolkit](https://github.com/aboutcode-org/scancode-toolkit) | Apache-2.0 AND CC-BY-4.0 |
| the npm CLI (npm audit) | [npm/cli](https://github.com/npm/cli) | Artistic-2.0 |
| govulncheck | [golang/vuln](https://github.com/golang/vuln) | BSD-3-Clause |
| Infection | [infection/infection](https://github.com/infection/infection) | BSD-3-Clause |
| mutmut | [boxed/mutmut](https://github.com/boxed/mutmut) | BSD-3-Clause |
| PHP_CodeSniffer | [PHPCSStandards/PHP_CodeSniffer](https://github.com/PHPCSStandards/PHP_CodeSniffer) | BSD-3-Clause |
| Scalafix | [scalacenter/scalafix](https://github.com/scalacenter/scalafix) | BSD-3-Clause |
| shfmt | [mvdan/sh](https://github.com/mvdan/sh) | BSD-3-Clause |
| the Go toolchain (go vet, native fuzzing, coverage) | [golang/go](https://github.com/golang/go) | BSD-3-Clause |
| PMD | [pmd/pmd](https://github.com/pmd/pmd) | BSD-style |
| JaCoCo | [jacoco/jacoco](https://github.com/jacoco/jacoco) | EPL-2.0 |
| Flawfinder | [david-a-wheeler/flawfinder](https://github.com/david-a-wheeler/flawfinder) | GPL-2.0 |
| ansible-lint | [ansible/ansible-lint](https://github.com/ansible/ansible-lint) | GPL-3.0 |
| bundler-audit | [rubysec/bundler-audit](https://github.com/rubysec/bundler-audit) | GPL-3.0 |
| Cppcheck | [danmar/cppcheck](https://github.com/danmar/cppcheck) | GPL-3.0 |
| golangci-lint | [golangci/golangci-lint](https://github.com/golangci/golangci-lint) | GPL-3.0 |
| Hadolint | [hadolint/hadolint](https://github.com/hadolint/hadolint) | GPL-3.0 |
| MobSF | [MobSF/Mobile-Security-Framework-MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) | GPL-3.0 |
| ShellCheck | [koalaman/shellcheck](https://github.com/koalaman/shellcheck) | GPL-3.0 |
| yamllint | [adrienverge/yamllint](https://github.com/adrienverge/yamllint) | GPL-3.0 |
| Knip | [webpro-nl/knip](https://github.com/webpro-nl/knip) | ISC |
| Checkstyle | [checkstyle/checkstyle](https://github.com/checkstyle/checkstyle) | LGPL-2.1 |
| Opengrep | [opengrep/opengrep](https://github.com/opengrep/opengrep) | LGPL-2.1 |
| Semgrep Community Edition | [semgrep/semgrep](https://github.com/semgrep/semgrep) | LGPL-2.1 |
| SpotBugs | [spotbugs/spotbugs](https://github.com/spotbugs/spotbugs) | LGPL-2.1 |
| Find Security Bugs | [find-sec-bugs/find-sec-bugs](https://github.com/find-sec-bugs/find-sec-bugs) | LGPL-3.0 |
| SonarQube Community Build | [SonarSource/sonarqube](https://github.com/SonarSource/sonarqube) | LGPL-3.0 |
| Hypothesis | [HypothesisWorks/hypothesis](https://github.com/HypothesisWorks/hypothesis) | MPL-2.0 |
| OpenTofu (tofu validate, tofu fmt) | [opentofu/opentofu](https://github.com/opentofu/opentofu) | MPL-2.0 |
| TFLint | [terraform-linters/tflint](https://github.com/terraform-linters/tflint) | MPL-2.0 |

Named but not offered: the CodeQL CLI (vendor terms), Brakeman (Brakeman Public Use License), Bearer CLI (Elastic License 2.0), the Terraform CLI (Business Source License), Terrascan and the original OWASP Dependency-Check repository (archived; Dependency-Check continues in the repository listed above), tfsec (publisher directs users to Trivy), and cfn_nag, LicenseFinder, Security Code Scan, and Horusec (little recent activity).

## Decision Input

| Decision | Basis | Admission |
| --- | --- | --- |
| Offer only open-source tools that need no paid plan for private code | The maintainer's stated need; licence and plan facts above | A rule about what the library names, not a claim about external practice. No typed strength |
| List Apache-2.0 and MIT first, other licences apart | The maintainer's instruction | Presentation |
| Cover ten language ecosystems | The maintainer's instruction; candidates from each ecosystem's common tools | Illustrative content; each entry cites its own repository (S5) |

## Residual Risk

The host's licence detection can be wrong or partial, and a repository can mix licences. Only tools with a known companion were checked for cost. Purposes come from one-line descriptions, not from use; only the maintainer's own stack has been exercised. The choice of which tools count as common for each language is the model's judgement. No independent review is recorded.
