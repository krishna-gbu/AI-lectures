import numpy as np
import sympy as sp

from strang_la import (
    cofactor_expansion,
    condition_number,
    correlation_matrix,
    covariance_matrix,
    determinant_by_elimination,
    dft_matrix,
    eigenpairs_symbolic,
    gauss_seidel,
    gaussian_elimination_steps,
    gram_schmidt,
    hill_cipher_decrypt,
    hill_cipher_encrypt,
    incidence_matrix,
    is_positive_definite,
    jacobi_method,
    least_squares,
    lu_factor,
    nullspace_basis,
    pagerank,
    pca,
    power_iteration,
    rank_k_svd,
    rref,
    weighted_least_squares,
)


def test_gaussian_elimination_steps_returns_upper_triangular_end_state():
    steps = gaussian_elimination_steps([[2, 1], [4, 5]], [[1], [2]])
    final_a = steps[-1]["A"]
    assert final_a[1, 0] == 0


def test_rref_and_nullspace_basis():
    matrix = [[1, 2, 3], [2, 4, 6]]
    reduced, pivots = rref(matrix)
    basis = nullspace_basis(matrix)
    assert pivots == (0,)
    assert reduced.rank() == 1
    assert len(basis) == 2


def test_lu_factorization():
    A = sp.Matrix([[2, 1], [4, 5]])
    P, L, U = lu_factor(A)
    assert P * A == L * U
    assert L[0, 0] == 1 and L[1, 1] == 1


def test_determinants_agree():
    A = [[3, 1, 2], [0, 4, 5], [1, 0, 6]]
    assert determinant_by_elimination(A) == cofactor_expansion(A)


def test_eigenpairs_symbolic_contains_expected_values():
    eigenpairs = eigenpairs_symbolic([[2, 0], [0, 3]])
    assert set(eigenpairs.keys()) == {sp.Integer(2), sp.Integer(3)}


def test_least_squares_matches_numpy():
    A = np.array([[1.0, 1.0], [1.0, 2.0], [1.0, 3.0]])
    b = np.array([1.0, 2.0, 2.0])
    x = least_squares(A, b)
    expected, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
    assert np.allclose(x, expected)


def test_gram_schmidt_builds_qr():
    A = np.array([[1.0, 1.0], [1.0, -1.0]])
    Q, R = gram_schmidt(A)
    assert np.allclose(Q.T @ Q, np.eye(2))
    assert np.allclose(Q @ R, A)


def test_power_iteration_finds_dominant_eigenvalue():
    eigenvalue, eigenvector, history = power_iteration([[4.0, 0.0], [0.0, 2.0]])
    assert abs(eigenvalue - 4.0) < 1e-6
    assert np.isclose(np.linalg.norm(eigenvector), 1.0)
    assert len(history) >= 1


def test_rank_k_svd_and_pca_shapes():
    A = np.array([[3.0, 1.0], [1.0, 3.0], [0.0, 2.0]])
    U_k, s_k, Vt_k, approximation = rank_k_svd(A, 1)
    result = pca(A, 1)
    assert U_k.shape == (3, 1)
    assert s_k.shape == (1,)
    assert Vt_k.shape == (1, 2)
    assert approximation.shape == A.shape
    assert result["components"].shape == (1, 2)


def test_dft_matrix_is_unitary():
    F = dft_matrix(4)
    assert np.allclose(F.conj().T @ F, np.eye(4))


def test_iterative_methods_and_condition_number():
    A = np.array([[4.0, 1.0], [1.0, 3.0]])
    b = np.array([1.0, 2.0])
    x_j, _ = jacobi_method(A, b, max_iter=200)
    x_gs, _ = gauss_seidel(A, b, max_iter=200)
    expected = np.linalg.solve(A, b)
    assert np.allclose(x_j, expected, atol=1e-6)
    assert np.allclose(x_gs, expected, atol=1e-6)
    assert condition_number(A) >= 1.0
    assert is_positive_definite(A)


def test_applications_helpers():
    edges = [(0, 1), (1, 2)]
    incidence = incidence_matrix(3, edges)
    assert incidence.shape == (2, 3)

    transition = np.array(
        [
            [0.0, 0.5, 1.0],
            [1.0, 0.0, 0.0],
            [0.0, 0.5, 0.0],
        ]
    )
    ranks = pagerank(transition)
    assert np.isclose(ranks.sum(), 1.0)


def test_statistics_and_weighted_least_squares():
    X = np.array([[1.0, 2.0], [2.0, 1.0], [3.0, 0.0]])
    cov = covariance_matrix(X)
    corr = correlation_matrix(X)
    assert cov.shape == (2, 2)
    assert corr.shape == (2, 2)

    A = np.array([[1.0, 0.0], [1.0, 1.0], [1.0, 2.0]])
    b = np.array([1.0, 2.0, 2.5])
    weights = np.array([1.0, 2.0, 1.0])
    x = weighted_least_squares(A, b, weights)
    assert x.shape == (2,)


def test_hill_cipher_round_trip():
    key = [[3, 3], [2, 5]]
    text = "HELP"
    encrypted = hill_cipher_encrypt(text, key)
    decrypted = hill_cipher_decrypt(encrypted, key)
    assert decrypted.startswith(text)
