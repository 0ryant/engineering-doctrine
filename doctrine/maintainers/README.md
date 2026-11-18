# Maintainer Patterns

These files govern how this library itself is changed. They bind the people and agents who change it and nobody else. If you are adopting the doctrine, skip this directory and start at [../README.md](../README.md).

They remain patterns. Their applicability condition is that you are changing this library ([ADR 0047](../../docs/adr/0047-separate-maintainer-doctrine-and-collapse-the-ai-native-sdlc.md)).

| File | What it owns |
| --- | --- |
| [doctrine-library-change-harness.md](doctrine-library-change-harness.md) | The change procedure: research, decision record, layered guidance, navigation, and verification. Also the release notes minimum (§9) and the maintainer checklist (§10). |
| [doctrine-content-lifecycle.md](doctrine-content-lifecycle.md) | The status vocabulary and its transitions: promotion, demotion, deprecation, exit, restoration, and the sweep. |
| [source-authority-and-evidence-grading.md](source-authority-and-evidence-grading.md) | Source classes, claim grades, and the evidence floor a rule has to meet. |

Kept outside this directory on purpose:

- [../DEPRECATED.md](../DEPRECATED.md) and [../EVIDENCE-EXCEPTIONS.md](../EVIDENCE-EXCEPTIONS.md), the two registers. Consumers and agents check them, and two skills name their paths.
- [../patterns/doctrine-versioning-and-consumer-compatibility.md](../patterns/doctrine-versioning-and-consumer-compatibility.md), which tells consumers what a release means for them.
- [../checklists/doctrine-change-checklist.md](../checklists/doctrine-change-checklist.md), the pre-merge list for a library change.
