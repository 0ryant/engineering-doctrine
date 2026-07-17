# Revision-Pinned External Control Profiles

Use this pattern when law, regulation, contract, customer agreement, or an estate decision applies an external control baseline to part of the engineering estate. It turns that baseline into an **addressable, revision-pinned operating profile** that composes with this library's principles, rather than scattering copied control text across them.

The core rule is:

> A control catalogue is not authority by itself. Record the source of applicability, exact baseline revision, bounded system and data scope, selected parameters and tailoring, assessment method, evidence, exceptions, and migration state.

The worked profile is NIST SP 800-171 for Controlled Unclassified Information (CUI). NIST states that Rev. 3 applies to nonfederal system components that process, store, transmit, or protect CUI and is intended for use through federal contracts or other agreements; [NARA's CUI Registry](https://www.archives.gov/cui) remains the authoritative federal catalogue of CUI categories and handling context. This pattern implements [ADR 0026](../../docs/adr/0026-adopt-revision-pinned-external-control-profiles.md); its source analysis is recorded in [research-nist-sp-800-171-control-profiles-2026-07.md](../evolution/research-nist-sp-800-171-control-profiles-2026-07.md).

---

## 1. Scope And Non-Goals

Apply this pattern when an accountable owner determines that an external baseline is binding or intentionally adopted for a named scope. For CUI, first establish the governing agreement, agency implementation policy, CUI category or categories, and system boundary.

This pattern is **not**:

- a declaration that every consumer handles CUI or must implement SP 800-171;
- legal advice or a substitute for the governing contract, agency policy, CUI Registry, or NIST publication;
- permission to self-select a newer or older revision when the agreement fixes another one;
- a control-by-control implementation guide, system security plan, or assessment report; or
- evidence of compliance merely because a document, scanner, or crosswalk exists.

Portable principles remain the default engineering baseline. External profiles add obligations only to their declared scope.

## 2. Invariants

1. **Applicability precedes mapping.** Record the law, regulation, contract clause, customer term, or approved estate decision that makes the profile relevant.
2. **The revision is exact.** Store the publication identifier, revision/update, effective date, and governing agreement version; never write only “NIST compliant”.
3. **Current and binding are separate facts.** [SP 800-171 Rev. 3](https://csrc.nist.gov/pubs/sp/800/171/r3/final) is NIST's current publication and supersedes Rev. 2. A binding agreement may still pin [Rev. 2, including its January 2021 update](https://csrc.nist.gov/pubs/sp/800/171/r2/upd1/final).
4. **The authority source decides the baseline.** A team does not silently upgrade, downgrade, blend, or cherry-pick revisions. Ambiguity is resolved with the contract, policy, and accountable compliance/legal authority.
5. **Assessment matches the profile.** Rev. 3 assessment uses [SP 800-171A Rev. 3](https://csrc.nist.gov/pubs/sp/800/171/a/r3/final) when that is the applicable method. Legacy or sector programmes use the assessment method and edition their authority source requires.
6. **Scope follows data and protection paths.** Identify every component that processes, stores, transmits, or protects in-scope data, including administrative, logging, backup, CI/CD, support, and third-party paths.
7. **Parameters and tailoring are decisions.** Rev. 3 organisation-defined parameters, non-applicable requirements, alternatives, and overlays have named owners, rationale, evidence, and approval.
8. **Evidence is requirement-bound.** Assessment objects, methods, depth, coverage, results, remediation, and exceptions point to the requirement, system boundary, profile version, and observation date they cover.
9. **Exceptions do not rewrite results.** A plan of action, compensating control, or authorised variance is a separate record with owner, scope, expiry, and approval; it does not turn a failed or unassessed requirement into a pass.
10. **Revision migration is a controlled change.** Use the publisher's change analysis, resolve new parameters, reassess the changed boundary, and keep the old profile until the governing authority accepts the new one.
11. **Tool authority cannot enlarge the boundary.** Automation, AI agents, model services, retrieval stores, and support tooling may handle in-scope data only when explicitly admitted to the profile boundary and granted bounded access.
12. **Operational evidence keeps the profile current.** Incidents, architecture changes, supplier changes, new data flows, and material control failures trigger boundary/profile review rather than waiting for the next annual audit.

## 3. Minimum Profile Record

The profile may live in a GRC system, repository, contract register, service catalogue, or linked records. It must remain reconstructable.

| Field | Minimum content |
| --- | --- |
| Profile identity | Stable ID, owner, status, effective date, review date. |
| Authority source | Contract/clause, regulation, customer agreement, or approved voluntary adoption; accountable interpreter. |
| Baseline | Publisher, publication, exact revision/update, source URL or digest, assessment method. |
| Data scope | CUI categories/markings or other regulated data classes; originator/agency constraints; dissemination and decontrol rules where applicable. |
| System boundary | Components, environments, identities, networks, stores, backups, logs, build/release paths, support tools, suppliers, and excluded components with rationale. |
| Parameters and tailoring | Organisation-defined parameters, overlays, alternatives, non-applicable determinations, and their approvals. |
| Requirement ownership | Implementer, evidence producer, control owner, assessor, risk owner, and authoriser. |
| Evidence | Requirement-to-evidence map; assessment objects/methods; depth/coverage; result; date; candidate/system version; retention location. |
| Findings and exceptions | Finding state, remediation/plan-of-action owner, due date, variance/waiver authority, compensating controls, expiry. |
| Migration | Current and target profiles, official delta source, changed requirements/parameters, re-assessment plan, acceptance decision. |

## 4. NIST SP 800-171 Profile Selection

| Situation | Profile treatment |
| --- | --- |
| New or renewed scope whose authority source permits the current NIST baseline | Adopt Rev. 3, resolve its organisation-defined parameters and tailoring, and assess using Rev. 3-compatible procedures. |
| Existing agreement explicitly pins Rev. 2 | Preserve Rev. 2 as the binding profile and use the assessment method named by that agreement; create a separate Rev. 3 migration record. |
| Agreement says the edition effective at solicitation/award | Record that date and edition as evidence. For example, current [DFARS 252.204-7012](https://www.acquisition.gov/dfars/252.204-7012-safeguarding-covered-defense-information-and-cyber-incident-reporting.) uses the edition effective when the solicitation was issued or one authorised by the contracting officer. |
| Authority source or version is ambiguous | Mark the profile unresolved and obtain an accountable interpretation; do not assert compliance or choose the convenient revision. |
| Critical programme or high-value asset requires enhanced APT protection | Evaluate a separately authorised [SP 800-172 Rev. 3](https://csrc.nist.gov/pubs/sp/800/172/r3/final) profile; do not silently treat it as part of the ordinary 800-171 baseline. |

NIST publishes a Rev. 2-to-Rev. 3 change analysis with Rev. 3. Use it as migration input, not as proof that old evidence satisfies new requirements. Changed families, structure, parameters, tailoring, and assessment procedures make simple identifier substitution unsafe.

## 5. Composition Across The Doctrine

The profile owns applicability and traceability. Existing principles own engineering behaviour.

| Doctrine surface | Profile obligation |
| --- | --- |
| [Privacy and data governance](../principles/privacy-and-data-governance.md) | Classify CUI separately from personal data; preserve category, marking, dissemination, retention, and decontrol metadata; avoid assuming privacy rules alone satisfy CUI handling. |
| [Zero trust and workload identity](../principles/zero-trust-and-workload-identity.md) | Bind users, workloads, administrators, and service calls to authenticated identities and least-privilege policy within the declared boundary. |
| [Configuration and secrets](../principles/configuration-and-secrets.md) | Keep profile parameters and approved configuration versioned; protect credentials and cryptographic material through the estate's controlled secret lifecycle. |
| [Secure development lifecycle](../principles/secure-development-lifecycle.md) | Treat applicable requirements as design constraints, acceptance claims, review criteria, tests, and vulnerability-response obligations. |
| [Threat modelling](../principles/threat-modeling-stride-lite.md) | Model CUI flows, protection components, suppliers, administrative paths, and boundary escape; test blast-radius claims. |
| [Dependencies and supply chain](../principles/dependencies-supply-chain.md) | Include external services, libraries, build systems, and suppliers in the scoped boundary and retain provenance/evidence required by the profile. |
| [Merge-path evidence](../principles/merge-path-evidence-and-pipeline-integrity.md) | Bind profile-aware checks, approvals, evidence, and exceptions to the exact change and protected baseline. |
| [Audit logging](../principles/audit-logging.md) | Capture security-relevant access and administrative events without copying CUI payloads unnecessarily; protect and retain evidence according to the profile. |
| [Reliability and incidents](../principles/reliability-slo-incidents.md) | Route suspected exposure, control failure, supplier incident, recovery, and notification into the governed incident path. |
| [AI and ML systems](../principles/ai-ml-systems.md) | Admit model providers, prompts, context stores, eval sets, logs, agent runners, and tools to the boundary before CUI use; run contracts cannot grant data authority the profile does not. |
| [AI-native SDLC](ai-native-software-development-lifecycle.md) | Carry profile ID/revision, data/system scope, requirement claims, assessment evidence, authority, exceptions, and runtime outcomes through the transition record. |

## 6. Assessment And Evidence Semantics

- Treat each applicable requirement as an addressable claim with implementation and assessment ownership.
- Record the assessment procedure, objects examined/interviewed/tested, depth, coverage, environment, date, assessor identity, and result.
- Use `pass`, `fail`, `inconclusive`, or an equally explicit estate vocabulary; absence or stale evidence is not success.
- Bind evidence to the system/profile version it assessed. A material boundary or parameter change invalidates affected evidence.
- Track remediation and authorised variances beside—not inside—the assessment result.
- Preserve enough evidence to reproduce the authorisation decision without storing unnecessary CUI, secrets, personal data, or full prompt transcripts.

SP 800-171A provides assessment procedures and permits assessment depth and coverage to be adapted. It does not make every self-assessment independent, sufficient, or contractually accepted; the authority source determines required assessor independence and acceptance.

## 7. AI, Agents, And External Services

This library infers the following operational rule from NIST's component-based scope and the doctrine's existing AI authority model:

> If a model endpoint, agent runner, retrieval/index service, prompt or trace store, observability sink, evaluation service, human-review tool, or support supplier processes, stores, transmits, or protects CUI, it is part of the candidate CUI boundary until an accountable scope decision proves otherwise.

Therefore:

- classification and boundary checks occur before prompt, retrieval, fine-tuning, evaluation, or tool execution;
- provider terms, location, subprocessors, retention, training use, administrative access, incident handling, and deletion/export capabilities are profile inputs;
- a run contract may narrow allowed data and tools but cannot make an unapproved provider or path acceptable;
- generated output derived from CUI remains governed according to the authority source; and
- agent logs, scratch space, checkpoints, screenshots, and verifier artefacts minimise or reference CUI rather than duplicating it by default.

## 8. Brownfield Adoption

1. **Discover applicability** — inventory agreements, CUI categories, existing SSPs/assessments, named owners, and revision pins.
2. **Register profiles** — create one record per materially distinct authority/baseline/scope; do not average several contracts into “NIST-ish”.
3. **Reconstruct boundaries** — follow representative CUI from receipt/creation through code, people, services, build/support paths, backups, logs, and disposal/decontrol.
4. **Bind evidence** — map requirements to owners, implementations, assessment procedures, evidence locations, results, findings, and exceptions.
5. **Plan revision migration** — use official deltas, resolve parameters, test changed controls, reassess, and obtain authority acceptance.
6. **Reconcile continuously** — trigger review from material change, incident, supplier drift, new CUI category, contract renewal, or publication update.

Pilot one real boundary and one failed or inconclusive assessment path before scaling a universal GRC schema.

## 9. Failure Modes

- Making SP 800-171 a universal engineering baseline without CUI applicability.
- Citing “Rev. 2/3” as if the revisions were interchangeable.
- Upgrading to Rev. 3 in documentation while the contract, assessment, or implementation remains on Rev. 2.
- Treating a crosswalk, SSP, POA&M, scanner report, or self-attestation as proof of requirement satisfaction.
- Omitting CI/CD, logs, backups, help desks, AI services, or subcontractors from the system boundary.
- Copying CUI into evidence stores, prompts, tickets, screenshots, or telemetry that are outside the boundary.
- Leaving organisation-defined parameters unresolved or hiding them in tool defaults.
- Carrying old assessment evidence across a material revision or boundary change without re-evaluation.
- Allowing permanent findings or exceptions with no owner, expiry, compensating control, or acceptance authority.

## 10. Consumer Impact

**Change class:** additive guidance for all consumers; normative tightening only for consumers that declare a binding or voluntarily adopted external control profile.

**Compatibility proposal:** **0.x minor**. Consumers without CUI or another external profile gain no new control catalogue. Affected consumers must identify the authority source, exact revision, boundary, parameters, evidence, exceptions, and migration state before making compliance claims.

## Related

- [Engineering Controls Governance Program](engineering-controls-governance-program.md)
- [Governance Program Readiness Checklist](../checklists/governance-program-readiness.md)
- [Secure Development Lifecycle And Vulnerability Response](../principles/secure-development-lifecycle.md)
- [Privacy And Data Governance](../principles/privacy-and-data-governance.md)
- [Merge Path Evidence And Pipeline Integrity](../principles/merge-path-evidence-and-pipeline-integrity.md)
- [AI-Native Software Development Lifecycle](ai-native-software-development-lifecycle.md)

## References

- NIST SP 800-171 Rev. 3: https://csrc.nist.gov/pubs/sp/800/171/r3/final
- NIST SP 800-171A Rev. 3: https://csrc.nist.gov/pubs/sp/800/171/a/r3/final
- NIST SP 800-171 Rev. 2, January 2021 update (withdrawn by NIST; retained here for revision-pinned obligations): https://csrc.nist.gov/pubs/sp/800/171/r2/upd1/final
- NIST announcement and Rev. 3 change summary: https://csrc.nist.gov/News/2024/updated-security-requirements-for-protecting-cui
- NARA CUI programme and Registry: https://www.archives.gov/cui
- DFARS 252.204-7012: https://www.acquisition.gov/dfars/252.204-7012-safeguarding-covered-defense-information-and-cyber-incident-reporting.
