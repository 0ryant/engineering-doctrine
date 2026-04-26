# 0006. Add Governance And Assurance Navigation And Adopt ADRs

Status: Accepted  
Decision date: 2026-04-26  
Recorded date: 2026-04-26  
Retrospective: No

## Context

New governance doctrine was added for merge-path evidence, pipeline integrity, engineering-controls governance, and control-suite tooling. The topic cuts across `principles/`, `patterns/`, `tooling/`, and `checklists/`, which made discoverability a concern.

The council check on 2026-04-26 converged on the same recommendation: create a dedicated **Governance & Assurance** navigation section, but do **not** create a new doctrine layer or `doctrine/governance/` folder.

Evidence:

- Current working-tree additions:
  - `doctrine/principles/merge-path-evidence-and-pipeline-integrity.md`
  - `doctrine/patterns/engineering-controls-governance-program.md`
  - `doctrine/tooling/merge-path-and-pipeline-control-suite.md`
  - `doctrine/checklists/governance-program-readiness.md`
- Council synthesis from 2026-04-26: navigation section yes; new folder/layer no; dogfood ADRs and governance controls in this repo

## Decision

Add a **Governance & Assurance** navigation section while preserving the existing doctrine layer taxonomy.

Also adopt ADRs for decisions about this doctrine library itself. Historical ADRs may be recorded retrospectively, but they must say so plainly.

## Consequences

- Governance becomes easier to find without weakening the layer split established in ADR 0003.
- Future structural doctrine decisions should get ADRs at decision time where practical.
- Retrospective ADRs are allowed only when they cite evidence and include both decision and recorded dates.
- This repo should apply its own governance advice proportionally: ADRs, sitemap freshness, link/reference hygiene, review ownership for high-impact files, and a lightweight threat model for poisoned doctrine.

## Follow-Ups

- Add the Governance & Assurance section to `doctrine/README.md`, `doctrine/REFERENCES.md`, and `ENGINEERING.md`.
- Consider a small `doctrine/governance-and-assurance.md` landing page if the section grows.
- Add review ownership / CODEOWNERS guidance for high-impact doctrine paths.
- Add a lightweight threat model for the doctrine repo itself.
