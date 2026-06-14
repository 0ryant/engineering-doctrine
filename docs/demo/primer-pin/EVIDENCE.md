# Evidence — LU-N06: self-proving primer content-pin

**Task.** Make the primer content-pin self-proving: compute sha256 over the
canonical in-repo primer body, assert it equals the hard-coded `PRIMER_SHA256`,
and wire a CI check that FAILS on drift.

**Date.** 2026-06-12
**Branch.** `feat/level-up-now-2026-06-12`

## What the integrity claim was

The canonical ~200-token anti-confabulation priming block lives in
`doctrine/skills/anti-confabulation.skill.md` (the first triple-backtick fenced
block). The doctrine pins it by SHA-256 in three places:

1. `PRIMER_SHA256` in `scripts/validate-contracts-v1.py` — the value every
   router-policy tier carries as `primer_sha256`.
2. The `priming_block_sha256` front-matter field of the skill file.
3. The in-prose `Canonical fingerprint: sha256:...` line of the skill file.

Before this change those three were **asserted text** — nothing recomputed the
hash from the actual block body, so the central claim was self-referential and
could silently rot the moment anyone edited the block.

## What changed

- **`scripts/verify-primer-pin.py`** (new, stdlib-only, deterministic).
  Extracts the priming block, normalises CRLF→LF, recomputes sha256 + byte/word
  counts, and asserts the recomputed hash equals `PRIMER_SHA256` AND that all
  three on-disk copies + the validator constant agree. Exits non-zero on any
  drift.
- **`.github/workflows/contracts.yml`** — new "Verify primer content-pin" step
  that runs `verify-primer-pin.py` before dependency install (so a drift fails
  fast, no third-party deps needed).
- **`scripts/validate-contracts-v1.py`** — imports the pin module, asserts its
  `PRIMER_SHA256` literal equals the pin's source of truth, and runs the pin as
  the first check in `main()`.
- **`doctrine/skills/anti-confabulation.skill.md`** — note that the pin is now
  machine-enforced, not merely asserted.

## Reproduction of the canonical hash (independent path)

The documented git-object reproducer agrees with the script:

```
$ git cat-file -p HEAD:doctrine/skills/anti-confabulation.skill.md \
  | awk '/^```$/{c++; if (c==1){p=1; next} else if (c==2){p=0}} p' | sha256sum
c138dd966c82f7bd792684ab3fef0f50d75aa9342468db8b5d265f24f3fb35a8  -
# bytes: 1444   words: 231
```

## Positive case — passes

```
$ python scripts/verify-primer-pin.py ; echo EXIT=$?
primer-pin: VALID (sha256=c138dd966c82f7bd792684ab3fef0f50d75aa9342468db8b5d265f24f3fb35a8, 1444 bytes, 231 words; recomputed from in-repo block, all 3 on-disk copies + validator constant agree)
EXIT=0
```

Wired into the full harness (first line of output):

```
$ python scripts/validate-contracts-v1.py
primer-pin: VALID (sha256=c138dd966c82f7bd792684ab3fef0f50d75aa9342468db8b5d265f24f3fb35a8)
pr-evidence-build-review: VALID
... (all contract cases VALID / negatives rejected as expected) ...
EXIT=0
```

## Drift cases — FAIL loudly (the point of the task)

All three were exercised by mutating the real file, running the script, then
restoring from git.

**Drift 1 — one word changed inside the priming block body:**

```
primer-pin: FAILED
  - PRIMER_SHA256 drift: recomputed sha256 of the in-repo priming block =
    5fef13fccea77d7075b4c20c882ce639b36b22cc418f6702d0b914494d55f9f0,
    but PRIMER_SHA256 = c138dd966c82f7bd792684ab3fef0f50d75aa9342468db8b5d265f24f3fb35a8
EXIT=1
```

**Drift 2 — stale front-matter `priming_block_sha256` (body unchanged):**

```
primer-pin: FAILED
  - front-matter priming_block_sha256 = 0000...0000 != c138...35a8
EXIT=1
```

**Drift 3 — drifted `PRIMER_SHA256` constant in the validator script:**

```
primer-pin: FAILED
  - validate-contracts-v1.py PRIMER_SHA256 = deadbeef...0000 != c138...35a8
EXIT=1
```

After each drift, `git checkout --` restored the file and the script returned
`EXIT=0` (`primer-pin: VALID`).

## Status

- Build: n/a (content/Python repo, no compile step).
- Tests: `scripts/verify-primer-pin.py` and `scripts/validate-contracts-v1.py`
  both green; three drift cases proven to fail.
