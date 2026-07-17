# Doctrine library change harness

Use this when **adding or substantially changing** content under `doctrine/`, `docs/adr/`, or the umbrella `ENGINEERING.md` in the **engineering-doctrine** repository. It is the maintainer workflow for *trustworthy* additions: **research → decision record (ADR) → layered guidance → navigation updates → verification**.

**Not for:** trivial one-line typos in a single file (use [doctrine-change-checklist.md](../checklists/doctrine-change-checklist.md) only).

**Related:** [doctrine-versioning-and-consumer-compatibility.md](doctrine-versioning-and-consumer-compatibility.md) (change classes, consumer impact), [normative-language-applicability-and-exceptions.md](normative-language-applicability-and-exceptions.md) (claim strength, scope, and exceptions), [how-to-read-this-doctrine.md](how-to-read-this-doctrine.md) (layering), [../checklists/doctrine-change-checklist.md](../checklists/doctrine-change-checklist.md) (pre-merge list).

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
3. **Classify each material claim** per [normative-language-applicability-and-exceptions.md](normative-language-applicability-and-exceptions.md): normative strength, content class, applicability conditions, expected evidence, and exception authority. Do not assign one normative level to a whole document.
4. **Classify the library change** per [doctrine-versioning-and-consumer-compatibility.md](doctrine-versioning-and-consumer-compatibility.md): editorial / navigation / additive guidance / normative tightening / replacement / estate-only / deprecation. A change to claim strength, applicability, evidence, or the exception path can change consumer obligations even when the prose becomes shorter.
5. If the idea does not fit a layer, stop and open an **issue** or **draft PR** (see [CONTRIBUTING.md](../../CONTRIBUTING.md)) before writing thousands of words.

---

## 2. Research (required for additions)

**Additions** (new principle, pattern, checklist, or normative text) need a **researched basis**, not unreferenced opinion.

| Expectation | What to do |
| --- | --- |
| **External grounding** | Point to standards, public frameworks, or widely cited practice in **REFERENCES**-style form (per-doc rationale tables, or [REFERENCES.md](../REFERENCES.md) if first-class). |
| **In-repo research note** (when the change is non-trivial or benchmark-driven) | Add or update a **dated** or titled file under [evolution/](../evolution/) (e.g. `research-*-2026-04.md`, gap analysis) describing sources and conclusions; the ADR links to it. |
| **Source authority and limits** | Distinguish binding external requirements, official guidance, observations, and this library's synthesis. Record the revision or retrieval date where drift matters, and say what a source does **not** establish. |
| **Honesty** | If evidence is thin, say so and scope the text as contextual guidance or an example, not industry law. Repository precedent can explain consistency; it cannot be the sole external grounding for a new portable control. |

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

**ADR must include (when new):** context, decision, alternatives considered, consequences, **evidence** (links or a research-note path), consumer impact and migration, acceptance criteria or measures, and residual risk. For retrospective ADRs, follow the **Honesty rule** in `docs/adr/README.md`.

---

## 4. Author the change (layered, cross-linked)

1. **Principles** — assert durable intent; link outward to **patterns** and **tooling** *where* teams next look for how-to.
2. **Patterns** — link back to **principles**; point to **tooling** for concrete examples; avoid duplicating long normative blocks.
3. **Tooling** — link to **principles** and **patterns**; keep vendor names here, not in principles.
   Public vendor names are allowed only as optional illustrations. Private
   product, repository, and programme names do not belong in any publishable
   layer; describe the capability class instead.
4. **Material claims** — state strength and content class at claim level; define who or what they apply to, what evidence demonstrates the outcome, and which authority can decide an exception. Keep an exception separate from the underlying rule and evidence verdict.
5. **Controls** — for a new or materially expanded control, name the failure it addresses, expected evidence, accountable owner, operating cost, review trigger, and how the control can be simplified or retired. Prefer an outcome and bounded choice over one universal mechanism where context legitimately differs.
6. **Checklists** — derive review prompts from the owning principle or pattern. If the addition creates a new obligation, add or extend a checklist under [checklists/](../checklists/) and link to the authority; do not make the checklist the only place the obligation exists.
7. **Umbrella** — keep [ENGINEERING.md](../../ENGINEERING.md) a compact constitution and route map. It may own core propositions and vocabulary, but detailed topic obligations have one canonical principle or pattern owner and are linked rather than copied.

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
3. Sample at least three materially different consumers or change classes. Confirm that applicability composition activates the intended controls without making every profile universal.
4. Search for duplicate normative owners and conflicting strength, scope, or exception wording. Treat contradictions as defects; do not resolve them by selecting the convenient copy.
5. Confirm cited sources support the claims attributed to them, exceptions do not rewrite failed or inconclusive evidence, and new controls have an accountable review and retirement path.
6. PR description: **change class**, **consumer impact**, **ADR link**, link to **research** note if any, and any residual verification limits.

---

## 7. Agent prompt (copy-paste)

Use this in Cursor / Claude / Codex when tasking an agent to implement a **doctrine addition** in this repository:

```text
You are editing the canonical engineering-doctrine library at ~/prj/engineering-doctrine (or the workspace path).

Task: <describe the addition in one short paragraph>

Follow doctrine/patterns/doctrine-library-change-harness.md in full:

1) Research: Ground the change in authoritative external references and a committed note under doctrine/evolution/ when the decision is non-trivial. Distinguish binding requirements, guidance, observations, and repository synthesis; record source limits.

2) ADR: If this is a structural or material library decision, create docs/adr/NNNN-<slug>.md (next NNNN) and update docs/adr/README.md index; OR reference an existing ADR and update it if the decision is refined. Include alternatives, consequences, consumer impact, acceptance measures, and residual risk. Skip only for pure editorial fixes.

3) Authority and layering: Place content in principles/ vs patterns/ vs tooling/ per timeless-principles-and-tooling.md. For every material claim, classify strength, content class, applicability, expected evidence, and exception authority per normative-language-applicability-and-exceptions.md. Cross-link principle ↔ pattern ↔ tooling; keep one canonical owner for detailed obligations.

4) Navigation: Regenerate doctrine/SITEMAP.md via ./scripts/generate-doctrine-sitemap.sh. Update glossary.md, REFERENCES.md, doctrine/README.md (and ENGINEERING.md / tldr-principles-and-mvp.md / how-to-read-this-doctrine.md if the spine or index should mention this area). Update checklists if adopters have new obligations.

5) Checklist: Complete doctrine/checklists/doctrine-change-checklist.md for this change; label change class and consumer impact for the PR. For a new control, document the failure addressed, evidence, owner, operating cost, review trigger, and simplification or retirement path.

6) Run ./scripts/doctrine-change-preflight.sh and fix any issues before claiming done.

Output: a short summary of files changed, ADR number, and change class; no drive-by refactors.
```

---

## 8. Why this harness exists

- **Research** without a paper trail reverts to taste wars.
- **ADRs** make repo-level decisions **auditable** without spelunking chat or git alone.
- **Claim-level strength and applicability** prevent a useful profile from becoming a universal burden.
- **Explicit exception and control-lifecycle rules** preserve evidence while making justified variance reviewable and temporary.
- **Layering, canonical ownership, and cross-links** keep principles portable and implementation swappable without duplicate authority.
- **SITEMAP, glossary, and REFERENCES** are the **discovery contract**; skipping them makes the library look larger without being easier to use.

For consumer-facing version semantics, see [doctrine-versioning-and-consumer-compatibility.md](doctrine-versioning-and-consumer-compatibility.md).
