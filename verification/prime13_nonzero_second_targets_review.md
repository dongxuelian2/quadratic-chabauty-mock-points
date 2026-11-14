# Independent review: prime-13 equality with nonzero second targets

## Outcome

The final proof in [prime13_nonzero_second_targets.md](../proofs/prime13_nonzero_second_targets.md) and the [on-disk standard-library checker](../scripts/check_prime13_nonzero_second_targets.py) pass independent review. The result proves full four-point equalities with genuinely nonzero actual second-height targets. It retains the separate zero-residual-target hypothesis; it does not resolve the remaining global residual comparison when odd split primes divide a−3.

The final reviewed proof SHA256 is21fda4ac8d2daf65676bdc538fda15b4aa8347527327097cdf78532faf408741. The checker SHA256 is8e03b1d8c5ab3dc2885716206a21f57f1f6164e25a5dd28aa747a131a9efa790. The checker was run after inclusion of all three examples and passed.

## Exact Weierstrass-disk image

In the class a≡1426 modulo2197, alpha≡8. The first endpoint coefficient is4 modulo13 and isolates all four endpoint centers. At either Weierstrass point the second quadratic coefficient beta=2r(2+alpha)/A² reduces to10 or3, both nonzero squares modulo13.

The earlier whole-series coefficient estimate becomes a coefficientwise Tate-algebra estimate after y=13z and division by169 beta z²: S−1 lies in169Z₁₃⟨z⟩, with coefficients tending to zero. This is stronger than merely having integral values on Z₁₃. The principal square root V lies in1+169Z₁₃⟨z⟩. Therefore T(z)=zV(z) differs from the identity by a13^(-2)-Lipschitz function in the13-adic norm. The contraction equation z=w−(T(z)−z) proves a unique inverse for every w∈Z₁₃. Since beta is a square unit, the exact second-height image on each entire W disk is169(Z₁₃)². Zero has only the center as preimage, and each nonzero target in that set has exactly two preimages on each disk.

Thus the stated filter on the complete global target proves the six-center upper bound. The warning about cancellations is necessary and correctly retained: testing individual local target valuations is insufficient in general. A nonzero intersection with the square image does not prove simultaneous scalar membership, because the first scalar condition remains to be imposed.

## Exact finite target computation

The first-digit test follows from log₁₃(q)≡13F(q) modulo169 and correctly tests all coefficient tuples, including cancellations between distinct primes.

The stronger rational-arithmetic test is also exact. After clearing denominators by D and forming R=∏q^(Dc_q), one has12Dt=log₁₃(R¹²). For a nonzero coefficient vector, unique prime factorization gives R≠1. Since R is positive and a13-adic unit, R¹²−1 is nonzero and has finite positive valuation e. Writing d=v₁₃(D), the logarithm expansion gives v₁₃(t)=e−d and precisely the displayed leading-unit formula. Higher logarithm terms have strictly larger valuation. Thus parity, the lower bound of two, and the residue-field square test decide membership in169(Z₁₃)² using finite rational arithmetic, even with cancellation or denominators.

Distinct rational coefficient vectors on distinct primes yield distinct logarithmic values. Therefore the test also computes the number N of distinct nonzero admissible targets. The candidate bound6+4N is correct; after exclusion of the W centers using the residual theorem, the full-set upper bound4+4N follows. Neither bound is asserted to be attained.

## Rank-one extension

The new rank theorem was checked independently. From8r−1=m²s and m odd, s≡7 modulo8. The assumption (2/q)=−1 for every q|m then implies s∤m, while r∤m²s is automatic. For q|m, the second elliptic curve has c′ a unit nonsquare and v_q(b′)=2v_q(m). An odd valuation of X is impossible in every range: cubic domination for negative valuation, a nonsquare middle coefficient below2v_q(m), and odd valuation of the linear term above it. Equality is even. Thus these q do not occur in the actual second descent image.

The remaining squareclass support is −1,2,r,s. The existing bounded2-adic argument depends only on v₂(c′)=6 and v₂(b′)=7, so it still leaves only1 and−s among odd representatives. The two-torsion translate and the explicit points at X=A,A+4 give exactly four second-image classes. The first image remains exactly{1,2r}. Hence the rank identity gives rank one, with actual-image upper and lower bounds, not an assumed local-global solubility principle.

## Arithmetic family and examples

In the r≡3 modulo8 subfamily, residual support is nonsplit. The exact second target is the displayed set of ternary sums ε_q v_q(m)log₁₃(q). The finite rational target filter therefore gives a concrete arithmetic family criterion. The simpler Fermat-quotient test is a sufficient specialization, not a necessary claim.

All three examples were independently checked by complete trial division, parameter arithmetic, and exact logarithmic residues:

- r=1255747, s=401839, m=5, a=−40183901. Trial bounds1120 and633. The nonzero second targets have valuation one and log₁₃(5)/13≡12.
- r=5930963, s=5271967, m=3, a=−189790813. Trial bounds2435 and2296. The nonzero second targets have valuation one and log₁₃(3)/13≡5.
- r=270643099, s=5997631, m=19, a=−8660579165. Trial bounds16451 and2449. The nonzero second targets have valuation two, with leading units5 and8, both nonsquares modulo13. This example genuinely requires the squareclass filter and is not covered by the odd-valuation test.

Each has8r−1=m²s, r≡3 modulo8, a≡1426 modulo2197, and a≡3 modulo16. Rank one and zero actual residual target follow from the proved arithmetic pattern and local theorems. Thus each full four-point equality is unconditional within the explicitly stated Selmer convention. No infinitude of prime-pattern parameters is asserted.

## Full-Selmer scope

The proof uses scalar conditions only for an upper bound. The separate uniform residual period and zero actual residual target exclude W±; rational endpoints supply the reverse inclusion. The nonzero second Tate-height target is not confused with the non-Tate residual target. All rank, local-image, congruence and compatibility assumptions are preserved. No outstanding mathematical or checker defect remains.
