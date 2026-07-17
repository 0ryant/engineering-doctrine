# Governance Program Readiness Checklist

Use when an **organisation** (not only a single repo) is standing up or reviewing **engineering controls governance** for merge paths, supply chain, and pipeline integrity. Aligns with [patterns/engineering-controls-governance-program.md](../patterns/engineering-controls-governance-program.md) and [principles/merge-path-evidence-and-pipeline-integrity.md](../principles/merge-path-evidence-and-pipeline-integrity.md).

## Policy And Ownership

```text
[ ] Written policy defines control classes by product criticality / data class (not only “we use Git”)
[ ] Each control class has a named owner and deputy; escalation path is published
[ ] Policy references external baselines in use (e.g. NIST CSF 2.0 GV.SC, NIST SSDF, sector regulator) with version or date
[ ] Every binding or voluntarily adopted external profile records its authority source, exact revision/update, effective date, accountable interpreter, and review trigger
[ ] Exception / risk-acceptance workflow exists: scope, justification, expiry, compensating control, approver role
```

## Inventory And Enforcement

```text
[ ] Inventory of business-critical repos and their protected branches / required checks exists
[ ] Inventory reconciled to reality at least quarterly (sample + diff process documented)
[ ] No merge path relies solely on “optional” or “warning-only” automation where policy claims enforcement
[ ] High-privilege pipeline definitions require same review bar as security-sensitive application code
[ ] External-profile boundaries include applicable data flows, identities, components, environments, build/support paths, logs/backups, suppliers, AI/model services, and justified exclusions
[ ] Organisation-defined parameters, tailoring, alternatives, and non-applicable determinations have named owners and approval evidence
```

## Evidence And Retention

```text
[ ] Evidence destinations (SARIF, SBOM, attestations, logs) are organisation-controlled with documented retention
[ ] Audit pack composition documented (what links + hashes auditors receive)
[ ] Requirement evidence is bound to the profile revision, system boundary, observation date, assessor/method, depth/coverage, result, and exception record
[ ] SBOM / provenance generation path defined where contracts or regulators expect it (follow active CISA / SPDX / CycloneDX guidance)
```

## Metrics And Calibration

```text
[ ] Coverage/activity metrics (e.g. gate coverage %, finding count) are paired with effectiveness, escaped-failure, false-result, recovery, and operating-cost evidence where material
[ ] Calibration exercises (golden PRs, simulated findings) run on documented cadence
[ ] Post-incident reviews update programme policy when root cause is control design—not only app bug
[ ] Publication or contract revision changes trigger an official-delta review, parameter resolution, migration plan, re-assessment, and accountable acceptance before the profile is relabelled
```

## Control Effectiveness And Lifecycle

Apply these rows to material controls; a low-materiality check may inherit a class-level record rather than create per-check ceremony.

```text
[ ] Each material control identifies its scope and activation condition, the concrete failure addressed, accountable owner, and authority source
[ ] Expected evidence includes operating or assessment evidence for the intended surface and a negative/calibration case that can exercise the claimed detection or prevention
[ ] Adoption and operating cost records material compute/licence cost, latency, human attention, false results, availability impact, and behavioural side effects
[ ] Effectiveness measures test risk reduction or escaped failure; control activity alone is not reported as the outcome
[ ] Review triggers include the applicable cadence plus incident, material architecture/supplier change, authority revision, degraded discrimination, or disproportionate cost
[ ] Review can retain, tune, replace/consolidate, or retire the control, with rationale and follow-up owner
[ ] Replacement or retirement preserves the underlying evidence obligation and requires accountable authority; externally mandated controls change only through their governing authority or an accepted equivalent
[ ] Failed or inconclusive evidence remains unchanged; any exception is a separate scoped, expiring authority decision
```

## Supplier And Acquisition

```text
[ ] Procurement templates reference cybersecurity supply-chain outcomes (per NIST CSF GV.SC-05 style contract integration)
[ ] Acquired repos are mapped to control baseline before joining production train
```

---

## References (External)

- NIST **CSF 2.0** (CSWP 29): https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final  
- NIST **SP 800-218** (SSDF): https://csrc.nist.gov/publications/detail/sp/800-218/final  
- NIST **SP 800-171 Rev. 3** (CUI in nonfederal systems): https://csrc.nist.gov/pubs/sp/800/171/r3/final
- NIST **SP 800-171A Rev. 3** (assessment procedures): https://csrc.nist.gov/pubs/sp/800/171/a/r3/final
- NIST **SP 1305** (CSF & C-SCRM): https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1305.pdf  
- NIST **SP 1303** (CSF 2.0 Enterprise Risk Management; Monitor–Evaluate–Adjust): https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1303.pdf
- **CISA SBOM**: https://www.cisa.gov/sbom  

---

*Introduced: 2026-04-26.*
