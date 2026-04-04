# Environment Promotion Pattern

Use this pattern when a team promotes software through multiple environments before production.

---

## Goal

Increase confidence by validating the same built artifact through progressively higher-trust environments.

---

## Core Model

```text
commit -> quality gate -> build immutable artefact -> deploy to non-prod -> verify -> approve/promote -> deploy same artefact to prod
```

---

## Rules

- Build once where the platform allows.
- Tag or version the artifact at build time.
- Do not rebuild the artifact separately for staging and production.
- Store environment differences in configuration, secrets, identity, and external bindings.
- Run explicit post-deploy verification in each environment.
- Promotion requires evidence, not assumption.

## What Environments Are For

- **Development / sandbox**: rapid validation, integration feedback, exploratory testing.
- **Staging / pre-production**: production-like validation, smoke tests, release confidence.
- **Production**: controlled release of already validated artifacts.

## What Environments Are Not For

- Separate lines of code.
- Hidden manual fixes.
- Last-minute rebuilding.
- Permanent drift from the mainline.

## Good Promotion Signals

- quality gate passed
- contracts validated
- artifact signed or checksummed where required
- smoke tests passed
- migration status known
- rollback or roll-forward path identified
- operator evidence published

## Anti-Patterns

- “Works in staging” but production uses a different build
- environment-specific branches
- manual file edits in deployed environments
- promotion with no verification evidence
- bundling infrastructure, app release, and recurring jobs into one opaque step
