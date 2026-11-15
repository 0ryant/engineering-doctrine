# Latest Developments Source Check

Date and source access date: 2026-11-15. Repository basis: `54fd5f39383c081fc62b3ccbae44735069e31201`.
Status: non-normative research record. It adopts no control, changes no consumer obligation, and approves no release.

## Question

What changed between roughly 2026-08-01 and 2026-11-15 in the standards, regulations, specifications, and guidance this library cites, and which changes affect doctrine rather than only citations?

## Method And Limits

Four delegated model agents each checked one domain against the library's existing pins in [REFERENCES.md](../REFERENCES.md) and the most recent landscape notes: AI agent protocols and identity; supply chain, secure development, and cryptography; AI governance and regulation; and delivery, APIs, operability, and accessibility. Each agent read live publisher pages and returned a ledger with its own verification state. The lead author then re-read the primary page for the claims that drive the headline findings.

Verification states used below:

- **V1** — primary page read and the relevant passage checked by the lead author in this session.
- **V2** — primary page read by a delegated agent; not re-checked by the lead author.
- **V3** — secondary sources only. Not admissible as grounding until a primary read.

Source classes follow [Source Authority And Evidence Grading](../patterns/source-authority-and-evidence-grading.md) §2. No archive copies were captured, and access dates are not revision pins. This is model research and model self-review, not independent human or domain review. Search coverage for September to November 2026 may be thin, so absence of a row is not evidence that nothing changed.

## Headline Findings

These affect doctrine, not just citations. Each is a candidate for a separate decision through the [change harness](../patterns/doctrine-library-change-harness.md); none is adopted here.

| # | Finding | Library gap | Suggested route |
| ---: | --- | --- | --- |
| 1 | **Post-quantum transition now has dates.** NIST IR 8547 was published final on 2026-10-27 (V1). The final text deprecates quantum-vulnerable public-key algorithms after 2030 and disallows them after 2035 (V2). US federal policy M-26-15 sets 2030–2031 deadlines for high-value systems (V2). | [API boundaries](../principles/api-boundaries-and-security.md) §2.1 already binds algorithms to maintained profiles, and [ADR 0022](../../docs/adr/0022-hash-function-convergence-blake3-ed25519-hmac.md) rejected a fixed menu. The library has no cryptographic inventory or agility expectation and no PQC citation. | Candidate ADR: cryptographic inventory and agility, with transition dates bound through [revision-pinned profiles](../patterns/revision-pinned-control-profiles.md), not a portable algorithm list. |
| 2 | **Valid build provenance does not prove an uncompromised build.** An analysis on the SLSA project's blog (2026-05-15, named practitioner author) of the TanStack npm compromise reports attestations that were "cryptographically valid" because the attacker used the legitimate pipeline's identity (V1). It recommends expected-builder checks, source attestations, verification summaries, and cache isolation. npm has since tightened trusted publishing and install-time defaults (V2). | [Dependencies](../principles/dependencies-supply-chain.md) §4 says provenance makes tampering detectable, which overstates it for in-pipeline compromise. Consumer-side verification policy and a publish-side long-lived-token rule are absent. Interacts with the open M16 SLSA decision. | Candidate ADR, paired with the M16 decision. |
| 3 | **EU Cyber Resilience Act reporting is live.** Manufacturers' obligations to report actively exploited vulnerabilities and severe incidents apply from 2026-09-11 through the ENISA single reporting platform (V1). The regulation's staged deadlines are an early warning within 24 hours, a notification within 72 hours, and a final report later (V2). | [Secure development lifecycle](../principles/secure-development-lifecycle.md) vulnerability response has no hook for a regulatory reporting clock. | Candidate profile-gated addition through revision-pinned profiles, activated only for manufacturers in scope; compare the existing Art 50 profile gate in [privacy](../principles/privacy-and-data-governance.md) §5.4. |
| 4 | **EU AI Act timeline changed.** The official timeline now shows Annex III high-risk rules from 2027-12-02 and Annex I from 2028-08-02, with a transitional deadline of 2026-12-02 for Art 50(2) providers already on the market before 2026-08-02, and new prohibitions from the same date (V1). The amending regulation is reported as Regulation (EU) 2026/1744 (V2; EUR-Lex text not retrieved). Art 4 literacy now reads as a duty to support literacy rather than ensure a sufficient level (V2). The first harmonised standard, EN 18286 for Art 17 quality management, has been cited (V2). | [ADR 0032](../../docs/adr/0032-add-ai-act-transparency-slopsquatting-gate-and-model-dataset-admission.md)'s Omnibus review trigger has fired. Privacy §5.4 lacks the transitional carve-out. [AI adoption controls](../patterns/ai-adoption-controls.md) §5 quotes superseded Art 4 wording. The 2026-08 gap audit still records the Omnibus as political agreement and zero harmonised standards. | Record the trigger outcome in ADR 0032; editorial updates for the dates and wording. The role-based literacy default stays portable doctrine. |
| 5 | **US model-risk guidance excludes generative and agentic AI.** SR 26-2 (2026-04-17) footnote 3 states that such models "are not within the scope of this guidance" (V1). | [AI adoption controls](../patterns/ai-adoption-controls.md) and [AI and ML-assisted systems](../principles/ai-ml-systems.md) cite SR 26-2 for effective challenge on AI systems including generative and agentic ones. | Editorial scope caveat: the library borrows the vocabulary; the source does not cover these systems. No control changes. |
| 6 | **OWASP published an LLM Top 10 for 2026** on 2026-08-03 (V1 for the page and date; V3 for its entry numbering). Secondary sources report renumbered entries. | Bare `LLM0x` identifiers in AI and ML-assisted systems, AI adoption controls, the agentic-loop crosswalk, and the glossary become ambiguous. | Editorial now: suffix existing identifiers with `:2025`. Adopting the 2026 edition is a separate candidate ADR after reading the PDF. |
| 7 | **The IETF workload-identity practices draft reached the IESG** (V2). It recommends short-lived credentials and says environment variables must not deliver workload identity credentials where the platform offers another method. | [Configuration and secrets](../principles/configuration-and-secrets.md) warns against credentials in environment variables but has no delivery rule. | Watch; consider an owner change when it becomes an RFC. The new [Secretless Workload Identity](../impl/secretless-workload-identity.md) reference cannot carry it first. |

## Corrections Made In This Change

The MCP Skills extension was cited as a stable, S1-equivalent extension at a `specification/stable/` path in [REFERENCES.md](../REFERENCES.md) and the [agent-ready discovery note](research-agent-ready-application-discovery-2026-11.md). The [extensions overview](https://modelcontextprotocol.io/extensions/overview) lists Skills over MCP as **Beta, destination not yet stated**, and the stable path returns HTTP 404 (both V1). Both citations now point to the beta path at S3 provisional, and the overview is added as the lifecycle source. The supported claim was already weak ("can be a protocol surface"), so it survives the downgrade, and the [agent-ready shipping profile](../patterns/agent-ready-application-shipping-profile.md) does not depend on this source. No consumer obligation changes.

The access date recorded on the original row could not have been accurate for a path that already returned 404. That is recorded here rather than rewritten.

## Editorial Batch Applied (2026-11-15)

Applied in the same change at the maintainer's request. Each item restates an external fact or labels a citation; none changes a control, its strength, its applicability, or an exception path. Sources were re-read by the lead author before editing (V1) unless marked.

| Item | Files | Source state |
| --- | --- | --- |
| OWASP LLM identifiers suffixed `:2025`; citations pinned to the 2025 edition page; the 2026 edition recorded as not adopted | [AI and ML-assisted systems](../principles/ai-ml-systems.md), [AI adoption controls](../patterns/ai-adoption-controls.md), [RAG retrieval baseline](../patterns/rag-retrieval-baseline.md), [glossary](../glossary.md), [REFERENCES](../REFERENCES.md) | V1: the rolling list page still presents the 2025 edition and links its 2025 resource page |
| Identity Assertion JWT Authorization Grant pin moved from draft-04 to draft-06 in the informative standards watch | [Zero trust](../principles/zero-trust-and-workload-identity.md) §2.1 | V1: draft-06, WG Document, no last call |
| OAuth 2.1 labelled as an Internet-Draft where doctrine and the glossary name it; the MCP authorization requirement is unchanged and still points at the pinned MCP revision | AI and ML-assisted systems §7, glossary | V1: draft-17, WG Document, IESG submission milestone December 2026 |
| SR 26-2 scope caveat: its footnote 3 excludes generative and agentic AI, so the library uses effective challenge as vocabulary for those systems | AI adoption controls, AI and ML-assisted systems, glossary, REFERENCES | V1 |
| AI Act: Art 50(2) transitional deadline of 2026-12-02 for systems already on the market; Art 4 wording as amended; a REFERENCES row for the amending regulation | [Privacy](../principles/privacy-and-data-governance.md) §5.4, AI and ML-assisted systems, AI adoption controls §§2 and 5, REFERENCES | V1 for the timeline and literacy FAQ; the regulation text itself was not retrieved |
| ADR 0032 review trigger outcome recorded | [ADR 0032](../../docs/adr/0032-add-ai-act-transparency-slopsquatting-gate-and-model-dataset-admission.md), [ADR index](../../docs/adr/README.md) | Same as above |

Headline findings 1–3 and 7 remain candidate decisions. The workload identity reference was renamed and reframed secretless-first at the same time; its [owner audit](research-impl-reference-batch-composition-2026-11.md#owner-audit-secretless-workload-identity) records why that stays within the owners' existing preference.

## Source Ledger

### AI Agents, Protocols, Identity, And Telemetry

| Development | Date | Source and class | Affects | Disposition | Verif. |
| --- | --- | --- | --- | --- | --- |
| MCP extension lifecycle: Experimental, Beta, Stable. Apps and the two authorization extensions are Stable; Tasks is Beta bound for core; Skills and Server Cards are Beta | Oct 2026 | [Extensions overview](https://modelcontextprotocol.io/extensions/overview), S5 | [MCP cross-check](research-mcp-spec-cross-check-2026-08.md) §3.3 is stale; input to the pending AI and ML §7 extensions-posture decision | Feed the pending ADR | V1 |
| MCP moves to a six-month release cycle; next revision 2027-03-30; 2026-07-28 remains current | 2026-11-11 | [MCP blog](https://blog.modelcontextprotocol.io/posts/mcp-release-cycle/), S5 | Revision-pinning cadence in AI and ML §7 | Editorial cadence note | V2 |
| MCP roadmap prioritises agent identity (DPoP, workload identity federation with identity-assertion grants) | 2026-08-22 | [MCP roadmap](https://blog.modelcontextprotocol.io/posts/mcp-roadmap/), S5, roadmap only | Zero trust §2.1 standards watch | Watch | V2 |
| Experimental MCP file transfer extension with an open credential-redirection risk | 2026-11-10 | [MCP blog](https://blog.modelcontextprotocol.io/posts/exploring-file-uploads-and-downloads-in-mcp/), S5 experimental | New trust surface | Watch | V2 |
| A2A and Agent Skills moved under a Linux Foundation agentic AI fund; spec content unchanged | Aug–Nov 2026 | [Foundation announcement](https://www.linuxfoundation.org/press/agentic-ai-foundation-announces-four-new-projects-agent-skills-open-responses-openenv-and-opensandbox), S7 for governance facts | Governance context only | Editorial | V2 |
| OWASP LLM Top 10 2026 | 2026-08-03 | [OWASP resource](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/), S4 awareness document | Headline 6 | See headline | V1 date; V3 entries |
| OWASP Securing Agentic Applications V2 supersedes v1.0; Agent Control Standard and GenAI red-teaming manual published | Sep–Nov 2026 | [OWASP GenAI resources](https://genai.owasp.org/resources/), S4 | Gap-audit §2.2 citation | Update citation after reading | V2 dates only |
| US executive order relabels "AI" as "Super Intelligence/SI" in agency materials; NIST renamed COSAiS to COSIS and states that issued documents are unaltered | 2026-09-29; 2026-10-20 | [NIST COSIS project page](https://csrc.nist.gov/projects/cosais), S2 | NIST row titles and URLs in REFERENCES and zero trust §2.1 | Keep "AI" as doctrine vocabulary and issued titles; note the alias; watch URL drift | V1 |
| NCCoE agent identity project still at concept paper; practice guide planned | checked 2026-11-15 | [NCCoE project](https://pages.nist.gov/nccoe-ai-identity/), S2 | Existing citation remains accurate | No action | V2 |
| Identity Assertion JWT Authorization Grant now draft-06 | 2026-10-30 | [IETF datatracker](https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/), S3 | Zero trust §2.1 cites draft-04 | Update the pin | V2 |
| WIMSE adopted an AI identity management draft; HTTP signature profile and workload identity practices sent to the IESG; RFC 10070 fixes an audience vulnerability in assertion grants | Sep–Nov 2026 | [WIMSE documents](https://datatracker.ietf.org/wg/wimse/documents/), S3; [RFC 10070](https://www.rfc-editor.org/info/rfc10070), S1 | Zero trust §2 and §2.1 | Watch; consider citing RFC 10070 | V2 |
| OpenTelemetry GenAI conventions remain Development, with breaking renames in November | Oct–Nov 2026 | [GenAI semconv repository](https://github.com/open-telemetry/semantic-conventions-genai), S3 | The commit pin in [observability tooling](../tooling/observability.md) still protects consumers | No action until adoption | V2 |

### Supply Chain, Secure Development, And Cryptography

| Development | Date | Source and class | Affects | Disposition | Verif. |
| --- | --- | --- | --- | --- | --- |
| NIST IR 8547 final: transition to post-quantum cryptography standards | 2026-10-27 | [NIST IR 8547](https://csrc.nist.gov/pubs/ir/8547/final), S2 | Headline 1 | Candidate ADR | V1 status and date; V2 dates in the text |
| US federal PQC migration memorandum M-26-15 | 2026-06-24 | [OMB M-26-15](https://www.whitehouse.gov/wp-content/uploads/2026/06/M-26-15-Execution-of-the-Migration-to-Post-Quantum-Cryptography.pdf), S2 | Headline 1; next to the existing OMB citation in merge-path | Fold into the headline 1 ADR | V2 |
| SLSA analysis: valid provenance from a compromised pipeline | 2026-05-15 | [SLSA blog](https://slsa.dev/blog/2026/05/mini-shai-hulud-what-slsa-can-and-cannot-do), S6 named practitioner on the project site | Headline 2 | Candidate ADR | V1 |
| npm v12 disables install scripts and git or remote dependencies by default; 2FA-bypass tokens lose publish rights; unvalidated trusted-publishing configurations expire | Jul–Oct 2026 | [GitHub changelog](https://github.blog/changelog/2026-07-08-npm-install-time-security-and-gat-bypass2fa-deprecation), S5 | Dependencies §7 install-script advice is now the npm default | Editorial; evidence for headline 2 | V2 |
| CRA single reporting platform live; manufacturers' reporting applies from 2026-09-11; stewards from 2027-12-11 | 2026-09-11 | [ENISA](https://www.enisa.europa.eu/news/the-cra-single-reporting-platform-is-launched), S2; [Commission CRA reporting](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting), S2 | Headline 3 | Candidate profile gate | V1 dates; V2 deadlines |
| CRA harmonised standards progressing; none cited in the Official Journal yet | Jul–Nov 2026 | Independent guide, S7 | Future dependencies and secure-development citations | Watch | V3 |
| CISA 2026 SBOM minimum elements replace the 2021 NTIA list | 2026-07-29 | [CISA](https://www.cisa.gov/resources-tools/resources/2026-minimum-elements-software-bill-materials-sbom), S2 | Dependencies and REFERENCES still name NTIA; merge-path already cites CISA | Resolve with the open SBOM baseline decision, not alone | V2 |
| NVD moves to risk-based enrichment and no longer adds its own CVSS where the numbering authority scored | 2026-04-15 | [NIST notice](https://www.nist.gov/node/1910421), S2 | Triage in secure development §3 and dependencies §2 implicitly assume NVD enrichment | Editorial caveat: use advisory and OSV data as well | V2 |
| OWASP Top 10:2025 live, with supply-chain failures at A03 | 2025–2026 | [OWASP Top 10](https://top10.owasp.org/2025), S4 awareness | Not cited; scorecard already logs the gap | Optional risk-salience citation | V2 list; V3 date |
| CWE 5.0 schema with breaking structural changes; no 2026 Top 25 yet | 2026-10-28 | [CWE news](https://cwe.mitre.org/news/archives/news2026.html), S1 for CWE | Tooling that consumes CWE data | Watch | V2 |

### AI Governance And Regulation

| Development | Date | Source and class | Affects | Disposition | Verif. |
| --- | --- | --- | --- | --- | --- |
| EU AI Act implementation timeline after the AI Omnibus | in force 2026-07 | [AI Act Service Desk timeline](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act), S2 | Headline 4 | Record ADR 0032 trigger outcome; editorial | V1 |
| Amending regulation identified as (EU) 2026/1744 | 2026-07 | [Commission AI framework page](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai), S2 | REFERENCES lacks a row for the amending act | Add the canonical ELI after a EUR-Lex read | V2 number; V3 OJ date |
| Art 4 literacy reworded | 2026-07 | [Commission AI literacy FAQ](https://digital-strategy.ec.europa.eu/en/faqs/ai-literacy-questions-answers), S2 | AI adoption controls §5 | Editorial | V2 |
| EN 18286 cited as the first harmonised standard under the AI Act | ~2026-10-14 | [Commission announcement](https://digital-strategy.ec.europa.eu/en/library/first-harmonised-standard-supporting-ai-act-published-official-journal), S2 | Gap audit row on harmonised standards | Optional grounding; watch further standards | V2 |
| Art 50 guidelines possibly formally adopted on 2026-11-05 | 2026-11-05 | [Commission guidelines page](https://digital-strategy.ec.europa.eu/en/library/guidelines-transparency-obligations-providers-and-deployers-ai-systems), S2 | REFERENCES Art 50 guidelines row | Pin once the adopted reference is confirmed | V2 page; V3 reference number |
| SR 26-2 excludes generative and agentic AI | 2026-04-17 | [SR 26-2 attachment](https://www.federalreserve.gov/supervisionreg/srletters/SR2602a1.pdf), S2 | Headline 5 | Editorial scope caveat | V1 |
| FCA AI good-practice publication: non-binding; covers ownership, monitoring, automation bias, exit planning, agent inventories | 2026-10-19 | [FCA](https://www.fca.org.uk/publications/good-poor-practice/ai-financial-services), S2 | Corroborates AI adoption controls §§1–5 | Optional corroborating citation | V2 |
| NIST states the AI RMF is being revised; no draft or date | ongoing | [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework), S2 | GOVERN references may renumber | Watch | V2 |
| ISO/IEC 27090 reported published | 2026-10-14 | ISO catalogue (not retrievable), V3 | Gap audit lists it as FDIS | Confirm before citing | V3 |
| UK AI risk package explores incident reporting; no AI bill | 2026-10-12 | [UK government](https://www.gov.uk/government/news/britain-steps-up-national-defences-against-growing-ai-risks), S2 | None yet | Watch | V2 |

US state AI laws (Colorado's replacement act, California, Texas) and federal preemption activity were checked for status only. The library does not cite them, and no row is proposed.

### Delivery, APIs, Operability, And Accessibility

| Development | Date | Source and class | Affects | Disposition | Verif. |
| --- | --- | --- | --- | --- | --- |
| DORA 2025 State of AI-assisted Software Development and the AI Capabilities Model | 2025-09-23 | [DORA 2025 report](https://dora.dev/research/2025/dora-report/), S4 | Developer experience and SRE citations name only the 2024 report | Update citation | V2 |
| DORA reportedly will not publish a 2026 report | 2026-09 | Social post and trade press, S7 | Avoid waiting for a 2026 edition | Watch; do not cite S7 | V3 |
| Idempotency-Key header draft-08, RateLimit fields draft-11, and OAuth 2.1 draft-17 all remain Internet-Drafts; OAuth 2.1 targets IESG submission in December 2026 | Oct 2026 | [IETF datatracker](https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/), S3 | AI and ML §7 and REFERENCES say "OAuth 2.1" without the draft label | Editorial label | V2 |
| HTTP API credential-protection BCP in the RFC Editor queue | 2026 | [IETF datatracker](https://datatracker.ietf.org/doc/draft-ietf-httpapi-privacy/), S3 | API boundaries §§1–2 | Cite on publication | V2 |
| Pre-window gap: RFC 9745 Deprecation header, RFC 9727 API catalog, RFC 9700 OAuth security BCP | 2025 | [RFC 9745](https://www.rfc-editor.org/info/rfc9745), [RFC 9700](https://www.rfc-editor.org/info/rfc9700), S1 | API boundaries §9 inventory and sunset; §2 OAuth | Update citations | V2 |
| OpenTelemetry semantic conventions v1.45.0: RPC stable; messaging attributes renamed; opt-in HTTP body attributes flagged as possibly sensitive | 2026-11-02 | [Release notes](https://github.com/open-telemetry/semantic-conventions/releases/tag/v1.45.0), S5 | Observability tooling; body capture conflicts with the content-not-captured default posture | Editorial caution in tooling | V2 |
| Kubernetes v1.37: pod certificates and cluster trust bundles GA; v1.36: user namespaces GA | 2026-04 to 2026-08 | [Kubernetes release blog](https://kubernetes.io/blog/2026/08/26/kubernetes-v1-37-release/), S5 | Kubernetes platform security and zero trust §2 examples | Editorial | V2 |
| Ingress-NGINX retired 2026-03-24 with an explicit security warning | 2026-01-29 statement | [Kubernetes statement](https://kubernetes.io/blog/2026/01/29/ingress-nginx-statement/), S5 | Kubernetes platform security; platform readiness | Editorial, phrased as end-of-life edge components | V2 |
| OpenFeature specification v0.9.0 with three breaking changes | 2026-08-12 | [OpenFeature update](https://openfeature.dev/blog/openfeature-mid-2026-update), S5 | Flag patterns cite the spec unpinned | Pin and check the breaking changes against evaluation-context claims | V2 |
| EN 301 549 V4.1.1 aligned to WCAG 2.2; Official Journal citation pending | 2026-09 | [ETSI](https://www.etsi.org/deliver/etsi_en/301500_301599/301549/04.01.01_60/en_301549v040101p.pdf), S1 | User-facing quality cites neither EN 301 549 nor the European Accessibility Act | Update citations after the OJ citation | V2 publication; V3 OJ status |

## Checked, No Material Change

- MCP core revision 2026-07-28 remains current; the registry remains preview with downstream scanning.
- A2A remains v1.0.1; the Agent Skills specification content is unchanged; AGENTS.md has no versioned specification.
- OWASP Agentic Top 10 2026 and the secure MCP server guide are unchanged.
- NIST SSDF: SP 800-218 Rev. 1 is still a draft, so the v1.1 final pin stands. SP 800-53 Release 5.2.0 is still current. SP 800-131A Rev. 3 is still a draft.
- SLSA v1.2 remains current; additional tracks are working drafts.
- AI 600-1, AI 100-2 E2025, ISO/IEC 42001, and PRA SS1/23 show no supersession.
- CloudEvents v1.0.2, RFC 9457, the five DORA delivery metrics, OpenTelemetry profiles (alpha), and the Collector (pre-1.0) are unchanged.

## Watch List And Triggers

| Item | Re-check when |
| --- | --- |
| MCP next core revision | 2027-03-30 release |
| OAuth 2.1, workload identity practices, Idempotency-Key, RateLimit fields | RFC publication |
| CRA harmonised standards and EN 301 549 V4.1.1 | Official Journal citation |
| NIST AI RMF revision, Cyber AI Profile, agent identity practice guide | Draft publication |
| OWASP LLM Top 10 2026 | Before any adoption decision (read the PDF) |
| CWE Top 25 2026 | Publication |
| CNSA 2.0 acquisition milestone | 2027-01-01 |

## Relationship To The Implementation References

The three references added alongside this note compose the current owners, and none of these findings changes an owner they cite today. Two findings could change those owners later: the workload identity delivery rule (configuration and secrets, zero trust) and the HTTP API standards (API boundaries). If adopted, the owner changes first and the reference follows.

## Consumer Impact

Change class: **editorial / navigation** for the citation correction and the editorial batch; the rest of this note is evidence only. No control, applicability rule, exception path, or consumer baseline changes. Every headline finding needs its own decision and consumer-impact review before it can affect adopters.

## Residual Risk

Most rows are V2: an agent read the primary page, but the lead author did not re-check it. Rows marked V3 are not admissible grounding. The research is model-run with model review and no independent human check. No archive captures exist, so later publisher edits cannot be distinguished from these readings. Time-sensitive items, especially the 2026-12-02 AI Act transitional deadline, may need action before the next sweep.
