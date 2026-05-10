"""Extract chapter-wise raw text from the local Strang PDF."""

from __future__ import annotations

import subprocess
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PDF_PATH = (
    PROJECT_ROOT.parent
    / "unread-notes"
    / "Ed 5, Gilbert Strang - Introduction to Linear Algebra (2016, Wellesley-Cambridge Press).pdf"
)
OUTPUT_DIR = PROJECT_ROOT / "chapter-extracts"

CHAPTERS = [
    (0, "preface-and-front-matter", 1, 10),
    (1, "introduction-to-vectors", 11, 40),
    (2, "solving-linear-equations", 41, 132),
    (3, "vector-spaces-and-subspaces", 133, 203),
    (4, "orthogonality", 204, 256),
    (5, "determinants", 257, 297),
    (6, "eigenvalues-and-eigenvectors", 298, 373),
    (7, "the-singular-value-decomposition", 374, 410),
    (8, "linear-transformations", 411, 439),
    (9, "complex-vectors-and-matrices", 440, 461),
    (10, "applications", 462, 517),
    (11, "numerical-linear-algebra", 518, 544),
    (12, "probability-and-statistics", 545, 584),
]


def extract_pages(start: int, end: int) -> str:
    output = subprocess.check_output(
        [
            "pdftotext",
            "-layout",
            "-f",
            str(start),
            "-l",
            str(end),
            str(PDF_PATH),
            "-",
        ]
    )
    return output.decode("utf-8", errors="ignore")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for number, slug, start, end in CHAPTERS:
        text = extract_pages(start, end)
        target = OUTPUT_DIR / f"{number:02d}-{slug}.txt"
        target.write_text(text)
        print(f"Wrote {target.relative_to(PROJECT_ROOT)} from PDF pages {start}-{end}")


if __name__ == "__main__":
    main()
