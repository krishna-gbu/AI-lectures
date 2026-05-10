# Strang Linear Algebra

This project is a full study track for **Gilbert Strang - Introduction to Linear Algebra (5th edition)**.

Goal simple hai:
- book ko chapter-by-chapter finish karna
- har major topic ko Python me implement karna
- notebooks ke through theory + code + practice ek jagah rakhna

Language simple Hinglish hai. Code standard English me hai.

## Source Book

Main PDF yahan hai:

- `../unread-notes/Ed 5, Gilbert Strang - Introduction to Linear Algebra (2016, Wellesley-Cambridge Press).pdf`

## Project Structure

- `notebooks/`
  Weekly study notebooks. Week 1 se Week 12 tak, plus final revision notebook.
- `src/strang_la/`
  Reusable Python functions.
- `tests/`
  Basic tests for the main APIs.
- `tools/generate_notebooks.py`
  Notebook generator. Agar template change karna ho to isko run karo.
- `tools/extract_more_images.py`
  PDF se additional page images extract karta hai (pdftoppm use karta hai). Output: `hinglish-notes/assets/strang/`.
- `tools/build_strang_visual_galleries.py`
  Har chapter ke liye visual gallery markdown files generate karta hai (`hinglish-notes/visuals/`).

## Install

Project root se:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Open the Project

```bash
source .venv/bin/activate
jupyter notebook
```

Then `notebooks/` folder kholo.

## Hinglish Notes

PDF ka chapter-wise Hinglish conversion yahan hai:

- `hinglish-notes/Strang-Linear-Algebra-Hinglish-Notes.md`
- `hinglish-notes/chapters/`
- `hinglish-notes/visuals/`

Raw chapter-wise text extracts yahan hain:

- `chapter-extracts/`

## What To Do First

If you are starting today, do only this:

1. Open `notebooks/week01_ch01_vectors.ipynb`
2. Read `hinglish-notes/chapters/01-introduction-to-vectors.md` — sections 1.1, 1.2, 1.3 (PDF kholne ki zaroorat nahi, notes self-sufficient hain)
3. Fill the `Reading Notes` section in the notebook
4. Solve 2-3 examples by hand
5. Run the code cells
6. Fill the `Recap and Self-Check` section

That is enough for Day 1.

## Weekly Order

Study in this order only:

1. `week01_ch01_vectors.ipynb`
2. `week02_ch02_elimination.ipynb`
3. `week03_ch03_vector_spaces.ipynb`
4. `week04_ch04_orthogonality.ipynb`
5. `week05_ch05_determinants.ipynb`
6. `week06_ch06_eigenvalues.ipynb`
7. `week07_ch07_svd_pca.ipynb`
8. `week08_ch08_transformations.ipynb`
9. `week09_ch09_complex_fft.ipynb`
10. `week10_ch10_applications.ipynb`
11. `week11_ch11_numerical_la.ipynb`
12. `week12_ch12_probability_stats.ipynb`
13. `final_revision.ipynb`

## Weekly Workflow

Har week same process follow karo:

1. Read the chapter Hinglish notes from `hinglish-notes/chapters/` (PDF nahi kholna — notes me sab kuch hai: examples, proofs, images)
2. Write short definitions and key ideas in the notebook
3. Do 2-3 worked examples by hand
4. Solve `8-12` textbook problems
5. Run notebook code cells
6. Compare result with library or notebook output
7. Write recap and mistake log

## Day-by-Day Flow

Har week ka suggested split:

1. Day 1: chapter reading + definitions
2. Day 2: examples by hand
3. Day 3: exercises
4. Day 4: Python implementation part 1
5. Day 5: Python implementation part 2
6. Day 6: revision + short self-test

## Chapter Mapping

- Week 1: Chapter 1, vectors, dot products, matrix intro, `Ax=b`
- Week 2: Chapter 2, elimination, inverse, LU, transpose, permutation
- Week 3: Chapter 3, vector spaces, nullspace, basis, dimension
- Week 4: Chapter 4, orthogonality, projections, least squares, Gram-Schmidt
- Week 5: Chapter 5, determinants, cofactors, Cramer's rule
- Week 6: Chapter 6, eigenvalues, diagonalization, symmetric and positive definite matrices
- Week 7: Chapter 7, SVD, rank-k approximation, PCA
- Week 8: Chapter 8, linear transformations and basis change
- Week 9: Chapter 9, complex numbers, unitary matrices, FFT
- Week 10: Chapter 10, applications like graphs, PageRank, Fourier series, graphics, cryptography
- Week 11: Chapter 11, numerical linear algebra, condition numbers, iterative methods
- Week 12: Chapter 12, covariance, Gaussian, weighted least squares

## Main Python Modules

### `src/strang_la/symbolic.py`

Use this for SymPy-based exact algebra:

- `gaussian_elimination_steps(A, b=None)`
- `rref(A)`
- `nullspace_basis(A)`
- `lu_factor(A)`
- `determinant_by_elimination(A)`
- `cofactor_expansion(A)`
- `inverse_gauss_jordan(A)`
- `eigenpairs_symbolic(A)`

### `src/strang_la/numeric.py`

Use this for NumPy-based numerical work:

- `least_squares(A, b)`
- `gram_schmidt(A)`
- `power_iteration(A)`
- `rank_k_svd(A, k)`
- `pca(X, k)`
- `dft_matrix(n)`
- `jacobi_method(A, b)`
- `gauss_seidel(A, b)`
- `condition_number(A)`
- `is_positive_definite(A)`

### `src/strang_la/applications.py`

Use this for applied demos:

- `pagerank(P)`
- `incidence_matrix(num_nodes, edges)`
- `covariance_matrix(X)`
- `correlation_matrix(X)`
- `weighted_least_squares(A, b, weights)`
- `fourier_series_fit(x, y, n_terms)`
- `affine_transform(points, A, offset=None)`
- `hill_cipher_encrypt(text, key)`
- `hill_cipher_decrypt(text, key)`
- `solve_linear_program(...)`

## Validation

Run tests:

```bash
pytest
```

Regenerate notebooks:

```bash
python tools/generate_notebooks.py
```

## If Something Breaks

If notebook imports fail:

```bash
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

If you changed notebook templates:

```bash
python tools/generate_notebooks.py
```

If you want to re-check code:

```bash
pytest
```

## Minimum Rule

Do not jump randomly between topics.

Finish in this order:
- read chapter
- write notes
- solve by hand
- run code
- revise

That is the whole system.
