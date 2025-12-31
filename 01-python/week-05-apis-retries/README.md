# Week 05 — APIs & Retries

Goal: call an HTTP API and implement basic retry logic with exponential backoff.

## Install dependency

```bash
pip install requests
```

## Run

```bash
python main.py
```

The script calls:

- `https://httpbin.org/get`

and prints the first 400 characters of the response body.
