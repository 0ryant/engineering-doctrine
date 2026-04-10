# Dependency Automation Tooling

**Example** patterns for automated dependency updates and security signal, related to [../principles/dependencies-supply-chain.md](../principles/dependencies-supply-chain.md). Your org’s bots, hosts, and policies may differ—see [../principles/timeless-principles-and-tooling.md](../principles/timeless-principles-and-tooling.md).

---

## Options At A Glance

| Tool | Strengths | Limits |
| --- | --- | --- |
| **GitHub Dependabot** | Native on GitHub, low setup, **Dependabot alerts** for vulnerabilities | Configuration less flexible; historically more **PR noise** in large repos |
| **Renovate** | **Grouping**, presets, **many platforms** (GitHub, GitLab, Azure DevOps, etc.), regex managers | More configuration; hosted app or self-hosted |
| **OSV / advisory APIs** | **Vulnerability** identification cross-ecosystem | Not a PR bot by itself |

Official comparison from Renovate (aims to be objective): https://docs.renovatebot.com/bot-comparison/

---

## Example policies

1. **GitHub-only, small repos** — enable **Dependabot version updates** + **Dependabot security updates**; use **grouped updates** where available to reduce noise ([GitHub blog, grouped updates](https://github.blog/2023-08-24-a-faster-way-to-manage-version-updates-with-dependabot/)).

2. **Monorepos, polyglot repos, or multi-platform Git hosts** — prefer **Renovate** with **organisational presets** (shared `renovate.json` inheritance), scheduled runs, and **grouping** rules per ecosystem.

3. **Security signal** — keep **Dependabot alerts** enabled on GitHub even when Renovate opens upgrade PRs; many teams use **alerts** as early signal and **Renovate** for structured upgrades (community-reported pattern).

4. **Licence policy** — add **SCA** tools that surface **copyleft** or **deny-listed** licences (for example **FOSSA**, **Snyk** licence checks, **GitHub** dependency review) where legal expects **automated** gates on the merge path.

**Why:** Renovate’s docs emphasise **grouping**, **dashboard**, and **multi-platform** support; Dependabot emphasises **zero config** and **tight GitHub integration**. The split avoids “200 PRs/week” meltdown on large JS monorepos while preserving GitHub’s **alerting**.

---

## Policy Hooks

- **Auto-merge** only for patch/minor per policy, with CI green; never blind-merge majors without review.
- **Pinning** — Renovate supports **rangeStrategy** and lockfile maintenance; Dependabot respects lockfiles per ecosystem.

---

## Rationale And Decisions

| Decision | Rationale |
| --- | --- |
| Automate updates | Humans forget; **cadence** beats heroics before releases. |
| Prefer grouping in large repos | Reduces **review fatigue** and **merge conflicts** (Renovate docs, community experience). |
| Keep security alerts separate from bot choice | **CVE signal** should not depend on a single bot’s PR cadence. |
| Org-level presets | Same **policy** across hundreds of repos. |

---

## References

- Renovate — **Bot comparison**: https://docs.renovatebot.com/bot-comparison/  
- Renovate — **Configuration options**: https://docs.renovatebot.com/configuration-options/  
- GitHub — **Dependabot documentation**: https://docs.github.com/en/code-security/dependabot  
- GitHub — **Grouped security updates** (Dependabot ecosystem): see GitHub changelog / docs for grouped updates evolution.  
- OSV (Open Source Vulnerabilities): https://osv.dev/  
- GitHub **Dependency review** (licence and vulnerability summary on PRs): https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review  
