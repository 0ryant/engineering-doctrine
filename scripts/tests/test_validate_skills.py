"""Tests for the governing-layer rule in scripts/validate-skills.py.

Incident (2026-11-18): ADR 0047 moved three maintainer patterns from
doctrine/patterns/ to doctrine/maintainers/. The validator recognised a pattern
only by the doctrine/patterns/ prefix, so the citation skill, whose governing
patterns had all moved, was refused with "governing must include at least one
principle or pattern" although its governing files are patterns.

The accepting arms guard that incident. The refusing arms prove the rule can
still fail: a skill governed only by a checklist or a register is refused, and
each refusal is checked by its exact text, not by a non-empty error list.
"""
from __future__ import annotations

import datetime as dt
import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

REPO = Path(__file__).resolve().parents[2]
VALIDATOR = REPO / "scripts" / "validate-skills.py"
SKILL = "evidence-graded-citation"
REASON = "governing must include at least one principle or pattern"
START, END = "  governing:\n", "  priming_block_sha256:"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_skills", VALIDATOR)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def schema(name: str) -> Draft202012Validator:
    return Draft202012Validator(json.loads((REPO / "contracts" / name).read_text(encoding="utf-8")))


class GoverningLayerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.validator = load_validator()
        self.validator.ROOT = self.root
        self.skill_dir = self.root / "doctrine" / "skills" / SKILL
        shutil.copytree(REPO / "doctrine" / "skills" / SKILL, self.skill_dir)
        self.rel = f"doctrine/skills/{SKILL}/SKILL.md"

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def errors_for(self, governing: list[str]) -> list[str]:
        """Rewrite the copied skill's governing list and validate it."""
        for path in governing:
            target = self.root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("# Fixture\n", encoding="utf-8")
        skill_md = self.skill_dir / "SKILL.md"
        text = skill_md.read_text(encoding="utf-8").replace("\r\n", "\n")
        self.assertEqual(text.count(START), 1, "fixture skill has no governing block to rewrite")
        start = text.index(START) + len(START)
        end = text.index(END)
        self.assertGreater(end, start, "governing block is not followed by the hash field")
        block = "".join(f"    - path: {path}\n" for path in governing)
        skill_md.write_bytes((text[:start] + block + text[end:]).encode("utf-8"))
        return self.validator.validate_skill(
            self.skill_dir,
            schema("skill.v1.schema.json"),
            schema("verifier-pack.v1.schema.json"),
            dt.date(2026, 11, 18),
        )

    def test_maintainer_pattern_governs(self) -> None:
        self.assertEqual(self.errors_for(["doctrine/maintainers/source-authority-and-evidence-grading.md"]), [])

    def test_pattern_governs(self) -> None:
        self.assertEqual(self.errors_for(["doctrine/patterns/fixture.md"]), [])

    def test_principle_governs(self) -> None:
        self.assertEqual(self.errors_for(["doctrine/principles/fixture.md"]), [])

    def test_checklist_alone_is_refused_for_the_stated_reason(self) -> None:
        self.assertEqual(self.errors_for(["doctrine/checklists/fixture.md"]), [f"{self.rel}: {REASON}"])

    def test_register_alone_is_refused_for_the_stated_reason(self) -> None:
        self.assertEqual(self.errors_for(["doctrine/EVIDENCE-EXCEPTIONS.md"]), [f"{self.rel}: {REASON}"])


if __name__ == "__main__":
    unittest.main()
