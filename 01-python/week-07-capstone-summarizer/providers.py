from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class LLMResponse:
    provider: str
    model: str
    created_at_utc: str
    content: str


def generate(*, provider: str, model: str, prompt: str) -> LLMResponse:
    provider = (provider or "").strip()
    model = (model or "").strip()

    created = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

    if provider == "mock":
        # Deterministic content derived from the prompt length (no randomness).
        n_chars = len(prompt)
        content = (
            "# Mock Summary\n\n"
            "## Summary\n"
            f"- Provider: mock\n- Model: {model}\n- Prompt chars: {n_chars}\n"
            "- Key idea: This is a deterministic placeholder summary.\n"
        )
        return LLMResponse(provider="mock", model=model or "mock-1", created_at_utc=created, content=content)

    raise ValueError(f"Unsupported provider: {provider!r}")
