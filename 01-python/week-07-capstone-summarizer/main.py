from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

from prompts import build_summary_prompt
from providers import generate


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Capstone summarizer")
    p.add_argument("--input", required=True, help="Path to input text file")
    p.add_argument("--output", required=True, help="Path to output markdown file")
    p.add_argument("--provider", default="mock", help="LLM provider (default: mock)")
    p.add_argument("--model", default="mock-1", help="Model name (default: mock-1)")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    in_path = Path(args.input)
    out_path = Path(args.output)

    source_text = in_path.read_text(encoding="utf-8")
    prompt = build_summary_prompt(source_text)

    resp = generate(provider=args.provider, model=args.model, prompt=prompt)

    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    md = (
        "# Summary Output\n\n"
        f"- Provider: `{resp.provider}`\n"
        f"- Model: `{resp.model}`\n"
        f"- Created (UTC): `{resp.created_at_utc}`\n"
        f"- Written (UTC): `{now_utc}`\n"
        f"- Source: `{in_path.as_posix()}`\n\n"
        "---\n\n"
        f"{resp.content.strip()}\n"
    )

    out_path.write_text(md, encoding="utf-8")
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
