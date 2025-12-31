# Week 08 — Reliability Basics

Goal: introduce lightweight validation, logging, and run reports.

## What you’ll build

- `validators.py` with a `validate_summary()` function
- `main.py` that:
  - reads an input file
  - creates a placeholder summary that includes `## Summary`
  - validates it
  - writes output markdown
  - writes `out/run_report.json` with metadata

## Run

```bash
python main.py --input ../week-07-capstone-summarizer/data/sample.txt --output out/validated_summary.md
```
