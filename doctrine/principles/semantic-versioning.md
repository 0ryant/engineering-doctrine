# Semantic Versioning Policy

This policy applies to **versioned publishable units**: libraries, packages, container images, versioned APIs, CLIs, desktop or mobile apps, infrastructure modules shipped as artefacts, and any other artefact consumers pin or upgrade **independently**.

It follows **[Semantic Versioning 2.0.0](https://semver.org/)** in spirit: **MAJOR.MINOR.PATCH** communicates risk of upgrade. If the organisation uses **calendar versioning**, **environment-only** tags, or vendor schemes for a given unit, document that exception next to the unit—do not pretend SemVer where it does not apply.

---

## 1. Scope

- **One version line per publishable unit** — not necessarily one version per Git repository. Monorepos may version each package or service independently.
- **Bump only units you materially changed** in that release. Dependent units pick up new versions only when their own code or contract changed.
- **Prefer the smallest bump that honestly describes consumer impact** — avoid vanity bumps (for example “patch number looks too large”) and avoid silent breaking changes in patch releases.

---

## 2. Patch (`x.y.Z`)

Use for **backward-compatible** changes: existing callers, scripts, and operators should keep working without code or config changes.

Typical contents:

- Bug fixes and regression repairs
- Security or reliability hardening that preserves observable behaviour
- Additive behaviour that does not break existing workflows or contracts
- Tests, docs, packaging, or UX refinements that **do not** change compatibility promises
- Performance improvements that do not change guarantees callers rely on

**Batching:** Multiple fixes or small improvements may ship in a **single patch** release when they are released together; do not invent extra patch bumps without a release.

---

## 3. Minor (`x.Y.0`)

Use when the release **adds** something meaningful in a **backward-compatible** way for consumers already on the current major line—or when **pre-1.0** semantics require it (see below).

Typical contents (post-1.0):

- New features, commands, endpoints, or optional capabilities
- Workflow expansions that remain compatible with existing automation
- Deprecations announced with a clear timeline (deprecation itself is usually minor if old paths still work)

**Pre-1.0 (`0.y.z`):** SemVer allows breaking changes during `0.x`. In practice, teams often use **minor** bumps for intentional breaking waves, milestone cuts, or expectation shifts, and **patch** for small compatible fixes—**document the convention** for your product so consumers know how to read `0.x` releases.

---

## 4. Major (`X.0.0`)

Use for **incompatible** changes for consumers of that unit’s public contract: they may need code, config, data migration, or operational changes.

Typical triggers:

- Removing or renaming commands, flags, endpoints, or fields
- Changing API or ABI signatures in ways existing callers cannot ignore
- Wire format, protocol, or serialisation changes that are not backward compatible
- Persisted data, schema, or vault formats that require migration
- **Default behaviour** changes that can break scripts, automation, integrations, or operator runbooks—even if the API shape is unchanged

**Graduating to `1.0.0`:** Move from `0.x` to **`1.0.0`** when core contracts are stable enough that breaking changes are **exceptional and deliberate**, not routine. That is a product and support promise, not only a technical tag.

---

## 5. Pre-release And Build Metadata

Use **pre-release** labels (`1.0.0-alpha.1`, `1.0.0-rc.2`) when consumers need ordering and risk signalling before a stable tag. Use **build metadata** (`+`) only for non-semantics (build IDs); it must not affect precedence per SemVer.

**Channels:** If you publish **multiple** trains (for example `beta`, `rc`, `stable`), document **who** may consume each channel, **promotion** rules between channels, and whether **pinning** to pre-releases is supported for production.

**HTTP API versioning (URL vs header):** There is **no** universal IETF rule—pick **one** approach per product and document it. Common patterns include **path** prefix (`/v1/...`), **`Accept`** header versioning (`Accept: application/vnd.example.v1+json`), or a **custom** header; **RFC 9110** defines `Accept` semantics. Breaking changes should align with **major** bumps for that API surface (or explicit sunset per §8).

---

## 6. Relationship To Contracts

Version bumps align with **contract** changes tracked in schemas, OpenAPI, CLI compatibility docs, and migration guides. A breaking schema or API change for external consumers generally implies a **major** bump for that unit unless the breaking surface is explicitly out of scope (private API only—and that boundary must be documented).

---

## 7. Release Hygiene

- **Single source of truth** for the version string in that unit’s manifest; derive everywhere else (see `ENGINEERING.md` distribution principles).
- **Lockfiles and reproducible builds** updated when dependencies change as part of the release process.
- **Changelog or release notes** reflect what changed and why **minor** or **major** was chosen when it is not obvious from titles alone.
- **Migration notes** ship with majors when operators or developers must act.

---

## 8. Deprecation And Sunset

- **Public** surfaces (API, CLI, event types, configuration keys) need a **documented** deprecation before removal: what is deprecated, **what** replaces it, and **until when** the old path remains available.
- **Notice period** should match blast radius: short for low-adoption internals (with explicit “private” boundary); longer for widespread integrations.
- **Telemetry or usage** signals, where ethical and legal, inform whether anyone still depends on a deprecated path before removal.
- Removal lands in a **major** (post-1.0) or an intentional **pre-1.0** breaking wave—consistent with your published `0.x` policy.
- **Avoid** “deprecated” labels that never get removed; track deprecations like any other engineering debt.

**Why:** SemVer encodes **breaking** change; deprecations are how you **communicate** breaks before the major that removes them—without surprising consumers.

---

## Short Reference

| Bump | Intent |
| --- | --- |
| **Patch** | Backward-compatible fixes and safe additions |
| **Minor** | Meaningful backward-compatible additions; pre-1.0 milestones per team policy |
| **Major** | Breaking changes, or `1.0.0` when the product’s compatibility story stabilises |

When in doubt, **classify by consumer impact**, not by internal refactor size.

---

## References

- **Semantic Versioning 2.0.0**: https://semver.org/  
- **RFC 9110** — HTTP Semantics (`Accept` header): https://www.rfc-editor.org/rfc/rfc9110.html  
- Azure Architecture Center — **RESTful web API design** (versioning discussion): https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#versioning-a-restful-web-api  
