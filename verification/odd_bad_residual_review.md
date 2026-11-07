# Independent audit: exact odd bad-prime images

The full proof was independently reviewed before publication, with direct checks of Betts–Dogra arXiv:1909.05734v2, Theorem 6.1.1, Corollary 8.2.1 and Lemma 8.2.2. No substantive correction was needed.

Checked steps:

- The elliptic rescaling is exact and the formal node chart has zt=-pi. Each neck has normalized length n/4, so contraction of the central valency-two rational component gives a stable interval of length n/2, with the basepoint at its midpoint. The formal unit satisfies U²+(pi²t²-1)U-t⁴=0, U(0)=1.
- The two component homologies are graphs of ±iota. Their separating bivectors have equal determinant terms, killed by the surface relation, and nonzero symmetric mixed tensors. Both full Tate projections vanish.
- The cited graph formula, together with the explicit nonzero endpoint charges, proves a nonzero linear slope. The unspecified linear map in Lemma 8.2.2 alone would not suffice for nonvanishing.
- Interior rational points have v(x²+1)=2k and coefficient 4k/n. Every k with 1<=k<n/4 is attained by x²+1=q^(2k) and Hensel lifting. Zero and both endpoint values are attained.
- In the nonsplit case Galois fixes only the midpoint of the interval. The ACTUAL image is zero; no claim that all H¹(Q_q,R) vanishes is made.
- The full joint image is {(0,delta)} with delta in the exact residual image. This retains the same-point condition.
- The odd good-reduction equivalence follows from the verified reducible stable fiber at a=3 modulo q and the j-valuation obstructions at denominator primes and a=-1 modulo q.

Executed check_odd_bad_residual.py:

    PASS: rescaled elliptic equation and exact neck identity.
    PASS: separating bivector has zero Tate projection and nonzero opposite Sym² parts.
    PASS: interior valuation-to-edge coefficients for n=1,...,64.

Finite algebra checks supplement the all-prime proof and the graph-comparison theorem. The prime 2, global transport Theta_p and the local p-adic discrepancy remain uncomputed.
