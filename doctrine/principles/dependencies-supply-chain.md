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
- **Security patches** merge on an **SLA** appropriate to severity. **Example estate defaults** (adjust per sector, **CISA KEV** / regulatory duty, internet exposure, and compensating controls—publish **yours** in an estate or security doc; numbers below are **illustrative**, not universal law):

| Severity (typical CVSS-aligned) | Target time to **patched release** or **approved compensating control** |
| --- | --- |
| **Critical** (e.g. network RCE, trivial auth bypass, wormable) | **24 hours** |
| **High** | **7 calendar days** |
| **Medium** | **30 calendar days** or next **scheduled** maintenance window (whichever is sooner) |
| **Low** | Next **regular** dependency cadence (e.g. weekly/biweekly bot merge) |

- **Known-exploited and triage order** — when a component matches [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) (or your estate’s equivalent **weaponisation** feed), treat it as **highest** urgency regardless of “ordinary” severity tables; use [FIRST EPSS](https://www.first.org/epss/user-guide) and asset context to **rank** non-KEV backlog, not to **ignore** KEV.

**Why:** Outdated dependencies are a **known** attack surface; automation reduces toil and inconsistency across repos. **Named SLAs** prevent “we’ll get to it” drift without pretending every CVE is equal.

---

## 3. SBOM And Scanning

- Produce **SBOMs** for shipped artefacts where the organisation or regulators expect them. **Generation alone is insufficient** for operations: each **immutable** artefact digest/version should retain an **SBOM** that can be **re-scanned** against **current** advisory feeds ([SPDX](https://spdx.dev/), [CycloneDX](https://cyclonedx.org/)—see [REFERENCES.md](REFERENCES.md)).
- **Continuous feed-backed re-evaluation** — on **promotion** or **deploy** to an environment, and when **material** feed updates land, re-check the **same** SBOM identity (**purl** / version / hash where available) against vulnerability intelligence; merge-time green does **not** authorise deploy after **new** disclosures unless policy explicitly allows a time-bounded exception ([merge-path-evidence-and-pipeline-integrity.md](merge-path-evidence-and-pipeline-integrity.md)).
- **Triage before promotion** — a releasable artefact with newly disclosed vulnerable components is **remediated**, **blocked**, or released only under an **explicit** risk acceptance with **owner**, **expiry**, and **compensating control** recorded next to the artefact evidence.
- **VEX / exploitability** — when a CVE appears in the SBOM but the shipped configuration is **not exploitable**, record disposition with **scope** (artefact version, environment) using a **VEX** document or equivalent **signed** attestation (for example CycloneDX [VEX](https://cyclonedx.org/capabilities/vex/)) so promotion evidence stays honest—**not** to replace scanning or future re-evaluation when code or reachability changes.
- **SCA** (dependency scanning) and **secret scanning** run on the merge path (already aligned with build principles).

**Why:** Executive Order 14028 (US) and sector norms increasingly expect **SBOM** evidence for critical software; even without regulation, SCA is table stakes. **AI-accelerated disclosure** widens the gap between “we built once with a green scan” and “what is exposed **now**.”

---

## 4. Licensing

- Maintain an **allowlist** or policy for **OSS licences** in distributed software; generate **NOTICE** / attribution files where required.

**Why:** Licence violations are **legal** risk; copying code without licence clarity is not acceptable at scale.

---

## 5. Provenance, Registry Hygiene, And Disclosure

- **Build provenance** — where customers or regulators expect **tamper-evident** delivery, emit **SLSA**-style attestations or equivalent **signed** build metadata; aligns with [build.md](build.md) §14.
- **Package registry hygiene** — use **scoped** names where ecosystems support them; watch for **typosquatting** and **dependency confusion** (publishing internal-looking package names on public registries).
- **Vulnerability disclosure to users** — for **shrink-wrapped** or **SaaS** products, coordinate **customer** comms with [secure-development-lifecycle.md](secure-development-lifecycle.md) (responsive vulnerability handling) and legal/comms.

**Why:** **SLSA** and EO **14028** norms treat **provenance** as evidence; registry attacks are **documented** supply-chain incidents; silent CVEs erode trust.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Automation + review | Balances **velocity** with **governance**; blocks neither security nor shipping. |
| SBOM where shipping | Makes incidents and audits **factual** (“what was in build X?”). |
| Explicit licence policy | Prevents **surprise** copyleft or attribution gaps in releases. |
| Provenance when required | **Attestations** answer “was this binary built from **this** source?” faster than manual forensics. |
| Published patch SLAs | Makes **RV** (respond) work **measurable**; aligns with SSDF-style expectations. |
| SBOM + promotion loop | **AI-accelerated disclosure** means merge-time green is insufficient without **re-scan** at promote/deploy. |

---

## References

- OWASP **Dependency-Check** / SCA concept (industry framing): https://owasp.org/www-project-dependency-check/  
- SPDX — **Software Bill of Materials** specification: https://spdx.dev/  
- NTIA / CISA **SBOM** minimum elements (US guidance): https://www.ntia.gov/SBOM  
- White House **Executive Order 14028** (secure software supply chain) — high-level driver for SBOM adoption in US federal context.  
- **SLSA** — Supply-chain Levels for Software Artifacts: https://slsa.dev/  
- OpenSSF **Supply-chain attacks** (awareness): https://openssf.org/  
