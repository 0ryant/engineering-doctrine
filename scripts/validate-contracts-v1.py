#!/usr/bin/env python3
"""
Validation harness for the v1 contract schemas.

Loads each schema, builds in-memory sample instances (matching the worked
examples in doctrine/patterns/run-contracts.md, verifier-packs.md, and the
ADR-0012 model-routing policy), and prints validation results. Run by CI
(.github/workflows/contracts.yml) and during authoring to confirm the
canonical examples remain self-validating. Also loads the on-disk YAML
examples under contracts/examples/ when PyYAML is available, so the shipped
examples are positively asserted, and runs cross-rule consistency checks
(tier reachability) and the interpreter-wrapper-block heuristic regex
behaviour battery.

Dependencies are pinned in requirements.txt at the repo root:
    pip install -r requirements.txt

Scope note: this harness validates contract SHAPE and intra-policy
consistency. It does NOT check on-disk sibling existence (skill <-> verifier
-pack); that gate, if any, lives in external catalog tooling.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

# Self-proving content-pin for the anti-confabulation priming block. Importing
# verify_primer_pin keeps PRIMER_SHA256 below honest: the pin recomputes the
# hash from the in-repo block and asserts every on-disk copy agrees.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import importlib

_primer_pin = importlib.import_module("verify-primer-pin")

try:
    import yaml  # type: ignore
    _HAVE_YAML = True
except ImportError:  # pragma: no cover - yaml is a soft dependency
    _HAVE_YAML = False

ROOT = Path(__file__).resolve().parents[1]
RUN_SCHEMA = ROOT / "contracts" / "run-contract.v1.schema.json"
VP_SCHEMA = ROOT / "contracts" / "verifier-pack.v1.schema.json"
RP_SCHEMA = ROOT / "contracts" / "router-policy.v1.schema.json"
EXAMPLES_DIR = ROOT / "contracts" / "examples"

PRIMER_SHA256 = "c138dd966c82f7bd792684ab3fef0f50d75aa9342468db8b5d265f24f3fb35a8"
# Guard: this literal MUST equal the pin's source-of-truth. verify-primer-pin
# also re-asserts this from the other direction (reading this file), so a drift
# fails CI whichever script runs first.
assert PRIMER_SHA256 == _primer_pin.PRIMER_SHA256, (
    "PRIMER_SHA256 here has drifted from scripts/verify-primer-pin.py"
)


def load(p: Path) -> dict:
    return json.loads(p.read_text(encoding="utf-8"))


def pr_evidence_build_review() -> dict:
    return {
        "name": "pr-evidence-build-review",
        "schema_version": "1.0.0",
        "description": "On every PR to example-org/pr-evidence: build the evidence pack, then have an LLM review it.",
        "trigger": {
            "type": "repo_event",
            "repo": "example-org/pr-evidence",
            "events": ["pull_request_opened", "pull_request_synchronize"],
        },
        "model_policy": {
            "allowed_models": ["opus", "sonnet"],
            "disallow_models": ["haiku"],
            "fallback": "fail",
        },
        "context": {
            "skills": ["pr-evidence-mcp", "cargo-build-and-test"],
            "memory": {"mode": "verified_only", "max_items": 32, "ceiling": "RemoteSigned"},
        },
        "capabilities": {
            "tools": [
                "pr-evidence.collect",
                "pr-evidence.verify",
                "cargo.build",
                "cargo.test",
                "tapprove.claim_audit",
            ]
        },
        "authority": {
            "filesystem": {
                "root": "/work/pr-evidence",
                "writable": ["target/", "out/", "audit/"],
                "readable": ["src/", "Cargo.toml", "Cargo.lock"],
            },
            "env": {"inherit": False, "allow": ["PATH", "RUSTUP_HOME", "CARGO_HOME"]},
            "network": {"mode": "deny"},
            "subprocess": {
                "allowed": [
                    "/usr/bin/cargo",
                    "/usr/bin/git",
                    "/usr/local/bin/pr-evidence",
                ]
            },
        },
        "hooks": {
            "before_tool_use": ["log-tool-id", "deny-out-of-scope-tools"],
            "after_tool_use": ["record-output-hash"],
            "before_final_answer": ["enforce-outputs-required-exists"],
            "on_stop": ["close-audit-log", "emit-cortex-receipt"],
        },
        "verifiers": [
            "pr-evidence-mcp-verifier-pack",
            "cargo-build-and-test-verifier-pack",
            "tapprove-claim-audit-meta-pack",
        ],
        "outputs": {
            "required": [
                "out/pack.json",
                "audit/run.jsonl",
                "target/release/pr-evidence",
            ],
            "optional": ["target/criterion/**"],
            "audit": {"jsonl_path": "audit/run.jsonl", "content_addressable": True},
        },
    }


def nightly_audit() -> dict:
    return {
        "name": "nightly-pr-evidence-audit",
        "schema_version": "1.0.0",
        "description": "Nightly at 02:00 UTC: re-verify every recent pr-evidence pack still validates and emit a cohort-health summary.",
        "trigger": {
            "type": "cron",
            "schedule": "0 2 * * *",
            "timezone": "UTC",
            "jitter_seconds": 600,
        },
        "model_policy": {
            "allowed_models": ["sonnet"],
            "disallow_models": ["haiku"],
            "fallback": "fail",
        },
        "context": {
            "skills": ["pr-evidence-mcp"],
            "memory": {"mode": "verified_only", "max_items": 16, "ceiling": "RemoteSigned"},
        },
        "capabilities": {"tools": ["pr-evidence.verify", "tapprove.claim_audit"]},
        "authority": {
            "filesystem": {"root": "/work/nightly-audit", "writable": ["out/", "audit/"]},
            "env": {"inherit": False, "allow": ["PATH"]},
            "network": {"mode": "deny"},
            "subprocess": {"allowed": ["/usr/local/bin/pr-evidence"]},
        },
        "hooks": {
            "before_run": ["acquire-nightly-lock"],
            "after_run": ["release-nightly-lock"],
            "on_stop": ["close-audit-log", "emit-cortex-receipt"],
        },
        "verifiers": [
            "pr-evidence-mcp-verifier-pack",
            "cohort-health-summary-pack",
        ],
        "outputs": {
            "required": ["out/summary.json", "audit/run.jsonl"],
            "audit": {"jsonl_path": "audit/run.jsonl", "content_addressable": True},
        },
    }


def pr_evidence_verifier_pack() -> dict:
    return {
        "name": "pr-evidence-mcp-verifier-pack",
        "skill": "pr-evidence-mcp",
        "version": "1.0.0",
        "schema_version": "1.0.0",
        "description": "Verify pr-evidence-mcp produces a complete, tamper-resistant evidence pack with bounded authority.",
        "setup": [
            "mkdir -p ${OUTPUT_DIR} ${SCRATCH}",
            "pr-evidence collect --out ${OUTPUT_DIR}/pack.json --audit ${AUDIT_LOG}",
        ],
        "teardown": ["rm -rf ${SCRATCH}"],
        "verifiers": [
            {
                "id": "cli_writes_declared_output",
                "kind": "cli_writes_declared_output",
                "description": "pr-evidence collect writes a non-empty pack.json at the declared output path",
                "command": "test -s ${OUTPUT_DIR}/pack.json",
                "expected_exit": 0,
                "expected_stdout_contains": None,
                "expected_stderr_contains": None,
                "expected_artefacts": ["${OUTPUT_DIR}/pack.json"],
                "failure_mode": "fail_loud",
                "severity": "fatal",
            },
            {
                "id": "verify_succeeds_on_valid_pack",
                "kind": "verify_succeeds_on_valid_input",
                "description": "pr-evidence verify exits 0 on a freshly-collected pack",
                "command": "pr-evidence verify ${OUTPUT_DIR}/pack.json",
                "expected_exit": 0,
                "expected_stdout_contains": "ok",
                "expected_stderr_contains": None,
                "expected_artefacts": [],
                "failure_mode": "fail_loud",
                "severity": "fatal",
                "preconditions": ["cli_writes_declared_output"],
            },
            {
                "id": "tamper_verify_fails",
                "kind": "tamper_verify_fails",
                "description": "modifying the pack invalidates verify",
                "command": "tamper-and-reverify ${OUTPUT_DIR}/pack.json",
                "expected_exit": 0,
                "expected_stdout_contains": None,
                "expected_stderr_contains": None,
                "expected_artefacts": [],
                "failure_mode": "fail_loud",
                "severity": "fatal",
                "preconditions": ["verify_succeeds_on_valid_pack"],
            },
            {
                "id": "missing_input_fails",
                "kind": "missing_input_fails",
                "description": "pr-evidence verify on a non-existent path exits non-zero",
                "command": "expect-nonzero pr-evidence verify /nonexistent/path",
                "expected_exit": 0,
                "expected_stdout_contains": None,
                "expected_stderr_contains": None,
                "expected_artefacts": [],
                "failure_mode": "fail_loud",
                "severity": "fatal",
            },
            {
                "id": "env_canary_not_in_subprocess",
                "kind": "env_canary_not_in_subprocess",
                "description": "a canary env var set at the parent does not propagate to the spawned CLI",
                "command": "canary-check pr-evidence collect --print-env",
                "expected_exit": 0,
                "expected_stdout_contains": None,
                "expected_stderr_contains": None,
                "expected_artefacts": [],
                "failure_mode": "fail_loud",
                "severity": "fatal",
            },
            {
                "id": "symlink_escape_rejected",
                "kind": "symlink_escape_rejected",
                "description": "collecting through a symlink that escapes the declared root is rejected",
                "command": "symlink-escape-check ${SCRATCH} ${OUTPUT_DIR}",
                "expected_exit": 0,
                "expected_stdout_contains": None,
                "expected_stderr_contains": None,
                "expected_artefacts": [],
                "failure_mode": "fail_loud",
                "severity": "fatal",
            },
            {
                "id": "output_cap_enforced",
                "kind": "output_cap_enforced",
                "description": "outputs larger than the declared cap are rejected, not silently truncated",
                "command": "size-cap-check ${OUTPUT_DIR}/pack.json ${OUTPUT_CAP_BYTES}",
                "expected_exit": 0,
                "expected_stdout_contains": None,
                "expected_stderr_contains": None,
                "expected_artefacts": [],
                "failure_mode": "mark_untrusted",
                "severity": "error",
            },
            {
                "id": "jsonl_audit_event_emitted",
                "kind": "jsonl_audit_event_emitted",
                "description": "exactly one well-formed JSONL audit event lands per CLI invocation",
                "command": "jsonl-singleton-check ${AUDIT_LOG}",
                "expected_exit": 0,
                "expected_stdout_contains": None,
                "expected_stderr_contains": None,
                "expected_artefacts": ["${AUDIT_LOG}"],
                "failure_mode": "fail_loud",
                "severity": "fatal",
            },
            {
                "id": "lockfile_generated",
                "kind": "lockfile_generated",
                "description": "regenerating the MCP server produces an mcpact.lock matching the running tool fingerprint",
                "command": "mcpact verify-lock ${MCPACT_OUT}/mcpact.lock",
                "expected_exit": 0,
                "expected_stdout_contains": "ok",
                "expected_stderr_contains": None,
                "expected_artefacts": ["${MCPACT_OUT}/mcpact.lock"],
                "failure_mode": "mark_untrusted",
                "severity": "error",
            },
            {
                "id": "host_registrations_generated",
                "kind": "host_registrations_generated",
                "description": "pr-evidence-mcp generates Claude/Cursor/Codex host registration files that validate against their schemas",
                "command": "host-registration-check ${MCPACT_OUT}/host",
                "expected_exit": 0,
                "expected_stdout_contains": None,
                "expected_stderr_contains": None,
                "expected_artefacts": [
                    "${MCPACT_OUT}/host/claude.json",
                    "${MCPACT_OUT}/host/cursor.json",
                    "${MCPACT_OUT}/host/codex.json",
                ],
                "failure_mode": "mark_untrusted",
                "severity": "error",
            },
        ],
    }


def default_production_router_policy() -> dict:
    """In-memory mirror of contracts/examples/default-production.router-policy.yaml.

    Encodes the council-D4 3-tier policy structurally: premium / default /
    narrow_scope, with the narrow_scope haiku tier behind mandatory external
    review at sample rate 1.0.
    """
    return {
        "$schema": "https://engineering-doctrine/contracts/router-policy.v1.schema.json",
        "policy_version": "1.0.0",
        "schema_version": "1.0.0",
        "description": "v3 production default -- 3-tier policy (premium/default/narrow_scope).",
        "tiers": {
            "premium": {
                "model": "claude-opus-4-7",
                "model_family": "opus_4_x",
                "primer": "anti-confab-200tok@1.0.0",
                "primer_sha256": PRIMER_SHA256,
                "verifier_pack": "pr-evidence-mcp-verifier-pack@1.0.0",
                "cell_classes": [
                    "security_critical",
                    "supervisor_change",
                    "doctrine_promotion",
                ],
                "max_cost_usd_per_cell": 10.00,
                "external_review_required": False,
            },
            "default": {
                "model": "claude-sonnet-4-6",
                "model_family": "sonnet_4_x",
                "primer": "anti-confab-200tok@1.0.0",
                "primer_sha256": PRIMER_SHA256,
                "verifier_pack": "pr-evidence-mcp-verifier-pack@1.0.0",
                "cell_classes": [
                    "greenfield_backbone",
                    "refactor_class",
                    "audit_class",
                    "build_class",
                    "artifact_production",
                    "research_class",
                ],
                "max_cost_usd_per_cell": 2.00,
                "external_review_required": False,
            },
            "narrow_scope": {
                "model": "claude-haiku-4-5-20251001",
                "model_family": "haiku_4_x",
                "primer": "anti-confab-200tok@1.0.0",
                "primer_sha256": PRIMER_SHA256,
                "verifier_pack": "pr-evidence-mcp-verifier-pack@1.0.0",
                "cell_classes": ["scaffolded_typed_authority"],
                "max_cost_usd_per_cell": 0.50,
                "external_review_required": True,
                "external_review_sample_rate": 1.0,
            },
        },
        "escalation_rules": [
            {
                "rule_id": "claim-audit-falsified-escalate",
                "when": {"claim_audit_verdict": "FALSIFIED", "attempts_so_far": 1},
                "action": {
                    "escalate_to_tier": "premium",
                    "add_primer": "anti-confab-200tok@1.0.0",
                    "max_cost_usd": 5.00,
                },
                "evidence_ref": "value-sheet/18-cross-product-test/v3/results/plan-b-v2-claim-audit-against-stage2/composite.md",
            },
            {
                "rule_id": "security-critical-premium-only",
                "when": {
                    "cell_class": [
                        "security_critical",
                        "supervisor_change",
                        "doctrine_promotion",
                    ]
                },
                "action": {"require_tier": "premium"},
                "evidence_ref": "value-sheet/18-cross-product-test/v2/results/test-1-backbone/canonical-scoring-opus.md",
            },
        ],
        "refusal_rules": [
            {
                "rule_id": "haiku-no-artifact-production-without-primer",
                "when": {
                    "model_family": "haiku_4_x",
                    "cell_class": "artifact_production",
                    "primer": None,
                },
                "action": {
                    "refuse_routing": True,
                    "reason": "Empirical: tools-haiku+SKILLS canonical 31 (v2 Stage 2 smoking gun).",
                },
                "evidence_ref": "value-sheet/18-cross-product-test/v2/results/test-1-backbone/canonical-scoring.md",
            },
            {
                "rule_id": "haiku-no-greenfield",
                "when": {
                    "model_family": "haiku_4_x",
                    "cell_class": "greenfield_backbone",
                },
                "action": {
                    "refuse_routing": True,
                    "reason": "Haiku-PRIMED canonical 73 < Sonnet 85; +10 self-canonical means cell cannot detect over-claims on greenfield.",
                },
                "evidence_ref": "value-sheet/18-cross-product-test/v2/results/test-1-backbone/canonical-scoring-haiku-primed.md",
            },
            {
                "rule_id": "haiku-narrow-scope-requires-external-review",
                "when": {
                    "cell_class": "scaffolded_typed_authority",
                    "model_family": "haiku_4_x",
                },
                "action": {
                    "require_external_review": True,
                    "reason": "+10 self-canonical on Haiku-PRIMED; production use requires external scoring.",
                },
                "evidence_ref": "value-sheet/18-cross-product-test/v2/results/test-1-backbone/canonical-scoring-haiku-primed.md",
            },
            {
                "rule_id": "interpreter-wrapper-block",
                "when": {
                    "command_matches": (
                        r"(?:^|[\s/])(?:env\s+|nohup\s+|xargs\s+)?"
                        r"(?:bash|sh|zsh|ash|dash|powershell|pwsh|cmd)(?:\.exe)?"
                        r"\s+(?:-[a-z]*c[a-z]*\b|--?c[a-z]*\b)"
                    )
                },
                "action": {
                    "refuse_routing": True,
                    "reason": "CC-2 FALSIFIED at corpus scale; best-effort defense-in-depth lint at router layer (corcept is authoritative).",
                },
                "evidence_ref": "value-sheet/18-cross-product-test/v2/results/per-tool-failure-mode-tests-results/composite.md",
            },
            {
                "rule_id": "primer-required-on-build-class",
                "when": {
                    "cell_class": ["build_class", "artifact_production", "refactor_class"],
                    "primer": None,
                },
                "action": {
                    "refuse_routing": True,
                    "reason": "Build-class cells must run with canonical primer for measurement-grade honesty (v2 evidence).",
                },
                "evidence_ref": "value-sheet/18-cross-product-test/v2/results/test-1-backbone/canonical-scoring.md",
            },
        ],
        "cost_ceilings": {
            "per_cell": {
                "premium_max_usd": 10.00,
                "default_max_usd": 2.00,
                "narrow_scope_max_usd": 0.50,
            },
            "per_session": {
                "operator_warning_at_usd": 20.00,
                "operator_kill_at_usd": 100.00,
            },
        },
        "audit": {"jsonl_path": "audit/router.jsonl", "content_addressable": True},
    }


def _as_list(v) -> list:
    return v if isinstance(v, list) else [v]


def refusal_kills_tier_inputs(policy: dict) -> list[str]:
    """Cross-rule consistency check (catches the enterprise-strict bug class).

    A tier always routes runs that carry the tier's model_family, the tier's
    (non-null) primer, and one of the tier's cell_classes. If a refusal rule
    matches such a route, the tier is structurally unreachable -- a
    contradiction the per-rule JSON-schema validation cannot detect because
    each rule is individually valid.

    Returns a list of human-readable violation strings (empty == consistent).
    Only refusal rules with a `refuse_routing` action can make a tier dead;
    `require_external_review` is a gate, not a denial, so it is excluded.
    Refusal shapes keyed on `primer: null` (unprimed routes) and on
    `command_matches` (runtime argv, not a tier input) never apply to a
    primed tier route and are likewise skipped.
    """
    violations: list[str] = []
    refusals = [
        r for r in policy.get("refusal_rules", [])
        if r.get("action", {}).get("refuse_routing") is True
    ]
    for tier_name, tier in policy.get("tiers", {}).items():
        family = tier.get("model_family")
        primer = tier.get("primer")
        for cell_class in tier.get("cell_classes", []):
            for rule in refusals:
                when = rule.get("when", {})
                if "command_matches" in when:
                    continue
                if "primer" in when and when["primer"] is None:
                    continue  # only fires on unprimed routes; tiers are primed
                # Evaluate the remaining (model_family / cell_class / primer) keys.
                if "model_family" in when and when["model_family"] != family:
                    continue
                if "cell_class" in when and cell_class not in _as_list(when["cell_class"]):
                    continue
                if "primer" in when and when["primer"] != primer:
                    continue
                violations.append(
                    f"tier '{tier_name}' (family={family}, primer={primer}, "
                    f"cell_class={cell_class}) is denied by refusal rule "
                    f"'{rule.get('rule_id')}' -- tier is unreachable"
                )
    return violations


def main() -> int:
    run_schema = load(RUN_SCHEMA)
    vp_schema = load(VP_SCHEMA)
    rp_schema = load(RP_SCHEMA)
    Draft202012Validator.check_schema(run_schema)
    Draft202012Validator.check_schema(vp_schema)
    Draft202012Validator.check_schema(rp_schema)
    rv = Draft202012Validator(run_schema)
    vv = Draft202012Validator(vp_schema)
    pv = Draft202012Validator(rp_schema)

    failures = 0

    # Content-pin: prove PRIMER_SHA256 actually matches the in-repo priming
    # block (recomputed) before any tier asserts it. This turns the central
    # integrity claim from asserted text into a checked invariant.
    pin_failures = _primer_pin.verify()
    if pin_failures:
        failures += 1
        print(f"primer-pin: {len(pin_failures)} drift(s)")
        for f in pin_failures:
            print(f"  - {f}")
    else:
        print(f"primer-pin: VALID (sha256={PRIMER_SHA256})")

    cases = [
        ("pr-evidence-build-review", rv, pr_evidence_build_review()),
        ("nightly-pr-evidence-audit", rv, nightly_audit()),
        ("pr-evidence-mcp-verifier-pack", vv, pr_evidence_verifier_pack()),
        ("default-production-router-policy", pv, default_production_router_policy()),
    ]
    for label, validator, instance in cases:
        errs = sorted(validator.iter_errors(instance), key=lambda e: list(e.absolute_path))
        if errs:
            failures += 1
            print(f"{label}: {len(errs)} validation errors")
            for e in errs[:5]:
                print(f"  - {list(e.absolute_path)}: {e.message}")
        else:
            print(f"{label}: VALID")

    # Negative: unknown top-level field is rejected.
    bad = dict(pr_evidence_build_review())
    bad["surprise_field"] = "should reject"
    errs = list(rv.iter_errors(bad))
    if not errs:
        failures += 1
        print("negative-unknown-field: FAILED to reject unknown field")
    else:
        print(f"negative-unknown-field: rejected as expected ({len(errs)} error)")

    # Negative: empty outputs.required is rejected.
    bad2 = dict(pr_evidence_build_review())
    bad2["outputs"] = {**bad2["outputs"], "required": []}
    errs = list(rv.iter_errors(bad2))
    if not errs:
        failures += 1
        print("negative-empty-required: FAILED to reject empty outputs.required")
    else:
        print(f"negative-empty-required: rejected as expected ({len(errs)} error)")

    # Negative: network allow_list mode without allow_list array.
    bad3 = dict(pr_evidence_build_review())
    bad3["authority"] = {**bad3["authority"], "network": {"mode": "allow_list"}}
    errs = list(rv.iter_errors(bad3))
    if not errs:
        failures += 1
        print("negative-network-missing-list: FAILED to reject allow_list without list")
    else:
        print(f"negative-network-missing-list: rejected as expected ({len(errs)} error)")

    # On-disk YAML examples -- positive cases. Only run if PyYAML is installed
    # so the harness still works in lean environments.
    if _HAVE_YAML and EXAMPLES_DIR.exists():
        for yaml_path in sorted(EXAMPLES_DIR.glob("*.router-policy.yaml")):
            label = yaml_path.name
            doc = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
            errs = sorted(pv.iter_errors(doc), key=lambda e: list(e.absolute_path))
            if errs:
                failures += 1
                print(f"{label}: {len(errs)} validation errors")
                for e in errs[:5]:
                    print(f"  - {list(e.absolute_path)}: {e.message}")
            else:
                print(f"{label}: VALID")
            # Cross-rule consistency: no tier may be denied by a refusal rule.
            tier_violations = refusal_kills_tier_inputs(doc)
            if tier_violations:
                failures += 1
                print(f"{label}: {len(tier_violations)} tier-reachability violation(s)")
                for v in tier_violations[:5]:
                    print(f"  - {v}")
            else:
                print(f"{label}: tier-reachability OK")
    else:
        print("(skipping on-disk YAML examples; PyYAML not installed)")

    # --- Router-policy negative cases ---

    # Negative: refusal_rules empty array is rejected (loud-not-silent).
    rp_bad1 = default_production_router_policy()
    rp_bad1 = {**rp_bad1, "refusal_rules": []}
    errs = list(pv.iter_errors(rp_bad1))
    if not errs:
        failures += 1
        print("router-negative-empty-refusals: FAILED to reject empty refusal_rules")
    else:
        print(f"router-negative-empty-refusals: rejected as expected ({len(errs)} error)")

    # Negative: refusal rule missing evidence_ref is rejected.
    rp_bad2 = default_production_router_policy()
    bad_refusal = dict(rp_bad2["refusal_rules"][0])
    bad_refusal.pop("evidence_ref")
    rp_bad2 = {**rp_bad2, "refusal_rules": [bad_refusal] + rp_bad2["refusal_rules"][1:]}
    errs = list(pv.iter_errors(rp_bad2))
    if not errs:
        failures += 1
        print("router-negative-missing-evidence: FAILED to reject refusal without evidence_ref")
    else:
        print(f"router-negative-missing-evidence: rejected as expected ({len(errs)} error)")

    # Negative: refusal_action.refuse_routing == false is rejected.
    rp_bad3 = default_production_router_policy()
    soft_refusal = dict(rp_bad3["refusal_rules"][3])  # interpreter-wrapper-block uses refuse_routing
    soft_refusal["action"] = {"refuse_routing": False, "reason": "soft refusal -- illegal"}
    new_rules = list(rp_bad3["refusal_rules"])
    new_rules[3] = soft_refusal
    rp_bad3 = {**rp_bad3, "refusal_rules": new_rules}
    errs = list(pv.iter_errors(rp_bad3))
    if not errs:
        failures += 1
        print("router-negative-soft-refusal: FAILED to reject refuse_routing=false")
    else:
        print(f"router-negative-soft-refusal: rejected as expected ({len(errs)} error)")

    # Negative: refusal_when mixes two discriminator shapes (oneOf violation).
    rp_bad4 = default_production_router_policy()
    mixed_when = dict(rp_bad4["refusal_rules"][0])
    mixed_when["when"] = {
        "cell_class": "artifact_production",
        "model_family": "haiku_4_x",
        "command_matches": "^bash",
    }
    new_rules = list(rp_bad4["refusal_rules"])
    new_rules[0] = mixed_when
    rp_bad4 = {**rp_bad4, "refusal_rules": new_rules}
    errs = list(pv.iter_errors(rp_bad4))
    if not errs:
        failures += 1
        print("router-negative-mixed-when: FAILED to reject mixed refusal_when discriminators")
    else:
        print(f"router-negative-mixed-when: rejected as expected ({len(errs)} error)")

    # Negative: unknown top-level field on router policy is rejected.
    rp_bad5 = default_production_router_policy()
    rp_bad5["random_extra"] = "nope"
    errs = list(pv.iter_errors(rp_bad5))
    if not errs:
        failures += 1
        print("router-negative-unknown-field: FAILED to reject unknown top-level field")
    else:
        print(f"router-negative-unknown-field: rejected as expected ({len(errs)} error)")

    # Negative: invalid cell_class enum value is rejected.
    rp_bad6 = default_production_router_policy()
    bad_class = dict(rp_bad6["refusal_rules"][1])  # haiku-no-greenfield uses (model_family + cell_class)
    bad_class["when"] = {
        "cell_class": "completely_made_up_class",
        "model_family": "haiku_4_x",
    }
    new_rules = list(rp_bad6["refusal_rules"])
    new_rules[1] = bad_class
    rp_bad6 = {**rp_bad6, "refusal_rules": new_rules}
    errs = list(pv.iter_errors(rp_bad6))
    if not errs:
        failures += 1
        print("router-negative-bad-cell-class: FAILED to reject unknown cell_class")
    else:
        print(f"router-negative-bad-cell-class: rejected as expected ({len(errs)} error)")

    # Negative: tiers missing the narrow_scope key is rejected
    # (the 3-tier structure is required).
    rp_bad7 = default_production_router_policy()
    rp_bad7 = {**rp_bad7, "tiers": {k: v for k, v in rp_bad7["tiers"].items() if k != "narrow_scope"}}
    errs = list(pv.iter_errors(rp_bad7))
    if not errs:
        failures += 1
        print("router-negative-missing-tier: FAILED to reject tiers missing narrow_scope")
    else:
        print(f"router-negative-missing-tier: rejected as expected ({len(errs)} error)")

    # Negative: tier missing primer_sha256 is rejected (council D5 hash pin).
    rp_bad8 = default_production_router_policy()
    bad_tier = dict(rp_bad8["tiers"]["default"])
    bad_tier.pop("primer_sha256")
    rp_bad8 = {**rp_bad8, "tiers": {**rp_bad8["tiers"], "default": bad_tier}}
    errs = list(pv.iter_errors(rp_bad8))
    if not errs:
        failures += 1
        print("router-negative-missing-primer-sha: FAILED to reject tier without primer_sha256")
    else:
        print(f"router-negative-missing-primer-sha: rejected as expected ({len(errs)} error)")

    # Negative: tier missing external_review_required is rejected.
    rp_bad9 = default_production_router_policy()
    bad_tier = dict(rp_bad9["tiers"]["narrow_scope"])
    bad_tier.pop("external_review_required")
    rp_bad9 = {**rp_bad9, "tiers": {**rp_bad9["tiers"], "narrow_scope": bad_tier}}
    errs = list(pv.iter_errors(rp_bad9))
    if not errs:
        failures += 1
        print("router-negative-missing-external-review: FAILED to reject tier without external_review_required")
    else:
        print(f"router-negative-missing-external-review: rejected as expected ({len(errs)} error)")

    # Negative: escalation action mixing escalate_to_tier and require_tier is rejected.
    rp_bad10 = default_production_router_policy()
    bad_esc = dict(rp_bad10["escalation_rules"][0])
    bad_esc["action"] = {
        "escalate_to_tier": "premium",
        "require_tier": "premium",
        "max_cost_usd": 5.00,
    }
    new_esc = list(rp_bad10["escalation_rules"])
    new_esc[0] = bad_esc
    rp_bad10 = {**rp_bad10, "escalation_rules": new_esc}
    errs = list(pv.iter_errors(rp_bad10))
    if not errs:
        failures += 1
        print("router-negative-mixed-escalation-action: FAILED to reject mixed escalation action discriminators")
    else:
        print(f"router-negative-mixed-escalation-action: rejected as expected ({len(errs)} error)")

    # Negative: invalid primer_sha256 (non-hex / wrong length) is rejected.
    rp_bad11 = default_production_router_policy()
    bad_tier = dict(rp_bad11["tiers"]["default"])
    bad_tier["primer_sha256"] = "not-a-real-sha"
    rp_bad11 = {**rp_bad11, "tiers": {**rp_bad11["tiers"], "default": bad_tier}}
    errs = list(pv.iter_errors(rp_bad11))
    if not errs:
        failures += 1
        print("router-negative-bad-primer-sha: FAILED to reject malformed primer_sha256")
    else:
        print(f"router-negative-bad-primer-sha: rejected as expected ({len(errs)} error)")

    # Negative: invalid tier_name in escalate_to_tier is rejected.
    rp_bad12 = default_production_router_policy()
    bad_esc = dict(rp_bad12["escalation_rules"][0])
    bad_esc["action"] = {
        "escalate_to_tier": "ultraplatinum",  # not a valid tier_name
        "max_cost_usd": 5.00,
    }
    new_esc = list(rp_bad12["escalation_rules"])
    new_esc[0] = bad_esc
    rp_bad12 = {**rp_bad12, "escalation_rules": new_esc}
    errs = list(pv.iter_errors(rp_bad12))
    if not errs:
        failures += 1
        print("router-negative-bad-tier-name: FAILED to reject invalid tier_name")
    else:
        print(f"router-negative-bad-tier-name: rejected as expected ({len(errs)} error)")

    # --- cross-rule tier-reachability consistency ---
    # Positive: the in-memory canonical policy keeps every tier reachable.
    pos_violations = refusal_kills_tier_inputs(default_production_router_policy())
    if pos_violations:
        failures += 1
        print(f"router-tier-reachability: FAILED ({pos_violations})")
    else:
        print("router-tier-reachability: OK (all tiers reachable)")

    # Negative: re-introduce the enterprise-strict bug (a family+primer refusal
    # that matches the narrow_scope tier inputs) and confirm the check fires.
    rp_dead = default_production_router_policy()
    rp_dead = {
        **rp_dead,
        "refusal_rules": rp_dead["refusal_rules"] + [
            {
                "rule_id": "haiku-primer-unbundled",
                "when": {
                    "model_family": "haiku_4_x",
                    "primer": "anti-confab-200tok@1.0.0",
                },
                "action": {"refuse_routing": True, "reason": "kills narrow_scope"},
                "evidence_ref": "doctrine/skills/anti-confabulation.skill.md",
            }
        ],
    }
    if not refusal_kills_tier_inputs(rp_dead):
        failures += 1
        print("router-negative-dead-tier: FAILED to detect unreachable tier")
    else:
        print("router-negative-dead-tier: detected as expected")

    # --- interpreter-wrapper-block heuristic regex behaviour ---
    #
    # This control is documented as a BEST-EFFORT heuristic lint (corcept is
    # the authoritative interpreter-bypass guard), but it must still catch the
    # common non-naive spellings of `<shell> -c` rather than only the bare
    # `bash -c` literal. The pattern is matched case-insensitively by the
    # consumer (router-policy schema, command_matches description).
    policy = default_production_router_policy()
    iwb = next(
        r for r in policy["refusal_rules"]
        if r["rule_id"] == "interpreter-wrapper-block"
    )
    iwb_re = re.compile(iwb["when"]["command_matches"], re.IGNORECASE)
    must_match = [
        "bash -c",
        "/bin/bash -c",
        "./bash -c",
        "env bash -c",
        "xargs sh -c",
        "nohup bash -c",
        "BASH -c",
        "bash -lc",
        "bash -ic",
        "bash --command",
        " bash -c",
        "powershell -Command",
        "pwsh.exe -Command",
    ]
    must_not_match = [
        "cargo build",
        "git status",
        "/usr/bin/cargo test",
        "echo bashful",
        "bash script.sh",
        "sh -n file",
    ]
    missed = [c for c in must_match if not iwb_re.search(c)]
    falsepos = [c for c in must_not_match if iwb_re.search(c)]
    if missed or falsepos:
        failures += 1
        print(
            "interpreter-wrapper-block-regex: FAILED "
            f"(bypassed: {missed}; false-positive: {falsepos})"
        )
    else:
        print(
            "interpreter-wrapper-block-regex: OK "
            f"({len(must_match)} bypass spellings caught, "
            f"{len(must_not_match)} benign commands ignored)"
        )

    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
