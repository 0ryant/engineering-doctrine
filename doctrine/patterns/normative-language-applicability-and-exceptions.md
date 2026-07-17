# Normative Language, Applicability, And Exceptions

Use this pattern to decide what a doctrine claim means, when it applies, what
evidence it expects, and how an authorised exception remains separate from the
underlying result. It implements [ADR 0028](../../docs/adr/0028-adopt-claim-level-authority-applicability-and-exceptions.md).

The core rule is:

> Determine applicability before enforcing strength. Keep the rule, evidence,
> authority decision, and exception as separately addressable records.

Research and source limits are recorded in
[research-doctrine-authority-applicability-2026-07.md](../evolution/research-doctrine-authority-applicability-2026-07.md).

---

## 1. Normative Strength And Content Class

This library uses the capitalised terms below with the meanings defined by
[BCP 14](https://www.rfc-editor.org/info/bcp14),
[RFC 2119](https://www.rfc-editor.org/rfc/rfc2119.html), and
[RFC 8174](https://www.rfc-editor.org/rfc/rfc8174.html). Only the capitalised
forms carry those special meanings. Lower-case words keep their ordinary
English meaning.

| Form | Meaning in this library | Authoring test |
| --- | --- | --- |
| `MUST` / `MUST NOT` | Required or prohibited within the claim's declared scope. | Would departure break an authority obligation, interoperability boundary, evidence integrity, or a safety/security property with generally unacceptable harm in that scope? |
| `SHOULD` / `SHOULD NOT` | Strong default. A different course can be valid only after its implications are understood and, when material to the adopting surface or its evidence, the reason is recorded. | Can a competent adopter name a bounded context where another choice achieves the outcome without unacceptable risk? |
| `MAY` | Permitted option, not a recommendation or obligation. | Would implementations remain conformant whether they select the option or not? |
| `CONTEXT-DEPENDENT` | Library content class requiring an explicit decision and trade-off analysis. It is not a BCP 14 keyword. | Do exposure, materiality, architecture, compatibility, observability, or cost determine the answer? |
| `EXAMPLE` | Non-normative illustration. | Could an adopter replace it while preserving every applicable outcome and constraint? |

BCP 14 does not require every normative sentence to contain a keyword. This
library nevertheless uses the keywords for material claims where ordinary
prose would leave strength ambiguous. Bold type, a checklist box, or an
imperative tone does not create authority by itself.

Do not assign one strength to a whole mixed document. A principle can contain a
`MUST`, several `SHOULD` defaults, context-dependent trade-offs, and examples.

## 2. Claim Anatomy

A material doctrine claim should make these elements discoverable in the claim
or its immediate section:

| Element | Question |
| --- | --- |
| Identity and owner | Which canonical section owns the claim and who is accountable for interpreting it in the adopting organisation? |
| Strength or class | Is it `MUST`, `SHOULD`, `MAY`, `CONTEXT-DEPENDENT`, or `EXAMPLE`? |
| Outcome or failure | What property is preserved, or what failure is prevented? |
| Applicability | Which surfaces, profiles, authority sources, or conditions activate it? |
| Evidence | What observable result can support or falsify the claim? |
| Exception | Is departure permitted, who can authorise it, and what record is required? |
| Lifecycle | What triggers review, and when can the control be simplified or retired? |

Not every sentence needs a schema. These elements are required where a
reasonable reader could otherwise disagree about obligation, scope, proof, or
authority.

## 3. Applicability Overlay

Applicability is an overlay on the existing principle, pattern, checklist,
tooling, and evolution layers. It does not create a new directory hierarchy.

Classify the dimensions that materially affect the decision. Example values
are prompts, not a universal scoring system.

| Dimension | Questions | Example values |
| --- | --- | --- |
| **Exposure** | Who can invoke, observe, or depend on the surface? | local, internal, partner, public |
| **Criticality and blast radius** | What fails, who is affected, and how far can failure propagate? | low, material, critical; one user, one tenant, multi-tenant, estate-wide |
| **Data and external obligations** | What information or binding authority is in scope? | public, internal, confidential, personal, regulated; contract or control-profile identifier |
| **Operational model and recoverability** | When must it operate and how reversible is failure? | ad hoc, business-hours, 24/7; reversible, compensatable, irreversible |
| **Change autonomy** | Who or what may propose, execute, authorise, and enact change? | human-only, AI-assisted, governed agent execution, agent-enacted through bounded non-model authority controls |
| **Consumer compatibility** | Who upgrades independently and what stability is promised? | single owner, internal multi-team, partner, public contract |
| **Observability** | Can success, failure, drift, and rollback be discriminated promptly? | strong, partial, weak; deterministic check, sampled evaluation, delayed outcome |

### Composition Procedure

1. **Establish the baseline.** Identify the portable core and topic principles
   relevant to the surface.
2. **Record material dimensions.** Do not classify dimensions that cannot
   change the selected control.
3. **Activate named profiles.** Examples include public service, critical
   production, regulated data, platform/infrastructure, AI-assisted delivery,
   or governed agent enactment.
4. **Add external authority.** When law, regulation, contract, or a voluntarily
   adopted framework applies, use
   [revision-pinned external control profiles](revision-pinned-control-profiles.md).
5. **Compose obligations.** Satisfy all compatible applicable claims. Where two
   controls protect the same property, use the stricter result. Where methods
   or authorities conflict, record the conflict and obtain an accountable
   decision.
6. **Bind evidence and exceptions.** Evidence and any authorised departure
   identify the exact claim, scope, candidate/system state, and time they
   cover.

Higher materiality does not always mean more documents or approvals. It means
more discriminating evidence, tighter authority, smaller blast radius, or
stronger recovery where those controls address the actual failure.

## 4. Worked Applicability Examples

These examples apply the same model to existing doctrine concerns and show why
one universal checklist is insufficient.

| Surface | Classification | Result |
| --- | --- | --- |
| Local, single-owner formatting utility with no sensitive data or deployment authority | Local exposure; low blast radius; human-run; reversible; strongly observable | Baseline source control and a repeatable quality check apply. A 24/7 SLO, formal privileged-action audit trail, and production release authorisation do not activate. |
| Public account service processing personal data | Public; material or critical; confidential/personal data; independent consumers; 24/7; partial reversibility | Boundary contracts, threat modelling, protected merge/release, privacy controls, SLO/incident ownership, and durable audit evidence for authentication, privilege, security-policy, and materially consequential actions activate. |
| Agent-produced change to production identity policy | High blast radius; security-sensitive; governed agent execution; weakly reversible; externally consequential | The agent may propose inside a bounded execution contract. Diverse challenge evidence, accountable human approval, least-privilege enactment of the authorised candidate, action receipts, rollback/containment, and runtime reconciliation activate. The producing agent cannot be sole verifier or authoriser. |

The examples do not create three fixed profiles or waive a stricter external
requirement. Adopters record the profile combinations that recur in their own
estate.

## 5. Exception Contract

An exception is a bounded authority decision to accept a stated deviation or
residual risk. It is not an edit to the rule and not a favourable test result.

### Minimum Record

| Field | Minimum content |
| --- | --- |
| Identity | Stable exception ID, status, created/effective dates. |
| Rule and profile | Canonical claim reference, doctrine/profile version, and any external authority source. |
| Exact scope | Systems, repositories, services, data, environments, actions, consumers, and excluded scope. |
| Finding and evidence | Actual result, evidence references, observation date, and known uncertainty. Preserve `fail`, `inconclusive`, absent, or stale states. |
| Rationale and residual risk | Why the default cannot currently be met, affected outcomes, likelihood/impact assumptions, and who bears the risk. |
| Authority | Requestor, accountable approver, and evidence that the approver may decide for this rule and scope. |
| Compensating control and detection | Alternative protection, monitoring, containment, and evidence that they operate. |
| Remediation | Owner, target state, work link, dependencies, and completion evidence. |
| Time bounds | Expiry, review trigger/cadence, renewal limit, and behaviour on expiry. |
| Closure | Closed, replaced, expired, or revoked state; final evidence and decision. |

### Admissibility Rules

1. The approving authority `MUST` cover the rule, scope, target, and period.
2. The exception `MUST` be narrower and shorter-lived than the rule it varies.
3. The underlying evidence result `MUST NOT` be changed to make the exception
   appear compliant.
4. Compensating controls and detection `MUST` be proportionate to the residual
   risk and independently observable where materiality requires it.
5. Expiry `MUST` block continued reliance unless a new, evidence-backed
   authority decision is recorded.
6. Material scope, candidate, authority, or risk changes `MUST` trigger review.
7. An exception `MUST NOT` claim to waive an external obligation unless the
   governing source recognises that variance and the recognised authority
   approves it.
8. The adopting organisation `MUST` retain live records in a controlled,
   queryable system of record and detect expired or orphaned exceptions.

Permanent deviations are changes to policy or profile, not endlessly renewed
exceptions. Propose the normative change with consumer impact and evidence.

## 6. Control Lifecycle And Anti-Bureaucracy

Every new or materially expanded control should state:

- the failure or unacceptable risk it addresses;
- the evidence that can show the control operates and discriminates that
  failure;
- its engineering, review, latency, privacy, and operational cost;
- an accountable owner and review trigger; and
- the condition for simplification, replacement, or retirement.

Review a control when its risk, platform, evidence discrimination, failure
history, or operating cost changes materially. Simplify or retire it when it is
duplicated, no longer addresses an applicable risk, cannot produce useful
evidence, or a cheaper control preserves the required outcome. Strengthen or
replace it when incidents, test escapes, or calibration show that it does not
discriminate the intended failure.

Removal remains a controlled change. Absence of a recent incident is not proof
that the control has no value, and control activity volume is not proof that it
works.

## 7. Authoring And Review Checks

For a new or changed material claim:

1. identify the canonical owner and eliminate duplicated normative copies;
2. select claim strength or content class intentionally;
3. state activation conditions and conflicting external authority;
4. name expected evidence and uncertainty semantics;
5. state whether an exception is permitted and which authority can grant it;
6. record consumer impact when meaning, strength, or applicability changes;
7. identify control cost and a review/retirement condition; and
8. keep examples, tool choices, live exceptions, and organisation-private
   records outside portable normative text.

## 8. Consumer Impact

**Change class:** normative replacement and normative tightening. The pattern
clarifies existing obligations and adds a general applicability/exception
contract. Consumers should migrate material local exceptions and review claims
whose previous imperative wording implied universal scope.

**Compatibility proposal:** `0.3.0`. Pinned consumers must review profile
activation and meaning changes before adoption.

## Related

- [How To Read This Doctrine](how-to-read-this-doctrine.md)
- [Doctrine Library Change Harness](doctrine-library-change-harness.md)
- [Engineering Controls Governance Program](engineering-controls-governance-program.md)
- [Revision-Pinned External Control Profiles](revision-pinned-control-profiles.md)
- [AI Adoption Controls](ai-adoption-controls.md)
- [AI-Native Software Development Lifecycle](ai-native-software-development-lifecycle.md)

## References

- RFC 2119: https://www.rfc-editor.org/rfc/rfc2119.html
- RFC 8174: https://www.rfc-editor.org/rfc/rfc8174.html
- NIST Cybersecurity Framework 2.0: https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final
- NIST SP 1301, Creating and Using Organisational Profiles: https://csrc.nist.gov/pubs/sp/1301/final
- NIST SP 800-53 Rev. 5: https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final
- NIST SP 800-37 Rev. 2: https://csrc.nist.gov/pubs/sp/800/37/r2/final
- NIST IR 8286A Rev. 1: https://csrc.nist.gov/pubs/ir/8286/a/r1/final
