"""Symbolic linear algebra helpers built on top of SymPy."""

from __future__ import annotations

from typing import Dict, List, Optional, Sequence, Tuple, Union

import sympy as sp

MatrixLike = Union[sp.MatrixBase, Sequence[Sequence[object]], Sequence[object]]


def to_sympy_matrix(data: MatrixLike) -> sp.Matrix:
    """Convert a nested sequence or SymPy matrix into a SymPy Matrix."""
    if isinstance(data, sp.MatrixBase):
        return sp.Matrix(data)
    return sp.Matrix(data)


def _split_augmented(augmented: sp.Matrix, num_columns: int) -> Tuple[sp.Matrix, Optional[sp.Matrix]]:
    if augmented.cols == num_columns:
        return augmented[:, :num_columns], None
    return augmented[:, :num_columns], augmented[:, num_columns:]


def gaussian_elimination_steps(
    A: MatrixLike,
    b: Optional[MatrixLike] = None,
) -> List[Dict[str, object]]:
    """Return forward-elimination snapshots for A or the augmented system [A | b]."""
    matrix = to_sympy_matrix(A)
    if b is not None:
        rhs = to_sympy_matrix(b)
        if rhs.rows != matrix.rows:
            raise ValueError("A and b must have the same number of rows.")
        if rhs.cols == 0:
            raise ValueError("b cannot be empty.")
        augmented = matrix.row_join(rhs)
    else:
        augmented = matrix.copy()

    steps: List[Dict[str, object]] = []

    def record(operation: str) -> None:
        current_a, current_b = _split_augmented(augmented.copy(), matrix.cols)
        steps.append(
            {
                "operation": operation,
                "A": current_a,
                "b": current_b,
            }
        )

    record("Start")

    pivot_row = 0
    for pivot_col in range(matrix.cols):
        if pivot_row >= matrix.rows:
            break

        pivot_candidate = None
        for row in range(pivot_row, matrix.rows):
            if sp.simplify(augmented[row, pivot_col]) != 0:
                pivot_candidate = row
                break

        if pivot_candidate is None:
            continue

        if pivot_candidate != pivot_row:
            augmented.row_swap(pivot_row, pivot_candidate)
            record(f"Swap R{pivot_row + 1} <-> R{pivot_candidate + 1}")

        pivot_value = augmented[pivot_row, pivot_col]
        for row in range(pivot_row + 1, matrix.rows):
            below = augmented[row, pivot_col]
            if sp.simplify(below) == 0:
                continue
            factor = sp.simplify(below / pivot_value)
            augmented.row_op(
                row,
                lambda value, col: sp.simplify(value - factor * augmented[pivot_row, col]),
            )
            record(f"R{row + 1} <- R{row + 1} - ({sp.sstr(factor)}) * R{pivot_row + 1}")

        pivot_row += 1

    return steps


def rref(A: MatrixLike) -> Tuple[sp.Matrix, Tuple[int, ...]]:
    """Return the reduced row echelon form and pivot columns."""
    return to_sympy_matrix(A).rref()


def nullspace_basis(A: MatrixLike) -> List[sp.Matrix]:
    """Return a basis for the nullspace of A."""
    return to_sympy_matrix(A).nullspace()


def lu_factor(A: MatrixLike) -> Tuple[sp.Matrix, sp.Matrix, sp.Matrix]:
    """Return P, L, U so that P * A = L * U."""
    matrix = to_sympy_matrix(A)
    if matrix.rows != matrix.cols:
        raise ValueError("LU factorization requires a square matrix.")

    n = matrix.rows
    U = matrix.copy()
    L = sp.eye(n)
    P = sp.eye(n)

    for pivot_col in range(n):
        pivot_row = None
        for row in range(pivot_col, n):
            if sp.simplify(U[row, pivot_col]) != 0:
                pivot_row = row
                break

        if pivot_row is None:
            raise ValueError("Matrix is singular; LU factorization without zero pivots failed.")

        if pivot_row != pivot_col:
            U.row_swap(pivot_col, pivot_row)
            P.row_swap(pivot_col, pivot_row)
            if pivot_col > 0:
                for col in range(pivot_col):
                    L[pivot_col, col], L[pivot_row, col] = L[pivot_row, col], L[pivot_col, col]

        pivot_value = U[pivot_col, pivot_col]
        for row in range(pivot_col + 1, n):
            factor = sp.simplify(U[row, pivot_col] / pivot_value)
            L[row, pivot_col] = factor
            U.row_op(
                row,
                lambda value, col: sp.simplify(value - factor * U[pivot_col, col]),
            )

    return P, L, U


def determinant_by_elimination(A: MatrixLike) -> sp.Expr:
    """Compute det(A) using elimination, keeping track of row swaps."""
    matrix = to_sympy_matrix(A)
    if matrix.rows != matrix.cols:
        raise ValueError("Determinant requires a square matrix.")

    U = matrix.copy()
    swaps = 0
    n = U.rows

    for pivot_col in range(n):
        pivot_row = None
        for row in range(pivot_col, n):
            if sp.simplify(U[row, pivot_col]) != 0:
                pivot_row = row
                break
        if pivot_row is None:
            return sp.Integer(0)
        if pivot_row != pivot_col:
            U.row_swap(pivot_col, pivot_row)
            swaps += 1

        pivot_value = U[pivot_col, pivot_col]
        for row in range(pivot_col + 1, n):
            if sp.simplify(U[row, pivot_col]) == 0:
                continue
            factor = sp.simplify(U[row, pivot_col] / pivot_value)
            U.row_op(
                row,
                lambda value, col: sp.simplify(value - factor * U[pivot_col, col]),
            )

    determinant = sp.Integer(-1) ** swaps
    for i in range(n):
        determinant *= sp.simplify(U[i, i])
    return sp.simplify(determinant)


def cofactor_expansion(A: MatrixLike) -> sp.Expr:
    """Compute det(A) recursively by cofactor expansion."""
    matrix = to_sympy_matrix(A)
    if matrix.rows != matrix.cols:
        raise ValueError("Determinant requires a square matrix.")
    if matrix.rows == 1:
        return matrix[0, 0]
    if matrix.rows == 2:
        return sp.simplify(matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0])

    determinant = sp.Integer(0)
    for col in range(matrix.cols):
        minor = matrix.minor_submatrix(0, col)
        determinant += ((-1) ** col) * matrix[0, col] * cofactor_expansion(minor)
    return sp.simplify(determinant)


def inverse_gauss_jordan(A: MatrixLike) -> sp.Matrix:
    """Invert A using SymPy's Gauss-Jordan based inverse routine."""
    matrix = to_sympy_matrix(A)
    if matrix.rows != matrix.cols:
        raise ValueError("Inverse requires a square matrix.")
    return matrix.inv(method="GE")


def eigenpairs_symbolic(A: MatrixLike) -> Dict[sp.Expr, List[sp.Matrix]]:
    """Return a dictionary of eigenvalue -> list of eigenvectors."""
    matrix = to_sympy_matrix(A)
    if matrix.rows != matrix.cols:
        raise ValueError("Eigenvalues require a square matrix.")

    result: Dict[sp.Expr, List[sp.Matrix]] = {}
    for eigenvalue, _, eigenvectors in matrix.eigenvects():
        result[sp.simplify(eigenvalue)] = [sp.Matrix(vector) for vector in eigenvectors]
    return result
