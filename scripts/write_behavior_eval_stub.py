#!/usr/bin/env python3
"""Write a behavior-regression eval stub for a generated model output.

This script records provenance for CI/manual behavior runs. It does not assign
quality scores; human review or a separate semantic judge must do that.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--eval-output", required=True, type=Path)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--model", default="configured_by_command_template")
    parser.add_argument("--artifact-name", default="behavior-regression-output")
    args = parser.parse_args()

    output = args.output_dir / f"{args.case}.out"
    if not output.exists() or output.stat().st_size == 0:
        print(f"Behavior eval stub failed: missing output {output}", file=sys.stderr)
        return 1

    record = {
        "case": args.case,
        "commit": args.commit,
        "model": args.model,
        "runtime_model_executed": True,
        "ci_controlled": True,
        "evidence_level": "ci_single_run",
        "score_interpretation": "unscored behavior artifact; requires human or semantic review",
        "model_output": str(output),
        "output_sha256": sha256_file(output),
        "output_bytes": output.stat().st_size,
        "artifact_name": args.artifact_name,
        "scoring_status": "PENDING_HUMAN_REVIEW",
        "blocking_failures": [],
    }

    args.eval_output.parent.mkdir(parents=True, exist_ok=True)
    args.eval_output.write_text(json.dumps(record, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote behavior eval stub: {args.eval_output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
