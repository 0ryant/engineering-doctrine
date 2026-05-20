#!/usr/bin/env python3
"""
Validation harness for the v1 run-contract and verifier-pack schemas.

Loads both schemas, builds in-memory sample instances (matching the worked
examples in doctrine/patterns/run-contracts.md and verifier-packs.md), and
prints validation results. Used by CI and during authoring to confirm the
canonical examples remain self-validating.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
RUN_SCHEMA = ROOT / "contracts" / "run-contract.v1.schema.json"
VP_SCHEMA = ROOT / "contracts" / "verifier-pack.v1.schema.json"


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


def main() -> int:
    run_schema = load(RUN_SCHEMA)
    vp_schema = load(VP_SCHEMA)
    Draft202012Validator.check_schema(run_schema)
    Draft202012Validator.check_schema(vp_schema)
    rv = Draft202012Validator(run_schema)
    vv = Draft202012Validator(vp_schema)

    failures = 0
    cases = [
        ("evidence-pack-build-review", rv, pr_evidence_build_review()),
        ("nightly-evidence-pack-audit", rv, nightly_audit()),
        ("evidence-pack-mcp-verifier-pack", vv, pr_evidence_verifier_pack()),
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

    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
