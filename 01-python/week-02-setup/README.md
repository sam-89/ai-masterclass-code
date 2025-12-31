# Week 02 — Setup (venv + env vars)

Goal: set up a virtual environment, understand environment variables, and run a simple script.

## 1) Create and activate a venv

### Windows (PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 2) Create a `.env` file (optional)

Copy the example file and edit the value:

```bash
cp .env.example .env
```

Then set `EXAMPLE_API_KEY` to something non-empty.

> Note: This repo ignores `.env` by default via `.gitignore`.

## 3) Run

```bash
python main.py
```

You should see:

- current UTC timestamp
- Python version
- which interpreter is being used
- current working directory
- whether `EXAMPLE_API_KEY` is set
