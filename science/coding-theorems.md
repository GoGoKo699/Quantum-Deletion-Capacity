# Coding bounds and the small-deletion capacity law

We use the [one-string operational model](model.md): $`n`$ supplied $`d`$-level carriers, preserved survivor order, observable final length, unrestricted preshared entanglement, and no internal frame labels or feedback. All logarithms are base two.

The [alignment-spectrum theorem](alignment-spectrum.md) supplies the only deletion-specific estimate needed for the converse. The coding arguments below keep all error constants and message-dimension rounding explicit. General coding ingredients and the closest deletion-channel results are credited in [related work](../references/RELATED_WORK.md).

## Finite-block quantities

Write $`m=n-k`$, $`c_{n,k}=\binom nk`$, and

```math
C_d=\frac{6}{(1-1/d)^3}\leq48.
```

Define

```math
a_{n,k}=c_{n,k}d^{-2(n-k)}
```

and the converse coefficient

```math
\Lambda_{n,k}
=\min\left\{
d^{2(n-k)},\,
\frac{d^{2(n-k)}C_d^k}{c_{n,k}}
\right\}.
```

The first term in $`\Lambda_{n,k}`$ is the output-dimension bound. The second is the alignment bound. The estimates are useful without optimizing the constant $`C_d`$.

### Fixed-count statement

For every integer $`M\geq1`$, there is an entanglement-assisted classical code for $`\mathcal N_{n,k}`$ whose average error satisfies

```math
\overline e\leq
\min\{1,\,4(M-1)a_{n,k}\}.
```

For every integer $`K\geq1`$, there is an entanglement-assisted quantum code with

```math
\epsilon_\diamond\leq
\min\{1,\,4(K^2-1)a_{n,k}\}.
```

In particular, for a prescribed $`0\lt \epsilon\lt 1`$, the integer

```math
K_{\mathrm{ach}}
=\left\lfloor
\sqrt{1+\frac{\epsilon}{4a_{n,k}}}
\right\rfloor
```

is achievable with $`\epsilon_\diamond\leq\epsilon`$. It is always at least one. This expression is a sufficient code size, not an exact finite-block optimum. At $`k=0`$, the identity channel separately achieves $`K=d^n`$ exactly.

Every entanglement-assisted classical $`M`$-label code obeys

```math
P_{\mathrm{succ}}\leq
\min\{1,\Lambda_{n,k}/M\}.
```

Every $`K`$-dimensional effective quantum channel obtained from such a transmission obeys

```math
F_e(\mathcal T)
\leq\min\{1,\Lambda_{n,k}/K^2\}.
```

Consequently, $`\epsilon_\diamond\leq\epsilon\lt 1`$ requires

```math
\begin{aligned}
\log_2 K
&\leq(n-k)\log_2 d\\
&\quad-\frac12\max\{0,\log_2c_{n,k}-k\log_2C_d\}\\
&\quad+\frac12\log_2\frac1{1-\epsilon}.
\end{aligned}
```

Equivalently, $`K\leq\lfloor\sqrt{\Lambda_{n,k}/(1-\epsilon)}\rfloor`$. The statements include $`K=1`$ and $`k=n`$; the empty-string channel cannot communicate a nontrivial message reliably.

### Independent-deletion statement

For $`q_k=q_{n,p}(k)`$, choose any set $`T\subseteq\{0,\ldots,n\}`$ of deletion counts. Put

```math
\tau_T=\sum_{k\notin T}q_k,
\qquad
\beta_T=\sum_{k\in T}q_k a_{n,k}.
```

For every integer $`K\geq1`$, a single codebook and a decoder conditioned only on the final length achieve

```math
\epsilon_\diamond
\leq\min\{1,\tau_T+4(K^2-1)\beta_T\}.
```

When $`\tau_T\lt \epsilon\lt 1`$ and $`\beta_T>0`$, a valid integer choice is

```math
K_{\mathrm{ach}}
=\left\lfloor
\sqrt{1+\frac{\epsilon-\tau_T}{4\beta_T}}
\right\rfloor.
```

The trivial $`K=1`$ message can always be transmitted with zero error, independently of this sufficient bound. The classical version replaces $`K^2-1`$ by $`M-1`$.

For every quantum code, the finite-block converse is

```math
F_e(\mathcal T)
\leq
\sum_{k=0}^n q_k
\min\{1,\Lambda_{n,k}/K^2\}.
```

Thus $`\epsilon_\diamond\leq\epsilon`$ implies that the right-hand side is at least $`1-\epsilon`$. This branchwise form remains useful when a typical-window asymptotic is inappropriate.

## One-block Weyl support packing

Let $`D_A=d^n`$ and $`D_B=d^{n-k}`$. The normalized Choi state is

```math
J_{n,k}
=(\mathrm{id}_{D_A}\otimes\mathcal N_{n,k})(\Phi_{D_A}).
```

The receiver's marginal is $`I_B/D_B`$. There are $`c_{n,k}d^k`$ partial-inner-product Kraus operators, so

```math
\mathrm{rank}J_{n,k}\leq c_{n,k}d^k.
```

The sender and receiver share $`n`$ maximally entangled $`d`$-level pairs. Choose each classical codeword independently from the product Weyl operators on the sender's $`n`$ halves. If the chosen Weyl is $`U`$, the received state is

```math
\rho_{U,k}
=(U^{\mathsf T}\otimes I_B)J_{n,k}
(U^*\otimes I_B).
```

The transpose acts on the receiver's retained halves. Weyl averaging gives

```math
\mathbb E_U\rho_{U,k}
=\frac{I_R}{D_A}\otimes\frac{I_B}{D_B}
=\frac{I_{RB}}{D_AD_B}.
```

This is a statement about the average of the received states; no covariance of the deletion channel is required.

For a codebook of $`M`$ words, let $`\Pi_{j,k}`$ be the support projector of its $`j`$th received state. Use the square-root measurement formed from these projectors, with the inverse defined on the support of their sum. Complete any unused measurement subspace to one fixed message label. The [Hayashi–Nagaoka inequality, Lemma 2](https://arxiv.org/abs/quant-ph/0206186), gives

```math
\overline e_k
\leq\frac4M
\sum_{i=1}^M\sum_{j\ne i}
\mathrm{Tr}(\rho_{i,k}\Pi_{j,k}).
```

The self-error term vanishes because $`\Pi_{i,k}`$ contains the support of $`\rho_{i,k}`$. For $`i\ne j`$, the two codewords are independent. Averaging $`\rho_{i,k}`$ while holding $`\Pi_{j,k}`$ fixed gives

```math
\mathbb E\mathrm{Tr}(\rho_{i,k}\Pi_{j,k})
=\frac{\mathrm{rank}J_{n,k}}{D_AD_B}
\leq\frac{c_{n,k}d^k}{d^{2n-k}}
=a_{n,k}.
```

It follows that $`\mathbb E\overline e_k\leq4(M-1)a_{n,k}`$. Some deterministic codebook therefore satisfies the fixed-count bound. The codebook is fixed independently of the message; its probabilistic existence does not supply a message-bearing side channel.

For independent deletions, use the same sampled codebook at every possible output length. On lengths indexed by $`T`$, use the corresponding support measurement; outside $`T`$, output a fixed label. Averaging the total error over both the codebook and the channel gives

```math
\mathbb E\overline e
\leq\tau_T+4(M-1)\beta_T.
```

Hence one codebook attains this total bound. It need not be separately optimal at each length. There is one transmitted string, one final output length, and one length-dependent decoding measurement. No internal block boundaries enter the construction.

## Exact conversions between classical and quantum codes

These conversions identify which error criterion is proved and account for the extra entanglement. They do not add a free classical communication channel.

### Teleportation for achievability

Take a classical code with the complete alphabet of $`K^2`$ teleportation correction labels, and average error $`\overline e`$ under the uniform prior. In addition to the entanglement used by that classical code, share one maximally entangled pair of Schmidt rank $`K`$, costing $`\log_2K`$ ebits.

The sender performs the generalized Bell measurement for teleportation and sends its label through the classical deletion-channel code. Every label is uniform with probability $`1/K^2`$, for every quantum message and reference. The receiver applies the correction indicated by the decoded label.

If $`P(\widehat j\mid j)`$ denotes the classical transition probabilities, the resulting quantum channel is a mixture of Weyl errors. Correct decoding contributes the identity channel with total probability $`1-\overline e`$; every wrong label contributes a nonidentity Weyl. Their maximally entangled Choi states are orthogonal. Therefore

```math
F_e(\mathcal T)=1-\overline e,
\qquad
\epsilon_\diamond(\mathcal T)=\overline e.
```

For the diamond norm, the upper bound follows by convexity and the lower bound follows by testing a maximally entangled input, whose erroneous Weyl components are orthogonal to the target. If only an upper bound $`\overline e\leq\epsilon`$ is known, both desired error guarantees follow with that same $`\epsilon`$.

Any classical abort must first be completed to a definite correction label. The equality concerns the actual error of this complete decoder; an error bound that counted an abort can only be more conservative.

The construction uses $`n\log_2d+\log_2K`$ ebits in total. This entanglement cost is not optimized. All $`K^2`$ correction labels are communicated through the length-$`n`$ deletion transmission.

### Dense coding for the converse

Let an arbitrary entanglement-assisted quantum code induce $`\mathcal T`$ on a $`K`$-dimensional register. Add one maximally entangled pair of Schmidt rank $`K`$. To send label $`j\in\{1,\ldots,K^2\}`$, apply a Weyl $`W_j`$ to the sender's half, pass that half through the quantum code, and perform the generalized Bell measurement at the receiver.

The identity

```math
(I\otimes W_j)|\Phi_K\rangle
=(W_j^{\mathsf T}\otimes I)|\Phi_K\rangle
```

moves the message unitary to the untouched reference. It commutes with the action of $`\mathrm{id}\otimes\mathcal T`$. The target Bell vector transforms by the same reference unitary, so the correct-decoding probability for every label is exactly

```math
P_{\mathrm{succ}}(j)=F_e(\mathcal T).
```

This equality holds for arbitrary $`\mathcal T`$ and does not assume Weyl covariance. The additional $`\log_2K`$ ebits are permitted by the model's unrestricted preshared-entanglement allowance. Applying a classical converse to these $`K^2`$ labels gives the quantum fidelity converse with no square-root loss in the error parameter.

## Arbitrary-encoder converse by CP domination

Let $`\mathcal R_{n-k}`$ be the completely depolarizing replacer,

```math
\mathcal R_{n-k}(X)
=\mathrm{Tr}(X)\frac{I_B}{d^{n-k}}.
```

The alignment-spectrum bound is

```math
\|J_{n,k}\|_\infty
\leq\frac{C_d^k}{d^k c_{n,k}}.
```

The normalized Choi matrix of $`\mathcal R_{n-k}`$ is $`I_{RB}/(D_AD_B)`$. Thus the Choi criterion for complete positivity gives

```math
\mathcal N_{n,k}
\leq_{\mathrm{CP}}
\frac{d^{2(n-k)}C_d^k}{c_{n,k}}\,
\mathcal R_{n-k}.
```

The output-dimension version is also valid:

```math
\mathcal N_{n,k}
\leq_{\mathrm{CP}}d^{2(n-k)}\mathcal R_{n-k}.
```

Indeed, for every positive $`X_{RB}`$,
$`X_{RB}\leq D_B\mathrm{Tr}_B(X_{RB})\otimes I_B`$.
One proof first pinches in a basis of $`B`$, paying $`D_B`$, and then bounds each diagonal block by their sum. Applying this inequality to $`J_{n,k}`$, whose $`R`$ marginal is $`I_R/D_A`$, proves the stated output-dimension coefficient. Combining the two inequalities yields

```math
\mathcal N_{n,k}
\leq_{\mathrm{CP}}\Lambda_{n,k}\mathcal R_{n-k}.
```

Now allow an arbitrary shared state, arbitrary message-dependent local encoders, and an arbitrary collective receiver. CP order persists when tensoring with the receiver's retained share and composing with encoding and decoding maps. Under the replacer channel, the receiver gets a fixed maximally mixed output and its original preshared marginal. A trace-preserving local encoder cannot signal to that marginal. The replacer output is therefore independent of the message.

For $`M`$ uniformly distributed labels and any complete decoding POVM, the replacer's average success is exactly $`1/M`$. Positivity of each success effect then gives

```math
P_{\mathrm{succ}}\leq\Lambda_{n,k}/M.
```

Clipping by one proves the fixed-count classical converse. This argument makes no assumption about optimal input states, Pauli covariance, product encoders, or the amount of initial entanglement.

In the independent-deletion model, the branch probability $`q_k`$ is independent of the message. The decoder can use the observed length, so applying the fixed-count bound branch by branch gives

```math
P_{\mathrm{succ}}
\leq\sum_{k=0}^n q_k\min\{1,\Lambda_{n,k}/M\}.
```

The dense-coding conversion proves the quantum version stated above.

## Capacity sandwich

Let $`h_2(x)=-x\log_2x-(1-x)\log_2(1-x)`$, with its continuous endpoint values. Define

```math
L_d(p)=\max\left\{0,(1-p)\log_2d-\frac12h_2(p)\right\}
```

and

```math
U_d(p)=(1-p)\log_2d
-\frac12\max\{0,h_2(p)-p\log_2C_d\}.
```

For every fixed $`d\geq2`$ and $`p\in[0,1]`$,

```math
\boxed{L_d(p)\leq Q_E^{\mathrm{del}}(p;d)\leq U_d(p).}
```

The expression for $`U_d`$ is the minimum of the erasure benchmark $`(1-p)\log_2d`$ and the alignment bound $`(1-p)\log_2d-\tfrac12h_2(p)+\tfrac p2\log_2C_d`$.

The exact endpoints are $`Q_E^{\mathrm{del}}(0;d)=\log_2d`$ and $`Q_E^{\mathrm{del}}(1;d)=0`$. The clipped lower bound can become zero at larger deletion probabilities; this does not assert that the capacity vanishes there. The upper and lower bounds generally do not coincide.

### Achievability and the order of limits

Fix $`0\lt p\lt 1`$, and define the classical-rate function

```math
f_d(x)=2(1-x)\log_2d-h_2(x).
```

Suppose a desired quantum rate $`R`$ satisfies $`0\leq2R\lt f_d(p)`$. Choose a fixed $`\eta>0`$ and $`\delta>0`$ such that

```math
\inf_{|x-p|\leq\eta}f_d(x)>2R+\delta,
```

where the interval is intersected with $`[0,1]`$. Use

```math
T_{n,\eta}
=\{k:|k/n-p|\leq\eta\},
\qquad
K_n=\lfloor2^{nR}\rfloor.
```

The type bound $`\binom nk\leq2^{nh_2(k/n)}`$ implies

```math
a_{n,k}\leq2^{-nf_d(k/n)}.
```

Hoeffding's binomial bound and the finite-block construction therefore give

```math
\epsilon_\diamond(\mathcal T_n)
\leq2e^{-2n\eta^2}+4\,2^{-n\delta}.
```

Both terms tend to zero. The typical window is chosen for a fixed rate gap before taking $`n\to\infty`$. After that limit, rates can approach $`f_d(p)/2`$ by shrinking the gap and choosing a correspondingly smaller fixed window. This proves the positive part of the lower bound; rate zero is always available.

### Strong converse above the explicit upper bound

Set

```math
g_d(x)=\min\left\{
2(1-x)\log_2d,\,
f_d(x)+x\log_2C_d
\right\}.
```

The reverse type bound

```math
\binom nk\geq\frac{2^{nh_2(k/n)}}{n+1}
```

implies

```math
\Lambda_{n,k}\leq(n+1)2^{ng_d(k/n)}.
```

Consider any sequence with $`\liminf_n n^{-1}\log_2K_n>g_d(p)/2`$. Choose a rate $`R`$ strictly between these quantities. Continuity permits fixed $`\eta,\delta>0`$ such that

```math
\sup_{|x-p|\leq\eta}g_d(x)\lt 2R-\delta.
```

For all sufficiently large $`n`$, the branchwise converse yields

```math
F_e(\mathcal T_n)
\leq2e^{-2n\eta^2}+(n+1)2^{-n\delta}
\longrightarrow0.
```

Hence $`\epsilon_\diamond(\mathcal T_n)\to1`$. Endpoint cases $`p=0,1`$ follow directly from their fixed-count channels.

This is a strong converse above the explicit upper bound $`g_d(p)/2`$. It does not establish a strong converse at the unknown exact capacity when the two bounds leave a gap.

## Leading synchronization penalty

For fixed $`d`$ and sufficiently small $`p`$, the positive lower expression applies and the interval between the two nontrivial bounds has width at most $`\tfrac p2\log_2C_d`$. Consequently,

```math
Q_E^{\mathrm{del}}(p;d)
=(1-p)\log_2d-\frac12h_2(p)+O(p)
=\log_2d-\frac p2\log_2\frac1p+O_d(p).
```

In particular, for qubits,

```math
Q_E^{\mathrm{del}}(p;2)
=1-\frac12h_2(p)+O(p).
```

Relative to position-labelled erasure, the additional loss is therefore

```math
Q_E^{\mathrm{erase}}(p;d)-Q_E^{\mathrm{del}}(p;d)
=\frac12p\log_2\frac1p+O_d(p).
```

The deletion pattern has entropy $`nh_2(p)`$. Conditioning on the final length removes only $`H(K_{\mathrm{del}})\leq\log_2(n+1)`$ bits, where $`K_{\mathrm{del}}`$ is the random deletion count. The coding and converse arguments show that the leading synchronization cost in entanglement-assisted quantum communication is half the pattern entropy per input carrier. The proof controls coherent overlaps between patterns; it does not give the receiver classical pattern labels. The coefficient of the linear-in-$`p`$ capacity term remains unresolved.

