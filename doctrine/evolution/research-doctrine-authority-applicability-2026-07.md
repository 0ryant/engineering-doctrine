# Research: Doctrine Authority, Applicability, Exceptions, And Control Lifecycle (2026-07)

**Purpose:** Test external feedback about normative precision, applicability,
exceptions, control cost, and information architecture against primary sources
and the current library.

**Decision records:** [ADR 0028](../../docs/adr/0028-adopt-claim-level-authority-applicability-and-exceptions.md)
and [ADR 0029](../../docs/adr/0029-adopt-a-compact-non-duplicative-core-constitution.md).

**Normative landing:** [Normative Language, Applicability, And Exceptions](../patterns/normative-language-applicability-and-exceptions.md).

---

## 1. Trigger And Existing Evidence

A substantive 2026 external review praised the library's separation of
principles, patterns, checklists, tooling, and estate choices, but challenged
its excess breadth at the point of use, duplicated authority, universal
wording, weak general applicability model, fragmented exceptions, and lack of
control-retirement mechanics. The review is proposal evidence, not authority.

Repository inspection supports the structural part of that diagnosis:

- [ENGINEERING.md](../../ENGINEERING.md) combines headline principles,
  implementation examples, detailed controls, a document catalogue, and a
  bootstrap checklist;
- [how-to-read-this-doctrine.md](../patterns/how-to-read-this-doctrine.md)
  previously allowed the umbrella to lag and instructed readers to resolve
  conflicts by selecting another source;
- applicability is already strong for AI materiality and
  [revision-pinned external profiles](../patterns/revision-pinned-control-profiles.md),
  but is not expressed once for the wider library; and
- exception fields exist in the
  [engineering-controls governance pattern](../patterns/engineering-controls-governance-program.md)
  and external profiles, but there is no compact general contract.

The research question is therefore not whether to add another content layer.
It is how to make claim strength, applicability, evidence, and exception
authority explicit while preserving the storage taxonomy adopted by
[ADR 0003](../../docs/adr/0003-split-doctrine-into-principles-patterns-tooling-checklists-and-evolution.md).

## 2. Primary Sources And Limits

Sources were re-opened on 2026-07-17. The last column prevents guidance from
being promoted beyond what the source establishes.

| Source | What it supports | Limit |
| --- | --- | --- |
| [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.html) and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174.html), BCP 14 | Defined meanings for capitalised `MUST`, `SHOULD`, `MAY`, and related terms; uppercase distinguishes the special meaning; imperatives should be used carefully rather than to impose an unnecessary implementation method. | BCP 14 is a writing convention for IETF specifications. This library adopts its vocabulary; the RFCs do not make any engineering control applicable. RFC 8174 also confirms that normative prose can exist without these keywords. |
| [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) and [SP 1301](https://csrc.nist.gov/pubs/sp/1301/final) | Outcome-focused guidance; organisational profiles tailor, assess, and prioritise outcomes using mission objectives, stakeholder expectations, threats, and requirements. | CSF profiles are cybersecurity-risk constructs, not a ready-made universal engineering taxonomy. The applicability dimensions in this note are repository synthesis. |
| [NIST SP 1302](https://csrc.nist.gov/pubs/sp/1302/final) | CSF Tiers characterise the rigour of cybersecurity risk governance and management and can be applied to organisational profiles. | Tiers do not represent system criticality, data class, or change autonomy. This library must not relabel those dimensions as NIST Tiers. |
| [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) and [SP 800-53B](https://csrc.nist.gov/pubs/sp/800/53/b/upd1/final) | Controls are flexible and customisable; baselines, scoping, organisation-defined parameters, tailoring, compensating controls, and overlays adapt protection to mission, requirements, risk, and operating context. | These publications serve security and privacy risk management, including US federal baselines. Their catalogues do not become this library's general baseline. |
| [NIST SP 800-37 Rev. 2](https://csrc.nist.gov/pubs/sp/800/37/r2/final) | A structured but flexible lifecycle connects selection, implementation, assessment, authorisation, accountability, continuous monitoring, and cost-effective risk decisions. | It does not prescribe this library's exception record or authorisation roles for every adopter. |
| [NIST IR 8286A Rev. 1](https://csrc.nist.gov/pubs/ir/8286/a/r1/final) | Risk scenarios and registers retain impact information so risk response and monitoring can be prioritised and communicated. | It is cybersecurity enterprise-risk guidance. The doctrine exception fields below are a portable synthesis, not a reproduction of its schema. |
| [NIST SP 800-218, SSDF 1.1](https://csrc.nist.gov/pubs/sp/800/218/final) | A core set of outcome-oriented secure-development practices can be integrated into different SDLC implementations; notional examples are not the only implementation choices. | SSDF does not set the authority strength or applicability of every non-security claim in this library. |
| [RFC 9110, HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html#name-idempotent-methods) | Idempotency is defined for request methods by intended effect and is important at automatic-retry boundaries; non-idempotent requests require knowledge or detection before automatic retry. | It does not say that every domain state transition is idempotent. The broader cross-boundary rule is repository synthesis. |
| [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) | Security logging content should be set during design and proportionate to risk; audit, transaction, and security logs can have distinct purposes; excessive blind logging creates noise and privacy exposure. | OWASP cheat sheets are practitioner guidance, not law and not a complete audit-control profile. |
| [OWASP Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) | Use maintained secure storage mechanisms where available, authenticated encryption, sound key management, and context-appropriate approved algorithms; do not design custom algorithms. | Concrete algorithms and parameters remain profile-, platform-, threat-, and regulation-dependent. |
| [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) | Password storage is a specialised hashing problem; Argon2id is the preferred general recommendation, scrypt is a fallback, and bcrypt is limited to legacy cases where newer choices are unavailable. | It does not justify treating bcrypt as a general password-derived key mechanism. Parameters change and belong in maintained security guidance. |

## 3. Findings

### 3.1 Strength, Applicability, And Content Class Are Separate

BCP 14 provides useful claim-level strength, but it does not answer whether a
claim applies. Applicability must be decided first. A `MUST` within a declared
public-service or contractual profile is not a universal rule for an unrelated
local utility.

`CONTEXT-DEPENDENT` and `EXAMPLE` are therefore content classes in this
library, not additions to BCP 14. The former requires an explicit trade-off;
the latter carries no obligation. A document can contain several strengths and
classes, so one document-wide `level: should` label would create false
precision.

### 3.2 Applicability Is A Composable Overlay

The existing layer taxonomy answers where content belongs. A separate overlay
answers what a consumer activates. The portable dimensions are:

- exposure;
- criticality and blast radius;
- data sensitivity and external obligations;
- operational model and recoverability;
- change autonomy;
- consumer compatibility; and
- observability of success and failure.

Named profiles may compose these dimensions. An external authority profile may
add non-negotiable requirements. When applicable controls overlap, the consumer
must satisfy all compatible obligations and use the stricter result; a genuine
conflict is an authority decision, not permission to choose the convenient
rule.

### 3.3 Exceptions Are Separate Authority Records

The general exception contract is synthesized from existing doctrine, NIST's
risk/authorisation lifecycle, and risk-register guidance. It retains the rule
and evidence result unchanged while separately recording authority, scope,
rationale, residual risk, compensating controls, evidence, owner, remediation,
effective period, review, and expiry detection.

The library cannot grant a waiver from law, regulation, contract, or an
external control profile. Only the authority recognised by that source can
approve a permitted variance. Live exception registers belong to adopting
organisations, not this public repository.

### 3.4 Controls Need A Lifecycle

NIST CSF, RMF, and SSDF all connect practices to outcomes, risk, accountability,
assessment, and improvement. This library synthesizes an anti-bureaucracy test:
every new or materially expanded control identifies the failure it addresses,
expected evidence, operating cost, accountable owner, review trigger, and the
condition for simplification or retirement. This is not a claim that every
control has a single causal metric; evidence limitations remain explicit.

### 3.5 The Umbrella Needs One Bounded Authority Surface

The existing principle/pattern/tooling/checklist/evolution split remains valid.
The missing view is a compact constitution that owns only the memorable core,
normative vocabulary, applicability/exception entry points, adoption route, and
links to canonical detail. Detailed requirements remain authoritative in their
topic principles or activated patterns. A conflict between the core and a
canonical detail source is a defect to repair, not a precedence feature.

## 4. Decision Ledger

| Proposal | Disposition | Basis |
| --- | --- | --- |
| Capitalised claim-level `MUST`, `SHOULD`, and `MAY` | **Take** | BCP 14 supplies established meanings and warns against unnecessary prescription. |
| `CONTEXT-DEPENDENT` and `EXAMPLE` as additional requirement levels | **Reject as requirement levels; take as content classes** | They answer different questions from BCP 14 strength. |
| Composable applicability dimensions and named profiles | **Take as library synthesis** | Consistent with NIST profile, tailoring, and risk-context mechanisms without copying a security catalogue. |
| Portable, expiring exception record | **Take as library synthesis** | Existing doctrine already requires most fields; RMF and risk-register sources support separate authorisation, response, and monitoring. |
| Exception changes a failed or absent result to pass | **Reject** | It destroys evidence integrity and conflicts with existing external-profile doctrine. |
| Live root exception register | **Reject** | It would publish one adopter's decisions and confuse a template with a system of record. |
| Control effectiveness, cost, review, and retirement fields | **Take as library synthesis** | Risk-based selection and continuous improvement require controls to remain purposeful and reviewable. |
| Compact core constitution | **Take** | Removes duplicated authority while preserving canonical depth. |
| New physical directories for core/default/profile/reference tiers | **Reject** | Applicability is an overlay; ADR 0003's layer taxonomy remains valid. |
| Strength metadata on every document in this release | **Defer** | Claim-level semantics should be established before a 100-plus-file metadata migration. |
| Universal idempotency, audit-everything, mandatory TDD, fixed layering, and umbrella algorithm menus | **Replace with scoped claims** | RFC 9110, OWASP guidance, and the sources above support boundary-, risk-, and profile-aware wording rather than universal implementation rules. |

## 5. Measures And Residual Limits

Implementation should measure outcomes rather than document volume:

- sampled material claims whose strength, applicability, evidence, and
  exception path can be identified without inference;
- unresolved conflicts or duplicated normative owners;
- active and expired exception age, compensating-control evidence, and closure;
- controls simplified or retired after review, alongside resulting incidents
  or regressions; and
- representative navigation tasks that reach the canonical source without
  treating research or examples as authority.

Residual limits:

- The proposed applicability dimensions are this library's synthesis and need
  consumer-specific values; no source establishes one universal scoring model.
- Stronger wording can create unnecessary cost; weaker wording can remove a
  necessary safety boundary. Each replacement claim still needs topic-source
  review and consumer-impact labelling.
- A recorded exception can become ceremonial approval if authority,
  compensating evidence, and expiry are not enforced.
- No cited source proves that a ten-proposition constitution is the optimum
  length. Compactness is judged by recall, routing, and absence of duplicated
  authority, not a line quota.

**Change class:** research and decision evidence. This note creates no adopter
obligation by itself.
