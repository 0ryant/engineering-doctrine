# Dependencies And Supply Chain

Durable rules for **third-party code** in production: **pinning**, **updates**, **licensing**, and **evidence** (SBOM) aligned with security and compliance expectations.

---

## 1. Pinning And Lockfiles

- **Lock** dependency resolution for applications (`Cargo.lock`, `package-lock.json`, `poetry.lock`, etc.) and **commit** locks for reproducible builds.
- **Libraries** intended for consumption follow ecosystem norms (some ecosystems omit lockfiles for libs—document the rule per language).

**Why:** Reproducible builds and CI are impossible if two installs resolve different graphs.

---

## 2. Update Cadence And Automation

- **Automate** update PRs with human review; do not rely on **ad-hoc** `npm update` before releases only.
- **Security patches** merge on an **SLA** appropriate to severity. **Example organisational defaults** (adjust per sector and policy—publish yours in an estate or security doc):

| Severity (typical CVSS-aligned) | Target time to **patched release** or **approved compensating control** |
| --- | --- |
| **Critical** (e.g. network RCE, trivial auth bypass, wormable) | **24 hours** |
| **High** | **7 calendar days** |
| **Medium** | **30 calendar days** or next **scheduled** maintenance window (whichever is sooner) |
| **Low** | Next **regular** dependency cadence (e.g. weekly/biweekly bot merge) |

**Why:** Outdated dependencies are a **known** attack surface; automation reduces toil and inconsistency across repos. **Named SLAs** prevent “we’ll get to it” drift without pretending every CVE is equal.

---

## 3. SBOM Generation And Attachment

- Produce an **SBOM** (Software Bill of Materials) for **every shipped artefact** — not only on request, and not only when regulators ask. Attach it to the artefact at build time so the questions "what was in this binary?" and "is this vulnerable component in production?" are answerable in seconds.
- **Format choice**: prefer **CycloneDX** (ECMA-424) for supply-chain depth (includes VEX, Cryptography BOM, AI/ML-BOM) or **SPDX** (ISO/IEC 5962:2021) where licence compliance is the primary driver. Either is acceptable; pick one per build pipeline and be consistent.
- **NTIA minimum elements** per component: name, version, unique identifier (PURL or CPE), supplier name, dependency relationships, known vulnerability references, and timestamp.
- **When to generate**: per-build for customer-facing or regulated software; per-release minimum for internal-only tooling. Do not rely on post-hoc reconstruction from VCS.
- **Attachment**: for container images, embed as an **OCI attestation** (standard in GHCR, ECR, GCR); for standalone binaries and packages, publish an adjacent `.sbom.json` alongside the release artefact. Machine-readable JSON or XML only — plain-text SBOMs cannot be reliably parsed.
- **SCA** (dependency scanning) and **secret scanning** run on every merge path, and separately on a scheduled cadence to catch newly published vulnerabilities against already-merged code.

**Why:** EU Cyber Resilience Act, US Executive Order 14028, and enterprise procurement increasingly treat **SBOM** as non-negotiable evidence. SCA on the merge path alone misses vulnerabilities disclosed after merge.

---

## 4. SLSA: Build Provenance And Pipeline Integrity

- **Target SLSA L2 as the starting baseline** for any artefact that ships externally or to regulated environments. SLSA L3 is the mature target for critical or customer-facing software. SLSA L1 (documented-but-unsigned provenance) is acceptable only for internal-only tooling.
- **SLSA level requirements** (abbreviated):

  | Level | Provenance | Key requirement |
  | --- | --- | --- |
  | **L1** | Unsigned, formatted | Build process documented; output includes provenance file |
  | **L2** | Signed; hosted platform prevents user tampering | Build runs on a hosted service (GitHub Actions, Azure DevOps) that generates and signs provenance; user config cannot influence the provenance itself |
  | **L3** | Signed; strict isolation between builds | Builds cannot influence each other's provenance; no shared writable cache across builds; separation of duties between build and signing |

- **Hermetic builds**: pin toolchain versions (compiler, base image by digest, not by tag), commit lockfiles, and ensure the build environment cannot fetch packages from the network during build. Two builds from the same inputs must produce the same output.
- **Base image pinning**: reference container base images by **digest** (`FROM golang:1.24.0@sha256:...`), not by mutable tag. Verify digest before pull in security-sensitive pipelines.
- **Build provenance attestation**: emit a signed provenance document (SLSA provenance JSON) as part of the build output; attach to the artefact via `cosign attest` or the SLSA GitHub generator action. This document answers "which commit, which pipeline, which runner produced this binary?"

**Why:** Supply-chain attacks increasingly target the build pipeline rather than the source code. SLSA provenance makes tampering between source and artefact **detectable**, not merely **prohibited**.

---

## 5. Artifact Signing With Sigstore

- **Sign container images and release binaries** using **cosign** with keyless signing via OIDC. In a hosted CI environment (GitHub Actions, Azure DevOps with Workload Identity), no long-lived private key is required — the CI runtime obtains a short-lived certificate from **Fulcio**, signs the artefact, and records the signature in the **Rekor** transparency log.
- **Verification** at deploy time: consumers validate the signature against the Rekor ledger and the identity that was permitted to sign (e.g., only the `release` workflow in `org/repo` may sign production images).
- **No long-lived signing keys in secret stores** for build pipelines that support OIDC. Key rotation burden and secret exfiltration risk both drop to zero for keyless flows.
- Where keyless signing is not available (air-gapped or legacy environments), use **cosign** with a KMS-backed key and rotate per the estates key-rotation policy.

**Why:** Signature verification closes the gap between "we fetched this image from our registry" and "we know this image was built from commit X by our authorised CI pipeline, not by anyone else."

---

## 6. Licensing

- Maintain an **allowlist** or policy for **OSS licences** in distributed software; generate **NOTICE** / attribution files where required.

**Why:** Licence violations are **legal** risk; copying code without licence clarity is not acceptable at scale.

---

## 7. Registry Hygiene, Dependency Confusion, And Disclosure

- **Scoped package names** for internal libraries where the ecosystem supports them (e.g. `@org/my-lib` for npm). Scoped names prevent dependency confusion attacks where an attacker publishes a package with the same unscoped name to a public registry.
- **Private registry precedence**: configure package managers to resolve internal packages from the private registry **first**, and validate lockfile integrity in CI (`npm ci`, `poetry install --no-update`, `go mod verify`). A regenerated lockfile that differs from the committed one is a build failure.
- **VEX (Vulnerability Exploitability eXchange)**: for SaaS or shrink-wrapped products with SBOMs, publish VEX documents to clarify which reported vulnerabilities are not reachable or not exploitable in your build configuration. CycloneDX supports VEX natively.
- **Vulnerability disclosure to users** — for **shrink-wrapped** or **SaaS** products, coordinate **customer** comms with [secure-development-lifecycle.md](secure-development-lifecycle.md) (responsive vulnerability handling) and legal/comms.

**Why:** Registry attacks and dependency confusion are **documented** incidents, not theoretical risks. VEX reduces noise from SBOM scanners and prevents unnecessary customer escalations for vulnerabilities in code paths that are never executed.

---


## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Automation + review | Balances **velocity** with **governance**; blocks neither security nor shipping. |
| SBOM per build | Makes incidents and audits **factual** ("what was in build X?") — not reconstructed after the fact. |
| CycloneDX preferred over SPDX | Better tooling support for VEX and security extensions; SPDX remains an acceptable alternative. |
| SLSA L2 as starting target | Achievable with standard CI providers; L3 (hermetic) reserved for mature pipelines. |
| Keyless cosign (OIDC + Rekor) | Eliminates long-lived signing key management; transparency log adds public accountability. |
| Scoped package names + lockfile CI | Prevents dependency confusion attacks at zero cost; `npm ci` / `poetry install --no-update` enforce integrity. |
| Explicit licence policy | Prevents **surprise** copyleft or attribution gaps in releases. |
| Published patch SLAs | Makes vulnerability response **measurable**; aligns with SSDF-style expectations. |

---

## References

- OWASP **Dependency-Check** / SCA concept (industry framing): https://owasp.org/www-project-dependency-check/
- SPDX — **Software Bill of Materials** specification: https://spdx.dev/
- NTIA / CISA **SBOM** minimum elements (US guidance): https://www.ntia.gov/SBOM
- White House **Executive Order 14028** (secure software supply chain): https://www.federalregister.gov/documents/2021/05/17/2021-10460/improving-the-nations-cybersecurity
- **SLSA** — Supply-chain Levels for Software Artifacts: https://slsa.dev/
- **SLSA** Getting Started guide: https://slsa.dev/get-started
- **Sigstore** — keyless signing and transparency: https://www.sigstore.dev/
- **CycloneDX** — SBOM and VEX standard: https://cyclonedx.org/
- EU **Cyber Resilience Act** (CRA) — SBOM and vulnerability disclosure obligations: https://www.european-parliament.europa.eu/doceo/document/TA-9-2024-0130_EN.pdf
- OpenSSF **Supply-chain attacks** (awareness): https://openssf.org/
