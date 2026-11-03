# Quantum Deletion Capacity

**How much quantum information is lost when the receiver knows how many carriers disappeared, but not their positions?** This project determines the leading synchronization cost of the ordered quantum deletion channel, even with unlimited preshared entanglement.

Each input is one string of qubits. Every qubit is independently deleted with probability $`p`$; the survivors retain their relative order, and the receiver observes only the final length. The entanglement-assisted quantum rate, in logical qubits per supplied qubit, satisfies

```math
Q_E^{\mathrm{del}}(p;2)
=1-\frac p2\log_2\frac1p+O(p),
\qquad p\downarrow0.
```

Known-position erasure has rate $`1-p`$. The additional leading loss comes from missing positional information. The result permits arbitrary collective encoders and decoders; preshared entanglement supplies no free message-bearing classical channel.

## Main results

| Setting | Established conclusion |
|---|---|
| Independent deletions, fixed carrier dimension | Matching leading small-deletion capacity bounds, with coefficient one-half in front of the positional-uncertainty term |
| Exactly one uniformly located deletion | An additional half-logarithmic loss in block length, at every fixed target error strictly between zero and one |
| Exactly $`k`$ uniformly located deletions | A finite-block converse for arbitrary entangled encoders and a direct one-string construction |
| Arbitrary number of deletions | A uniform Choi spectral estimate with a constant exponential in $`k`$, independent of block length |

For fixed local dimension $`d\ge2`$, define $`h_2`$ as the binary entropy and $`C_d=6/(1-1/d)^3`$. The explicit capacity bounds are

```math
\max\!\left\{0,(1-p)\log_2d-\frac12h_2(p)\right\}
\le Q_E^{\mathrm{del}}(p;d)
\le
\min\!\left\{
(1-p)\log_2d,
(1-p)\log_2d-\frac12h_2(p)+\frac p2\log_2C_d
\right\}.
```

The constant is deliberately loose: the gap between the two nontrivial bounds is linear in $`p`$, so they determine the leading $`p\log(1/p)`$ term without determining its linear correction. The exact capacity at a general positive deletion probability remains open.

## Read the science

| Question | Authoritative account |
|---|---|
| What channel, assistance and error criterion are allowed? | [Operational model](science/model.md) |
| Why can hidden deletion patterns not all become indistinguishable to the converse? | [Alignment geometry and the Choi spectrum](science/alignment-spectrum.md) |
| How are the finite-block bounds and capacity law proved? | [Coding theorems](science/coding-theorems.md) |
| What does the synchronization cost mean, and how do the resources enter? | [Interpretation and worked example](science/interpretation.md) |
| Which ideas are inherited, and what is added? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| Which finite statements can be reproduced? | [Verification](verification/README.md) |

The [science entrypoint](science/README.md) follows the proof dependencies. The [LLM reading guide](llms.txt) maps specific questions to the same authoritative files.

## Proof mechanism

The normalized Choi state of uniform $`k`$-deletion obeys

```math
\|J_{n,k}\|_\infty
\le\frac{C_d^k}{d^k\binom nk}.
```

Its complementary Gram matrix consists of permutation blocks weighted by disagreements between survivor ranks. Counting mismatch runs bounds the total overlap with any fixed deletion pattern. A completely positive comparison with a replacer then controls every entanglement-assisted encoder. For achievability, a Weyl code and a collective support measurement act on one entire string; teleportation correction labels are sent through that code.

The order-preserving overlap geometry has a direct antecedent in [ordered Hayden–Preskill recovery](references/RELATED_WORK.md#ordered-haydenpreskill-recovery). The uniform spectral estimate and its transmission-rate consequence are the additional results developed here.

## Reproduce the finite checks

Install the dependency and run the suite from the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The suite constructs small Kraus matrices directly and checks the Gram-block identity, normalization, scalar spectral reduction and recorded finite row sums. These checks support their enumerated cases. The universal converse and capacity asymptotics depend on the analytical proofs.

## Scope

The rate charges every input carrier, including any internal markers. The model supplies the final output length but no deleted-position flags, arrival-time labels, internal frame boundaries or feedback. Entanglement consumption is stated and unoptimized; the decoder is unrestricted. The result does not assert an unassisted capacity law, an efficient decoder, or the sharp coefficient of the linear remainder.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
