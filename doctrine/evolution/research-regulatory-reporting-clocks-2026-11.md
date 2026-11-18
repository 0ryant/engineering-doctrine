# Regulatory Reporting Clocks In Vulnerability Response

Date and source access date: 2026-11-18. Repository basis: `8b518c9` and the companion change.
Status: research basis for [ADR 0055](../../docs/adr/0055-add-profile-gated-regulatory-reporting-clocks.md) (accepted 2026-11-18). Model research and model review; no independent human, legal, or domain review.

## Question

The [latest-developments note](research-latest-developments-2026-11.md) recorded that EU Cyber Resilience Act reporting went live on 2026-09-11 and that [secure development lifecycle](../principles/secure-development-lifecycle.md) §3 has no hook for a regulatory reporting clock. What does the regulation require, and what is the smallest portable rule that lets an estate in scope meet it without making the regulation universal doctrine?

## Source Ledger

Classes follow [Source Authority And Evidence Grading](../patterns/source-authority-and-evidence-grading.md) §2. EUR-Lex returned empty responses on the access date, so a delegated agent retrieved the Official Journal text from the EU Publications Office and the lead author re-read every cited passage in that retrieved copy. The Commission reporting page was read live by the lead author. No archive copies were captured.

| Source | Class and scope | Supports | Does not establish |
| --- | --- | --- | --- |
| [Regulation (EU) 2024/2847](http://data.europa.eu/eli/reg/2024/2847/oj), Art 14, Art 3(42), Art 24(3), Art 69(3), Art 71(2) (retrieved from the [Publications Office](http://publications.europa.eu/resource/celex/32024R2847)) | S1, the norm | A manufacturer notifies an actively exploited vulnerability, or a severe incident affecting the product's security, to the coordinator CSIRT and ENISA through the single reporting platform. Early warning within 24 hours of becoming aware; notification within 72 hours; final report no later than 14 days after a corrective or mitigating measure is available (vulnerabilities) or within one month after the 72-hour notification (incidents). Users are informed under Art 14(8). Art 14 applies from 2026-09-11, including to products placed on the market earlier; the rest of the regulation applies from 2027-12-11 | Whether a given estate is a manufacturer or its product is in scope; that is a legal determination |
| [Commission guidance C/2026/6013](http://publications.europa.eu/resource/celex/52026XC06013), section 9.1 (OJ C, 2026-11-17) | S2, institutional guidance; states that it is not binding | A manufacturer is regarded as aware when, after an initial assessment, it has a reasonable degree of certainty that exploitation or a severe incident has occurred; the emphasis is on prompt initial assessment; no report is owed for exploitation the manufacturer already knew of before 2026-09-11 | A binding interpretation; only the Court of Justice gives one |
| [Commission CRA reporting page](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting) (last update 2026-09-11) | S2 summary | Start date, the 24-hour and 72-hour steps, steward reporting from 2027-12-11, and the ENISA single reporting platform | The page shortens Art 14(2)(c) to "a corrective measure"; the regulation says "corrective or mitigating" |
| [ENISA launch notice](https://www.enisa.europa.eu/news/the-cra-single-reporting-platform-is-launched) (2026-09-11) | S2; read by a delegated agent only | The platform was deployed at initial operating capability on the start date | Full platform functionality |

Amendments checked by the delegated agent in Publications Office metadata: one adopted amendment (the European Health Data Space regulation) and three English corrigenda, none touching Art 3, 14, 24, 69, or 71. That check was not repeated by the lead author.

## Library Text Today

- Secure development §3 covers advisories, exploit-signal triage, coordinated disclosure, customer communications, and root-cause class. It names no clock, recipient, or channel.
- The [incident lifecycle](../patterns/incident-lifecycle-and-on-call-operations.md) pattern mentions regulatory communication "only when the estate demands it" and has no deadline handling.
- [Revision-Pinned External Control Profiles](../patterns/revision-pinned-control-profiles.md) already routes external baselines into vulnerability response and incidents, but its minimum record has no field for a reporting duty.
- [Privacy](../principles/privacy-and-data-governance.md) §5.4 is the precedent for a profile-gated regulatory duty: applicability first, typed duties only while the profile is active, and no doctrine exception that claims to waive the law.

## Synthesis

1. **The duty is regime-specific; the preparation is general.** Which regime applies, to whom, and with which deadlines is a legal determination that belongs in a profile. What every such regime needs from engineering is the same: know the trigger, record when the estate became aware, and have a prepared path to the recipient.
2. **A 24-hour clock is an on-call problem.** The first deadline can fall outside office hours and before root cause is known. A team that first has to find out who may file, and where, will miss it. That is the engineering reason for a typed rule once a profile is active.
3. **Two triggers, two final-report clocks.** Under the CRA an exploited vulnerability and a severe incident share the 24-hour and 72-hour steps but end differently. A runbook that treats them as one will mis-time the final report.
4. **Awareness needs a record.** The guidance ties the clock to a reasonable degree of certainty after an initial assessment. Recording when that point was reached, and by whom, is the only way to show a deadline was met.
5. **The hook should be generic.** Other regimes carry reporting clocks. Wording the rule for "a profile with a reporting clock" lets them reuse it; the CRA is the worked example.

## Decision Input

| Element | Owner | Strength proposed |
| --- | --- | --- |
| Applicability and regime detail | The registered profile | Not doctrine; the profile carries role, scope, triggers, deadlines, recipient, channel, and pinned sources |
| Runbooks name triggers, clock start, deadlines, recipient, channel, and authorised submitter; the record states when and by whom awareness was established | [Secure development lifecycle](../principles/secure-development-lifecycle.md) §3.1 | MUST while a profile with a reporting clock is active |
| Reporting path exercised before it is needed | Same | SHOULD, same scope |
| Profile record carries reporting obligations where the baseline imposes them | [Revision-Pinned External Control Profiles](../patterns/revision-pinned-control-profiles.md) §3 | Additive record field |

Admission: the deadlines are a **conformance claim** satisfied by the pinned regulation (S1). The preparation rule is the library's own; it is admitted at **C2 with explicit risk asymmetry**: preparing costs a runbook section and an exercise, while missing a statutory deadline is regulatory exposure for the manufacturer.

## Residual Risk

This is not legal advice, and scope under the regulation was not analysed. The regulation text was read in a copy retrieved by an agent from the Publications Office, not from EUR-Lex. The Commission guidance was published one day before the access date and is not binding. Single-language corrigenda and the delegated and implementing acts were not read in full. No independent review is recorded.
