# ADR 0061: Execute The First Exits And Settle How An Exit Is Carried Out

- **Status:** Proposed
- **Decision date:** pending operator acceptance
- **Recorded date:** 2026-11-20
- **Retrospective:** No
- **Deciders:** Repository operator
- **Review provenance:** Decided item by item on 2026-11-20 by a model council at the operator's instruction, and by the operator himself where a decision says so; drafted and reviewed by models of one family; no independent human or domain review recorded
- **Research:** [Decision council, November 2026](../../doctrine/evolution/research-v080-decision-council-2026-11.md)
- **Canonical owner:** [Doctrine Content Lifecycle](../../doctrine/maintainers/doctrine-content-lifecycle.md) §4 (banner template) and §5 (repointing; exit-banner form). It binds maintainers only; no consumer rule changes
- **Derived landings:** the three exiting files ([flag pattern](../../doctrine/patterns/feature-flag-lifecycle.md), [AWS stub](../../doctrine/tooling/estates/aws-container-runtimes.md), [GCP stub](../../doctrine/tooling/estates/gcp-container-runtimes.md)); the [lifecycle register](../../doctrine/DEPRECATED.md) and [evidence exception register](../../doctrine/EVIDENCE-EXCEPTIONS.md); a dated note on [ADR 0045](0045-execute-the-first-lifecycle-sweep.md); the [doctrine README](../../doctrine/README.md), [references map](../../doctrine/REFERENCES.md), and [estates README](../../doctrine/tooling/estates/README.md); `scripts/check-principles-glance.sh` and a new test; the `v0.8.0` sweep record; a pointer line in two August research notes ([target state](../../doctrine/evolution/research-target-state-and-irreversible-decisions-2026-08.md), [source authority](../../doctrine/evolution/research-source-authority-and-evidence-weighting-2026-08.md)); the changelog, sitemap, and ADR index
- **Relationship to earlier decisions:** executes the exits ADR 0045 declared and clarifies its decision 3; first removal under [ADR 0038](0038-adopt-a-doctrine-content-lifecycle.md); reads lifecycle §5 as [ADR 0047](0047-separate-maintainer-doctrine-and-collapse-the-ai-native-sdlc.md) D5 does; settles the banner form the `v0.6.2` notes left open; discharges EX-0001 ([ADR 0040](0040-adopt-source-authority-classes-and-evidence-weighted-citations.md)); depends on ADR 0064 for one schema value

## Context

ADR 0045 deprecated three files at `v0.5.0`. Under the [lifecycle pattern](../../doctrine/maintainers/doctrine-content-lifecycle.md) a deprecated file later exits: its path stays and holds only a banner, called a tombstone. An exit is Superseded when a named successor replaced the file, and Retired when nothing did.

No file has exited yet. `v0.8.0` is the first release that can carry an exit, and preparing it showed five points the texts leave open. A model council decided them on 2026-11-20, in eight votes, each 5 to 0. This record carries those decisions; the edits follow in the release change, after acceptance.

## Decision

### What the operator is accepting

1. The three files deprecated at `v0.5.0` become tombstones at `v0.8.0`, tagged no earlier than 2026-12-14T09:38:16Z.
2. The AWS and GCP stubs exit as Retired, and a dated note on ADR 0045 says so.
3. The form the six live banners use becomes the banner form; the template is amended and exit banners follow it.
4. At an exit, links are repointed in live files only; ADRs, evolution notes, and the changelog keep theirs.
5. Evidence exception EX-0001 is discharged at the `v0.8.0` sweep by recording archive links; addresses with none are recorded as unrecoverable.
6. The archive link used is the copy nearest the citation's access date, flagged when captured after admission.

### For the operator to confirm

These six points were not voted on their own.

- The guard script learns the exit words, with a test that can fail, as the council's review asked. [GOV-14]
- Lifecycle §5 gains one sentence that writes down the exit banner's form.
- Where an exit has no successor, a live link to it is removed.
- Every archive row shows its capture date, early or late.
- A fresh capture is requested from a public archive only with his go-ahead.
- Archive links go in the sweep record, with one pointer line in each note. The notes' source tables are not edited.

### D1. The three files deprecated at `v0.5.0` exit at `v0.8.0`

**Question.** Whether `v0.8.0` turns the three deprecated files into tombstones or keeps them for another release.

**Text now.** [Lifecycle §4](../../doctrine/maintainers/doctrine-content-lifecycle.md#4-deprecation-mechanics): "every dying-table entry past its 90-day floor MUST receive a recorded keep-or-execute verdict at each §8 sweep".

**Decision.** All three exit. `feature-flag-lifecycle.md` (1,762 words) is Superseded by [feature-flag-governance.md](../../doctrine/patterns/feature-flag-governance.md). The two stubs (153 and 148 words) are Retired (D2). The sweep records "execute" for each.

The earliest tag time is 2026-12-14T09:38:16Z, from ADR 0045's clarification of 2026-09-19. Checked on 2026-11-20: the `v0.5.0` tag object reads 2026-09-15T10:38:16+01:00, and that moment is 90 days later. Lifecycle §4 says removal "MUST NOT ship earlier".

No further ADR is needed. ADR 0045 named each target, replacement, and exit, as lifecycle §4 asks. Sections 4 to 6 then ask only for release work: a recorded verdict, the tombstone, and the register row moved.

**Proposed edit.** Replace each file's content with its title line and the banner in D3. Move its register row to the table of executed exits, with the exit state, a one-line rationale, both ADRs, and `v0.8.0`. Rewrite the register's closing paragraph, which opens "Nothing has yet been retired."

**Who decided.** Council, 5 to 0 on each file; awaits the operator's acceptance.

**Change class.** No class in [versioning §3](../../doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md) fits, and no release note has labelled an executed exit. Versioning §7 says "removals"; that label is proposed.

**Consumer impact.** Links to the old flag pattern still resolve and land on the tombstone. Cite the replacement; its §10 maps old sections to new. The stubs held no guidance. Pins at `v0.7.0` or earlier see no change.

### D2. The two estate stubs exit as Retired

**Question.** ADR 0045 calls the stubs "retired" and also names a "replacement". A tombstone carries one exit state.

**Text now.** ADR 0045 decision 3: "The AWS and GCP estate stubs are retired, not filled." and "Their replacement is TEMPLATE.md". Lifecycle §1 says the exit states "MUST NOT be collapsed into one label".

**Decision.** Both exit as Retired. The tombstone names no successor and may say where to start. [TEMPLATE.md](../../doctrine/tooling/estates/TEMPLATE.md) is a blank form added in the same commit as the stubs, and nothing moved into it.

**Proposed edit.** On acceptance, append this to ADR 0045, with the acceptance date in its heading:

```text
## Clarification (YYYY-MM-DD): Exit State Of The Estate Stubs

Decision 3 says the AWS and GCP estate stubs "are retired, not filled". It
also says "Their replacement is TEMPLATE.md". Read against
[lifecycle §1](../../doctrine/maintainers/doctrine-content-lifecycle.md#1-lifecycle-states),
the two phrases point at different exit states: Retired means no successor,
and Superseded means replaced by a named successor.

The exit state of both stubs is Retired. "Replacement" in decision 3 answers
what [lifecycle §4](../../doctrine/maintainers/doctrine-content-lifecycle.md#4-deprecation-mechanics)
asks of every deprecation: name an Active replacement, or say that none is
required. It tells a reader where to start instead. It does not make
TEMPLATE.md a successor. The template was added in the same commit as the
stubs, it is a blank form, and nothing from the stubs moved into it.

Each tombstone therefore reads Retired and names no successor. It may still
tell a reader to start a new supplement from TEMPLATE.md. The register's
tombstone rows record Retired.

This is a clarification, recorded by
[ADR 0061](0061-execute-the-first-exits-and-settle-how-an-exit-is-carried-out.md).
It makes no new lifecycle decision and changes no status: decision 3 already
said "retired". The original decision text remains as history.
```

**Who decided.** Council, 5 to 0; awaits the operator's acceptance.

**Change class.** None in versioning §3 fits. The `v0.7.0` notes used "clarification".

**Consumer impact.** None.

### D3. One banner form, and the three exit banners

**Question.** The lifecycle pattern prints one banner template; the six live banners use another form. This decides which stands and what an exit banner says.

**Text now.** The lifecycle §4 template opens `> **Status: Deprecated**` and ends "This text remains accurate at every tag in which it ships." Live banners open `> **Deprecated since v0.5.0**` and lack that sentence. The `v0.6.2` release notes say "which is canonical is left open".

**Decision.** The live form stands. The template is amended to match, and no live banner is restamped. The template's last sentence is dropped and added to no banner; [versioning §6](../../doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md#6-deprecation-and-removal) keeps its promise for consumers. An exit banner uses the same form, with the exit state and the exit release.

**Proposed edit.** In lifecycle §4, replace the three template lines with:

```text
> **Deprecated since v<X.Y.Z>** ([ADR <NNNN>](<ADR link>)): this file is superseded by
> <replacement link> (or: this file is retiring, followed by where to start instead, or by
> "no replacement is required"). Earliest removal: the first minor release cut at least
> 90 days after v<X.Y.Z>, per [lifecycle §4](<link to this section>); this floor does not
> trigger automatic removal. <One instruction to the reader, such as "Cite the replacement.">
```

In lifecycle §5, after "The full text remains reachable at any pinned tag.", add:

```text
The exit banner uses the form of the deprecation banner in §4. It opens `> **Superseded since v<X.Y.Z>**`, `> **Retired since v<X.Y.Z>**`, or `> **Rescinded since v<X.Y.Z>**`, where the version is the release that executes the exit.
```

The whole content of `doctrine/patterns/feature-flag-lifecycle.md`:

```text
# Feature Flag Lifecycle

> **Superseded since v0.8.0** ([ADR 0045](../../docs/adr/0045-execute-the-first-lifecycle-sweep.md)): this file is superseded by [feature-flag-governance.md](feature-flag-governance.md). The full text last shipped at v0.7.0 and stays readable at that tag. Cite the replacement.
```

Of `doctrine/tooling/estates/aws-container-runtimes.md`:

```text
# Supplement: AWS Container Runtimes (Stub Estate)

> **Retired since v0.8.0** ([ADR 0045](../../../docs/adr/0045-execute-the-first-lifecycle-sweep.md)): this stub was a placeholder with no guidance, and it has no successor. The full text last shipped at v0.7.0 and stays readable at that tag. To write an estate supplement, start from [TEMPLATE.md](TEMPLATE.md).
```

Of `doctrine/tooling/estates/gcp-container-runtimes.md`:

```text
# Supplement: GCP Container Runtimes (Stub Estate)

> **Retired since v0.8.0** ([ADR 0045](../../../docs/adr/0045-execute-the-first-lifecycle-sweep.md)): this stub was a placeholder with no guidance, and it has no successor. The full text last shipped at v0.7.0 and stays readable at that tag. To write an estate supplement, start from [TEMPLATE.md](TEMPLATE.md).
```

If a tag is cut between `v0.7.0` and `v0.8.0`, the banners name it. In `scripts/check-principles-glance.sh`, line 30, replace `^> \*\*deprecated` with `^> \*\*(deprecated|superseded|retired|rescinded)`, and add `scripts/tests/test_principles_glance.py`.

**Who decided.** Council, 5 to 0; awaits the operator's acceptance.

**Change class.** None in versioning §3 fits. The `v0.7.0` notes used "clarification" and "maintainer tooling".

**Consumer impact.** None. The navigation pack's check already matches these banners; no pack version changes.

### D4. At an exit, links are repointed in live files only

**Question.** Which links to a new tombstone are changed in the same change.

**Text now.** [Lifecycle §5](../../doctrine/maintainers/doctrine-content-lifecycle.md#5-removal-stamping-and-restoration): "Inbound links inside the corpus MUST be repointed in the same change". ADR 0047 D5: "ADRs, evolution notes, and the changelog are records: they keep their old links".

**Decision.** Live files only. A record is a file under `docs/adr/` or `doctrine/evolution/`, or the changelog. It keeps its links, which then land on the tombstone.

**Proposed edit.** In that lifecycle §5 sentence, replace "inside the corpus" with "in live files". Add after it:

```text
A live file is any file that is not a record. ADRs, evolution notes, and the changelog are records: they keep their links, which then land on the tombstone. The register and the generated sitemap list the exited path itself and keep it. Where the exit names no successor, a live link is removed.
```

Links today, counted on 2026-11-20 by resolving every Markdown link in tracked files:

| Exiting path | Live files, one link each | Register and sitemap | Record files (links) |
| --- | --- | --- | --- |
| `feature-flag-lifecycle.md` | None | 2 | 6 (11) |
| `aws-container-runtimes.md` | `doctrine/README.md`, `doctrine/REFERENCES.md`, `doctrine/tooling/estates/README.md` | 2 | 4 (4) |
| `gcp-container-runtimes.md` | The same three | 2 | 4 (4) |

The release change removes the six stub entries from those three files. The flag pattern needs one plain-text edit: in `doctrine/README.md`, "deprecated since v0.5.0" becomes "superseded at v0.8.0".

**Who decided.** Council, 5 to 0; awaits the operator's acceptance.

**Change class.** None in versioning §3 fits. The label is "clarification"; the release note adds that it narrows the widest reading of a typed maintainer duty.

**Consumer impact.** None. Consumers' own links keep resolving.

### D5. Evidence exception EX-0001 is discharged at the `v0.8.0` sweep

**Question.** [Source grading §6](../../doctrine/maintainers/source-authority-and-evidence-grading.md#6-citation-metadata-and-temporal-discipline) asks for an archived copy of a cited page at admission. Two August research notes have none, and were admitted under a time-limited exception, EX-0001. This decides whether it is discharged, renewed, or left to expire.

**Text now.** The [evidence exception register](../../doctrine/EVIDENCE-EXCEPTIONS.md) sets the expiry: "2027-02-12, or discharge at the first sweep that captures archives for still-reachable ledger rows, whichever first". On expiry, "the claim loses its typed standing or the citation is removed". The operator is the approver.

**Decision.** Discharge. The sweep looks up an archived copy for each of the 60 web addresses in the two notes' source tables, under D6. An address with no copy is recorded as unrecoverable, with the reason. The entry then moves to the discharged table.

Expiry would take citations out of two research records, or strip typed standing from claims that lean on them. Source grading §8 names where repeated renewal ends: "Permanent downref".

**Proposed edit.** The sweep record carries one row per address: note (`source-authority` or `target-state`), source rows, address, access date, archive link, capture date, flag. The register row moves to the discharged table, with the date, the counts, and a link to that record. Each note gains one dated pointer line.

**Who decided.** Council, 5 to 0; awaits the operator's acceptance.

**Change class.** None in versioning §3 fits. The `v0.6.0` notes used "evidence only".

**Consumer impact.** None.

### D6. Which archived copy counts

**Question.** A lookup made months later returns copies crawled at other times. This decides which may stand behind a citation read on 2026-08-12.

**Text now.** Source grading §6: "durability is created at citation time, never later". No text says which copy counts after admission. The Internet Archive's [help page](https://archive.org/help/wayback_api.php), read on 2026-11-20, says its lookup "just returns a single closest snapshot". Three lookups that day, asking for 2026-08-12, returned copies dated 2026-07-22, 2026-02-26, and 2024-10-21.

**Decision.** The copy nearest the citation's recorded access date, with its capture date shown. A capture later than admission, 2026-08-12 for both notes, is flagged. Where no copy exists, a fresh capture is the fallback, also flagged. Where neither is possible, the address is unrecoverable. Source grading §6 is unchanged.

**Proposed edit.** No rule file changes. The sweep record states the rule above its table.

**Who decided.** Council, 5 to 0; awaits the operator's acceptance.

**Change class.** As D5.

**Consumer impact.** None.

### What the release depends on

- The tool contract, `contracts/doctrine-tool-contract.v1.schema.json`, lists the statuses a tool server may report: `["active", "deprecated", "retired", "proposed"]`. None fits a Superseded exit. [ADR 0064](0064-settle-the-librarys-own-rules-records-and-tool-contract.md) adds one. The old flag pattern's exit ships in the same release as that change, and waits if it does not land.
- The ADR 0045 note and the amended template land before the first register row is written.

### What needs the operator in person

Accept this record. Cut the `v0.8.0` tag. Approve the discharge of EX-0001 as its named approver, including the addresses recorded as unrecoverable.

## Control Cost And Lifecycle

- D1 ends three deprecations that otherwise need a verdict at every sweep. Cost: one change.
- D2 stops a tombstone saying content moved. Cost: none. Review if `TEMPLATE.md` moves.
- D3 leaves one banner form. Cost: one template edit, one script line.
- D4 keeps records unedited at every exit. Cost: three live files edited now.
- D5 and D6 close an exception before it expires. Cost: about 60 lookups, once.
- Retirement: each decision is reversible by ADR; lifecycle §5 covers restoring a file.

## Alternatives Considered

- **Keep the files Deprecated.** Not taken. Each sweep would owe a keep verdict with no reason to give.
- **Stubs Superseded by the template.** Not taken. It tells readers guidance moved, and none did.
- **The template's form, or both forms.** Not taken. One restamps six banners. The other leaves two forms for every guard and test.
- **Repoint links in records too.** Not taken. It changes what an accepted record appears to cite.
- **Renew EX-0001, or accept any archived copy, or only a fresh one.** Not taken. Renewal defers the work. Any copy may be years from the read. A fresh one shows the page months later.

## Consumer Impact And Migration

Change class: none of the seven in versioning §3 fits. Proposed release-note labels: **removal** (D1), **clarification** (D2 to D4), **maintainer tooling** (the guard), **evidence only** (D5, D6). ADR 0064 would add the first three to §3. Compatibility: pre-1.0 minor.

Migration: as D1. A tool server reports the new status once ADR 0064 lands.

## Acceptance Criteria

Run from the repository root at the `v0.8.0` tag, after preflight and the link check pass. Each fails today.

1. `test "$(git for-each-ref --format='%(taggerdate:unix)' refs/tags/v0.8.0)" -ge 1797241096` succeeds (the floor).
2. For each of the three files, `grep -cv '^[[:space:]]*$'` prints `2` and `grep -cE '^> \*\*(Superseded|Retired) since v0\.8\.0\*\* '` prints `1`.
3. `git grep -lE '\]\([^)]*(feature-flag-lifecycle|aws-container-runtimes|gcp-container-runtimes)\.md' -- '*.md' ':!docs/adr' ':!doctrine/evolution' ':!CHANGELOG.md'` prints only `doctrine/DEPRECATED.md` and `doctrine/SITEMAP.md`.
4. In `doctrine/DEPRECATED.md`, `grep -c '| Superseded | v0\.5\.0 |'` prints `1` and `grep -c '| Retired | v0\.5\.0 |'` prints `2`.
5. `grep -c 'Exit State Of The Estate Stubs' docs/adr/0045-execute-the-first-lifecycle-sweep.md` prints `1`. In the lifecycle pattern, `grep -c 'Status: Deprecated'` prints `0` and `grep -c 'Inbound links in live files'` prints `1`.
6. `grep -cF '(deprecated|superseded|retired|rescinded)' scripts/check-principles-glance.sh` prints `1`, and the unit tests pass with the new test, which fails with "active principle files with no glance row" when the old pattern is restored.
7. `grep -c '"superseded"' contracts/doctrine-tool-contract.v1.schema.json` prints `1` or more.
8. `awk '/^## Discharged/{t=1} t' doctrine/EVIDENCE-EXCEPTIONS.md | grep -c '^| EX-0001 '` prints `1`, and `grep -cE '^\| (source-authority|target-state) \|' doctrine/evolution/sweep-*.md` shows `60` for the new record.

## Residual Risk

- These are the library's first exits. A dry run on a branch is prudent.
- The guard change is tested on a fixture only; no principle file exits here.
- A consumer's link into a section of the old flag pattern lands on a tombstone with no sections.
- D6 rests on one help page and three lookups. One nearest copy was almost 22 months early, and nobody has checked that quoted sentences are in the copies.
- If the release slips past 2027-02-11, the discharge runs on its own or EX-0001 lapses.
- Council and drafter are models of one family. Their unanimity is not independent evidence, and no human or domain review is recorded.
