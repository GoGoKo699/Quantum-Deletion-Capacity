# Thirty milestones for quantum deletion capacity

This is the common understanding map for the project's scientific account. It contains exactly **M01–M30**, with stable conceptual targets, earlier dependencies, and pointers to their authoritative sources. The selected educational anchor is [Wilde's _Quantum Information Theory_](anchor.md#selected-source), using the pinned author manuscript arXiv:1106.1445v8. Section numbers below refer to that manuscript. The [focused reading route](anchor.md#focused-reading-route) locates them, and the [bridge](bridge.md) explains how they connect to this project.

The allocation is **12 background/preliminaries milestones** followed by **18 narrative/innovation milestones**. The first phase builds from one carrier to a complete communication problem. The second needs more room because the result connects several distinct steps: local alignment geometry, a uniform matrix bound, a converse for arbitrary encoders, direct coding on one string, and asymptotic conclusions. This allocation follows those dependencies rather than the anchor's chapter divisions. The final milestone in each phase integrates its earlier material.

The map covers the central scientific story. Exact constants, boundary cases, and specialist calculations have one authoritative home in the linked science files. Wilde supplies the named foundations; the local science files supply the deletion-specific arguments. Primary research cited through [Related work](../references/RELATED_WORK.md) records attribution and imported proof ingredients.

## Phase I: background/preliminaries

<a id="m01"></a>

### M01 — One carrier and the loss of a subsystem

**Phase:** Background/preliminaries.

**Central question:** What mathematical operation represents a quantum carrier disappearing?

**Understanding target:** Identify a carrier's finite-dimensional state space, a string's tensor-product space, and the partial trace over missing subsystems. Explain why tracing out a carrier also removes access to its correlations with the retained systems.

**Dependencies and story role:** No earlier milestone. This fixes the smallest physical operation from which the channel is built.

**Conceptual connection:** Physical loss becomes a quantum channel on states, including states entangled with other carriers.

**Source pointers:** Wilde, §4.4; [one transmitted string](../science/model.md#one-transmitted-string); [notation and assumptions](anchor.md#notation-and-assumptions).

<a id="m02"></a>

### M02 — Relative order and missing position information

**Phase:** Background/preliminaries.

**Central question:** What can the receiver infer from an ordered survivor string and its final length?

**Understanding target:** Distinguish the survivor order, the original carrier positions, and the deletion count. Explain the extra information provided by position-labelled erasure and why free internal frame boundaries would change the deletion channel.

**Dependencies and story role:** [M01](#m01). The local loss operation now has an explicitly specified observable output.

**Conceptual connection:** A channel is determined by both its surviving quantum systems and the classical side information made available with them.

**Source pointers:** Wilde, §4.5; [one transmitted string](../science/model.md#one-transmitted-string); [resource and scope boundaries](../science/model.md#resource-and-scope-boundaries); [the physical task](bridge.md#the-physical-task).

<a id="m03"></a>

### M03 — Quantum messages and untouched references

**Phase:** Background/preliminaries.

**Central question:** What must a transmission preserve when the message is entangled with another system?

**Understanding target:** Describe the message, an untouched reference, and a completely positive trace-preserving encoding-channel-decoding composition. Explain why preserving a chosen collection of isolated input states is weaker than preserving an arbitrary quantum message with its correlations.

**Dependencies and story role:** [M01](#m01)–[M02](#m02). The physical channel becomes a task of transmitting quantum information.

**Conceptual connection:** Complete positivity and reference systems connect local operations to the correctness of a full quantum communication protocol.

**Source pointers:** Wilde, §§4.4, 5.1–5.2; [entanglement-assisted quantum codes](../science/model.md#entanglement-assisted-quantum-codes).

<a id="m04"></a>

### M04 — Maximally entangled pairs and moving an operator

**Phase:** Background/preliminaries.

**Central question:** Why can an operation on one half of a maximally entangled pair be represented on the other half?

**Understanding target:** Recognize the normalized maximally entangled state and its maximally mixed marginals. Understand the transpose identity, including which basis defines the transpose and which subsystem remains untouched.

**Dependencies and story role:** [M03](#m03). This introduces the common algebraic object behind channel representations, Weyl encoding, teleportation, and dense coding.

**Conceptual connection:** The same entangled pair serves as a communication resource and as a probe that represents an entire channel.

**Source pointers:** Wilde, §§3.8, 5.1 and Chapter 6; [one-block Weyl support packing](../science/coding-theorems.md#one-block-weyl-support-packing); [dense coding](../science/coding-theorems.md#dense-coding-for-the-converse).

<a id="m05"></a>

### M05 — Three representations of a noisy channel

**Phase:** Background/preliminaries.

**Central question:** How do Kraus operators, an environment, and a Choi state describe the same channel?

**Understanding target:** Relate a Kraus representation to an isometric dilation and to the normalized Choi state. Explain why the Choi state and the complementary output for a maximally mixed input have the same nonzero spectrum, while the environment's basis labels need not be observable at the receiver.

**Dependencies and story role:** [M03](#m03)–[M04](#m04). The communication task gains the matrix representations used by both proof directions.

**Conceptual connection:** A purification turns a channel question into a spectral question about either side of a bipartite state.

**Source pointers:** Wilde, §§4.5, 5.1–5.2; [channel and normalization](../science/alignment-spectrum.md#1-channel-and-normalization).

<a id="m06"></a>

### M06 — Support size and largest eigenvalue do different jobs

**Phase:** Background/preliminaries.

**Central question:** Which features of a received state help construct a code, and which constrain every code?

**Understanding target:** Distinguish the support projector, rank, purity, and operator norm of a positive matrix. Identify support size as the quantity used in the packing construction and the largest Choi eigenvalue as the quantity needed for the universal converse.

**Dependencies and story role:** [M05](#m05). The state representations now have precise quantitative purposes.

**Conceptual connection:** Counting dimensions and controlling the weight in the most concentrated direction provide complementary information about distinguishability.

**Source pointers:** Wilde, §§16.3–16.4 for support-based packing; [alignment spectrum](../science/alignment-spectrum.md); [one-block Weyl support packing](../science/coding-theorems.md#one-block-weyl-support-packing).

<a id="m07"></a>

### M07 — Preshared entanglement and the absence of signalling

**Phase:** Background/preliminaries.

**Central question:** What does entanglement assistance allow before any carrier is transmitted?

**Understanding target:** Describe an arbitrary preshared state independent of the message and reference, followed by local encoding. Explain why local trace-preserving operations leave the receiver's initial marginal independent of the message, and why preshared entanglement supplies no message-bearing classical channel by itself.

**Dependencies and story role:** [M03](#m03)–[M04](#m04). This fixes the assistance model before comparing communication rates.

**Conceptual connection:** No signalling is the operational reason a replacer channel will later erase the advantage of every possible encoder.

**Source pointers:** Wilde, §21.3 and §22.1; [entanglement-assisted quantum codes](../science/model.md#entanglement-assisted-quantum-codes); [auxiliary classical codes](../science/model.md#auxiliary-classical-codes).

<a id="m08"></a>

### M08 — Teleportation and dense coding as resource conversions

**Phase:** Background/preliminaries.

**Central question:** Why do entanglement-assisted classical and quantum message sizes differ by a factor of two in their logarithms?

**Understanding target:** Account for a maximally entangled pair, a quantum system, and the classical correction labels in the unit protocols. A quantum message of dimension K requires K squared teleportation labels, all of which must be carried by the allowed communication channel.

**Dependencies and story role:** [M04](#m04), [M07](#m07). This establishes the resource conversion that will transfer the finite classical bounds to quantum transmission.

**Conceptual connection:** The factor one-half in the final quantum rate combines a standard communication conversion with a deletion-specific classical bound.

**Source pointers:** Wilde, Chapter 6 and §22.1; [exact conversions](../science/coding-theorems.md#exact-conversions-between-classical-and-quantum-codes); [why quantum rates have a factor of one-half](bridge.md#why-quantum-rates-have-a-factor-of-one-half).

<a id="m09"></a>

### M09 — Error that remains meaningful with a reference

**Phase:** Background/preliminaries.

**Central question:** How can the performance of a quantum code be stated without choosing a preferred input message?

**Understanding target:** Distinguish half-diamond error from squared-overlap entanglement fidelity. Understand that one minus entanglement fidelity is bounded above by half-diamond error in general; equality in the construction comes from its particular random-Weyl form.

**Dependencies and story role:** [M03](#m03)–[M04](#m04), [M08](#m08). Resource conversions now have an explicit quantum error criterion.

**Conceptual connection:** A reference-stable channel distance makes the communication claim valid when the transmitted system participates in a larger quantum task.

**Source pointers:** Wilde, Chapter 9, especially §9.5; [error conventions](../science/model.md#entanglement-assisted-quantum-codes); [exact conversions](../science/coding-theorems.md#exact-conversions-between-classical-and-quantum-codes).

<a id="m10"></a>

### M10 — Distinguishing a finite ensemble by its supports

**Phase:** Background/preliminaries.

**Central question:** How does a collective measurement decode many nonorthogonal received states?

**Understanding target:** Explain the square-root measurement built from support projectors and the roles of its self-error and cross-error terms. Understand how the Hayashi–Nagaoka inequality converts overlap control into an average classical decoding bound and why a zero self-error term is useful here.

**Dependencies and story role:** [M05](#m05)–[M06](#m06), [M09](#m09). This supplies the decoding tool needed to turn a state ensemble into an achievable rate.

**Conceptual connection:** A small expected overlap between independently selected codewords yields the existence of a deterministic codebook with small average error.

**Source pointers:** Wilde, §§16.3–16.4, including Lemma 16.4.1; [one-block Weyl support packing](../science/coding-theorems.md#one-block-weyl-support-packing); [standard coding ingredients](../references/RELATED_WORK.md#standard-coding-ingredients).

<a id="m11"></a>

### M11 — Pattern counts, binary entropy, and concentration

**Phase:** Background/preliminaries.

**Central question:** How does a finite number of possible deletion patterns become a rate penalty?

**Understanding target:** Relate the binomial number of patterns at a fixed deletion count to binary entropy at a fixed deletion fraction. Distinguish this pattern count from the binomial probability of that count, and explain why independent deletions concentrate in a window of counts as the string grows.

**Dependencies and story role:** [M02](#m02), [M06](#m06). This prepares the transition from one-block matrix and coding bounds to asymptotic rates.

**Conceptual connection:** Entropy describes the exponential growth of possible alignments; the spectral proof is needed to establish how their coherent overlaps affect communication.

**Source pointers:** [independent deletions](../science/model.md#independent-deletions); [achievability and the order of limits](../science/coding-theorems.md#achievability-and-the-order-of-limits); Wilde, §21.3 for the asymptotic coding framework.

<a id="m12"></a>

### M12 — The complete operational problem

**Phase:** Background/preliminaries.

**Central question:** What exactly is being optimized when this project speaks of deletion capacity?

**Understanding target:** Assemble fixed carrier dimension, one message-independent input length, ordered survivors, observable final length, unlimited preshared entanglement, arbitrary collective operations, and vanishing half-diamond error into one code sequence. State the rate in logical qubits per supplied carrier using a lower limit of the block rates.

**Dependencies and story role:** [M01](#m01)–[M11](#m11). This integrates the foundations into the precise task studied throughout the narrative phase.

**Conceptual connection:** A capacity formula acquires its physical meaning only together with its observable output, resource charges, error convention, and order of limits.

**Source pointers:** Wilde, §21.3 and §22.1; [operational model](../science/model.md), especially [rate and capacity](../science/model.md#rate-and-capacity); [the physical task](bridge.md#the-physical-task).

## Phase II: narrative/innovation

<a id="m13"></a>

### M13 — A fixed deletion count as the local channel

**Phase:** Narrative/innovation.

**Central question:** How can the random-length channel be resolved into components that admit an exact analysis?

**Understanding target:** Specify the uniform fixed-count channel, its ordered output, and its Kraus labels for a deleted subset and a deleted symbol word. Explain why conditioning independent deletions on their count gives this channel and why the branch probabilities are independent of the encoded state.

**Dependencies and story role:** [M05](#m05), [M11](#m11)–[M12](#m12). The second phase starts from a single fully specified channel component.

**Conceptual connection:** The receiver's final-length information permits a branch decomposition without revealing the hidden positions inside each branch.

**Source pointers:** [channel and normalization](../science/alignment-spectrum.md#1-channel-and-normalization); [one transmitted string](../science/model.md#one-transmitted-string).

<a id="m14"></a>

### M14 — Two nearby deletions in a four-qubit string

**Phase:** Narrative/innovation.

**Central question:** What overlap remains between two different deletion patterns?

**Understanding target:** Follow the patterns deleting position 2 or position 3 from four qubits. Identify the one mismatched survivor rank, distinguish the relative factor one-half from the normalized Gram block, and explain how off-diagonal blocks survive even though pattern labels form an orthogonal basis.

**Dependencies and story role:** [M05](#m05)–[M06](#m06), [M13](#m13). A complete small example exposes the local mechanism that the general proof must control.

**Conceptual connection:** Hidden patterns cannot simply be treated as an incoherent list of distinguishable classical errors when evaluating the channel spectrum.

**Source pointers:** [four-carrier example](../science/interpretation.md#a-four-carrier-alignment-example); [four qubits and one deletion](bridge.md#four-qubits-and-one-deletion); [single-deletion spectrum](../science/alignment-spectrum.md#4-a-single-deletion).

<a id="m15"></a>

### M15 — The order-preserving contraction graph

**Phase:** Narrative/innovation.

**Central question:** Why does preserving survivor order make the overlap calculation tractable?

**Understanding target:** Form the increasing partial bijection between equal output ranks of two survivor lists. Explain why its components are paths or fixed loops, and how paths constrain deleted symbols while fixed loops contribute free symbol sums.

**Dependencies and story role:** [M13](#m13)–[M14](#m14). The toy overlap becomes a structural fact valid for every pair of patterns.

**Conceptual connection:** Relative order imposes a strong restriction on a tensor contraction that would have a different geometry under arbitrary positional scrambling.

**Source pointers:** [permutation-block identity](../science/alignment-spectrum.md#2-the-exact-permutation-block-identity); [ordered Hayden–Preskill antecedent](../references/RELATED_WORK.md#ordered-haydenpreskill-recovery).

<a id="m16"></a>

### M16 — Keeping the deleted symbols gives permutation blocks

**Phase:** Narrative/innovation.

**Central question:** What matrix structure is lost if only a scalar overlap statistic is retained?

**Understanding target:** Explain why a Gram block is a positive scalar, determined by mismatched survivor ranks, times a permutation of deleted symbol words. Track the normalization by the number of patterns and deleted-word dimension, and recognize that several deletions can produce nontrivial permutations.

**Dependencies and story role:** [M05](#m05), [M15](#m15). This upgrades the graph calculation into the exact matrix identity needed for an operator-norm estimate.

**Conceptual connection:** Retaining the environment's symbol structure preserves the information required to bound the largest eigenvalue, beyond a purity calculation.

**Source pointers:** [exact permutation-block identity](../science/alignment-spectrum.md#2-the-exact-permutation-block-identity); [contribution after attribution](../references/RELATED_WORK.md#contribution-after-attribution).

<a id="m17"></a>

### M17 — From matrix blocks to a scalar alignment matrix

**Phase:** Narrative/innovation.

**Central question:** How can a large block matrix be controlled by weights indexed only by deletion patterns?

**Understanding target:** Use the norm-preserving property of permutation blocks to compare with the nonnegative scalar matrix of alignment weights. Explain the matching lower bound supplied by the uniform deleted-word vector and the subsequent upper bound by the largest scalar row sum.

**Dependencies and story role:** [M06](#m06), [M16](#m16). The spectral problem is reduced to a weighted counting problem with one pattern held fixed.

**Conceptual connection:** A common invariant vector makes the scalar reduction exact at the top eigenvalue, while the row sum offers a tractable uniform upper bound.

**Source pointers:** [alignment geometry and the Choi spectrum](../science/alignment-spectrum.md), especially [counting all alignments from one pattern](../science/alignment-spectrum.md#3-counting-all-alignments-from-one-pattern).

<a id="m18"></a>

### M18 — Mismatch runs are anchored by missing positions

**Phase:** Narrative/innovation.

**Central question:** Why can the sum over many other patterns be organized using the fixed pattern's holes?

**Understanding target:** Identify maximal runs of mismatched survivor ranks between matching anchors, including string boundaries. Explain why every run contains a nonempty consecutive group of holes from the fixed pattern and why different runs use disjoint groups.

**Dependencies and story role:** [M15](#m15), [M17](#m17). This supplies the combinatorial localization that prevents a row bound from growing exponentially in the full string length.

**Conceptual connection:** Global uncertainty in survivor alignment is constrained by local defects in an ordered string.

**Source pointers:** [counting all alignments from one pattern](../science/alignment-spectrum.md#3-counting-all-alignments-from-one-pattern).

<a id="m19"></a>

### M19 — Weighted counting costs exponentially in deletions

**Phase:** Narrative/innovation.

**Central question:** How does the decay with mismatch length offset the number of possible runs?

**Understanding target:** Understand the overcount by hole-group schemes, interval placements, and compatible survivor choices. Explain why the geometrically weighted sum for each group is bounded exponentially in its number of holes, yielding a row-sum bound exponential in the deletion count with a constant independent of block length.

**Dependencies and story role:** [M18](#m18). The local run decomposition produces the quantitative uniform estimate.

**Conceptual connection:** The proof balances combinatorial multiplicity against overlap decay; counting all patterns without their weights would lose the desired positional penalty.

**Source pointers:** [weighted run count and generating function](../science/alignment-spectrum.md#3-counting-all-alignments-from-one-pattern).

<a id="m20"></a>

### M20 — The uniform Choi spectral bound

**Phase:** Narrative/innovation.

**Central question:** Which part of the alignment count survives after all coherent overlaps are included?

**Understanding target:** Interpret the Choi-norm bound as the reciprocal of the deleted-word dimension and the binomial pattern count, multiplied by a constant to the power of the deletion count. Explain why the constant is uniform in block length and why its logarithm contributes only a linear-in-deletions correction.

**Dependencies and story role:** [M13](#m13)–[M19](#m19). This integrates the alignment argument into the main spectral theorem.

**Conceptual connection:** The binomial positional uncertainty remains visible even after coherent pattern overlaps are accounted for, making it available to an operational converse.

**Source pointers:** [spectral theorem](../science/alignment-spectrum.md); [finite-block quantities](../science/coding-theorems.md#finite-block-quantities); [from the spectrum to coding](../science/alignment-spectrum.md#5-from-the-spectrum-to-coding).

<a id="m21"></a>

### M21 — A Choi bound becomes a completely positive comparison

**Phase:** Narrative/innovation.

**Central question:** How can a spectral estimate constrain a channel acting on an arbitrarily entangled input?

**Understanding target:** Translate the normalized Choi operator inequality into domination of the deletion channel by a scalar multiple of the maximally mixed replacer in completely positive order. Explain why this order persists with ancillary systems and why the output-dimension bound provides a useful second cap.

**Dependencies and story role:** [M03](#m03), [M05](#m05), [M20](#m20). The spectral result is converted into a statement applicable inside an arbitrary protocol.

**Conceptual connection:** Complete positivity is the link between a matrix inequality for one channel representation and a constraint valid for every entangled encoding.

**Source pointers:** Wilde, §§4.4–4.5 for channel foundations; [arbitrary-encoder converse by CP domination](../science/coding-theorems.md#arbitrary-encoder-converse-by-cp-domination); [Choi state to universal converse](bridge.md#from-a-choi-state-to-a-universal-converse).

<a id="m22"></a>

### M22 — A converse for every encoder

**Phase:** Narrative/innovation.

**Central question:** Why does the converse apply beyond the particular code used for achievability?

**Understanding target:** Follow arbitrary entangled encoders through the replacer comparison. Use independence of the initial shared state from the classical message and no signalling to obtain replacer success equal to the reciprocal message count, then derive the finite-block success bound with its trivial cap.

**Dependencies and story role:** [M07](#m07), [M21](#m21). This establishes an operational bound on all permitted classical communication strategies.

**Conceptual connection:** A channel-level comparison avoids optimizing over encoder families and supplies the universality needed for a quantum capacity converse.

**Source pointers:** [auxiliary classical codes](../science/model.md#auxiliary-classical-codes); [arbitrary-encoder converse](../science/coding-theorems.md#arbitrary-encoder-converse-by-cp-domination); [fixed-count statement](../science/coding-theorems.md#fixed-count-statement).

<a id="m23"></a>

### M23 — Weyl encodings produce a tractable ensemble

**Phase:** Narrative/innovation.

**Central question:** Which explicit received-state ensemble makes support packing effective?

**Understanding target:** Start with one maximally entangled pair per input carrier, encode using product Weyl operators, and use the transpose identity to express the received states as an orbit of the normalized Choi state. Explain their maximally mixed ensemble average and the Choi support-rank bound.

**Dependencies and story role:** [M04](#m04)–[M06](#m06), [M10](#m10), [M13](#m13). The constructive branch now has an explicit ensemble whose overlaps can be averaged.

**Conceptual connection:** Entanglement and symmetry make a useful code ensemble analyzable without asserting that this input optimizes the deletion channel's capacity.

**Source pointers:** Wilde, Chapter 6 and §§16.3–16.4; [one-block Weyl support packing](../science/coding-theorems.md#one-block-weyl-support-packing).

<a id="m24"></a>

### M24 — Packing messages into one whole string

**Phase:** Narrative/innovation.

**Central question:** How is a communication code obtained without giving the receiver extra block boundaries?

**Understanding target:** Combine the support measurement with Weyl averaging to obtain a finite classical error bound for one length-n input string. Explain why the vanishing self-error and controlled cross terms give a deterministic codebook, and why the argument needs no independently framed subblocks.

**Dependencies and story role:** [M02](#m02), [M10](#m10), [M23](#m23). This supplies achievability in exactly the channel model used by the converse.

**Conceptual connection:** The direct finite-block construction closes the gap between standard packing tools and a synchronization channel whose internal boundaries are unobserved.

**Source pointers:** Wilde, §§16.3–16.4; [one-block Weyl support packing](../science/coding-theorems.md#one-block-weyl-support-packing); [packing one whole string](bridge.md#packing-one-whole-string).

<a id="m25"></a>

### M25 — Quantum coding with exact errors and charged entanglement

**Phase:** Narrative/innovation.

**Central question:** What survives when the finite classical bounds are converted into quantum bounds?

**Understanding target:** Explain why teleportation through the actual classical code gives a random-Weyl channel whose half-diamond error equals the classical error after every decoder outcome is assigned a correction label. Follow dense coding through an arbitrary effective quantum channel to success equal to its entanglement fidelity, without a covariance assumption. Account for the construction's $`n\log_2d+\log_2K`$ ebits, whose consumption is unoptimized, and the integer choice of logical dimension, including dimension one.

**Dependencies and story role:** [M08](#m08)–[M09](#m09), [M22](#m22), [M24](#m24). The two classical bounds become matching quantum statements under the declared error and resource conventions.

**Conceptual connection:** The standard unit protocols transfer the bounds exactly only when correction communication, error definitions, and entanglement charges are tracked together.

**Source pointers:** Wilde, Chapter 6 and §22.1; [exact conversions](../science/coding-theorems.md#exact-conversions-between-classical-and-quantum-codes); [finite-block quantities](../science/coding-theorems.md#finite-block-quantities).

<a id="m26"></a>

### M26 — The finite-block cost of hidden positions

**Phase:** Narrative/innovation.

**Central question:** How much additional logical dimension is lost when a sparse number of deletion locations is hidden?

**Understanding target:** Interpret the optimal log dimension as the surviving-carrier term minus half the logarithm of the binomial pattern count, up to the stated linear-in-deletions remainder. Understand the half-logarithmic block-length loss for one deletion. Keep the fixed carrier dimension, fixed target error strictly between zero and one, and sparse deletion-count regime $`1\le k=o(n)`$ attached to this statement.

**Dependencies and story role:** [M11](#m11), [M20](#m20), [M25](#m25). The finite-block proof becomes a sharp statement of synchronization cost in a concrete regime.

**Conceptual connection:** The cost of locating a rare missing subsystem remains substantial even when its direct dimensional loss is only one carrier.

**Source pointers:** [positional-uncertainty term](../science/interpretation.md#the-positional-uncertainty-term); [fixed-count statement](../science/coding-theorems.md#fixed-count-statement); [finite-length and small-deletion statements](bridge.md#finite-length-and-small-deletion-statements).

<a id="m27"></a>

### M27 — One codebook across fluctuating output lengths

**Phase:** Narrative/innovation.

**Central question:** How does fixed-count achievability become a code for independent deletions?

**Understanding target:** Explain why averaging over codebooks and count branches produces one deterministic codebook shared across the observed lengths, with a decoder selected by final length. Separate the atypical-count error from the packing error and state the order of limits: fix deletion probability and a strict rate gap, choose a suitable window, then let the string length grow.

**Dependencies and story role:** [M11](#m11)–[M13](#m13), [M24](#m24)–[M25](#m25). The construction reaches the physical independent-deletion channel without introducing free framing.

**Conceptual connection:** Observable total length permits branch-dependent decoding while a common encoding preserves the one-string communication model.

**Source pointers:** [independent-deletion statement](../science/coding-theorems.md#independent-deletion-statement); [achievability and the order of limits](../science/coding-theorems.md#achievability-and-the-order-of-limits); Wilde, §21.3 for comparison with standard asymptotic coding.

<a id="m28"></a>

### M28 — Where the proved strong converse begins

**Phase:** Narrative/innovation.

**Central question:** Above which rates does every allowed quantum code fail asymptotically?

**Understanding target:** Combine the branchwise arbitrary-encoder converse with a typical window to show entanglement fidelity tends to zero, and half-diamond error to one, for rates strictly above the explicit upper bound. Distinguish that proved threshold from the still-unknown exact capacity and preserve the strict inequality on rate.

**Dependencies and story role:** [M09](#m09), [M11](#m11), [M21](#m21)–[M22](#m22), [M25](#m25), [M27](#m27). The finite-block universality becomes a global asymptotic impossibility statement.

**Conceptual connection:** A strong converse is a claim about the limiting error of every code; its threshold must be tied to the bound actually established.

**Source pointers:** [strong converse above the explicit upper bound](../science/coding-theorems.md#strong-converse-above-the-explicit-upper-bound); [rate and capacity](../science/model.md#rate-and-capacity).

<a id="m29"></a>

### M29 — The all-probability sandwich and the small-deletion law

**Phase:** Narrative/innovation.

**Central question:** Which asymptotic feature is determined even though the exact capacity remains unknown?

**Understanding target:** Read the lower bound clipped at zero and the upper bound clipped by the position-labelled erasure benchmark. Explain why their gap is at most linear in deletion probability for fixed carrier dimension, so the leading positional cost has coefficient one-half multiplying the small-deletion binary-entropy term. Take the small-probability limit after defining capacity at each fixed probability.

**Dependencies and story role:** [M08](#m08), [M11](#m11)–[M12](#m12), [M20](#m20), [M27](#m27)–[M28](#m28). The construction and converse combine into the main capacity conclusion.

**Conceptual connection:** Matching a nonanalytic leading term can settle the dominant physical cost without determining the full capacity curve or its linear correction.

**Source pointers:** [capacity sandwich](../science/coding-theorems.md#capacity-sandwich); [leading synchronization penalty](../science/coding-theorems.md#leading-synchronization-penalty); [from one block to independent deletion](../science/interpretation.md#from-one-block-to-independent-deletion).

<a id="m30"></a>

### M30 — The complete mechanism, its contribution, and its limits

**Phase:** Narrative/innovation.

**Central question:** What does the full argument establish about the physical cost of hidden positions?

**Understanding target:** Connect ordered pattern overlaps, the uniform Choi bound, the arbitrary-encoder converse, and one-string packing to the half-entropy quantum penalty. Separate the inherited overlap geometry, packing inequality, and unit protocols from the added uniform spectral estimate and its transmission consequence. Keep unlimited, explicitly charged but unoptimized entanglement, unrestricted decoding, the fixed-error corollary, and the proved strong-converse threshold visible when discussing implications.

**Dependencies and story role:** [M12](#m12)–[M29](#m29). This integrates the narrative into the complete scientific conclusion and its remaining questions.

**Conceptual connection:** Relative order preserves an extensive communication rate, while unobserved positions impose a measurable additional cost; exact positive-probability capacity, the sharp linear term, limited entanglement, and efficient decoding remain separate problems.

**Source pointers:** [interpretation and remaining questions](../science/interpretation.md); [contribution after attribution](../references/RELATED_WORK.md#contribution-after-attribution); [what the result does and does not explain](bridge.md#what-the-result-does-and-does-not-explain); [source and result boundaries](anchor.md#source-and-result-boundaries).
