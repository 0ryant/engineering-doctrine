# Merge Path Evidence And Pipeline Integrity

**Portable intent:** The **default-branch merge path** is a **controlled channel** for changing software. **Automation definitions** that execute that path (workflows, job graphs, deployment hooks) are **security-relevant artefacts**, not ancillary text. **Evidence** produced on the path—tests, scan results, bills of materials, attestations—must be **authenticable**, **retrievable**, and **scoped** so organisations can **prove** what was checked before code became authoritative.

This principle **adds** merge-path and pipeline-specific invariants. It does **not** restate general build-surface vocabulary or dependency-licence policy; those remain separate topics so each file stays auditable on its own.

---

## 1. Definitions (Normative For This File)

| Term | Meaning here |
| --- | --- |
| **Merge path** | The sequence of human and automated steps after which commits are eligible to become the **protected baseline** for a repository (e.g. default branch, release train). |
| **Pipeline definition** | Machine-readable automation that runs on behalf of the repo: CI job graphs, release workflows, packaging hooks, and **third-party** steps they invoke. |
| **Evidence** | Durable outputs that demonstrate which checks ran and what they concluded: logs under retention policy, published test reports, SARIF or equivalent, SBOM files, signed attestations, checksum manifests. |
| **Gate** | An automated check configured so that **policy violations prevent** the merge path from completing successfully for the protected baseline. |

---

## 2. Invariants

1. **Non-bypassable gates for agreed scope** — Every automated control claimed as a **merge requirement** for the protected baseline must be **enforced** by platform configuration (protected branches, required contexts, equivalent server-side rules). Local-only scripts do not satisfy merge enforcement.

2. **Pipeline definitions in scope** — Pipeline definitions that can **read secrets**, **mutate production**, **publish packages**, or **alter downstream** systems are **in the same trust class** as application code for review and static analysis. “Application-only” threat models are incomplete when automation holds privileges.

3. **Binding outcomes, not advisory logs** — A tool step that **always succeeds** while emitting warnings is **telemetry**, not a **gate**. If policy requires a finding class to block merge, the automation must **fail the merge path** on violation.

4. **Evidence accompanies authority** — Where automation is granted **write** or **deploy** authority, retain (or stream to an organisation-controlled store) enough **evidence** to answer: *which revision*, *which workflow identity*, *which artefacts*, *which human approvals* (if any), and *which policy version* applied.

5. **Reproducible resolution where practicable** — For **application** deliverables, dependency resolution should be **locked** or otherwise **reproducible** so SBOMs and vuln analyses refer to a **stable graph** (ecosystem norms for libraries may differ—publish the estate rule).

6. **Transparency artefacts when stakeholders require them** — When law, contract, sector norm, or enterprise policy demands **SBOMs**, **VEX**, or **build provenance**, those artefacts are **release inputs**, not post-hoc narratives. Minimum content should follow recognised community or regulator specifications active at adoption time.

7. **Time-bounded exceptions** — Risk acceptances for failing gates carry **owners**, **expiry**, and **compensating controls**. Silent indefinite waivers are treated as **control failure**.

---

## 3. Rationale (Why These Invariants)

| Invariant | Rationale |
| --- | --- |
| 1 | Server-side enforcement is what auditors and incident responders can rely on; developer laptops are not a system of record. |
| 2 | Field incidents show **CI/CD graphs** and **privileged tokens** are abused as often as application bugs; NIST SSDF **PS** explicitly addresses protecting development pipelines. |
| 3 | “Green” builds that never fail train organisations to ignore signal; OWASP CI/CD risk work stresses **flow control** and **integrity** of pipelines. |
| 4 | Without evidence, post-incident questions (“was this binary ever scanned?”) cannot be answered factually—contradicts **zero trust** verification expectations. |
| 5 | Unpinned graphs make SBOMs and incident response **non-repeatable**. |
| 6 | Regulators and large buyers increasingly expect **machine-readable** transparency; US federal guidance on SBOM elements has **moved forward** independently of any single vendor stack. |
| 7 | Governance without expiry becomes **organisational debt** and violates enterprise risk management norms (see CSF **Govern** and supply-chain categories). |

---

## 4. Relationship To Other Doctrine Files

Other files in this library address **build surfaces**, **semantic versioning**, **collaboration mechanics**, and **dependency policy** in general terms. **This** file is the **canonical** place for: **merge path as controlled channel**, **pipeline definitions as security artefacts**, **binding gates vs advisory tools**, and **evidence** expectations tied to automation authority. If another file conflicts on merge-path specifics, **this file wins** until harmonised by an explicit edit.

---

## References (External — Primary Evidence)

- NIST **SP 800-218**, *Secure Software Development Framework (SSDF) Version 1.1* — practice groups **Prepare, Protect, Produce, Respond**; **PS** covers protecting development environments and tooling: https://csrc.nist.gov/publications/detail/sp/800-218/final  
- NIST **Cybersecurity Framework 2.0** (CSF 2.0), NIST **CSWP 29** — **Govern (GV)** function; **GV.SC** (*Cybersecurity Supply Chain Risk Management*) outcomes for programme-level supply-chain governance: https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final  
- NIST news release on **CSF 2.0** (governance and supply-chain emphasis): https://www.nist.gov/news-events/news/2024/02/nist-releases-version-20-landmark-cybersecurity-framework  
- NIST **IR 8179** — *Criticality Analysis Process Model: Prioritizing Systems and Components* (tailoring assurance to mission-critical assets): https://csrc.nist.gov/pubs/ir/8179/final  
- **SLSA** — Supply-chain Levels for Software Artifacts; **Build** track and **provenance** predicate (verify **how** artefacts were produced): https://slsa.dev/spec/v1.2/  
- **in-toto** attestations framework (provenance attestation pattern): https://in-toto.io/  
- **SPDX** — Software Package Data Exchange (SBOM format family): https://spdx.dev/  
- **CycloneDX** — OWASP bill of materials standard: https://cyclonedx.org/  
- **CISA** — Software Bill of Materials (SBOM) programme hub: https://www.cisa.gov/sbom  
- **CISA** — *2025 Minimum Elements for a Software Bill of Materials (SBOM)* (draft; superseding narrative for NTIA 2021 minimum elements—verify **current** published status on CISA site): https://www.cisa.gov/resources-tools/resources/2025-minimum-elements-software-bill-materials-sbom  
- **CISA** & partners — *A Shared Vision of Software Bill of Materials (SBOM) for Cybersecurity* (joint guidance PDF on cisa.gov): https://www.cisa.gov/sites/default/files/2025-09/joint-guidance-a-shared-vision-of-software-bill-of-materials-for-cybersecurity_508c.pdf  
- The White House — **Executive Order 14028** (May 12, 2021) — *Improving the Nation’s Cybersecurity* (historical driver for SBOM and secure development practices in US federal procurement context): https://www.federalregister.gov/documents/2021/05/17/2021-10460/improving-the-nations-cybersecurity  
- OMB / The White House — **M-26-05**, *Adopting a Risk-based Approach to Software and Hardware Security* (Jan. 23, 2026; rescinds M-22-18 / M-23-16; **agency discretion** on attestations/SBOM while still pointing agencies to NIST SP 800-218 and CISA SBOM materials): https://www.whitehouse.gov/wp-content/uploads/2026/01/M-26-05-Adopting-a-Risk-based-Approach-to-Software-and-Hardware-Security.pdf  
- OWASP — **Top 10 CI/CD Security Risks** project: https://owasp.org/www-project-top-10-ci-cd-security-risks/  
- **Filippo Valsorda** — *A Retrospective Survey of 2024/2025 Open Source Supply Chain Compromises* (field pattern analysis): https://words.filippo.io/compromise-survey/  
- **OpenSSF** — supply-chain security initiative (community coordination): https://openssf.org/  
- **FIRST** — Coordinated Vulnerability Disclosure: https://www.first.org/global/sigs/vulnerability-coordination  

---

*Introduced: 2026-04-26. Review at least annually or after major US federal software policy or CSF publication updates.*
