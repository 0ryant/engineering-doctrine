# Dependencies And Supply Chain

Durable rules for **third-party code** in production: **pinning**, **updates**, **licensing**, and **evidence** (SBOM) aligned with security and compliance expectations. Admission of **AI-proposed** dependencies is gated pre-install per [ai-ml-systems.md](ai-ml-systems.md) §4, enforced here (§7). When a supplier, build service, support path, external model, or other dependency enters a declared contractual/regulatory boundary, [Revision-Pinned External Control Profiles](../patterns/revision-pinned-control-profiles.md) records the exact authority, baseline revision, scope, assessment evidence, flow-down obligations, and exceptions.

---

## 1. Pinning And Lockfiles

- **Lock** dependency resolution for applications (`Cargo.lock`, `package-lock.json`, `poetry.lock`, etc.) and **commit** locks for reproducible builds.
- **Libraries** intended for consumption follow ecosystem norms (some ecosystems omit lockfiles for libs—document the rule per language).

**Why:** Reproducible builds and CI are impossible if two installs resolve different graphs.

---

## 2. Update Cadence And Automation

- **Automate** update PRs with human review; do not rely on **ad-hoc** `npm update` before releases only.
- **Security patches** merge on an **SLA** appropriate to severity. **Example estate defaults** (adjust per sector, **CISA KEV** / regulatory duty, internet exposure, and compensating controls—publish **yours** in an estate or security doc; numbers below are **illustrative**, not universal law):

| Severity (typical CVSS-aligned) | Target time to **patched release** or **approved compensating control** |
| --- | --- |
| **Critical** (e.g. network RCE, trivial auth bypass, wormable) | **24 hours** |
| **High** | **7 calendar days** |
| **Medium** | **30 calendar days** or next **scheduled** maintenance window (whichever is sooner) |
| **Low** | Next **regular** dependency cadence (e.g. weekly/biweekly bot merge) |

- **Known-exploited and triage order** — when a component matches [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) (or your estate’s equivalent **weaponisation** feed), treat it as **highest** urgency regardless of “ordinary” severity tables; use [FIRST EPSS](https://www.first.org/epss/user-guide) and asset context to **rank** non-KEV backlog, not to **ignore** KEV.
- **Protocol dependencies with published lifecycles** — when a protocol adopted under [Revision-Pinned External Control Profiles](../patterns/revision-pinned-control-profiles.md) publishes a deprecation policy (for example **MCP**'s minimum **twelve-month** deprecation window — [2026-07-28 changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog)), treat announced deprecations as **update-cadence inputs**: schedule migration off deprecated features **inside** the publisher's window against the pinned revision in the profile record — not as an emergency when removal ships.

**Why:** Outdated dependencies are a **known** attack surface; automation reduces toil and inconsistency across repos. **Named SLAs** prevent “we’ll get to it” drift without pretending every CVE is equal.

---

## 3. SBOM Generation And Attachment

- Produce an **SBOM** (Software Bill of Materials) for **every shipped artefact** — not only on request, and not only when regulators ask. Attach it to the artefact at build time so the questions "what was in this binary?" and "is this vulnerable component in production?" are answerable in seconds.
- **Format choice**: prefer **CycloneDX** (ECMA-424) for supply-chain depth (includes VEX, Cryptography BOM, AI/ML-BOM) or **SPDX** (ISO/IEC 5962:2021) where licence compliance is the primary driver. Either is acceptable; pick one per build pipeline and be consistent.
- **NTIA minimum elements** per component: name, version, unique identifier (PURL or CPE), supplier name, dependency relationships, known vulnerability references, and timestamp.
- **When to generate**: per-build for customer-facing or regulated software; per-release minimum for internal-only tooling. Do not rely on post-hoc reconstruction from VCS.
- **Attachment**: for container images, embed as an **OCI attestation** (standard in GHCR, ECR, GCR); for standalone binaries and packages, publish an adjacent `.sbom.json` alongside the release artefact. Machine-readable JSON or XML only — plain-text SBOMs cannot be reliably parsed. Generation alone is insufficient for operations: each **immutable** artefact digest/version should retain an **SBOM** that can be **re-scanned** against **current** advisory feeds ([SPDX](https://spdx.dev/), [CycloneDX](https://cyclonedx.org/)—see [../REFERENCES.md](../REFERENCES.md)).
- **Continuous feed-backed re-evaluation** — on **promotion** or **deploy** to an environment, and when **material** feed updates land, re-check the **same** SBOM identity (**purl** / version / hash where available) against vulnerability intelligence; merge-time green does **not** authorise deploy after **new** disclosures unless policy explicitly allows a time-bounded exception ([merge-path-evidence-and-pipeline-integrity.md](merge-path-evidence-and-pipeline-integrity.md)).
- **Triage before promotion** — a releasable artefact with newly disclosed vulnerable components is **remediated**, **blocked**, or released only under an **explicit** risk acceptance with **owner**, **expiry**, and **compensating control** recorded next to the artefact evidence.
- **VEX / exploitability** — when a CVE appears in the SBOM but the shipped configuration is **not exploitable**, record disposition with **scope** (artefact version, environment) using a **VEX** document or equivalent **signed** attestation (for example CycloneDX [VEX](https://cyclonedx.org/capabilities/vex/)) so promotion evidence stays honest—**not** to replace scanning or future re-evaluation when code or reachability changes.
- **SCA** (dependency scanning) and **secret scanning** run on every merge path, and separately on a scheduled cadence to catch newly published vulnerabilities against already-merged code.

**Why:** EU Cyber Resilience Act, US Executive Order 14028, and enterprise procurement increasingly treat **SBOM** as non-negotiable evidence. SCA on the merge path alone misses vulnerabilities disclosed after merge, and **AI-accelerated disclosure** widens the gap between “we built once with a green scan” and “what is exposed **now**.”

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

## 7. Registry Hygiene, Dependency Confusion, Slopsquatting, And Disclosure

- **Scoped package names** for internal libraries where the ecosystem supports them (e.g. `@org/my-lib` for npm). Scoped names prevent dependency confusion attacks where an attacker publishes a package with the same unscoped name to a public registry.
- **Private registry precedence**: configure package managers to resolve internal packages from the private registry **first**, and validate lockfile integrity in CI (`npm ci`, `poetry install --no-update`, `go mod verify`). A regenerated lockfile that differs from the committed one is a build failure.
- **Slopsquatting is distinct from dependency confusion — and the controls above do not stop it.** An LLM or agent invents a **plausible but non-existent** package name; an attacker registers that name on the public registry; installation then **succeeds legitimately**. There is no internal name to scope, nothing for private-registry precedence to shadow, and the resulting **lockfile is internally consistent**, so lockfile-integrity CI passes. The names are **repeatable, hence squattable**: across 2.23 million packages recommended by 16 code-generating LLMs, **19.7%** were hallucinations (205,474 unique names; ~5.2% for commercial models vs 21.7% for open-source), and **43%** of hallucinated names recurred in **all ten** re-runs of the same prompt ([Spracklen et al., USENIX Security 2025](https://arxiv.org/abs/2406.10279) — measured on a **2024 model cohort**; the **2026 frontier-cohort** replication finds lower per-model rates of **4.62–6.10%** but **127** package names all five evaluated models invent **identically**, **53** still registrable after registry defences — [Churilov 2026](https://arxiv.org/abs/2605.17062)). Separately, the surface is proven live: a researcher-registered PyPI package matching the widely hallucinated `huggingface-cli` name drew **15,000+** downloads in three months ([The Register, 2024-03-28](https://www.theregister.com/2024/03/28/ai_bots_hallucinate_software_packages/)), and the hallucinated npm name `react-codeshift` spread through 47 LLM-generated agent skills into 237 repos ([Aikido, 2026-02](https://www.aikido.dev/blog/slopsquatting-ai-package-hallucination-attacks)).
- **Slopsquatting mitigations**: (1) the **pre-install verification gate** for AI-proposed dependencies — existence, registry age, publisher identity, download history, checked **between** agent output and the package manager — is owned by [ai-ml-systems.md](ai-ml-systems.md) §4 and surfaced at merge through a **CI dependency-review gate** on the PR's dependency diff (for example [GitHub dependency review](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review) as a required check — the forcing function; the registry lookup itself is the evidence); for a solo developer the gate is a **registry lookup before install**, not a process. (2) **Lockfile discipline**: agents never regenerate a lockfile unless explicitly asked; install exactly from the committed lockfile (`npm ci`) and halt on divergence; dependency and lockfile diffs in **agent-authored PRs** MUST receive explicit human review ([../patterns/code-review-and-change-approval.md](../patterns/code-review-and-change-approval.md) §6). (3) **Curated registry allowlist or private proxy** so unknown names cannot resolve from the public registry, with install scripts disabled by default ([Nesbitt, 2026-04-09](https://nesbitt.io/2026/04/09/package-security-defenses-for-ai-agents.html)).
- **VEX (Vulnerability Exploitability eXchange)**: for SaaS or shrink-wrapped products with SBOMs, publish VEX documents to clarify which reported vulnerabilities are not reachable or not exploitable in your build configuration. CycloneDX supports VEX natively.
- **Vulnerability disclosure to users** — for **shrink-wrapped** or **SaaS** products, coordinate **customer** comms with [secure-development-lifecycle.md](secure-development-lifecycle.md) (responsive vulnerability handling) and legal/comms.

**Why:** Registry attacks and dependency confusion are **documented** incidents, not theoretical risks — and **slopsquatting** extends them to names no human ever typed: because models hallucinate the **same** plausible names repeatedly, attackers can harvest and pre-register them before a victim ever runs an install. VEX reduces noise from SBOM scanners and prevents unnecessary customer escalations for vulnerabilities in code paths that are never executed.

---

## 8. Models And Datasets As Dependencies

A third-party **model artifact** (weights, checkpoints, adapters, tokenizers) or **dataset** entering **production or estate-governed** use is a **dependency** and passes the same admission discipline as code — this section extends §1 (pinning), §3 (BOM evidence), and §5 (Sigstore signing) to ML artifacts. It applies to **any locally loaded third-party model**, including **embedding and reranker** models, not only fine-tuned or custom-trained weights ([ai-ml-systems.md](ai-ml-systems.md) §2 Tiers B–C).

- **Pin by digest.** Model and dataset artifacts MUST be pinned by **version and content digest** and resolved from a **declared source** — never a floating hub reference fetched at build or deploy time (§1 applied to ML artifacts).
- **Verify the publisher, not the popularity.** Admission rests on **verified publisher identity**; download counts, likes, and trending placement are attackable signals and MUST NOT serve as admission evidence.
- **Verify signatures where the publisher signs.** Where a publisher signs model artifacts, consumers MUST verify the signature **and its transparency-log entry** before first use, reusing the §5 keyless machinery (Fulcio identity, Rekor ledger) — not a parallel trust stack. The **OpenSSF Model Signing (OMS)** specification (v1; PKI-agnostic; signatures as **Sigstore bundles**) with the **model-signing v1.0** library/CLI (OpenSSF AI/ML Working Group, 2025-04-04) is the reference implementation. Estates SHOULD sign **internally produced** model artifacts under the same CI identity rules as §5.
- **Treat pickle-class deserialization as code execution.** Pickle-format checkpoints execute arbitrary code at load time (Hugging Face's own security documentation describes pickle loading as arbitrary code execution). Production model loading MUST use **non-executable weight formats** (**safetensors**-class: tensor data only, no deserialization hooks). Where a pickle-class artifact is unavoidable, loading MUST be gated: **sandboxed deserialization** (isolated, least-privilege, no-egress loader) plus a recorded, expiring **exception** ([../patterns/normative-language-applicability-and-exceptions.md](../patterns/normative-language-applicability-and-exceptions.md) §5). Restricted unpicklers (for example `torch.load` with `weights_only=True`, the PyTorch 2.6 default) are **defence-in-depth**, not a substitute for safe formats or sandboxing.
- **Scan on ingest — and treat scanners as evadable.** Model files SHOULD be scanned at admission (malware plus pickle-import scanning); hub-side scanning — for example Hugging Face's built-in ClamAV + pickle-import scan and integrated third-party scanners — satisfies this for hub-sourced artifacts but is **explicitly not foolproof** per the hub's own documentation. A green scan does NOT reclassify a pickle-class artifact as safe; the format and sandbox rules above still apply.
- **Inventory with AIBOM-class records.** Each production model SHOULD carry an **AIBOM-class record** — artifact identity and digest, publisher, licence, base-model lineage, training-data references — attached to the artifact like the §3 SBOM. Formats are **emerging**: **CycloneDX ML-BOM** (1.6+) and the **SPDX 3.0 AI and Dataset profiles** are the candidate standards; record the information now, and route any hard format mandate through an ADR when one standard settles.
- **Datasets: digests and provenance.** Training, fine-tuning, and evaluation datasets behind production models MUST be pinned by **digest** with **provenance/lineage** tracked per revision — a hash and a changelog, cheap and testable. Each revision SHOULD additionally be **cryptographically signed** by whoever made the change, per the joint CISA/NSA/FBI **AI Data Security** guidance (2025-05-22). **Corpus size is not a poisoning defence**: admission control is per-source provenance, not dilution.
- **Provenance framing.** SLSA v1.2 defines only **Build** and **Source** tracks — there is **no ratified AI/ML track**; applying Build-track provenance and attestations to model artifacts is community practice, cited as such, not a compliance claim.

**Ownership and lifecycle:** the owner of the consuming system owns model/dataset admission evidence. Estates that cannot yet meet the signing or safe-format bar use the bounded, expiring exception contract with compensating controls — not softened rule text. Review triggers: OMS spec revision, AIBOM format standardisation (CycloneDX/SPDX), or a ratified SLSA ML track.

**Why:** Model hubs distribute **executable** artifacts under popularity signals anyone can game; pickle deserialization RCE and tampered or poisoned artifacts are the failure modes this closes. Digest + publisher + signature + AIBOM evidence makes model admission answer the same question §5 answers for images: *built and published by whom, verified how?*

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
| Pre-install gate for AI-proposed packages | Slopsquats install **legitimately** — scoped names, registry precedence, and lockfile CI never fire; only a **pre-install** existence/provenance check discriminates, and it costs one registry lookup. |
| Explicit licence policy | Prevents **surprise** copyleft or attribution gaps in releases. |
| Provenance when required | **Attestations** answer “was this binary built from **this** source?” faster than manual forensics. |
| Published patch SLAs | Makes vulnerability response **measurable**; aligns with SSDF-style expectations. |
| SBOM + promotion loop | **AI-accelerated disclosure** means merge-time green is insufficient without **re-scan** at promote/deploy. |
| Models/datasets admitted like code (§8) | **Pickle-class deserialization is code execution** and hub scanning is evadable; digest + publisher + signature + AIBOM evidence extends the §1/§3/§5 machinery to ML artifacts instead of trusting popularity signals. |

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
- Spracklen et al. — **package hallucinations by code-generating LLMs** (USENIX Security 2025; 2024 model cohort): https://arxiv.org/abs/2406.10279
- Churilov — **2026 frontier-cohort replication** (cross-model-identical hallucinated names remain registrable): https://arxiv.org/abs/2605.17062
- The Register — hallucinated `huggingface-cli` **PyPI registration and downloads** (2024-03-28): https://www.theregister.com/2024/03/28/ai_bots_hallucinate_software_packages/
- Aikido — **slopsquatting incidents** (`react-codeshift`, malicious npm packages; 2026-02): https://www.aikido.dev/blog/slopsquatting-ai-package-hallucination-attacks
- Nesbitt — **package security defenses for AI agents** (2026-04-09): https://nesbitt.io/2026/04/09/package-security-defenses-for-ai-agents.html
- Socket — **slopsquatting** coverage (term coined by Seth Larson, PSF; 2025-04): https://socket.dev/blog/slopsquatting-how-ai-hallucinations-are-fueling-a-new-class-of-supply-chain-attacks
- GitHub — **dependency review** (PR dependency-diff gate): https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review
- OpenSSF **Model Signing v1.0** — AI/ML Working Group launch (Sigstore-based signing for ML models): https://openssf.org/blog/2025/04/04/launch-of-model-signing-v1-0-openssf-ai-ml-working-group-secures-the-machine-learning-supply-chain/
- OpenSSF **Model Signing (OMS) specification** (v1; Sigstore bundle format): https://github.com/ossf/model-signing-spec
- Hugging Face Hub — **Pickle scanning** (pickle as arbitrary code execution; safe formats incl. safetensors): https://huggingface.co/docs/hub/security-pickle
- PyTorch 2.6 — `torch.load` **weights_only=True** default: https://pytorch.org/blog/pytorch2-6/
- CycloneDX **ML-BOM** capability (model and dataset transparency): https://cyclonedx.org/capabilities/mlbom/
- SPDX 3.0 — **AI and Dataset profiles** (Linux Foundation announcement): https://www.linuxfoundation.org/press/spdx-3-revolutionizes-software-management-in-systems-with-enhanced-functionality-and-streamlined-use-cases
- **SLSA v1.2 tracks** (Build and Source; no AI/ML track): https://slsa.dev/spec/v1.2/tracks
- CISA/NSA/FBI — **AI Data Security** CSI (2025-05-22): https://media.defense.gov/2025/May/22/2003720601/-1/-1/0/CSI_AI_DATA_SECURITY.PDF
