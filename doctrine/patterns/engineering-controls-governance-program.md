# Engineering Controls Governance Program

**What this is:** A **pattern** for how an organisation **runs** engineering security controls across repositories—not the contents of a single `quality.yml`, but the **programme**: ownership, policy, exceptions, measurement, and **audit consumability**. Use it when standing up or maturing **merge-path**, **supply-chain**, and **pipeline-integrity** capabilities at scale.

**Companion principle:** [merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md) states **what** must be true on the merge path. **This** file states **how organisations govern** those controls over time.

---

## 1. Problem Statement

Without a programme, teams accumulate **inconsistent** gates, **stale** waivers, **unowned** scanners, and **evidence** scattered across vendor UIs. Auditors and customers then receive **screenshots** instead of **correlated records**. NIST **CSF 2.0** elevates **Govern** and cybersecurity supply-chain risk management (**GV.SC**) as first-class outcomes. An organisation claiming consistent controls across a material estate therefore needs an owned governance mechanism, but its record depth and cadence remain proportional to risk, authority, and operating cost.

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
| **Metrics** | Coverage and activity indicators paired with detection, escaped-failure, recovery, and operating-cost evidence; a gate count is not a risk-reduction outcome. |
| **Supplier alignment** | For acquired or contracted software, **GV.SC**-style requirements in agreements (NIST CSF 2.0 **GV.SC-05** articulates contract integration of cybersecurity supply-chain requirements). |
| **External control profiles** | Register the source of applicability, exact baseline revision/update, system/data boundary, organisation-defined parameters or tailoring, assessment method, evidence owners, exceptions, and migration state. CUI example: [revision-pinned-control-profiles.md](revision-pinned-control-profiles.md). |

---

## 2.1 Proportionate Control Lifecycle

Use a lifecycle record for a **material control**: a binding gate, a control with elevated authority or non-trivial adoption/operating cost, an externally required control, or a control generating repeated failures, exceptions, or delivery friction. A low-materiality check may inherit a class-level record; do not create a governance ticket for every lint rule or repository setting. Apply the claim and exception semantics in [Normative Language, Applicability, And Exceptions](normative-language-applicability-and-exceptions.md).

### Minimum Material-Control Record

| Field | Requirement |
| --- | --- |
| **Control and scope** | Stable identity; affected repositories, systems, data, change classes, or external profile; activation condition. |
| **Failure addressed** | Concrete failure or risk scenario and the consequence the control is intended to reduce. “Best practice” alone is insufficient. |
| **Authority and owner** | Accountable owner; policy, contract, regulation, or risk decision that authorises the control; escalation path. |
| **Expected evidence** | Evidence that the control operated on the intended surface and a negative or calibration case showing that it can detect or block the claimed failure. |
| **Effectiveness measure** | Detection/escape, incident, bypass, false-result, recovery, or other outcome signal, with material limitations. Activity volume is not proof of effectiveness. |
| **Cost and side effects** | Adoption work, compute/licence cost where material, review latency, human attention, false positives, availability impact, and behaviour the control may distort. |
| **Review trigger** | Risk/profile cadence plus events such as an incident, material architecture or supplier change, authority revision, persistent false results, or cost beyond the accepted range. |
| **Simplify or retire condition** | Evidence and authority needed to tune, consolidate, replace, or remove the control without losing the underlying risk outcome or external obligation. |

The record may be a policy catalogue entry, control-profile row, ADR, or other durable system of record. Reuse existing governance data rather than duplicating it in every repository.

### Review Decisions

| Decision | Required disposition |
| --- | --- |
| **Retain** | Evidence supports the risk reduction and cost remains proportionate; record the next trigger or cadence. |
| **Tune** | Keep the outcome and authority while changing scope, threshold, implementation, or evidence to improve discrimination or cost. |
| **Replace or consolidate** | Demonstrate that the successor covers the same failure and applicable authority; migrate policy, evidence routing, and consumers before withdrawing the predecessor. |
| **Retire** | Accountable authority accepts evidence that the failure no longer applies or is covered elsewhere; remove enforcement and stale access while retaining the historical decision and required evidence. |

A failed or inconclusive result remains failed or inconclusive. An exception is a separate, scoped, expiring authority decision; neither an exception nor a retirement decision rewrites technical evidence. A control required by law, contract, regulation, or an adopted external profile cannot be retired solely because local activity or cost looks unfavourable: the governing authority must cease to apply or accept an evidenced alternative.

### Worked Calibration Examples

| Existing control | Failure, evidence, and cost | Review outcome |
| --- | --- | --- |
| **Secret detection on a protected merge path** | Addresses credentials entering version control. Evidence includes a harmless canary/negative test, binding-gate receipts, sampled false results, and escaped-secret incidents. Cost includes latency and investigation of false positives. | **Retain or tune:** preserve blocking coverage for material paths; improve patterns, allow safe test fixtures through reviewed rules, or scope depth by change class when evidence shows noise without weakening detection. |
| **Duplicate repository-local scanner beside an equivalent centrally enforced gate** | Both instances address the same prohibited change and emit overlapping findings. Evidence shows the central gate is bound to the exact candidate, blocks a negative test, covers the repository inventory, and retains results. The local duplicate adds latency and triage work without detecting a distinct failure. | **Consolidate and retire the duplicate instance:** keep the evidence obligation and calibration at the central gate, migrate any unique rule first, update required-check policy, and preserve the retirement decision. |

**Why:** NIST SP 1303 describes a Monitor–Evaluate–Adjust cycle that checks whether controls remain implemented and effective, whether they impair operations and efficiency, and whether they achieve the desired risk result. The lifecycle above generalises that discipline without making a NIST control catalogue universally binding.

---

## 3. Cadence (Example Defaults)

Adjust per sector and regulator. Example **enterprise** cadences:

| Activity | Default cadence |
| --- | --- |
| Inventory vs protected-branch reality | **Quarterly** |
| Waiver / risk-acceptance review | **Monthly** sampling; **all** expiring items within 30 days of expiry |
| Control calibration (golden tests) | At the risk/profile-defined cadence; **after** major implementation changes, relevant incidents, or evidence that discrimination has degraded |
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
| Counting checks, scans, or findings as the outcome | Measures control activity while hiding escaped failures, false results, delay, cost, and behavioural distortion. |
| Permanent control with no review or removal condition | Lets obsolete or duplicate controls accumulate after their risk, authority, or implementation has changed. |

---

## References (External)

- NIST **CSF 2.0** (CSWP 29) — **Govern (GV)** function; **GV.SC** Cybersecurity Supply Chain Risk Management category: https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final  
- NIST **SP 1305** — *CSF 2.0 and Cybersecurity Supply Chain Risk Management* (guidance tying CSF to C-SCRM practice): https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1305.pdf  
- NIST **SP 800-218** — SSDF (development and pipeline **protection** practices): https://csrc.nist.gov/publications/detail/sp/800-218/final  
- NIST **SP 1303** — CSF 2.0 Enterprise Risk Management Quick-Start Guide, including the Monitor–Evaluate–Adjust cycle for control effectiveness and efficiency: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1303.pdf
- ISO/IEC **27001:2022** — Annex A controls include **organisational** roles, supplier relationships, and improvement (use official ISO catalogue for control text; this pattern maps conceptually, not normatively).  
- The White House / OMB — **M-26-05** (Jan. 2026) — federal **risk-based** software/hardware assurance; cites NIST SP 800-218 and CISA SBOM materials as **optional** references for agencies: https://www.whitehouse.gov/wp-content/uploads/2026/01/M-26-05-Adopting-a-Risk-based-Approach-to-Software-and-Hardware-Security.pdf  
- **COSO** — *Internal Control — Integrated Framework* (2013) — internal control components (control environment, monitoring activities) as **enterprise** analogue for control lifecycle: https://www.coso.org/Pages/ic-integrated-framework.aspx  

---

*Introduced: 2026-04-26.*
