# ADR 0026: Adopt Revision-Pinned External Control Profiles

- **Status:** Accepted
- **Decision date:** 2026-07-17
- **Recorded date:** 2026-07-17
- **Retrospective:** No

## Context

The doctrine already has portable principles for secure development, privacy/data governance, identity, configuration, supply chain, merge evidence, audit, incidents, and AI systems. NIST SP 800-171 Rev. 3 is relevant across all of those surfaces when a consumer handles CUI, but it is not a universal engineering baseline.

NIST marks Rev. 3 as current and Rev. 2 as withdrawn/superseded. Real agreements can nevertheless pin the edition effective at solicitation or another authorised edition. Treating “Rev. 2/3” as one profile would erase material structural, parameter, tailoring, and assessment differences. Copying individual requirements into principle files would also detach them from applicability and revision history.

Research and source limits are recorded in [research-nist-sp-800-171-control-profiles-2026-07.md](../../doctrine/evolution/research-nist-sp-800-171-control-profiles-2026-07.md).

## Decision

Adopt [Revision-Pinned External Control Profiles](../../doctrine/patterns/revision-pinned-control-profiles.md) as the compositional pattern for CUI and other externally imposed engineering baselines.

The pattern requires:

1. a source of applicability before control mapping;
2. an exact baseline revision/update and effective date;
3. bounded data, system, supplier, automation, and support scope;
4. resolved parameters, tailoring, alternatives, and accountable owners;
5. a matching assessment method and requirement-bound evidence;
6. separate findings, exceptions, and authority decisions;
7. controlled revision migration using publisher change material and re-assessment; and
8. explicit admission of AI/model/agent/tool paths that handle in-scope data.

SP 800-171 Rev. 3 is the current NIST profile for new adoption where the governing authority permits it. Rev. 2 is retained only as a named legacy profile where an agreement or assessment programme pins it. The authority source—not this library—decides which revision is binding.

Portable principles remain universal. The profile links them together for affected consumers and does not reproduce the NIST control catalogue.

## Alternatives Considered

### Cite SP 800-171 only from the AI-native SDLC

Rejected. Its scope spans governance, data, access, audit, configuration, incidents, acquisition, supply chain, and operations.

### Make Rev. 3 a universal security baseline

Rejected. This would turn CUI-specific contractual guidance into global law and make unaffected consumers appear non-compliant.

### Keep Rev. 2 and Rev. 3 side by side without a selection rule

Rejected. It invites revision blending, stale assessment evidence, and ambiguous compliance claims.

### Copy control requirements into every related principle

Rejected. It would duplicate external normative text, drift as NIST changes, and lose the authority/revision/boundary context.

## Consequences

### Positive

- The wider doctrine gains one auditable path from external authority to engineering implementation and evidence.
- Rev. 2 legacy obligations and Rev. 3 migrations can coexist without pretending they are equivalent.
- Existing principles remain portable and do not become US-federal-only.
- CUI use by AI services and agent tooling becomes a boundary decision rather than a prompt-policy afterthought.

### Costs And Risks

- Affected consumers must inventory agreements, boundaries, suppliers, parameters, evidence, and exceptions.
- The library does not supply a control-by-control SSP or assessment implementation.
- Agency, sector, CMMC, FedRAMP, export-control, and CUI Specified overlays still require estate-specific interpretation.
- Misclassification of applicability remains possible without accountable legal/compliance review.

## Consumer Impact

**Change class:** additive guidance for the general library; normative tightening for consumers that declare a binding or voluntarily adopted external profile.

**Compatibility proposal:** 0.x minor. Consumers without applicable CUI/external-profile scope have no new baseline. Affected consumers should register the exact authority, revision, boundary, assessment, exception, and migration state before adopting the new profile language.

## Acceptance Evidence

- Canonical pattern defines applicability, revision selection, scope, parameters, assessment, evidence, migration, and AI/service admission.
- Governance and readiness surfaces reference revision-pinned profiles.
- Security, privacy/data, merge evidence, audit, and AI principles link to the profile without copying the catalogue.
- NIST Rev. 3, Rev. 3 assessment procedures, Rev. 2 legacy source, NARA CUI Registry, and current DFARS revision-selection evidence are indexed.
