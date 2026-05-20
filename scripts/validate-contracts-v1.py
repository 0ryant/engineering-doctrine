#!/usr/bin/env python3
"""
Validation harness for the v1 contract schemas.

Loads each schema, builds in-memory sample instances (matching the worked
examples in doctrine/patterns/run-contracts.md, verifier-packs.md, and the
ADR-0012 model-routing policy), and prints validation results. Used by CI
and during authoring to confirm the canonical examples remain self-
validating. Also loads the on-disk YAML examples under contracts/examples/
when PyYAML is available, so the shipped examples are positively asserted.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

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


def load(p: Path) -> dict:
    return json.loads(p.read_text(encoding="utf-8"))


def pr_evidence_build_review() -> dict:
    return {
        "name": "evidence-pack-build-review",
        "schema_version": "1.0.0",
        "description": "On every PR to agent-authority-framework/evidence-pack: build the evidence pack, then have an LLM review it.",
        "trigger": {
            "type": "repo_event",
            "repo": "agent-authority-framework/evidence-pack",
            "events": ["pull_request_opened", "pull_request_synchronize"],
        },
        "model_policy": {
            "allowed_models": ["model-high-capability", "model-balanced"],
            "disallow_models": ["narrow-scope model"],
            "fallback": "fail",
        },
        "context": {
            "skills": ["evidence-pack-mcp", "cargo-build-and-test"],
            "memory": {"mode": "verified_only", "max_items": 32, "ceiling": "RemoteSigned"},
        },
        "capabilities": {
            "tools": [
                "evidence-pack.collect",
                "evidence-pack.verify",
                "cargo.build",
                "cargo.test",
                "review.claim_audit",
            ]
        },
        "authority": {
            "filesystem": {
                "root": "/work/evidence-pack",
                "writable": ["target/", "out/", "audit/"],
                "readable": ["src/", "Cargo.toml", "Cargo.lock"],
            },
            "env": {"inherit": False, "allow": ["PATH", "RUSTUP_HOME", "CARGO_HOME"]},
            "network": {"mode": "deny"},
            "subprocess": {
                "allowed": [
                    "/usr/bin/cargo",
                    "/usr/bin/git",
                    "/usr/local/bin/evidence-pack",
                ]
            },
        },
        "hooks": {
            "before_tool_use": ["log-tool-id", "deny-out-of-scope-tools"],
            "after_tool_use": ["record-output-hash"],
            "before_final_answer": ["enforce-outputs-required-exists"],
            "on_stop": ["close-audit-log", "emit-run-receipt"],
        },
        "verifiers": [
            "evidence-pack-mcp-verifier-pack",
            "cargo-build-and-test-verifier-pack",
            "review-claim-audit-meta-pack",
        ],
        "outputs": {
            "required": [
                "out/pack.json",
                "audit/run.jsonl",
                "target/release/evidence-pack",
            ],
            "optional": ["target/criterion/**"],
            "audit": {"jsonl_path": "audit/run.jsonl", "content_addressable": True},
        },
    }


def nightly_audit() -> dict:
    return {
        "name": "nightly-evidence-pack-audit",
        "schema_version": "1.0.0",
        "description": "Nightly at 02:00 UTC: re-verify every recent evidence-pack pack still validates and emit a cohort-health summary.",
        "trigger": {
            "type": "cron",
            "schedule": "0 2 * * *",
            "timezone": "UTC",
            "jitter_seconds": 600,
        },
        "model_policy": {
            "allowed_models": ["model-balanced"],
            "disallow_models": ["narrow-scope model"],
            "fallback": "fail",
        },
        "context": {
            "skills": ["evidence-pack-mcp"],
            "memory": {"mode": "verified_only", "max_items": 16, "ceiling": "RemoteSigned"},
        },
        "capabilities": {"tools": ["evidence-pack.verify", "review.claim_audit"]},
        "authority": {
            "filesystem": {"root": "/work/nightly-audit", "writable": ["out/", "audit/"]},
            "env": {"inherit": False, "allow": ["PATH"]},
            "network": {"mode": "deny"},
            "subprocess": {"allowed": ["/usr/local/bin/evidence-pack"]},
        },
        "hooks": {
            "before_run": ["acquire-nightly-lock"],
            "after_run": ["release-nightly-lock"],
            "on_stop": ["close-audit-log", "emit-run-receipt"],
        },
        "verifiers": [
            "evidence-pack-mcp-verifier-pack",
            "cohort-health-summary-pack",
        ],
        "outputs": {
            "required": ["out/summary.json", "audit/run.jsonl"],
            "audit": {"jsonl_path": "audit/run.jsonl", "content_addressable": True},
        },
    }


def pr_evidence_verifier_pack() -> dict:
    return {
        "name": "evidence-pack-mcp-verifier-pack",
        "skill": "evidence-pack-mcp",
        "version": "1.0.0",
        "schema_version": "1.0.0",
        "description": "Verify evidence-pack-mcp produces a complete, tamper-resistant evidence pack with bounded authority.",
        "setup": [
            "mkdir -p ${OUTPUT_DIR} ${SCRATCH}",
            "evidence-pack collect --out ${OUTPUT_DIR}/pack.json --audit ${AUDIT_LOG}",
        ],
        "teardown": ["rm -rf ${SCRATCH}"],
        "verifiers": [
            {
                "id": "cli_writes_declared_output",
                "kind": "cli_writes_declared_output",
                "description": "evidence-pack collect writes a non-empty pack.json at the declared output path",
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
                "description": "evidence-pack verify exits 0 on a freshly-collected pack",
                "command": "evidence-pack verify ${OUTPUT_DIR}/pack.json",
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
                "description": "evidence-pack verify on a non-existent path exits non-zero",
                "command": "expect-nonzero evidence-pack verify /nonexistent/path",
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
                "command": "canary-check evidence-pack collect --print-env",
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
                "description": "regenerating the MCP server produces an tool-contract.lock matching the running tool fingerprint",
                "command": "tool-contract verify-lock ${TOOL_CONTRACT_OUT}/tool-contract.lock",
                "expected_exit": 0,
                "expected_stdout_contains": "ok",
                "expected_stderr_contains": None,
                "expected_artefacts": ["${TOOL_CONTRACT_OUT}/tool-contract.lock"],
                "failure_mode": "mark_untrusted",
                "severity": "error",
            },
            {
                "id": "host_registrations_generated",
                "kind": "host_registrations_generated",
                "description": "evidence-pack-mcp generates Claude/Cursor/Codex host registration files that validate against their schemas",
                "command": "host-registration-check ${TOOL_CONTRACT_OUT}/host",
                "expected_exit": 0,
                "expected_stdout_contains": None,
                "expected_stderr_contains": None,
                "expected_artefacts": [
                    "${TOOL_CONTRACT_OUT}/host/claude.json",
                    "${TOOL_CONTRACT_OUT}/host/cursor.json",
                    "${TOOL_CONTRACT_OUT}/host/codex.json",
                ],
                "failure_mode": "mark_untrusted",
                "severity": "error",
            },
        ],
    }


PRIMER_SHA256 = "c138dd966c82f7bd792684ab3fef0f50d75aa9342468db8b5d265f24f3fb35a8"


def default_production_router_policy() -> dict:
    """In-memory mirror of contracts/examples/default-production.router-policy.yaml.

    Encodes the council-D4 3-tier policy structurally: premium / default /
    narrow_scope, with the narrow_scope narrow-scope model tier behind mandatory external
    review at sample rate 1.0.
    """
    return {
        "$schema": "https://engineering-doctrine/contracts/router-policy.v1.schema.json",
        "policy_version": "1.0.0",
        "schema_version": "1.0.0",
        "description": "v3 production default — 3-tier policy (premium/default/narrow_scope).",
        "tiers": {
            "premium": {
                "model": "claude-model-high-capability-4-7",
                "model_family": "model_high_capability",
                "primer": "anti-confab-200tok@1.0.0",
                "primer_sha256": PRIMER_SHA256,
                "verifier_pack": "evidence-pack-mcp-verifier-pack@1.0.0",
                "cell_classes": [
                    "security_critical",
                    "supervisor_change",
                    "doctrine_promotion",
                ],
                "max_cost_usd_per_cell": 10.00,
                "external_review_required": False,
            },
            "default": {
                "model": "claude-model-balanced-4-6",
                "model_family": "model_balanced",
                "primer": "anti-confab-200tok@1.0.0",
                "primer_sha256": PRIMER_SHA256,
                "verifier_pack": "evidence-pack-mcp-verifier-pack@1.0.0",
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
                "model": "claude-narrow-scope model-4-5-20251001",
                "model_family": "model_narrow",
                "primer": "anti-confab-200tok@1.0.0",
                "primer_sha256": PRIMER_SHA256,
                "verifier_pack": "evidence-pack-mcp-verifier-pack@1.0.0",
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
                "evidence_ref": "evidence-workbook/18-cross-product-test/v3/results/plan-b-v2-claim-audit-against-stage2/composite.md",
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
                "evidence_ref": "evidence-workbook/18-cross-product-test/v2/results/test-1-backbone/canonical-scoring-model-high-capability.md",
            },
        ],
        "refusal_rules": [
            {
                "rule_id": "narrow-scope model-no-artifact-production-without-primer",
                "when": {
                    "model_family": "model_narrow",
                    "cell_class": "artifact_production",
                    "primer": None,
                },
                "action": {
                    "refuse_routing": True,
                    "reason": "Empirical: tools-narrow-scope model+SKILLS canonical 31 (v2 Stage 2 smoking gun).",
                },
                "evidence_ref": "evidence-workbook/18-cross-product-test/v2/results/test-1-backbone/canonical-scoring.md",
            },
            {
                "rule_id": "narrow-scope model-no-greenfield",
                "when": {
                    "model_family": "model_narrow",
                    "cell_class": "greenfield_backbone",
                },
                "action": {
                    "refuse_routing": True,
                    "reason": "narrow-scope model-PRIMED canonical 73 < model-balanced 85; Δ +10 self-canonical means cell cannot detect over-claims on greenfield.",
                },
                "evidence_ref": "evidence-workbook/18-cross-product-test/v2/results/test-1-backbone/canonical-scoring-narrow-scope model-primed.md",
            },
            {
                "rule_id": "narrow-scope model-narrow-scope-requires-external-review",
                "when": {
                    "cell_class": "scaffolded_typed_authority",
                    "model_family": "model_narrow",
                },
                "action": {
                    "require_external_review": True,
                    "reason": "Δ +10 self-canonical on narrow-scope model-PRIMED; production use requires external scoring.",
                },
                "evidence_ref": "evidence-workbook/18-cross-product-test/v2/results/test-1-backbone/canonical-scoring-narrow-scope model-primed.md",
            },
            {
                "rule_id": "interpreter-wrapper-block",
                "when": {"command_matches": "^(bash|sh|zsh|powershell|pwsh|cmd)\\s+-c"},
                "action": {
                    "refuse_routing": True,
                    "reason": "CC-2 FALSIFIED at corpus scale (host-policy-layer benchmark interpreter-wrapper class 20%); defense-in-depth at router layer.",
                },
                "evidence_ref": "evidence-workbook/18-cross-product-test/v2/results/per-tool-failure-mode-tests-results/composite.md",
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
                "evidence_ref": "evidence-workbook/18-cross-product-test/v2/results/test-1-backbone/canonical-scoring.md",
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
    cases = [
        ("evidence-pack-build-review", rv, pr_evidence_build_review()),
        ("nightly-evidence-pack-audit", rv, nightly_audit()),
        ("evidence-pack-mcp-verifier-pack", vv, pr_evidence_verifier_pack()),
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

    # On-disk YAML examples — positive cases. Only run if PyYAML is installed
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
    else:
        print("(skipping on-disk YAML examples; PyYAML not installed)")

    # Negative: unknown top-level field on run-contract is rejected.
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
        "model_family": "model_narrow",
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
    bad_class = dict(rp_bad6["refusal_rules"][1])  # narrow-scope model-no-greenfield uses (model_family + cell_class)
    bad_class["when"] = {
        "cell_class": "completely_made_up_class",
        "model_family": "model_narrow",
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

    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
