# ADR 0044: Adopt An Agent-Facing Consumption Contract, Skill Schema, And Library/Server Boundary

- **Status:** Accepted
- **Decision date:** 2026-09-03
- **Recorded date:** 2026-09-03
- **Retrospective:** No
- **Builds on:** [ADR 0027](0027-keep-public-doctrine-implementation-neutral.md) (implementation neutrality), [ADR 0038](0038-adopt-a-doctrine-content-lifecycle.md) (lifecycle), [ADR 0043](0043-replace-agent-coauthorship-disclosure-with-a-method-record.md) (method record)

## Context

This library is increasingly consumed by agents rather than read by people, through a doctrine retrieval server maintained separately and through skills injected into agent prompts. Neither surface had a contract in the library, and the gap showed in four concrete defects found on 2026-09-03:

1. **The only skill had an unreproducible hash.** `doctrine/skills/anti-confabulation.skill.md` was described in `doctrine/README.md` and `doctrine/REFERENCES.md` as carrying priming block SHA-256 `c138dd96…`; the server that vendors it served `12cc05d5…`; hashing the file, its Instructions section, or the section with a trailing newline produced three further values, none matching either. The block was not machine-delimited, so no hash could be recomputed from the file.
2. **The skill referenced a verifier pack that did not exist.** `anti-confabulation-verifier-pack@1.0.0` appeared in the skill, the pattern, and the run-contract schema note, and no such pack was present anywhere in the repository. The run-contract schema calls the sibling pack "REQUIRED BY CONVENTION" and says on-disk existence is not checked; nothing checked it.
3. **The skill did not follow the sibling layout the library mandates.** [verifier-packs.md §6](../../doctrine/patterns/verifier-packs.md) fixes `<skill-root>/<skill>/SKILL.md` beside `<skill-root>/<skill>/verifier-pack.yml` and calls a skill that cannot point to its pack inadmissible. The file was a flat `.skill.md`.
4. **The question "should the server move into this repo" had no principled answer.** The server is under a different licence from the library's Apache-2.0, depends on private crates, and carries a Rust toolchain plus fuzz, mutation, and vulnerability workflows. Nothing in the library said whether a consumer of that shape belongs inside it.

Separately, the owner asked which skills an agent needs to get the most from the doctrine. Without a schema, a lifecycle, and a derivation rule, answering that produces sprawl: skills that restate doctrine in a second voice, drift from it, and accrete without review, which is the failure [ADR 0038](0038-adopt-a-doctrine-content-lifecycle.md) exists to prevent for every other file class.

## Decision

1. **Library/server boundary (normative).** The library ships the agent-facing *contract*: skills, the skill manifest schema and validator, the tool contract, and the skills register. A retrieval server is a **consumer** pinned to a library revision under [doctrine-versioning-and-consumer-compatibility.md](../../doctrine/patterns/doctrine-versioning-and-consumer-compatibility.md) and is not vendored into the library. This follows ADR 0027 decision 3 and the dependency direction: skills are meaningless without doctrine; a server is meaningless without a toolchain the library does not have.

2. **Tool contract (normative for governed paths).** [contracts/doctrine-tool-contract.v1.schema.json](../../contracts/doctrine-tool-contract.v1.schema.json) fixes tool names, request and response shapes, evidence cards with revision-pinned citations and trust labels (`live` / `cached` / `fallback`), a fixed list of forbidden capabilities, and a proposal-only write whose receipt cannot claim application. A server asserts conformance from its health tool; the library verifies no server.

3. **Skill manifest schema (normative for library skills).** [contracts/skill.v1.schema.json](../../contracts/skill.v1.schema.json) governs SKILL.md front matter. Top-level `name` and `description` follow the SKILL.md convention used by agent hosts (verified against the published Agent Skills specification on 2026-09-03, which reserves `name`, `description`, `license`, `compatibility`, `metadata` as a string map, and `allowed-tools`); library fields live under the documented extension key `doctrine`. `authority` is the constant `advisory`. Every skill names at least one governing principle or pattern.

4. **Priming block and hash (normative for library skills).** The Instructions section holds exactly one ```` ```priming ```` fenced block of at most 4096 bytes. `priming_block_sha256` is the SHA-256 of that block, LF-normalised, fence lines excluded, single trailing newline. `scripts/validate-skills.py` recomputes it, and its `assert-primed` subcommand is the reference `priming_active` verifier command.

5. **Sibling pack enforced (normative for library skills).** Every skill ships `verifier-pack.yml` beside it, validating against the verifier-pack schema, mirroring the skill by name, and containing at least one `priming_active` assertion. The validator fails a skill without one; the doctrine preflight and CI run the validator.

6. **Lifecycle and tiers (normative for library skills).** Skills are first-class doctrine files under ADR 0038: `active` / `deprecated` / `retired`, with a `review_date` the validator enforces. Four tiers with injection defaults are defined in [doctrine/skills/README.md](../../doctrine/skills/README.md); the register carries active skills and a roadmap whose rows may not be cited, injected, or pinned.

7. **Initial cohort.** Five skills land with this ADR: `anti-confabulation` migrated to 1.1.0 (instruction text unchanged; the 1.0.0 hash is not carried forward because it was never reproducible), and four new: `doctrine-navigation`, `normative-language-reading`, `evidence-graded-citation` (Tier 0), and `method-record-classification` (Tier 1, discharging ADR 0043). Each says `evaluation.evidence: null`.

8. **Pattern.** [agent-doctrine-consumption.md](../../doctrine/patterns/agent-doctrine-consumption.md) is the owning pattern for decisions 1–6.

## Alternatives Considered

### Vendor the server into this repository

Rejected. Three hard blockers independent of design: the server's licence differs from the library's Apache-2.0 (ADR 0025), so the tree would need per-directory licensing; its build depends on private crates, so a public clone would not build; and its docs and workflows carry local paths and private names that ADR 0027 decision 6 would require scrubbing from reachable history. Beyond blockers, it inverts the consumer relationship the versioning pattern defines and drags a Rust toolchain into a Markdown library's every pull.

### Skills as free-form Markdown with a hash in the README

Status quo. Rejected by the evidence in Context: with no machine-delimited block, the hash cannot be recomputed and three copies of it diverged unnoticed.

### Put library fields in the host convention's `metadata` map

Rejected. That map is string-to-string; `governing` and `applies_to` are lists and `governing` entries carry sections. Flattening them loses the derivation the validator checks. The `doctrine` extension key keeps `name` and `description` conformant and lets a strict host strip the extension while keeping the hash-pinned body.

### Skills without verifier packs for "just primers"

Rejected. A primer with no observable behaviour is unfalsifiable and would be the first skill class exempt from the sibling rule the library already calls rigid. Every pack here has at least `priming_active` plus form checks on the produced report; what a pack cannot check is stated in each skill's Limits.

### Land all roadmap skills now

Rejected. Twenty further skills drafted in one pass would be exactly the accretion ADR 0038 guards against. The roadmap makes the derivation visible before the file exists; each skill lands through the harness on its own evidence.

### Name the server and its tools as the reference implementation

Rejected per ADR 0027. The contract states the capability; conformance is a server's claim against the contract.

## Consequences

- Any skill that fails the validator is inadmissible; the preflight and CI enforce this.
- `anti-confabulation@1.0.0` references in the pattern and run-contract examples move to 1.1.0. Consumers pinning 1.0.0 by name receive the same instruction text but must re-pin to obtain a verifiable hash.
- A server exposing this library gains a conformance target and a health-report shape; it loses nothing it already did legitimately.
- The library commits to maintaining `contracts/skill.v1.schema.json`, `contracts/doctrine-tool-contract.v1.schema.json`, and `scripts/validate-skills.py` under the same versioning discipline as the other contracts.
- `docs/skill/DoctrineLibraryChange/SKILL.md` is a maintainer-facing host skill, not a doctrine skill, and is deliberately left outside this schema.

## Consumer Impact

**Change class:** additive guidance and navigation for consumers; normative tightening for library maintainers only. Migration: re-pin `anti-confabulation@1.0.0` to `@1.1.0` and repoint any link to `doctrine/skills/anti-confabulation.skill.md` at `doctrine/skills/anti-confabulation/SKILL.md`.

## Acceptance Evidence

- `python scripts/validate-skills.py` reports 5 skills, 0 errors; `python scripts/validate-contracts-v1.py` remains green.
- `assert-primed` returns 0 on a prompt containing the `doctrine-navigation` block and 1 on a prompt that does not contain the `anti-confabulation` block (positive and negative case recorded in the landing session).
- Both new JSON Schemas parse as Draft 2020-12 and are loaded by the validator.
- Every relative link in the new and changed files resolves; the doctrine preflight regenerates the sitemap with the new paths.
- All references to the old `.skill.md` path in README, REFERENCES, SEMANTIC_INDEX, and test protocols are repointed.

## Review Note

Drafted and landed in a single agent session under the owner's direction; council review was not run. The commit carries a method record per ADR 0043 with `class=generated`. Skills in the initial cohort ship with `evaluation.evidence: null` and should not be treated as effective until an estate evaluation exists.
