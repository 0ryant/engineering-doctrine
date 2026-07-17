# Engineering Controls Governance Program

**What this is:** A **pattern** for how an organisation **runs** engineering security controls across repositories—not the contents of a single `quality.yml`, but the **programme**: ownership, policy, exceptions, measurement, and **audit consumability**. Use it when standing up or maturing **merge-path**, **supply-chain**, and **pipeline-integrity** capabilities at scale.

**Companion principle:** [merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md) states **what** must be true on the merge path. **This** file states **how organisations govern** those controls over time.

---

## 1. Problem Statement

Without a programme, teams accumulate **inconsistent** gates, **stale** waivers, **unowned** scanners, and **evidence** scattered across vendor UIs. Auditors and customers then receive **screenshots** instead of **correlated records**. NIST **CSF 2.0** explicitly elevates **Govern** and **cybersecurity supply chain risk management (GV.SC)** as first-class outcomes—programme design is not optional for enterprises claiming mature posture.

---

## 2. Programme Components

| Component | Outcome |
| --- | --- |
| **Policy baseline** | Written criteria: which repos require which **control classes** (secret detection, SCA, pipeline static analysis, SBOM, provenance) keyed off **criticality** or **data class**—not flat one-size-fits-all unless deliberately chosen. |
| **Ownership** | Named **control owners** (role + escalation path) for each control class; deputy for absence. |
| **Inventory** | Register of **protected branches**, **required checks**, and **release** workflows per business-critical repo; reconciled quarterly or on material org change. |
| **Exception process** | Risk acceptance records: **scope**, **justification**, **expiry**, **compensating control**, **approver**; stored in ticket or governance tool with **stable IDs** referenced in-repo. |
| **Calibration** | Periodic proof that controls **detect** what they claim (golden files, test PRs, tabletop on simulated compromise). |
| **Evidence routing** | Logs, SARIF, SBOMs, attestations land in **organisation-controlled** retention (SIEM, artefact registry, GRC)—not only ephemeral CI UI. |
| **Metrics** | Leading indicators: % repos with enforced gates, mean time to remediate **critical** dependency findings, waiver age distribution, pipeline-definition review coverage. |
| **Supplier alignment** | For acquired or contracted software, **GV.SC**-style requirements in agreements (NIST CSF 2.0 **GV.SC-05** articulates contract integration of cybersecurity supply-chain requirements). |
| **External control profiles** | Register the source of applicability, exact baseline revision/update, system/data boundary, organisation-defined parameters or tailoring, assessment method, evidence owners, exceptions, and migration state. CUI example: [revision-pinned-control-profiles.md](revision-pinned-control-profiles.md). |

---

## 3. Cadence (Example Defaults)

Adjust per sector and regulator. Example **enterprise** cadences:

| Activity | Default cadence |
| --- | --- |
| Inventory vs protected-branch reality | **Quarterly** |
| Waiver / risk-acceptance review | **Monthly** sampling; **all** expiring items within 30 days of expiry |
| Control calibration (golden tests) | **Semiannual** minimum; **after** major CI provider or scanner upgrade |
| Policy text vs NIST / sector baseline diff | **Annual**; **ad hoc** on US OMB or EU regulatory shifts affecting your estate |
| External-profile applicability, revision, parameter, and boundary review | **On contract/authority change**, material architecture or supplier change, publication update, incident, and at the estate's documented periodic cadence |

---

## 4. Audit And Assurance Consumption

Prepare **audit packs** as **links + hashes**, not narrative only:

- Policy version ID and effective date  
- Export or query proving **required checks** on default branch for sampled repos  
- Sample of last **N** merges with associated evidence bundle references  
- Exception register extract (active + expired in period)  
- Evidence that **pipeline definitions** for high-privilege workflows underwent **peer review** (sampled PRs)
- For external profiles: authority source, exact revision/update, parameter/tailoring decisions, scoped boundary, requirement-to-evidence map, assessment depth/coverage, open findings, and accepted migration state

This mirrors **CSF 2.0** intent: governance outcomes are **demonstrable**, not asserted.

---

## 5. Anti-Patterns

| Anti-pattern | Why it fails |
| --- | --- |
| “We have a scanner” without **enforcement** | Violates **binding gate** invariant in [merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md). |
| Per-repo snowflake with **no** inventory | Cannot measure or improve; breaks **Identify** outcomes in CSF. |
| Waivers only in chat | No **system of record**; fails enterprise risk management traceability. |
| Evidence only in CI vendor UI beyond retention | Incident response and litigation hold cannot reconstruct history. |
| “NIST compliant” with no authority, revision, boundary, or assessment method | Blends catalogues and cannot show which obligation or system the evidence covers. |

---

## References (External)

- NIST **CSF 2.0** (CSWP 29) — **Govern (GV)** function; **GV.SC** Cybersecurity Supply Chain Risk Management category: https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final  
- NIST **SP 1305** — *CSF 2.0 and Cybersecurity Supply Chain Risk Management* (guidance tying CSF to C-SCRM practice): https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1305.pdf  
- NIST **SP 800-218** — SSDF (development and pipeline **protection** practices): https://csrc.nist.gov/publications/detail/sp/800-218/final  
- ISO/IEC **27001:2022** — Annex A controls include **organisational** roles, supplier relationships, and improvement (use official ISO catalogue for control text; this pattern maps conceptually, not normatively).  
- The White House / OMB — **M-26-05** (Jan. 2026) — federal **risk-based** software/hardware assurance; cites NIST SP 800-218 and CISA SBOM materials as **optional** references for agencies: https://www.whitehouse.gov/wp-content/uploads/2026/01/M-26-05-Adopting-a-Risk-based-Approach-to-Software-and-Hardware-Security.pdf  
- **COSO** — *Internal Control — Integrated Framework* (2013) — internal control components (control environment, monitoring activities) as **enterprise** analogue for control lifecycle: https://www.coso.org/Pages/ic-integrated-framework.aspx  

---

*Introduced: 2026-04-26.*
