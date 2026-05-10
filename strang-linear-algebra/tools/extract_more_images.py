"""
Extract additional images from the Strang 5th ed. PDF for sections that need more visuals.

Usage:
    cd strang-linear-algebra
    python tools/extract_more_images.py

Requirements:
    - poppler (pdfimages + pdftoppm) installed via homebrew: brew install poppler
    - PDF at the path below (5th edition)

This script renders entire PDF pages as high-quality JPEGs using pdftoppm,
then saves them to the assets folder following the naming convention:
    page-{pdf_page_number}-img-001.jpg

After running, each chapter's notes will reference these images.
"""

from __future__ import annotations

import subprocess
import tempfile
import shutil
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PDF_PATH = (
    PROJECT_ROOT.parent
    / "unread-notes"
    / "Ed 5, Gilbert Strang - Introduction to Linear Algebra (2016, Wellesley-Cambridge Press).pdf"
)
ASSETS_DIR = PROJECT_ROOT / "hinglish-notes" / "assets" / "strang"

# ──────────────────────────────────────────────────────────────────────────────
# Pages to extract per chapter.
# Key = chapter slug, Value = list of (pdf_page_number, label) tuples.
# PDF page = book page + 10  (for 5th edition with 10 front-matter pages).
# Pick pages that have figures/diagrams, not just text.
# ──────────────────────────────────────────────────────────────────────────────
PAGES_TO_EXTRACT: dict[str, list[tuple[int, str]]] = {
    "01-introduction-to-vectors": [
        # Already has: 11,15,17,22,28,33,35,39 — add more from 1.1-1.3
        (13, "Worked Ex 1.1A — plane spanned by v and w in 3D"),
        (19, "Dot product cosine formula — angle between vectors"),
        (26, "Schwarz inequality and triangle inequality diagram"),
    ],
    "02-solving-linear-equations": [
        # Already has: 42,47,59,71,84,97,111,126 — add for 2.5/2.6/2.7
        (93,  "Invertibility conditions — singular vs invertible matrix"),
        (101, "LU factorization — multipliers stored in L, pivots in U"),
        (105, "Forward substitution Ly=b then back substitution Ux=y"),
        (113, "Transpose rules — (AB)T = BT AT diagram"),
        (117, "Symmetric matrix and LDLt factorization"),
        (120, "Permutation matrices PA=LU"),
    ],
    "03-vector-spaces-and-subspaces": [
        # Already has: 135,147,152,161,168,179,194,200 — add for 3.4/3.5
        (171, "Independence test — pivot count in matrix"),
        (175, "Basis definition — spanning + independent"),
        (183, "Four subspaces diagram with dimensions r, n-r, m-r"),
        (187, "Rank-nullity theorem — dim of column space + nullspace = n"),
        (191, "Rank(AB) inequalities"),
    ],
    "04-orthogonality": [
        # Already has: 205,209,218,221,234,238,247,252 — add more
        (198, "Orthogonal complement V-perp definition"),
        (213, "Normal equations derivation — AT(b-Ax)=0"),
        (229, "Least squares line fitting — error perpendicular to column space"),
        (241, "Gram-Schmidt process step by step"),
        (248, "QR factorization — R entries as dot products"),
    ],
    "05-determinants": [
        # Already has: 260,269,275,276,284,285,288,292 — add for 10 rules
        (251, "Determinant rules 1-3: identity, row swap, linearity"),
        (253, "Determinant rules 4-6: equal rows, subtraction, zero row"),
        (255, "Determinant rules 7-8: triangular matrix, singular matrix"),
        (258, "Determinant rules 9-10: det(AB), det(AT)"),
        (262, "Product of pivots = determinant"),
        (265, "Worked Example 5.1A — checkerboard and singular matrices"),
        (272, "Big formula — sum over permutations"),
        (278, "Cofactor Cij = (-1)^(i+j) Mij — sign checkerboard"),
    ],
    "06-eigenvalues-and-eigenvectors": [
        # Already has: 299,308,319,330,334,346,363,368 — add for full coverage
        (290, "Eigenvalue equation Ax=lambda x — characteristic polynomial"),
        (293, "Trace = sum of eigenvalues, det = product of eigenvalues"),
        (302, "Diagonalization A = X Lambda X-inv"),
        (307, "Matrix powers Ak = X Lambda^k X-inv"),
        (313, "Fibonacci — difference equation, golden ratio eigenvalue"),
        (322, "Stability: real negative lambda -> decay, positive -> growth"),
        (337, "Symmetric matrix — real eigenvalues, orthogonal eigenvectors"),
        (341, "Spectral theorem A = Q Lambda Qt"),
        (348, "Positive definite — five equivalent tests"),
        (355, "Ellipse xTSx=1 — axes = eigenvectors, lengths = 1/sqrt(lambda)"),
    ],
    "07-the-singular-value-decomposition": [
        # Already has: 377,380,381,384,396,404,405,408
        (367, "SVD overview A=U Sigma VT — four subspaces from singular vectors"),
        (372, "Image compression — rank-k approximation and error"),
        (376, "Computing SVD — ATA eigenvalues give singular values squared"),
        (388, "PCA — principal components from SVD of centered data"),
        (392, "Polar decomposition A = QS"),
        (399, "Pseudoinverse A+ = V Sigma+ UT — least squares connection"),
    ],
    "08-linear-transformations": [
        # Already has: 413,414,415,416,422,423,433,439
        (402, "Linear transformation rules T(u+v)=T(u)+T(v), T(cu)=cT(u)"),
        (407, "Rotation, reflection, projection — standard 2D transformations"),
        (410, "Matrix of T — column j = T(vj) in output basis"),
        (418, "Similar matrices B=M-inv AM — same T, different bases"),
        (426, "Jordan normal form — generalized eigenvectors"),
        (431, "Nilpotent matrix powers K^2=0"),
    ],
    "09-complex-vectors-and-matrices": [
        # Already has: 442,445,449,451,452,456,459,460
        (433, "Euler formula e^{i theta} = cos+i sin — unit circle"),
        (436, "Nth roots of unity — equally spaced on unit circle"),
        (440, "Complex inner product u*v — conjugate transpose"),
        (444, "Hermitian matrix — real eigenvalues proof"),
        (447, "DFT matrix F4 — orthogonal columns, F*F = nI"),
        (453, "FFT butterfly diagram — O(n log n) algorithm"),
    ],
    "10-applications": [
        # Already has: 464,467,475,480,486,489,494,507
        (455, "Incidence matrix — graph to matrix encoding"),
        (461, "Kirchhoff current law matrix form Ax = b"),
        (469, "Spring-mass stiffness matrix K = AT C A"),
        (477, "Markov steady state — eigenvector for lambda=1"),
        (483, "Leontief model — geometric series (I-A)^-1"),
        (491, "Linear programming — corner of feasible region"),
        (499, "Fourier series — orthogonal sine/cosine basis"),
        (504, "Computer graphics — homogeneous coordinates 3x3 matrix"),
    ],
    "11-numerical-linear-algebra": [
        # Already has: 522,524,525,526,530,535,536,541
        (513, "Partial pivoting — swap rows to get largest pivot"),
        (518, "LU factorization with PA=LU — backward stability"),
        (520, "Banded matrix — bandwidth w, cost O(nw^2)"),
        (528, "Condition number kappa = sigma1/sigman"),
        (532, "Error amplification — delta_x/x <= kappa * delta_b/b"),
        (537, "Jacobi vs Gauss-Seidel iteration comparison"),
        (539, "Conjugate gradient — Krylov subspace method"),
    ],
    "12-probability-and-statistics": [
        # Already has: 548,552,556,559,560,563,565,570
        (540, "Mean E[X] and variance Var(X) = E[X^2]-mu^2"),
        (543, "Normal distribution N(mu, sigma^2) — bell curve"),
        (546, "Joint probability matrix — independence = rank 1"),
        (551, "Covariance matrix V = E[(X-mu)(X-mu)T]"),
        (557, "Multivariate Gaussian — ellipsoid level curves"),
        (562, "Weighted least squares — ATV^-1 A x = ATV^-1 b"),
        (567, "Gauss-Markov theorem — BLUE estimator"),
    ],
}


def render_page_as_jpeg(pdf_path: Path, page_num: int, output_path: Path, dpi: int = 150) -> None:
    """Render a single PDF page as a JPEG using pdftoppm."""
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        prefix = tmp_path / "page"
        subprocess.check_call([
            "pdftoppm",
            "-f", str(page_num),
            "-l", str(page_num),
            "-r", str(dpi),
            "-jpeg",
            str(pdf_path),
            str(prefix),
        ], stderr=subprocess.DEVNULL)
        # pdftoppm names output like page-001.jpg
        generated = sorted(tmp_path.glob("page-*.jpg"))
        if not generated:
            generated = sorted(tmp_path.glob("page-*.jpeg"))
        if not generated:
            raise FileNotFoundError(f"pdftoppm produced no output for page {page_num}")
        shutil.copy2(generated[0], output_path)


def chapter_slug_to_number(slug: str) -> int:
    return int(slug.split("-")[0])


def main() -> None:
    if not PDF_PATH.exists():
        print(f"ERROR: PDF not found at:\n  {PDF_PATH}")
        print()
        print("Please place the 5th edition PDF at that path, then re-run this script.")
        return

    print(f"PDF found: {PDF_PATH.name}")
    print()

    total_extracted = 0
    for slug, pages in PAGES_TO_EXTRACT.items():
        chapter_dir = ASSETS_DIR / slug
        chapter_dir.mkdir(parents=True, exist_ok=True)

        for pdf_page, label in pages:
            output_file = chapter_dir / f"page-{pdf_page:03d}-img-001.jpg"
            if output_file.exists():
                print(f"  [skip] {output_file.name} (already exists)")
                continue
            try:
                render_page_as_jpeg(PDF_PATH, pdf_page, output_file)
                print(f"  [OK]   {slug}/{output_file.name}  —  {label}")
                total_extracted += 1
            except Exception as exc:
                print(f"  [FAIL] page {pdf_page}: {exc}")

    print()
    print(f"Done. {total_extracted} new images extracted.")
    print()
    print("Next step: run tools/embed_new_images.py to add image tags to the notes.")


if __name__ == "__main__":
    main()
