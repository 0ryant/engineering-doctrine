# Supply-Chain Evidence: SLSA Attribution, Provenance Limits, Triggers, And The SBOM Baseline

Date and source access date: 2026-11-18. Repository basis: `8b518c9` and the companion change.
Status: research basis for [ADR 0053](../../docs/adr/0053-correct-slsa-attribution-and-settle-supply-chain-evidence.md) (accepted 2026-11-18). Model research and model review; no independent human or domain review.

## Question

Four open items meet in [dependencies and supply chain](../principles/dependencies-supply-chain.md) §§3–5:

- **M16** (the [corpus review](research-full-corpus-council-review-2026-08.md) and the [source-maintenance note](research-v060-source-maintenance-2026-09.md#m16-slsa-attribution--decision-remains-open)): the section mandates hermetic builds unconditionally and attributes requirements to SLSA levels that the specification does not state.
- **M18**: the same sections are untyped, and the SBOM field list is attributed to a baseline that does not contain it.
- **Finding 13** of the [batch 2 owner audit](research-impl-backlog-batch-2-composition-2026-11.md#owner-gaps-and-contradictions-found): SBOM and provenance triggers differ across five files.
- **Finding 2** of the [latest-developments note](research-latest-developments-2026-11.md): valid provenance was issued for a compromised build.

What do the current primary sources say, and what is the smallest consistent set of rules?

## Source Ledger

Classes follow [Source Authority And Evidence Grading](../patterns/source-authority-and-evidence-grading.md) §2. A delegated agent retrieved each page and saved its text. The lead author re-read every passage cited below in those saved copies, and read the SLSA build requirements page and the CISA landing page live. No archive copies were captured.

| Source | Class and scope | Supports | Does not establish |
| --- | --- | --- | --- |
| [SLSA v1.2 Build track](https://slsa.dev/spec/v1.2/build-track-basics) and [build requirements](https://slsa.dev/spec/v1.2/build-requirements) (status Approved) | S4, versioned foundation specification; the norm for claims about SLSA levels | L1: a consistent build process and platform-generated provenance that may be incomplete or unsigned. L2: a hosted platform generates and signs the provenance and the consumer validates its authenticity; it addresses tampering after the build. L3: runs cannot influence one another, environments are ephemeral, a build cannot poison a cache used by another, signing material is not accessible to user-defined build steps, and the platform's control plane generates or verifies every provenance field. The page states that the isolation requirement is not "hermetic", which it glosses as no network access and defers to future directions. L3 is described as intended for most software releases | Any requirement for hermetic or reproducible builds at L1 to L3; a ban on shared caches as such; the phrase "separation of duties"; certification of any named CI product at a level |
| [SLSA v1.2 FAQ](https://slsa.dev/spec/v1.2/faq) and [future directions](https://slsa.dev/spec/v1.2/future-directions) | S4 | Verified reproducible builds are one way to meet requirements, not a requirement. Hermetic and reproducible builds are possible items for a future higher level. SBOM formats are not part of the Build track | A commitment to a future level |
| [SLSA v1.2 Verifying artifacts](https://slsa.dev/spec/v1.2/verifying-artifacts) and [threats](https://slsa.dev/spec/v1.2/threats) | S4 | Verification should check the builder identity against trusted builders, the signature, and that build type and external parameters match expectations; expectations cover at least builder identity and canonical source repository. Build-track protection depends on a consumer verifying against expectations. L3 does not cover compromise of the build platform itself. A verification summary lets consumers rely on a trusted verifier | Protection against attacker code running in the expected builder from the expected source |
| [SLSA blog, "Mini Shai-Hulud: Where SLSA's Boundaries Fall"](https://slsa.dev/blog/2026/05/mini-shai-hulud-what-slsa-can-and-cannot-do) (2026-05-15, named author; states it was written with model assistance) | S6, named practitioner on the project site; secondary for the incident | In the May 2026 npm compromise, fork code poisoned a cache that a release workflow restored; code from the cache took the workflow's identity token and published packages whose attestations named the correct builder, repository, and workflow. An expected-builder check would have passed. A platform meeting L3 isolation would have blocked the cache route. The post recommends treating shared caches as a trust boundary, source attestations, verification summaries, and builders that keep signing identity out of reach of build steps | The incident facts independently; the maintainers' post-mortem and advisory were not read |
| [npm trusted publishing](https://docs.npmjs.com/trusted-publishers/) and the [GitHub changelog of 2026-07-08](https://github.blog/changelog/2026-07-08-npm-install-time-security-and-gat-bypass2fa-deprecation/) | S5, product-scoped | Trusted publishing lets CI publish with a short-lived, workflow-specific identity instead of a long-lived token. npm 12 makes dependency install scripts and git or remote dependencies opt-in. Tokens that bypass two-factor authentication are expected to lose management rights from August 2026 and direct publish rights around January 2027 | That the token changes have taken effect; both dates are stated as expectations |
| [CISA, 2026 Minimum Elements for an SBOM](https://www.cisa.gov/resources-tools/resources/2026-minimum-elements-software-bill-materials-sbom) (2026-07-29, with NSA, FBI, and 15 partner agencies) | S2, institutional guidance | It updates and replaces NTIA's 2021 minimum elements. Seventeen data fields, ten of them new, including component hash, licence, tool name and version, generation context, and SBOM author signature. It states that it creates no new requirements. Vulnerability data is not a field; advisories such as VEX carry it | When an SBOM is legally required |
| [NTIA, The Minimum Elements For an SBOM](https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom) (2021-07-12) | S2, historical | Seven data fields: supplier name, component name, version, other unique identifiers, dependency relationship, author of SBOM data, timestamp. It recommends tracking vulnerability data separately | A current baseline |
| [Sigstore: cosign 2.0](https://blog.sigstore.dev/cosign-2-0-released/) and the cosign verify reference | S5, product-scoped | Keyless verification requires the verifier to state the expected certificate identity and issuer | That an identity check shows the build was uncompromised |

## Library Text Against The Sources

| Library statement | Finding |
| --- | --- |
| §4 level table, L1 "Build process documented" | The specification asks for a consistent process, not documentation |
| L2 "user config cannot influence the provenance itself" | That is an L3 property. At L2 some fields may be tenant-generated |
| L2 "(GitHub Actions, Azure DevOps)" | The specification names products only as examples of hosted platforms; hosted is necessary, not sufficient |
| L3 "no shared writable cache across builds; separation of duties between build and signing" | The specification bans cache poisoning, not shared caches, and requires that signing material be out of reach of user-defined steps |
| "Hermetic builds … ensure the build environment cannot fetch packages from the network … must produce the same output", and the rationale's "L3 (hermetic)" | SLSA v1.2 requires neither at any level. A hosted L2 pipeline that resolves from a lockfile breaks the bullet as written |
| "SLSA provenance makes tampering between source and artefact detectable" | Only when a consumer verifies it against expectations, and not for code that runs inside a compromised workflow |
| §5 "secret exfiltration risk … drop to zero for keyless flows" | The short-lived identity can be taken from a compromised job; [zero trust](../principles/zero-trust-and-workload-identity.md) §2 already says so |
| §3 "NTIA minimum elements … known vulnerability references" | Not an NTIA field, and NTIA advises tracking it separately. The baseline is also superseded |

Trigger wording today: unconditional in dependencies §3 ("every shipped artefact") and effectively universal in §4; conditional in [build](../principles/build.md) §14, [merge path](../principles/merge-path-evidence-and-pipeline-integrity.md) invariant 6, and three checklists, using four different trigger sets. Merge path states that it wins on conflict, so the conditional reading already prevails in practice.

## Synthesis

1. **Attribution is a factual correction.** The level table can be restated from the specification without changing what the library asks of consumers.
2. **Hermeticity is library policy and should be scoped.** The corpus review and the security scorecard both recommended splitting reproducible inputs, which cost little and are already required by §1, from hermetic and reproducible builds, which need platform change. The specification's own note supports the split.
3. **One trigger set.** "Shipped externally, to regulated environments, or demanded by law, contract, or estate policy" covers every trigger the five files use. Below that line an SBOM is cheap enough to recommend for every production artefact, which keeps the intent of "not only when regulators ask".
4. **Provenance needs a stated limit and a verification rule.** The specification, its threats page, and the incident analysis agree: provenance protects when verified against expectations, and it records what ran, not whether what ran was intended.
5. **Caches are a trust boundary.** The specification's L3 requirement and the incident point at the same control: a release build should not consume a cache that lower-trust builds can write. Build §11 owns caches and says nothing about trust.
6. **Publishing with long-lived tokens is already covered.** The secretless default in zero trust §2 applies to registry publishing wherever the registry accepts federated identity. A pointer is enough.
7. **The SBOM baseline should follow the active specification.** Merge path invariant 6 already says so. CISA 2026 is the current reference; vulnerability data belongs in VEX, where the library already puts exploitability.

## Decision Input

| Decision | Owner | Strength proposed | Admission |
| --- | --- | --- | --- |
| D1 Restate the SLSA Build levels from v1.2 | Dependencies §4 | Factual correction | Conformance claim, pinned specification (S4) |
| D2 Reproducible inputs stay; hermetic and reproducible builds become context-dependent | Dependencies §4 | SHOULD, context-dependent | Loosening; the specification's own scope note |
| D3 SBOM, provenance, and signing typed on one trigger set | Dependencies §§3–5 | MUST where shipped externally, regulated, or demanded; SHOULD otherwise | Internal consistency with merge path invariant 6; the MUST scope matches the strictest existing trigger |
| D4 Provenance limits stated; consumers verify against expectations | Dependencies §§4–5 | SHOULD | C2: one S4 specification, corroborated by product documentation and an incident analysis |
| D5 Release builds restore only caches of the same or higher trust | [Build](../principles/build.md) §11 | SHOULD | C2: the S4 specification's L3 requirement and an S6 incident analysis; both from one project, flagged as single-family |
| D6 SBOM content follows the active baseline; CISA 2026 is the reference | Dependencies §3 | SHOULD | C2: one S2 source that replaces the prior S2 source |

## Corrections To The Earlier Record

The [latest-developments note](research-latest-developments-2026-11.md) said the SLSA post "recommends expected-builder checks". It does, but it also says that check would have passed in this incident. The same note dated the npm token changes to July to October 2026; the changelog states them as expectations for August 2026 and about January 2027.

## Residual Risk

The SLSA and incident sources come from one project, and the incident account is secondary. Estates differ in what "regulated" and "shipped externally" mean. Typing §§3–5 turns reader judgement into stated strength, which may surface non-conformance that was previously unlabelled. No independent review is recorded.
