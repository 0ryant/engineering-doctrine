# 0022. Cryptographic Primitives By Purpose

Status: Proposed
Decision date: 2026-05-20
Recorded date: 2026-05-20
Retrospective: No

## Context

Content addressing, digital signatures, message authentication, password
storage, and key derivation solve different problems. Treating them as one
generic “hashing” requirement leads to algorithm confusion, unverifiable
receipts, or unsafe reuse of primitives outside their design purpose.

Portable doctrine should define purpose and migration obligations without
embedding one organisation's product inventory.

## Proposed Decision

Use these defaults where an estate has not adopted a stronger compatible
profile:

| Purpose | Default | Boundary |
| --- | --- | --- |
| Content addressing, hash chains, receipt and file fingerprints | BLAKE3 with a 256-bit output | Domain-separate record types; record algorithm and canonicalisation version. |
| Digital signatures | Ed25519 | Record key identity and trust class; signatures provide integrity/origin only to the extent the trust root is authoritative. |
| Shared-secret message authentication | HMAC-SHA256 | Use only where sender and verifier intentionally share a secret; do not use as a public signature. |

Additional rules:

1. Plain SHA-256 remains acceptable where an external protocol, standard, or
   compatibility contract requires it; label that boundary explicitly.
2. Password storage uses a password-hashing or key-derivation function selected
   by the estate security profile, not any content-addressing primitive above.
3. Every signed or hashed format carries an algorithm identifier and
   canonicalisation/version field.
4. Algorithm migration uses dual-read or versioned verification during a bounded
   transition; never reinterpret an old digest under a new algorithm name.
5. Cryptographic agility is a format and trust-root concern, not permission for
   arbitrary runtime algorithm selection.

## Consequences

- Verifiers can dispatch by explicit purpose and algorithm identifier.
- Cross-language implementations share test vectors and canonical bytes.
- Estates still need key custody, rotation, revocation, and trust-root policy.
- Post-quantum migration and password-storage parameters remain separate
  decisions.

## Consumer Impact

**Change class:** normative replacement of a portfolio inventory with portable
purpose-based guidance. Consumers should inventory formats, record current
algorithms honestly, and migrate only through versioned compatibility plans.

## Verification

- Cross-language test vectors produce identical canonical bytes and digests.
- Signature verification rejects an unknown key identity and tampered payload.
- HMAC verification is not accepted as public-key origin evidence.
- A migration fixture verifies both explicitly versioned old and new records and
  rejects algorithm-name substitution.

## References

- [RFC 8032](https://www.rfc-editor.org/rfc/rfc8032) — Ed25519.
- [RFC 2104](https://www.rfc-editor.org/rfc/rfc2104) — HMAC.
- [FIPS 180-4](https://csrc.nist.gov/pubs/fips/180-4/upd1/final) — SHA-2.
- [BLAKE3 specification](https://github.com/BLAKE3-team/BLAKE3-specs) — BLAKE3.
- [ADR 0027](0027-keep-public-doctrine-implementation-neutral.md).
