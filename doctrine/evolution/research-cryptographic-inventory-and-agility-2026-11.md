# Cryptographic Inventory, Agility, And The Post-Quantum Transition

Date and source access date: 2026-11-18. Repository basis: `8b518c9` and the companion change.
Status: research basis for [ADR 0054](../../docs/adr/0054-add-cryptographic-inventory-and-agility.md) (accepted 2026-11-18). Model research and model review; no independent human or cryptographic review.

## Question

The [latest-developments note](research-latest-developments-2026-11.md) recorded that the post-quantum transition now has dates and that the library has no cryptographic inventory or agility expectation. [API boundaries](../principles/api-boundaries-and-security.md) §2.1 already binds algorithms and transition dates to maintained profiles, and [ADR 0022](../../docs/adr/0022-hash-function-convergence-blake3-ed25519-hmac.md) rejected a fixed algorithm menu. What should the library add, and what should stay in profiles?

## Source Ledger

Classes follow [Source Authority And Evidence Grading](../patterns/source-authority-and-evidence-grading.md) §2. A delegated agent retrieved each document and saved its text. The lead author read the NIST IR 8547 landing page live in the earlier source check and re-read every passage cited below in the saved copies. The NSA CNSA 2.0 FAQ could not be retrieved and is not relied on. No archive copies were captured.

| Source | Class and scope | Supports | Does not establish |
| --- | --- | --- | --- |
| [NIST IR 8547](https://csrc.nist.gov/pubs/ir/8547/final), Transition to Post-Quantum Cryptography Standards (final, 2026-10-27) | S2, institutional guidance; binding only through other instruments | NIST will deprecate quantum-vulnerable public-key cryptography after 2030 and disallow it under NIST standards and guidelines after 2035. The tables cover ECDSA, EdDSA, RSA, and finite-field and elliptic-curve key establishment. Migration starts with cryptographic inventories and planning. Long-term agility is needed. "Harvest now, decrypt later" puts encrypted data at risk today. Deprecated means usable at the data owner's risk; disallowed means no longer allowed for the purpose | An obligation on non-federal organisations; an inventory format; a definition of agility |
| [US Executive Order 14412](https://www.whitehouse.gov/presidential-actions/2026/06/securing-the-nation-against-advanced-cryptographic-attacks/) (2026-06-22) and [OMB M-26-15](https://www.whitehouse.gov/wp-content/uploads/2026/06/M-26-15-Execution-of-the-Migration-to-Post-Quantum-Cryptography.pdf) (2026-06-24) | S2, binding on US federal civilian agencies only | The order sets 2030-12-31 for key establishment and 2031-12-31 for signatures on high-value and high-impact federal systems. The memorandum phases migration from inventory (2026 to 2027) to full migration (2035), asks for a central cryptography bill of materials, and treats agility as an architectural principle | Anything for other organisations. The memorandum words its phases as "should" |
| [NIST CSWP 39 update 1](https://csrc.nist.gov/pubs/cswp/39/upd1/considerations-for-achieving-crypto-agility/final), Considerations for Achieving Crypto Agility (2025-12-19, updated 2026-06-29; the original is withdrawn) | S2, white paper; considerations, not requirements | Agility is the capability to replace and adapt algorithms in protocols, applications, hardware, and infrastructure while preserving security and operations. Inventory cryptography use, led by data criticality. Avoid gratuitous algorithm options and remove disallowed algorithms | A single definition; the paper gives context-dependent ones |
| [UK NCSC, Timelines for migration to post-quantum cryptography](https://www.ncsc.gov.uk/guidance/pqc-migration-timelines) (v1.0, 2025-03-20) | S2, institutional guidance | By 2028 complete discovery and an initial plan; by 2031 complete the highest-priority migrations; by 2035 complete migration | A mandate. It says early discovery need not be a formal itemised inventory |
| [EU coordinated implementation roadmap for the transition to post-quantum cryptography](https://digital-strategy.ec.europa.eu/en/library/coordinated-implementation-roadmap-transition-post-quantum-cryptography) (NIS Cooperation Group, v1.1, 2025-06-11) | S2, recommendations to Member States | By end 2026, national roadmaps and first steps; by end 2030, high-risk use cases transitioned; by end 2035, medium-risk transitioned. Cryptographic asset management is a first, no-regret step. Agility is described as modular replaceability of cryptographic components | An obligation on organisations |
| [CycloneDX cryptography bill of materials](https://cyclonedx.org/capabilities/cbom/) | S5, product-scoped format documentation | A format for recording algorithms, keys, certificates, and their relationships to software | That any format is required |
| NIST FIPS 203, 204, 205 (final, 2024-08-13) | S1 for the algorithms | Post-quantum key-encapsulation and signature standards exist and are final | Which algorithm a consumer should choose |

## Library Text Today

- API boundaries §2.1 binds "algorithm suites, key sizes, key lifecycle, password-storage parameters, and transition dates" to the threat model and a maintained profile, and refuses a portable algorithm menu.
- ADR 0022 is Rejected. Its rejected proposal included a fixed menu and three agility rules: signed or hashed formats carry an algorithm identifier and version; migration uses dual-read or versioned verification for a bounded time; agility is a format and trust-root concern, not arbitrary runtime selection. It left post-quantum migration as a separate decision.
- [Configuration and secrets](../principles/configuration-and-secrets.md) §2 versions signing keys during cutover. Nothing else addresses algorithm replacement.
- [Dependencies](../principles/dependencies-supply-chain.md) §3 mentions a cryptography bill of materials only as a format capability.
- No file mentions post-quantum cryptography, a cryptographic inventory, or agility.

## Synthesis

1. **Dates belong in profiles.** The authorities differ in scope and dates: US federal agencies, national security systems, EU Member States, and UK guidance each set their own. Stating 2030 or 2035 as library dates would contradict §2.1 and ADR 0022 and would be wrong for most consumers. The profile pattern's rule that current and binding are separate facts fits: NIST's transition guidance document SP 800-131A is still at Revision 2 while IR 8547 states a new schedule.
2. **Inventory is the shared first step.** NIST, the NCSC, the EU roadmap, and the US memorandum all start with knowing where public-key cryptography is used. That is four institutions with different mandates. They differ on form, from informal discovery to a maintained bill of materials, so the library should ask for the inventory and leave the format open.
3. **Agility needs one definition.** The sources disagree on whether agility means negotiation, configuration, or modular replacement. The definition that fits this library is NIST's capability wording joined to ADR 0022's rejected-but-sound format rules: replaceable by configuration, update, or provider change; persisted formats carry an algorithm identifier; migration is bounded; retired options are removed. Arbitrary runtime choice is excluded.
4. **Long-lived confidentiality changes priority.** Data captured today can be decrypted later if its key establishment is quantum-vulnerable. That makes key establishment for long-lived secrets more urgent than signatures, which every schedule reflects.
5. **Re-adopting part of a rejected ADR must be explicit.** ADR 0022 was rejected for its menu. Its format rules were not the reason. A new decision can adopt them at SHOULD strength and say so.

## Decision Input

| Element | Owner | Strength proposed | Admission |
| --- | --- | --- | --- |
| Cryptographic inventory for estate-governed and production systems, format open, longest-lived confidential data first | [API boundaries](../principles/api-boundaries-and-security.md) §2.2 | SHOULD | C1: four independent S2 institutions |
| Agility for new designs and material changes, with the format and migration rules | Same | SHOULD | C2: NIST CSWP 39 and the EU roadmap, with differing definitions noted |
| Post-quantum transition dates | The active profile, per §2.1 | Not doctrine; IR 8547 named as an example baseline | Conformance through the profile |
| Long-lived confidentiality recorded in the threat model | Same §2.2 | SHOULD | C2: NIST IR 8547, corroborated by the schedules' ordering |

## Residual Risk

The NSA national-security timeline was not read. The inventory rule asks for effort before most consumers face a binding date. Agility has no agreed definition, so the library's choice may differ from a regulator's. Post-quantum algorithm selection, hybrid schemes, and performance were not analysed and stay with profiles and platform guidance. No cryptographic expert review is recorded.
