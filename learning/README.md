# Learning the quantum deletion-capacity result

The central question is how much quantum communication is lost when missing carriers also hide their original positions. This route connects entanglement-assisted communication to the alignment geometry that determines the leading cost of that uncertainty.

The selected educational anchor is **Mark M. Wilde, _Quantum Information Theory_, second edition (2017)**, using the pinned author manuscript [_From Classical to Quantum Shannon Theory_, arXiv:1106.1445v8, 14 July 2019](https://arxiv.org/abs/1106.1445v8). Its unit protocols, packing argument, and entanglement-assisted communication chapters supply the background. The project's own science files supply the ordered-deletion spectrum and the direct coding argument for one transmitted string.

## Reading routes

| Purpose | Starting point |
|---|---|
| Locate the selected Wilde sections and translate notation | [Educational anchor](anchor.md) |
| Follow a concrete example into the main proof ideas | [Source-to-project bridge](bridge.md) |
| See the complete conceptual dependency structure | [Thirty-milestone map](milestones.md) |
| Read exact definitions, theorem statements, and proofs | [Scientific account](../science/README.md) |
| Separate inherited tools from the additional result | [Related work and attribution](../references/RELATED_WORK.md) |

The [bridge](bridge.md) is a connected first route through the physical task, a four-qubit example, and the two coding directions. The [milestone map](milestones.md) gives stable understanding targets and dependencies for the same story. Each record points to the canonical statement, proof, or example, so a reader can move directly from a conceptual question to the scientific account.

## Why the map has two phases

The map contains exactly **M01–M30**, allocated as **12 background/preliminaries milestones** and **18 narrative/innovation milestones**. This allocation follows the proof's structure. Twelve targets assemble the quantum objects, communication resources, error criterion, and coding language into the complete operational problem. The longer second phase follows the deletion-specific chain: individual pattern overlaps, a uniform spectral estimate, bounds for every encoder, an explicit construction, and the asymptotic interpretation.

| Part of the map | Conceptual development |
|---|---|
| [M01–M06](milestones.md#m01) | Individual carriers and quantum channels become the state representations and spectral quantities used in the proof. |
| [M07–M12](milestones.md#m07) | Entanglement, communication conversions, errors, and packing assemble into one precise capacity problem. |
| [M13–M20](milestones.md#m13) | A local overlap between two deletion patterns becomes an operator-norm bound uniform in block length and deletion count. |
| [M21–M26](milestones.md#m21) | That bound and a one-string construction determine finite-block transmission limits, including the fixed-error sparse-deletion law. |
| [M27–M30](milestones.md#m27) | Length fluctuations, asymptotic limits, and attribution assemble the capacity conclusion and its physical scope. |

Each phase moves from local objects to a global synthesis. The milestones describe the project's core scientific story; specialist calculations remain in the linked proofs.

## The result and the model travel together

For qubits, the leading small-deletion law is

```math
Q_E^{\mathrm{del}}(p;2)
=1-\frac p2\log_2\frac1p+O(p),
\qquad p\downarrow0.
```

Here $`p`$ is the independent deletion probability per carrier. A code sends one string whose supplied length is fixed independently of the message. The receiver obtains the survivors in order and their final length. Every marker is charged as an input carrier; deleted-position flags, internal frame boundaries, arrival-time labels, feedback, and a message-bearing classical side channel are absent. Preshared entanglement is unlimited, the encoder and decoder may act collectively, and the error criterion is stable under adjoining an arbitrary reference. The construction states its entanglement consumption explicitly and makes no efficient-decoding claim. These conventions are fixed in the [operational model](../science/model.md).

The finite-block sparse-deletion statement has a **fixed target error strictly between zero and one**. The capacity statement first takes long-code limits at each fixed deletion probability, then examines small deletion probability. The [strong converse](../science/coding-theorems.md#strong-converse-above-the-explicit-upper-bound) applies to rates strictly above the explicit upper bound; the exact capacity at a general positive deletion probability remains undetermined. The [coding theorems](../science/coding-theorems.md) retain the exact error constants, integer rounding, and clipped all-probability bounds.
