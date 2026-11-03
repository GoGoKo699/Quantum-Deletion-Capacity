"""Independent Kraus-vector construction and finite scalar-row enumeration.

The Kraus vectors are constructed by placing deleted and surviving words into
their positions. This code does not import the matrix-construction script.
"""

import itertools
import json
import math

import numpy as np


ROW_CASES = ((4, 1), (6, 2), (8, 3), (10, 4), (14, 3))


def run(tolerance=1e-12):
    rows = []
    for n, k in ROW_CASES:
        survivors = np.array(
            list(itertools.combinations(range(n), n - k)), dtype=np.int16
        )
        maximum = 0.0
        argmax = None
        for start in range(0, len(survivors), 128):
            q = (
                survivors[start : start + 128, None, :] != survivors[None, :, :]
            ).sum(axis=2)
            sums = np.sum(2.0 ** (-q), axis=1)
            index = int(np.argmax(sums))
            if sums[index] > maximum:
                maximum = float(sums[index])
                argmax = [int(value) for value in survivors[start + index]]
        rows.append(
            {
                "n": n,
                "k": k,
                "d": 2,
                "row_max": maximum,
                "crude_bound": 48**k,
                "survivor_argmax": argmax,
            }
        )

    n, k, d = 6, 2, 2
    m = n - k
    input_dimension = d**n
    number_of_sets = math.comb(n, k)
    deletion_sets = list(itertools.combinations(range(n), k))
    vectors = []
    for deleted in deletion_sets:
        surviving = [i for i in range(n) if i not in deleted]
        for deleted_word in itertools.product(range(d), repeat=k):
            vector = np.zeros(input_dimension * d**m, dtype=np.float64)
            for surviving_word in itertools.product(range(d), repeat=m):
                inputs = [None] * n
                for position, value in zip(deleted, deleted_word):
                    inputs[position] = value
                for position, value in zip(surviving, surviving_word):
                    inputs[position] = value
                input_index = sum(
                    value * d ** (n - 1 - i) for i, value in enumerate(inputs)
                )
                output_index = sum(
                    value * d ** (m - 1 - i)
                    for i, value in enumerate(surviving_word)
                )
                vector[output_index * input_dimension + input_index] = 1.0 / math.sqrt(
                    input_dimension * number_of_sets
                )
            vectors.append(vector)

    vectors = np.array(vectors, dtype=np.float64)
    gram = vectors @ vectors.T
    bad_blocks = 0
    for i, deleted_left in enumerate(deletion_sets):
        x = [position for position in range(n) if position not in deleted_left]
        for j, deleted_right in enumerate(deletion_sets):
            y = [position for position in range(n) if position not in deleted_right]
            q = sum(a != b for a, b in zip(x, y))
            block = gram[
                i * d**k : (i + 1) * d**k,
                j * d**k : (j + 1) * d**k,
            ]
            scaled = block * number_of_sets * d ** (k + q)
            good = (
                np.allclose(scaled, scaled.round(), atol=tolerance, rtol=0.0)
                and np.allclose(scaled.sum(axis=0), 1.0, atol=tolerance, rtol=0.0)
                and np.allclose(scaled.sum(axis=1), 1.0, atol=tolerance, rtol=0.0)
            )
            bad_blocks += int(not good)

    if bad_blocks:
        raise AssertionError(f"{bad_blocks} of the 225 independent Gram blocks failed")

    return {
        "scalar_rows": rows,
        "direct_kraus_check": {
            "n": n,
            "k": k,
            "d": d,
            "blocks_inspected": len(deletion_sets) ** 2,
            "bad_blocks": bad_blocks,
            "trace": float(np.trace(gram)),
            "spectral_norm": float(np.linalg.eigvalsh(gram)[-1]),
            "maximum_row_sum": float(np.max(gram.sum(axis=1))),
        },
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
