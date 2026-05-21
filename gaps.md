# gaps

Source: `C:/Users/0ryant/prj/ecosystem-catalog/manager-reports/2026-05-21-ecosystem-synthesis-next-level.md`

## Goal

Harmonise public doctrine positioning and licensing language across the catalog
and the doctrine repository.

## Missing

- Single source of wording for the current licence posture.
- Catalog language that matches the repository README.
- Release-surface wording for public, gated, and commercial-use paths.
- Clear pointer from policy-control mapping back to doctrine principles.

## Steps

1. Confirm the current license and commercial-positioning language with the
   operator.
2. Update ecosystem-catalog references to match the doctrine README.
3. Add or update a short doctrine positioning note if the wording is intended
   to be canonical.
4. Link the ecosystem policy-control map to the doctrine semantic index.
5. Run markdown lint in both repos.
6. Keep normative doctrine changes out of this file unless a doctrine harness
   task is explicitly opened.

## Acceptance evidence

- Catalog, release-surface, and doctrine README wording no longer conflict.
- Policy-control map cites doctrine as the source of principles, not as a
  certification claim.
- Markdown lint passes for touched docs.

## Stop conditions

- Do not change `doctrine/`, `docs/adr/`, or `ENGINEERING.md` without the
  doctrine library change harness.
- Do not state certification or audit readiness from doctrine text alone.
