# 0025. Restore Apache-2.0 As The Project Licence

Status: Accepted
Decision date: 2026-07-17
Recorded date: 2026-07-17
Retrospective: No

## Context

Engineering Doctrine is a reference library whose primary adoption mechanics are copying, forking, vendoring, subtrees, submodules, and adaptation into internal handbooks and engineering systems. Its public value depends on making those paths straightforward for individual, enterprise, and commercial consumers.

The `v0.1.0` release used Apache-2.0. Commit `5f6d783` changed the default branch to AGPL-3.0-or-later as an attempt to preserve downstream improvements and create a commercial-licensing boundary. No `v0.2.0` release was subsequently tagged. The repository also retained conflicting Apache-2.0 statements in contribution and doctrine surfaces, so the default-branch licence posture was not consistently represented.

AGPL-3.0-or-later is an open-source licence designed to require source availability for modified network-interactive versions. That protection is useful for some hosted software, but it is poorly aligned with an adoption-first doctrine library and creates review friction for organisations with restrictive copyleft policies. Apache-2.0 permits use, modification, and redistribution while retaining notice requirements and an explicit patent grant.

The maintainer has confirmed that this repository is their work and that no employer or other contributor constraint prevents this additional licence grant.

Evidence:

- Git tag `v0.1.0` and the root licence at that tag establish the original Apache-2.0 release.
- Commit `5f6d783` records the AGPL-3.0-or-later switch.
- [GNU AGPL version 3, section 13](https://www.gnu.org/licenses/agpl-3.0.en.html#section13) states the remote-network source-offer obligation for modified versions.
- [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) states the copyright, redistribution, and patent grants adopted here.
- [Google's published AGPL policy](https://opensource.google/documentation/reference/using/agpl-policy/) is one concrete example of enterprise policy friction; it is evidence of a possible adoption barrier, not a claim that every enterprise follows the same policy.

## Decision

1. Restore **Apache-2.0** as the default licence for the repository.
2. Offer all repository material controlled by the maintainer, including material first published during the AGPL default-branch interval beginning at commit `5f6d783`, under Apache-2.0 from 2026-07-17 onward.
3. Do not revoke or rewrite prior AGPL grants. A recipient who obtained covered material under AGPL may continue to rely on that grant or use the additional Apache-2.0 grant where applicable.
4. Keep the current root `LICENSE` as the single machine-detectable project licence. Preserve the former licence state through Git history and this ADR rather than a competing root licence file.
5. Treat separate hosted products or proprietary tooling as separate licensing decisions. The public doctrine library will not be used as the commercial moat.

## Consequences

### Positive

- Consumers can copy and adapt the library into internal or proprietary systems without copyleft source-disclosure obligations from this project.
- The licence aligns with the repository's stated portability and adoption mechanics.
- Root, contribution, governance, and doctrine licence statements become consistent.
- Apache-2.0's explicit patent grant remains available to consumers.

### Negative

- Downstream users may keep modifications private and are not required to contribute improvements upstream.
- The repository no longer creates a copyleft boundary intended to drive separate commercial licensing.
- Historical AGPL grants remain valid, so the licence history cannot accurately be described as though the AGPL interval never occurred.

## Consumer Impact And Migration

**Change class:** normative replacement; rights-expanding for consumers.

No consumer migration is required. Current and future consumers may use the repository under Apache-2.0. Recipients of material from the AGPL interval retain their AGPL permissions and may use the additional Apache-2.0 grant for material covered by this decision.

Release classification: include this decision in the next `0.x` minor release because licence posture is material even though the change relaxes obligations.

## Verification

- The root `LICENSE` contains Apache License 2.0 and no competing root licence file remains.
- README, CONTRIBUTING, GOVERNANCE, SECURITY, CHANGELOG, doctrine metadata, and explanatory prose do not claim AGPL is the current default.
- `docs/adr/README.md` indexes this decision.
- The doctrine change preflight completes without introducing unrelated changes.
