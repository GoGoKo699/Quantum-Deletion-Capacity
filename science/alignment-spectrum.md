# Alignment geometry and the Choi spectrum

An unknown deletion pattern changes the correspondence between input positions and output ranks. Two patterns therefore remain partly coherent in a Stinespring environment: nearby patterns can produce the same ordered output from many input basis strings. This section keeps that coherence explicitly and bounds its total contribution. The resulting estimate is uniform in the block length and in the number of deletions:

```math
\|J_{n,k}\|_\infty
\le
\frac{C_d^k}{d^k\binom{n}{k}},
\qquad
C_d=\frac{6}{(1-1/d)^3}\le48.
```

Here $`J_{n,k}`$ is the normalized Choi state of uniform deletion of $`k`$ positions from $`n`$ carriers of local dimension $`d\ge2`$. The constant is explicit and independent of $`n`$ and $`k`$. Its value affects the linear remainder in the small-deletion capacity bounds; the factor $`\binom{n}{k}^{-1}`$ determines the leading synchronization penalty.

Order-preserving alignment graphs already appear in [Alencar, Moreira and Silva, Appendix A, Lemma 6](https://arxiv.org/abs/2607.15537), where they evaluate the Choi purity of the ordered deletion channel for Hayden–Preskill recovery. We use the same underlying observation that an increasing partial matching has only fixed-point cycles. The argument below retains the deleted basis words, obtains a matrix of permutation blocks, and controls the sum of overlaps for every fixed deletion pattern. These additional steps give the uniform spectral estimate needed for the coding converse.

## 1. Channel and normalization

Let $`[n]=\{1,\ldots,n\}`$, let $`0\le k\le n`$, and write $`m=n-k`$. The input and output spaces are

```math
\mathcal H_A=(\mathbb C^d)^{\otimes n},
\qquad
\mathcal H_B=(\mathbb C^d)^{\otimes m}.
```

When $`m=0`$, the output is the one-dimensional empty-string space. For a deletion set $`S=\{s_1<\cdots<s_k\}`$, let

```math
x(S)=(x_1<\cdots<x_m)
```

be the increasing enumeration of $`[n]\setminus S`$. A basis word $`a=(a_1,\ldots,a_k)\in\{0,\ldots,d-1\}^k`$ specifies the deleted symbols. Define

```math
K_{S,a}|z_1,\ldots,z_n\rangle
=
\left(\prod_{j=1}^{k}\delta_{z_{s_j},a_j}\right)
|z_{x_1},\ldots,z_{x_m}\rangle.
```

The empty products and empty words have their usual meanings. For each fixed $`S`$, the operators $`K_{S,a}`$ implement the partial trace over $`S`$ while placing the surviving tensor factors in their original order. Thus

```math
\mathcal N_{n,k}(\rho)
=
\frac{1}{\binom{n}{k}}
\sum_{\substack{S\subseteq[n]\\|S|=k}}
\sum_a K_{S,a}\rho K_{S,a}^{\dagger}.
```

A Stinespring isometry is

```math
V=
\frac{1}{\sqrt{\binom{n}{k}}}
\sum_{S,a}K_{S,a}\otimes|S,a\rangle_E.
```

Let $`|\Phi_{d^n}\rangle`$ be a normalized maximally entangled state on $`R A`$, and set

```math
J_{n,k}
=
(\operatorname{id}_R\otimes\mathcal N_{n,k})
\bigl(|\Phi_{d^n}\rangle\langle\Phi_{d^n}|\bigr),
\qquad
\sigma_E
=
\operatorname{Tr}_B\left[V\frac{I_A}{d^n}V^{\dagger}\right].
```

Both operators have trace one. They are complementary reductions of the pure state $`(I_R\otimes V)|\Phi_{d^n}\rangle`$, so their nonzero eigenvalues agree. In particular,

```math
\|J_{n,k}\|_\infty=\|\sigma_E\|_\infty.
```

The environmental matrix elements are the normalized Kraus Gram entries

```math
\langle S,a|\sigma_E|T,b\rangle
=
\frac{\operatorname{Tr}(K_{T,b}^{\dagger}K_{S,a})}
{d^n\binom{n}{k}}.
```

## 2. The exact permutation-block identity

For two deletion sets $`S,T`$, write $`x=x(S)`$ and $`y=x(T)`$, and define the number of unequal survivor ranks by

```math
q(S,T)
=
\left|\{i\in[m]:x_i\ne y_i\}\right|.
```

**Lemma 1.** For every $`S,T`$, there is a permutation matrix $`P_{S,T}`$ on the $`d^k`$ deleted basis words such that

```math
(\sigma_E)_{S,T}
=
\frac{d^{-q(S,T)}}{d^k\binom{n}{k}}\,P_{S,T}.
```

The permutation can be nontrivial: the path matching between deleted positions need not preserve their order within the two deleted-word registers. It obeys $`P_{T,S}=P_{S,T}^{\dagger}`$ and $`P_{S,S}=I`$.

**Proof.** Expanding the trace in the input basis gives

```math
\operatorname{Tr}(K_{T,b}^{\dagger}K_{S,a})
=
\sum_{z\in\{0,\ldots,d-1\}^n}
\mathbf 1\{z_S=a\}\,
\mathbf 1\{z_T=b\}
\prod_{i=1}^{m}\mathbf 1\{z_{x_i}=z_{y_i}\}.
```

Consider the directed graph on $`[n]`$ with edges $`x_i\to y_i`$. Each vertex has at most one outgoing and one incoming edge. The partial map $`x_i\mapsto y_i`$ is strictly increasing. It has no directed cycle of length greater than one: starting from the smallest vertex of such a cycle would produce a strictly increasing sequence of successive images until returning to the starting vertex.

Every connected component is consequently a fixed loop or a directed path, with an isolated vertex counted as a path of length zero. A path starts at a vertex of $`T`$, where no incoming edge exists, and ends at a vertex of $`S`$, where no outgoing edge exists. Its other vertices lie in both survivor sets. Thus every path contains exactly one deleted position from each pattern. These paths pair the $`k`$ positions of $`S`$ bijectively with the $`k`$ positions of $`T`$.

Once $`z_S=a`$ is fixed, the equality constraints determine every symbol on every path. They force one compatible word $`b`$ on $`T`$, obtained by permuting the coordinates of $`a`$. Every fixed loop contributes one freely chosen basis symbol. There are exactly $`m-q(S,T)`$ fixed loops, and therefore

```math
\operatorname{Tr}(K_{T,b}^{\dagger}K_{S,a})
=
d^{m-q(S,T)}(P_{S,T})_{a,b}.
```

Substituting $`m=n-k`$ into the Gram formula proves the claim. The pairing is bijective for all choices of $`a`$, so each row and each column of $`P_{S,T}`$ contains exactly one unit entry. $`\square`$

This identity gives a scalar representation of the largest eigenvalue. Define the matrix indexed by deletion sets

```math
A_{n,k}(S,T)=d^{-q(S,T)}.
```

**Corollary 2.** The largest eigenvalues satisfy

```math
\|J_{n,k}\|_\infty
=
\frac{\lambda_{\max}(A_{n,k})}
{d^k\binom{n}{k}}
\le
\frac{1}{d^k\binom{n}{k}}
\max_S\sum_Td^{-q(S,T)}.
```

**Proof.** Let $`u=d^{-k/2}\sum_a|a\rangle`$. Every $`P_{S,T}`$ fixes $`u`$, so the subspace of vectors with blocks $`v_S=\alpha_Su`$ is invariant and the restriction of $`d^k\binom{n}{k}\sigma_E`$ to it is $`A_{n,k}`$. Conversely, for arbitrary blocks $`v_S`$,

```math
d^k\binom{n}{k}\,v^{\dagger}\sigma_Ev
\le
\sum_{S,T}d^{-q(S,T)}\|v_S\|\,\|v_T\|
\le
\lambda_{\max}(A_{n,k})\sum_S\|v_S\|^2.
```

The first inequality uses that each $`P_{S,T}`$ is unitary. The second is the Rayleigh bound for the real symmetric matrix $`A_{n,k}`$. These two observations prove equality of the largest eigenvalues. The final inequality follows from the maximum row sum of a nonnegative matrix. $`\square`$

## 3. Counting all alignments from one pattern

The next lemma bounds each row separately. Its dependence on $`k`$ is the point needed for the capacity law.

**Lemma 3.** Let $`0<r<1`$. For every fixed deletion set $`S`$ of size $`k`$,

```math
\sum_{\substack{T\subseteq[n]\\|T|=k}}
r^{q(S,T)}
\le
\left(\frac{6}{(1-r)^3}\right)^k.
```

**Proof.** Fix $`x=x(S)`$ and consider the survivor sequence $`y=x(T)`$. Add common boundary anchors

```math
x_0=y_0=0,
\qquad
x_{m+1}=y_{m+1}=n+1.
```

Partition the unequal ranks $`\{i:x_i\ne y_i\}`$ into maximal consecutive runs. A run $`\{a,\ldots,b\}`$ has length $`\ell=b-a+1\ge1`$. Maximality supplies common matching anchors at ranks $`a-1`$ and $`b+1`$, including the added anchors at either boundary. The physical interval

```math
I=\{x_{a-1}+1,\ldots,x_{b+1}-1\}
```

contains exactly $`\ell`$ survivors of $`x`$ and some number $`s`$ of deleted positions of $`S`$. Consequently $`|I|=\ell+s`$. The $`\ell`$ corresponding survivors of $`y`$ also lie in $`I`$.

The number $`s`$ is positive. If $`s=0`$, the interval would contain only the $`\ell`$ sites already occupied by $`x_a,\ldots,x_b`$. The strictly increasing $`y_a,\ldots,y_b`$ would then be forced to occupy exactly those sites, contradicting the definition of the run.

The holes $`S\cap I`$ form a nonempty consecutive group in the ordered list of $`S`$. Intervals belonging to different runs are disjoint, because a matching survivor separates any two consecutive runs. Thus the runs select disjoint consecutive groups of holes; some holes can remain unused.

Encode this group scheme by giving each of the $`k`$ holes one of three labels: unused, beginning a group, or continuing the preceding group. Every valid scheme has one such encoding, so there are at most $`3^k`$ schemes. Invalid label strings can be included when making an upper bound.

Fix one group containing $`s\ge1`$ holes and fix a run length $`\ell\ge1`$. Its interval has length $`\ell+s`$ and contains the prescribed first hole of the group, so there are at most $`\ell+s+1`$ possible intervals. Requiring the interval to stay inside $`[n]`$, to have the correct matching anchors, and to contain exactly the prescribed holes can only reduce this number. Within an interval there are at most

```math
\binom{\ell+s}{\ell}
=
\binom{\ell+s}{s}
```

choices for the increasing $`y`$-subsequence. We also allow choices that accidentally contain matching ranks; this again enlarges the count.

These records constitute an injective description of every actual $`T`$. The group scheme and intervals identify the runs of ranks in the known sequence $`x`$; the selected subsequences determine $`y`$ on each run; and outside the runs $`y`$ equals $`x`$. Hence the full sequence $`y`$, and therefore its complementary deletion set $`T`$, is recovered from the record.

Each run contributes $`r^{\ell}`$ to the weight $`r^{q(S,T)}`$. For a group of $`s`$ holes, the total weighted number of its possible records is bounded by

```math
\begin{aligned}
\sum_{\ell\ge1}
(\ell+s+1)\binom{\ell+s}{s}r^{\ell}
&\le
\sum_{\ell\ge0}
(\ell+s+1)\binom{\ell+s}{s}r^{\ell}\\
&=
\frac{s+1}{(1-r)^{s+2}}\\
&\le
\left(\frac{2}{(1-r)^3}\right)^s.
\end{aligned}
```

The equality is the binomial generating function. The last inequality uses $`s+1\le2^s`$ and $`s+2\le3s`$, valid for every integer $`s\ge1`$.

For a fixed group scheme, multiply these bounds over its groups. The groups use at most $`k`$ holes, so the product is at most $`[2/(1-r)^3]^k`$. Summing over at most $`3^k`$ schemes proves the result. Independent choices of run lengths and intervals have overcounted possible alignments by ignoring their disjointness and the finite string length; both changes are in the direction of the desired upper bound. The all-unused scheme accounts for $`y=x`$ and its weight one. $`\square`$

Taking $`r=1/d`$ in Lemma 3 and applying Corollary 2 proves the announced estimate.

**Theorem 4.** For every $`d\ge2`$, $`n\ge1`$, and $`0\le k\le n`$,

```math
\boxed{
\|J_{n,k}\|_\infty
\le
\frac{C_d^k}{d^k\binom{n}{k}},
\qquad
C_d=\frac{6}{(1-1/d)^3}\le48.
}
```

At $`k=0`$, the channel is the identity, the environmental space is one-dimensional, and $`\|J_{n,0}\|_\infty=1`$; the bound is exact. At $`k=n`$, the only deletion pattern removes the whole string, so $`\sigma_E=I/d^n`$ and $`\|J_{n,n}\|_\infty=d^{-n}`$. There are no survivor ranks or mismatch runs in that case, and the exact row sum is one. The theorem remains valid, with a loose constant factor. The same boundary conventions cover runs that touch either end when $`0<k<n`$.

## 4. A single deletion

For $`k=1`$, label the deletion sets by the removed positions $`s,t\in[n]`$. The survivor sequences differ in exactly $`|s-t|`$ ranks, and a one-symbol word has no nontrivial coordinate permutation. Hence

```math
\sigma_E
=
\frac{T_n(r)\otimes I_d}{dn},
\qquad
r=\frac1d,
\qquad
[T_n(r)]_{s,t}=r^{|s-t|}.
```

This finite Toeplitz matrix makes the coherence between nearby deletion positions explicit. Its largest eigenvalue has the elementary bounds

```math
1+2\sum_{h=1}^{n-1}\left(1-\frac hn\right)r^h
\le
\lambda_{\max}(T_n(r))
\le
\frac{1+r}{1-r}.
```

The lower bound is the Rayleigh quotient of the normalized constant vector, and the upper bound is the infinite geometric row sum. For fixed $`d`$, the two bounds converge to the same value, giving

```math
\lambda_{\max}(T_n(1/d))
\longrightarrow
\frac{d+1}{d-1},
\qquad
\|J_{n,1}\|_\infty
=
\frac{1}{dn}
\left(\frac{d+1}{d-1}+o(1)\right).
```

The exact matrix and these norm bounds provide a direct check of the general normalization and overlap mechanism. The capacity argument uses the uniform bound of Theorem 4, which also covers growing deletion counts.

## 5. From the spectrum to coding

The normalized Choi state of maximally mixed replacement on the $`d^m`$-dimensional output is $`I_{RB}/d^{n+m}`$. Theorem 4 therefore yields the completely positive order bound

```math
\mathcal N_{n,k}
\le_{\mathrm{CP}}
\frac{d^{2(n-k)}C_d^k}{\binom{n}{k}}
\,\mathcal R_{n-k},
\qquad
\mathcal R_{n-k}(X)
=\operatorname{Tr}(X)\frac{I_B}{d^{n-k}}.
```

Because this is an inequality between completely positive maps, it remains valid after adjoining an arbitrary reference system and applying it to any encoded input. The coding converse uses this property to cover arbitrary entanglement-assisted encoders. No maximally mixed input optimality assumption is required. The spectral calculation supplies a uniform comparison of the channel itself.

## Reference

J. V. R. Alencar, A. R. P. Moreira, and J. B. R. Silva, *Microscopic Side Information Controls Ordered Hayden–Preskill Recovery*, [arXiv:2607.15537v1](https://arxiv.org/abs/2607.15537), Appendix A, Lemma 6 (2026).
