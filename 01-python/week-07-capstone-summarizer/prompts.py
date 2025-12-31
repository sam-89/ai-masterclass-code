from __future__ import annotations


def build_summary_prompt(text: str) -> str:
    return (
        "You are a helpful assistant. Summarize the following text in markdown. "
        "Return a short title and a '## Summary' section with bullet points.\n\n"
        f"TEXT:\n{text.strip()}\n"
    )
