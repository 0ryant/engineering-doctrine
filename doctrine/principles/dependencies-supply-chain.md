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
- **Security patches** merge on an **SLA** appropriate to severity.

**Why:** Outdated dependencies are a **known** attack surface; automation reduces toil and inconsistency across repos.

---

## 3. SBOM And Scanning

- Produce **SBOMs** for shipped artefacts where the organisation or regulators expect them.
- **SCA** (dependency scanning) and **secret scanning** run on the merge path (already aligned with build principles).

**Why:** Executive Order 14028 (US) and sector norms increasingly expect **SBOM** evidence for critical software; even without regulation, SCA is table stakes.

---

## 4. Licensing

- Maintain an **allowlist** or policy for **OSS licences** in distributed software; generate **NOTICE** / attribution files where required.

**Why:** Licence violations are **legal** risk; copying code without licence clarity is not acceptable at scale.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Automation + review | Balances **velocity** with **governance**; blocks neither security nor shipping. |
| SBOM where shipping | Makes incidents and audits **factual** (“what was in build X?”). |
| Explicit licence policy | Prevents **surprise** copyleft or attribution gaps in releases. |

---

## References

- OWASP **Dependency-Check** / SCA concept (industry framing): https://owasp.org/www-project-dependency-check/  
- SPDX — **Software Bill of Materials** specification: https://spdx.dev/  
- NTIA / CISA **SBOM** minimum elements (US guidance): https://www.ntia.gov/SBOM  
- White House **Executive Order 14028** (secure software supply chain) — high-level driver for SBOM adoption in US federal context.  
