# Doctrine library change harness

Use this when **adding or substantially changing** content under `doctrine/`, `docs/adr/`, or the umbrella `ENGINEERING.md` in the **engineering-doctrine** repository. It is the maintainer workflow for *trustworthy* additions: **research → decision record (ADR) → layered guidance → navigation updates → verification**.

**Not for:** trivial one-line typos in a single file (use [doctrine-change-checklist.md](../checklists/doctrine-change-checklist.md) only).

**Related:** [doctrine-versioning-and-consumer-compatibility.md](doctrine-versioning-and-consumer-compatibility.md) (change classes, consumer impact), [how-to-read-this-doctrine.md](how-to-read-this-doctrine.md) (layering), [../checklists/doctrine-change-checklist.md](../checklists/doctrine-change-checklist.md) (pre-merge list).

---

## 1. Intake: scope and layer

1. **Name the change** in one sentence (outcome, not file names).
2. **Choose the layer** per [timeless-principles-and-tooling.md](../principles/timeless-principles-and-tooling.md):
   - **Principle** — timeless intent; no vendor SKUs; cite rationale and **references**.
   - **Pattern** — how surfaces fit; may reference examples.
   - **Tooling** — illustrative stack, filenames, bots; **optional** to adopt.
     Do not name organisation-private portfolio implementations; keep those in
     the consuming organisation's private estate documentation.
   - **Estates** — org-specific only: `doctrine/tooling/estates/`.
3. **Classify** per [doctrine-versioning-and-consumer-compatibility.md](doctrine-versioning-and-consumer-compatibility.md): editorial / navigation / additive guidance / normative tightening / replacement / estate-only / deprecation.
4. If the idea does not fit a layer, stop and open an **issue** or **draft PR** (see [CONTRIBUTING.md](../../CONTRIBUTING.md)) before writing thousands of words.

---

## 2. Research (required for additions)

**Additions** (new principle, pattern, checklist, or normative text) need a **researched basis**, not unreferenced opinion.

| Expectation | What to do |
| --- | --- |
| **External grounding** | Point to standards, public frameworks, or widely cited practice in **REFERENCES**-style form (per-doc rationale tables, or [REFERENCES.md](../REFERENCES.md) if first-class). |
| **In-repo research note** (when the change is non-trivial or benchmark-driven) | Add or update a **dated** or titled file under [evolution/](../evolution/) (e.g. `research-*-2026-04.md`, gap analysis) describing sources and conclusions; the ADR links to it. |
| **Honesty** | If evidence is thin, say so and scope the text as *team default* or *example*, not industry law. |

**Editorial** fixes (typos, links) may skip a new research file but should still use the checklist.

---

## 3. ADR (Architecture Decision Record)

**Structural, navigational, or policy-shaping** changes to *this* library get an **ADR** per [docs/adr/README.md](../../docs/adr/README.md).

| Situation | Action |
| --- | --- |
| **No ADR yet** for this decision | **Create** a new `docs/adr/NNNN-short-title.md` (next **number** in sequence; update [docs/adr/README.md](../../docs/adr/README.md) **Index** table). |
| **ADR already exists** and this PR **implements** it | **Reference** that ADR in the PR; update ADR **Status** or add a short **Amendment** section if the implementation refined the decision. |
| **Pure editorial** (typos, formatting) | ADR not required. |
| **New principle/pattern** that does not restructure the repo | Prefer **at least one** ADR that names *why* the library adds this area (or explicitly extends an existing ADR with a new subsection and link). |

**ADR must include (when new):** context, decision, consequences, **evidence** (links, research note path, or commits). For retrospective ADRs, follow the **Honesty rule** in `docs/adr/README.md`.

---

## 4. Author the change (layered, cross-linked)

1. **Principles** — assert durable intent; link outward to **patterns** and **tooling** *where* teams next look for how-to.
2. **Patterns** — link back to **principles**; point to **tooling** for concrete examples; avoid duplicating long normative blocks.
3. **Tooling** — link to **principles** and **patterns**; keep vendor names here, not in principles.
   Public vendor names are allowed only as optional illustrations. Private
   product, repository, and programme names do not belong in any publishable
   layer; describe the capability class instead.
4. **Checklists** — if the addition creates a **new obligation** for adopters, add or extend a checklist under [checklists/](../checklists/); link from the principle/pattern.
5. **Umbrella** — if [ENGINEERING.md](../../ENGINEERING.md) has a one-line index or section for this area, add or update it; do not invent the only copy of a rule in the umbrella (see [doctrine-change-checklist.md](../checklists/doctrine-change-checklist.md)).

**Avoid orphan pages:** every new first-class file should be reachable from [doctrine/README.md](../README.md) **or** a clear hub (e.g. `how-to-read-this-doctrine.md`) and from at least one related sibling doc.

---

## 5. Navigation and discovery (do not ship half-wired)

Run through this table before opening the PR.

| Artifact | When to update |
| --- | --- |
| [doctrine/SITEMAP.md](../SITEMAP.md) | **Always** after add/remove/rename of Markdown under `doctrine/`: run `./scripts/generate-doctrine-sitemap.sh` from the repo root. |
| [glossary.md](../glossary.md) | New **acronyms**, product names, or internal terms that appear in multiple docs. |
| [REFERENCES.md](../REFERENCES.md) | New **first-class** doctrine file, new **standards** citations, or new **Internal doctrine map** row for repo navigability. |
| [doctrine/README.md](../README.md) | **Start Here**, section lists, or topic hubs when a doc should be **discoverable** from the entry point. |
| [patterns/how-to-read-this-doctrine.md](how-to-read-this-doctrine.md) | If reading order or “where to look for X” changes materially. |
| [tldr-principles-and-mvp.md](../tldr-principles-and-mvp.md) | If the **spine** or **MVP** slice should call out this area. |
| [ENGINEERING.md](../../ENGINEERING.md) | If the **umbrella** index should point at the new principle or area. |
| [CHANGELOG.md](../../CHANGELOG.md) | **Material** releases: per [doctrine-versioning](doctrine-versioning-and-consumer-compatibility.md) and [GOVERNANCE.md](../../GOVERNANCE.md) (not every tiny PR). |
| **Related evolution notes** | **Optional:** [evolution/moscow-review.md](../evolution/moscow-review.md) or gap analyses for large shifts. |

---

## 6. Verify

1. Run `./scripts/doctrine-change-preflight.sh` (sitemap + sanity reminders).
2. Re-read [doctrine-change-checklist.md](../checklists/doctrine-change-checklist.md) and check every box that applies.
3. PR description: **change class**, **consumer impact**, **ADR link**, link to **research** note if any.

---

## 7. Agent prompt (copy-paste)

Use this in Cursor / Claude / Codex when tasking an agent to implement a **doctrine addition** in this repository:

```text
You are editing the canonical engineering-doctrine library at ~/prj/engineering-doctrine (or the workspace path).

Task: <describe the addition in one short paragraph>

Follow doctrine/patterns/doctrine-library-change-harness.md in full:

1) Research: Ground the change in external references and/or a committed note under doctrine/evolution/; cite sources in the new/edited doc and REFERENCES.md where appropriate.

2) ADR: If this is a structural or material library decision, create docs/adr/NNNN-<slug>.md (next NNNN) and update docs/adr/README.md index; OR reference an existing ADR and update it if the decision is refined. Skip only for pure editorial fixes.

3) Layering: Place content in principles/ vs patterns/ vs tooling/ per timeless-principles-and-tooling.md. Cross-link principle ↔ pattern ↔ tooling so nothing is an orphan.

4) Navigation: Regenerate doctrine/SITEMAP.md via ./scripts/generate-doctrine-sitemap.sh. Update glossary.md, REFERENCES.md, doctrine/README.md (and ENGINEERING.md / tldr-principles-and-mvp.md / how-to-read-this-doctrine.md if the spine or index should mention this area). Update checklists if adopters have new obligations.

5) Checklist: Complete doctrine/checklists/doctrine-change-checklist.md for this change; label change class and consumer impact for the PR.

6) Run ./scripts/doctrine-change-preflight.sh and fix any issues before claiming done.

Output: a short summary of files changed, ADR number, and change class; no drive-by refactors.
```

---

## 8. Why this harness exists

- **Research** without a paper trail reverts to taste wars.
- **ADRs** make repo-level decisions **auditable** without spelunking chat or git alone.
- **Layering and cross-links** keep principles portable and implementation swappable.
- **SITEMAP, glossary, and REFERENCES** are the **discovery contract**; skipping them makes the library look larger without being easier to use.

For consumer-facing version semantics, see [doctrine-versioning-and-consumer-compatibility.md](doctrine-versioning-and-consumer-compatibility.md).
