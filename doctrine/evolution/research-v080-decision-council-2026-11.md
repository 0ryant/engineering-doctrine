# Decision Council, November 2026

Date: 2026-11-20. Repository basis: `e0efe31` (tag `v0.7.0`).
Status: non-normative research record. It adopts no control and changes no consumer obligation. It is the research basis for ADRs 0061 to 0064, all Proposed. A council of model instances, all of one model family, did the work in one day at the repository operator's direction. No independent human or domain review took place.

## What Was Asked And By Whom

On 2026-11-20, after `v0.7.0` was tagged, the repository operator asked for a council to review the ADRs and evolution notes, do research, and decide what the next tagged release should be. When that round had reported, he told the council to make all the open decisions.

The rules in this library are his. A council decision is a proposal, and it binds only when he accepts the ADR that carries it.

## Method

A seat is one model instance given one slice of the library or one point of view. The chair is the session that briefed the seats, checked their claims against the tree, and wrote the drafts. An adversary is a seat told to attack a draft.

The first round decided the release. Seven seats worked read-only from one brief, without sight of each other. Each took one slice: the release rules, every ADR, the review register, the early evolution notes, the recent ones, outside sources, and a cold read as an adopter. The chair drafted a decision. An adversary attacked it and returned eight amendments, and all eight were taken.

The second round took the open decisions. The chair wrote one docket of 62 questions, each with lettered options. Two panels voted: five seats on the 39 questions that shape the release, and three seats on the other 23. Each vote recorded whether the choice changes a rule, and its basis: the operator's own text, the library's mechanics, an outside source read that day, or the seat's judgement. A script tallied the votes. A question needed three votes of five, or two of three. With no majority, the rule was to take the option that changes least and set a dated revisit. A second adversary reviewed the whole slate.

| Seat | Panel | Lens |
| --- | --- | --- |
| Adopter | Five-seat | What a reader at a pinned tag must do, re-read or re-pin |
| Maintainer | Five-seat | The cost now and at every later release, for one maintainer |
| Constitution | Both | Decide from what the operator has already written |
| Risk | Both | What breaks if the choice is wrong, who notices, and whether it can be undone |
| Sceptic | Both | Prefer the option that removes text or adds none |
| Adversary | Neither | Whether each tallied decision holds against the operator's accepted text |

## Outcome In Numbers

| Measure | Count |
| --- | ---: |
| Questions | 62 |
| Votes cast | 264 |
| Abstentions | 0 |
| Decided by majority | 61 |
| Unanimous | 25 |
| Decided by a margin of one vote | 25 |
| No majority | 1 |
| Upheld by the adversary | 49 |
| Changed by the adversary | 3 |
| Flagged for the operator | 10 |

The three changes were two majorities overturned and the one question with no majority, settled by the least-change rule. Three of the ten flagged decisions had been unanimous.

The operator answered the ten flagged questions himself the same day. Six had to be put to him a second time in plain words, because the first summaries used the council's shorthand. Two answers are recorded as the chair's reading and await his confirmation. Three answers went against the council's vote.

- The council voted five to nil to delete the exception that lets an independently calibrated model judge be the sole authority for a high-materiality acceptance. He kept the exception, and the earlier decision that says "never" is to be amended to match. [AI-05]
- The council voted five to nil to trigger the rule that gives an agent an account of its own on what the agent can do, with new triggers named. He kept the rule's tests as written. The only edit proposed removes a tier label. [AI-01, SEC-15]
- The council voted three of five to reword the tracked hook and tool configuration files. He left them as they are. [LIB-11]

## The Release Decision

Five first-round seats recommended a minor release next, and two recommended a patch first. The adversary tested four claimed fact errors on the publishers' pages. Two were real, the first two in the table below, and both have shipped in every tag since `v0.2.0`. On that evidence the council recommended a small patch that corrected named facts and changed no rule, with the minor to follow.

The operator declined the patch. The next tag is `v0.8.0`, and the fact corrections ride it. The window runs from 2026-12-18 to 2027-02-11. The opening date clears the 90-day floor of 2026-12-14 for the three files deprecated at `v0.5.0`, and the date to which the operator set other work aside. The closing date lets the release sweep record a verdict on [evidence exception EX-0001](../EVIDENCE-EXCEPTIONS.md) before it expires on 2027-02-12. Scope freezes at a checkpoint on 2027-01-15.

## Outside Sources Read

Each read below was made on 2026-11-20 on the publisher's own page, with no summarising model in between. The table paraphrases each passage. Classes follow [Source Authority And Evidence Grading](../maintainers/source-authority-and-evidence-grading.md) §2, and each S5 page is cited within its own product's scope. No archive copies were captured.

| Claim checked | Publisher's page and class | What the page says | Read by |
| --- | --- | --- | --- |
| A Go command listed as a lockfile check is not one | [Go Modules Reference](https://go.dev/ref/mod#go-mod-verify), S5 | `go mod verify` checks cached modules against the hashes recorded at download. It does not use the checksum file to verify module content. | First adversary |
| A CI platform in a keyless-signing example is not a supported issuer | [Fulcio: OIDC usage](https://raw.githubusercontent.com/sigstore/fulcio/main/docs/oidc.md), S5 | The platform in the library's example is not among the supported issuers and appears nowhere in the file. Nobody checked the deployed service against it. | First adversary |
| One EU AI Act transition ends on 2026-12-02 | [Regulation (EU) 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj), Article 111(4) as added, S1 | Providers of synthetic-content systems on the market before 2 August 2026 must comply with Article 50(2) by 2 December 2026. | First adversary |
| A saved infrastructure plan holds secrets in clear | [Terraform: plan command](https://developer.hashicorp.com/terraform/cli/commands/plan), S5 | Sensitive values hidden in terminal output are written in clear to the saved file, which should be treated as sensitive. | Both adversaries; risk, five-seat panel |
| The first build-provenance level does not stop tampering | [SLSA v1.2: Build track basics](https://slsa.dev/spec/v1.2/build-track-basics), S4 | Level 1 provenance helps prevent mistakes and is easy to bypass or forge. Level 2 adds protection against tampering after the build. | Risk, three-seat panel |
| A lock file does not pin infrastructure modules | [Terraform: dependency lock file](https://developer.hashicorp.com/terraform/language/files/dependency-lock), S5 | The lock file records provider selections only. For remote modules the tool selects the newest version that meets the constraint. | Risk, three-seat panel |
| The US directive behind the known-exploited catalogue was replaced | [CISA BOD 26-04](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk), S1 for US federal civilian agencies only | It replaces and revokes two earlier directives, one of them the 2021 directive on known exploited vulnerabilities. | Risk, three-seat panel |
| The next agent-protocol revision is due on 2027-03-30 | [MCP: release cycle](https://blog.modelcontextprotocol.io/posts/mcp-release-cycle/), S5 | The next release is targeted for 30 March 2027. | Risk, three-seat panel; second adversary |
| A large project bars agent sign-off lines | [Linux kernel: coding assistants](https://raw.githubusercontent.com/torvalds/linux/master/Documentation/process/coding-assistants.rst), S5 | Agents must not add the sign-off tag. Only a person can certify the origin statement. | Risk, five-seat panel; second adversary |
| An archive lookup returns one snapshot | [Internet Archive: availability API](https://archive.org/help/wayback_api.php), S5 | A single snapshot, the closest to the time asked for. | Risk, five-seat panel |

Each page was opened again the same day for this note, and the recorded passage was found, with two exceptions. The regulation is not re-verified on EUR-Lex, which answered a scripted request with HTTP 202 and no content. The passage was found in the [Publications Office copy](https://publications.europa.eu/resource/celex/32026R1744) of the Official Journal text. The directive's timeline table is an image. The seat read it, and it was not re-read for this note.

Other direct reads recorded that day, on which less depends, are not listed.

## What The Method Cannot Show

- **One model family.** Every seat, the chair and both adversaries are instances of one model family, and that family drafted much of the library. Agreement among them is not independent evidence.
- **A vote fixes a direction, not wording.** Behind twelve winning letters, the seats that chose the same option meant different edits, strengths or dates. The text is settled only when the operator reads the drafted record.
- **Thin margins.** Twenty-five decisions turned on one vote, eighteen of them in the three-seat panel.
- **No abstentions.** The docket let a seat abstain where a question turned on a fact it could not establish. None did, on 264 votes, although seats named votes that rest on facts only the operator has. One such fact arrived after the vote: the library is in use in at least three enterprises (operator's statement, 2026-11-20).
- **Strengths were not voted on separately.** Where a decision names MUST or SHOULD, one or more winning seats proposed it.
- **Summarised reads.** Most of the first round's outside reads went through a summarising fetch, in which a small model extracted the answer from the publisher's page. Those are leads, and none is in the table above.
- **Private working papers.** The votes, the seats' reasoning and the tally are not published, so a reader cannot re-run the count.

## The Adversary's Accretion Count

The second adversary counted what the slate does to rule text: principles, patterns, checklists, contracts and maintainer rules. After its three changes, 14 decisions add rule text, 15 remove or narrow it, and 33 leave it alone. About 2,300 words come out. Of those, 2,063 are the three exits that [ADR 0045](../../docs/adr/0045-execute-the-first-lifecycle-sweep.md) ordered in September, which this council only schedules. By the adversary's estimate the slate needed five to seven new ADRs and several dated amendments to earlier ones. It also creates nine standing duties that fall on one person. Its verdict in one line: the slate holds on rules and accretes on process and record.

The count is one seat's classification, made before the operator answered the flagged questions. It was not redone.

## Left Out On Purpose

- A set of possible upgrades that the operator set aside until 2026-12-18. Four questions overlapped it, and each was decided or deferred in a way that starts none of that work.
- The nine rules he kept as written on 2026-11-18, listed in the [full review](review-full-doctrine-2026-11.md).
- The content of the rewrite of the AI-native lifecycle pattern, which waits for its own ADR.
- Whether an agent may carry out a change in production. The panel voted three to two for a general condition. The adversary sent the question to its own ADR, to be drafted by 2027-01-15, because [ADR 0059](../../docs/adr/0059-apply-three-constitution-rules-to-settled-inconsistencies.md) keeps that judgement for the operator.

## Where The Decisions Landed

Four proposed records carry the decisions.

- [ADR 0061: Execute The First Exits And Settle How An Exit Is Carried Out](../../docs/adr/0061-execute-the-first-exits-and-settle-how-an-exit-is-carried-out.md)
- [ADR 0062: Close The Carried Release Criteria By Decision](../../docs/adr/0062-close-the-carried-release-criteria-by-decision.md)
- [ADR 0063: Settle Open Questions In The Rules Adopters Follow](../../docs/adr/0063-settle-open-questions-in-the-rules-adopters-follow.md)
- [ADR 0064: Settle The Library's Own Rules, Records, And Tool Contract](../../docs/adr/0064-settle-the-librarys-own-rules-records-and-tool-contract.md)
