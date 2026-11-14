# Independent audit: infinite zero-second-target family

The source audit checked Zywina arXiv:2505.16960v1, Theorem 1.5, Lemma 3.1 including the absorbed S1' case, the S2/S3 local conditions, equation (3.13), Lemma 4.1, and the distinct-j construction in Section 4. Every source case gives positive odd valuation of a+1 either absent or exactly one. The dyadic S0 condition gives a+5 in 16 Z_2. The rank transfer was checked against both isogenous source equations, rather than inferred from matching j-invariants.

A separate review checked that S0 may initially include an arbitrary fixed odd p, and that its allowed center m_p=1, b_p sufficiently divisible by p imposes the claimed neighborhood without altering the prime-ideal or rank arguments.

Executed standard-library check_infinite_second_target.py:

    PASS: 435 exact parameter/isogeny-model/j-identity checks.
    PASS: complete source valuation table has positive differences only 1.

The script checks algebra, not rank or infinitude. Those use the cited theorem and construction. Finitely many elliptic involutions on a fixed genus-two curve justify passing from infinitely many quotient j-values to infinitely many geometric curve classes.

Scope retained: rational parameters only; no first-target vanishing, no disappearance of the denominator height shift, no general full-depth-two equality. Even the prescribed p-adic neighborhood does not by itself verify the earlier integral-parameter analytic hypothesis.
