from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Document:
    source: str
    text: str
    chars: int
    lines: int


def clean_lines(raw: str) -> str:
    # Normalize line endings, trim trailing whitespace, drop extra blank lines.
    # Keep content readable while removing noise.
    lines = [ln.strip() for ln in raw.replace("\r\n", "\n").replace("\r", "\n").split("\n")]
    cleaned_lines = []
    last_was_blank = False
    for ln in lines:
        is_blank = ln == ""
        if is_blank and last_was_blank:
            continue
        cleaned_lines.append(ln)
        last_was_blank = is_blank
    return "\n".join(cleaned_lines).strip() + "\n"


def load_documents(data_dir: Path) -> list[Document]:
    docs: list[Document] = []
    for path in sorted(p for p in data_dir.rglob("*") if p.is_file()):
        raw = path.read_text(encoding="utf-8")
        cleaned = clean_lines(raw)
        docs.append(
            Document(
                source=path.name,
                text=cleaned,
                chars=len(cleaned),
                lines=len(cleaned.splitlines()),
            )
        )
    return docs


def write_outputs(docs: list[Document], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for doc in docs:
        stem = Path(doc.source).stem
        out_path = out_dir / f"cleaned_{stem}.txt"
        out_path.write_text(doc.text, encoding="utf-8")


def main() -> None:
    here = Path(__file__).parent
    data_dir = here / "data"
    out_dir = here / "out"

    docs = load_documents(data_dir)
    write_outputs(docs, out_dir)

    print(f"Loaded {len(docs)} documents")
    for d in docs:
        print(f"- {d.source}: {d.lines} lines, {d.chars} chars")


if __name__ == "__main__":
    main()
