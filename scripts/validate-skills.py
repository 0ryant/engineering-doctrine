#!/usr/bin/env python3
"""
Validator for doctrine skills (ADR 0044).

Checks every doctrine/skills/<name>/SKILL.md:
  * YAML front matter validates against contracts/skill.v1.schema.json
  * front-matter name equals the directory name
  * exactly one fenced block with info string ``priming``, at most 4096 bytes
  * doctrine.priming_block_sha256 equals SHA-256 of that block (LF-normalised,
    fence lines excluded, single trailing newline)
  * every doctrine.governing[].path resolves on disk, and at least one is a
    principle or pattern
  * the sibling verifier-pack.yml exists, validates against
    contracts/verifier-pack.v1.schema.json, mirrors this skill by name, and
    contains at least one priming_active verifier
  * required body sections are present in order
  * review_date is not in the past for active skills

Subcommands:
  validate                     (default) validate every skill; exit 1 on any failure
  hash --skill NAME            print the canonical priming-block hash for NAME
  assert-primed --skill NAME --prompt FILE
                               exit 0 iff FILE contains the priming block for NAME
                               verbatim and the manifest hash matches. This is the
                               reference priming_active verifier command.

Dependencies: pyyaml, jsonschema (see requirements.txt).
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "doctrine" / "skills"
SKILL_SCHEMA = ROOT / "contracts" / "skill.v1.schema.json"
PACK_SCHEMA = ROOT / "contracts" / "verifier-pack.v1.schema.json"
MAX_BLOCK_BYTES = 4096
REQUIRED_SECTIONS = [
    "## Purpose",
    "## Instructions",
    "## Run-Contract Use",
    "## Required Independent Checks",
    "## Failure Handling",
    "## Limits",
]
FRONT_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
PRIMING_RE = re.compile(r"^```priming\n(.*?)^```[ \t]*$", re.S | re.M)


def _read_lf(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def split_skill(path: Path) -> tuple[dict, str]:
    text = _read_lf(path)
    m = FRONT_RE.match(text)
    if not m:
        raise ValueError("missing YAML front matter delimited by --- lines")
    front = yaml.safe_load(m.group(1))
    if not isinstance(front, dict):
        raise ValueError("front matter is not a mapping")
    return front, text[m.end():]


def priming_block(body: str) -> bytes:
    blocks = PRIMING_RE.findall(body)
    if len(blocks) != 1:
        raise ValueError(f"expected exactly one ```priming fenced block, found {len(blocks)}")
    block = blocks[0].rstrip("\n") + "\n"
    return block.encode("utf-8")


def block_hash(block: bytes) -> str:
    return hashlib.sha256(block).hexdigest()


def skill_dirs() -> list[Path]:
    if not SKILLS_DIR.is_dir():
        return []
    return sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir() and (p / "SKILL.md").is_file())


def validate_skill(skill_dir: Path, skill_validator, pack_validator, today: _dt.date) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    rel = skill_md.relative_to(ROOT).as_posix()
    try:
        front, body = split_skill(skill_md)
    except Exception as exc:  # noqa: BLE001 - report every failure shape
        return [f"{rel}: {exc}"]

    for err in sorted(skill_validator.iter_errors(front), key=lambda e: list(e.path)):
        loc = "/".join(str(p) for p in err.path) or "<root>"
        errors.append(f"{rel}: front matter {loc}: {err.message}")
    if errors:
        return errors

    name = front["name"]
    doc = front["doctrine"]
    if name != skill_dir.name:
        errors.append(f"{rel}: name `{name}` does not match directory `{skill_dir.name}`")

    block = b""
    try:
        block = priming_block(body)
    except ValueError as exc:
        errors.append(f"{rel}: {exc}")
    if block:
        if len(block) > MAX_BLOCK_BYTES:
            errors.append(f"{rel}: priming block is {len(block)} bytes; cap is {MAX_BLOCK_BYTES}")
        actual = block_hash(block)
        if actual != doc["priming_block_sha256"]:
            errors.append(
                f"{rel}: priming_block_sha256 mismatch: manifest {doc['priming_block_sha256'][:12]} actual {actual[:12]}"
            )
        declared_bytes = doc.get("priming_block_bytes")
        if declared_bytes is not None and declared_bytes != len(block):
            errors.append(f"{rel}: priming_block_bytes {declared_bytes} != actual {len(block)}")

    pos = -1
    for section in REQUIRED_SECTIONS:
        idx = body.find("\n" + section)
        if idx < 0:
            errors.append(f"{rel}: missing required section `{section}`")
        elif idx < pos:
            errors.append(f"{rel}: section `{section}` out of order")
        else:
            pos = idx

    has_authority_layer = False
    for entry in doc["governing"]:
        p = ROOT / entry["path"]
        if not p.exists():
            errors.append(f"{rel}: governing path does not exist: {entry['path']}")
        if entry["path"].startswith(("doctrine/principles/", "doctrine/patterns/")):
            has_authority_layer = True
    if not has_authority_layer:
        errors.append(f"{rel}: governing must include at least one principle or pattern")

    if doc["status"] == "active":
        review = _dt.date.fromisoformat(doc["review_date"])
        if review < today:
            errors.append(f"{rel}: active skill is past its review_date {review}")
    if doc["status"] == "deprecated" and not doc.get("superseded_by"):
        errors.append(f"{rel}: deprecated skill must name superseded_by")

    pack_path = skill_dir / "verifier-pack.yml"
    prel = pack_path.relative_to(ROOT).as_posix()
    if not pack_path.is_file():
        errors.append(f"{rel}: sibling verifier pack missing at {prel}")
        return errors
    try:
        pack_doc = yaml.safe_load(_read_lf(pack_path))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{prel}: YAML parse error: {exc}")
        return errors
    pack = pack_doc.get("verifier_pack", pack_doc) if isinstance(pack_doc, dict) else None
    if not isinstance(pack, dict):
        errors.append(f"{prel}: expected a mapping, optionally under verifier_pack:")
        return errors
    for err in sorted(pack_validator.iter_errors(pack), key=lambda e: list(e.path)):
        loc = "/".join(str(p) for p in err.path) or "<root>"
        errors.append(f"{prel}: {loc}: {err.message}")
    if pack.get("skill") != name:
        errors.append(f"{prel}: pack.skill `{pack.get('skill')}` does not mirror skill `{name}`")
    if pack.get("name") != f"{name}-verifier-pack":
        errors.append(f"{prel}: pack.name should be `{name}-verifier-pack`")
    kinds = [v.get("kind") for v in pack.get("verifiers", []) if isinstance(v, dict)]
    if "priming_active" not in kinds:
        errors.append(f"{prel}: pack must contain a priming_active verifier")
    return errors


def cmd_validate(_args) -> int:
    skill_validator = Draft202012Validator(_load_json(SKILL_SCHEMA))
    pack_validator = Draft202012Validator(_load_json(PACK_SCHEMA))
    dirs = skill_dirs()
    if not dirs:
        print("validate-skills: no skills found under doctrine/skills/", file=sys.stderr)
        return 1
    today = _dt.date.today()
    total_errors = 0
    for d in dirs:
        errs = validate_skill(d, skill_validator, pack_validator, today)
        status = "OK  " if not errs else "FAIL"
        print(f"[{status}] {d.name}")
        for e in errs:
            print(f"       {e}")
        total_errors += len(errs)
    print(f"validate-skills: {len(dirs)} skill(s), {total_errors} error(s)")
    return 1 if total_errors else 0


def cmd_hash(args) -> int:
    _front, body = split_skill(SKILLS_DIR / args.skill / "SKILL.md")
    block = priming_block(body)
    print(f"{block_hash(block)}  {len(block)} bytes")
    return 0


def cmd_assert_primed(args) -> int:
    skill_md = SKILLS_DIR / args.skill / "SKILL.md"
    front, body = split_skill(skill_md)
    block = priming_block(body)
    expected = front["doctrine"]["priming_block_sha256"]
    actual = block_hash(block)
    if actual != expected:
        print(f"priming_active: FAIL manifest hash {expected[:12]} != canonical {actual[:12]}")
        return 1
    prompt = Path(args.prompt).read_bytes().replace(b"\r\n", b"\n")
    if block.rstrip(b"\n") not in prompt:
        print(f"priming_active: FAIL priming block for `{args.skill}` not present verbatim in {args.prompt}")
        return 1
    print(f"priming_active: OK `{args.skill}@{front['doctrine']['version']}` sha256:{actual}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd")
    sub.add_parser("validate")
    h = sub.add_parser("hash")
    h.add_argument("--skill", required=True)
    a = sub.add_parser("assert-primed")
    a.add_argument("--skill", required=True)
    a.add_argument("--prompt", required=True)
    args = parser.parse_args(argv)
    if args.cmd in (None, "validate"):
        return cmd_validate(args)
    if args.cmd == "hash":
        return cmd_hash(args)
    return cmd_assert_primed(args)


if __name__ == "__main__":
    sys.exit(main())
