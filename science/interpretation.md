# The cost of hidden positions

Losing a carrier and losing its position are different physical changes. An erasure flag identifies the missing tensor factor. A deletion closes the gap: the receiver knows the order of the survivors but must also cope with uncertainty about how output ranks correspond to input positions. The [model](model.md) retains this uncertainty even when sender and receiver share unrestricted entanglement.

## The positional-uncertainty term

For exactly $`k`$ uniformly chosen deletions, the number of possible patterns is $`\binom nk`$. Let $`K^*_{n,k,\epsilon}`$ be the largest achievable logical dimension at half-diamond error at most $`\epsilon`$. For fixed $`d`$, fixed $`0<\epsilon<1`$, and $`1\le k=o(n)`$, the [finite-block bounds](coding-theorems.md) give the optimal number of logical qubits as

```math
\log_2K^*_{n,k,\epsilon}
=(n-k)\log_2d-\frac12\log_2\binom nk
+O_{d,\epsilon}(k+1).
```

The first term is the information carried by the surviving dimensions. The second is half the logarithm of the number of possible alignments. This formula does not follow simply by declaring the deletion pattern a classical error label: different patterns have coherent overlaps in the channel's complementary representation. The spectral proof is what controls those overlaps for arbitrary quantum encoders.

At $`k=1`$, the alignment count is $`n`$, giving the additional loss

```math
\frac12\log_2n+O_{d,\epsilon}(1).
```

For $`1\le k=o(n)`$, the elementary bounds

```math
\left(\frac nk\right)^k
\le\binom nk
\le\left(\frac{en}{k}\right)^k
```

show that the extra loss is

```math
\frac k2\log_2\frac nk+O_{d,\epsilon}(k).
```

Here the target error $`0<\epsilon<1`$ is fixed. The exact coding statements retain the separate dependence on $`\epsilon`$ and $`1-\epsilon`$; they should be used when the target error changes with block length.

## A four-carrier alignment example

Take one deletion from four qubits. Compare the deletion patterns $`S=\{2\}`$ and $`T=\{3\}`$:

| Pattern | Surviving input positions, in output order |
|---|---|
| Delete position 2 | 1, 3, 4 |
| Delete position 3 | 1, 2, 4 |

Only the second output rank disagrees, so $`q(S,T)=1`$. In the Kraus Gram contraction, equality of the two ordered outputs ties the basis symbols at positions 2 and 3 together. The relative alignment factor is $`d^{-1}=1/2`$; with the full normalization, this Gram block is $`I_2/16`$. This is an overlap calculation in the channel representation; it does not assume that the receiver measures or knows the original basis string.

For all four single-deletion patterns, the exact complementary state is

```math
\sigma_E=\frac{T_4\otimes I_2}{8},
\qquad
T_4=
\begin{pmatrix}
1&1/2&1/4&1/8\\
1/2&1&1/2&1/4\\
1/4&1/2&1&1/2\\
1/8&1/4&1/2&1
\end{pmatrix}.
```

Nearby deletions have larger off-diagonal Gram blocks than distant deletions. The pattern-register basis vectors are orthogonal, but the complementary state is not diagonal in that basis. Replacing it by an incoherent classical pattern register would change the spectral calculation. Nevertheless, the total overlap stays bounded as $`n`$ grows: for qubits, the largest eigenvalue of the corresponding $`T_n`$ tends to 3. The normalized Choi norm is consequently of order $`1/n`$. That scaling is enough to retain the logarithmic positional penalty in the converse.

For several deletions, the deleted-symbol blocks can contain nontrivial permutations, and the single-deletion Toeplitz formula no longer applies. The [mismatch-run proof](alignment-spectrum.md) bounds all patterns at once, with a factor at most $`C_d^k`$.

## From one block to independent deletion

In a length-$`n`$ transmission with fixed deletion probability $`p`$, the deletion count concentrates near $`np`$. The binomial-pattern term becomes

```math
\frac1n\log_2\binom n{np}\longrightarrow h_2(p),
```

with an integer approximation to $`np`$ understood. The finite-block packing and converse bounds then give

```math
Q_E^{\mathrm{del}}(p;d)
=(1-p)\log_2d-\frac12h_2(p)+O_d(p)
=\log_2d-\frac p2\log_2\frac1p+O_d(p).
```

The limits are ordered: first a sequence of long codes at each fixed $`p`$, then $`p\downarrow0`$. The codebook acts on the whole input string and the receiver uses only its final length. Treating independently decoded subblocks as if their boundaries were free would define a more informative channel and would not establish this statement.

The erasure comparison is a benchmark from entanglement-assisted channel coding: revealing every erased position gives rate $`(1-p)\log_2d`$. Forgetting those flags yields the deletion output, so the benchmark is an upper bound. The [standard capacity result](../references/RELATED_WORK.md#standard-coding-ingredients) and the explicit constructions here have different roles: the deletion proof is carried out directly for the one-string channel sequence.

## Why the coefficient is one-half

The auxiliary entanglement-assisted classical code transmits approximately

```math
2(n-k)\log_2d-\log_2\binom nk
```

bits, up to the stated error and linear-in-$`k`$ terms. A $`K`$-dimensional quantum message has $`K^2`$ teleportation correction labels. Sending those labels through the classical code turns the logarithmic classical message count into twice the logarithmic quantum dimension. Dense coding supplies the reverse conversion for the converse, without assuming that the effective quantum channel is covariant.

The factor of two is a standard entanglement-assisted communication relation. The deletion-specific work is establishing the classical message bound with arbitrary encoders and matching it on the same unframed channel. The [coding proof](coding-theorems.md) also shows that the teleportation construction meets the half-diamond error criterion exactly at its actual classical decoding error.

## Resources and remaining questions

The exhibited quantum construction shares $`n`$ maximally entangled pairs of dimension $`d`$ and one pair of dimension $`K`$. Their total entanglement entropy is $`n\log_2d+\log_2K`$ ebits. This cost is stated so that the rate is not mistaken for an unassisted protocol; it is not optimized. The receiver may perform a collective measurement of arbitrary complexity.

The theorem determines a leading small-deletion law. Improving the explicit constant could tighten finite-block estimates, but would not determine the sharp linear coefficient by itself. Exact capacity at fixed nonzero $`p`$, limited entanglement, unassisted transmission, efficient decoding, and additional timing or feedback resources require separate arguments.
