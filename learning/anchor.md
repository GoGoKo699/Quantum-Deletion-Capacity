# Educational anchor

Mark Wilde's treatment of entanglement-assisted communication provides the route into this project: understand the communication resources, see how a quantum measurement separates codewords, and then connect those tools to the cost of hidden deletion positions. The [bridge](bridge.md) supplies that connection. The [30-milestone map](milestones.md) organizes the project's understanding targets.

## Selected source

**Mark M. Wilde, _Quantum Information Theory_, second edition, Cambridge University Press (2017).** [Publisher DOI](https://doi.org/10.1017/9781316809976).

The accessible reading reference is the author's manuscript, **_From Classical to Quantum Shannon Theory_, [arXiv:1106.1445v8](https://arxiv.org/abs/1106.1445v8), posted 14 July 2019**. The [versioned PDF](https://arxiv.org/pdf/1106.1445v8) fixes the chapter and section pointers below. The [author-hosted PDF](https://www.markwilde.com/qit-notes.pdf) is a convenient alternative that may contain later corrections; its pagination need not match the pinned version.

These are published and accessible forms of one educational source. The primary papers used for attribution and proof ingredients have a separate home in [related work](../references/RELATED_WORK.md).

## Focused reading route

Use the relevant section alongside the corresponding part of the bridge. The route does not require reading the entire book first.

| Wilde route | Idea to bring to this project | Project connection |
|---|---|---|
| Chapter 6, especially §§6.2 and 6.5 | Teleportation, dense coding, and their qudit resource accounting | [The factor of one-half](bridge.md#why-quantum-rates-have-a-factor-of-one-half) |
| Chapter 16, especially §16.3 and §16.4 | Packing statement and proof; the Hayashi–Nagaoka inequality is Lemma 16.4.1 | [One-string support packing](bridge.md#packing-one-whole-string) |
| Chapter 21, especially §§21.1–21.5 | The entanglement-assisted classical task, optimized channel mutual information, and coding/converse roles | [A converse for arbitrary encoders](bridge.md#from-a-choi-state-to-a-universal-converse) |
| §22.1 | Entanglement-assisted quantum communication and conversion from classical communication | [Resources and exact errors](bridge.md#why-quantum-rates-have-a-factor-of-one-half) |

For individual prerequisites, the same source provides Schmidt decomposition in §3.8, noisy channels in Chapter 4, purification and isometric evolution in §§5.1–5.2, distance and channel fidelity in Chapter 9, and coherent information versus mutual information in §§11.5–11.6. The bridge defines the objects it needs before using them.

## Notation and assumptions

**Registers.** In Wilde's channel expression $`\rho_{AB}=(\mathrm{id}_A\otimes\mathcal N_{A'\to B})(\phi_{AA'})`$, $`A`$ is the purifying reference. Here that role is called $`R`$, and the transmitted input is $`A^n=A_1\otimes\cdots\otimes A_n`$. Each carrier has fixed dimension $`d`$. After exactly $`k`$ deletions, the survivor register $`B`$ has dimension $`d^{n-k}`$. A Stinespring environment is called $`E`$; it is a mathematical description of discarded information, not a register available to the receiver. The [operational model](../science/model.md) fixes all of these roles.

**Normalized states.** We write $`\tau=I/d^n`$ for the maximally mixed input. Our maximally entangled vector and Choi state are normalized:

```math
|\Phi_D\rangle=\frac1{\sqrt D}\sum_{j=0}^{D-1}|j\rangle|j\rangle,
\qquad
\Phi_D=|\Phi_D\rangle\langle\Phi_D|,
```

```math
J_{n,k}=(\mathrm{id}_R\otimes\mathcal N_{n,k})(\Phi_{d^n}),
\qquad
\mathrm{Tr}J_{n,k}=1.
```

An expression constructed with the unnormalized vector $`|\Gamma_D\rangle=\sum_j|j\rangle|j\rangle`$ must be divided by $`D`$ to obtain this normalized Choi state. That factor matters in the spectral bound. The norm $`\|J_{n,k}\|_\infty`$ is the largest eigenvalue, whereas $`\mathrm{Tr}(J_{n,k}^2)`$ is the purity. They are different quantities. The [four-qubit example](bridge.md#four-qubits-and-one-deletion) makes the normalization explicit.

**Messages and rates.** Lowercase $`k`$ counts deleted carriers. Uppercase $`K`$ is the dimension of the logical quantum message, and $`M`$ counts classical message labels. All logarithms are base two. The quantum rate is $`(\log_2K)/n`$ qubits of information per supplied carrier; the noiseless rate is $`\log_2d`$. An ebit is one bit of shared entanglement entropy. Entanglement assistance permits arbitrary initial shared entanglement, but it supplies no message-bearing classical channel. Markers and redundancy use charged input carriers.

**Errors.** The project uses the squared-overlap entanglement fidelity $`F_e`$ and the reference-stable error $`\epsilon_\diamond=\tfrac12\|\mathcal T-\mathrm{id}_K\|_\diamond`$ of the effective logical channel $`\mathstrut \mathcal T`$. The square in the fidelity convention and the factor one-half in the diamond distance are fixed in the [model](../science/model.md#entanglement-assisted-quantum-codes). The [finite conversions](bridge.md#why-quantum-rates-have-a-factor-of-one-half) explain exactly how a classical decoding error becomes a quantum error; no generic average-input-to-worst-input equivalence is assumed.

**Channel uses.** The capacity studied here belongs to the sequence $`\{\mathcal N_{n,p}\}_{n\ge1}`$: one length-$`n`$ input string produces one ordered output string. Independently applying a fixed block channel many times would supply a separate output boundary for each use. Those boundaries are absent here. Consequently, the memoryless coding theorem in the anchor is background for the method, while the project's direct [one-block proof](../science/coding-theorems.md#one-block-weyl-support-packing) establishes achievability for the actual unframed string.

## Source and result boundaries

The anchor explains the general communication language and inherited tools. The project supplies the ordered-deletion calculation: exact permutation blocks in a complementary state, a uniform bound on their combined spectral weight, a comparison with a replacer channel that holds for every encoder, and a single codebook that works across the observable output lengths.

The order-preserving overlap geometry has a research antecedent in Alencar, Moreira and Silva. Their purity calculation is credited in the [alignment proof](../science/alignment-spectrum.md); it does not by itself give the uniform largest-eigenvalue bound used here. The packing inequality and standard capacity ingredients are likewise attributed in [related work](../references/RELATED_WORK.md#standard-coding-ingredients). These research dependencies are distinct from the selected educational anchor.

The bridge explains why the pieces fit. Exact quantifiers, constants, endpoint cases and proofs remain in the [scientific account](../science/README.md), and [verification](../verification/README.md) documents finite numerical checks. The learning route supports global understanding without claiming to replace those specialist arguments.
