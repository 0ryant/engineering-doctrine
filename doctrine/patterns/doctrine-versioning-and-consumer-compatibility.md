# Doctrine Versioning And Consumer Compatibility

This pattern defines how this **doctrine library itself** should communicate change to downstream repos, teams, and estates that copy, fork, subtree, submodule, or cite it.

It complements [semantic-versioning.md](../principles/semantic-versioning.md): that principle governs publishable software units; this file governs a **portable doctrine source** whose public contract is guidance, obligations, examples, and adoption expectations.

---

## 1. What Counts As The Doctrine Contract

For consumers, the contract is not only file contents. It includes:

- **Normative expectations** in `doctrine/principles/` and the umbrella `ENGINEERING.md`.
- **Adoption mechanics** in `patterns/`, `checklists/`, and `tooling/estates/minimum-viable-doctrine.template.md`.
- **Layering rules**: principles stay portable; tooling is illustrative; estates are organisation-specific.
- **Compatibility promises** about whether an update should be safe to absorb without changing a consumer repo's policy, CI gates, or team operating model.

**Why:** Consumers need to know whether an upstream pull is editorial, additive, or policy-changing before they import it into their own repo or programme.

---

## 2. Release Line And Labels

Use **SemVer-shaped tags** for public releases of this library once releases are published:

| Release kind | Meaning for doctrine consumers |
| --- | --- |
| **Patch** (`x.y.Z`) | Editorial fixes, broken links, typos, clarifications, navigation updates, examples that do not change adoption expectations. |
| **Minor** (`x.Y.0`) | New principle, pattern, checklist, tooling illustration, or adoption aid that is **additive** and does not make existing compliant consumers non-compliant. |
| **Major** (`X.0.0`) | A normative shift: changed principle meaning, stricter baseline, removed or renamed doctrine surface, changed layering rule, or new default that can invalidate existing local doctrine. |

Before a formal `1.0.0`, use `0.y.z` with the same intent: **minor** may contain intentional normative movement; **patch** stays safe and compatible.

**Why:** This keeps a familiar upgrade vocabulary without pretending Markdown doctrine has the exact same compatibility surface as a binary package.

---

## 3. Change Classes

Every substantive doctrine change should be labelled in the PR, release note, or evolution entry using one of these classes:

| Class | Examples | Consumer expectation |
| --- | --- | --- |
| **Editorial** | Typos, grammar, formatting, link repairs | Safe to absorb automatically after basic review. |
| **Navigation** | README, sitemap, cross-link, reading-order updates | Safe unless it changes precedence or adoption order. |
| **Additive guidance** | New optional pattern, example, checklist row, reference | Review and adopt when relevant; does not make current practice wrong. |
| **Normative tightening** | New required gate, stronger "must", shorter waiver window, stricter default | Treat as policy change; consumers decide adoption date and exceptions. |
| **Normative replacement** | Old guidance superseded by different default | Requires migration note and consumer impact statement. |
| **Estate-only** | Cloud, vendor, org, regulatory mapping under `tooling/estates/` | Only affected estates need action. |
| **Deprecation** | Planned removal or replacement of a file, rule, or blessed path | Consumers get a target replacement and sunset timing. |

**Why:** Consumers should not have to infer compatibility from diff size. A one-line "must" can matter more than a new 100-line example.

---

## 4. Release Notes Minimum

Each material release or dated release note should include:

- **Summary** — what changed and why.
- **Change class list** — editorial, additive, normative tightening, replacement, estate-only, deprecation.
- **Consumer impact** — who should act: all consumers, only event-driven repos, only AI/RAG systems, only a named estate, etc.
- **Migration notes** — what to do before adopting a normative tightening or replacement.
- **Compatibility statement** — patch / minor / major rationale.
- **Evidence** — links to changed files, references, gap analyses, ADRs, or issue IDs.

**Why:** Doctrine is used to justify work. Release notes should tell adopters what policy conversation they are importing.

---

## 5. Consumer Upgrade Policy

Downstream repos should treat this library like a dependency:

- **Pin** a tag, commit, subtree merge, or submodule revision; do not silently track `main` for policy-sensitive adoption.
- **Record** the chosen import mechanism in the consumer repo's README or local `.doctrine/` entrypoint.
- **Review** minor and major updates for local impact before importing them.
- **Preserve local overrides** in `.doctrine/` or estate supplements; do not edit upstream text in place without noting divergence.
- **Log exceptions** with owner, reason, expiry, and replacement path when local policy intentionally lags upstream.
- **Avoid cherry-picking normative paragraphs** without their rationale and references; that creates orphan rules.

**Why:** Portable doctrine only stays useful when consumers can intentionally absorb updates instead of inheriting surprise policy changes.

---

## 6. Deprecation And Removal

When replacing a doctrine surface:

- Mark the old file, section, or rule as **deprecated** with a link to the replacement.
- State whether the old guidance is still acceptable, discouraged, or invalid.
- Keep redirects or cross-links for at least one minor release where practical.
- Remove only in a **major** release after migration notes exist, unless the old text is actively harmful or insecure.

**Why:** Teams may have embedded links in READMEs, templates, ADRs, onboarding docs, and audit packs.

---

## 7. Dated Evolution Notes Vs Formal Releases

Dated files in `doctrine/evolution/` remain useful for research and audit trails, but they are **not** a substitute for a compatibility signal.

Use dated evolution notes for:

- Gap analyses
- Research synthesis
- MoSCoW backlog changes
- External review summaries

Use release notes or tags for:

- Consumer-facing adoption bundles
- Normative changes
- Deprecations and removals
- Compatibility claims

**Why:** Research says "why we changed"; release policy says "what consumers should do now."

---

## 8. Maintainer Checklist

Before merging a material doctrine change:

```text
[ ] Change class labelled: editorial / navigation / additive / normative tightening / replacement / estate-only / deprecation
[ ] Principle vs tooling vs estate boundary checked
[ ] Consumer impact stated in PR, evolution note, or release note
[ ] Migration notes added for normative tightening, replacement, or removal
[ ] Deprecated surfaces link to replacements
[ ] doctrine/README.md and REFERENCES.md internal map updated if a first-class file was added
[ ] doctrine/SITEMAP.md regenerated after Markdown file changes
[ ] Release kind proposed: patch / minor / major (or 0.x equivalent)
```

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| SemVer-shaped labels | Familiar to consumers and enough to communicate adoption risk. |
| Change classes | Markdown policy risk is semantic; diff size is misleading. |
| Consumer pinning | Prevents surprise policy drift in downstream repos. |
| Dated notes plus releases | Keeps research/audit history separate from upgrade instructions. |
| Deprecation before removal | Protects embedded links and local adoption plans. |

---

## Related

- [how-to-read-this-doctrine.md](how-to-read-this-doctrine.md) — layers, adoption mechanics, conflict resolution.
- [adoption-playbook.md](adoption-playbook.md) — team and org migration toward doctrine.
- [../checklists/doctrine-change-checklist.md](../checklists/doctrine-change-checklist.md) — editing this library.
- [../principles/semantic-versioning.md](../principles/semantic-versioning.md) — SemVer for software artefacts.
