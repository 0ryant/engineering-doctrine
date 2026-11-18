# ADR 0060: Name Only Open-Source Gate Tools Usable Without A Paid Plan

- **Status:** Accepted
- **Decision date:** 2026-11-18
- **Recorded date:** 2026-11-18
- **Retrospective:** No
- **Deciders:** Repository operator
- **Review provenance:** Operator-directed (the selection rule, the separate table for licences other than Apache-2.0 and MIT, coverage beyond the maintainer's own languages, and the exception in D6 are his) and operator-accepted on 2026-11-18; drafted and reviewed by a model, no independent human or domain review recorded
- **Research:** [Scanner tooling map](../../doctrine/evolution/research-scanner-tooling-map-2026-11.md)
- **Canonical owner:** none changes. The rules scanners serve stay with their owners: [Build](../../doctrine/principles/build.md) §10, [Dependencies And Supply Chain](../../doctrine/principles/dependencies-supply-chain.md) §§2 to 7, [Merge Path](../../doctrine/principles/merge-path-evidence-and-pipeline-integrity.md) §2, [Testing Strategy](../../doctrine/principles/testing-strategy.md) §§5 and 6
- **Derived landings:** new tooling page [Scanners And Quality Gates](../../doctrine/tooling/scanners-and-quality-gates.md); a pointer from the [control suite](../../doctrine/tooling/merge-path-and-pipeline-control-suite.md) §1; one sentence reworded in [dependency automation](../../doctrine/tooling/dependency-automation.md); pointers from the five implementation references that describe a quality gate ([CI/CD delivery](../../doctrine/impl/cicd-delivery.md), [testing and verification](../../doctrine/impl/testing-and-verification.md), [Git hooks](../../doctrine/impl/git-hooks.md), [dependency adoption](../../doctrine/impl/dependency-adoption.md), [infrastructure delivery](../../doctrine/impl/infrastructure-delivery.md)); a semantic-index route

- **Relationship to earlier decisions:** D6 is a narrow, disclosed exception to decision 1 of [ADR 0027](0027-keep-public-doctrine-implementation-neutral.md), which bars naming the maintainer's portfolio tools.

## Context

The library names scanner classes in its rules and maps them to categories of tool in the control suite page. It names almost no tools. A reader who accepts "secret scanning on every merge path" still has to work out which scanner, what it costs, and whether its licence is acceptable to their employer.

The maintainer set three conditions for closing that gap:

1. A tool the library offers must be open source and usable in an enterprise without incurring cost.
2. Tools under Apache-2.0 or MIT are listed first; tools under any other open-source licence go in a separate table.
3. The map must not be biased to the maintainer's own languages. It should cover any language an enterprise estate is likely to hold.

Checking 137 projects against those conditions showed two things worth a rule. Licences are not what memory says: one widely used fuzzer now carries a network-copyleft licence, and several familiar tools are no longer open source. And an open-source tool can ship with a companion that is not free for private code.

## Decision

### D1. Selection rule for gate tools the library names

A scanner or quality-gate tool is offered as an option in the tooling layer only if both hold:

- it carries an open-source licence; and
- it can run on a private, commercial codebase without a paid plan or a licence key.

The rule covers scanners and quality-gate tools. It does not cover the hosts, platforms, brokers, and observability products that other tooling pages use as worked examples.

### D2. Presentation

- Tools under Apache-2.0 or MIT, including dual licences and the MIT-0 and LLVM-exception variants, are listed first.
- Tools under any other open-source licence are listed in a separate table with the licence named and a family label (permissive, weak copyleft, strong copyleft, network copyleft).
- A companion that needs a paid plan, or carries terms that are not open source, is listed in its own table so that the open-source tool beside it is not mistaken for it.
- Tools that fail D1 are named once, under "not offered", with the reason.

The library classifies licences. It does not interpret their obligations; an adopting organisation's own licence policy decides.

### D3. Coverage

The page lists cross-language tools first, then per-language tools for Rust, Java and Kotlin, JavaScript and TypeScript, Python, Go, C# and .NET, C and C++, Ruby, PHP, and Swift, with shell, SQL, YAML, container, and infrastructure formats covered by the cross-language and other-licence tables. An empty cell is left empty.

### D4. Dated facts

Licences and plan terms are stated with the date they were read. The page sits in a fading layer, so each lifecycle sweep re-reads them; a licence change moves or removes a row.

### D5. One existing sentence

[Dependency automation](../../doctrine/tooling/dependency-automation.md) named two commercial products as licence-check examples. That sentence now points to the new page.

### D6. One disclosed exception to the portability boundary

[ADR 0027](0027-keep-public-doctrine-implementation-neutral.md) bars naming the maintainer's own portfolio tools in the library and asks for the capability to be stated generically. One such tool is named: **taudit**, a scanner for the authority that CI/CD pipelines hold (secrets, identities, trust boundaries).

- It is named because it is public, open source, and meets D1, the same test every other tool on the page passed. The maintainer relicensed it from AGPL-3.0-or-later to MIT on 2026-11-18.
- It is listed last in the pipeline-definitions row of the first table, and the page states that the library's maintainer wrote it.
- Its GitHub Action wrapper has no licence file, so the wrapper is listed under other terms and not offered.
- The exception covers the tooling page, this ADR, and the research note's ledger. No other portfolio tool is named, no principle, pattern, or checklist names this one, and ADR 0027 otherwise stands.

## Control Cost And Lifecycle

| Decision | Failure addressed | Evidence | Operating cost | Review trigger |
| --- | --- | --- | --- | --- |
| D1, D2 | A reader adopts a tool the library named and meets a licence their employer bars, or a bill | The licence and plan terms recorded per tool in the research note | Re-reading about 137 repositories at each sweep; a script does the licence lookup | A listed tool changes licence or pricing |
| D3 | Guidance that only fits one language stack | Per-language table with stated gaps | Upkeep grows with each language added | A language in real use has no row |
| D6 | A reader takes the maintainer's own tool for a neutral recommendation | The disclosure sentence on the page | None | Any further portfolio tool proposed for the page; that needs its own decision |
| D4 | Stale licence facts presented as current | The date on the page and the sweep record | Part of the existing sweep | A sweep finds a changed licence |

Retirement: the page can be removed without touching any rule. If upkeep proves too costly, shrink it to the cross-language table.

## Alternatives Considered

- **Apache-2.0 and MIT only.** The first proposal. Relaxed by the maintainer: it would exclude the standard shell and YAML linters, the common JVM analysers, and every general multi-language static analyser.
- **Keep categories only, name no tools.** The position before this ADR. It leaves each adopter to repeat the licence and cost checks.
- **Name any popular tool, including commercial ones.** Rejected: the stated need is use in an enterprise without cost.
- **Mark which tools the maintainer runs.** Not done. It would publish detail of private repositories. The private inventory informed the candidate list and stays out of the library.
- **Keep the maintainer's own scanner out, as ADR 0027 would.** The first draft did. The maintainer chose to list it, with the interest disclosed.
- **Interpret licence obligations for the reader.** Rejected. The library is not a source of legal advice, and organisations differ.

## Consumer Impact And Migration

Change class: **additive guidance**. No obligation is added or changed. Consumers gain an optional map from control classes to tools.

Migration: none.

## Acceptance Criteria

- The tooling page lists only tools that meet D1, in the three tables D2 describes, with the date the facts were read.
- Every tool on the page has a licence recorded in the research note.
- The page says which listed tool the maintainer wrote, and names no other portfolio tool.
- The control suite page and the five implementation references that describe a quality gate point to the new page, and the semantic index routes to it.
- The ADR index lists this decision, and doctrine preflight passes.

## Residual Risk

- Licences were read by a script from each repository's detected licence, with the licence file read where detection failed. A repository can mix licences across components.
- "No paid plan" was checked on the publishers' own pages for eight tools with a known companion service. Other tools were taken to be free because they are plain command-line programs; that was not checked one by one. Hosts other than one were not checked.
- What each tool does is described from its own one-line description, not from running it. Only the tools in the maintainer's private estate have been used.
- Licence family labels are a common classification, not a legal reading.
- taudit's MIT licence is recorded on the maintainer's statement and his relicensing commit of 2026-11-18. The published repository still carried AGPL-3.0-or-later when this ADR was accepted, and the page says so. If the change is not published, that row is wrong and moves to the other-licences table.
- D6 puts the maintainer's own tool on a page of recommendations. The interest is disclosed, but the listing was not reviewed by anyone without it, and the exception may be read as precedent.
- Drafted and checked by a model. No independent review is recorded.
