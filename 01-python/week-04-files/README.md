# Week 04 — Files

Goal: read input files, clean/normalize their contents, represent them as Python objects, and write outputs.

## What you’ll build

- `data/` contains a couple sample files
- `main.py` loads all files under `data/`
- it creates a `Document` dataclass with:
  - `source` (filename)
  - `text` (cleaned text)
  - `chars` (character count)
  - `lines` (line count)
- it writes cleaned outputs to `out/cleaned_<name>.txt`

## Run

```bash
python main.py
```

Check the `out/` folder after running.
