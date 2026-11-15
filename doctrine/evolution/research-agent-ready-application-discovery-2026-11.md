# Research: agent-ready application discovery — 2026-11

## Question

How should an estate express the decision that every application it ships must
be usable by both people and coding agents without relying on hidden setup or
repository-only documentation?

## Evidence boundary

Public specifications establish interoperable Skill shapes and concrete
autocomplete mechanisms. They do **not** establish that every application in
every estate should be forced into one universal interface. “Every app” is an
accountable estate/profile decision. Portable doctrine should define the
profile and its evidence, not silently make it the baseline for all consumers.

## Source ledger

| Source | Class and role | Pin / accessed | Supports | Does not establish |
| --- | --- | --- | --- | --- |
| [Agent Skills specification](https://agentskills.io/specification) | S4, primary for the published cross-host Skill form | Rolling whole-spec reference; accessed 2026-11-15; no archive captured because repository tooling has no archive step | A Skill can be a portable, metadata-bearing, progressively disclosed agent instruction package | That a Skill is authoritative, effective, safe, or mandatory for every app |
| [MCP stable Skills extension](https://github.com/modelcontextprotocol/ext-skills/blob/main/specification/stable/skills.mdx) | S1-equivalent within the extension's own protocol scope; primary | Stable branch path, monitored as rolling; accessed 2026-11-15; no archive captured | Machine discovery and retrieval of versioned Skills can be a protocol surface | Host support, user consent, or the quality of any Skill |
| [Bash programmable completion](https://www.gnu.org/software/bash/manual/html_node/Programmable-Completion.html) | S5, S1-equivalent within Bash behaviour; primary | Rolling product manual; accessed 2026-11-15 | A shell exposes a defined programmable completion mechanism | That Bash is the required shell or that completion should be hand-written |
| [PowerShell argument completion](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_argument_completion) | S5, primary for PowerShell behaviour | Rolling product documentation; accessed 2026-11-15 | A second major shell exposes a supported completion mechanism | Cross-shell parity or a portable generator |
| [Build Principles section 7](../principles/build.md#7-release-artefacts-include-operational-usefulness) | Repository authority | Pinned by consuming doctrine revision | Shell completions and other operationally required material are release artefacts, not afterthoughts | Which estates must require them for every app |
| [Agent Doctrine Consumption section 3](../patterns/agent-doctrine-consumption.md#3-skills) | Repository authority | Pinned by consuming doctrine revision | Skills are advisory, versioned, hashable and subject to lifecycle/evaluation | A product-specific Skill schema or release inventory |

## Synthesis

1. A Skill and autocomplete solve different discoverability failures. A Skill
   tells an agent what the product does, how to use it and where it must stop.
   Autocomplete tells a person or tool what valid actions exist at the point of
   use. One cannot substitute for the other.
2. Source-tree presence is weak evidence. Both surfaces can disappear from a
   package, installer, static exporter or host adapter. Exact packaged and
   installed-byte checks are the discriminating gate.
3. “All apps” requires a closed inventory. Without it, a new executable or
   adapter can evade the rule by being called unsupported, internal or merely
   an exporter after implementation.
4. Autocomplete is interface-specific. CLIs use generated shell completion;
   graphical applications use command/action autocomplete or a command
   palette; API-first applications use schema-backed IDE/client completion.
   The profile owns the outcome, not one mechanism.
5. Skills remain advisory. Packaging a Skill does not grant product authority,
   host trust, user consent or evidence that an agent followed it.

## Decision input

Adopt an optional, named **agent-ready application shipping profile**. An
estate activates it over an explicit app-surface inventory. Once activated,
each shippable row must carry both a versioned Skill bundle and an appropriate
autocomplete/discovery surface, with exact-artifact tests. The decision is a
normative tightening only for adopters that activate the profile.

## Risk asymmetry and limits

The profile adds packaging, inventory and compatibility-test cost. The guarded
failure is a shipped application that works only for maintainers who know its
hidden commands, or an agent that guesses unsafe/obsolete behaviour because no
bounded Skill is discoverable. For an estate deliberately standardising on
agent-ready applications, that cost is small relative to repeated integration
and misuse risk. This is a C2 risk-asymmetry judgement, not an empirical claim
that the profile improves every product or user.
