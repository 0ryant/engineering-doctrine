# Dependencies And Supply Chain

Durable rules for **third-party code** in production: **pinning**, **updates**, **licensing**, and **evidence** (SBOM) aligned with security and compliance expectations. Admission of **AI-proposed** dependencies is gated pre-install per [ai-ml-systems.md](ai-ml-systems.md) §4, enforced here (§7). When a supplier, build service, support path, external model, or other dependency enters a declared contractual/regulatory boundary, [Revision-Pinned External Control Profiles](../patterns/revision-pinned-control-profiles.md) records the exact authority, baseline revision, scope, assessment evidence, flow-down obligations, and exceptions.

For the normal admission sequence, start with [Dependency Adoption](../impl/dependency-adoption.md).

---

## 1. Pinning And Lockfiles

- **Lock** dependency resolution for applications (`Cargo.lock`, `package-lock.json`, `poetry.lock`, etc.) and **commit** locks for reproducible builds.
- **Libraries** intended for consumption follow ecosystem norms (some ecosystems omit lockfiles for libs—document the rule per language).

**Why:** Reproducible builds and CI are impossible if two installs resolve different graphs.

---

## 2. Update Cadence And Automation

- **Automate** update PRs; do not rely on **ad-hoc** `npm update` before releases only. Updates that estate policy classifies as **low risk** MAY merge through a **documented bot-only path** ([collaboration.md](collaboration.md) §2) once **required checks** pass; other updates get **human review**. Agent-authored dependency and lockfile diffs keep the explicit human review in [code-review-and-change-approval.md](../patterns/code-review-and-change-approval.md) §6 ([ADR 0052](../../docs/adr/0052-close-owner-gaps-from-implementation-batch-2.md)).
- **Security patches** reach a patched release, or an approved compensating control, within an **SLA** appropriate to severity. **Example estate defaults** (adjust per sector, **CISA KEV** / regulatory duty, internet exposure, and compensating controls—publish **yours** in an estate or security doc; numbers below are **illustrative**, not universal law):

| Severity (typical CVSS-aligned) | Target time to **patched release** or **approved compensating control** |
| --- | --- |
| **Critical** (e.g. network RCE, trivial auth bypass, wormable) | **24 hours** |
| **High** | **7 calendar days** |
| **Medium** | **30 calendar days** or next **scheduled** maintenance window (whichever is sooner) |
| **Low** | Next **regular** dependency cadence (e.g. weekly/biweekly bot merge) |

- **Known-exploited and triage order** — when a component matches [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) (or your estate’s equivalent **weaponisation** feed), treat it as **highest** urgency regardless of “ordinary” severity tables; use [FIRST EPSS](https://www.first.org/epss/) and asset context to **rank** non-KEV backlog, not to **ignore** KEV.
- **Protocol dependencies with published lifecycles** — when a protocol adopted under [Revision-Pinned External Control Profiles](../patterns/revision-pinned-control-profiles.md) publishes a deprecation policy (for example **MCP**'s minimum **twelve-month** deprecation window — [2026-07-28 changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog)), treat announced deprecations as **update-cadence inputs**: schedule migration off deprecated features **inside** the publisher's window against the pinned revision in the profile record — not as an emergency when removal ships.

**Why:** Outdated dependencies are a **known** attack surface; automation reduces toil and inconsistency across repos. **Named SLAs** prevent “we’ll get to it” drift without pretending every CVE is equal.

---

## 3. SBOM Generation And Attachment

- **MUST (artefacts shipped to customers or other external parties, artefacts for regulated environments, and any artefact for which law, contract, or estate policy demands one):** produce a machine-readable **SBOM** (Software Bill of Materials) at build time and attach it to the artefact.
- **SHOULD (every other production artefact):** do the same, not only on request, so the questions "what was in this binary?" and "is this vulnerable component in production?" are answerable in seconds.
- **Format choice**: prefer **CycloneDX** (ECMA-424) for supply-chain depth (includes VEX, Cryptography BOM, AI/ML-BOM) or **SPDX** (ISO/IEC 5962:2021) where licence compliance is the primary driver. Either is acceptable; pick one per build pipeline and be consistent. The cryptographic inventory expectation that a cryptography BOM can serve is in [api-boundaries-and-security.md](api-boundaries-and-security.md) §2.2.
- **Minimum content — SHOULD:** meet the minimum-elements baseline active at adoption time ([merge-path-evidence-and-pipeline-integrity.md](merge-path-evidence-and-pipeline-integrity.md) invariant 6). Where no other baseline binds, use CISA's **2026 Minimum Elements for an SBOM** (2026-07-29), which replaces NTIA's 2021 list and adds, among others, component hash, licence, tool name and version, generation context, and SBOM author signature. Neither list makes vulnerability data a minimum element: keep exploitability and advisory data in the **VEX** and advisory records below, linked to the SBOM, not embedded in it.
- **When to generate**: per-build for customer-facing or regulated software; per-release minimum for internal-only tooling. Do not rely on post-hoc reconstruction from VCS.
- **Attachment**: for container images, attach the SBOM to the image digest as an **OCI attestation**, using the registry's supported mechanism; for standalone binaries and packages, publish an adjacent `.sbom.json` alongside the release artefact. Machine-readable JSON or XML only — plain-text SBOMs cannot be reliably parsed. Generation alone is insufficient for operations: each **immutable** artefact digest/version should retain an **SBOM** that can be **re-scanned** against **current** advisory feeds ([SPDX](https://spdx.dev/), [CycloneDX](https://cyclonedx.org/)—see [../REFERENCES.md](../REFERENCES.md)).
- **Continuous feed-backed re-evaluation** — on **promotion** or **deploy** to an environment, and when **material** feed updates land, re-check the **same** SBOM identity (**purl** / version / hash where available) against vulnerability intelligence; merge-time green does **not** authorise deploy after **new** disclosures unless policy explicitly allows a time-bounded exception ([merge-path-evidence-and-pipeline-integrity.md](merge-path-evidence-and-pipeline-integrity.md)).
- **Triage before promotion** — a releasable artefact with newly disclosed vulnerable components is **remediated**, **blocked**, or released only under an **explicit** risk acceptance with **owner**, **expiry**, and **compensating control** recorded next to the artefact evidence.
- **VEX / exploitability** — when a CVE appears in the SBOM but the shipped configuration is **not exploitable**, record disposition with **scope** (artefact version, environment) using a **VEX** document or equivalent **signed** attestation (for example CycloneDX [VEX](https://cyclonedx.org/capabilities/vex/)) so promotion evidence stays honest—**not** to replace scanning or future re-evaluation when code or reachability changes.
- **SCA** (dependency scanning) and **secret scanning** run on every merge path, and separately on a scheduled cadence to catch newly published vulnerabilities against already-merged code.

**Why:** EU Cyber Resilience Act, US Executive Order 14028, and enterprise procurement increasingly expect an **SBOM** as evidence, with triggers that differ by regime and buyer ([ADR 0053](../../docs/adr/0053-correct-slsa-attribution-and-settle-supply-chain-evidence.md)). SCA on the merge path alone misses vulnerabilities disclosed after merge, and **AI-accelerated disclosure** widens the gap between “we built once with a green scan” and “what is exposed **now**.”

---

## 4. SLSA: Build Provenance And Pipeline Integrity

- **SHOULD (artefacts shipped externally or to regulated environments):** target **SLSA Build L2** as the starting baseline: signed provenance generated by a hosted build platform. **Build L3** is the target for critical or customer-facing software. Build L1 (provenance that may be unsigned) is acceptable only for internal-only tooling.
- **MUST (where law, contract, or estate policy demands provenance):** it is a release input at the level demanded ([merge-path-evidence-and-pipeline-integrity.md](merge-path-evidence-and-pipeline-integrity.md) invariant 6).
- **SLSA v1.2 Build levels** (abbreviated from the specification). A level describes the build platform, so confirm which level the platform meets instead of assuming it:

  | Level | What the specification requires | Addresses |
  | --- | --- | --- |
  | **L1** | The producer follows a consistent build process; the platform generates provenance describing who built the artefact, how, and from which top-level inputs. Provenance may be incomplete or unsigned. | Mistakes; missing documentation |
  | **L2** | A hosted build platform generates and signs the provenance, and the consumer validates its authenticity. | Tampering after the build |
  | **L3** | A hardened platform: runs cannot influence one another (isolated, ephemeral environments; no cache poisoning), signing material is out of reach of user-defined build steps, and the platform's control plane generates or verifies every provenance field. | Tampering during the build |

- **What provenance shows.** Provenance records which builder, source, and parameters produced an artefact. It does not show that the code that ran in the build was the code the producer intended: a compromised workflow on the legitimate builder produces valid provenance. It protects only when a consumer verifies it against expectations.
- **SHOULD (consumers of provenance, at deploy or admission, and at dependency admission where a publisher provides it):** verify against **expectations**, not only that a valid attestation exists: the expected builder identity, the expected source repository, and the build type and parameters where the format carries them. A verification summary from a verifier the estate trusts MAY stand in for re-verifying each attestation.
- **Reproducible inputs** (library policy, not a SLSA requirement): pin toolchain versions, reference base images by digest (below), and build from committed lockfiles (§1), so the same commit resolves the same inputs.
- **Hermetic and reproducible builds — SHOULD, context-dependent:** where the threat model, a Build L3 target, or an active profile calls for it, builds run with declared inputs only (in the strong form, no network access during the build), and outputs are reproducible apart from documented nondeterminism. SLSA v1.2 requires neither at any Build level; this is an estate hardening target, not a level claim.
- **Base image pinning**: reference container base images by **digest** (`FROM golang:1.24.0@sha256:...`), not by mutable tag. Verify digest before pull in security-sensitive pipelines.
- **Build provenance attestation** (how the provenance rules above are met): use the build platform's own provenance mechanism, and confirm which Build level the platform documents for it. The attestation is attached to the artefact and answers "which commit, which pipeline, which runner produced this binary?" A provenance statement assembled and signed by a user-defined build step does not by itself meet Build L2, which requires the platform's control plane to generate it ([ADR 0058](../../docs/adr/0058-sharpen-four-rules-after-the-november-2026-review.md)).
- **Cache trust:** release and deploy builds restore only caches written at the same or higher trust ([build.md](build.md) §11).

**Why:** Supply-chain attacks increasingly target the build pipeline rather than the source code. Verified provenance makes tampering after the build **detectable**, and an isolated build platform makes tampering during the build hard. Neither vouches for the workflow's own code: in the May 2026 npm compromise analysed on the SLSA project blog, attacker code reached a release workflow through a poisoned cache and published packages with valid attestations ([ADR 0053](../../docs/adr/0053-correct-slsa-attribution-and-settle-supply-chain-evidence.md)). Evidence note: the verification and cache rules rest on the SLSA specification and one incident analysis from the same project.

---

## 5. Artifact Signing With Sigstore

- **SHOULD (container images and release binaries shipped externally or deployed to production):** sign them using **cosign** with keyless signing via OIDC. In a hosted CI environment (GitHub Actions, Azure DevOps with Workload Identity), no long-lived private key is required — the CI runtime obtains a short-lived certificate from **Fulcio**, signs the artefact, and records the signature in the **Rekor** transparency log.
- **SHOULD (where signatures are produced):** verify at deploy or admission against the Rekor ledger and the **identity and issuer** permitted to sign (e.g., only the `release` workflow in `org/repo` may sign production images). A check that accepts any valid signature says nothing about origin.
- **No long-lived signing keys in secret stores** for build pipelines that support OIDC. This is the secretless default of [zero-trust-and-workload-identity.md](zero-trust-and-workload-identity.md) §2 applied to signing, and the same default covers publishing to package registries that accept a federated publishing identity. Keyless flows remove the stored key and its rotation burden. They do not remove theft of the short-lived credential from a compromised job, which is why build isolation and cache trust (§4) still matter.
- Where keyless signing is not available (air-gapped or legacy environments), use **cosign** with a KMS-backed key and rotate per the estate's key-rotation policy.

**Why:** Signature verification closes the gap between "we fetched this image from our registry" and "this image was signed by our authorised CI pipeline identity". It does not show that only intended code ran in that pipeline (§4).

---

## 6. Licensing

- Maintain an **allowlist** or policy for **OSS licences** in distributed software; generate **NOTICE** / attribution files where required.

**Why:** Licence violations are **legal** risk; copying code without licence clarity is not acceptable at scale.

---

## 7. Registry Hygiene, Dependency Confusion, Slopsquatting, And Disclosure

- **Scoped package names** for internal libraries where the ecosystem supports them (e.g. `@org/my-lib` for npm). Scoped names prevent dependency confusion attacks where an attacker publishes a package with the same unscoped name to a public registry.
- **Private registry precedence**: configure package managers to resolve internal packages from the private registry **first**, and validate lockfile integrity in CI (`npm ci`, `poetry check --lock`, `go mod verify`). A regenerated lockfile that differs from the committed one is a build failure.
- **Slopsquatting is distinct from dependency confusion — and the controls above do not stop it.** An LLM or agent invents a **plausible but non-existent** package name; an attacker registers that name on the public registry; installation then **succeeds legitimately**. There is no internal name to scope, nothing for private-registry precedence to shadow, and the resulting **lockfile is internally consistent**, so lockfile-integrity CI passes. Repeatable invented names can be pre-registered by attackers. The [dated evidence record](../evolution/research-v060-source-maintenance-2026-09.md#m16-package-hallucination-evidence-placement) carries the study cohorts, reported rates and separate incident narration behind this risk statement.
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
| SLSA Build L2 as starting target | Achievable on hosted build platforms; L3 needs a platform that isolates builds and keeps signing material out of build steps. Hermetic builds are a separate hardening target that SLSA v1.2 does not require ([ADR 0053](../../docs/adr/0053-correct-slsa-attribution-and-settle-supply-chain-evidence.md)). |
| Keyless cosign (OIDC + Rekor) | Eliminates long-lived signing key management; transparency log adds public accountability. |
| Scoped package names + lockfile CI | Prevents dependency confusion attacks at zero cost; `npm ci` / `poetry check --lock` enforce integrity. |
| Pre-install gate for AI-proposed packages | Slopsquats install **legitimately** — scoped names, registry precedence, and lockfile CI never fire; only a **pre-install** existence/provenance check discriminates, and it costs one registry lookup. |
| Explicit licence policy | Prevents **surprise** copyleft or attribution gaps in releases. |
| Provenance verified against expectations | **Attestations** record which builder and source produced an artefact. They protect only when a consumer checks them against the expected builder and source, and they do not vouch for code that ran inside a compromised workflow ([ADR 0053](../../docs/adr/0053-correct-slsa-attribution-and-settle-supply-chain-evidence.md)). |
| Published patch SLAs | Makes vulnerability response **measurable**; aligns with SSDF-style expectations. |
| SBOM + promotion loop | **AI-accelerated disclosure** means merge-time green is insufficient without **re-scan** at promote/deploy. |
| Models/datasets admitted like code (§8) | **Pickle-class deserialization is code execution** and hub scanning is evadable; digest + publisher + signature + AIBOM evidence extends the §1/§3/§5 machinery to ML artifacts instead of trusting popularity signals. |
| Documented bot-only path for low-risk updates | Reviewing every trivial bump builds update backlogs; unpolicied auto-merge removes the check. An estate-defined low-risk class, gated by required checks, matches collaboration §2 and this file's own cadence row ([ADR 0052](../../docs/adr/0052-close-owner-gaps-from-implementation-batch-2.md)). |
| SBOM, provenance, and signing typed on one trigger set | An SBOM is required where artefacts leave the estate, enter regulated environments, or are demanded by law, contract, or policy, and recommended elsewhere. Provenance and signing are recommended for the same artefacts; provenance is required where demanded. One trigger set replaces the four previously in use ([ADR 0053](../../docs/adr/0053-correct-slsa-attribution-and-settle-supply-chain-evidence.md)). |

---

## References

- OWASP **Dependency-Check** / SCA concept (industry framing): https://owasp.org/www-project-dependency-check/
- SPDX — **Software Bill of Materials** specification: https://spdx.dev/
- CISA — **2026 Minimum Elements for a Software Bill of Materials (SBOM)** (S2; 2026-07-29; replaces the 2021 NTIA list; accessed 2026-11-18): https://www.cisa.gov/resources-tools/resources/2026-minimum-elements-software-bill-materials-sbom
- NTIA — *The Minimum Elements For a Software Bill of Materials (SBOM)* (2021-07-12; historical baseline): https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom
- White House **Executive Order 14028** (secure software supply chain): https://www.federalregister.gov/documents/2021/05/17/2021-10460/improving-the-nations-cybersecurity
- **SLSA** — Supply-chain Levels for Software Artifacts: https://slsa.dev/
- **SLSA** Getting Started guide: https://slsa.dev/get-started
- **Sigstore** — keyless signing and transparency: https://www.sigstore.dev/
- **CycloneDX** — SBOM and VEX standard: https://cyclonedx.org/
- EU **Cyber Resilience Act** (CRA) — SBOM and vulnerability disclosure obligations: https://eur-lex.europa.eu/eli/reg/2024/2847/oj
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
- Renovate — **automerge** (waits for required checks; recommended for updates you would merge anyway; lockfile maintenance and dev dependencies as lowest risk) (S5, product-scoped, accessed 2026-11-18): https://docs.renovatebot.com/key-concepts/automerge/  
- **SLSA v1.2 Build track** — levels and build requirements (S4; status Approved; accessed 2026-11-18): https://slsa.dev/spec/v1.2/build-track-basics and https://slsa.dev/spec/v1.2/build-requirements  
- **SLSA v1.2** — verifying artifacts and threats (S4; accessed 2026-11-18): https://slsa.dev/spec/v1.2/verifying-artifacts and https://slsa.dev/spec/v1.2/threats  
- SLSA blog — **Mini Shai-Hulud: Where SLSA's Boundaries Fall** (S6, named practitioner; 2026-05-15; secondary for the incident; accessed 2026-11-18): https://slsa.dev/blog/2026/05/mini-shai-hulud-what-slsa-can-and-cannot-do  
- Sigstore — **cosign 2.0** (identity and issuer required at verification) (S5, product-scoped; 2023-02-23; accessed 2026-11-18): https://blog.sigstore.dev/cosign-2-0-released/  
- npm — **trusted publishing** (short-lived workflow identity instead of a long-lived token) (S5, product-scoped; accessed 2026-11-18): https://docs.npmjs.com/trusted-publishers/  
