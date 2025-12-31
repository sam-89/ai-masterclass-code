from __future__ import annotations

import argparse
import json
import logging
from datetime import datetime, timezone
from pathlib import Path

from validators import ValidationError, validate_summary


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Reliability basics: validate outputs + run report")
    p.add_argument("--input", required=True, help="Path to input text file")
    p.add_argument("--output", required=True, help="Path to output markdown file")
    return p.parse_args()


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)sZ %(levelname)s %(message)s",
    )

    args = parse_args()
    in_path = Path(args.input)
    out_path = Path(args.output)

    logging.info("reading input: %s", in_path)
    source = in_path.read_text(encoding="utf-8")

    # Placeholder summary: in a real project this would come from a model/provider.
    summary = (
        "# Validated Summary\n\n"
        "## Summary\n"
        "- This is a placeholder summary.\n"
        f"- Source chars: {len(source)}\n"
        "- Next step: replace this with real generation.\n"
    )

    status = "ok"
    error = None
    try:
        validate_summary(summary, min_len=40, max_len=10_000)
        logging.info("validation passed")
    except ValidationError as e:
        status = "error"
        error = str(e)
        logging.error("validation failed: %s", e)
        raise
    finally:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(summary, encoding="utf-8")
        logging.info("wrote output: %s", out_path)

        report_dir = out_path.parent / "run_report"
        # keep spec path: out/run_report.json
        report_path = out_path.parent / "run_report.json"
        report = {
            "status": status,
            "error": error,
            "input": in_path.as_posix(),
            "output": out_path.as_posix(),
            "created_at_utc": utc_now(),
            "input_chars": len(source),
            "output_chars": len(summary),
        }
        report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        logging.info("wrote report: %s", report_path)


if __name__ == "__main__":
    main()
