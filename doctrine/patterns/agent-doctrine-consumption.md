# Agent Doctrine Consumption

**Applies when** an AI agent, or a tool server acting for agents, reads, cites,
or proposes changes to this library. It does not apply to a person reading the
Markdown, and it adds nothing to the obligations of the doctrine itself. It
fixes three things that were previously implicit: what the library ships for
agents and what it leaves to a server; the shape of retrieval evidence; and the
form, hashing, and lifecycle of skills.

Related: [how-to-read-this-doctrine.md](how-to-read-this-doctrine.md) (layers),
[run-contracts.md](run-contracts.md) and [verifier-packs.md](verifier-packs.md)
(governed execution), [anti-confabulation-priming.md](anti-confabulation-priming.md)
(the first skill), [doctrine-versioning-and-consumer-compatibility.md](doctrine-versioning-and-consumer-compatibility.md)
(pinning), [../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) §7
(retrieval, indexes, tool surfaces). Rationale:
[ADR 0044](../../docs/adr/0044-adopt-agent-facing-consumption-contract-skill-schema-and-server-boundary.md).

---

## 1. The Library / Server Boundary

The library ships what any conforming server needs and nothing that belongs to
one implementation:

| The library ships | A server ships |
| --- | --- |
| Skills: `doctrine/skills/<name>/SKILL.md` with a hash-pinned priming block and a sibling `verifier-pack.yml` (§3) | The transport (for example an MCP endpoint), authentication, caching, indexing, and hosting |
| The tool contract: [../../contracts/doctrine-tool-contract.v1.schema.json](../../contracts/doctrine-tool-contract.v1.schema.json) — tool names, request and response shapes, trust labels, the proposal-only boundary (§2) | An implementation of those tools that validates against the contract |
| The manifest schema: [../../contracts/skill.v1.schema.json](../../contracts/skill.v1.schema.json) and the validator `scripts/validate-skills.py` | Vendoring of skills at a pinned library revision, re-hashed at build time |
| The register: [../skills/README.md](../skills/README.md) — active skills, tiers, roadmap | Its own health report asserting which library revision it serves and that no forbidden tool is registered |

A server is a **consumer** of the library under
[doctrine-versioning-and-consumer-compatibility.md](doctrine-versioning-and-consumer-compatibility.md):
it pins a library revision, absorbs releases by change class, and is not
vendored into the library. This follows [ADR 0027](../../docs/adr/0027-keep-public-doctrine-implementation-neutral.md):
the library states the portable capability ("doctrine retrieval server",
"skill vendoring") and never names an implementation.

**Why the split:** a server has a build toolchain, a release cadence, a licence,
and a security surface of its own. Putting it inside a Markdown library couples
the doctrine contract to one implementation and drags that surface into every
consumer's pull. The skills and contracts, by contrast, are meaningless without
the doctrine they derive from, so they live beside it.

---

## 2. The Retrieval Contract

Where a server exposes the library to agents, the following are **MUST** for
estate-governed and production paths and **SHOULD** for local single-user use.
Applicability: any tool surface whose output an agent will cite or act on.

- **Evidence cards, not bodies.** Retrieval returns a bounded excerpt with a
  revision-pinned citation (`path`, `section`, `revision`, `content_sha256`),
  the entry's layer and lifecycle status, and a **trust label** (`live`,
  `cached`, `fallback`, with `verified_at`). A fallback card MUST NOT be
  presented as live evidence. Failure prevented: an agent quoting stale or
  vendored text as if it were the current library.
- **Layer is visible.** Every card says which layer it came from. Agents take
  authority only from principles and patterns; a checklist, tooling file,
  estate supplement, or evolution note returned by search is context, not
  obligation ([how-to-read-this-doctrine.md](how-to-read-this-doctrine.md)).
- **Status is visible.** Deprecated and retired entries are excluded by default
  and labelled when included ([doctrine-content-lifecycle.md](doctrine-content-lifecycle.md)).
- **Proposal-only writes.** The only mutating tool writes a proposal to a
  review queue and returns a receipt whose `applied` field is fixed `false`. No
  tool may apply, promote, delete, or bypass review for active doctrine, and
  the health tool asserts that absence. The review path is
  [doctrine-library-change-harness.md](doctrine-library-change-harness.md);
  the server is not part of it. Failure prevented: silent mutation of the
  source of truth by an agent that was only asked to look something up.
- **Health before trust.** An agent SHOULD call the health tool at session
  start and whenever cards look empty, stale, or local, and SHOULD refuse to
  cite from a server whose source check is in error. A server with no library
  root bound can still serve vendored skills (they are content-addressed) but
  cannot serve evidence cards, and its health report says so.

Git remains the source of truth. Indexes, caches, prompt bundles, and agent
memory are derivative surfaces and carry no authority of their own
([../principles/ai-ml-systems.md](../principles/ai-ml-systems.md) §1, §7).

---

## 3. Skills

A **skill** is a small, advisory priming artefact derived from named doctrine.
It changes how an agent reads, cites, or produces; it never decides whether
the result is acceptable. Authority stays with the governing files and with
independent verification.

### 3.1 Form

- Layout: `doctrine/skills/<name>/SKILL.md` beside
  `doctrine/skills/<name>/verifier-pack.yml`, the sibling convention fixed by
  [verifier-packs.md §6](verifier-packs.md). A skill that cannot point to its
  pack is inadmissible.
- Front matter validates against
  [../../contracts/skill.v1.schema.json](../../contracts/skill.v1.schema.json).
  Top-level `name` and `description` follow the SKILL.md convention common to
  agent hosts so the file is consumable unchanged; library-governed fields live
  under the `doctrine` key.
- Body sections in fixed order: Purpose, Instructions, Run-Contract Use,
  Required Independent Checks, Failure Handling, Limits. Instructions holds
  exactly one ```` ```priming ```` fenced block of at most 4096 bytes. That
  block is the only part a host injects; everything else is for the reader.
- **Hash.** `doctrine.priming_block_sha256` is the SHA-256 of the block bytes,
  LF-normalised, fence lines excluded, single trailing newline. The validator
  recomputes it; a host MUST re-hash before injecting; a pack's
  `priming_active` verifier asserts the block is present verbatim in the
  rendered prompt. Failure prevented: a "skill" whose hash exists in three
  places and matches none of them, which is what the library shipped before
  this pattern.
- **Governing.** At least one governing path is a principle or pattern. A
  checklist alone cannot govern a skill, because no obligation exists only in a
  checklist.
- **Authority** is fixed to `advisory` in the schema. There is no way to
  declare a skill that approves or verifies.

### 3.2 Tiers And Injection

| Tier | Contents | Injection default |
| --- | --- | --- |
| 0 | Always-on primers for reading and citing the library | `estate-policy` |
| 1 | Change-lifecycle procedures every agent-assisted change passes through | `estate-policy` on the producing task class |
| 2 | Readiness assessments derived from an owning checklist | `explicit-only` |
| 3 | Design-time specialists | `explicit-only` |

`estate-policy` means an estate MAY auto-inject through a versioned, evaluated
policy whose owner and review date are addressable, and the expanded run
contract MUST show the injection ([anti-confabulation-priming.md §4.1](anti-confabulation-priming.md)).
`explicit-only` means the skill loads only when the run contract lists it.
Either way, no run gains invisible context.

### 3.3 Lifecycle

Skills are first-class doctrine files under
[doctrine-content-lifecycle.md](doctrine-content-lifecycle.md): `active` by
default, `deprecated` with a named successor, `retired` as a tombstone that
MUST NOT be loaded. Every manifest carries a `review_date`; the validator fails
an active skill past it. Any byte change to the priming block bumps the
version and the hash; consumers pin `<name>@<version>`.

### 3.4 Evaluation

A manifest states its `model_scope` and points at the evaluation that justifies
it, or says `evidence: null`. The reference skills in this library say null:
no portable evaluation ships with them, and a host SHOULD treat them as
experimental for its own cell until an estate evaluation exists
([anti-confabulation-priming.md §6](anti-confabulation-priming.md)). A skill is
not made effective by being well-formed.

---

## 4. Pinning And Compatibility

- A server or host pins a library **revision** and reports it in every
  response. Absorbing a new revision is a consumer decision made by change
  class ([doctrine-versioning-and-consumer-compatibility.md §3](doctrine-versioning-and-consumer-compatibility.md)).
- Skills are pinned by `<name>@<version>` and verified by hash, so a skill can
  be vendored at one revision and still be checked against the library at
  another.
- The tool contract and the manifest schema are versioned with the other
  contracts under `contracts/`. A breaking change to either is a **normative
  replacement** and carries a migration note.

---

## 5. Failure Modes

| Failure | Guard |
| --- | --- |
| Fabricated or mislocated citation | Cards carry path, revision, and content hash; the navigation skill pack fails loud on an unresolvable path |
| Stale or vendored text cited as current | Trust label on every card; fallback is never labelled live |
| Agent mutates doctrine through a lookup surface | No mutating tool exists except proposal-to-queue; health asserts absence |
| Skill drift between library and server | Content hash recomputed by the validator, re-hashed by the host, asserted by `priming_active` |
| Skill sprawl | Register with tiers and roadmap; review dates enforced; advisory authority fixed in schema |
| Skill presented as effective without evidence | `evaluation.evidence` is required and may be null; null is a visible claim of no evidence |

---

## 6. Consumer Impact

**Change class:** additive guidance for consumers; navigation for the moved
reference skill; normative tightening for library maintainers only (skills
MUST validate; the sibling pack is now enforced rather than conventional).
No consumer repo policy, CI gate, or operating model changes on absorbing this
pattern. A server that already exposes this library SHOULD emit the contract
document from its health tool and label trust on its cards.

---

## 7. Honest v1 Gap

- No conforming server is named or shipped here, by design; conformance is
  asserted by a server against the contract, and this library has not verified
  any server against it.
- The reference verifier packs check form (paths resolve, tags present,
  trailers well-formed). They cannot check that a citation supports a claim or
  that a `curated` revision was material. Those stay with reviewers.
- The tool contract fixes shapes and invariants, not ranking, indexing, or
  query semantics. Two conforming servers can return different cards for the
  same query.
- Tier 2 and Tier 3 skills are roadmap rows, not files.

---

## Rationale And Decisions

- **Why skills live in the library and servers do not:** skills are meaningless
  without the doctrine they derive from, and a server is meaningless without a
  toolchain the library does not have. The line follows dependency direction.
- **Why the hash is over the block and not the file:** hosts inject the block,
  not the file; a hash over prose that is never injected verifies nothing a
  verifier can observe.
- **Why authority is a schema constant:** the temptation to write a skill that
  "approves" is real and the cheapest place to refuse it is the manifest.
- **Why proposal-only is a contract invariant rather than a server setting:** a
  setting can be flipped; an invariant the health tool must assert cannot be
  flipped quietly.

## Related

- [ai-adoption-controls.md](ai-adoption-controls.md), [agentic-loop-design.md](agentic-loop-design.md)
- [code-review-and-change-approval.md §6.1](code-review-and-change-approval.md) and the `method-record-classification` skill
- [../skills/README.md](../skills/README.md)
