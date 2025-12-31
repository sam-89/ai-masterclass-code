from __future__ import annotations

import os
import sys
from datetime import datetime, timezone
from pathlib import Path


def main() -> None:
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    print(f"timestamp_utc: {now_utc}")
    print(f"python_version: {sys.version.split()[0]}")
    print(f"sys.executable: {sys.executable}")
    print(f"cwd: {Path.cwd()}")

    api_key = os.getenv("EXAMPLE_API_KEY")
    is_set = bool(api_key and api_key.strip())
    print(f"EXAMPLE_API_KEY set: {is_set}")


if __name__ == "__main__":
    main()
