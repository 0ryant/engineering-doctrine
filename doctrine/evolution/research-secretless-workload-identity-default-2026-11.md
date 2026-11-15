# Secretless Workload Identity As The Default

Date and source access date: 2026-11-15. Repository basis: `54fd5f39383c081fc62b3ccbae44735069e31201` and the companion change.
Status: research basis for [ADR 0051](../../docs/adr/0051-make-secretless-workload-identity-the-default.md) (accepted 2026-11-15). Model research and model review; no independent human or domain review.

## Question

Should estate-governed and production workloads be required to authenticate with federated or platform-issued short-lived credentials wherever the target supports them, instead of holding stored long-lived secrets?

## Current Doctrine

[Zero trust](../principles/zero-trust-and-workload-identity.md) §2 says workloads **prefer** short-lived, audience-scoped credentials. [Configuration and secrets](../principles/configuration-and-secrets.md) §1 lists secret stores, managed identity, and short-lived tokens as alternatives, and §4 asks for CI federation "where possible". Zero trust §1 already requires a documented exception for shared static service passwords. Nothing makes the secretless path the default, and nothing records why a stored secret exists when federation was available.

The maintainer asked for secretless to be the preferred stance. The [Secretless Workload Identity](../impl/secretless-workload-identity.md) reference can only lead with the owners' existing preference, so a default needs an owner change.

## Source Ledger

Classes follow [Source Authority And Evidence Grading](../patterns/source-authority-and-evidence-grading.md) §2. All primary pages were read by the lead author on the access date (V1). No archive copies were captured.

| Source | Class and scope | Supports | Does not establish |
| --- | --- | --- | --- |
| [AWS IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) | S5, product-scoped; persuasive outside AWS | The provider requires workloads to use temporary credentials through roles, and keeps long-term access keys for workloads that cannot use roles or for third-party clients that lack support | That every target outside AWS supports federation, or any incident-rate effect |
| [Google Cloud: best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys) | S5, product-scoped; persuasive outside Google Cloud | The provider recommends avoiding user-managed keys and treating them "as an exception rather than the norm", with attached identities and workload identity federation as alternatives | A cross-provider standard |
| [IETF WIMSE workload identity practices, draft-08](https://datatracker.ietf.org/doc/draft-ietf-wimse-workload-identity-practices/) | S3, Informational draft awaiting AD go-ahead | Short-lived credentials are recommended when platform credentials are exchanged for access tokens (§5.4); environment variables must not deliver workload identity credentials where the platform offers another pattern (§5.1.4) | A ratified standard; neither statement is admitted as a normative floor here |
| [OWASP Non-Human Identities Top 10, 2025](https://owasp.github.io/www-project-non-human-identities-top-10/2025) | S4 awareness document | Secret leakage (NHI2) and long-lived secrets (NHI7) are ranked risk categories | Mitigation effectiveness; the overview page gives titles only |
| [NIST SP 800-207](https://csrc.nist.gov/publications/detail/sp/800-207/final) (already cited) | S2 | No implicit trust from location; per-request verification | Any credential-lifetime rule |
| [SLSA blog: what SLSA can and cannot do](https://slsa.dev/blog/2026/05/mini-shai-hulud-what-slsa-can-and-cannot-do) | S6, named practitioner; primary for the incident analysis | Counter-evidence: an attacker inside a pipeline used the job's legitimate OIDC identity to produce valid attestations | That federation is unsafe; it shows short-lived tokens can still be stolen at runtime |

The CISA and NSA joint CI/CD guidance already cited in REFERENCES was not retrievable on the access date (HTTP 403), so it is not used here.

## Synthesis

1. **Convergent vendor practice, not a standard.** Two major providers each make temporary workload credentials the default inside their own platforms and keep long-term keys for workloads that cannot use them. The IETF work points the same way but is still a draft. This supports a portable default scoped to targets that support federation. It does not support a ban.
2. **The fallback is legitimate.** Many third-party APIs, webhook senders, and legacy systems accept only static keys. Both providers keep a long-term-key path for this reason. A default that turned every such key into an exception would generate permanent exceptions, which the [exception contract](../patterns/normative-language-applicability-and-exceptions.md#5-exception-contract) treats as a sign the rule is wrong.
3. **Secretless is not risk-free.** Runtime token theft from a compromised job remains possible. Short lifetime and audience scoping bound the damage window; they do not prevent it. Pipeline integrity and provenance verification stay necessary.
4. **The failure being addressed.** Stored long-lived secrets are committed, logged, copied into CI settings, shared across services, and left unrotated. The OWASP list ranks leakage and longevity as distinct risks. A registered fallback makes each remaining secret visible and owned.

## Decision Input

Make the secretless path the default for estate-governed and production workloads, including CI and CD jobs, wherever the target accepts federated or platform-issued identity. A stored secret for such a target becomes an exception. A stored secret for a target that cannot federate stays allowed but is recorded with owner, rotation, blast radius, and the reason federation is unavailable.

Keep out of the normative change:

- the WIMSE environment-variable rule, until it is published as an RFC;
- local development and human access, which have their own paths;
- agent identity specifics, which zero trust §2.1 already governs and which inherit the default.

Admission: **C2 with explicit risk asymmetry.** The sources are product-scoped vendor guidance (S5), a standards draft (S3), and an awareness list (S4). They converge, but none is a portable binding standard. The cost is federation setup and a fallback register; the guarded failure is long-lived credential leakage with wide blast radius.

## Residual Risk

Vendor guidance is persuasive only inside its own products. The default rests on convergence and risk asymmetry, not on measured incident reduction. If the WIMSE draft changes materially before publication, or a credible standard emerges, revisit the scope. A large fallback register would show the default reaching fewer targets than intended.
