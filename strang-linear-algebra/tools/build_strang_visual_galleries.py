"""Extract representative visuals from the Strang PDF and build chapter galleries."""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from collections import defaultdict
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PDF_PATH = (
    PROJECT_ROOT.parent
    / "unread-notes"
    / "Ed 5, Gilbert Strang - Introduction to Linear Algebra (2016, Wellesley-Cambridge Press).pdf"
)
CHAPTERS_DIR = PROJECT_ROOT / "hinglish-notes" / "chapters"
VISUALS_DIR = PROJECT_ROOT / "hinglish-notes" / "visuals"
ASSETS_DIR = PROJECT_ROOT / "hinglish-notes" / "assets" / "strang"

CHAPTERS = {
    1: {"slug": "introduction-to-vectors", "title": "Introduction to Vectors", "pages": (11, 40)},
    2: {"slug": "solving-linear-equations", "title": "Solving Linear Equations", "pages": (41, 132)},
    3: {"slug": "vector-spaces-and-subspaces", "title": "Vector Spaces and Subspaces", "pages": (133, 203)},
    4: {"slug": "orthogonality", "title": "Orthogonality", "pages": (204, 256)},
    5: {"slug": "determinants", "title": "Determinants", "pages": (257, 297)},
    6: {"slug": "eigenvalues-and-eigenvectors", "title": "Eigenvalues and Eigenvectors", "pages": (298, 373)},
    7: {"slug": "the-singular-value-decomposition", "title": "The Singular Value Decomposition (SVD)", "pages": (374, 410)},
    8: {"slug": "linear-transformations", "title": "Linear Transformations", "pages": (411, 439)},
    9: {"slug": "complex-vectors-and-matrices", "title": "Complex Vectors and Matrices", "pages": (440, 461)},
    10: {"slug": "applications", "title": "Applications", "pages": (462, 517)},
    11: {"slug": "numerical-linear-algebra", "title": "Numerical Linear Algebra", "pages": (518, 544)},
    12: {"slug": "probability-and-statistics", "title": "Linear Algebra in Probability & Statistics", "pages": (545, 584)},
}

MAX_PREVIEWS = 8


def chapter_for_page(page: int) -> int | None:
    for chapter, meta in CHAPTERS.items():
        start, end = meta["pages"]
        if start <= page <= end:
            return chapter
    return None


def parse_pdfimages_list() -> dict[int, list[dict]]:
    output = subprocess.check_output(["pdfimages", "-list", str(PDF_PATH)]).decode("utf-8", errors="ignore")
    per_page_index: dict[int, int] = defaultdict(int)
    chapter_candidates: dict[int, list[dict]] = defaultdict(list)

    for line in output.splitlines()[2:]:
        parts = line.split()
        if len(parts) < 16 or not parts[0].isdigit():
            continue
        page = int(parts[0])
        local_index = per_page_index[page]
        per_page_index[page] += 1

        image_type = parts[2]
        width = int(parts[3])
        height = int(parts[4])
        encoding = parts[8].lower()
        x_ppi = int(parts[12])
        y_ppi = int(parts[13])
        chapter = chapter_for_page(page)
        if chapter is None or image_type != "image":
            continue

        area = width * height
        ratio = max(width / height, height / width)

        # Keep images that look like real figures, and skip tiny OCR fragments or whole-page scans.
        if x_ppi < 300 or y_ppi < 300:
            continue
        if encoding != "jpeg":
            continue
        if width < 300 or height < 180:
            continue
        if area < 120_000 or area > 3_000_000:
            continue
        if ratio > 8:
            continue

        chapter_candidates[chapter].append(
            {
                "page": page,
                "local_index": local_index,
                "width": width,
                "height": height,
                "area": area,
            }
        )

    return chapter_candidates


def choose_previews(candidates: list[dict]) -> list[dict]:
    best_per_page: list[dict] = []
    grouped: dict[int, list[dict]] = defaultdict(list)
    for candidate in candidates:
        grouped[candidate["page"]].append(candidate)
    for page in sorted(grouped):
        best = max(grouped[page], key=lambda item: item["area"])
        best_per_page.append(best)

    if len(best_per_page) <= MAX_PREVIEWS:
        return best_per_page

    selected = []
    seen_pages = set()
    total = len(best_per_page)
    for i in range(MAX_PREVIEWS):
        idx = round(i * (total - 1) / (MAX_PREVIEWS - 1))
        candidate = best_per_page[idx]
        if candidate["page"] in seen_pages:
            continue
        seen_pages.add(candidate["page"])
        selected.append(candidate)
    return selected


def extract_page_images(page: int, temp_dir: Path) -> None:
    prefix = temp_dir / "img"
    subprocess.check_call(
        [
            "pdfimages",
            "-f",
            str(page),
            "-l",
            str(page),
            "-all",
            "-p",
            str(PDF_PATH),
            str(prefix),
        ]
    )


def copy_preview_image(page: int, local_index: int, target_dir: Path) -> Path:
    with tempfile.TemporaryDirectory() as temp_name:
        temp_dir = Path(temp_name)
        extract_page_images(page, temp_dir)
        pattern = f"img-{page:03d}-{local_index:03d}.*"
        matches = list(temp_dir.glob(pattern))
        if not matches:
            raise FileNotFoundError(f"No extracted image found for page {page}, local index {local_index}")
        source = matches[0]
        target = target_dir / f"page-{page:03d}-img-{local_index:03d}{source.suffix.lower()}"
        shutil.copy2(source, target)
        return target


def build_gallery_markdown(chapter: int, previews: list[dict], copied_paths: list[Path]) -> str:
    meta = CHAPTERS[chapter]
    lines = [
        f"# Chapter {chapter} Visual Gallery",
        "",
        f"These are representative visuals extracted from **{meta['title']}**.",
        "",
        "Use them with the chapter notes and original PDF.",
        "",
    ]

    for preview, path in zip(previews, copied_paths):
        rel = Path("..") / "assets" / "strang" / f"{chapter:02d}-{meta['slug']}" / path.name
        lines.extend(
            [
                f"## PDF Page {preview['page']}",
                "",
                f"![Chapter {chapter} visual from PDF page {preview['page']}]({rel.as_posix()})",
                "",
            ]
        )

    return "\n".join(lines) + "\n"


def inject_gallery_link(chapter: int) -> None:
    meta = CHAPTERS[chapter]
    path = CHAPTERS_DIR / f"{chapter:02d}-{meta['slug']}.md"
    text = path.read_text()
    link_line = f"Visual gallery: [`{chapter:02d}-{meta['slug']}.md`](../visuals/{chapter:02d}-{meta['slug']}.md)"
    if link_line in text:
        return
    lines = text.splitlines()
    if len(lines) < 2:
        return
    lines.insert(1, "")
    lines.insert(2, link_line)
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    VISUALS_DIR.mkdir(parents=True, exist_ok=True)
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)

    candidates = parse_pdfimages_list()

    for chapter, chapter_candidates in candidates.items():
        meta = CHAPTERS[chapter]
        previews = choose_previews(chapter_candidates)
        target_dir = ASSETS_DIR / f"{chapter:02d}-{meta['slug']}"
        if target_dir.exists():
            shutil.rmtree(target_dir)
        target_dir.mkdir(parents=True, exist_ok=True)

        copied_paths = []
        for preview in previews:
            copied = copy_preview_image(preview["page"], preview["local_index"], target_dir)
            copied_paths.append(copied)

        gallery = build_gallery_markdown(chapter, previews, copied_paths)
        gallery_path = VISUALS_DIR / f"{chapter:02d}-{meta['slug']}.md"
        gallery_path.write_text(gallery)
        inject_gallery_link(chapter)
        print(f"Wrote {gallery_path.relative_to(PROJECT_ROOT)} with {len(copied_paths)} preview images")


if __name__ == "__main__":
    main()
