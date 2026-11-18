# ADR 0055: Add Profile-Gated Regulatory Reporting Clocks To Vulnerability Response

- **Status:** Accepted
- **Decision date:** 2026-11-18
- **Recorded date:** 2026-11-18
- **Retrospective:** No
- **Deciders:** Repository operator
- **Review provenance:** Operator-directed and operator-accepted on 2026-11-18; drafted and reviewed by a model, no independent human, legal, or domain review recorded
- **Research:** [Regulatory reporting clocks in vulnerability response](../../doctrine/evolution/research-regulatory-reporting-clocks-2026-11.md); finding 3 in the [latest-developments note](../../doctrine/evolution/research-latest-developments-2026-11.md)
- **Canonical owner:** [Secure Development Lifecycle](../../doctrine/principles/secure-development-lifecycle.md) §3.1
- **Derived landings:** [Revision-Pinned External Control Profiles](../../doctrine/patterns/revision-pinned-control-profiles.md) §§3, 5 (record field and composition row); [Incident Lifecycle](../../doctrine/patterns/incident-lifecycle-and-on-call-operations.md) §4 (pointer); [Governance Program Readiness](../../doctrine/checklists/governance-program-readiness.md)

## Context

The EU Cyber Resilience Act's reporting duty has applied since 2026-09-11. A manufacturer in scope reports an actively exploited vulnerability, or a severe incident affecting a product's security, within 24 hours of becoming aware, again within 72 hours, and with a final report later. The library's vulnerability response names no clock, recipient, or channel, and its profile record has no field for a reporting duty.

Whether the regulation applies to an estate is a legal determination. The library already handles duties of that kind through profile gates, as [privacy](../../doctrine/principles/privacy-and-data-governance.md) §5.4 does for AI Act transparency.

## Decision

Add §3.1 "Regulatory Reporting Clocks (Profile-Gated)" to the secure development lifecycle principle.

- **Applicability first.** Reporting clocks are not universal doctrine. An estate activates them by registering the regime as an external control profile. The profile carries the applicability decision, triggers, deadlines, recipient, channel, and pinned sources.
- **MUST (profile with a reporting clock active):** vulnerability-response and incident runbooks name each reporting trigger, the event that starts the clock, the deadlines, the recipient and channel, and who is authorised to submit. The vulnerability or incident record states when the estate became aware and who made that determination.
- **SHOULD (same scope):** the reporting path is exercised before it is needed: access to the channel works, the on-call route reaches an authorised submitter outside office hours, and triage asks the regime's trigger question early.
- **Exceptions:** only the governing regime grants variances. A doctrine exception cannot waive a statutory deadline.
- The Cyber Resilience Act, Article 14, is the worked example in the owner text. It is an example of a profile, not a claim that consumers are in scope.

The profile pattern's minimum record gains a "Reporting obligations" row, filled only where the baseline imposes them.

## Control Cost And Lifecycle

| Failure addressed | Evidence | Operating cost | Review trigger |
| --- | --- | --- | --- |
| A statutory reporting deadline missed because nobody knew who files, where, or when the clock started | Runbook section naming triggers, deadlines, recipient, channel, and submitter; awareness time in the record; exercise notes | One runbook section per active profile and a periodic exercise | A missed or near-missed deadline; a change to the regime's deadlines or channel; a second regime registering a clock |

The rule costs nothing for estates with no such profile. It can be simplified if profile owners find the record field alone is enough.

## Alternatives Considered

- **State the CRA deadlines as universal doctrine.** Rejected; most consumers are not manufacturers in scope, and the library does not make legal determinations.
- **Leave it to the profile pattern with no owner text.** Rejected; the pattern routes obligations but says nothing about a clock that starts on an on-call shift, and the preparation is an engineering matter.
- **Put the rule in the incident lifecycle pattern.** Rejected as owner; exploited vulnerabilities are handled under vulnerability response even when no incident is declared. The pattern gets a pointer.
- **A SHOULD for runbook preparation.** Rejected; once a profile is active the deadline is binding, and the preparation is the minimum that makes it reachable.

## Consumer Impact And Migration

Change class: **additive guidance** for all consumers; **normative tightening** only for consumers with an active profile that carries a reporting clock. Compatibility: pre-1.0 minor.

Migration for consumers in scope: register the profile; add the reporting section to vulnerability-response and incident runbooks; record awareness time in the vulnerability or incident record; exercise the path once.

## Acceptance Criteria

- Secure development §3.1 states applicability, the typed duties, the exception rule, and the worked example with pinned sources.
- The profile pattern's record and composition table carry the reporting obligation.
- The incident lifecycle pattern points to §3.1 from its communications section.
- Governance Program Readiness carries one derived prompt.
- The stale cross-reference in the SSDF table (dependencies §5 for disclosure) points to §7.
- The ADR index lists this decision, and doctrine preflight passes.

## Residual Risk

This is not legal advice. The regulation was read in a copy retrieved from the EU Publications Office, and the Commission guidance on "becoming aware" is one day old and not binding. Scope under the regulation, and other regimes' clocks, were not analysed. Model review only.
