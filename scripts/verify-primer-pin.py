#!/usr/bin/env python3
"""Self-proving content-pin for the anti-confabulation priming block.

The doctrine ships a single load-bearing integrity claim: the canonical
~200-token priming block embedded in
``doctrine/skills/anti-confabulation.skill.md`` is an immutable artefact whose
SHA-256 is ``PRIMER_SHA256``. That hash is hard-coded in three places that MUST
never drift apart:

  1. ``PRIMER_SHA256`` in ``scripts/validate-contracts-v1.py`` (the value every
     router-policy tier pins as ``primer_sha256``).
  2. The ``priming_block_sha256`` front-matter field of the skill file.
  3. The in-prose ``Canonical fingerprint: sha256:...`` line of the skill file.

Until now those three were just *asserted text*: nothing recomputed the hash
from the actual block body, so the central claim was self-referential and could
silently rot the moment anyone edited the block. This script closes that gap.
It:

  * extracts the canonical priming block (the first triple-backtick fence in the
    skill file), normalising CRLF -> LF so a Windows checkout hashes identically
    to the canonical LF-only Git object;
  * recomputes the SHA-256, byte count and word count over that body;
  * asserts the recomputed hash equals the hard-coded ``PRIMER_SHA256`` and the
    declared byte/word counts; and
  * asserts all three on-disk copies of the hash agree with it.

Any drift (edited block, paraphrased copy, stale front-matter, mismatched
constant) FAILS loudly with a non-zero exit. It is wired into CI via
``.github/workflows/contracts.yml`` and is also called from
``validate-contracts-v1.py`` so the pin is proven on every push and PR.

Deterministic, no third-party dependencies (stdlib only).
"""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "doctrine" / "skills" / "anti-confabulation.skill.md"

# The single source of truth. Kept byte-identical to PRIMER_SHA256 in
# scripts/validate-contracts-v1.py; verify_consistency() asserts they agree.
PRIMER_SHA256 = "c138dd966c82f7bd792684ab3fef0f50d75aa9342468db8b5d265f24f3fb35a8"
PRIMER_BYTES = 1444
PRIMER_WORDS = 231


class PinError(Exception):
    """Raised when the content-pin fails to prove out."""


def read_normalised(path: Path) -> str:
    """Read *path* and normalise CRLF/CR to LF (canonical Git object form)."""
    raw = path.read_bytes()
    return raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n").decode("utf-8")


def extract_priming_block(text: str) -> str:
    """Return the canonical priming-block body, with its trailing newline.

    The canonical body is the content of the FIRST plain triple-backtick fenced
    block in the skill file (the block under "## The canonical priming block").
    Each content line carries a trailing LF, matching the documented reproducer

        git cat-file -p HEAD:doctrine/skills/anti-confabulation.skill.md \\
          | awk '/^```$/{c++; if (c==1){p=1; next} else if (c==2){p=0}} p' \\
          | sha256sum
    """
    lines = text.split("\n")
    body: list[str] | None = None
    for line in lines:
        if line.rstrip() == "```":
            if body is None:
                body = []          # opening fence
                continue
            # closing fence of the first block -> done
            return "".join(f"{ln}\n" for ln in body)
        if body is not None:
            body.append(line)
    raise PinError(
        f"no closing ``` fence found for the canonical priming block in {SKILL}"
    )


def find_front_matter_hash(text: str) -> str | None:
    m = re.search(r"^priming_block_sha256:\s*([0-9a-fA-F]{64})\s*$", text, re.M)
    return m.group(1).lower() if m else None


def find_front_matter_bytes(text: str) -> int | None:
    m = re.search(r"^priming_block_bytes:\s*(\d+)\s*$", text, re.M)
    return int(m.group(1)) if m else None


def find_front_matter_words(text: str) -> int | None:
    m = re.search(r"^priming_block_words:\s*(\d+)\s*$", text, re.M)
    return int(m.group(1)) if m else None


def find_prose_fingerprint(text: str) -> str | None:
    m = re.search(r"sha256:([0-9a-fA-F]{64})", text)
    return m.group(1).lower() if m else None


def verify() -> list[str]:
    """Run every pin assertion. Returns a list of human-readable failures."""
    failures: list[str] = []

    if not SKILL.exists():
        return [f"skill file not found: {SKILL}"]

    text = read_normalised(SKILL)
    body = extract_priming_block(text)
    body_bytes = body.encode("utf-8")

    computed_sha = hashlib.sha256(body_bytes).hexdigest()
    computed_bytes = len(body_bytes)
    computed_words = len(body.split())

    # 1. The recomputed hash MUST equal the hard-coded constant.
    if computed_sha != PRIMER_SHA256:
        failures.append(
            "PRIMER_SHA256 drift: recomputed sha256 of the in-repo priming "
            f"block = {computed_sha}, but PRIMER_SHA256 = {PRIMER_SHA256}"
        )

    # 2. Byte/word counts must match the declared invariants.
    if computed_bytes != PRIMER_BYTES:
        failures.append(
            f"byte-count drift: block is {computed_bytes} bytes, "
            f"expected {PRIMER_BYTES}"
        )
    if computed_words != PRIMER_WORDS:
        failures.append(
            f"word-count drift: block is {computed_words} words, "
            f"expected {PRIMER_WORDS}"
        )

    # 3. Front-matter copy must agree with the constant.
    fm_hash = find_front_matter_hash(text)
    if fm_hash is None:
        failures.append("front-matter priming_block_sha256 not found")
    elif fm_hash != PRIMER_SHA256:
        failures.append(
            f"front-matter priming_block_sha256 = {fm_hash} != {PRIMER_SHA256}"
        )

    fm_bytes = find_front_matter_bytes(text)
    if fm_bytes is not None and fm_bytes != computed_bytes:
        failures.append(
            f"front-matter priming_block_bytes = {fm_bytes} != {computed_bytes}"
        )
    fm_words = find_front_matter_words(text)
    if fm_words is not None and fm_words != computed_words:
        failures.append(
            f"front-matter priming_block_words = {fm_words} != {computed_words}"
        )

    # 4. In-prose "Canonical fingerprint: sha256:..." copy must agree too.
    prose_hash = find_prose_fingerprint(text)
    if prose_hash is None:
        failures.append("in-prose sha256 fingerprint not found")
    elif prose_hash != PRIMER_SHA256:
        failures.append(
            f"in-prose fingerprint sha256:{prose_hash} != {PRIMER_SHA256}"
        )

    # 5. The validator harness constant must agree with this one.
    failures.extend(_verify_validator_constant())

    return failures


def _verify_validator_constant() -> list[str]:
    """Assert scripts/validate-contracts-v1.py pins the same PRIMER_SHA256."""
    validator = ROOT / "scripts" / "validate-contracts-v1.py"
    if not validator.exists():
        return [f"validator script not found: {validator}"]
    vtext = read_normalised(validator)
    m = re.search(
        r'^PRIMER_SHA256\s*=\s*"([0-9a-fA-F]{64})"\s*$', vtext, re.M
    )
    if m is None:
        return ["PRIMER_SHA256 constant not found in validate-contracts-v1.py"]
    if m.group(1).lower() != PRIMER_SHA256:
        return [
            "validate-contracts-v1.py PRIMER_SHA256 = "
            f"{m.group(1)} != {PRIMER_SHA256}"
        ]
    return []


def main() -> int:
    failures = verify()
    if failures:
        print("primer-pin: FAILED")
        for f in failures:
            print(f"  - {f}")
        return 1
    print(
        "primer-pin: VALID "
        f"(sha256={PRIMER_SHA256}, {PRIMER_BYTES} bytes, {PRIMER_WORDS} words; "
        "recomputed from in-repo block, all 3 on-disk copies + validator "
        "constant agree)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
