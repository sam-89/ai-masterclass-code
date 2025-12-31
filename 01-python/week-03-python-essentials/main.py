from __future__ import annotations

from dataclasses import dataclass

from text_utils import clean_text, split_sentences


@dataclass(frozen=True)
class Config:
    lowercase: bool = True
    min_sentence_len: int = 12


def main() -> None:
    cfg = Config(lowercase=True, min_sentence_len=12)

    sample = """
    Hello   world!  This is a sample   text.

    It has weird   spacing, and multiple lines.
    Can we clean it? Yes, we can.
    """

    cleaned = clean_text(sample, lowercase=cfg.lowercase)
    sentences = split_sentences(cleaned)

    keep = [s for s in sentences if len(s) >= cfg.min_sentence_len]

    print("CLEANED TEXT:")
    print(cleaned)
    print("\nSENTENCES (filtered):")
    for i, s in enumerate(keep, start=1):
        print(f"{i:02d}. {s}")


if __name__ == "__main__":
    main()
