"""Run every verifier-pack check under doctrine/skills against fixtures.

scripts/validate-skills.py checks a pack's shape and the skill's block hash. It
does not execute the checks, so a check that can never fail, or one that
rejects correct input, passes validation. This module executes each check
command against at least one input it should accept and one it should reject.

A check with no accepting or no rejecting fixture fails the suite, so a new
check cannot be added without both.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / "doctrine" / "skills"

NAV = "doctrine-navigation"
CITE = "evidence-graded-citation"
READ = "normative-language-reading"
CONFAB = "anti-confabulation"
METHOD = "method-record-classification"

HUMAN = ("Jane Human", "jane@example.com")
TOOL_TRAILER = "Some Tool <noreply@tool.example>"
RECORD = "Produced-With: harness=h@1.2; doctrine=d@abc123; class="

# A small library the navigation checks can resolve against, independent of
# which real files are deprecated at any given revision.
LIBRARY = {
    "doctrine/principles/build.md": "# Build\n\nActive text.\n",
    "doctrine/patterns/active.md": "# Active\n\nBody.\n",
    "doctrine/patterns/dying.md": "# Dying\n\n> **Deprecated since v0.5.0** (ADR 0045): superseded by active.md.\n\nBody.\n",
    "doctrine/patterns/templated.md": "# Templated\n\n> **Status: Deprecated** (ADR 0001, since v0.1.0) - superseded by active.md\n\nBody.\n",
    "doctrine/patterns/gone.md": "# Gone\n\n> **Status: Retired** (ADR 0002). Last full text at v0.1.0.\n",
    "doctrine/patterns/explains-banners.md": "# Lifecycle\n\n" + "Body line.\n" * 20 + "> **Status: Deprecated** (ADR <NNNN>, since v<X.Y.Z>)\n",
}

# (skill, check id, label, should the check accept it, fixture)
CASES = [
    (NAV, "cited_paths_resolve", "cites a file that exists", True, {"report": "See doctrine/principles/build.md section 5.\n", "library": LIBRARY}),
    (NAV, "cited_paths_resolve", "cites a file that does not exist", False, {"report": "See doctrine/principles/nonexistent.md section 2.\n", "library": LIBRARY}),
    (NAV, "obligations_cite_authority_layer", "obligation citing the umbrella", True, {"report": "Each control SHOULD name its owner (ENGINEERING.md).\n"}),
    (NAV, "obligations_cite_authority_layer", "obligation citing a principle", True, {"report": "Teams MUST review changes per doctrine/principles/collaboration.md section 2.\n"}),
    (NAV, "obligations_cite_authority_layer", "no obligation asserted", True, {"report": "The file describes build surfaces.\n"}),
    (NAV, "obligations_cite_authority_layer", "obligation with no citation", False, {"report": "Teams MUST review every change.\n"}),
    (NAV, "obligations_cite_authority_layer", "obligation citing only a checklist", False, {"report": "Teams MUST do this per doctrine/checklists/build-readiness.md.\n"}),
    (NAV, "obligations_cite_authority_layer", "obligation citing only an implementation reference", False, {"report": "Teams SHOULD do this per doctrine/impl/service-api.md.\n"}),
    (NAV, "cited_files_not_deprecated", "cites an active file", True, {"report": "Per doctrine/patterns/active.md section 3.\n", "library": LIBRARY}),
    (NAV, "cited_files_not_deprecated", "cites a file that only describes the banner in its body", True, {"report": "Per doctrine/patterns/explains-banners.md.\n", "library": LIBRARY}),
    (NAV, "cited_files_not_deprecated", "cites a file with the banner form live files use", False, {"report": "Per doctrine/patterns/dying.md section 3.\n", "library": LIBRARY}),
    (NAV, "cited_files_not_deprecated", "cites a file with the lifecycle template banner", False, {"report": "Per doctrine/patterns/templated.md.\n", "library": LIBRARY}),
    (NAV, "cited_files_not_deprecated", "cites a retired tombstone", False, {"report": "Per doctrine/patterns/gone.md.\n", "library": LIBRARY}),

    (CITE, "citations_carry_source_class", "URL with class S5", True, {"report": "Source https://example.org/a [S5 C2, accessed 2026-11-18]\n"}),
    (CITE, "citations_carry_source_class", "URL classed X as the priming block writes it", True, {"report": "Source https://example.org/a [X C4, accessed 2026-11-18]\n"}),
    (CITE, "citations_carry_source_class", "URL with no class", False, {"report": "Source https://example.org/a accessed 2026-11-18\n"}),
    (CITE, "citations_carry_source_class", "URL beside a bare letter X that is not a class tag", False, {"report": "Platform X docs https://example.org/a accessed 2026-11-18\n"}),
    (CITE, "citations_carry_accessed_date", "URL with accessed date", True, {"report": "Source https://example.org/a [S5 C2, accessed 2026-11-18]\n"}),
    (CITE, "citations_carry_accessed_date", "URL with no date", False, {"report": "Source https://example.org/a [S5 C2]\n"}),
    (CITE, "must_claims_meet_floor", "C1 MUST", True, {"report": "Services MUST rotate keys [S2 C1, accessed 2026-11-18].\n"}),
    (CITE, "must_claims_meet_floor", "C3 MUST citing a registered exception", True, {"report": "Services MUST rotate keys [S5 C3, accessed 2026-11-18], admitted under EX-0003.\n"}),
    (CITE, "must_claims_meet_floor", "no MUST at all", True, {"report": "Teams usually rotate keys [S6 C3, accessed 2026-11-18].\n"}),
    (CITE, "must_claims_meet_floor", "C3 MUST with no exception", False, {"report": "Services MUST rotate keys [S5 C3, accessed 2026-11-18].\n"}),
    (CITE, "must_claims_meet_floor", "one excepted MUST and one not", False, {"report": "A MUST hold [S6 C3] under EX-0001.\nB MUST NOT happen [S7 C4].\n"}),
    (CITE, "disconfirmation_search_stated", "grades with a search statement", True, {"report": "Claim [S5 C2]. No contrary evidence found after searching the vendor docs.\n"}),
    (CITE, "disconfirmation_search_stated", "grades with no search statement", False, {"report": "Claim [S5 C2].\n"}),

    (READ, "no_document_wide_strength", "per-claim strength", True, {"report": "doctrine/principles/build.md section 5: SHOULD - publish from a release entrypoint.\n"}),
    (READ, "no_document_wide_strength", "whole-document strength", False, {"report": "This pattern is a MUST for all teams.\n"}),
    (READ, "exceptions_carry_expiry_and_authority", "complete exception", True, {"report": "Exception to build section 9, approved by the platform lead, expires 2027-01-31.\n"}),
    (READ, "exceptions_carry_expiry_and_authority", "the word used for a runtime error", True, {"report": "The handler raises an exception on timeout.\n"}),
    (READ, "exceptions_carry_expiry_and_authority", "a runtime error in a request path", True, {"report": "The request handler throws an exception when the retry policy is exhausted.\n"}),
    (READ, "exceptions_carry_expiry_and_authority", "proposed exception with no expiry or authority", False, {"report": "We propose an exception to build section 9.\n"}),
    (READ, "exceptions_carry_expiry_and_authority", "exception to a MUST with no expiry or authority", False, {"report": "An exception to the MUST in doctrine/principles/build.md is needed.\n"}),
    (READ, "evidence_state_named", "clean pass", True, {"report": "All 32 unit tests passed.\n"}),
    (READ, "evidence_state_named", "an honest count of passes and failures", True, {"report": "29 tests passed and 3 failed.\n"}),
    (READ, "evidence_state_named", "inconclusive called a pass", False, {"report": "The load test was inconclusive, so it passes.\n"}),
    (READ, "evidence_state_named", "stale evidence called a pass", False, {"report": "The scan result is stale but the gate passed.\n"}),

    (CONFAB, "declared_outputs_exist", "all declared outputs exist", True, {"declared": "ok"}),
    (CONFAB, "declared_outputs_exist", "a declared output is missing", False, {"declared": "missing"}),
    (CONFAB, "declared_outputs_exist", "nothing declared", False, {"declared": "empty"}),
    (CONFAB, "report_declares_unverified", "states what is unverified", True, {"report": "Unverified: behaviour under load.\n"}),
    (CONFAB, "report_declares_unverified", "says nothing about limits", False, {"report": "Done. Everything works.\n"}),
    (CONFAB, "report_binds_candidate", "names a commit", True, {"report": "Candidate 31cdea8 built and tested.\n"}),
    (CONFAB, "report_binds_candidate", "names a content digest", True, {"report": "Artefact sha256:" + "ab12" * 16 + " verified.\n"}),
    (CONFAB, "report_binds_candidate", "names no candidate", False, {"report": "Built and tested.\n"}),
    (CONFAB, "report_binds_candidate", "names no candidate but contains a date as digits", False, {"report": "Built and tested on 20261118.\n"}),

    (METHOD, "authorship_fields_human_only", "human co-author on the allowlist", True, {"candidate": (HUMAN, "feat: x\n\nCo-Authored-By: Jane Human <jane@example.com>\n")}),
    (METHOD, "authorship_fields_human_only", "no trailers", True, {"candidate": (HUMAN, "feat: x\n")}),
    (METHOD, "authorship_fields_human_only", "tool named as co-author", False, {"candidate": (HUMAN, "feat: x\n\nCo-Authored-By: " + TOOL_TRAILER + "\n")}),
    (METHOD, "authorship_fields_human_only", "tool named in a sign-off line", False, {"candidate": (HUMAN, "feat: x\n\nSigned-off-by: " + TOOL_TRAILER + "\n")}),
    (METHOD, "authorship_fields_human_only", "empty allowlist", False, {"candidate": (HUMAN, "feat: x\n"), "allowlist": ""}),
    (METHOD, "commit_author_human", "human author on the allowlist", True, {"candidate": (HUMAN, "feat: x\n")}),
    (METHOD, "commit_author_human", "bot as commit author", False, {"candidate": (("build-bot", "bot@ci.example"), "feat: x\n")}),
    (METHOD, "method_record_well_formed", "well-formed record", True, {"candidate": (HUMAN, "feat: x\n\n" + RECORD + "generated\n")}),
    (METHOD, "method_record_well_formed", "no record, which an authored change may omit", True, {"candidate": (HUMAN, "feat: x\n")}),
    (METHOD, "method_record_well_formed", "class outside the vocabulary", False, {"candidate": (HUMAN, "feat: x\n\n" + RECORD + "assisted\n")}),
    (METHOD, "curated_pins_both_revisions", "curated with both revisions", True, {"candidate": (HUMAN, "feat: x\n\n" + RECORD + "curated\n")}),
    (METHOD, "curated_pins_both_revisions", "curated with no revisions", False, {"candidate": (HUMAN, "feat: x\n\nProduced-With: harness=h; class=curated\n")}),
]
for _skill in (NAV, CITE, READ, CONFAB, METHOD):
    CASES.append((_skill, "priming_active", "rendered prompt contains the block", True, {"prompt": "verbatim"}))
    CASES.append((_skill, "priming_active", "rendered prompt has an altered block", False, {"prompt": "altered"}))


def find_bash() -> str | None:
    """Prefer Git's own bash on Windows; a bare `bash` there can be a different subsystem."""
    if os.name == "nt":
        git = shutil.which("git")
        if git:
            for parent in Path(git).resolve().parents:
                candidate = parent / "bin" / "bash.exe"
                if candidate.exists():
                    return str(candidate)
    return shutil.which("bash")


def load_pack(skill: str) -> dict:
    data = yaml.safe_load((SKILLS / skill / "verifier-pack.yml").read_text(encoding="utf-8"))
    return data.get("verifier_pack", data)


def priming_block(skill: str) -> str:
    text = (SKILLS / skill / "SKILL.md").read_text(encoding="utf-8").replace("\r\n", "\n")
    return text.split("```priming\n", 1)[1].split("```", 1)[0]


class SkillPackChecksTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.bash = find_bash()
        if not cls.bash:
            raise AssertionError("bash is required to execute verifier-pack checks; none was found")
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.tmp = Path(cls.temp_dir.name)
        cls.counter = 0
        cls.packs = {p.parent.name: load_pack(p.parent.name) for p in sorted(SKILLS.glob("*/verifier-pack.yml"))}

    @classmethod
    def tearDownClass(cls) -> None:
        cls.temp_dir.cleanup()

    def fresh(self, suffix: str = "") -> Path:
        type(self).counter += 1
        return self.tmp / f"f{self.counter}{suffix}"

    def write(self, text: str, suffix: str = ".txt") -> str:
        path = self.fresh(suffix)
        path.write_bytes(text.encode("utf-8"))
        return path.as_posix()

    def library(self, files: dict[str, str]) -> str:
        root = self.fresh("-library")
        for rel, text in files.items():
            target = root / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(text.encode("utf-8"))
        return root.as_posix()

    def candidate(self, author: tuple[str, str], message: str) -> str:
        repo = self.fresh("-candidate")
        repo.mkdir()
        hooks = self.fresh("-hooks")
        hooks.mkdir()

        def git(*args: str) -> None:
            subprocess.run(
                ["git", "-C", str(repo), "-c", f"core.hooksPath={hooks.as_posix()}", "-c", "commit.gpgsign=false",
                 "-c", f"user.name={author[0]}", "-c", f"user.email={author[1]}", *args],
                check=True, capture_output=True, text=True,
            )

        git("init", "--quiet")
        (repo / "file.txt").write_text("content\n", encoding="utf-8")
        git("add", "file.txt")
        git("commit", "--quiet", "-m", message)
        return repo.as_posix()

    def environment(self, skill: str, fixture: dict) -> dict[str, str]:
        env = dict(os.environ)
        env["PATH"] = str(Path(sys.executable).parent) + os.pathsep + env.get("PATH", "")
        env["DOCTRINE_ROOT"] = self.library(fixture["library"]) if "library" in fixture else ROOT.as_posix()
        if "report" in fixture:
            env["REPORT"] = self.write(fixture["report"])
        if "declared" in fixture:
            present = self.write("content\n")
            listing = {"ok": present + "\n", "missing": (self.tmp / "absent.txt").as_posix() + "\n", "empty": ""}[fixture["declared"]]
            env["DECLARED_OUTPUTS"] = self.write(listing)
        if "candidate" in fixture:
            env["CANDIDATE"] = self.candidate(*fixture["candidate"])
            env["HUMAN_AUTHOR_ALLOWLIST"] = self.write(fixture.get("allowlist", "Jane Human <jane@example.com>\n"))
        if "prompt" in fixture:
            block = priming_block(skill)
            if fixture["prompt"] == "altered":
                block = block.replace("1.", "1. (edited)", 1)
            env["RENDERED_PROMPT"] = self.write("System prompt.\n\n" + block + "\nEnd.\n")
        return env

    def accepted(self, skill: str, check_id: str, fixture: dict) -> bool:
        verifier = next(v for v in self.packs[skill]["verifiers"] if v["id"] == check_id)
        result = subprocess.run(
            [self.bash, "-c", verifier["command"]],
            env=self.environment(skill, fixture), capture_output=True, text=True,
        )
        ok = result.returncode == verifier.get("expected_exit", 0)
        expected_text = verifier.get("expected_stdout_contains")
        if ok and expected_text:
            ok = expected_text in result.stdout
        return ok

    def test_each_check_accepts_and_rejects_the_right_inputs(self) -> None:
        for skill, check_id, label, should_accept, fixture in CASES:
            with self.subTest(skill=skill, check=check_id, case=label):
                self.assertEqual(self.accepted(skill, check_id, fixture), should_accept)

    def test_every_check_has_an_accepting_and_a_rejecting_fixture(self) -> None:
        covered: dict[tuple[str, str], set[bool]] = {}
        for skill, check_id, _label, should_accept, _fixture in CASES:
            covered.setdefault((skill, check_id), set()).add(should_accept)
        self.assertTrue(self.packs, "no verifier packs were found")
        for skill, pack in self.packs.items():
            for verifier in pack["verifiers"]:
                with self.subTest(skill=skill, check=verifier["id"]):
                    self.assertEqual(covered.get((skill, verifier["id"]), set()), {True, False})

    def test_every_fixture_names_a_real_check(self) -> None:
        known = {(skill, v["id"]) for skill, pack in self.packs.items() for v in pack["verifiers"]}
        for skill, check_id, label, _should_accept, _fixture in CASES:
            with self.subTest(skill=skill, check=check_id, case=label):
                self.assertIn((skill, check_id), known)


if __name__ == "__main__":
    unittest.main()
