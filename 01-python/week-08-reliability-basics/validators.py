from __future__ import annotations


class ValidationError(ValueError):
    pass


def validate_summary(
    summary_md: str,
    *,
    min_len: int = 40,
    max_len: int = 10_000,
) -> None:
    if not summary_md or not summary_md.strip():
        raise ValidationError("summary is empty")

    s = summary_md.strip()

    if len(s) < min_len:
        raise ValidationError(f"summary too short (len={len(s)} < {min_len})")

    if "## Summary" not in s:
        raise ValidationError("summary missing required heading '## Summary'")

    if len(s) > max_len:
        raise ValidationError(f"summary too long (len={len(s)} > {max_len})")
