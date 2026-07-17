# AXIOM Record: Doctrine-Grounded AI-Native SDLC

## Problem

The source council document proposes an authority-and-evidence lifecycle for AI-native software delivery, but it is explicitly non-binding, relies on a narrow vendor landscape, and leaves key lifecycle rules and adoption decisions open.

## Goal

Produce an amended, research-grounded SDLC and fold it into the engineering-doctrine library at the correct layers without weakening existing repository authority, protected merge paths, security gates, or accountable human judgement.

## Constraints

- Preserve the source DOCX as research input; the integrated deliverables are Markdown in this repository.
- Use authoritative external sources and distinguish requirements, recommendations, and synthesis.
- Follow the doctrine library change harness for substantive doctrine, ADR, and navigation edits.
- Do not write to AXIOM runtime roots or import USER/MEMORY context.
- Execute as one controlled lane; no subagents were requested and the source, doctrine synthesis, document rewrite, and verification share a tight integration boundary.

## Criteria

- `CHK[1]`: The complete source document is extracted and its layout is inspected before amendment.
- `CHK[2]`: The lifecycle is traceable to existing doctrine and current primary/authoritative external sources, with material source limits stated.
- `CHK[3]`: The adopted lifecycle defines states, admissibility gates, authority separation, evidence classes, materiality scaling, deterministic enactment, runtime reconciliation, and brownfield adoption.
- `CHK[4]`: Library integration includes a research/evolution basis, ADR, layered canonical content, cross-links, and navigation updates appropriate to the change class.
- `CHK[5]`: The Markdown pattern, checklist, research note, ADR, principle/tooling anchors, and navigation surfaces are complete, cross-linked, and repository-validated.
- `CHK[6]`: Repository checks pass after the final edits and pre-existing state remains preserved.
- `CHK[7]`: AWS, Microsoft, and Anthropic vendor observations are re-reviewed, classified through take/defer/reject decisions, and converted into bounded pilot tasks and measures without granting them doctrine authority.
- `CHK[8]`: The canonical pattern directly cites external goal-cascade and measurement sources and defines an objective-to-outcome operating contract that distinguishes tasks and outputs from observed outcomes.
- `CHK[9]`: A repository-native Mermaid diagram accurately visualises the adopted objective-to-outcome chain, S0–S10 lifecycle, deterministic control boundary, and repair/reconciliation loops without introducing new authority or states.

## Test Strategy

- Extract DOCX paragraphs, tables, tracked changes, and comments with bundled document tooling.
- Render the source DOCX to page images and inspect every page before using it as research input.
- Map every normative lifecycle rule to canonical doctrine or a cited external source; label synthesis where no source directly mandates the rule.
- Compare the vendor workflows with the adopted lifecycle and the closed run-contract v1 boundary; do not imply unsupported schema fields or product requirements.
- Run the doctrine preflight and all relevant repository checks.
- Inspect final diffs and compare initial/final Git status.

## Decisions

- `DEC[1]`: Treat the source as a proposed evolution note, not doctrine authority; adoption requires an ADR and canonical pattern/checklist integration.
- `DEC[2]`: Preserve a conventional lifecycle vocabulary for usability, but model progress as evidence-backed state transitions rather than agent-enhanced phases.
- `DEC[3]`: Keep deterministic policy, build, promotion, and receipt surfaces separate from agentic clarification, design, implementation, and semantic challenge.
- `DEC[4]`: Treat Word as source-only after operator clarification; remove the generated Word draft and deliver the lifecycle through canonical Markdown layers.
- `DEC[5]`: Take portable operational lessons from AWS, Microsoft, and Anthropic—versioned clarification, multi-agent lineage/workspace ownership, long-running checkpoints and safe resume, isolated previews, action receipts, and operations-originated feedback—while rejecting vendor rituals, product stacks, and unverified speed/quality claims as doctrine.
- `DEC[6]`: Preserve run-contract v1 as one closed envelope per execution. Multi-agent DAGs and resume identity remain external coordination records until a separately justified contract/workflow version types them.
- `DEC[7]`: Permit operational agents to register S0 observations and propose remediation, but never to detect, implement, approve, and deploy one change as a closed authority loop.
- `DEC[8]`: Adopt stakeholder need → objective/standing obligation → guardrailed outcome measures → intervention hypothesis → tasks/run contracts → outputs → observed outcomes → continue/change/stop decision. AI may propose the mapping and work decomposition; accountable business/product governance owns objectives, measure validity, portfolio priority, capacity, and the final decision. Reject a direct KPI-to-task compiler because it erases causal assumptions and invites metric gaming.
- `DEC[9]`: Present the lifecycle as a Mermaid flowchart in the canonical Markdown pattern. Use four visible boundaries—accountable direction/value, agent-assisted delivery, deterministic control, and runtime/portfolio reconciliation—and show fail, deny, rollback, and feedback paths explicitly.

## Evidence

- `CMD(git status --short, exit=0)`: Initial worktree was clean.
- `USER(operator-supplied council-session DOCX)`: 234 paragraphs, 23 tables, no comments, and no tracked insertions/deletions were extracted.
- `CMD(LibreOffice DOCX-to-PDF conversion, exit=0)`: Source document rendered to PDF after using a valid Windows LibreOffice profile URI.
- `WEB(primary authorities, 2026-07-17)`: NIST SSDF 1.1/SP 800-218A, NIST AI RMF 1.0, NCSC secure-AI guidance, ISO/IEC 5338:2023 official abstract, SLSA v1.2, and Regulation (EU) 2024/1689 were verified; vendor material was classified as observation, not normative authority.
- `WEB(vendor source review, 2026-07-17)`: AWS AI-DLC, Microsoft's AI-led SDLC demonstration, and Anthropic's complete 18-page 2026 Agentic Coding Trends Report were re-reviewed; claims, predictions, operating patterns, limits, and product specificity were classified.
- `WEB(goal cascade and measurement review, 2026-07-17)`: ISACA COBIT 2019 goals cascade, Basili et al. GQM+Strategies, the original University of Maryland GQM report, NIST AI RMF Core, DORA's current metrics guidance, and Google's practitioner OKR playbook were reviewed. The sources support traceable goals and contextual measurement while warning, directly or by implication, against treating activity metrics as business outcomes.
- `FILE(doctrine/patterns/ai-native-software-development-lifecycle.md)`: S0–S10 lifecycle, admissibility, authority, evidence, materiality/autonomy, deterministic boundary, P0–P5 adoption, measures, failure modes, and consumer impact landed.
- `FILE(doctrine/patterns/ai-native-software-development-lifecycle.md#22-lifecycle-at-a-glance)`: Mermaid flowchart maps the existing objective-to-outcome and S0–S10 records, including evidence repair, denied authority, rollback/containment, and portfolio feedback.
- `CMD(npx @mermaid-js/mermaid-cli, exit=0)`: The final Mermaid source rendered to PNG and was visually inspected; a four-column layout replaced long cross-diagram feedback arrows with explicit repeat/re-entry endpoints.
- `FILE(docs/adr/0024-adopt-a-doctrine-grounded-ai-native-software-development-lifecycle.md)`: Adoption decision, alternatives, consequences, acceptance, measures, and residual risks recorded.
- `CMD(bash ./scripts/doctrine-change-preflight.sh, exit=1)`: Direct WSL execution exposed CRLF in the checked-out shell script (`pipefail\r`), an execution-environment issue rather than a doctrine check failure.
- `CMD(CRLF-normalised doctrine preflight with documented Python sitemap fallback, exit=0)`: The same harness checks ran from repository root and regenerated the sitemap without modifying the shell script.
- `FILE(.gitattributes)`: `*.sh text eol=lf` makes the shell-entrypoint contract explicit for Windows and POSIX checkouts.
- `CMD(bash ./scripts/doctrine-change-preflight.sh, exit=0)`: The actual POSIX preflight passes after LF normalisation; no fallback or in-memory script rewrite is required.
- `CMD(relative Markdown link audit, exit=0)`: All 1,123 relative links in the 22 currently changed or new Markdown files resolve; the count includes concurrent operator work outside ADR 0024.
- `CMD(git diff --check, exit=0)`: No whitespace errors were found.
- `CMD(python scripts/validate-contracts-v1.py, exit=0)`: Run-contract, verifier-pack, router-policy, primer-pin, negative, tier-reachability, and interpreter-wrapper checks pass after clarifying the multi-agent boundary.
- `USER(operator-supplied council-session DOCX)`: The source remained unchanged during analysis; temporary render/build artefacts were removed.

## Check Results

- `CHK[1] PASS`: Complete structural extraction and 13-page rendered inspection recorded.
- `CHK[2] PASS`: Primary authorities and vendor observations are classified and cited; the eleven-state synthesis is labelled as this library's design choice.
- `CHK[3] PASS`: The canonical pattern covers state, evidence, authority, materiality/autonomy, deterministic enactment, reconciliation, and brownfield adoption.
- `CHK[4] PASS`: ADR, research note, principle/pattern/tooling/checklist layering, glossary, references, indexes, and release note are cross-linked.
- `CHK[5] PASS`: The final deliverable is Markdown only and all changed/new Markdown link targets resolve.
- `CHK[6] PASS`: The actual POSIX doctrine preflight, contract suite, link audit, and diff checks pass. `.gitattributes` closes the Windows-checkout CRLF failure mode; the operator's source remains unchanged and no AXIOM runtime root was modified.
- `CHK[7] PASS`: Vendor findings are recorded as take/investigate/reject decisions and mapped to five role-owned pilot tasks with acceptance evidence, measures, and stop conditions.
- `CHK[8] PASS`: The canonical lifecycle embeds direct external citations at the objective-to-outcome rule, defines measure contracts and authority boundaries, and makes task/output completion non-equivalent to outcome evidence.
- `CHK[9] PASS`: The Mermaid source is repository-native, uses supported flowchart syntax, contains no orphan lifecycle nodes, and preserves the adopted authority and feedback semantics.

## Residual Risk

The control model is research-grounded but the eleven-state granularity, portable transition/coordination schema, resume identity, autonomy thresholds, and objective-to-outcome attribution model are not yet empirically validated. Objectives and KPIs can still create false precision, local optimisation, or Goodhart effects even with guardrails. Vendor case studies and forecasts are not independent comparative evidence. ADR 0024 therefore requires a bounded brownfield pilot—including failed/inconclusive, stopped/resumed, isolated-preview, parallel-work, operations-originated, and objective-to-outcome paths—before those deferred choices are standardised.
