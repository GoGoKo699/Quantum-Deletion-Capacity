# Operational model

We study quantum information sent through an ordered string of carriers when some carriers disappear and the receiver is told only the final length. The locations of the missing carriers are unavailable. The communication rate counts all carriers supplied to the channel, including any carriers used as markers or redundancy.

The [coding theorems](coding-theorems.md) give finite-block error bounds and the resulting capacity bounds. Their converse uses the [alignment-spectrum estimate](alignment-spectrum.md). See [related work](../references/RELATED_WORK.md) for attribution and comparisons.

## One transmitted string

Fix an integer local dimension $`d\geq 2`$. A transmission supplies exactly $`n\geq 1`$ carriers,

```math
A^n=A_1\otimes\cdots\otimes A_n,
\qquad A_i\cong\mathbb C^d.
```

The input can be entangled across all carriers and with a reference. The integer $`n`$ is fixed independently of the message. The receiver obtains one ordered output string after the transmission. Surviving carriers retain their relative order, but have no original-position labels.

The model supplies no arrival-time information, feedback during the transmission, or internal frame boundaries. The receiver may determine the total output length. A code may put markers inside the transmitted string, but those markers occupy the same charged $`n`$ carriers and use the same fixed local dimension $`d`$. No additional message-bearing classical channel is available.

### Exactly $`k`$ deletions

For $`0\leq k\leq n`$, choose a deletion set $`S\subseteq\{1,\ldots,n\}`$ uniformly among the $`\binom nk`$ sets of size $`k`$. Trace out its carriers, and identify the survivors with a register $`B_{n-k}\cong(\mathbb C^d)^{\otimes(n-k)}`$ in increasing original-position order. Thus

```math
\mathcal N_{n,k}(\rho)
=\frac{1}{\binom nk}
\sum_{\substack{S\subseteq\{1,\ldots,n\}\\ |S|=k}}
V_S\operatorname{Tr}_{A_S}(\rho)V_S^\dagger,
```

where $`V_S`$ is the order-preserving identification of the surviving tensor factors with $`B_{n-k}`$. The number $`k`$ is known from the final length $`n-k`$, but the set $`S`$ is not supplied.

At $`k=0`$ this is the identity channel on $`n`$ carriers. At $`k=n`$ the output is the one-dimensional empty-string register.

### Independent deletions

For a deletion probability $`p\in[0,1]`$, each carrier is deleted independently. Let

```math
q_{n,p}(k)=\binom nk p^k(1-p)^{n-k}.
```

The channel is the orthogonal direct sum

```math
\mathcal N_{n,p}(\rho)
=\bigoplus_{k=0}^n q_{n,p}(k)\mathcal N_{n,k}(\rho).
```

The direct-sum label records the observable final length. It records no further information about the deletion pattern. In particular, $`q_{n,p}(k)`$ is independent of the input and message.

The parameter $`p`$ specifies the channel for which the code is designed. We do not analyze universal coding for an unknown deletion probability. The local dimension $`d`$ is fixed in the small-$`p`$ asymptotic.

## Entanglement-assisted quantum codes

The sender and receiver may initially share an arbitrary finite-dimensional state $`\omega_{A_0B_0}`$, independent of the quantum message and its reference. Its dimension is unrestricted and may grow with $`n`$. Local operations and classical computation are unrestricted. The shared state need not be returned, and its consumption is not optimized.

A code for a $`K`$-dimensional quantum message consists of a completely positive trace-preserving encoder

```math
\mathcal E:Q\otimes A_0\longrightarrow A^n
```

and a completely positive trace-preserving decoder

```math
\mathcal D:B\otimes B_0\longrightarrow\widehat Q,
\qquad Q\cong\widehat Q\cong\mathbb C^K.
```

Here $`B=B_{n-k}`$ for fixed-count deletion and $`B=\bigoplus_k B_{n-k}`$ for independent deletion. The decoder may condition its operation on the observed length. Private ancillary registers and discarding can be included in these maps.

Together with the shared state and deletion channel, these maps induce an effective channel $`\mathcal T:Q\to\widehat Q`$. We use the reference-stable error

```math
\epsilon_\diamond(\mathcal T)
=\frac12\|\mathcal T-\operatorname{id}_K\|_\diamond.
```

Thus the guarantee applies to every input, including a message entangled with an inaccessible reference. A reference of dimension $`K`$ suffices in this norm. A decoder with an abort outcome must complete that branch to a quantum output; an abort is not a free successful transmission.

We also state converse bounds for the squared-overlap entanglement fidelity

```math
F_e(\mathcal T)
=\langle\Phi_K|
(\operatorname{id}_K\otimes\mathcal T)(\Phi_K)
|\Phi_K\rangle,
\qquad
|\Phi_K\rangle
=\frac1{\sqrt K}\sum_{j=0}^{K-1}|j\rangle|j\rangle,
```

where $`\Phi_K=|\Phi_K\rangle\langle\Phi_K|`$. The conventions imply

```math
1-F_e(\mathcal T)\leq\epsilon_\diamond(\mathcal T).
```

The achievability proof constructs a random-Weyl effective channel for which equality holds. Consequently, it supplies the diamond-norm criterion directly, without converting an average-input fidelity into a worst-input claim.

## Rate and capacity

All logarithms are base two. The rate of a quantum code is

```math
R_n=\frac{\log_2 K}{n},
```

measured in qubits of information per supplied $`d`$-level carrier. In particular, the noiseless rate is $`\log_2 d`$.

Call a rate $`R`$ achievable if a sequence of codes for $`\mathcal N_{n,p}`$ satisfies $`\liminf_{n\to\infty}(\log_2K_n)/n\geq R`$ and $`\epsilon_\diamond(\mathcal T_n)\to0`$. Let $`Q_E^{\mathrm{del}}(p;d)`$ be the supremum of these rates. The subscript $`E`$ denotes unrestricted preshared entanglement. It does not grant a classical communication channel or access to the deletion environment.

Each code uses one length-$`n`$ input string and one final output string. The achievability proof does not concatenate independently decoded blocks with externally supplied boundaries. The converse covers arbitrary encoders within this one-transmission model, including encoders that use charged internal markers.

For comparison, if each missing position were reported by an erasure flag, the entanglement-assisted quantum capacity would be

```math
Q_E^{\mathrm{erase}}(p;d)=(1-p)\log_2 d.
```

Deleting the flags and joining the survivors recovers the deletion output. This makes the erasure rate an upper benchmark, while keeping the additional synchronization cost explicit.

## Auxiliary classical codes

The proofs use classical codes with $`M\geq1`$ equiprobable labels and an initial shared state independent of that label. The sender encodes the label using its share of the state, sends exactly $`n`$ carriers, and the receiver performs a complete $`M`$-outcome measurement. Their error is the average error over the uniform labels.

These classical codes are auxiliary communication protocols, not free side information. In the quantum construction, they carry all teleportation correction labels through the deletion channel itself. Conversely, dense coding converts any effective $`K`$-dimensional quantum channel into a classical $`K^2`$-label protocol by adding a $`K`$-dimensional maximally entangled pair. Both conversions are explicit in the [coding proof](coding-theorems.md#exact-conversions-between-classical-and-quantum-codes).

## Resource and scope boundaries

- The charged communication resource is the number $`n`$ of supplied carriers. Lost carriers, markers, and redundancy all count.
- Preshared entanglement is available without a rate restriction, but the constructions state the amount they use. They make no optimal entanglement-consumption claim.
- Encoders and decoders may act collectively. The existence proof does not establish an efficient decoder, a practical gate count, or a finite-memory implementation.
- The noise acts only by tracing out selected carriers. Additional local noise, insertions, substitutions, timing leakage, and interactive feedback define different channels.
- The capacity result determines the leading small-deletion penalty and an explicit all-$`p`$ sandwich. It does not determine the exact capacity at a general positive $`p`$ or the unassisted quantum capacity.

