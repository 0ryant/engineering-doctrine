# Research: MCP 2026-07-28 Spec Cross-Check And Gap Map (August 2026)

**Status:** research note (non-normative). **Date:** 2026-08-06. **Method:** 4-agent deep-research verification (authorization, deprecation/transport, security sources, corpus extraction) of every MCP claim in the corpus against primary sources, three days after [ADR 0031](../../docs/adr/0031-add-agent-identity-mcp-revision-pinning-and-asi-crosswalk-coverage.md) landed the revision-pinned MCP baseline; drafts critiqued by a three-critic council (doctrine fidelity, independent fact re-verification, coherence) with all blockers and majors resolved before landing. Proposals route via ADR per repo convention ([../../docs/adr/](../../docs/adr/)). Corrections found by this cross-check land via [ADR 0037](../../docs/adr/0037-land-mcp-cross-check-correction-batch.md).

---

## 1. Purpose and method

The August 2026 gap audit ([research-bleeding-edge-ai-landscape-gap-audit-2026-08.md](research-bleeding-edge-ai-landscape-gap-audit-2026-08.md)) closed S2 (MCP under-specification) via ADR 0031 while the 2026-07-28 specification revision was days old. This note records a **depth pass**: each normative claim in [ai-ml-systems.md](../principles/ai-ml-systems.md) §7 and its companion edits was re-verified against the published spec text (not the changelog summary alone), and the revision's mechanics were researched deeply enough to ground the §4 gap map. Where an absence is a **deliberate non-gap** (implementation neutrality, doctrine altitude) rather than an unconsidered gap, the note says so explicitly (§3.4, §4 preamble).

Every claim verdict below traces to a primary source (spec pages, SEP texts, the official deprecated-features registry, NSA/OWASP documents, NVD records, vendor advisories). Items that could not be confirmed against primary sources carry **(unverified)** flags. This note is **non-normative**: it changes nothing by itself; normative changes go through ADRs.

---

## 2. Verification results — the §7 baseline holds

All five §7 bullets and the ADR 0031 companion edits survived verification. Verdicts:

| Claim (home) | Verdict | Detail |
|---|---|---|
| Revision pinning MUST; both changelog characterizations ([ai-ml-systems.md](../principles/ai-ml-systems.md) §7) | **Valid** | 2025-06-18 and 2026-07-28 descriptions accurate; CIMD phrasing gains precision via ADR 0037 (acronym expansion, citation split) |
| Remote servers: OAuth 2.1 resource-server + RFC 8707 MUST (§7) | **Valid as doctrine** | RFC 8707 resource indicators remain MUST-level in the [2026-07-28 authorization spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization). Attribution note: **"external IdP" is this doctrine's tightening, not spec text** — the spec permits the authorization server to be "hosted with the resource server or a separate entity," and authorization itself is OPTIONAL at spec level (SHOULD-conform for HTTP transports). The doctrine MUST stands on its own authority |
| Registry posture curated, not open (§7) | **Valid, strengthened** | Official registry still **preview** (2026-08-06 check). [Moderation policy](https://modelcontextprotocol.io/registry/moderation-policy) verbatim: consumers "should assume minimal-to-no moderation"; servers with security vulnerabilities are explicitly **not** removed. Registry documentation describes metadata hosting only — no package signing or attestation. The [corpus-review](research-full-corpus-council-review-2026-08.md) staleness flag on the live "preview" claim stays correct as a flag |
| Gateways MUST NOT key on `Mcp-Session-Id` for 2026-07-28+ pairs (§7) | **Valid** | Confirmed; the spec adds that modern-only servers SHOULD ignore the header and not mint or echo session IDs (SHOULD-level in spec; the doctrine gateway MUST NOT stands on doctrine authority) |
| NSA CSI + OWASP guide as informative baselines (§7) | **Valid** | NSA CSI release date **2026-05-20** confirmed (press release, doc U/OO/6030316-26); OWASP guide v1.0 / 2026-02-16 confirmed. Caveat: the OWASP guide **predates 2026-07-28** and frames session security in session-ID and session-isolation terms; no revision-updated edition exists as of 2026-08-06 |
| Deprecation-cadence bullet ([dependencies-supply-chain.md](../principles/dependencies-supply-chain.md)) | **Valid** | The twelve-month minimum window is confirmed in the [feature-lifecycle policy](https://modelcontextprotocol.io/community/feature-lifecycle) (SEP-2596); instances now enumerable — see §4 row 3 |
| Glossary MCP entry, api-boundaries Related pointer | **Valid** | No corrections needed |

---

## 3. Landscape digest — 2026-07-28 mechanics relevant to doctrine

### 3.1 Deprecation clocks (primary: [deprecated-features registry](https://modelcontextprotocol.io/specification/2026-07-28/deprecated))

| Feature | State | Earliest removal | Official migration |
|---|---|---|---|
| Roots | Deprecated (SEP-2577) | First revision **released** on or after **2027-07-28** | Tool parameters, resource URIs, or server configuration |
| Sampling (incl. 2025-11-25 sampling-with-tools) | Deprecated (SEP-2577) | ≥ 2027-07-28 | Direct LLM-provider APIs |
| Logging | Deprecated (SEP-2577) | ≥ 2027-07-28 | stderr (stdio); OpenTelemetry for observability |
| Dynamic Client Registration (RFC 7591) | Deprecated (PR #2858) | ≥ 2027-07-28 | Client ID Metadata Documents (CIMD, SHOULD; introduced 2025-11-25 via SEP-991) |
| `includeContext` `"thisServer"`/`"allServers"` | Deprecated | Follows Sampling | — |
| HTTP+SSE transport | Deprecated (since 2025-03-26; formalised) | **Three months after SEP-2596 reaches Final** — a different clock | Streamable HTTP |
| Sessions / `initialize` handshake / `Mcp-Session-Id` | **Removed — no deprecation window** | Already absent from 2026-07-28 | Survives only on pairs pinned ≤ 2025-11-25; migration is the revision migration itself. Legacy clients have **no fall-forward** against modern-only servers — a migration-ordering input (clients before servers) |

During a deprecation window, wire behaviour is unchanged; implementations that encounter deprecated capabilities MUST still handle them correctly, and new implementations SHOULD NOT adopt deprecated features. Expedited removal exists only for a vulnerability with a published security advisory or documented in-the-wild exploitation for which no in-place mitigation exists, with a ninety-day floor.

### 3.2 Statelessness, MRTR, and state handles

- **MRTR** (SEP-2322, building on SEP-2260) replaces all server-initiated requests: servers return `resultType: "input_required"`; the client retries the original request with the responses. Spec-normative security text worth doctrine attention: servers **MUST treat `requestState` as attacker-controlled input**; when it influences authorization, resource access, or business logic they MUST protect its integrity (HMAC or AEAD), SHOULD bind it to the authenticated principal, a TTL, and a digest of the originating request, and MUST enforce any single-use invariant server-side.
- **State handles** replace sessions for cross-call state (server-minted strings passed as tool arguments — a convention, not a protocol feature). The spec's [security page](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) replaces "Session Hijacking" with "**State Handle Hijacking**": possession of a handle **MUST NOT** be treated as authentication; servers SHOULD use secure-random handles and SHOULD bind them server-side to the authenticated principal. The handle-entropy guidance in SEP-2567 (128-bit minimum for unauthenticated servers) is explicitly **non-normative** — the MUST/SHOULD distinction matters for citation discipline.
- **Era coexistence**: one endpoint MAY serve both eras; dual-era clients fall back to `initialize` against legacy servers. The fall-forward asymmetry feeds the §3.1 sessions row.

### 3.3 Extensions (first-class since 2026-07-28, SEP-2133)

Official extensions, hosted in official `ext-*` repositories with versioning independent of core, all opt-in and negotiated via capabilities: **MCP Apps** (`io.modelcontextprotocol/ui` — server-supplied sandboxed-iframe HTML UIs; shipped in Claude, ChatGPT, VS Code, M365 Copilot), **Tasks** (`io.modelcontextprotocol/tasks` — graduated from experimental core; poll-based), **Enterprise-Managed Authorization** (`io.modelcontextprotocol/enterprise-managed-authorization` — stable 2026-06-18; the MCP binding of the IETF ID-JAG draft the zero-trust §2.1 standards watch already tracks; Okta, Anthropic, VS Code at launch), and OAuth client credentials. MCP Apps is a genuinely **new trust surface**: servers ship renderable UI content into hosts, mediated by the host's consent/audit path.

### 3.4 Governance and ecosystem

- **Confirmed (resolves the April note's hedge):** Anthropic donated MCP to the **Agentic AI Foundation** — a Linux Foundation directed fund co-founded by Anthropic, OpenAI, and Block — on **2025-12-09** ([announcement](https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/)). Working groups are now the primary development vehicle (2026 roadmap).
- Tier-1 SDKs shipped coordinated releases with 2026-07-28 support on the spec-final date (TypeScript, Python, Go, C#; Rust in beta); Kotlin and Swift SDKs remain 0.x without it. The corpus names no SDKs — a **deliberate non-gap**, consistent with implementation neutrality ([ADR 0027](../../docs/adr/0027-keep-public-doctrine-implementation-neutral.md)).
- No host vendor (Anthropic, OpenAI, Microsoft) has published a legacy-server support cutoff as of 2026-08-06. The spec's backward-compatibility provisions and the lifecycle policy leave 2025-11-25 pairs functional, with dual-era clients falling back automatically.

### 3.5 Security landscape (verified corrections included)

- **StdioServerParameters command-injection class** (OX Security supply-chain advisory, 2026-04-15): **14 CVEs**, flagship **CVE-2026-30623** (LiteLLM; CVSS 9.8 per NVD/CISA-ADP); the config-to-command execution path in official SDKs is **wontfixed as intended behaviour** by Anthropic, LangChain, FastMCP, and others; no safer-exec API had appeared in the 2026-07-28-aligned SDK releases as of 2026-08-06. Untrusted input reaching MCP server *configuration* is therefore a permanent estate responsibility, not a patchable vendor defect. Note: "MCP by Design" is the title of the **Cloud Security Alliance research note** about these findings, not OX's advisory.
- **CVE-2026-33032** (nginx-ui missing auth on `/mcp_message`, CVSS 9.8, actively exploited per VulnCheck KEV 2026-04-13) is a **separate** vulnerability frequently conflated with the class above; CISA KEV inclusion is conflictingly reported **(unverified — check the KEV catalog directly before citing)**.
- **SmartLoader campaign** (Straiker STAR Labs, publicised 2026-02-17): trojanized "Oura Ring" MCP server delivering StealC infostealer, published to **MCP Market, a third-party aggregator — not the official registry**. Supports the §7 distinction between namespace authenticity and trust, and the curated-allowlist stance.
- **Prevalence studies — two distinct "66%" figures circulate and are routinely conflated:** arXiv:2506.13538 reports 5.5% of 1,899 open-source servers exhibiting tool-poisoning *vulnerability patterns* by static scan (not confirmed-malicious) and 66% showing **code smells**; AgentSeal's own scan reports **security findings** in 66% of 1,808 servers (static attack surface, not confirmed vulnerabilities), toxic data flows in 555 of 5,125 servers in a later scan, and successful runtime exploitation of flagged critical/high findings on 6 high-profile servers in a follow-up validation. MCPTox (arXiv:2508.14925) reports tool-poisoning attack success up to 72.8% on live servers, with more-capable models more susceptible. Cite the specific study and finding class, never a bare "66%".
- NSA CSI content caveat: the PDF bot-blocks fetchers; its recommendation detail is triangulated from consistent secondary analyses — spot-check against the PDF before quoting it verbatim.

---

## 4. Prioritised action list

Ordered by severity, then ascending effort. Change class per doctrine versioning vocabulary; normative changes route via ADR. Rows 8–10 are the correction batch, landed by [ADR 0037](../../docs/adr/0037-land-mcp-cross-check-correction-batch.md) alongside this note. Wire-level mechanics (subscription demultiplexing, era probing, transport internals) are deliberately excluded as below doctrine altitude. Corpus-internal record: the `tool-contract.lock` / running-tool-fingerprint concept exists only as a fixture string in `scripts/validate-contracts-v1.py` line 276, with no doctrine home — treated as naming-only, not a latent obligation.

| # | Action | Target file(s) | Class | ADR? |
|---|---|---|---|---|
| 1 | **Post-session state security**: new §7 sub-bullet for 2026-07-28+ pairs — state handles are never authentication (spec MUST); servers treat MRTR `requestState` as attacker-controlled, with integrity protection when it influences authorization or business logic (spec MUST); distinguish spec-normative from SEP-advisory guidance | ai-ml-systems.md §7 (new sub-bullet) | normative | yes |
| 2 | **Extensions posture**: extensions are opt-in and individually adoptable; MCP Apps as a new content-into-host trust surface (host consent/audit path, template review); Tasks for long-running operations | ai-ml-systems.md §7, possibly agentic-loop-design.md | normative | yes |
| 3 | **Deprecation ledger**: record the §3.1 clock table as cadence inputs under the existing protocol-deprecation bullet — Roots/Sampling/Logging/DCR earliest removal ≥ 2027-07-28, HTTP+SSE's separate clock, sessions Removed with **no** window and the client-before-server migration-ordering consequence; REFERENCES row for the deprecated-features registry | dependencies-supply-chain.md, REFERENCES.md | additive guidance | no |
| 4 | **SDK config-injection evidence**: cross-link the StdioServerParameters evidence (§3.5) as a named admission consideration for MCP servers — configuration is already a governed trust surface per merge-path §1/§2; any new obligation routes with the row 1–2 future ADR, and the admission-surface overlap with still-open gap-audit row 22 is noted there | dependencies-supply-chain.md (cross-link) | additive guidance | no |
| 5 | **EMA cross-link**: add Enterprise-Managed Authorization (stable 2026-06-18, MCP binding of the tracked ID-JAG draft) to the §2.1 standards-watch block | zero-trust-and-workload-identity.md §2.1 | editorial (informative block) | no |
| 6 | **Row-22 evidence annotation**: annotate the still-open registry-attestation action (gap-audit row 22) with the strengthened evidence — official registry does no scanning or signing, "minimal-to-no moderation," SmartLoader hit a third-party aggregator | gap-audit note §7 (annotation); future ADR unchanged | editorial | no |
| 7 | **Prevalence citations**: index arXiv:2506.13538 and arXiv:2508.14925 as the citable tool-poisoning evidence base | REFERENCES.md | editorial | no |
| 8 | NSA CSI date correction and RC-vs-final URL repair in the gap-audit §2.9 rows; auth-change enumeration replacing the unenumerated "six"; "External IdP" removed from the spec-description row (doctrine tightening, not spec text — §2) | research-bleeding-edge-ai-landscape-gap-audit-2026-08.md | editorial (corrective; ADR 0037) | ADR 0037 |
| 9 | AAIF hedge resolution (dated update) in the April note; CIMD acronym expansion and citation split in §7 | research-enterprise-rag-agents-indexing-2026-04.md, ai-ml-systems.md §7 | editorial (corrective; ADR 0037) | ADR 0037 |
| 10 | Fixture grammar fix; `tool-contract.lock` recorded as fixture-only (see this section's preamble) | scripts/validate-contracts-v1.py; this note (record) | editorial (corrective; ADR 0037) | ADR 0037 |
| 11 | **Watch** (no doctrine change): OWASP secure-MCP guide revision (currently session-era); host legacy-server support cutoffs; the spec's forecast upgrade of AS-side RFC 9207 `iss` emission from SHOULD to MUST; CIMD adoption trajectory now that DCR is deprecated; MCP server-card / trust-annotation SEPs | evolution/ (this note) | — | no |

---

## 5. References

| Source | URL |
|---|---|
| MCP 2026-07-28 changelog | https://modelcontextprotocol.io/specification/2026-07-28/changelog |
| MCP 2026-07-28 authorization spec | https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization |
| MCP client registration (CIMD) | https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration |
| MCP deprecated-features registry | https://modelcontextprotocol.io/specification/2026-07-28/deprecated |
| MCP feature-lifecycle policy (SEP-2596) | https://modelcontextprotocol.io/community/feature-lifecycle |
| MCP security best practices (2026-07-28) | https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices |
| MRTR pattern spec | https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr |
| Sessionless MCP (SEP-2567) | https://modelcontextprotocol.io/seps/2567-sessionless-mcp.md |
| Deprecate Roots/Sampling/Logging (SEP-2577) | https://modelcontextprotocol.io/seps/2577-deprecate-roots-sampling-and-logging |
| Extensions overview | https://modelcontextprotocol.io/extensions/overview |
| Enterprise-Managed Authorization extension | https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization |
| 2026-07-28 final announcement | https://blog.modelcontextprotocol.io/posts/2026-07-28/ |
| MCP joins Agentic AI Foundation (2025-12-09) | https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/ |
| Registry moderation policy | https://modelcontextprotocol.io/registry/moderation-policy |
| NSA press release (CSI, 2026-05-20) | https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4496698/ |
| OX Security MCP supply-chain advisory | https://www.ox.security/blog/mcp-supply-chain-advisory-rce-vulnerabilities-across-the-ai-ecosystem/ |
| CSA research note ("MCP by Design") | https://labs.cloudsecurityalliance.org/research/csa-research-note-mcp-by-design-rce-ox-security-20260420-csa/ |
| CVE-2026-30623 (LiteLLM, StdioServerParameters class) | https://nvd.nist.gov/vuln/detail/CVE-2026-30623 |
| CVE-2026-33032 (nginx-ui, distinct) | https://nvd.nist.gov/vuln/detail/CVE-2026-33032 |
| Straiker STAR Labs — SmartLoader/Oura report | https://www.straiker.ai/blog/smartloader-clones-oura-ring-mcp-to-deploy-supply-chain-attack |
| MCP servers at first glance (5.5%/1,899; 66% code smells) | https://arxiv.org/abs/2506.13538 |
| MCPTox (tool-poisoning success rates) | https://arxiv.org/abs/2508.14925 |
| AgentSeal — 1,808-server scan (66% security findings) *(site bot-blocks fetchers; title verified via search index)* | https://agentseal.org/blog/mcp-server-security-findings |
| AgentSeal — toxic data flows (555/5,125) *(same caveat)* | https://agentseal.org/blog/toxic-data-flows-mcp-servers |
| IETF ID-JAG draft (-04) | https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/ |
