"""Split the complete Hinglish notes file into separate chapter markdown files."""

from __future__ import annotations

import re
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
NOTES_DIR = PROJECT_ROOT / "hinglish-notes"
MASTER = NOTES_DIR / "Strang-Linear-Algebra-Hinglish-Notes.md"
CHAPTER_DIR = NOTES_DIR / "chapters"

SLUGS = {
    1: "introduction-to-vectors",
    2: "solving-linear-equations",
    3: "vector-spaces-and-subspaces",
    4: "orthogonality",
    5: "determinants",
    6: "eigenvalues-and-eigenvectors",
    7: "the-singular-value-decomposition",
    8: "linear-transformations",
    9: "complex-vectors-and-matrices",
    10: "applications",
    11: "numerical-linear-algebra",
    12: "probability-and-statistics",
}


def main() -> None:
    text = MASTER.read_text()
    CHAPTER_DIR.mkdir(parents=True, exist_ok=True)

    parts = re.split(r"(?=^# Chapter \d+ - )", text, flags=re.MULTILINE)
    intro = parts[0].strip()
    (CHAPTER_DIR / "00-preface-and-roadmap.md").write_text(intro + "\n")

    for part in parts[1:]:
        first_line = part.splitlines()[0].strip()
        match = re.match(r"# Chapter (\d+) - (.+)", first_line)
        if not match:
            continue
        number = int(match.group(1))
        slug = SLUGS[number]
        target = CHAPTER_DIR / f"{number:02d}-{slug}.md"
        target.write_text(part.strip() + "\n")
        print(f"Wrote {target.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
