# 0004. Add Navigation, References, Glossary, And Evolution Tracking

Status: Accepted (retrospective)  
Decision date: 2026-04-10  
Recorded date: 2026-04-26  
Retrospective: Yes

## Context

As doctrine grew, discoverability and evidence became their own maintenance problem. The repository added a TL;DR, glossary, deeper references, a gap-analysis evolution note, and stronger navigation/checklist links.

Evidence:

- Commit `cda5294` — "Doctrine: gap-fill references, TL;DR, glossary, and navigation" (`2026-04-10`)
- Files introduced included `doctrine/tldr-principles-and-mvp.md`, `doctrine/glossary.md`, and `doctrine/evolution/deep-research-section-gaps.md`
- The same commit expanded `doctrine/REFERENCES.md`, `doctrine/patterns/how-to-read-this-doctrine.md`, and multiple checklists

## Decision

Treat **navigation**, **references**, **glossary**, and **evolution tracking** as first-class parts of the doctrine system.

The library should help readers answer:

- Where do I start?
- Which file wins when details conflict?
- Which external sources support a principle?
- What gaps or thin areas are known?

## Consequences

- New first-class docs should update navigation and references where relevant.
- Substantive research should land in versioned markdown, not remain in chat.
- The sitemap and README become maintenance surfaces, not passive generated clutter.

## Honesty Note

This ADR was written after the commit landed. It reconstructs the decision from repository evidence and should not be read as proof that an ADR existed on 2026-04-10.
