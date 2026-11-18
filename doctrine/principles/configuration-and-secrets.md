# Configuration And Secrets

Durable rules for non-secret configuration, secrets, rotation, and dynamic settings so environments stay reproducible and least-privilege. Complements [build.md](build.md) (surfaces), [dependencies-supply-chain.md](dependencies-supply-chain.md), and Core Proposition 7 (Protect Proportionately To Risk) in `ENGINEERING.md`. External-profile parameters, approved values, implementation evidence, and exceptions remain bound to the exact authority and revision through [Revision-Pinned External Control Profiles](../patterns/revision-pinned-control-profiles.md).

For how a workload normally obtains credentials, start with [Secretless Workload Identity](../impl/secretless-workload-identity.md).

---

## 1. Separate Config From Secrets

- **Configuration** — feature flags, endpoints, pool sizes, log levels: safe to load from files or env when values are not credentials.
- **Secrets** — passwords, API keys, signing keys, client secrets: never treat as normal config. Where the target accepts federated or platform identity, workloads use it instead of a stored secret; [zero trust §2](zero-trust-and-workload-identity.md#2-workload-identity) owns that secretless default and its registered fallback. Secret stores hold the fallbacks.
- **SHOULD: bind environment-specific configuration at deploy or start time.** Values that differ between environments are supplied when the artefact is deployed or started, not built into it, so the same built artefact can be promoted ([build.md](build.md) §5). A packaged safe default for when a configuration source is unavailable is compatible with this (§3) ([ADR 0057](../../docs/adr/0057-close-owner-gaps-from-implementation-batch-3.md)).

**Why:** The [Twelve-Factor App](https://12factor.net/config) config principle is often misread as “put everything in env”—credentials in env on developer laptops and CI logs are a recurring breach class. NIST SSDF PS practices expect protection of software components including secrets handling (see [NIST SP 800-218](https://csrc.nist.gov/publications/detail/sp/800-218/final)).

---

## 2. Rotation And Lifecycle

- Rotate long-lived secrets on a cadence and after personnel or incident events; document who triggers rotation and blast radius.
- Prefer automated rotation where the platform supports it (managed identities, dynamic DB credentials).
- Version or epoch signing keys when multiple verifiers exist during cutover.

**Why:** Static keys age into undeletable debt; rotation without process causes outages—both need explicit design.

---

## 3. Dynamic Configuration And Kill Switches

- Remote or dynamic config is appropriate for kill switches and gradual rollout when the control plane is authenticated and audited.
- Defaults must be safe when the config service is unavailable (fail closed or last-known-good per product policy).

**Why:** Aligns with [collaboration.md](collaboration.md) feature-flag discipline; avoids “redeploy to turn it off” as the only path for user-visible risk.

---

## 4. Local And CI

- **`.env.example`** (or equivalent) lists names and shape, not values; real secrets never committed.
- CI and CD jobs follow the secretless default in [zero trust §2](zero-trust-and-workload-identity.md#2-workload-identity): OIDC federation where the target supports it, otherwise ephemeral scoped credentials or a registered fallback—not permanent org-wide PATs on every fork.

**Why:** Matches shift security left expectations in [secure-development-lifecycle.md](secure-development-lifecycle.md) and supply-chain hardening in [dependencies-supply-chain.md](dependencies-supply-chain.md).

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Config ≠ secrets | Reduces accidental exfil via logs, dumps, and support bundles. |
| Rotation as policy | Meets organisational and regulatory expectations without naming a single vault product. |
| Secretless default owned elsewhere | How a workload proves identity belongs to zero trust §2 ([ADR 0051](../../docs/adr/0051-make-secretless-workload-identity-the-default.md)); this file keeps secret handling and points there. |
| Configuration bound at deploy time | Building environment values into an artefact forces a rebuild per environment, so the tested artefact is not the deployed one ([ADR 0057](../../docs/adr/0057-close-owner-gaps-from-implementation-batch-3.md)). |

---

## References

- *The Twelve-Factor App* — Config: https://12factor.net/config  
- NIST SP 800-218 (SSDF) — secure development practices including protection of software and environments: https://csrc.nist.gov/publications/detail/sp/800-218/final  
- OWASP — Secrets Management (Cheat Sheet): https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html  
- *The Twelve-Factor App* — **Build, release, run** (S6; accessed 2026-11-18): https://12factor.net/build-release-run  
- Kubernetes documentation — **ConfigMaps** (environment-specific configuration decoupled from images) (S5; accessed 2026-11-18): https://kubernetes.io/docs/concepts/configuration/configmap/  
- DORA — capability: **deployment automation** (same packages for every environment) (S4; accessed 2026-11-18): https://dora.dev/capabilities/deployment-automation/  
