"""Generate the weekly study notebooks for the Strang linear algebra track."""

from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent
from uuid import uuid4


PROJECT_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_DIR = PROJECT_ROOT / "notebooks"


def markdown_cell(text: str) -> dict:
    clean = dedent(text).strip()
    return {
        "cell_type": "markdown",
        "id": uuid4().hex[:8],
        "metadata": {},
        "source": [line + "\n" for line in clean.splitlines()],
    }


def code_cell(code: str) -> dict:
    clean = dedent(code).strip()
    return {
        "cell_type": "code",
        "execution_count": None,
        "id": uuid4().hex[:8],
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in clean.splitlines()],
    }


SETUP_CODE = dedent(
    """
    from pathlib import Path
    import sys

    import numpy as np
    import sympy as sp
    import matplotlib.pyplot as plt
    from IPython.display import display

    candidates = [Path.cwd(), Path.cwd().parent]
    for base in candidates:
        if (base / "src").exists():
            PROJECT_ROOT = base
            break
    else:
        raise RuntimeError("Run this notebook from the project root or from notebooks/.")

    sys.path.insert(0, str(PROJECT_ROOT / "src"))

    from strang_la import *
    from strang_la.viz import plot_gaussian_contours, plot_singular_values, plot_transformation_grid, plot_vectors

    np.set_printoptions(precision=4, suppress=True)
    sp.init_printing()
    """
).strip()


WEEK_DATA = [
    {
        "filename": "week01_ch01_vectors.ipynb",
        "title": "Week 1 - Chapter 1: Vectors and Ax = b",
        "chapter_focus": "1.1 to 1.3",
        "topics": [
            "vectors and linear combinations",
            "dot products and length",
            "matrix intro and simple symbolic solve",
        ],
        "exercise_plan": "Target: 8-10 review problems across 1.1, 1.2, 1.3 plus 1 challenge problem.",
        "demo_code": dedent(
            """
            v = np.array([2.0, 1.0])
            w = np.array([1.0, 3.0])
            plot_vectors([v, w, v + w], labels=["v", "w", "v+w"], title="Vector addition")
            plt.show()

            dot = float(v @ w)
            angle_deg = np.degrees(np.arccos(dot / (np.linalg.norm(v) * np.linalg.norm(w))))
            print("dot(v, w) =", dot)
            print("angle(v, w) in degrees =", round(angle_deg, 2))

            A = sp.Matrix([[2, 1], [1, 3]])
            b = sp.Matrix([5, 4])
            print("Solution to Ax=b:", A.LUsolve(b))
            """
        ).strip(),
    },
    {
        "filename": "week02_ch02_elimination.ipynb",
        "title": "Week 2 - Chapter 2: Elimination, Inverse, LU",
        "chapter_focus": "2.1 to 2.7",
        "topics": [
            "row picture and column picture",
            "Gaussian elimination",
            "Gauss-Jordan inverse and LU factorization",
        ],
        "exercise_plan": "Target: 9-12 review problems across 2.1 to 2.7 plus 1 challenge problem.",
        "demo_code": dedent(
            """
            A = sp.Matrix([[2, 1, 1], [4, -6, 0], [-2, 7, 2]])
            b = sp.Matrix([5, -2, 9])
            steps = gaussian_elimination_steps(A, b)
            print("Number of elimination snapshots:", len(steps))
            print("Last operation:", steps[-1]["operation"])
            print("Upper-triangular A:")
            display(steps[-1]["A"])

            P, L, U = lu_factor(A)
            print("Check P*A == L*U:", sp.simplify(P * A - L * U) == sp.zeros(*A.shape))
            print("Inverse from Gauss-Jordan:")
            display(inverse_gauss_jordan(sp.Matrix([[1, 2], [3, 5]])))
            """
        ).strip(),
    },
    {
        "filename": "week03_ch03_vector_spaces.ipynb",
        "title": "Week 3 - Chapter 3: Vector Spaces and Subspaces",
        "chapter_focus": "3.1 to 3.5",
        "topics": [
            "spaces and subspaces",
            "nullspace and complete solution",
            "basis, dimension, four subspaces",
        ],
        "exercise_plan": "Target: 8-10 review problems across 3.1 to 3.5 plus 1 challenge problem.",
        "demo_code": dedent(
            """
            A = sp.Matrix([[1, 2, 3, 1], [2, 4, 7, 3], [1, 2, 4, 2]])
            reduced, pivots = rref(A)
            print("Pivot columns:", pivots)
            display(reduced)

            basis = nullspace_basis(A)
            print("Nullspace basis vectors:")
            for vec in basis:
                display(vec)

            b = sp.Matrix([1, 3, 1])
            solution_set = sp.linsolve((A[:, :3], b))
            print("Sample complete solution structure for a 3-column slice:")
            display(solution_set)
            """
        ).strip(),
    },
    {
        "filename": "week04_ch04_orthogonality.ipynb",
        "title": "Week 4 - Chapter 4: Orthogonality and Least Squares",
        "chapter_focus": "4.1 to 4.4",
        "topics": [
            "orthogonality of subspaces",
            "projections and least squares",
            "orthonormal basis and Gram-Schmidt",
        ],
        "exercise_plan": "Target: 8-10 review problems across 4.1 to 4.4 plus 1 challenge problem.",
        "demo_code": dedent(
            """
            a = np.array([2.0, 2.0, 1.0])
            b = np.array([3.0, 4.0, 4.0])
            projection = project_onto_vector(b, a)
            print("Projection of b onto span(a):", projection)

            X = np.array([[1.0, 0.0], [1.0, 1.0], [1.0, 2.0], [1.0, 3.0]])
            y = np.array([1.0, 2.0, 2.0, 4.0])
            coeffs = least_squares(X, y)
            print("Least-squares line coefficients:", coeffs)

            Q, R = gram_schmidt(X)
            print("Q^T Q:")
            print(np.round(Q.T @ Q, 6))
            """
        ).strip(),
    },
    {
        "filename": "week05_ch05_determinants.ipynb",
        "title": "Week 5 - Chapter 5: Determinants",
        "chapter_focus": "5.1 to 5.3",
        "topics": [
            "determinant properties",
            "cofactors and permutations",
            "Cramer's rule and volume",
        ],
        "exercise_plan": "Target: 8-9 review problems across 5.1 to 5.3 plus 1 challenge problem.",
        "demo_code": dedent(
            """
            A = sp.Matrix([[3, 1, 2], [0, 4, 5], [1, 0, 6]])
            det_elim = determinant_by_elimination(A)
            det_cofactor = cofactor_expansion(A)
            print("det by elimination =", det_elim)
            print("det by cofactor expansion =", det_cofactor)
            print("SymPy det =", A.det())
            """
        ).strip(),
    },
    {
        "filename": "week06_ch06_eigenvalues.ipynb",
        "title": "Week 6 - Chapter 6: Eigenvalues and Positive Definite Matrices",
        "chapter_focus": "6.1 to 6.5",
        "topics": [
            "eigenvalues and eigenvectors",
            "diagonalization and differential equations",
            "symmetric and positive definite matrices",
        ],
        "exercise_plan": "Target: 8-10 review problems across 6.1 to 6.5 plus 1 challenge problem.",
        "demo_code": dedent(
            """
            A = sp.Matrix([[4, 1], [2, 3]])
            eigenpairs = eigenpairs_symbolic(A)
            print("Symbolic eigenpairs:")
            for value, vectors in eigenpairs.items():
                print("eigenvalue =", value)
                for vector in vectors:
                    display(vector)

            dominant_value, dominant_vector, history = power_iteration([[4.0, 1.0], [2.0, 3.0]])
            print("Dominant eigenvalue from power iteration:", dominant_value)
            print("Dominant eigenvector:", dominant_vector)

            S = np.array([[2.0, -1.0], [-1.0, 2.0]])
            print("Is S positive definite?", is_positive_definite(S))
            """
        ).strip(),
    },
    {
        "filename": "week07_ch07_svd_pca.ipynb",
        "title": "Week 7 - Chapter 7: SVD and PCA",
        "chapter_focus": "7.1 to 7.4",
        "topics": [
            "SVD for image/data thinking",
            "rank-k approximation",
            "PCA from the SVD",
        ],
        "exercise_plan": "Target: 8-9 review problems across 7.1 to 7.4 plus 1 challenge problem.",
        "demo_code": dedent(
            """
            A = np.array(
                [
                    [3.0, 1.0, 1.0],
                    [1.0, 3.0, 1.0],
                    [1.0, 1.0, 3.0],
                ]
            )
            U_k, s_k, Vt_k, approximation = rank_k_svd(A, 2)
            print("Top singular values:", s_k)
            print("Rank-2 approximation:")
            print(np.round(approximation, 4))
            plot_singular_values(np.linalg.svd(A, compute_uv=False))
            plt.show()

            X = np.array(
                [
                    [2.0, 1.0],
                    [3.0, 2.0],
                    [4.0, 2.0],
                    [5.0, 3.0],
                ]
            )
            pca_result = pca(X, 1)
            print("Principal component:", pca_result["components"])
            print("Explained ratio:", pca_result["explained_ratio"])
            """
        ).strip(),
    },
    {
        "filename": "week08_ch08_transformations.ipynb",
        "title": "Week 8 - Chapter 8: Linear Transformations",
        "chapter_focus": "8.1 to 8.3",
        "topics": [
            "idea of a linear transformation",
            "matrix of a transformation",
            "good basis and change of basis",
        ],
        "exercise_plan": "Target: 8-9 review problems across 8.1 to 8.3 plus 1 challenge problem.",
        "demo_code": dedent(
            """
            A = np.array([[1.5, 0.5], [0.0, 1.0]])
            plot_transformation_grid(A)
            plt.show()

            points = np.array([[0.0, 0.0], [1.0, 0.0], [0.2, 1.0]])
            moved = affine_transform(points, A, offset=[0.5, -0.25])
            print("Original points:")
            print(points)
            print("Affine transformed points:")
            print(np.round(moved, 4))
            """
        ).strip(),
    },
    {
        "filename": "week09_ch09_complex_fft.ipynb",
        "title": "Week 9 - Chapter 9: Complex Numbers and FFT",
        "chapter_focus": "9.1 to 9.3",
        "topics": [
            "complex numbers",
            "Hermitian and unitary matrices",
            "DFT matrix and FFT comparison",
        ],
        "exercise_plan": "Target: 8-9 review problems across 9.1 to 9.3 plus 1 challenge problem.",
        "demo_code": dedent(
            """
            F = dft_matrix(4)
            print("F^* F:")
            print(np.round(F.conj().T @ F, 6))

            x = np.array([1.0, 2.0, 0.0, -1.0], dtype=complex)
            direct = F @ x
            fft_scaled = np.fft.fft(x) / np.sqrt(len(x))
            print("Direct DFT:", np.round(direct, 4))
            print("NumPy FFT scaled:", np.round(fft_scaled, 4))
            """
        ).strip(),
    },
    {
        "filename": "week10_ch10_applications.ipynb",
        "title": "Week 10 - Chapter 10: Applications",
        "chapter_focus": "10.1 to 10.7",
        "topics": [
            "graphs and networks",
            "Markov/PageRank and Fourier series",
            "graphics, LP, and cryptography demos",
        ],
        "exercise_plan": "Target: 8-10 review problems across 10.1 to 10.7 plus 1 challenge problem.",
        "demo_code": dedent(
            """
            edges = [(0, 1), (1, 2), (2, 0)]
            B = incidence_matrix(3, edges)
            print("Incidence matrix:")
            print(B)

            P = np.array(
                [
                    [0.0, 0.5, 1.0],
                    [1.0, 0.0, 0.0],
                    [0.0, 0.5, 0.0],
                ]
            )
            print("PageRank:", np.round(pagerank(P), 4))

            x = np.linspace(0, 2 * np.pi, 50, endpoint=False)
            y = np.sin(x) + 0.5 * np.cos(2 * x)
            fit = fourier_series_fit(x, y, n_terms=2)
            print("Fourier coefficients:", np.round(fit["coefficients"], 4))

            key = [[3, 3], [2, 5]]
            encrypted = hill_cipher_encrypt("HELP", key)
            print("Encrypted HELP ->", encrypted)
            print("Decrypted back ->", hill_cipher_decrypt(encrypted, key))

            try:
                lp_result = solve_linear_program(
                    c=[-3, -2],
                    A_ub=[[1, 1], [1, 0], [0, 1]],
                    b_ub=[4, 2, 3],
                    bounds=[(0, None), (0, None)],
                )
                print("LP solution:", np.round(lp_result.x, 4))
            except ImportError as exc:
                print(exc)
            """
        ).strip(),
    },
    {
        "filename": "week11_ch11_numerical_la.ipynb",
        "title": "Week 11 - Chapter 11: Numerical Linear Algebra",
        "chapter_focus": "11.1 to 11.3",
        "topics": [
            "practical elimination",
            "norms and condition numbers",
            "iterative methods and preconditioners",
        ],
        "exercise_plan": "Target: 8-9 review problems across 11.1 to 11.3 plus 1 challenge problem.",
        "demo_code": dedent(
            """
            A = np.array([[4.0, 1.0], [1.0, 3.0]])
            b = np.array([1.0, 2.0])
            print("Condition number:", condition_number(A))

            x_jacobi, jacobi_history = jacobi_method(A, b, max_iter=50)
            x_gs, gs_history = gauss_seidel(A, b, max_iter=50)
            exact = np.linalg.solve(A, b)

            print("Jacobi solution:", np.round(x_jacobi, 6))
            print("Gauss-Seidel solution:", np.round(x_gs, 6))
            print("Exact solution:", np.round(exact, 6))
            print("Final Jacobi residual:", jacobi_history[-1])
            print("Final Gauss-Seidel residual:", gs_history[-1])
            """
        ).strip(),
    },
    {
        "filename": "week12_ch12_probability_stats.ipynb",
        "title": "Week 12 - Chapter 12: Probability and Statistics",
        "chapter_focus": "12.1 to 12.3",
        "topics": [
            "mean, variance, and covariance",
            "joint probability and Gaussian thinking",
            "weighted least squares",
        ],
        "exercise_plan": "Target: 8-9 review problems across 12.1 to 12.3 plus 1 challenge problem.",
        "demo_code": dedent(
            """
            X = np.array(
                [
                    [1.0, 2.0],
                    [2.0, 1.0],
                    [3.0, 0.0],
                    [4.0, 1.0],
                ]
            )
            cov = covariance_matrix(X)
            corr = correlation_matrix(X)
            print("Covariance matrix:")
            print(np.round(cov, 4))
            print("Correlation matrix:")
            print(np.round(corr, 4))

            plot_gaussian_contours(mean=[0.0, 0.0], cov=[[2.0, 0.8], [0.8, 1.5]])
            plt.show()

            A = np.array([[1.0, 0.0], [1.0, 1.0], [1.0, 2.0], [1.0, 3.0]])
            b = np.array([1.0, 2.0, 2.0, 4.0])
            weights = np.array([1.0, 2.0, 2.0, 1.0])
            print("Weighted least-squares coefficients:", np.round(weighted_least_squares(A, b, weights), 4))
            """
        ).strip(),
    },
]


FINAL_REVISION = {
    "filename": "final_revision.ipynb",
    "title": "Final Revision - Strang Linear Algebra Full Track",
    "chapter_focus": "Chapters 1 to 12",
    "topics": [
        "core formulas and mental models",
        "library cross-checks",
        "final self-test",
    ],
    "exercise_plan": "Target: revisit weak chapters, solve 1 challenge from an early chapter and 1 from a later chapter.",
    "demo_code": dedent(
        """
        A = sp.Matrix([[2, 1], [1, 3]])
        print("RREF:")
        display(rref(A)[0])

        P, L, U = lu_factor(A)
        print("LU check:", sp.simplify(P * A - L * U) == sp.zeros(*A.shape))

        eigval, eigvec, _ = power_iteration([[4.0, 1.0], [2.0, 3.0]])
        print("Dominant eigenvalue:", eigval)

        X = np.array([[2.0, 1.0], [3.0, 2.0], [4.0, 2.0], [5.0, 3.0]])
        print("Top PCA component:")
        print(pca(X, 1)["components"])

        print("PageRank check:")
        print(pagerank([[0.0, 1.0], [1.0, 0.0]]))
        """
    ).strip(),
}


def build_notebook(title: str, chapter_focus: str, topics, exercise_plan: str, demo_code: str) -> dict:
    markdown_intro = f"""
    # {title}

    **Chapter focus:** {chapter_focus}

    This notebook is part of the 12-week Strang plan. Language simple Hinglish me rakhi gayi hai, but code and math notation standard form me hai.

    **This week ke main topics**
    - {topics[0]}
    - {topics[1]}
    - {topics[2]}
    """

    markdown_flow = f"""
    ## Study Flow

    1. Day 1: chapter reading + key definitions
    2. Day 2: worked examples by hand
    3. Day 3: textbook exercises
    4. Day 4: Python implementation part 1
    5. Day 5: Python implementation part 2
    6. Day 6: recap + mistakes review + short quiz

    **Exercise plan**
    - {exercise_plan}
    - Do not copy problem statements here; use the local PDF and note only problem numbers in your own log.
    """

    markdown_notes = """
    ## Reading Notes

    Write short notes here after reading:
    - Definition 1:
    - Definition 2:
    - One thing that felt confusing:
    - One visual intuition:

    ## Worked Examples

    Solve 2-3 examples by hand before you run the code below.
    """

    markdown_recap = """
    ## Recap and Self-Check

    Fill this after the session:
    - Can I explain the main theorem/result in my own words?
    - Can I do one problem without looking at notes?
    - Which mistake repeated today?
    - What should I revise tomorrow?
    """

    notebook = {
        "cells": [
            markdown_cell(markdown_intro),
            markdown_cell(markdown_flow),
            code_cell(SETUP_CODE),
            markdown_cell(markdown_notes),
            code_cell(demo_code),
            markdown_cell(markdown_recap),
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
                "version": "3.9",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    return notebook


def main() -> None:
    NOTEBOOK_DIR.mkdir(parents=True, exist_ok=True)
    for week in WEEK_DATA + [FINAL_REVISION]:
        notebook = build_notebook(
            title=week["title"],
            chapter_focus=week["chapter_focus"],
            topics=week["topics"],
            exercise_plan=week["exercise_plan"],
            demo_code=week["demo_code"],
        )
        target = NOTEBOOK_DIR / week["filename"]
        target.write_text(json.dumps(notebook, indent=2))
        print(f"Wrote {target.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
