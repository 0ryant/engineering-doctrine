# Configuration And Secrets

Durable rules for **non-secret configuration**, **secrets**, **rotation**, and **dynamic settings** so environments stay **reproducible** and **least-privilege**. Complements [build.md](build.md) (surfaces), [dependencies-supply-chain.md](dependencies-supply-chain.md), and umbrella **Configuration And Secrets** in `ENGINEERING.md`. External-profile parameters, approved values, implementation evidence, and exceptions remain bound to the exact authority and revision through [Revision-Pinned External Control Profiles](../patterns/revision-pinned-control-profiles.md).

---

## 1. Separate Config From Secrets

- **Configuration** — feature flags, endpoints, pool sizes, log levels: safe to load from files or env **when** values are not credentials.
- **Secrets** — passwords, API keys, signing keys, client secrets: never treat as normal config; use **secret stores**, **managed identity**, or **short-lived** tokens (OIDC) per estate.

**Why:** The [Twelve-Factor App](https://12factor.net/config) config principle is often misread as “put everything in env”—**credentials** in env on developer laptops and CI logs are a recurring breach class. NIST SSDF **PS** practices expect **protection** of software components including secrets handling (see [NIST SP 800-218](https://csrc.nist.gov/publications/detail/sp/800-218/final)).

---

## 2. Rotation And Lifecycle

- **Rotate** long-lived secrets on a **cadence** and after **personnel** or **incident** events; document **who** triggers rotation and **blast radius**.
- Prefer **automated** rotation where the platform supports it (managed identities, dynamic DB credentials).
- **Version** or **epoch** signing keys when multiple verifiers exist during cutover.

**Why:** Static keys age into **undeletable** debt; rotation without process causes outages—both need explicit design.

---

## 3. Dynamic Configuration And Kill Switches

- **Remote** or **dynamic** config is appropriate for **kill switches** and gradual rollout when the control plane is **authenticated** and **audited**.
- Defaults must be **safe** when the config service is unavailable (fail closed or last-known-good per product policy).

**Why:** Aligns with [collaboration.md](collaboration.md) feature-flag discipline; avoids “redeploy to turn it off” as the only path for user-visible risk.

---

## 4. Local And CI

- **`.env.example`** (or equivalent) lists **names** and **shape**, not values; real secrets never committed.
- CI receives secrets via **OIDC** or **ephemeral** scoped credentials where possible—not permanent org-wide PATs on every fork.

**Why:** Matches **shift security left** expectations in `ENGINEERING.md` and supply-chain hardening in [dependencies-supply-chain.md](dependencies-supply-chain.md).

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Config ≠ secrets | Reduces accidental **exfil** via logs, dumps, and support bundles. |
| Rotation as policy | Meets **organisational** and **regulatory** expectations without naming a single vault product. |

---

## References

- *The Twelve-Factor App* — **Config**: https://12factor.net/config  
- NIST **SP 800-218** (SSDF) — secure development practices including protection of software and environments: https://csrc.nist.gov/publications/detail/sp/800-218/final  
- OWASP — **Secrets Management** (Cheat Sheet): https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html  
