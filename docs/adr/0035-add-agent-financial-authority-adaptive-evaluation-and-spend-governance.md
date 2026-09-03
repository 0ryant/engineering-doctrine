# ADR 0035: Add Agent Financial Authority, Adaptive Evaluation, And Spend Governance

- **Status:** Accepted
- **Decision date:** 2026-08-03
- **Recorded date:** 2026-08-03
- **Retrospective:** No

## Context

Final closure batch from the August 2026 gap audit ([research-bleeding-edge-ai-landscape-gap-audit-2026-08.md](../../doctrine/evolution/research-bleeding-edge-ai-landscape-gap-audit-2026-08.md)): the last normative gap (G11), two stale areas (S3, S4), and the S5 editorial refresh. With this ADR, every original audit finding is closed or explicitly tracked (G12/G13 remain low-severity watch items; crosswalk residues live in audit rows 19–22).

- **G11 — agent financial authority.** Every major payment network and agent platform shipped agent-payment rails in 2025–26 (Google-led AP2 mandates, Stripe ACP shared payment tokens, Mastercard Agentic Tokens, Visa Intelligent Commerce), all converging on registered per-agent identity, scoped limited-authority tokens, spending limits, and human approval for material transactions. Doctrine had token budgets but nothing on money agents *move*.
- **S3 — static-replay adversarial testing.** Adaptive attackers bypass defences reporting near-zero static attack success at >90% rates (Nasr et al.), and joint US/UK AISI agent-hijack red-teaming moved success from 11% to 81% once attackers iterated. Doctrine's adversarial CI predated agentic surfaces and never distinguished static replay from adaptive evaluation — including for the dual-path/CaMeL architecture doctrine itself recommends, whose published validations are static-benchmark only.
- **S4 — self-built-only spend controls.** Vendor spend planes matured (Azure agent-unit metering, Bedrock inference profiles/quotas, OpenAI/Anthropic org spend limits); doctrine's §7 knew only self-built breakers. **S5** — three SP 800-53 citations pinned at r5/upd1 while Release 5.2.0 (2025-08) added SI-02(07), SA-15(13), SA-24; none joined an 800-53B baseline, so they enter as candidates at the next baseline-diff cycle.

Council provenance: 11-agent draft council; 1 blocker (a shared References anchor that would have interleaved the two drafts' rows — resolved by single-pass consolidated application) and majors resolved in landed text. Verification note: the drafted "AWS Bedrock AgentCore Payments (preview)" citation failed primary verification during landing — the cited product page mentions no payments capability — and was removed from doctrine body; it is recorded here as an unverified vendor claim pending a payments-specific source. AP2's "draft standard" label was likewise softened to its verified framing (announced 2025-09, 60+ payments-sector supporters).

## Decision

1. **Agent financial authority (normative — G11).** New §7.1 in [cost-and-finops.md](../../doctrine/principles/cost-and-finops.md): **default-deny** — agents hold no payment instruments or transaction authority unless explicitly granted per-agent, inventory-recorded, on a dedicated §2.1 principal (money movement is on the materiality axis by definition; estates that never grant inherit only this bullet); granted authority is **session-scoped and budget-limited** outside the prompt, extending §7's budget discipline (one discipline, two denominations) with delegation unable to widen a payment budget; **materiality-tiered human approval** using the existing applicability vocabulary, with irreversible/critical-value transactions starting at approve-before-execute; **payment audit trails** carrying the full §2.1 attribution chain, idempotent across retries. AP2/Stripe/Mastercard/Visa cited as an informative standards watch. The agentic-loop §6 irreversibility enumeration gains **money-movement**; ASI02/ASI03 crosswalk cells gain navigational links.
2. **Adaptive evaluation (normative — S3).** [testing-strategy.md](../../doctrine/principles/testing-strategy.md) §5: agent tool-call paths and agent/skill configuration join the tiered adversarial surfaces (agent-definition artefacts are Tier 0 via the trust class); at blocking tiers, injection/hijack defence claims MUST be evidenced by **adaptive (attacker-iterates) evaluation**, with an explicit **trigger** (defence deployment, material change, model swap — not per merge) and **minimum viable form** (scoped human red-team with repeated trials, ~25 attempts per the AISI protocol; harnesses scale it). [agentic-loop-design.md](../../doctrine/patterns/agentic-loop-design.md) §9.4 attaches the duty to the dual-path/CaMeL claims: adopting the architecture does not discharge the testing duty. ai-adoption-controls §3 gains the agent-hijack harm-surface row (pointer to the canonical bar, per single-home discipline) and refreshed taxonomy references.
3. **Vendor-native spend governance (additive guidance — S4).** cost-and-finops §7 prefers vendor/org-level spend limits and entitlement defaults where the platform provides them, with self-built breakers as the **backstop layer and portable floor that remains in place** (the council rejected phrasing that read as licence to drop them); §4 gains agent-unit metering in anomaly scans (runaway loops that per-call token metrics smear) and Tier-D capacity planning.
4. **SP 800-53 Release 5.2.0 (editorial — S5).** Three citing files updated; the governance cadence table records catalog additions outside any 800-53B baseline as next-diff-cycle candidates, not automatic obligations.

## Alternatives Considered

### Fold financial authority into the autonomy slider

Rejected. The slider gates actions an agent is authorised to attempt; payment authority is **absent by default** — a stricter posture than any slider position, with grants routed through the exception contract rather than slider advancement.

### Mandate AP2-style cryptographic mandates now

Rejected. AP2 is announced, not settled; the portable invariants (default-deny, scoped budgets, tiered approval, attribution) are protocol-independent. Binding a protocol routes through revision-pinned profiles when one stabilises.

### Adaptive evaluation per merge

Rejected on council critique: an attacker-iterates exercise per Tier-0 steering-file edit is unrunnable and would rot into waivers. The duty binds at deployment/material-change/model-swap; merges reference current evidence.

### Drop self-built breakers where vendors enforce limits

Rejected. Vendor limits are preferred primary but plan-dependent and provider-scoped; the portable floor survives provider switches and application bugs.

## Consequences

### Positive

- The last ungoverned agent capability class — money movement — now has a floor the whole payments ecosystem already agrees on, at zero cost to estates that never grant it.
- Defence-effectiveness claims acquire an evidence bar that matches attacker behaviour, with a first-deployment form a small team can run in an afternoon.
- Spend governance uses the platform's own enforcement plane first, keeping the portable backstop.

### Costs And Risks

- Estates granting payment authority must stand up tier tables, scoped credentials, and payment audit joins.
- Adaptive exercises add a recurring red-team cost at defence-change/model-swap boundaries.
- The payments standards watch (AP2/ACP/Agentic Tokens/Intelligent Commerce) is pre-consolidation and will need revisiting; the unverified AgentCore Payments claim stays out of doctrine until primary-sourced.

## Consumer Impact

**Change class:** normative for estates granting agents financial authority (G11) or claiming injection/hijack defence effectiveness at blocking tiers (S3); additive guidance for spend governance (S4); editorial (S5). Estates outside those scopes change nothing — G11's default-deny is trivially satisfied by never granting.

**Compatibility proposal:** 0.x minor. All new MUSTs are activation-gated; S3 sharpens the evidence bar for testing duties that already bound, without expanding who they bind.

## Acceptance Evidence

- Audit provenance: G11/S3/S4/S5 confirmed (S-items verified stale) in the August 2026 audit; closure recorded in its §7 action list (rows 10, 14, 15, 18) — completing the audit's original finding set.
- Council provenance: 11-agent council; blocker and all majors resolved; one vendor citation removed on failed verification during landing.
- Primary sources indexed: AP2 announcement, Stripe/Mastercard/Visa agent-payment releases, OWASP AI Agent Security Cheat Sheet; Nasr et al. adaptive-attacks study, US/UK AISI hijacking-evaluations protocol, NIST AI 100-2e2025; Azure agent-unit pricing, Foundry cost management, Bedrock inference profiles/quotas, OpenAI/Anthropic spend-limit docs; NIST SP 800-53 Release 5.2.0 change record.

**Review provenance:** the council review cited above was model self-review (agent critics re-reading agent drafts). No independent human or domain review of this ADR has been recorded as of 2026-09-03.
