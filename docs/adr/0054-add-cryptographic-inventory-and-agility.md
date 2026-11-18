# ADR 0054: Add Cryptographic Inventory And Agility; Bind Post-Quantum Dates Through Profiles

- **Status:** Accepted
- **Decision date:** 2026-11-18
- **Recorded date:** 2026-11-18
- **Retrospective:** No
- **Deciders:** Repository operator
- **Review provenance:** Operator-directed and operator-accepted on 2026-11-18; drafted and reviewed by a model, no independent human or cryptographic review recorded
- **Research:** [Cryptographic inventory, agility, and the post-quantum transition](../../doctrine/evolution/research-cryptographic-inventory-and-agility-2026-11.md); finding 1 in the [latest-developments note](../../doctrine/evolution/research-latest-developments-2026-11.md)
- **Canonical owner:** [API Boundaries And Security](../../doctrine/principles/api-boundaries-and-security.md) §2.2
- **Derived landings:** [Dependencies And Supply Chain](../../doctrine/principles/dependencies-supply-chain.md) §3 (pointer); [Platform Readiness](../../doctrine/checklists/platform-readiness.md); [glossary](../../doctrine/glossary.md)
- **Relationship to earlier decisions:** [ADR 0022](0022-hash-function-convergence-blake3-ed25519-hmac.md) stays Rejected. This ADR adopts two of the format rules its rejected proposal contained, at SHOULD strength, and does not adopt its algorithm menu.

## Context

NIST IR 8547 went final on 2026-10-27: quantum-vulnerable public-key algorithms are deprecated under NIST standards after 2030 and disallowed after 2035. US federal policy, UK guidance, and an EU roadmap set their own milestones for their own audiences. All of them start with an inventory of where public-key cryptography is used.

The library binds algorithms and transition dates to maintained profiles and refuses a portable menu. It has no expectation that a consumer knows where its cryptography is, or can replace it.

## Decision

Add §2.2 "Cryptographic Inventory And Agility" to the API boundaries principle.

- **SHOULD (estate-governed and production systems):** keep a cryptographic inventory: where public-key cryptography is used for key establishment and signatures, which algorithms and key sizes are in use, and which data must stay confidential beyond the transition horizon. Start with the data that has the longest confidentiality life. A cryptography bill of materials is one way to hold it; no format is required.
- **SHOULD (new designs and material changes):** design for agility. Algorithms, parameters, and keys can be replaced through configuration, a library or module update, or a provider change, without redesigning the protocol or data format. Persisted signed or encrypted formats carry an algorithm identifier and version. Migration uses a bounded dual-read or dual-verify period. Retired algorithms are removed. Agility is not arbitrary runtime algorithm choice.
- **SHOULD:** the threat model records data whose confidentiality must outlast the transition, because traffic captured now can be decrypted later.
- **Dates stay profile-bound.** Post-quantum deadlines bind through the active profile under §2.1. The owner text names IR 8547 as an example of a baseline a profile might pin and states no library date.

The library names no post-quantum algorithm.

## Control Cost And Lifecycle

| Failure addressed | Evidence | Operating cost | Review trigger |
| --- | --- | --- | --- |
| A binding transition date arrives and the estate cannot say where its public-key cryptography is, or cannot change it without redesign | The inventory; design notes showing algorithm identifiers and a migration path; threat-model entries for long-lived confidential data | Discovery effort, largest for estates with bespoke cryptography; small for those using managed services and standard protocols | A profile with a transition date becomes binding; NIST revises SP 800-131A or issues bill-of-materials guidance; a regulator defines agility differently |

The inventory rule can be narrowed if consumers on managed platforms show it adds nothing beyond their provider's attestations.

## Alternatives Considered

- **State 2030 and 2035 as library dates.** Rejected; the dates bind different audiences, and §2.1 and ADR 0022 keep such parameters in profiles.
- **Name the post-quantum algorithms.** Rejected for the same reason ADR 0022 was.
- **Require a cryptography bill of materials.** Rejected; the sources differ on form, and UK guidance says early discovery need not be an itemised inventory.
- **A MUST for the inventory.** Deferred; no source binds non-federal consumers, and a MUST would arrive before most profiles do.
- **Leave everything to profiles.** Rejected; a profile can set a date but cannot make an estate able to meet it, and inventory and agility are the engineering preparation every schedule assumes.
- **Place the rule in dependencies §3 beside the bill-of-materials mention.** Rejected as owner; §2.1 is where the library's cryptographic choices live. Dependencies gets a pointer.

## Consumer Impact And Migration

Change class: **normative additions** at SHOULD. Compatibility: pre-1.0 minor.

Migration: list where public-key cryptography is used, starting with systems that protect long-lived confidential data; record that data in threat models; for new designs, carry algorithm identifiers in persisted formats and plan a bounded migration path; register a profile when a transition date becomes binding.

## Acceptance Criteria

- API boundaries §2.2 states the three typed rules, the profile binding, and the example baseline with pinned sources.
- Dependencies §3 points to §2.2 from its bill-of-materials mention.
- Platform Readiness carries one derived prompt.
- The glossary defines cryptographic agility, cryptographic inventory, and post-quantum cryptography.
- The ADR index lists this decision and notes ADR 0022's status is unchanged, and doctrine preflight passes.

## Residual Risk

No cryptographic expert reviewed this. The national-security timeline was not read. Agility has no agreed definition across the sources. The inventory asks for effort ahead of a binding date for most consumers. Model review only.
