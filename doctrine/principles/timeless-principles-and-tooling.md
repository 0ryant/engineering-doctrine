# Timeless Principles And Replaceable Tooling

How this repository stays **useful for years** while stacks change: separate **what must stay true** from **how you implement it today**.

---

## 1. Principles Are Platform And Vendor Agnostic

- **Principles** describe **outcomes**, **constraints**, and **trade-offs**—for example “promote immutable artefacts,” “contracts validated in CI,” “least privilege,” “correlate logs and traces.”
- They **do not** name a single cloud, a single CI product, or a single managed service as **the** answer for all readers.
- Where examples appear in principles, they are **illustrative** (“for example,” “such as”), not mandatory selections.

**Why:** Vendor SKUs and feature names change often; **intent** changes slowly. Doctrine that hard-codes products becomes stale and fights teams on different estates.

---

## 2. Tooling Is Illustrative And Estate-Specific

- **Tooling** documents capture **one possible** way to satisfy principles with concrete products and filenames (`.pipelines/`, `justfile`, a particular bot).
- **Estate supplements** live under `doctrine/tooling/estates/`—**optional** notes for a given organisation, region, or cloud (for example one team’s Azure mappings). They are **not** global law.
- Teams **swap** tooling while keeping the same **surface contracts** (quality gate, build artefact, deploy unit, verification) described in [build.md](build.md) and `ENGINEERING.md`.

**Why:** The split matches how senior engineers work: **interfaces and invariants** are negotiated; **implementations** are upgraded on a different cadence.

---

## 3. Standards Without Mandating A Full Stack

- Adopting a **wire format** or **specification** (for example for events or telemetry) does **not** mean adopting every project adjacent to that spec in an ecosystem catalogue.
- Interoperability choices are **narrow**: encode the **minimum** standard shape needed at boundaries.

**Why:** Avoids “standards creep” and **CNCF** or **vendor** stack pressure; see [interoperability-and-standards.md](interoperability-and-standards.md).

---

## 4. How To Change This Repository

- If an **operating model** change is real (how you ship, what you measure, what “done” means), update **principles** with **rationale** and **references**.
- If only **tools** change, update **tooling** / **estates** first; **avoid** editing principles unless the invariant actually changed.

---

## 5. Convictions, Interop Standards, And Team Validation

- **Interop choices** (for example a **standard envelope** for events) are **deliberate** standards at boundaries—they are not metaphysical truths. They are defensible **contract** decisions; teams may negotiate exceptions with a **recorded** migration story. See [interoperability-and-standards.md](interoperability-and-standards.md).
- **Illustrative tables** (languages, local container engines, example CI filenames) in `ENGINEERING.md` and **tooling** are **defaults for templates**, not mandatory global law. Organisation standardisation belongs in **`tooling/estates/`** when it must be shared.
- Doctrine that moves from **solo** depth to **multi-team** use should expect **pushback**, **legacy** code that violates many rules at once, and **time pressure** against contracts—address with **prioritisation** and pilots, not wholesale adoption overload. See [../patterns/adoption-playbook.md](../patterns/adoption-playbook.md).

**Why:** Without this distinction, preferences and **current** commercial context (for example workstation licensing) read as **timeless** principles and undermine trust.

---

## 6. Illustrative Map To NIST SSDF Practices (SP 800-218)

NIST’s **Secure Software Development Framework (SSDF)** groups practices into **Prepare (PO)**, **Protect (PS)**, **Produce (PW)**, and **Respond (RV)**. This repo is **not** a control framework mapping, but adopters often ask “where does SSDF live here?” The table below is a **non-exhaustive** cross-walk:

| SSDF group | Example practices | Doctrine touchpoints |
| --- | --- | --- |
| **PO** — Prepare the organisation | Security training, roles, supply-chain risk planning | [collaboration.md](collaboration.md) (ownership, review), [secure-development-lifecycle.md](secure-development-lifecycle.md), [dependencies-supply-chain.md](dependencies-supply-chain.md) |
| **PS** — Protect the software | Tamper-resistant environments, secrets management | [configuration-and-secrets.md](configuration-and-secrets.md), [build.md](build.md), [kubernetes-platform-security.md](kubernetes-platform-security.md) |
| **PW** — Produce well-secured software | Design review, secure coding, provenance, testing | [threat-modeling-stride-lite.md](threat-modeling-stride-lite.md), [testing-strategy.md](testing-strategy.md), [api-boundaries-and-security.md](api-boundaries-and-security.md), [build.md](build.md) §14 (SLSA) |
| **RV** — Respond to vulnerabilities | Identify, triage, disclose, learn | [secure-development-lifecycle.md](secure-development-lifecycle.md), [dependencies-supply-chain.md](dependencies-supply-chain.md) §5, [reliability-slo-incidents.md](reliability-slo-incidents.md) (post-incident learning) |

**Why:** SP 800-218 gives **auditors** and **security** partners a familiar vocabulary; mapping reduces duplicate questionnaires.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Principles avoid product mandates | Maximises **reuse** across clouds and acquisitions. |
| Explicit tooling tier | Lets templates be **opinionated** without pretending those opinions are physics. |
| Estate folder | Isolates **organisation-local** guidance from portable doctrine. |
| SSDF cross-walk table | Helps **regulated** readers without turning the repo into a **SOC2** checklist. |

---

## References

- (Conceptual) *Dan McKinley — Choose Boring Technology* — stability vs novelty in engineering choices: https://mcfunley.com/choose-boring-technology  
- DORA — linking **practices** to **delivery outcomes**: https://dora.dev/ (see also [measurement-and-dora.md](measurement-and-dora.md))  
- NIST **SP 800-218** — Secure Software Development Framework (SSDF): https://csrc.nist.gov/publications/detail/sp/800-218/final  
