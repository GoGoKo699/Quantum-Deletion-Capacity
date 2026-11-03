# Related work and attribution

This account distinguishes standard communication tools, prior quantum deletion results, and the uniform spectral estimate used in the [coding theorem](../science/coding-theorems.md). The compared operational model has fixed carrier dimension, one transmitted string, hidden deletion positions, observable final length, and unlimited preshared entanglement. Its leading small-deletion rate does not resolve the general exact adversarial deletion-code problem.

## Standard coding ingredients

**Hayashi and Nagaoka, “General formulas for capacity of classical-quantum channels,” IEEE Transactions on Information Theory 49, 1753–1768 (2003).** [Primary preprint](https://arxiv.org/abs/quant-ph/0206186), [DOI](https://doi.org/10.1109/TIT.2003.813556).

Lemma 2 is the operator inequality used for the square-root measurement. With parameter one, the self-error term has coefficient two and the cross terms have coefficient four. In this project's support-projector packing proof, the self term is zero and independent Weyl averaging bounds each cross term. The inequality and the general packing method are inherited; the proof here applies them directly to one deletion string and a single codebook shared across all observed output lengths.

**Bennett, Shor, Smolin and Thapliyal, “Entanglement-assisted capacity of a quantum channel and the reverse Shannon theorem,” IEEE Transactions on Information Theory 48, 2637–2655 (2002).** [Primary preprint](https://arxiv.org/abs/quant-ph/0106052), [DOI](https://doi.org/10.1109/TIT.2002.802612).

This is a foundational source for entanglement-assisted capacity and its relation to quantum communication. The flagged erasure benchmark follows from this framework. The present deletion proof does not obtain one-string achievability by repeatedly using an independently framed block channel. It supplies direct finite-block coding and writes out the teleportation and dense-coding conversions, including their error metrics and entanglement charges.

## Classical small-deletion capacity

**Kanoria and Montanari, “On the deletion channel with small deletion probability,” ISIT 2010, 1002–1006.** [Primary preprint, arXiv:0912.5176v3](https://arxiv.org/abs/0912.5176v3), [author-hosted paper](https://web.stanford.edu/~montanar/RESEARCH/FILEPAP/del_arxiv.pdf).

The classical binary deletion channel already has a nonanalytic capacity loss with leading coefficient one in front of $`p\log_2(1/p)`$. A logarithmic synchronization penalty is therefore an established phenomenon. This project determines the coefficient one-half for entanglement-assisted quantum transmission and supplies a converse that permits arbitrary quantum encodings. It does not transfer a classical converse by restricting quantum inputs to basis states.

## Quantum synchronization constructions

**Leahy, Touchette and Yao, “Quantum Insertion-Deletion Channels,” arXiv:1901.00984v1 (2019).** [Primary paper](https://arxiv.org/abs/1901.00984v1).

This paper develops quantum insertion-deletion models and synchronization-string reductions. Its Theorem 5.1 includes a fixed-qubit construction: an adversarial fraction $`\delta`$ of insertion-deletion errors is converted into corruption/erasure errors with overhead of order $`\sqrt{\delta\log(1/\delta)}`$. Thus quantum synchronization methods cannot all be dismissed as enlarged-alphabet constructions. That result supplies neither the small-$`p`$ entanglement-assisted capacity coefficient nor the arbitrary-encoder converse established here. Section 6 discusses improving the unoptimized bounds.

**Matsumoto and Hagiwara, “Constructions of $`\ell`$-Adic $`t`$-Deletion-Correcting Quantum Codes,” IEICE Transactions on Fundamentals E105-A, 571–575 (2022).** [Primary preprint, arXiv:2102.04230v2](https://arxiv.org/abs/2102.04230v2), [journal paper](https://doi.org/10.1587/transfun.2021EAP1034).

The useful erasure-to-deletion construction adds cyclic positional labels, changing $`\ell`$-level carriers into $`(t+1)\ell`$-level carriers. The entanglement-assisted extension in Section 4.5 retains that enlarged alphabet. This is a genuine deletion-correction construction, but its rate cannot be inserted unchanged into a fixed-qubit small-deletion capacity statement. Its other, arbitrary-dimension construction corrects one deletion at asymptotically vanishing rate.

## Ordered Hayden–Preskill recovery

**Alencar, Moreira and Silva, “Microscopic Side Information Controls Ordered Hayden–Preskill Recovery,” arXiv:2607.15537v1 (2026).** [Primary record](https://arxiv.org/abs/2607.15537v1), [author-uploaded full text](https://www.researchgate.net/publication/410594495_Microscopic_Side_Information_Controls_Ordered_Hayden--Preskill_Recovery).

Appendix A uses the same ordered fixed-survivor channel. Its Lemma 6 evaluates the Choi purity by counting coincidences between equal survivor ranks. The contraction graph is order preserving, so only fixed-point cycles contribute. This overlap geometry is a direct antecedent and is credited in the [spectral proof](../science/alignment-spectrum.md).

The inspected recovery theorem fixes the diary size and considers a sparse-survivor regime, with a threshold at survivor count of order $`n^{2/3}`$. The present capacity problem instead retains nearly all carriers and transmits an extensive message. Retaining the deleted symbol words produces exact permutation Gram blocks; bounding every row of their scalar overlap matrix then yields a uniform Choi operator-norm estimate. That estimate controls arbitrary entangled encoders. The purity identity and sparse-survivor estimates do not supply this low-deletion transmission bound by themselves.

## Broader deletion-code context

**Hagiwara, “Introduction to Quantum Deletion Error-Correcting Codes,” IEICE Transactions on Fundamentals E108-A, 363–375 (2025).** [Primary review](https://globals.ieice.org/en_transactions/fundamentals/10.1587/transfun.2024TAI0001/_f), [DOI](https://doi.org/10.1587/transfun.2024TAI0001).

Section 5.3 and Problem 21 discuss the limited general bounds available for quantum deletion codes. This supplies context, not a certificate that no later relevant theorem exists. The current result addresses stochastic transmission with entanglement assistance, rather than the exact optimum of adversarial deletion codes.

**Bulled and Ouyang, “The equivalence of quantum deletion and insertion errors on permutation-invariant codes” (2026).** [Primary preprint](https://arxiv.org/abs/2602.08780), [journal article](https://doi.org/10.1038/s41534-026-01371-3).

Its equivalences concern permutation-invariant codes. That restriction and correction question differ from arbitrary-encoder high-rate entanglement-assisted transmission through ordered deletion. The comparison here uses the official abstract and inspected source material; it does not rely on an unverified full-text capacity claim.

## Relation to full positional scrambling

[Quantum-Permutation-Noise-Limits](https://github.com/GoGoKo699/Quantum-Permutation-Noise-Limits/blob/1ae12780408c9b120a90a6dd55b1ea1fe74d62cd/science/model.md) studies full positional twirling followed by local noise, including erasure. That twirl discards relative order, whereas ordered deletion retains it. The noisy two-way-assisted model in that account also starts without preshared ebits. Missing positional information is a common physical issue, but the channel and assistance model are different. A capacity ceiling for the fully twirled channel does not establish the extensive ordered-deletion rate considered here.

## Contribution after attribution

The contribution is the uniform bound

```math
\|J_{n,k}\|_\infty
\le\frac{C_d^k}{d^k\binom nk},
```

its arbitrary-encoder completely-positive-order converse, and a one-string construction with a matching leading synchronization cost. The overlap geometry, square-root measurement inequality, and entanglement-assisted communication conversions are inherited ingredients. The scientific distinction is the resulting fixed-dimensional capacity law with an explicit operational model and finite-error bounds. This source comparison is bounded; it is not an exhaustive priority certificate.
