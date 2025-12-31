from __future__ import annotations

import time
from typing import Optional

import requests


def get_with_retries(url: str, *, timeout_s: float = 5.0, retries: int = 3) -> requests.Response:
    backoff_s = 1.0
    last_exc: Optional[BaseException] = None

    for attempt in range(1, retries + 1):
        try:
            resp = requests.get(url, timeout=timeout_s)
            if resp.status_code == 429 or 500 <= resp.status_code < 600:
                raise requests.HTTPError(f"retryable status={resp.status_code}", response=resp)
            return resp
        except (requests.Timeout, requests.ConnectionError, requests.HTTPError) as exc:
            last_exc = exc
            if attempt == retries:
                break

            # Exponential backoff: 1s, 2s, 4s, ...
            time.sleep(backoff_s)
            backoff_s *= 2

    raise RuntimeError(f"Request failed after {retries} attempts") from last_exc


def main() -> None:
    url = "https://httpbin.org/get"
    resp = get_with_retries(url, timeout_s=5.0, retries=3)
    text = resp.text
    print(f"status: {resp.status_code}")
    print(text[:400])


if __name__ == "__main__":
    main()
