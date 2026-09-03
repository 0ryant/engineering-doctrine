# ADR 0032: Add AI Act Transparency, Slopsquatting Gate, And Model/Dataset Admission

- **Status:** Accepted
- **Decision date:** 2026-08-03
- **Recorded date:** 2026-08-03
- **Retrospective:** No
- **Amends:** [ADR 0031](0031-add-agent-identity-mcp-revision-pinning-and-asi-crosswalk-coverage.md) decision 1 (agent-identity principal floor, now tiered)

## Context

Second closure batch from the August 2026 gap audit ([research-bleeding-edge-ai-landscape-gap-audit-2026-08.md](../../doctrine/evolution/research-bleeding-edge-ai-landscape-gap-audit-2026-08.md)), closing three adversarially verified high-severity gaps:

- **G2 — EU AI Act Article 50 transparency.** In force since 2026-08-02: four obligation families (AI-interaction disclosure and machine-readable marking for providers; exposure notification and deepfake labelling for deployers), Commission guidelines (2026-07-20) and Code of Practice on Transparency of AI-generated Content (final 2026-06-10, adequacy opinion 2026-07-08). Doctrine said nothing.
- **G3 — Slopsquatting.** Hallucinated package names are repeatable, hence pre-registrable by attackers; a slopsquat installs legitimately, so scoped names, private-registry precedence, SCA, and lockfile CI all pass. Evidence: Spracklen et al. (USENIX Security 2025; 2024 cohort — 19.7% hallucination, 43% repeat-in-all-10) and the 2026 frontier-cohort replication (Churilov, arXiv 2605.17062 — 4.62–6.10% rates, 127 cross-model-identical names, 53 registrable; verified during landing after the council flagged a citation discrepancy).
- **G4 — Models/datasets as dependencies.** Pickle-class deserialization is code execution; hubs rank by gameable popularity signals; OpenSSF Model Signing v1.0 (Sigstore bundles) and AIBOM formats (CycloneDX ML-BOM, SPDX 3.0 AI/Dataset profiles) matured in 2025–26. Doctrine's supply-chain file covered only code artifacts.

Council provenance: 11-agent draft council; critique yielded 1 blocker (a G3/G4 anchor collision, resolved by apply order) and 6 majors, all resolved before landing — notably: role-split qualifiers on every G2 pointer surface (no cross-role imposition), the G3 gate's enforcement-vs-evidence separation (CI dependency review is the forcing function; the registry lookup is the discriminating evidence — dependency review does not test registry age or publisher), and the G4 dataset bullet split into MUST (digest + provenance) / SHOULD (revision signing).

## Decision

1. **AI Act transparency (normative, profile-gated).** New §5.4 in [privacy-and-data-governance.md](../../doctrine/principles/privacy-and-data-governance.md) is the canonical home: the four Art 50 families as typed engineering duties, activated **only** by registering an EU AI Act external control profile ([revision-pinned-control-profiles.md](../../doctrine/patterns/revision-pinned-control-profiles.md)) that carries the jurisdiction/role applicability decision. Pointer surfaces (ai-adoption-controls §§2–3 launch gate and harm-matrix row, §5 literacy bullet, ai-ml-systems §5, ai-adoption-readiness checklist) are role-qualified. Pending-legislation status: the **Digital Omnibus**, if adopted, would defer high-risk Annex III duties but does not currently alter Art 50; a provisionally agreed transition for Art 50(2) marking on systems already on the market (until 2026-12-02) was pending formal adoption at decision date — review trigger for §5.4, tracked here rather than in doctrine body text.
2. **Slopsquatting gate (normative).** ai-ml-systems §4 gains a pre-install verification gate for AI-proposed dependencies (MUST in estate-governed/production paths; SHOULD for local single-user development): existence, registry age, publisher identity, download history, checked between agent output and the package manager. dependencies-supply-chain §7 gains the slopsquatting distinction, evidence, and mitigations (gate + lockfile discipline + curated allowlist/proxy); code-review-and-change-approval §6 requires explicit review of dependency/lockfile diffs in agent-authored PRs.
3. **Model/dataset admission (normative).** New §8 in dependencies-supply-chain: digest pinning, publisher-not-popularity verification, OMS/Sigstore signature + transparency-log verification where publishers sign, safetensors-class formats with pickle-class loading gated behind sandboxing + expiring exception, SHOULD-level ingest scanning (hub-side scanning satisfies for hub-sourced artifacts), SHOULD-level AIBOM records (formats cited as emerging, not mandated), datasets pinned by digest with per-revision provenance (MUST) and revision signing (SHOULD, per CISA/NSA/FBI AI Data Security CSI), SLSA honestly framed (no ratified ML track). The agentic-loop §11 ASI04 crosswalk cell now cites this coverage; its residual gap (registry-level attestation for agent/tool packages) is tracked as audit action row 22.
4. **Amendment to ADR 0031 — tiered agent-principal floor.** The §2.1 first-class-identity floor is re-cut on capability × materiality: dedicated per-agent principal MUST for high-autonomy/material agents (per-agent revocation and non-union least privilege are unrecoverable on shared principals); shared team principals MAY serve lower-autonomy agents given harness-stamped per-agent attribution and recorded fleet-wide-revocation acceptance. Rationale: operator feedback that team-shared SPNs are BAU for shared pipelines and single-lifecycle rotation; an unscoped dedicated-principal floor fails the library's own adoption economics (repeated exceptions signal a mis-set floor and re-absorb into the path). The named anti-pattern narrows to shared *unattributed* principals.
5. **Style ruling (recorded per ADR 0028 discipline).** New normative content in privacy-and-data-governance §5.4 and dependencies-supply-chain §8 uses typed capitalised BCP-14 keywords inside files whose older sections use bolded lowercase imperatives; typed keywords are the forward convention for new normative sections (consistent with ADR 0031's zero-trust §2.1); retrofitting older sections is deferred, not implied. Council-proposed glossary entries for the three Art 50 duty names were declined — §5.4 carries the definitions; jurisdiction-specific duty names do not earn standalone glossary slots.

## Alternatives Considered

### Art 50 duties as universal doctrine

Rejected. The library makes no regulatory claims for adopters (ADR 0023 precedent); the control profile carries the applicability decision, and non-EU estates inherit nothing.

### Slopsquatting handled by existing SCA/lockfile controls

Rejected on evidence: a slopsquat installs legitimately and keeps the lockfile consistent; only a pre-install existence/provenance check discriminates.

### Mandating model signing and AIBOM formats outright

Rejected. Most publishers do not yet sign; AIBOM formats are unsettled. Signature verification is mandatory only **where the publisher signs**; format mandates route through a future ADR when a standard settles.

### Keeping the unscoped per-agent principal floor (status quo of ADR 0031)

Rejected per decision 4: it lands hardest on the lightest contexts and contradicts the library's exception-re-absorption rule.

## Consequences

### Positive

- EU-scope estates get launch-gated, role-correct Art 50 duties with a registered profile as evidence; everyone else inherits nothing.
- The cheapest effective slopsquatting control (one registry lookup, pre-install) lands where the attack actually happens, with the CI gate as forcing function.
- ML artifacts enter production under the same admission question as containers: built and published by whom, verified how?
- The agent-identity floor now matches operational reality without giving up the kill-switch property where it matters.

### Costs And Risks

- Art 50 duty content depends on Commission guidance that is still evolving (Digital Omnibus transition pending — review trigger).
- The pre-install gate relies on reviewer/installer discipline between agent output and install; tooling that automates the registry lookup is not yet prescribed.
- Pickle-class exceptions require sandbox capability some estates lack; the expiring-exception contract carries the interim risk.
- Shared-principal fleets accept fleet-wide revocation; a single misbehaving low-tier agent can force a team-wide credential rotation.

## Consumer Impact

**Change class:** normative for consumers with EU AI Act scope (G2), estate-governed AI-assisted delivery paths (G3), locally loaded third-party models/datasets in production (G4), or agents holding their own workload identity (amendment); additive guidance otherwise.

**Compatibility proposal:** 0.x minor. All new MUSTs are scope-gated (profile registration, estate-governed paths, production model loading, high-autonomy agents). The ADR 0031 amendment *loosens* the shared-principal prohibition at low tiers; no consumer becomes newly non-compliant by it.

## Acceptance Evidence

- Audit provenance: G2/G3/G4 confirmed by adversarial verification; closure recorded in the audit note §7 (rows 2, 3, 7) alongside new residual-tracking row 22.
- Council provenance: 11-agent council; blocker and all majors resolved in landed text; the G3 citation discrepancy resolved by verifying arXiv 2605.17062 against the live record during landing.
- Primary sources indexed in REFERENCES.md and per-file References: EUR-Lex/Art 50 + Commission guidelines and Code of Practice; Spracklen + Churilov package-hallucination studies with in-the-wild incident reporting; OMS spec + model-signing v1.0, Hugging Face pickle-scanning docs, PyTorch 2.6 weights_only default, CycloneDX ML-BOM, SPDX 3.0, SLSA v1.2 tracks, CISA/NSA/FBI AI Data Security CSI.

**Review provenance:** the council review cited above was model self-review (agent critics re-reading agent drafts). No independent human or domain review of this ADR has been recorded as of 2026-09-03.
