# ADR 0053: Correct SLSA Attribution And Settle Supply-Chain Evidence Rules

- **Status:** Accepted
- **Decision date:** 2026-11-18
- **Recorded date:** 2026-11-18
- **Retrospective:** No
- **Deciders:** Repository operator
- **Review provenance:** Operator-directed and operator-accepted on 2026-11-18; drafted and reviewed by a model, no independent human or domain review recorded
- **Research:** [Supply-chain evidence decisions](../../doctrine/evolution/research-supply-chain-evidence-decisions-2026-11.md)
- **Canonical owners:** [Dependencies And Supply Chain](../../doctrine/principles/dependencies-supply-chain.md) §§3–5 (D1–D4, D6); [Build](../../doctrine/principles/build.md) §11 (D5)
- **Derived landings:** [Build](../../doctrine/principles/build.md) §14 (pointer); [Build Readiness](../../doctrine/checklists/build-readiness.md); [Release Readiness](../../doctrine/checklists/release-readiness.md); [Platform Readiness](../../doctrine/checklists/platform-readiness.md); [Dependency Adoption](../../doctrine/impl/dependency-adoption.md)

## Context

Four recorded items meet in dependencies §§3–5. M16: the section requires hermetic builds unconditionally and attributes requirements to SLSA levels that the specification does not state. M18: the sections are untyped and the SBOM field list is attributed to a baseline that does not contain it and has been replaced. Finding 13 of the batch 2 owner audit: SBOM and provenance triggers differ across five files. Finding 2 of the latest-developments note: an incident produced valid provenance for a compromised build.

## Decision

### D1. Restate the SLSA Build levels from v1.2

The level table in dependencies §4 is rewritten from the specification: what L1, L2, and L3 require, and what each addresses. Product names leave the table. The text says a level describes the build platform, so a producer confirms which level its platform meets.

### D2. Keep reproducible inputs; scope hermetic and reproducible builds

- Pinned toolchains, base images by digest, and builds from committed lockfiles stay as library policy and are labelled as such, not as SLSA requirements.
- **SHOULD, context-dependent:** hermetic builds (declared inputs only; in the strong form, no network access during the build) and reproducible outputs apply where the threat model, a Build L3 target, or an active profile calls for them.

This resolves M16 by the second of its two recorded options.

### D3. Type SBOM, provenance, and signing on one trigger set

The trigger set is: artefacts shipped to customers or other external parties, artefacts for regulated environments, and any artefact for which law, contract, or estate policy demands the evidence.

- **SBOM. MUST** for the trigger set. **SHOULD** for every other production artefact. Internal-only tooling keeps its per-release minimum.
- **Provenance. SHOULD** target SLSA Build L2 for artefacts shipped externally or to regulated environments, with Build L3 as the target for critical or customer-facing software. **MUST** where law, contract, or estate policy demands provenance, at the level demanded.
- **Signing. SHOULD** for container images and release binaries shipped externally or deployed to production.

Build §14 and the readiness checklists point to dependencies §§3–4 for the trigger instead of stating their own. Merge path invariant 6 is unchanged and consistent.

### D4. State what provenance shows, and verify against expectations

- The owner text says provenance records which builder, source, and parameters produced an artefact, and that it does not show the code that ran was the code the producer intended.
- **SHOULD (consumers of provenance or signatures, at deploy or admission and at dependency admission where a publisher provides them):** verify against expectations: the expected builder identity and issuer, the expected source repository, and build type and parameters where the format carries them. Accepting any valid signature or attestation is not verification of origin.
- **MAY:** a verification summary from a verifier the estate trusts stands in for re-verifying each attestation.
- Overstated claims in §§4–5 are corrected. Registry publishing from CI is routed to the secretless default in zero trust §2.

### D5. Release builds restore only caches of the same or higher trust

Owner: build §11.

- **SHOULD (release and deploy builds):** restore only caches written by builds of the same or higher trust. A cache that builds of unreviewed changes can write is not an input to a release build.

### D6. SBOM content follows the active baseline

- **SHOULD:** SBOM content meets the minimum-elements baseline active at adoption time. Where no other baseline binds, the reference is CISA's 2026 Minimum Elements, which replaces the 2021 NTIA list.
- "Known vulnerability references" leaves the per-component list. Neither baseline makes vulnerability data a minimum element; it stays in the VEX and advisory records the section already requires.

This, with D3, resolves M18.

## Control Cost And Lifecycle

| Decision | Failure addressed | Evidence | Operating cost | Review trigger |
| --- | --- | --- | --- | --- |
| D1 | Teams claiming a SLSA level on a wrong definition, or blocked by a control SLSA does not impose | The corrected table and its pinned source | None | A new SLSA version |
| D2 | A baseline rule that every hosted pipeline breaks | Recorded hardening target where applied | Lower than before for most consumers | An incident traced to undeclared build inputs |
| D3 | Four trigger sets; unlabelled strength | SBOM, provenance, and signature attached to artefacts in the trigger set | SBOM generation for external and regulated artefacts, where not already done | A regime or buyer demanding more than the trigger set |
| D4 | Valid attestations accepted without checking who built what from where | Verification policy naming expected builder, issuer, and source | Policy definition and upkeep | An accepted artefact later found to come from an unexpected builder or source |
| D5 | A release build consuming a cache poisoned by a lower-trust build | Cache scoping in pipeline configuration | Possible loss of cache reuse between pull-request and release builds | A cache-related build compromise |
| D6 | SBOMs built to a superseded field list | SBOM fields against the active baseline | Tool configuration | A successor baseline |

Each rule can be simplified or retired if its review trigger shows cost without benefit.

## Alternatives Considered

- **M16 option 1: keep hermetic builds unconditional and label them library policy.** Rejected; the rule contradicts the section's own L2 baseline, and both the corpus review and the security scorecard recommended scoping it.
- **Make SBOMs a MUST for every artefact.** Rejected; merge path, which wins on conflict, already conditions them, and the cheapest consistent line is MUST where the artefact leaves the estate or is demanded.
- **Make provenance verification a MUST.** Deferred; the specification itself words verification as SHOULD, and verification tooling varies by ecosystem.
- **Require Build L3 for all release builds.** Rejected for now; the specification notes L3 usually needs significant platform change. D5 takes the one L3 property that the incident turned on.
- **Leave the SBOM baseline at NTIA 2021 for stability.** Rejected; its publisher's successor replaces it, and merge path already cites the successor.

## Consumer Impact And Migration

Change class: **factual correction** (D1), **normative loosening** (D2), **typing with scoped strength** (D3: a MUST for artefacts in the trigger set, a SHOULD elsewhere, where the text was previously an untyped imperative), **normative additions** at SHOULD (D4, D5), and **baseline update** (D6). Compatibility: pre-1.0 minor.

Migration: check any SLSA level claim against the corrected table; record where hermetic or reproducible builds apply; confirm SBOMs exist for artefacts in the trigger set; write the verification expectations (builder, issuer, source) used at deploy or admission; scope release-build caches away from lower-trust builds; move SBOM tooling to the active field list.

## Acceptance Criteria

- Dependencies §§3–5 carry the corrected table, the typed rules with scope, the provenance limit, and corrected claims.
- Build §11 carries the cache rule; build §14 points to dependencies for triggers.
- Build, release, and platform readiness prompts use the single trigger set and link their owners.
- Dependency Adoption reflects the typed SBOM scope and the expectations check.
- References cite SLSA v1.2 pages, CISA 2026, and NTIA 2021 as historical.
- The readiness record marks M16 and M18 decided here, and the batch 2 audit marks finding 13 decided here.
- The ADR index lists this decision, and doctrine preflight passes.

## Residual Risk

The SLSA specification and the incident analysis come from one project, and the incident account is secondary. "Regulated" and "shipped externally" remain estate judgements. Typing the sections may surface non-conformance that was previously unlabelled. Model review only.
