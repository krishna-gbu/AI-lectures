"""Numeric linear algebra helpers built on top of NumPy."""

from __future__ import annotations

from typing import Dict, Optional, Sequence, Tuple, Union

import numpy as np

ArrayLike = Union[np.ndarray, Sequence[Sequence[float]], Sequence[float]]


def to_numpy_array(data: ArrayLike, dtype=float) -> np.ndarray:
    """Convert a nested sequence to a NumPy array."""
    return np.asarray(data, dtype=dtype)


def project_onto_vector(b: ArrayLike, a: ArrayLike) -> np.ndarray:
    """Project b onto the line spanned by a."""
    b_arr = to_numpy_array(b, dtype=float)
    a_arr = to_numpy_array(a, dtype=float)
    denominator = float(a_arr @ a_arr)
    if np.isclose(denominator, 0.0):
        raise ValueError("Cannot project onto the zero vector.")
    return ((b_arr @ a_arr) / denominator) * a_arr


def project_onto_subspace(A: ArrayLike, b: ArrayLike) -> np.ndarray:
    """Project b onto the column space of A."""
    A_arr = to_numpy_array(A, dtype=float)
    b_arr = to_numpy_array(b, dtype=float)
    coefficients = least_squares(A_arr, b_arr)
    return A_arr @ coefficients


def least_squares(A: ArrayLike, b: ArrayLike) -> np.ndarray:
    """Solve min_x ||Ax - b||_2 using NumPy's lstsq."""
    A_arr = to_numpy_array(A, dtype=float)
    b_arr = to_numpy_array(b, dtype=float)
    solution, _, _, _ = np.linalg.lstsq(A_arr, b_arr, rcond=None)
    return solution


def gram_schmidt(A: ArrayLike, tol: float = 1e-12) -> Tuple[np.ndarray, np.ndarray]:
    """Return Q, R using classical Gram-Schmidt on the columns of A."""
    A_arr = to_numpy_array(A, dtype=float)
    if A_arr.ndim != 2:
        raise ValueError("A must be a 2D array.")

    m, n = A_arr.shape
    Q = np.zeros((m, n), dtype=float)
    R = np.zeros((n, n), dtype=float)

    for j in range(n):
        v = A_arr[:, j].astype(float).copy()
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], v)
            v = v - R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)
        if R[j, j] < tol:
            raise ValueError("Columns are linearly dependent to within tolerance.")
        Q[:, j] = v / R[j, j]

    return Q, R


def power_iteration(
    A: ArrayLike,
    num_iter: int = 100,
    tol: float = 1e-10,
    x0: Optional[ArrayLike] = None,
) -> Tuple[float, np.ndarray, list]:
    """Return dominant eigenvalue, eigenvector, and history via power iteration."""
    A_arr = to_numpy_array(A, dtype=float)
    if A_arr.ndim != 2 or A_arr.shape[0] != A_arr.shape[1]:
        raise ValueError("A must be square.")

    n = A_arr.shape[0]
    if x0 is None:
        x = np.ones(n, dtype=float)
    else:
        x = to_numpy_array(x0, dtype=float).reshape(n)

    x = x / np.linalg.norm(x)
    eigenvalue_old = 0.0
    history = []

    for _ in range(num_iter):
        y = A_arr @ x
        norm_y = np.linalg.norm(y)
        if np.isclose(norm_y, 0.0):
            raise ValueError("Encountered zero vector during power iteration.")
        x = y / norm_y
        eigenvalue = float(x @ (A_arr @ x))
        history.append(eigenvalue)
        if abs(eigenvalue - eigenvalue_old) < tol:
            break
        eigenvalue_old = eigenvalue

    return eigenvalue, x, history


def rank_k_svd(A: ArrayLike, k: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return truncated SVD pieces and the rank-k approximation."""
    A_arr = to_numpy_array(A, dtype=float)
    U, singular_values, Vt = np.linalg.svd(A_arr, full_matrices=False)
    if k < 1 or k > min(A_arr.shape):
        raise ValueError("k must be between 1 and min(A.shape).")
    U_k = U[:, :k]
    s_k = singular_values[:k]
    Vt_k = Vt[:k, :]
    approximation = U_k @ np.diag(s_k) @ Vt_k
    return U_k, s_k, Vt_k, approximation


def pca(
    X: ArrayLike,
    k: int,
    center: bool = True,
    scale: bool = False,
) -> Dict[str, np.ndarray]:
    """Compute PCA by the SVD."""
    X_arr = to_numpy_array(X, dtype=float)
    if X_arr.ndim != 2:
        raise ValueError("X must be a 2D array.")
    if k < 1 or k > min(X_arr.shape):
        raise ValueError("k must be between 1 and min(X.shape).")

    mean = X_arr.mean(axis=0) if center else np.zeros(X_arr.shape[1])
    X_centered = X_arr - mean

    if scale:
        std = X_centered.std(axis=0, ddof=1)
        std[std == 0] = 1.0
        X_proc = X_centered / std
    else:
        std = np.ones(X_arr.shape[1])
        X_proc = X_centered

    U, s, Vt = np.linalg.svd(X_proc, full_matrices=False)
    explained_variance = (s ** 2) / max(X_arr.shape[0] - 1, 1)
    total_variance = explained_variance.sum()
    explained_ratio = explained_variance / total_variance if total_variance else explained_variance

    components = Vt[:k]
    scores = X_proc @ components.T

    return {
        "mean": mean,
        "scale": std,
        "components": components,
        "scores": scores,
        "singular_values": s[:k],
        "explained_variance": explained_variance[:k],
        "explained_ratio": explained_ratio[:k],
    }


def dft_matrix(n: int) -> np.ndarray:
    """Return the unitary DFT matrix of size n x n."""
    if n < 1:
        raise ValueError("n must be positive.")
    indices = np.arange(n)
    omega = np.exp(-2j * np.pi * np.outer(indices, indices) / n)
    return omega / np.sqrt(n)


def condition_number(A: ArrayLike) -> float:
    """Return the 2-norm condition number."""
    return float(np.linalg.cond(to_numpy_array(A, dtype=float)))


def jacobi_method(
    A: ArrayLike,
    b: ArrayLike,
    x0: Optional[ArrayLike] = None,
    max_iter: int = 100,
    tol: float = 1e-10,
) -> Tuple[np.ndarray, list]:
    """Solve Ax=b with Jacobi iteration."""
    A_arr = to_numpy_array(A, dtype=float)
    b_arr = to_numpy_array(b, dtype=float)
    n = A_arr.shape[0]
    x = np.zeros(n, dtype=float) if x0 is None else to_numpy_array(x0, dtype=float).reshape(n)
    D = np.diag(A_arr)
    if np.any(np.isclose(D, 0.0)):
        raise ValueError("Jacobi method requires nonzero diagonal entries.")
    R = A_arr - np.diagflat(D)
    history = []

    for _ in range(max_iter):
        x_new = (b_arr - R @ x) / D
        history.append(np.linalg.norm(A_arr @ x_new - b_arr))
        if np.linalg.norm(x_new - x) < tol:
            x = x_new
            break
        x = x_new

    return x, history


def gauss_seidel(
    A: ArrayLike,
    b: ArrayLike,
    x0: Optional[ArrayLike] = None,
    max_iter: int = 100,
    tol: float = 1e-10,
) -> Tuple[np.ndarray, list]:
    """Solve Ax=b with Gauss-Seidel iteration."""
    A_arr = to_numpy_array(A, dtype=float)
    b_arr = to_numpy_array(b, dtype=float)
    n = A_arr.shape[0]
    x = np.zeros(n, dtype=float) if x0 is None else to_numpy_array(x0, dtype=float).reshape(n)
    history = []

    for _ in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            if np.isclose(A_arr[i, i], 0.0):
                raise ValueError("Gauss-Seidel requires nonzero diagonal entries.")
            left = A_arr[i, :i] @ x[:i]
            right = A_arr[i, i + 1 :] @ x_old[i + 1 :]
            x[i] = (b_arr[i] - left - right) / A_arr[i, i]
        history.append(np.linalg.norm(A_arr @ x - b_arr))
        if np.linalg.norm(x - x_old) < tol:
            break

    return x, history


def is_positive_definite(A: ArrayLike, tol: float = 1e-10) -> bool:
    """Check if a symmetric matrix is positive definite."""
    A_arr = to_numpy_array(A, dtype=float)
    if not np.allclose(A_arr, A_arr.T, atol=tol):
        return False
    eigenvalues = np.linalg.eigvalsh(A_arr)
    return bool(np.all(eigenvalues > tol))
