"""Finite checks from explicit deletion Kraus matrices.

The input basis is enumerated directly. No path decomposition is used to
construct the matrices or their Gram matrix.
"""

import json
from itertools import combinations, product
from math import comb

import numpy as np


CASES = (
    (2, 1, 0),
    (2, 1, 1),
    (2, 3, 0),
    (2, 3, 3),
    (2, 3, 1),
    (2, 4, 2),
    (2, 5, 2),
    (3, 4, 2),
)


def run(tolerance=1e-12):
    """Return the eight previously specified (d, n, k) checks."""
    reports = []
    for d, n, k in CASES:
        deletion_sets = list(combinations(range(n), k))
        deleted_words = list(product(range(d), repeat=k))
        input_words = list(product(range(d), repeat=n))
        m = n - k
        kraus = []
        survivors = []

        for deleted in deletion_sets:
            remaining = [i for i in range(n) if i not in deleted]
            survivors.append(remaining)
            for word in deleted_words:
                matrix = np.zeros((d**m, d**n), dtype=np.float64)
                for column, inputs in enumerate(input_words):
                    if tuple(inputs[i] for i in deleted) == word:
                        row = sum(
                            inputs[i] * d ** (m - 1 - rank)
                            for rank, i in enumerate(remaining)
                        )
                        matrix[row, column] = 1.0
                kraus.append(matrix)

        gram = np.array(
            [[np.vdot(left, right) for right in kraus] for left in kraus],
            dtype=np.float64,
        ) / (d**n * comb(n, k))
        scalar = np.array(
            [
                [d ** (-sum(a != b for a, b in zip(x, y))) for y in survivors]
                for x in survivors
            ],
            dtype=np.float64,
        )

        permutation_error = 0.0
        for i, x in enumerate(survivors):
            for j, y in enumerate(survivors):
                q = sum(a != b for a, b in zip(x, y))
                scale = d ** (-k - q) / comb(n, k)
                block = gram[
                    i * d**k : (i + 1) * d**k,
                    j * d**k : (j + 1) * d**k,
                ] / scale
                permutation_error = max(
                    permutation_error,
                    float(np.max(np.abs(block.sum(axis=0) - 1.0))),
                    float(np.max(np.abs(block.sum(axis=1) - 1.0))),
                    float(np.max(np.abs(block - np.round(block)))),
                )

        gram_top = float(np.linalg.eigvalsh(gram)[-1])
        scalar_top = float(np.linalg.eigvalsh(scalar)[-1] / (d**k * comb(n, k)))
        trace = float(np.trace(gram))
        top_difference = abs(gram_top - scalar_top)
        case = f"d={d}, n={n}, k={k}"
        if permutation_error >= tolerance:
            raise AssertionError(f"Permutation-block check failed for {case}")
        if abs(trace - 1.0) >= tolerance:
            raise AssertionError(f"Trace normalization failed for {case}")
        if top_difference >= tolerance:
            raise AssertionError(f"Scalar spectral reduction failed for {case}")

        reports.append(
            {
                "d": d,
                "n": n,
                "k": k,
                "trace": trace,
                "permutation_error": permutation_error,
                "gram_top": gram_top,
                "scalar_top": scalar_top,
                "top_difference": top_difference,
                "maximum_scalar_row_sum": float(scalar.sum(axis=1).max()),
            }
        )
    return reports


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
