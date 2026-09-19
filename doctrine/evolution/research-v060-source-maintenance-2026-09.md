# v0.6.0 Source And Editorial Maintenance

Date and source access date: 2026-09-19.
Status: non-normative research and editorial repair record; not release approval.
Evidence: directly inspected repository text and publisher material, followed by
model review. No independent human or domain review is claimed.

This note covers only m01, m02, m03, m13, m14, m18, m21, m23 and m27 in the
[readiness reconciliation](v060-readiness-2026-09.md), plus research for M16.
The repairs preserve existing duties, activation, strength and exception
authority. Citation pins identify evidence; they do not upgrade a consumer's
protocol, telemetry or control-profile baseline. M16's policy decision remains
open.

Change class: **editorial / navigation**. No consumer migration is introduced.
[ADR 0036](../../docs/adr/0036-land-v050-correction-batch-from-the-corpus-review.md)
records the earlier correction batch;
[ADR 0040](../../docs/adr/0040-adopt-source-authority-classes-and-evidence-weighted-citations.md)
and [source grading](../patterns/source-authority-and-evidence-grading.md)
govern this evidence record;
[ADR 0049](../../docs/adr/0049-add-doctrine-integrity-gates-and-obligation-routing.md)
governs the existing link and printed-example checks. No new policy decision
or ADR acceptance is made here.

## Evidence Method And Limits

All external sources below were accessed on 2026-09-19. Each source record
states its class, claim-specific scope, role and pin. Publisher descriptions
are evidence of documented behaviour, not live implementation tests. Sources
from one publisher count once for independence. Local source captures with
SHA-256 hashes were retained separately; no public archive URL is claimed.
Repository references in m02/m13 establish existing doctrine only.

This is a bounded citation check, not the full release-delta source sweep or
an admission review of neighbouring untyped claims. Descriptive removals do
not establish that the opposite empirical claim is true.

## m01 Registry Status

**Before:** [AI/ML §7](../principles/ai-ml-systems.md) embedded a live preview
label in the allowlist rule. **After:** the rule retains curated admission,
namespace authentication and the distinction between publication and vetting;
the transient status is recorded here.

The [publisher's about page](https://modelcontextprotocol.io/registry/about)
still described the registry as preview, with possible breaking changes or
data resets, on the access date. It documents metadata hosting, namespace
authentication and delegated code scanning. The same material was inspected
at [registry commit d1dcaf3fb36338d45ccdba98b5b8aea915e7d50d](https://github.com/modelcontextprotocol/registry/blob/d1dcaf3fb36338d45ccdba98b5b8aea915e7d50d/docs/modelcontextprotocol-io/about.mdx).
**S5, primary, product-scoped; commit pin; C2 for documented registry behaviour.**
Limit: this does not prove scanning coverage, safety of a listed server, or
host compliance. Review when the publisher changes the trust model.

## m02 Exception Review Route

**Before:** [zero trust §2.1](../principles/zero-trust-and-workload-identity.md)
named governance re-absorption without a destination. **After:** that phrase
links to the existing
[exception contract §5](../patterns/normative-language-applicability-and-exceptions.md#5-exception-contract),
including its route for permanent deviations into policy/profile revision.
No exception approver, expiry, principal-isolation condition or review duty
has changed. Evidence is the existing canonical text; no external claim is
added.

## m03 Unbounded Cost Claim

**Before:** [cost §7](../principles/cost-and-finops.md) called inference the
fastest-growing cloud cost category for engineering teams in 2026 and compared
one workflow's exposure with an entire service's monthly budget without a
defined population or measurement. **After:** the rationale states the
mechanism: usage charges accumulate across calls and retries, and budgets and
circuit breakers bound exposure.

The removed ranking is not treated as verified, false, or replaced by another
market estimate. No new empirical ranking is admitted. The existing controls,
provider-limit caveats, cost accounting and loop-economics evidence route
remain intact.

## m13 Merge-Path Readability

**Before:** [merge-path §1/§2](../principles/merge-path-evidence-and-pipeline-integrity.md)
put the agent-definition boundary in one table cell and combined attack
history, review duties and admission links in one long invariant.
**After:** the boundary follows the definition table, and invariant 2 has
separate paragraphs for the threat example, review duties and admission route.

The privileged capabilities, merge-path/standing-credential activation,
interactive-session exclusion, protected-path treatment, no-self-review rule,
informed-reviewer duty and third-party admission route are retained. The
existing attack citations were not re-admitted or independently re-audited
as part of this formatting repair.

## m14 SBOM Publication Status

**Before:** the [merge-path references](../principles/merge-path-evidence-and-pipeline-integrity.md)
called the 2025 minimum-elements publication a draft while implying a
superseding role. **After:** the reference distinguishes that historical draft
from the published 2026 successor.

- [2025 publisher landing page](https://www.cisa.gov/resources-tools/resources/2025-minimum-elements-software-bill-materials-sbom): published 2025-08-22; still explicitly describes a public-comment draft, with comments closing 2025-10-03. **S3 provisional, primary, draft-guidance scope; pin: 2025 draft and captured landing page.** It is not evidence of a final 2025 baseline.
- [2026 publisher landing page](https://www.cisa.gov/resources-tools/resources/2026-minimum-elements-software-bill-materials-sbom): published 2026-07-29; identifies released joint guidance incorporating the 2025 consultation and replacing NTIA's 2021 minimum elements. It links the [July 2026 publication](https://www.cisa.gov/sites/default/files/2026-07/2026_cisa_sbom_minimum_elements_508c.pdf). **S2, primary, institutional SBOM guidance; pin: July 2026 edition and captured landing page; C2 for the publisher's publication/successor statement.**

The status finding comes from the publisher's landing-page text, retrieved
directly after the browsing service could not fetch it. This check does not
assess every changed SBOM field or establish a legal obligation. Existing
profile pins and any migration decision remain under
[revision-pinned control profiles](../patterns/revision-pinned-control-profiles.md).
Review on further publisher revision or when an estate considers migration.

## m18 Registry Support Claim

**Before:** [dependencies §3](../principles/dependencies-supply-chain.md)
called OCI attestation support standard across three named registries.
**After:** attachment remains required through the selected registry's
supported attestation mechanism, associated with the image digest; the
blanket product-support assertion is removed.

[OCI image-spec v1.1.1 manifest](https://github.com/opencontainers/image-spec/blob/v1.1.1/manifest.md)
was inspected as a boundary check: its artifact packaging and optional
`subject` descriptor describe associations to another manifest. **S4,
primary, versioned foundation specification; pin: v1.1.1.** This establishes
neither attestation semantics nor implementation support in any registry.
The repair adopts no new OCI version or attestation format and preserves
machine readability, per-artifact retention, rescanning and promotion duties.

## m21 GenAI Telemetry Compatibility

**Before:** [observability tooling](../tooling/observability.md) combined live
stability/version claims, vendor defaults, adoption claims and an unqualified
absence-of-cost assertion. **After:** the illustration is bounded to an
inspected commit, distinguishes specification advice from runtime behaviour,
and removes the unsupported exclusivity and backend-adoption claims.

The dedicated repository was inspected at commit
`c88d504ab3d9879f8e50d3cc87e69775e11db234` (publisher commit date 2026-09-16):

- [GenAI overview](https://github.com/open-telemetry/semantic-conventions-genai/blob/c88d504ab3d9879f8e50d3cc87e69775e11db234/docs/gen-ai/README.md): Development status.
- [Model/tool spans](https://github.com/open-telemetry/semantic-conventions-genai/blob/c88d504ab3d9879f8e50d3cc87e69775e11db234/docs/gen-ai/gen-ai-spans.md) and [agent spans](https://github.com/open-telemetry/semantic-conventions-genai/blob/c88d504ab3d9879f8e50d3cc87e69775e11db234/docs/gen-ai/gen-ai-agent-spans.md): inference, embeddings, create/invoke agent, invoke workflow, plan and execute-tool vocabulary; sensitive message content is opt-in, with default omission recommended.
- [Metrics](https://github.com/open-telemetry/semantic-conventions-genai/blob/c88d504ab3d9879f8e50d3cc87e69775e11db234/docs/gen-ai/gen-ai-metrics.md) and [GenAI attribute registry](https://github.com/open-telemetry/semantic-conventions-genai/blob/c88d504ab3d9879f8e50d3cc87e69775e11db234/model/gen-ai/registry.yaml): token/latency signals; no generic cost, price or currency field found in those inspected surfaces. This is a scoped absence finding, not a promise about future revisions or every provider-specific extension.

**S3 provisional, primary developing specification; commit pin; C2 for the
snapshot's documented vocabulary and status.** The core repository's
[v1.42.0 changelog](https://github.com/open-telemetry/semantic-conventions/blob/v1.42.0/CHANGELOG.md#v1420)
confirms relocation and deprecation in the core repository. **S4, primary
versioned foundation release record; pin: v1.42.0.** It is the same publisher,
not independent corroboration. Repository relocation does not mean the
dedicated repository has retired the `gen_ai.*` namespace.

No SDK, exporter, backend or billing integration was run. Pinning and the
existing mapping-layer advice remain; consumer instrumentation pins do not
change. Review on a selected convention or instrumentation upgrade.

## m23 Migration Guidance

**Before:** [data/migrations references](../principles/data-and-migrations.md)
cited a practitioner overview for safe/unsafe DDL. **Finding:** the
[James Ross Jr. article](https://www.jamesrossjr.com/blog/database-migrations-guide)
exists, is titled as cited and displays publication date 2026-03-03. **S6,
secondary practitioner guidance; dated article and captured page.** It explains
expand/contract, but incorrectly calls ordinary `CREATE INDEX` an access-share
lock. Its constant-default example is scoped to PostgreSQL 14+; that is narrower
than the documented support, not an explicit claim that the feature began in 14.

PostgreSQL's own documentation supplies the precise locking and version details:

- [PostgreSQL 18 explicit locking](https://www.postgresql.org/docs/18/explicit-locking.html) assigns ordinary `CREATE INDEX` a `SHARE` lock; `ACCESS SHARE` alone does not block ordinary writes.
- [PostgreSQL 18 CREATE INDEX](https://www.postgresql.org/docs/18/sql-createindex.html) documents the concurrent-build option, waits, load and failure caveats. It does not guarantee zero application impact.
- [PostgreSQL 11 modifying tables](https://www.postgresql.org/docs/11/ddl-alter.html) already documents fast constant-default addition. The [version 18 counterpart](https://www.postgresql.org/docs/18/ddl-alter.html) retains that distinction and explains why volatile defaults may require staged work.

**S5, primary product documentation; pins: PostgreSQL majors 11 and 18 plus
captured pages; C2 for these engine-specific behaviours.** Version 11 is used
only to check the historical threshold, not recommended for adoption. The
canonical reference now points to the three version 18 pages for DDL details;
existing parallel-change and book references remain. Database versions,
forward-only duties and batch defaults are unchanged. The article's existence
rejects the historical fabrication suspicion; its technical limitations
justify replacing this supporting citation without alleging fabrication.

## m27 Platform Survey Claim

**Before:** [platform rationale](../principles/platform-engineering.md)
asserted that consumer NPS is a leading indicator of platform health.
**After:** surveys, including NPS, are satisfaction feedback alongside adoption
and delivery measures, without a predictive-health assertion.

The [CNCF Platforms White Paper v1](https://github.com/cncf/tag-app-delivery/blob/cadc7760e7e55a8c9a26c58c53d9d567fd6dcb9d/platforms-whitepaper/v1/index.md)
lists NPS or other user-satisfaction surveys among several measurement
categories. **S4, primary foundation-reviewed guidance; pin: commit
`cadc7760e7e55a8c9a26c58c53d9d567fd6dcb9d`; C2 for the paper's measurement
guidance.** It does not supply longitudinal evidence that NPS predicts
platform health. No new survey mandate or metric target is introduced.

## M16 SLSA Attribution — Decision Remains Open

[SLSA v1.2 Build requirements](https://slsa.dev/spec/v1.2/build-requirements)
are marked Approved and distinguish L2 authentic provenance/hosted builds from
L3 unforgeable provenance/isolation. The isolation discussion explicitly
distinguishes hermeticity; it does not impose a no-network build requirement.
It prohibits cache poisoning rather than all cache sharing. The
[v1.2 FAQ](https://slsa.dev/spec/v1.2/faq#q-what-about-reproducible-builds)
distinguishes reproducible outputs from independent verified reproduction;
verified reproducible builds are an implementation option, not a directly
required SLSA mechanism. **S4, primary approved foundation specification;
pin: v1.2; C2 for specification interpretation.**

This does not make an L2 minimum inconsistent with an additional library
requirement for hermetic or reproducible builds. The owner must decide between:

1. Retain those additional duties, explicitly identify them as library policy
   beyond the pinned SLSA level, and separately correct the level table's
   attribution, scope and evidence requirements.
2. Change their applicability or strength through the pending policy work,
   with consumer-impact and source-admission review.

Neither option is adopted here. Dependencies §4 is unchanged. Source checking
alone cannot choose the policy strength or justify marking M16 resolved.
