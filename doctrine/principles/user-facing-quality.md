# User-Facing Quality: Accessibility And Internationalisation

Durable rules for **software with a UI** (web, desktop, mobile): **accessibility** is part of **quality**, not decoration; **internationalisation** is planned early when multiple locales matter.

---

## 0. Scope

- This principle applies **when the product exposes a user interface** to humans (graphical, TTY with semantics, or hybrid). Pure libraries, CLIs that are **operator-only** with no compliance target, and headless workers may **document “UI N/A”** and skip WCAG targets—still follow any **organisation** accessibility policy if one exists.
- **Desktop OS, kiosk, or institutional** surfaces often face **stronger** legal and procurement requirements than internal tools. When those surfaces are **in roadmap**, plan **WCAG-aligned** engineering early—not as a late polish pass.
- The full doctrine tree is **not** a substitute for **jurisdiction-specific** legal advice where regulated sectors apply.

---

## 1. Accessibility (A11y)

- Meet an **explicit** standard (for example **WCAG 2.2** Level AA for web properties) where the product is customer-facing or legally required.
- **Keyboard** navigation, **visible focus**, **focus order**, **programmatic name/role** for controls, **labels** (visible or associated), **contrast**, and **motion** (`prefers-reduced-motion`) matter for compliance and **usability**.
- **Screen reader** and **voice control** flows: preserve a sensible **reading order**; don’t rely on colour alone for state; provide text alternatives for non-decorative imagery and icons that convey meaning.
- **Custom widgets** (data grids, sliders, drag-and-drop) need **documented** interaction and ARIA patterns appropriate to the platform; prefer **native** controls when they meet requirements.
- Automated **a11y** checks in CI where feasible (**linting** against known anti-patterns); **manual** and **assistive-tech** smoke tests for critical journeys—automation cannot prove full compliance.

**Why:** WCAG is the de-facto benchmark; many jurisdictions reference accessible ICT for public and enterprise procurement. Beyond law, a11y improves **everyone’s** experience (voice control, bright sunlight, motor limitations).

---

## 2. Internationalisation (i18n) And Localisation (l10n)

- **Externalise strings** early; avoid concatenating translated fragments.
- Plan for **pluralisation**, **gender**, **RTL** layouts, and **locale-aware** dates/numbers/currency.
- **Pseudo-localisation** in CI can catch overflow and missing strings before translators see them.
- **Locale negotiation** — document how the user or system selects language/region; avoid silent fallbacks that confuse audits.

**Why:** Retrofitting i18n after a large English-only codebase is expensive; layout assumptions break **RTL** and long translations.

---

## 3. Mobile, Voice-First, And Document Surfaces

- **Mobile** — respect **platform** accessibility settings (Dynamic Type, TalkBack/VoiceOver); touch targets and **gesture** alternatives should meet **WCAG**-aligned guidance for the **web** or **native** stack you ship.
- **Voice UIs** — design **confirmations** and **disambiguation** for spoken commands; log **structured** intent for debugging **without** storing raw audio unless contractually allowed.
- **PDF** and **static** exports — if customers **consume** compliance or billing PDFs, apply **tagged PDF** / **logical reading order** practices (see **PDF/UA** references) and test with **screen readers** where required.

**Why:** Procurement and **public-sector** RFPs increasingly mention **mobile** and **document** accessibility—not only marketing sites.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| WCAG AA as default public-web target | Balances **rigour** with achievability; AAA is situational. |
| §0 scope | Prevents **performative** a11y rules on headless-only repos while flagging **OS/desktop** risk early. |
| CI a11y gates where possible | Catches **regressions** early; does not replace human review. |
| i18n as architecture | Prevents **string debt** and layout bugs in global launches. |
| Mobile/PDF explicit | Common **gap** between “web AA” claims and **actual** customer artefacts. |

---

## References

- W3C **WCAG 2.2** (Web Content Accessibility Guidelines): https://www.w3.org/TR/WCAG22/  
- W3C **Internationalization** resources: https://www.w3.org/International/  
- MDN — **Internationalization API** overview (browser): https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl  
- PDF Association — **PDF/UA** (accessible PDF overview): https://www.pdfa.org/resource/pdfua-basics/  
