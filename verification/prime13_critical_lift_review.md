# Independent review of the prime-13 critical-lift continuation

## Outcome and scope

The refined first-height argument and the simultaneous two-height argument in [prime13_critical_lift.md](../proofs/prime13_critical_lift.md) pass independent mathematical review. The conclusions are distinct. First, for odd integral a≡9 modulo13, the first scalar has exactly the six centers except possibly in the two classes a≡581 or1426 modulo2197. Second, on the entire formerly omitted class a≡74 modulo169, the simultaneous zero locus of the two scalars is exactly those six centers. Applying the second assertion to the Selmer set requires the actual second target to be zero; it is not automatic from the nonsplit support of a−3.

Under the stated Mordell–Weil-abelian-image and actual-local-image convention, rank one, a≡3 modulo8, and nonsplit odd-prime support in a−3, the refined first-height statement and uniform residual period give the full four-point equality outside the two fine lifts. In either fine lift, the explicit second-target valuation criterion below is sufficient. The mod8 generality uses the separate dyadic actual-image theorem, not an assertion that the ambient dyadic H¹ always vanishes.

## Exact constants and parameter refinement

The exact quintuple identities were evaluated independently in all thirteen classes a=74+169c modulo2197. They give ψ₅/13≡12, N≡9, Q≡3, t₅/13≡3 and ell/13≡11 modulo13. Thus ell has valuation one throughout the critical disk. The previously established h/13 formula gives h∈13²Z₁₃, and alpha=h/ell² is integral. Z≡5.

The formal expansions ω/dt=1+(a−3)t²+…, ζ=1/t+2t+… imply B(t)=(a−1)t²/2+O(13⁴) when v₁₃(t)=1. Consequently B(t₅)/169≡10. Independently reducing the rational quintuple expression U modulo13³ gives log₁₃(U)/169≡12+c. Equivalently, U¹²−1∈13² and log₁₃U≡(U¹²−1)/12 modulo13³; its parameter derivative U′/U is1 modulo13. Combining these values yields alpha≡12+6c modulo13. All thirteen residues were checked separately, rather than inferred from two numerical samples.

## Endpoint isolation

The exact first endpoint quadratic coefficient is κ=1−Z+alpha(1−ell), hence κ≡alpha−4. When this is a unit, the entire first scalar divided by x² is κ+13²Z₁₃ on the punctured disk. The second scalar has exact slope s=−2(1+Z+alpha ell)≡1, and its entire quotient by x is s+13²Z₁₃. Reciprocity transfers these statements to infinity, with the correct second-scalar invariance. Thus the second zero condition isolates all four endpoint centers throughout the critical class, and the first does so unless c≡3.

These assertions use the exact integrated endpoint formulas, not finite Taylor tests. Numerator series and constants are integral; at most two integrations or products of single primitives occur. The coefficient bound is −2 floor(log₁₃n). The odd second-scalar tail satisfies n−1−2 floor(log₁₃n)≥2 for n≥3. The even first-scalar tail satisfies n−2−2 floor(log₁₃n)≥2 for n≥4. Both lower bounds tend to infinity, proving the whole-disk estimates.

## Weierstrass isolation

At W=(r,0), r²=−1, f′(r)=−2rA is a unit, so x(y) is an integral even series with constant r. The first logarithm slopes are −1/A and −r/A; the second slopes are (1−r)/(2A) and −(1+r)/(2A). The two-torsion centers have zero odd logarithm and odd primitive. Independently differentiating the height, explicit logarithm, and quadratic terms gives

    [y²]rho=−(a+1+2alpha)/A²,
    [y²]rho*=2r(2+alpha)/A².

If the second coefficient vanishes modulo13, alpha≡−2, and the first numerator is A, a unit. Therefore the two coefficients cannot both vanish. The first coefficient vanishes precisely at alpha≡8, namely c≡8.

Both scalar series are even with zero constant, and the same denominator bound shows that after division by y² the whole higher tail lies in13²Z₁₃. Thus simultaneous zeros on either W disk consist only of its center. This proves the joint six-center theorem and, together with the endpoint calculation, the two exceptional fine lifts for the first-only theorem. The already established reduction has exactly six points, so no disk is omitted.

## Actual local targets and full containment

For a≡3 modulo8, the first actual target is zero. The second is zero exactly when every odd q|a+1 has m=v_q(a+1)=1, or has odd m and (2/q)=−1. Squarefree odd part of a+1 is a simple sufficient condition. The exact local-image formulas in [reciprocal_local_targets.md](../proofs/reciprocal_local_targets.md) justify this criterion: split primes contribute the attained values ±2k(m−k)/m·log₁₃q, nonsplit even multiplicity contributes ±m/2·log₁₃q, and nonsplit odd multiplicity contributes only zero. Every local image contains zero. Since q≠13 and log₁₃q≠0, the global target is zero exactly under the displayed local condition. Neither 'multiplicities at most three' nor nonsplit support in a−3 is sufficient.

Concrete checks confirm this distinction. The critical parameter a=4299 has A=8·3·179 and a≡3 modulo8, but a+1=4·5²·43, giving nonzero second image {0,±log₁₃5}. Indeed u=5 has v²=32203600, a square in Q₅ since it is25 times a unit congruent4 modulo5, and realizes −log₁₃5. No rank claim is made for this example. The separate rank-one parameter a=−1373 has A=−32·43 and 8·43−1=7³, so the published prime-power descent theorem gives rank one, while its second image at7 is {0,±(4/3)log₁₃7}. This latter example is outside the critical13-adic class.

The full-containment argument retains the first-model endpoint bridge and applies Theorem18 directly to the second model at (u,v)=(-1,-4), which is away from its coordinate endpoints. Compatible isogeny heights give alpha′=2alpha. With zero actual residual target, the already certified [uniform13-adic holomorphic period](../proofs/universal_thirteen_adic_residual.md) excludes W±. Rational endpoints give the reverse inclusion. Scalar vanishing alone is never treated as sufficient for full membership.

## Unconditional fine-lift examples

Both new examples pass independent complete trial division:

    r=326923, q=2615383=8r−1, a=−10461533≡581 modulo2197;
    trial bounds571 and1617.

    r=95731, q=765847=8r−1, a=−3063389≡1426 modulo2197;
    trial bounds309 and875.

In each case r≡3 modulo8, a≡3 modulo16, A=−32r and a+1=−4q. The existing [elementary descent theorem](../proofs/checkable_rank_patterns.md) proves rank one. Both scalar targets and all actual residual targets are zero. The new joint argument therefore proves the four-point full-depth-two equality in both genuinely remaining fine lifts. The proof does not claim that these particular examples possess extra first-scalar zeros, and it makes no infinitude assertion.

## Review status

The exact constants, all thirteen alpha residues, two-height quadratic coefficients, entire-series estimates, explicit local-target criterion, Selmer-containment scope, and both arithmetic examples have passed independent review. The first-only refinement does not use a second-target hypothesis outside the two explicitly retained fine lifts.

The complete final prose was read and approved. The [standalone standard-library checker](../scripts/check_prime13_critical_lift.py) passes after the one-line correction adding the missing return value to floorlog13. That implementation correction does not alter any mathematical formula or claim. Finite checks supplement, rather than replace, the whole-series proofs.
