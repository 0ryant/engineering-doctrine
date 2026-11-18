# Applying The Constitution's Own Rules To Open Inconsistencies

Date and source access date: 2026-11-18. Repository basis: `8887ff7`.
Status: research basis for [ADR 0059](../../docs/adr/0059-apply-three-constitution-rules-to-settled-inconsistencies.md) (accepted 2026-11-18). Model research and model review; no independent human or domain review.

## Question

The [November 2026 review](review-full-doctrine-2026-11.md) left 52 inconsistencies for the maintainer to decide. How many does `ENGINEERING.md` already decide, and what does applying it change?

## Method

Each open finding in the [register](review-full-doctrine-2026-11-findings.json) was read against the current text of both sides, then tested against three sentences of `ENGINEERING.md`:

| Rule | Where | Test applied |
| --- | --- | --- |
| "Satisfy compatible obligations together and use the stricter result where controls protect the same property." | Applicability And Profiles | Do both statements protect one property, and can both be met at once? If yes, the stricter strength or wider scope stands. |
| "Use one authority per concept." | Core Proposition 9 | Is one concept defined, listed, or thresholded in two places? If yes, one page owns it and the others cite it. Where the copies differ, the owner takes their union so that nothing is loosened. |
| "checklists derive review questions." | Opening paragraph | Does a checklist prompt or an implementation reference state something no principle or pattern states? If yes, the owner gains the rule or the prompt is reworded to what the owner says. |

A finding was left out when settling it needs a judgement the three sentences do not supply.

## Result

Thirty of the 52 are settled, with two findings the review had left open (the timeouts gap and a duplicate of the pinning finding).

| Rule | Findings settled |
| --- | --- |
| Stricter result | SEC-08, XC-31, XC-10, AI-18, DEL-02, SEC-16, XC-14, DEL-13, XC-16, DEL-08; and DEL-18, UMB-09 by the recorded exception |
| One authority | SEC-07, XC-30, AI-03, OPS-05, XC-32, OPS-04, XC-09, OPS-10, XC-20, XC-25, XC-26, AI-10, XC-23, UMB-08 |
| Checklists derive | DEL-12, OPS-13, SOPS-01, DEL-05, SEC-14, OPS-16 |

Twenty-two decisions stay open. They are listed under Residual Risk in the ADR.

### Points That Needed Care

1. **Same-artefact promotion is the one place the stricter result was not taken.** The unconditional form cannot be met where a platform forces a rebuild. Three implementation references already said a rebuild is a new candidate, with no owner behind them. Build §5 and Core Proposition 5 now carry that sentence.
2. **"Equivalent to a digest" needed a definition.** A published package version is immutable in a registry that forbids overwriting; a container tag is not unless the registry enforces it. The test written into build §5 is whether the registry or store will re-point the identifier.
3. **The six approval lists cover two concepts.** Four list change classes that need human approval before merge. One lists classes of run-time agent action. One lists what a model council cannot approve, and cited the first group while dropping an item. The change-class list is now the union of the four, in the principle. The run-time list stays in the agentic loop pattern with a sentence separating the two. Whether an agent may take a reversible run-time action in those classes without approval is not settled by any of the three rules and is left open (AI-04).
4. **The owner of the class list is the principle, not the pattern with the widest list.** ADR 0047 part 3 proposes to collapse the lifecycle pattern. The content is the same either way.
5. **The lockfile-review MUST already existed.** It was typed in dependencies §7, which cites code review §6 as its source, while §6 stated it untyped. Typing it at its owner changes no obligation.
6. **Widening a MUST.** The model-call telemetry MUST named production calls under a section that applies to production and estate-governed paths. Taking the section's scope is the stricter result. It is the one MUST whose reach grows, and it is listed separately in the ADR so it can be struck.

## Source Ledger For The Added Rules

Classes follow [Source Authority And Evidence Grading](../patterns/source-authority-and-evidence-grading.md) §2. The lead author read each page, or a saved copy of it, on 2026-11-18. No archive copies were captured. Publisher counts treat each organisation as one source.

### Timeouts, Retries, And Overload

| Source | Class and scope | Supports | Qualifies |
| --- | --- | --- | --- |
| [Google SRE Book, ch. 22, Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) | S4, edited book (2016) | Set a deadline; propagate it; do not work on requests past their deadline; randomised exponential backoff; limit retries per request; a retry budget; avoid retries at several levels; a distinct overload response so callers back off; load shedding and graceful degradation | Picking a deadline "can be something of an art"; complex degradation can itself cause problems |
| [Google SRE Book, ch. 21, Handling Overload](https://sre.google/sre-book/handling-overload/) | S4, edited book | A per-request limit of three attempts; a per-client budget keeping retries under a tenth of requests; only the layer immediately above retries | The numbers are the publisher's own |
| [AWS Well-Architected Framework, REL05](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel05.html) | S5, vendor framework | Throttle above tested capacity; backoff with jitter and a bounded attempt limit; explicit timeouts on calls across a process boundary; fail fast and limit queues. Names retries "at several layers at once" and "a framework default" timeout as common faults | None stated |
| [Timeouts, retries, and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/), Amazon Builders' Library (2019) | S6, vendor engineering, named author; same organisation as the row above | A timeout on any remote call; retries "can make matters significantly worse" under overload; retry at a single point in the stack; limit retries locally with a token bucket; calls with side effects are not safe to retry without idempotency | The URL now redirects to the publisher's community site; the page shows the author's first name only |
| [Azure Architecture Center, Retry pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry) (2024-07-18) | S5, vendor framework | Retry transient faults only; increasing delays up to a maximum number of attempts; nested retry policies add delay, so the lower level fails fast; after repeated failure stop sending requests and probe later (circuit breaker); non-idempotent operations may run twice | For interactive paths, fewer retries and a short delay |
| [gRPC, Deadlines](https://grpc.io/docs/guides/deadlines/) | S5, product-scoped | No deadline is set by default; always set a realistic one; propagation is supported and in some languages must be enabled | A deadline that is too short wastes server work |

One S4 source and three further organisations support each rule. Admission: C2. The rules are admitted at SHOULD.

### A Secret That Reached A Shared Remote

| Source | Class and scope | Supports | Qualifies |
| --- | --- | --- | --- |
| [GitHub Docs, Removing sensitive data from a repository](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository) | S5, product-scoped; authoritative for what its own platform retains | "as a first step you need to revoke and/or rotate that secret"; rewritten history remains reachable in other clones, in forks, by commit hash in cached views, and through pull requests | Rotation alone "may be sufficient to solve your problem" |
| [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) §§2.7.3, 9.2 | S4, foundation cheat sheet | Potentially compromised secrets "must" be revoked; exposed keys "should undergo immediate revocation"; a new secret is created quickly, preferably by automation | History rewriting has side effects to weigh |

Admission: C2, one S4 source and one in-scope S5 source. Admitted at SHOULD. The evidence would also carry a MUST with a recorded risk asymmetry (an unrotated leaked credential stays usable by anyone holding a copy; rotation is cheap), which the maintainer may choose.

### Publish Steps Behind An Explicit Release Entrypoint

| Source | Class and scope | Supports | Qualifies |
| --- | --- | --- | --- |
| [OWASP Top 10 CI/CD Security Risks, CICD-SEC-1](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-01-Insufficient-Flow-Control-Mechanisms) (v1.0, 2022) | S4, foundation project | The risk is pushing code or artefacts down the pipeline with no additional approval or review; recommends that accounts cannot trigger production build and deployment pipelines without it | About approval, not about how a publish step is triggered |
| [PyPI, trusted publishers: security model](https://docs.pypi.org/trusted-publishers/security-model/) | S5, product-scoped | Not every workflow should be trusted to upload; a dedicated release workflow; a dedicated environment with manual approvers; a separate build job so few steps hold the publishing credential | One package registry |

Admission: C2, flagged. The sources support restricting and approving publication. The specific form (a tag, a parameter, or a separate job) is this library's, taken from its own tooling page and checklist.

### Categories Of Personal Data Per System

| Source | Class and scope | Supports | Qualifies |
| --- | --- | --- | --- |
| [NIST Privacy Framework v1.0](https://doi.org/10.6028/NIST.CSWP.01162020) (2020-01-16), Core category ID.IM-P | S2, voluntary framework | Systems that process data are inventoried (ID.IM-P1); categories of individuals are inventoried (P3); data elements are inventoried (P6) | Voluntary; a version 1.1 draft exists and was not used |
| [ICO, What do we need to document under Article 30 of the GDPR?](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/documentation/what-do-we-need-to-document-under-article-30-of-the-gdpr/) | S2, regulator guidance for one regime | Controllers document the categories of individuals and of personal data, and retention schedules for the categories where possible | A legal duty in that regime only; the regulation's own text was not read |

Admission: two independent S2 sources would give C1 for the practice. It is recorded as C2 because one source is voluntary and the other is regime-specific. Admitted at SHOULD, with formal records of processing left to a registered profile.

## Decision Input

| Decision | Owner | Strength | Admission |
| --- | --- | --- | --- |
| D1 stricter result, seven topics and one exception | Owners named per topic in the ADR | Existing strengths; one SHOULD raised to an existing MUST; one MUST's scope widened to its section's stated scope | Internal consistency with `ENGINEERING.md`; no new claim about external practice |
| D2 one authority, nine concepts | Owners named per concept in the ADR | Unchanged, except that the union of four lists is taken | Internal consistency |
| D3 leaked secret | [Configuration and secrets](../principles/configuration-and-secrets.md) §2 | SHOULD | C2 |
| D3 timeouts, retries, overload | [Errors and failure modes](../principles/errors-and-failure-modes.md) §4 | SHOULD, production services | C2 |
| D3 publish entrypoint | [Build](../principles/build.md) §5 | SHOULD | C2, flagged for indirectness |
| D3 personal-data categories | [Privacy and data governance](../principles/privacy-and-data-governance.md) §1 | SHOULD | C2 |

## Residual Risk

The three sentences were applied by a model, and "the stricter result" cannot see why a weaker statement was written. The union of the class lists may gate a class its original list left out on purpose. The added rules rest mostly on vendor guidance and one edited book; none was tested against an adopter. No independent review is recorded.
