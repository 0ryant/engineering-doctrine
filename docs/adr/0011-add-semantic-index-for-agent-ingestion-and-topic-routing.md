# 0011. Add Semantic Index For Agent Ingestion And Topic Routing

Status: Accepted
Decision date: 2026-05-09
Recorded date: 2026-05-09
Retrospective: No

## Context

The doctrine library already has several discovery surfaces:

- [../../doctrine/README.md](../../doctrine/README.md) for human entry and section lists.
- [../../doctrine/SITEMAP.md](../../doctrine/SITEMAP.md) for a generated complete file list.
- [../../doctrine/REFERENCES.md](../../doctrine/REFERENCES.md) for external authorities and an internal map.
- [../../AGENTS.md](../../AGENTS.md) for agent contributor instructions.

Those surfaces are useful, but they do not give agents a compact semantic route from task intent to the small set of source docs they must ingest before acting. The AI/RAG doctrine also says repo state is authoritative while indexes and embeddings are derivatives, and the RAG research recommends explicit corpus and retrieval design rather than naive indexing.

Evidence:

- User request on 2026-05-09 to build a full semantic index and link it so agents ingest the important doctrine.
- [../../doctrine/principles/ai-ml-systems.md](../../doctrine/principles/ai-ml-systems.md) - truth in repo, agent context, retrieval/index lifecycle, and tool-surface governance.
- [../../doctrine/evolution/research-enterprise-rag-agents-indexing-2026-04.md](../../doctrine/evolution/research-enterprise-rag-agents-indexing-2026-04.md) - enterprise RAG, indexing, and agent tooling research.
- ADR 0004 - prior decision to add navigation, references, glossary, and evolution tracking.

## Decision

Add [../../doctrine/SEMANTIC_INDEX.md](../../doctrine/SEMANTIC_INDEX.md) as a curated semantic router for humans and agents.

The index will:

- State that it is not a new doctrine layer and does not override source docs.
- Define critical agent context for substantive work.
- Map task intents to canonical principle, pattern, tooling, checklist, ADR, and evolution routes.
- Connect research/evidence notes to the doctrine areas they support.
- Be linked from agent and human entrypoints so it is visible before deep work.

## Consequences

- Agents get a clearer ingestion contract without treating generated embeddings or chat transcripts as authority.
- Human readers gain a route-by-intent map that complements the sitemap and references index.
- The library adds a new navigation artifact; future first-class topic additions should consider whether their route belongs in the semantic index.
- This is an additive navigation change. It introduces no new adopter obligation and no normative tightening.
