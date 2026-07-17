# Research: NIST SP 800-171 As A Revision-Pinned Doctrine Profile (2026-07)

## Question

What should this engineering-doctrine library learn from NIST SP 800-171 Rev. 2 and Rev. 3, and should those publications be folded only into the software lifecycle or across the wider doctrine?

## Conclusion

SP 800-171 is broader than secure development. Its requirements span access control, awareness, audit, assessment/authorisation/monitoring, configuration, identity, incident response, maintenance, media, physical protection, planning, personnel, risk, acquisition, communications protection, system integrity, and supply-chain risk. It therefore belongs as a **conditional cross-doctrine profile**, not as an SDLC-only citation.

It must not become a universal baseline. NIST describes SP 800-171 as requirements for protecting CUI in nonfederal systems and as material intended for federal contracts and other agreements. Applicability comes from the governing authority and CUI scope. The library should preserve its portable principles and compose an exact, revision-pinned profile only where relevant.

## Primary Sources And Limits

| Source | What it supports | Limit |
| --- | --- | --- |
| [NIST SP 800-171 Rev. 3](https://csrc.nist.gov/pubs/sp/800/171/r3/final), May 2024 | Current NIST publication; supersedes Rev. 2; applies to components that process, store, transmit, or protect CUI; intended for contracts/agreements; lists 17 control families and provides official Rev. 2-to-Rev. 3 change material. | Recommended requirements do not create a private organisation's obligation without an authority source. |
| [NIST SP 800-171A Rev. 3](https://csrc.nist.gov/pubs/sp/800/171/a/r3/final), May 2024 | Assessment procedures, objects, methods, and adaptable depth/coverage for Rev. 3 requirements. | Does not determine which assessor or acceptance model a contract requires. |
| [NIST Rev. 3 publication announcement](https://csrc.nist.gov/News/2024/updated-security-requirements-for-protecting-cui) | Rev. 3 alignment to SP 800-53 Rev. 5, organisation-defined parameters, new tailoring criteria, and concurrent assessment publication. | Summary only; use the publications for normative content. |
| [NIST SP 800-171 Rev. 2, January 2021 update](https://csrc.nist.gov/pubs/sp/800/171/r2/upd1/final) | Historical baseline, scope, SSP context, and legacy companion assessment surface. NIST marks it withdrawn and superseded by Rev. 3. | Withdrawal does not by itself rewrite an existing contract or sector programme. |
| [NARA CUI programme and Registry](https://www.archives.gov/cui) | Government-wide CUI categories, markings, policy context, and instruction to consult agency implementation policy. | The registry does not identify a consumer's contract scope by itself. |
| [DFARS 252.204-7012](https://www.acquisition.gov/dfars/252.204-7012-safeguarding-covered-defense-information-and-cyber-incident-reporting.) (current page reviewed 2026-07-17) | Concrete evidence that an agreement can bind the NIST edition effective at solicitation or one authorised by the contracting officer; includes supplier flow-down and incident duties. | DoD-specific; not portable law for every doctrine consumer. |
| [NIST SP 800-172 Rev. 3](https://csrc.nist.gov/pubs/sp/800/172/r3/final), May 2026 | Separate enhanced CUI requirements for critical programmes/high-value assets facing advanced persistent threats. | Not automatically part of an ordinary SP 800-171 profile. |

## Rev. 2 And Rev. 3 Are Not Interchangeable

| Dimension | Rev. 2 | Rev. 3 implication |
| --- | --- | --- |
| NIST status | Withdrawn/superseded, but may remain contractually pinned. | Current NIST publication. |
| Structure | 14 requirement families and Rev. 2 requirement identifiers. | 17 families, direct SP 800-53 Rev. 5 alignment, revised structure and tailoring. |
| Parameters | Many values embedded or left to implementation context. | Explicit organisation-defined parameters require governed values. |
| Assessment | Legacy SP 800-171A or sector/contract assessment methodology. | SP 800-171A Rev. 3 when the applicable authority adopts it. |
| Migration | Evidence may remain valid only for the pinned Rev. 2 profile. | Use official change analysis, resolve parameters, test changes, and reassess; do not rename old evidence. |

The library therefore rejects the label “Rev. 2/3 compliant”. A defensible record identifies one exact baseline for one authority source and boundary, plus a separate migration state where necessary.

## Wider Doctrine Mapping

| Doctrine area | Finding |
| --- | --- |
| Governance and acquisition | Profile ownership, applicability, parameters, supplier flow-down, exceptions, assessment acceptance, and revision monitoring belong in the engineering-controls governance programme. |
| Data governance | CUI classification, category/marking, dissemination, retention, and decontrol must be distinct from personal-data classifications even where one record is both. |
| Architecture and identity | The scope is component- and flow-based; identity, least privilege, system boundary, remote access, administrative paths, and protection components are architecture constraints. |
| Secure development and change | Applicable requirements become design constraints, acceptance claims, tests, review criteria, and release evidence; SSDF remains the general secure-development source. |
| Supply chain | Suppliers, cloud/model providers, CI/CD, dependencies, external services, and provenance/evidence stores may enter the boundary. |
| Audit and assessment | Evidence must be requirement-, revision-, boundary-, date-, depth-, and coverage-bound; a plan of action or waiver is not a pass. |
| Operations and incidents | Material change, control drift, exposure, supplier incidents, recovery, notification, and remediation must reconcile back to the profile. |
| AI and agents | If a model, prompt store, retrieval index, runner, tool, log sink, or reviewer processes/stores/transmits/protects CUI, it is a candidate in-scope component. This is the library's synthesis from NIST's component scope and existing AI/run-contract doctrine. |

## Adoption Decisions

| Decision | Disposition | Reason |
| --- | --- | --- |
| Make SP 800-171 a universal doctrine baseline | **Reject** | Applicability is CUI- and authority-specific; universal adoption creates compliance theatre and unnecessary cost. |
| Cite it only in the AI-native SDLC | **Reject** | The baseline spans governance, data, identity, audit, configuration, incidents, acquisition, physical/media, and supply chain. |
| Copy requirements into each principle | **Reject** | Duplicates NIST, loses revision identity, and creates drift. |
| Add a revision-pinned external-profile pattern | **Take** | Preserves portable principles while making applicability, revision, scope, evidence, and migration explicit. |
| Treat Rev. 3 as current for new profiles | **Take with authority guard** | NIST marks Rev. 3 current, but the governing agreement controls adoption. |
| Preserve Rev. 2 where explicitly pinned | **Take as legacy compatibility** | Current federal clauses can bind an edition by solicitation/authorisation; NIST withdrawal alone is not a contract amendment. |
| Pair requirements with assessment evidence | **Take** | SP 800-171A provides the evidence procedure surface missing from a catalogue-only citation. |
| Encode every requirement in repository schemas now | **Defer** | Control content, parameters, overlays, and assessment programmes vary; pilot a real profile before standardising a machine contract. |

## Residual Limits

- This research does not determine whether any particular consumer holds CUI or which contract clause applies.
- It does not interpret CMMC, agency-specific overlays, FedRAMP, export-control regimes, or CUI Specified safeguards.
- It does not provide a legal conclusion, SSP, POA&M, assessment score, or certification.
- NIST's crosswalks and change analysis reduce migration effort but do not prove implementation equivalence.
- A real pilot is still required to calibrate evidence retention, boundary granularity, ODP ownership, and agent/provider admission.
