"""Visualization helpers for notebook demos."""

from __future__ import annotations

from typing import Iterable, Optional, Sequence

import matplotlib.pyplot as plt
import numpy as np


def plot_vectors(
    vectors: Sequence[Sequence[float]],
    labels: Optional[Sequence[str]] = None,
    colors: Optional[Sequence[str]] = None,
    ax=None,
    title: Optional[str] = None,
):
    """Plot 2D vectors from the origin."""
    vectors_arr = [np.asarray(vector, dtype=float) for vector in vectors]
    if any(vector.shape != (2,) for vector in vectors_arr):
        raise ValueError("plot_vectors currently supports only 2D vectors.")

    if ax is None:
        _, ax = plt.subplots(figsize=(5, 5))

    labels = labels or [f"v{i + 1}" for i in range(len(vectors_arr))]
    colors = colors or ["tab:blue", "tab:orange", "tab:green", "tab:red"]

    limit = max(1.0, max(np.max(np.abs(vector)) for vector in vectors_arr) + 1.0)
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)
    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)

    for idx, vector in enumerate(vectors_arr):
        color = colors[idx % len(colors)]
        ax.arrow(0, 0, vector[0], vector[1], head_width=0.12, length_includes_head=True, color=color)
        ax.text(vector[0], vector[1], labels[idx], color=color)

    ax.set_title(title or "Vector picture")
    return ax


def plot_transformation_grid(A: Sequence[Sequence[float]], grid_limit: int = 2, ax=None):
    """Plot the image of a square grid under a 2x2 transformation."""
    matrix = np.asarray(A, dtype=float)
    if matrix.shape != (2, 2):
        raise ValueError("plot_transformation_grid requires a 2x2 matrix.")

    if ax is None:
        _, ax = plt.subplots(figsize=(5, 5))

    ax.set_aspect("equal")
    ax.grid(True, alpha=0.2)
    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)

    t = np.linspace(-grid_limit, grid_limit, 100)
    for c in range(-grid_limit, grid_limit + 1):
        vertical = np.vstack([np.full_like(t, c), t])
        horizontal = np.vstack([t, np.full_like(t, c)])
        transformed_vertical = matrix @ vertical
        transformed_horizontal = matrix @ horizontal
        ax.plot(transformed_vertical[0], transformed_vertical[1], color="tab:blue", alpha=0.5)
        ax.plot(transformed_horizontal[0], transformed_horizontal[1], color="tab:orange", alpha=0.5)

    transformed_basis = matrix @ np.eye(2)
    plot_vectors(transformed_basis.T, labels=["A e1", "A e2"], colors=["tab:red", "tab:green"], ax=ax)
    ax.set_title("Transformation grid")
    return ax


def plot_singular_values(singular_values: Iterable[float], ax=None):
    """Plot singular values as a scree chart."""
    values = np.asarray(list(singular_values), dtype=float)
    if ax is None:
        _, ax = plt.subplots(figsize=(6, 3))
    ax.plot(np.arange(1, len(values) + 1), values, marker="o")
    ax.set_xlabel("Index")
    ax.set_ylabel("Singular value")
    ax.set_title("Singular values")
    ax.grid(True, alpha=0.3)
    return ax


def plot_gaussian_contours(mean, cov, ax=None, grid_size: int = 200):
    """Plot contours for a 2D Gaussian distribution."""
    mean_arr = np.asarray(mean, dtype=float)
    cov_arr = np.asarray(cov, dtype=float)
    if mean_arr.shape != (2,) or cov_arr.shape != (2, 2):
        raise ValueError("plot_gaussian_contours expects mean shape (2,) and cov shape (2, 2).")

    if ax is None:
        _, ax = plt.subplots(figsize=(5, 5))

    x = np.linspace(mean_arr[0] - 4, mean_arr[0] + 4, grid_size)
    y = np.linspace(mean_arr[1] - 4, mean_arr[1] + 4, grid_size)
    X, Y = np.meshgrid(x, y)
    pos = np.dstack((X, Y))
    inv_cov = np.linalg.inv(cov_arr)
    diff = pos - mean_arr
    exponent = np.einsum("...i,ij,...j->...", diff, inv_cov, diff)
    Z = np.exp(-0.5 * exponent)

    ax.contour(X, Y, Z, levels=6)
    ax.set_title("Gaussian contours")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_aspect("equal")
    return ax
