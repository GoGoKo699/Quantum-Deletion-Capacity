# Finite verification

These deterministic checks verify finite instances of the Kraus Gram identity and its scalar spectral reduction in [Alignment geometry and the Choi spectrum](../science/alignment-spectrum.md). They use two separate direct constructions of deletion Kraus operators. Neither construction uses the graph decomposition to produce its matrices.

## Run

Install the single dependency once:

```bash
python -m pip install -r verification/requirements.txt
```

Then run all checks from the repository root:

```bash
python verification/run_all.py
```

The script prints a JSON report with `"status": "passed"`, the Python and NumPy versions, tolerances, and all measured values. A failed assertion or changed reference value produces a nonzero exit status. The reference file is resolved relative to the script, so invoking the script by its absolute path from another directory also works. No network access or random seed is needed for the checks.

## What is checked

`direct_kraus_blocks.py` enumerates the input basis and builds each deletion Kraus matrix. Its eight cases are listed as $`(d,n,k)`$:

| Local dimension $`d`$ | Input length $`n`$ | Deleted count $`k`$ |
|---|---|---|
| 2 | 1 | 0 |
| 2 | 1 | 1 |
| 2 | 3 | 0 |
| 2 | 3 | 3 |
| 2 | 3 | 1 |
| 2 | 4 | 2 |
| 2 | 5 | 2 |
| 3 | 4 | 2 |

For every case, it checks that the normalized Gram matrix has trace one, that every appropriately scaled deletion-set block is a permutation matrix, and that the top Gram eigenvalue equals the top scalar-alignment eigenvalue divided by $`d^k\binom nk`$. The cases include identity transmission, deletion of the whole string, single deletion, multiple deletions, and qutrit carriers. The maximum scalar row sum is also recorded.

`independent_contraction.py` constructs normalized vectorized Kraus operators by inserting independently enumerated deleted and surviving words into their input positions. For $`(d,n,k)=(2,6,2)`$ it checks all 225 deletion-set blocks. It records their failure count, the trace, the spectral norm, and the maximum Gram row sum.

The same script preserves five scalar row-sum enumerations for qubits: $`(n,k)=(4,1),(6,2),(8,3),(10,4),(14,3)`$. It records each exact enumerated maximum, one maximizing survivor set, and the analytic upper bound $`48^k`$. The displayed survivor positions use zero-based indexing. These finite rows are consistency checks of the stated kernel and bound.

## Tolerances and reference values

Structural checks use absolute tolerance $`10^{-12}`$; the independent block checks set relative tolerance to zero. `expected-results.json` retains the previously observed numerical values. The runner compares floating-point reference values with absolute and relative tolerances both equal to $`10^{-12}`$. Integers, case lists, and maximizing survivor indices must agree exactly. The two construction scripts preserve their separate implementations.

The reference values include the independent six-qubit result: zero failed blocks, trace one to floating-point precision, spectral norm approximately `0.07390772826905823`, and maximum Gram row sum approximately `0.084375`. The complete values and tolerances are in the JSON file. The package was reproduced with Python 3.12.14 and NumPy 2.3.5. Last-bit differences between numerical libraries are allowed by the declared tolerances.

## Scope

The checks address normalization, deleted-coordinate permutations, small-instance spectra, and the listed finite row sums. The proof of the uniform row bound, the channel comparison, and the small-deletion capacity law is analytical. These scripts do not prove those asymptotic statements, establish an optimal value of $`C_d`$, construct an efficient decoder, or measure communication performance. No randomized coding simulation is included.
