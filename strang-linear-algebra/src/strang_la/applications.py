"""Applied linear algebra demos used in later study notebooks."""

from __future__ import annotations

import string
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np
import sympy as sp

from .numeric import least_squares, to_numpy_array


def incidence_matrix(num_nodes: int, edges: Sequence[Tuple[int, int]]) -> np.ndarray:
    """Build the edge-node incidence matrix for a directed graph."""
    matrix = np.zeros((len(edges), num_nodes), dtype=float)
    for row, (start, end) in enumerate(edges):
        matrix[row, start] = -1.0
        matrix[row, end] = 1.0
    return matrix


def pagerank(
    P: Sequence[Sequence[float]],
    damping: float = 0.85,
    tol: float = 1e-10,
    max_iter: int = 200,
) -> np.ndarray:
    """Compute PageRank from a column-stochastic transition matrix."""
    matrix = to_numpy_array(P, dtype=float)
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("P must be a square matrix.")

    column_sums = matrix.sum(axis=0)
    fixed = matrix.copy()
    n = fixed.shape[0]
    for col in range(n):
        if np.isclose(column_sums[col], 0.0):
            fixed[:, col] = 1.0 / n
        else:
            fixed[:, col] = fixed[:, col] / column_sums[col]

    rank = np.full(n, 1.0 / n)
    teleport = np.full(n, (1.0 - damping) / n)
    for _ in range(max_iter):
        next_rank = damping * (fixed @ rank) + teleport
        if np.linalg.norm(next_rank - rank, ord=1) < tol:
            rank = next_rank
            break
        rank = next_rank
    return rank / rank.sum()


def covariance_matrix(X: Sequence[Sequence[float]], bias: bool = False) -> np.ndarray:
    """Return the covariance matrix for row-wise observations."""
    X_arr = to_numpy_array(X, dtype=float)
    return np.cov(X_arr, rowvar=False, bias=bias)


def correlation_matrix(X: Sequence[Sequence[float]]) -> np.ndarray:
    """Return the correlation matrix for row-wise observations."""
    X_arr = to_numpy_array(X, dtype=float)
    return np.corrcoef(X_arr, rowvar=False)


def weighted_least_squares(
    A: Sequence[Sequence[float]],
    b: Sequence[float],
    weights: Sequence[float],
) -> np.ndarray:
    """Solve weighted least squares via normal equations."""
    A_arr = to_numpy_array(A, dtype=float)
    b_arr = to_numpy_array(b, dtype=float)
    w_arr = to_numpy_array(weights, dtype=float)
    if A_arr.shape[0] != b_arr.shape[0] or A_arr.shape[0] != w_arr.shape[0]:
        raise ValueError("A, b, and weights must agree in their number of rows.")
    W = np.diag(w_arr)
    lhs = A_arr.T @ W @ A_arr
    rhs = A_arr.T @ W @ b_arr
    return np.linalg.solve(lhs, rhs)


def affine_transform(
    points: Sequence[Sequence[float]],
    A: Sequence[Sequence[float]],
    offset: Optional[Sequence[float]] = None,
) -> np.ndarray:
    """Apply x -> A x + offset to row-wise points."""
    pts = to_numpy_array(points, dtype=float)
    matrix = to_numpy_array(A, dtype=float)
    shift = np.zeros(matrix.shape[0]) if offset is None else to_numpy_array(offset, dtype=float)
    return (matrix @ pts.T).T + shift


def fourier_series_fit(
    x: Sequence[float],
    y: Sequence[float],
    n_terms: int,
) -> Dict[str, np.ndarray]:
    """Fit a Fourier series using linear least squares."""
    x_arr = to_numpy_array(x, dtype=float)
    y_arr = to_numpy_array(y, dtype=float)
    columns = [np.ones_like(x_arr)]
    for k in range(1, n_terms + 1):
        columns.append(np.cos(k * x_arr))
        columns.append(np.sin(k * x_arr))
    design = np.column_stack(columns)
    coeffs = least_squares(design, y_arr)
    reconstruction = design @ coeffs
    return {
        "design": design,
        "coefficients": coeffs,
        "reconstruction": reconstruction,
    }


def solve_linear_program(
    c: Sequence[float],
    A_ub: Sequence[Sequence[float]],
    b_ub: Sequence[float],
    bounds: Optional[Sequence[Tuple[Optional[float], Optional[float]]]] = None,
):
    """Solve a linear program with SciPy when available."""
    try:
        from scipy.optimize import linprog
    except ImportError as exc:
        raise ImportError("scipy is required for linear programming demos.") from exc

    return linprog(c=c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")


_ALPHABET = string.ascii_uppercase


def _clean_text(text: str) -> str:
    return "".join(ch for ch in text.upper() if ch in _ALPHABET)


def _text_to_numbers(text: str) -> List[int]:
    return [_ALPHABET.index(ch) for ch in text]


def _numbers_to_text(numbers: Iterable[int]) -> str:
    return "".join(_ALPHABET[int(number) % 26] for number in numbers)


def hill_cipher_encrypt(text: str, key: Sequence[Sequence[int]]) -> str:
    """Encrypt text using a Hill cipher key."""
    key_matrix = sp.Matrix(key)
    n = key_matrix.rows
    if key_matrix.rows != key_matrix.cols:
        raise ValueError("Hill cipher key must be square.")

    clean = _clean_text(text)
    padding = (-len(clean)) % n
    clean = clean + ("X" * padding)
    numbers = _text_to_numbers(clean)

    encrypted: List[int] = []
    for start in range(0, len(numbers), n):
        block = sp.Matrix(numbers[start : start + n])
        encoded = (key_matrix * block) % 26
        encrypted.extend(int(value) for value in encoded)
    return _numbers_to_text(encrypted)


def hill_cipher_decrypt(text: str, key: Sequence[Sequence[int]]) -> str:
    """Decrypt Hill cipher text using modular matrix inversion."""
    key_matrix = sp.Matrix(key)
    inverse = key_matrix.inv_mod(26)
    n = key_matrix.rows
    clean = _clean_text(text)
    numbers = _text_to_numbers(clean)

    decrypted: List[int] = []
    for start in range(0, len(numbers), n):
        block = sp.Matrix(numbers[start : start + n])
        decoded = (inverse * block) % 26
        decrypted.extend(int(value) for value in decoded)
    return _numbers_to_text(decrypted)
