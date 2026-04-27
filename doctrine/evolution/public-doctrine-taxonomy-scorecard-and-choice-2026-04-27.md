# Public Doctrine Taxonomy, Honest Scorecard, And “Which To Choose When”

**Date:** 2026-04-27.  
**Purpose:** Complement [public-doctrine-benchmark-gap-analysis-2026-04.md](public-doctrine-benchmark-gap-analysis-2026-04.md) (benchmark *corpus* and first scorecard) with: (1) a **taxonomy** of *kinds* of public doctrine, (2) a **refreshed honest scorecard** for *this* library after late-April work, and (3) a **practical** **guide** to **which** external (or internal) source to lead with **when**—without pretending one PDF rules every estate.

**Method:** Synthesis of the April benchmark, recent additions (code review, GitOps, public governance, ADR index, CHANGELOG), and explicit positioning—**not** a new web crawl; cite primary URLs where the reader should go deeper.

---

## 1. Taxonomy: kinds of public doctrine

“Public doctrine” is not one thing. These **categories** overlap, but the **purchasing question** and **default reader** differ.

| Kind | Typical form | What it optimises for | Examples (entry points) |
| --- | --- | --- | --- |
| **A — Company engineering handbook** | Large Markdown tree, culture + process + stack | Onboarding, alignment, *their* product context | [GitLab Handbook — Engineering](https://handbook.gitlab.com/handbook/engineering/), [Sourcegraph handbook](https://github.com/sourcegraph/handbook) |
| **B — Productised playbook (consultancy / product shop)** | Playbook + small guides | Delivery craft, team agreements, design/dev workflow | [thoughtbot Playbook](https://thoughtbot.com/playbook), [18F Guides](https://github.com/18F/guides) |
| **C — Narrow, high-clarity standard** | Small set of *rules* or *factors* | One slice (e.g. appFactor), maximum portability | [Twelve-Factor App](https://12factor.net/), [MADR](https://adr.github.io/madr/) |
| **D — Outcome metrics and research** | Papers, annual reports, metric definitions | Improvement science, *what to measure* | [DORA](https://dora.dev/), [SPACE](https://queue.acm.org/detail.cfm?id=3454124) (ACM Queue) |
| **E — Reliability / operations canon** | Books, long-form chapters | SLOs, incident practice, toil, launch control | [Google SRE Book](https://sre.google/sre-book/table-of-contents/) |
| **F — Security / compliance frameworks** | Standards, control catalogues, verification guides | Defensible baselines, audit language | [NIST SSDF](https://csrc.nist.gov/Projects/SSDF), [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) |
| **G — Platform / cloud / CNCF** | Whitepapers, tagged maturity models | Internal platforms, golden paths, capability building | [CNCF Platform Engineering Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/) |
| **H — Government / public-service** | Codes of practice, delivery principles | User need, accessibility, open standards, spend rules | [GOV.UK Technology Code of Practice](https://www.gov.uk/guidance/the-technology-code-of-practice) |
| **I — Open operational definitions** | Versioned *principles* for a practice | Interop vocabulary (e.g. *GitOps*) | [OpenGitOps](https://opengitops.dev/) ([PRINCIPLES v1.0.0](https://raw.githubusercontent.com/open-gitops/documents/v1.0.0/PRINCIPLES.md)) |
| **J — “Portable” multi-repo engineering doctrine (this library)** | Principles / patterns / toolings / checklists + evolution | Reuse across products and estates; **no** single employer as hero | [how-to-read-this-doctrine.md](../patterns/how-to-read-this-doctrine.md) |

**Honest line:** handbooks in **A** and **B** are often **deeper** on *people, politics, and product* than **J**. **F** and **H** are **deeper** on *assurance* than **J**. **J** is built to **avoid** enshrining one vendor, one cloud, or one company’s OKR—**that** is the trade.

---

## 2. Refreshed scorecard: *this* repository (2026-04-27)

Scale: **5 = distinctive or leads typical public corpora for portable doctrine**, **4 = strong**, **3 = present but still thin or calibration-heavy**, **2 = spotty**, **1 = absent**.

*Adjustments since [public-doctrine-benchmark-gap-analysis-2026-04.md](public-doctrine-benchmark-gap-analysis-2026-04.md): code review, GitOps, repo governance, ADRs, and versioning are now explicit.*

| Category | Score | One-line evidence | Still honestly weaker than best-in-class *somewhere* |
| --- | ---: | --- | --- |
| Layering (principles / tooling / estates) | 5 | `timeless-principles-and-tooling.md`, `how-to-read-this-doctrine.md` | — |
| Contracts, events, idempotency, interop | 5 | Event contracts, state machines, CloudEvents, patterns | Add OpenAPI *example* only if teams ask (April note stands) |
| Code review, merge path, *high-risk* review | 4.5 | [code-review-and-change-approval.md](../patterns/code-review-and-change-approval.md), merge-path principle, collaboration | Google [eng-practices](https://github.com/google/eng-practices) is still *tighter* on *author*/*reviewer* micro-behaviours; we are **enough** for policy + escalation |
| GitOps / declarative ops | 4.5 | [gitops-and-declarative-operations.md](../patterns/gitops-and-declarative-operations.md) cites OpenGitOps, OWASP CI/CD, NIST, 12factor | Argo/Flux *runbooks* and cloud-specific *how* stay estate-only by design |
| Build, delivery surfaces, supply chain, provenance | 4.5 | Build, SLSA refs, dependencies, merge-path tooling | Consumer scorecard by **criticality** still optional (April “Could”) |
| Security SDLC, STRIDE, API security | 4 | Broad SSDF / OWASP / disclosure alignment | Compact “portable” vuln *intake* **pattern** still a nice add (April “Should” family) |
| Trunk, collaboration, branch protection | 4.5 | `collaboration.md`, trunk pattern, `tooling/collaboration.md` | GitLab *numbers* on **allocation** and **managers**—we do not clone **A**-handbook |
| Reliability, SLO, incidents, on-call, chaos | 4.5 | Principles + [incident-lifecycle…](../patterns/incident-lifecycle-and-on-call-operations.md) + chaos pattern | Paging tools, status products—estate |
| DevEx (first-class) | 4 | `developer-experience.md`, scorecard, ADR 0007 | **Calibration** with real teams, not more prose |
| Platform / golden paths | 4 | [platform-as-product…](../patterns/platform-as-product-and-golden-paths.md) + CNCF refs | **Portal** product still never mandated (intentional) |
| Public repo governance, license, security reporting | 4.5 | CONTRIBUTING, SECURITY, GOVERNANCE, Apache-2.0 | No CoC file yet (optional per April); enable host **private** reporting if you promise it in SECURITY |
| AI/ML, RAG, agents | 4.5 | `ai-ml-systems.md`, research, ADR 0005 | Hyperscaler **landing zone** *templates* stay out of `principles/` (intentional) |
| **Product / user-need / service design handshake** | 2.5 | User-facing quality, privacy | GOV.UK / 18F / thoughtbot start from **outcomes**; we start from **engineering control**—still a **structural** gap, not a bug |
| **Capacity allocation (features vs toil vs risk)** | 2.5 | Toil, DORA, adoption | No single **portable** principle with numbers like **Google SRE**-style budgets |
| **Support model, status page, known-issue cadence** | 3 | Incident/release comms | No full **portable** support *pattern* (April “true silence”) |
| **Data class / handling taxonomy** | 2.5 | Privacy, audit | Portable **class labels** not yet a first-class pattern |

**Blunt average:** for **portable, forkable, multi-tenant** engineering law, this library is **strong** in **technical** and **delivery** *control* language and **weaker** on **outcome** and **customer** *operating* systems. That is **a choice**; see §4.

---

## 3. Which to choose *when* (decision guide)

Use this when someone asks: *Should we follow Google, GitLab, this doctrine, or NIST?*

| Your situation | **Lead** with (primary) | **Layer in** from this library (`J`) | **Do not** substitute |
| --- | --- | --- | --- |
| You need **onboarding** and **culture** for *one* company | **A** (that company’s handbook) | Principles that survive **forking**; `adoption-playbook` | A wholesale copy of **A** into portable principles |
| You need **strong code review** *norms* (author/reviewer) | [Google eng-practices](https://github.com/google/eng-practices) (review) | [code-review-and-change-approval.md](../patterns/code-review-and-change-approval.md) for **duties**, **blocker/nit**, **escalation**, **agent** diffs | Thinking Google’s doc **replaces** your **CI** or **merge** **policy** |
| You need **SRE / reliability** depth | **E** (SRE book) + **D** (DORA) | `reliability-slo-incidents`, incident **lifecycle** pattern, chaos pattern | SRE org chart from Google as **universal** law |
| You need **security** audit language | **F** (SSDF, ASVS) + your regulator | STRIDE-lite, API security, merge-path, supply chain principles | A single **SaaS** checklist as *the* “standard” in `principles/` |
| You need **GitOps** *definition* and *interop* | **I** (OpenGitOps) + [OWASP CI/CD top 10](https://owasp.org/www-project-top-10-ci-cd-security-risks/) | [gitops-and-declarative-operations.md](../patterns/gitops-and-declarative-operations.md) + merge-path | Argo **vs** Flux **fights** in `principles/` |
| You need **platform / golden paths** maturity language | **G** (CNCF PEMM) + **D** | [platform-as-product…](../patterns/platform-as-product-and-golden-paths.md), DevEx scorecard | Mandating **Backstage** in portable doctrine |
| You need **public sector** *proportionality* and **accessibility** | **H** (e.g. GOV.UK TCoP) + WCAG | `user-facing-quality`, `documentation-knowledge` | Copying **GOV.UK** **cloud** **mandates** into non-gov estate |
| You need **small-app** *portability* rules | **C** (12-factor) | `build`, `configuration-and-secrets`, `container-runtime-choice` (conditional) | 12-factor as **complete** K8s policy |
| You need **many teams** to **pin** a **common** *engineering* *baseline* across repos | **J** (this library) as **spine** | `ENGINEERING.md` umbrella + estate overlays | This repo as **product** *roadmap* or *HR* policy |
| You need **decision** *records* for **your** *product* | **C** (MADR) + host docs | `docs/adr/` in **this** repo for **doctrine** *meta*; product ADRs in *product* repos | One global ADR for all services without ownership |

**Rule of thumb:** **External** = **evidence** and **naming**; **this** library = **layering**, **local** `.doctrine/`, and **gaps** you **admit** in **evolution** notes.

---

## 4. When *this* library is the wrong primary home

- **You are writing** employment policy, compensation philosophy, or **OKR** **cascades** — use **A** (internal) or your HR/legal process.
- **You need a legally binding** control matrix for a **named** **regime** (e.g. FedRAMP) — use **F** + estate crosswalk, not `principles/` alone.
- **You need user research, service design, and journey mapping** as the *primary* *artefact* — use **B** / **H**-style *service* guidance; this library is **downstream** of agreed requirements.
- **You need a single cloud’s** Well-Architected **pillar** *scores* — use that cloud’s *estate* doc; we avoid **turning** one cloud into *portable* law.

---

## 5. Gaps to watch (short list)

The **detailed** gap inventory remains in [public-doctrine-benchmark-gap-analysis-2026-04.md](public-doctrine-benchmark-gap-analysis-2026-04.md) and [anti-patterns-and-failure-modes-gap-analysis-2026-04.md](anti-patterns-and-failure-modes-gap-analysis-2026-04.md). Highest **honest** **residuals** as of 2026-04-27:

1. **Product / user-need** handshake and **outcome** language (still 2.5).
2. **Engineering capacity allocation** (still 2.5) — toil and DORA *mention*; **defended** *budget* **as** a **principle** is not yet written in one place.
3. **Support, status, known-issues** rhythm (3).
4. **Data classification** driving logging/AI/retention (2.5).

**Code review** and **GitOps** moved from *thin* to *strong enough to cite*; **public** **governance** and **versioning** moved from *gap* to *addressed* for the **repo** itself.

---

## 6. Bottom line

- **This library** is the **right** **primary** **spine** when you want **portable** **engineering** *law* for **many** codebases: **principles** **vs** **tooling**, **contracts**, **trunk** **+** **merge** **path**, **GitOps** **language** **tied** to **OpenGitOps/OWASP**, **AI** **governed**, and **adoption** that **does** **not** **pretend** to be a **company** **handbook**.

- **Choose** a **famous** **handbook** **(A/B)** when the **question** is **“**how** **do** **we** **behave** **as** **$Company**”**; **choose** **this** when the **question** is **“**what** **do** **we** **pin** **in** **git** **so** **every** **service** **team** **does** **not** **reinvent** **SLOs**, **events**, and **CI** **truth**”**.

- **Scorecard** in §2: **no** **category** is **1** in **core** **technical** **discipline** anymore; the **low** **numbers** are **intentional** **scope** on **product**-**adjacent** and **governance** **theatre** you **should** **not** **fake** **portably** without **your** **org’s** **names** **on** it.

**Sleep note:** the April benchmark file is still the **long** **audit**; this file is the **map** and **picking** **guide**—**keep** **both** **linked** from [honest-review-synthesis.md](honest-review-synthesis.md) **and** the **evolution** **index**.
