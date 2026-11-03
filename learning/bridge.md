# From entanglement-assisted communication to ordered deletion

The question is how much information is lost when a missing quantum carrier also loses its position label. Preshared entanglement helps communication, but it does not remove that uncertainty. This bridge connects the [selected Wilde source](anchor.md) to the result: at small deletion probability, hidden positions cost an additional $`\tfrac12p\log_2(1/p)`$ qubits per supplied carrier, to leading order.

The [milestone map](milestones.md) separates the prerequisite framework from the deletion-specific argument. Exact statements and proofs are in the [scientific account](../science/README.md).

## The physical task

Imagine sending a train of $`n`$ quantum carriers, each with $`d`$ distinguishable basis levels. Some carriers disappear. The survivors arrive in their original relative order, and the receiver knows how many remain. The receiver does not know their original position numbers. A missing carrier with a reported position would be an **erasure**; closing the gap while hiding that position creates a **deletion**.

The sender may encode a logical quantum message jointly across the entire train. The receiver may combine all survivors with its share of an initially entangled state. The target is to recover the message even when it was entangled with an inaccessible reference. Correctly recovering a measured basis label would be a weaker task: a quantum code must also preserve superpositions and correlations with that reference.

The communication budget is the supplied length $`n`$, including lost carriers, markers and redundancy. The local dimension $`d`$ is fixed. Shared entanglement has no rate restriction, but there is no additional classical message channel, arrival-time information, feedback during transmission or supplied internal frame boundary. The [model](../science/model.md) makes these distinctions explicit.

There are two noise laws. In the fixed-count channel $`\mathcal N_{n,k}`$, exactly $`k`$ uniformly chosen positions disappear. In $`\mathcal N_{n,p}`$, each position disappears independently with probability $`p`$. The latter is a mixture of the fixed-count channels, with weights $`\binom nkp^k(1-p)^{n-k}`$. Different output lengths are distinguishable, so the receiver can use a decoder appropriate to the observed deletion count. This gives no labels for the particular missing positions.

## Four qubits and one deletion

Take $`n=4`$, $`k=1`$ and $`d=2`$. For the basis input $`|0011\rangle`$, deleting position 1 or 2 gives $`|011\rangle`$, while deleting position 3 or 4 gives $`|001\rangle`$. The output state is

```math
\mathcal N_{4,1}(|0011\rangle\langle0011|)
=\frac12|011\rangle\langle011|
+\frac12|001\rangle\langle001|.
```

A computational-basis measurement therefore returns either string with probability one-half. Even this simple observation cannot identify the deleted position uniquely. The channel itself does not measure the input in this basis: deletion is a partial trace, and its action on coherent or entangled inputs must be kept.

To examine that action, consider four shared Bell pairs. Send one half of each pair through the channel and retain the other four as a reference $`R`$. The resulting state on $`R`$ and the three survivors is the normalized Choi state $`J_{4,1}`$. It encodes the entire channel, although it is obtained from one particular input.

A convenient representation keeps a mathematical environment label $`(s,a)`$: the deleted position $`s\in\{1,2,3,4\}`$ and its basis bit $`a\in\{0,1\}`$. Define the raw partial-inner-product operators by

```math
K_{s,a}|z_1z_2z_3z_4\rangle
=\delta_{z_s,a}|z_1\cdots z_{s-1}z_{s+1}\cdots z_4\rangle.
```

The channel Kraus operators are $`K_{s,a}/2`$, because each deleted position has probability $`1/4`$. The environment state for the maximally mixed input has entries

```math
\langle s,a|\sigma_E|t,b\rangle
=\frac{\mathrm{Tr}(K_{t,b}^{\dagger}K_{s,a})}{16\cdot4}.
```

Now compare deleting position 2 with deleting position 3. Their ordered survivor lists are $`(1,3,4)`$ and $`(1,2,4)`$. Equality of the two output words requires $`z_3=z_2`$. The deleted-bit conditions also require $`z_2=a`$ and $`z_3=b`$. Thus the trace is zero unless $`a=b`$; if they agree, $`z_1`$ and $`z_4`$ remain free, giving four basis strings. Therefore

```math
\mathrm{Tr}(K_{3,b}^{\dagger}K_{2,a})=4\delta_{ab},
\qquad
(\sigma_E)_{2,3}=\frac{I_2}{16}.
```

For a diagonal block, only the one deleted bit is fixed and three bits remain free. Its value is $`I_2/8`$. The **relative overlap factor is $`1/2`$**, while the **fully normalized off-diagonal block is $`I_2/16`$**. Confusing these two numbers would lose both the input-state normalization and the deletion-pattern probability.

The same calculation specifies the entire eight-dimensional environment state:

```math
(\sigma_E)_{s,t}=\frac{2^{-|s-t|}}8\,I_2,
\qquad s,t\in\{1,2,3,4\}.
```

Its four diagonal blocks each have trace $`1/4`$, so the whole state has trace one. Nearby deleted positions have larger off-diagonal blocks because they disagree at fewer survivor ranks. The basis vectors $`|s,a\rangle`$ are orthogonal; the state nevertheless has coherence between them. Replacing this state by a diagonal classical record would change the calculation.

The states $`J_{4,1}`$ and $`\sigma_E`$ are the two reductions of a pure state across the split $`RB:E`$. Their nonzero eigenvalues therefore agree. This is the useful connection to the purification and Schmidt-decomposition tools in the anchor. For several deletions, a block can also permute the deleted-word coordinates. The general [alignment proof](../science/alignment-spectrum.md#2-the-exact-permutation-block-identity) keeps those permutations and bounds all overlaps together.

## From a Choi state to a universal converse

A converse must apply to every permitted encoder, including one that chooses a highly nonuniform input and uses a large entangled reference. Calculating an information quantity for the maximally mixed input alone does not accomplish that.

For a state on $`RB`$, the coherent information is $`S(B)-S(RB)`$, whereas the mutual information is $`S(R)+S(B)-S(RB)`$; $`S`$ denotes von Neumann entropy. Chapter 21 of the anchor optimizes mutual information over channel inputs for the entanglement-assisted classical capacity of a memoryless channel. A value evaluated at $`J_{n,k}`$ is one input's value. Neither its coherent information nor its mutual information establishes that this input is optimal for deletion. In particular, the Weyl averaging used in the construction below does not prove covariance of the deletion channel.

The project obtains a universal statement from a different property of the same Choi state. The [spectral theorem](../science/alignment-spectrum.md#3-counting-all-alignments-from-one-pattern) proves

```math
\|J_{n,k}\|_\infty
\leq\frac{C_d^k}{d^k\binom nk},
\qquad
C_d=\frac{6}{(1-1/d)^3}\leq48.
```

The norm is the largest eigenvalue. The proof first expresses every environment block through its alignment factor and then bounds the total contribution from all patterns relative to any fixed pattern. This uniform control is stronger than an average-overlap or purity calculation for the purpose needed here.

Let $`\mathcal R_{n-k}`$ discard its input and output the maximally mixed state on the $`n-k`$ surviving carriers. Its normalized Choi state is $`I_{RB}/d^{2n-k}`$. An upper bound on every eigenvalue of $`J_{n,k}`$ therefore gives a completely positive order comparison. Combining it with the output-dimension bound yields

```math
\mathcal N_{n,k}\leq_{\mathrm{CP}}\Lambda_{n,k}\mathcal R_{n-k},
\qquad
\Lambda_{n,k}
=\min\left\{d^{2(n-k)},
\frac{d^{2(n-k)}C_d^k}{\binom nk}\right\}.
```

Here $`\leq_{\mathrm{CP}}`$ means that the difference between the right and left maps is completely positive. The comparison remains true after adjoining any reference and composing with encoding and decoding operations. This is what turns a calculation using a maximally entangled test input into a statement about arbitrary actual inputs.

Under the replacer channel, the receiver sees a fixed output. Its retained entangled share also has a message-independent marginal: a trace-preserving operation at the sender cannot signal to that share. Any complete measurement therefore guesses among $`M`$ equiprobable classical messages with average success exactly $`1/M`$. The order comparison gives

```math
P_{\mathrm{succ}}\leq\min\{1,\Lambda_{n,k}/M\}.
```

The [converse proof](../science/coding-theorems.md#arbitrary-encoder-converse-by-cp-domination) supplies the details. It does not select a supposedly optimal input or restrict the amount of shared entanglement.

## Packing one whole string

The matching construction begins with $`n`$ shared maximally entangled pairs of dimension $`d`$. To send a classical label, the sender applies its codeword's product Weyl operator to its halves and sends the entire length-$`n`$ string. Weyl operators are the finite-dimensional shift and phase operations that generalize the qubit Pauli operators.

The receiver holds its original halves and the survivors. For each output length, the possible received states are unitarily related to $`J_{n,k}`$ on the retained halves. This follows by transposing a unitary across a maximally entangled pair; it requires no channel covariance. Uniformly sampling a Weyl codeword makes the average received state maximally mixed on dimension $`d^{2n-k}`$.

Each codeword state has support rank at most $`d^k\binom nk`$, the number of Kraus operators. Its support projector is a test that accepts that codeword state with probability one. Combining the tests with a square-root measurement gives a complete decoder, after assigning any unused measurement subspace to one label.

The packing argument in Chapter 16 explains how to control confusion between such tests. In this application, independently sampled codewords give

```math
\mathbb E\,\mathrm{Tr}(\rho_{i,k}\Pi_{j,k})
=\frac{\mathrm{rank}J_{n,k}}{d^{2n-k}}
\leq \binom nk\,d^{-2(n-k)}
\quad(i\ne j).
```

Here $`\rho_{i,k}`$ is a received codeword state and $`\Pi_{j,k}`$ is another codeword's support projector. The expectation averages the state while holding the independent projector fixed. It does not assert that the support projectors themselves average to a multiple of the identity. The Hayashi–Nagaoka inequality then gives a deterministic codebook with average classical error

```math
\overline e_k\leq
\min\left\{1,\,4(M-1)\binom nk\,d^{-2(n-k)}\right\}.
```

The randomness proves that a suitable codebook exists; the selected codebook is fixed before the message is chosen. The [coding proof](../science/coding-theorems.md#one-block-weyl-support-packing) gives the measurement and expectation explicitly.

**Why frame boundaries are not free.** If two strings were sent as separately framed channel uses, the receiver would learn where the first output ended, even if its random surviving length changed. In one longer deletion string, only the total length is supplied. A separate length for each internal block is additional information. Communicating it, or protecting markers that reveal it, requires a construction and charged carriers. This issue already arises for classical messages; preshared entanglement alone does not supply those labels.

For independent deletions, the construction therefore chooses **one codebook for the whole string**, averages its total error over likely deletion counts, and lets the receiver choose its measurement using the final length. An unlikely length is included in the error bound. This directly proves coding for $`\mathcal N_{n,p}`$, without substituting repeated uses of an independently framed smaller channel.

## Why quantum rates have a factor of one-half

A $`K`$-dimensional quantum message contains $`\log_2K`$ logical qubits. Teleporting it produces $`K^2`$ possible correction labels, requiring $`2\log_2K`$ classical bits. These labels are uniform even when the message is entangled with a reference.

Use the classical deletion code to transmit those labels and share one additional maximally entangled pair of dimension $`K`$ for teleportation. The correction information travels through the same deletion transmission; there is no free classical link. This conversion is the operational reason that a logarithmic classical-message bound becomes twice a logarithmic quantum-dimension bound, as in Chapter 6 and §22.1 of the anchor.

The finite-error statement is especially useful here. Let $`\mathstrut \mathcal T`$ be the effective quantum channel, and use the conventions

```math
F_e(\mathcal T)
=\langle\Phi_K|(\mathrm{id}_K\otimes\mathcal T)(\Phi_K)
|\Phi_K\rangle,
\qquad
\epsilon_\diamond(\mathcal T)
=\frac12\|\mathcal T-\mathrm{id}_K\|_\diamond.
```

The fidelity is the squared overlap with the ideal maximally entangled output. The diamond distance tests every logical input together with a reference. For an arbitrary channel, $`1-F_e\leq\epsilon_\diamond`$; a small error on the single maximally entangled test should not silently be declared the same worst-input error.

For this teleportation construction, a complete classical decoder with actual average error $`\overline e`$ produces a mixture of Weyl errors. Correctly decoded labels give the identity; incorrect labels give nonidentity Weyls. Distinct Weyl errors send a maximally entangled input to orthogonal Bell states, so the [exact conversion](../science/coding-theorems.md#teleportation-for-achievability) gives

```math
F_e(\mathcal T)=1-\overline e,
\qquad
\epsilon_\diamond(\mathcal T)=\overline e.
```

Thus a classical average-error guarantee supplies the required reference-stable quantum guarantee for this explicit channel. Any abort outcome is first assigned a definite correction label and counted in the completed decoder.

For the reverse direction, add a $`K`$-dimensional entangled pair to any proposed quantum code and use dense coding to send $`K^2`$ labels. The sender's Weyl can be moved to the untouched reference by transposition. The probability of the correct Bell outcome is exactly $`F_e(\mathcal T)`$ for every label, even when $`\mathstrut \mathcal T`$ is not covariant. Applying the classical converse gives

```math
F_e(\mathcal T)\leq\min\{1,\Lambda_{n,k}/K^2\}.
```

The [dense-coding proof](../science/coding-theorems.md#dense-coding-for-the-converse) makes this step independent of any input-optimization assumption.

The exhibited quantum construction uses $`n\log_2d+\log_2K`$ ebits: the first term for the Weyl code and the second for teleportation. Its entanglement consumption is not optimized. The factor one-half in the rate describes the conversion between classical correction labels and quantum dimension; it is not a statement that half the surviving carriers are discarded.

## Finite-length and small-deletion statements

Let $`K^*_{n,k,\epsilon}`$ be the largest logical dimension attainable at half-diamond error at most a fixed $`0\lt \epsilon\lt 1`$. For fixed $`d`$ and $`1\leq k=o(n)`$, the finite bounds give

```math
\log_2K^*_{n,k,\epsilon}
=(n-k)\log_2d-\frac12\log_2\binom nk
+O_{d,\epsilon}(k+1).
```

The surviving dimension supplies the first term. Uncertainty among $`\binom nk`$ alignments supplies the additional logarithmic loss, to this precision. For one deletion, that extra loss is $`\tfrac12\log_2n+O_{d,\epsilon}(1)`$. The four-qubit example illustrates the mechanism; it is not an asymptotic capacity calculation.

The target error is fixed in this expression. If it decreases with block length, the separate error terms and integer rounding in the [finite-count theorem](../science/coding-theorems.md#fixed-count-statement) must be retained. At zero deletions the identity channel transmits $`d^n`$ dimensions perfectly. At $`k=n`$ the empty output cannot communicate a nontrivial message reliably.

For independent deletion at a fixed probability $`p`$, the deletion count concentrates near $`np`$, and

```math
\frac1n\log_2\binom n{\lfloor np\rfloor}\longrightarrow h_2(p),
\qquad
h_2(p)=-p\log_2p-(1-p)\log_2(1-p).
```

The same codebook must handle those likely lengths. The one-string construction and branchwise converse do exactly this. Their [capacity sandwich](../science/coding-theorems.md#capacity-sandwich), including the nonnegative and erasure-bound clipping, has nontrivial terms

```math
(1-p)\log_2d-\frac12h_2(p)
\leq Q_E^{\mathrm{del}}(p;d)
\leq(1-p)\log_2d-\frac12h_2(p)+\frac p2\log_2C_d.
```

At fixed $`d`$, the gap between these terms is proportional to $`p`$. Since $`h_2(p)=p\log_2(1/p)+O(p)`$, they determine

```math
Q_E^{\mathrm{del}}(p;d)
=\log_2d-\frac p2\log_2\frac1p+O_d(p).
```

The order of limits matters: first take long codes at each fixed $`p`$ with error tending to zero, then study $`p\downarrow0`$. The local alphabet is not enlarged as $`p`$ decreases.

Revealing every missing position gives the erasure benchmark $`(1-p)\log_2d`$. Hiding those positions therefore costs an additional $`\tfrac12p\log_2(1/p)+O_d(p)`$. The bounds establish a leading coefficient, while the coefficient of the term linear in $`p`$ and the exact capacity at a general positive $`p`$ remain unresolved.

## What the result does and does not explain

The decoder need not recover the deletion set as a separate classical output. The count of possible patterns enters through support size in the construction and through the overlap spectrum in the converse. Their coherent overlaps contribute at most a factor $`C_d^k`$ to the bound; its logarithm changes a term proportional to $`k`$, while $`\log_2\binom nk`$ determines the leading synchronization penalty.

The general communication conversions and packing tools come from established quantum information theory. The order-preserving overlap graph is credited to the prior ordered Hayden–Preskill analysis in [related work](../references/RELATED_WORK.md#ordered-haydenpreskill-recovery). Retaining the deleted-symbol words and controlling every alignment row provide the additional uniform spectral estimate used for this capacity problem. The [specialist proof](../science/alignment-spectrum.md) contains that combinatorial step.

The operational conclusion concerns unrestricted preshared entanglement, fixed carrier dimension and a collective decoder for one ordered string. It does not determine the unassisted capacity, an optimal entanglement budget, an efficient decoding algorithm or a feedback-assisted rate. The [verification package](../verification/README.md) checks finite Kraus contractions and normalizations; the general result rests on the analytic counting, packing and converse arguments.
