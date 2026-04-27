# Cursor rules (optional install)

This folder holds a **portable** Cursor rule for editing the engineering-doctrine library. The default repo [`.gitignore`](../../.gitignore) ignores `.cursor/`, so rules are not committed there by default.

## Install

Copy the rule into your local clone:

```bash
mkdir -p .cursor/rules
cp docs/cursor/doctrine-library-change.mdc .cursor/rules/
```

Or merge the YAML `description` and body into an existing **always-apply** rule you use for this repo.

## Source of truth

The full procedure lives in [`doctrine/patterns/doctrine-library-change-harness.md`](../../doctrine/patterns/doctrine-library-change-harness.md). The `.mdc` file is a short reminder; the harness is canonical.
