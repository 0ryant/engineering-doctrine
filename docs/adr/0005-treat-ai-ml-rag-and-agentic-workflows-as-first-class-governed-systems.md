# 0005. Treat AI/ML, RAG, And Agentic Workflows As First-Class Governed Systems

Status: Accepted (retrospective)  
Decision date: 2026-04-10  
Recorded date: 2026-04-26  
Retrospective: Yes

## Context

The library later added explicit AI/ML, RAG, retrieval, MCP, and internal-agent governance content. This made AI-assisted systems part of ordinary engineering doctrine rather than an external appendix.

Evidence:

- Commit `8923929` — "Doctrine: first-class AI/ML systems, RAG/MCP, research and checklists" (`2026-04-10`)
- Files introduced included `doctrine/principles/ai-ml-systems.md`, `doctrine/patterns/rag-retrieval-baseline.md`, `doctrine/tooling/ai-assisted-development.md`, `doctrine/tooling/vector-retrieval-and-embedding-illustration.md`, and three `doctrine/evolution/research-*` notes

## Decision

Treat **AI/ML systems**, **retrieval systems**, and **agentic workflows** as governed engineering systems subject to the same core expectations as other software:

- Explicit tiers or risk classes.
- Merge-path controls.
- Evaluation and regression evidence.
- Privacy and data-governance boundaries.
- Clear distinction between portable intent and estate-specific tooling.

## Consequences

- AI content belongs in `principles/`, `patterns/`, `tooling/`, and `evolution/` according to the same layer split as the rest of the library.
- Internal agent systems should not bypass CI, review, or governance because they are “assistant” workflows.
- Retrieval indexes, model choices, and vendor platforms remain implementation details unless the operating model changes.

## Honesty Note

This ADR was written after the commit landed. It reconstructs the decision from repository evidence and should not be read as proof that an ADR existed on 2026-04-10.
