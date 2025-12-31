# Week 07 — Capstone: Summarizer (CLI)

Goal: build a tiny summarizer tool with a provider abstraction.

## What you’ll build

- `prompts.py` builds the summarization prompt
- `providers.py` implements a `mock` provider
- `main.py` wires everything together into a CLI

## Run

```bash
python main.py --input data/sample.txt --output out/summary.md
```

Optional args:

- `--provider` (default: `mock`)
- `--model` (default: `mock-1`)
