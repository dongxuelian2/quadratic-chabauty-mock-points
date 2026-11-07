# The actual dyadic image vanishes throughout a≡3 modulo8

Status: independently reviewed. The explicit disk geometry, the primary prime-to-residue-characteristic path lemma, the central-fiber argument and transported involution have all been checked. This theorem concerns actual point images, not the whole local cohomology group.

## 1. Theorem and scope

Let a∈Z₂ satisfy a≡3 modulo8 and a≠3, let p be odd, and put

    C_a: y²=x⁶+a x⁴+a x²+1,
    E_a: Y²=X³+(a−3)X²−(a−3)X.

Base the curve at b₊=(0,1). Retain the reciprocal-family quotient

    1→R→U_R→H→1,
    H=V_pJ(C_a)≅V_pE_a⊕V_pE_a,
    R=Sym²V_pE_a,

obtained from U₂ by quotienting its two-dimensional Tate central summand T. Then

    j_(R,2)(C_a(Q₂))={0}.                           (1)

Together with the established vanishing of both independent Tate coordinates, this gives the exact same-point joint image

    Xi₂={(0,0)}.                                   (2)

No rationality of a, global rank assumption, non-CM assumption, or lower bound v₂(a−3)≥4 is needed. The singular value a=3 must be excluded; a=−1 is already excluded by the congruence.

Equation (1) does not assert H¹(Q₂,R)=0. Actual point images can vanish even when that ambient vector space is nonzero.

## 2. Four explicit analytic disks exhaust all rational points

Write f_a(x)=x⁶+a x⁴+a x²+1. If x is a 2-adic unit, then x² is1 or9 modulo16 and

    f_a(x)≡(a+1)(x²+1)≡8 modulo16,

which is not a square. If v₂(x)=1, then f_a(x)≡5 modulo8, again not a square. Thus every finite rational point with integral x has x∈4Z₂.

Set x=4t. Then

    f_a(4t)=1+16a t²+256a t⁴+4096t⁶.

The binomial square root s(t) congruent to1 belongs to 1+8Z₂⟨t⟩ and is overconvergent. Indeed its n-th nonconstant binomial term has coefficient valuation at least

    4n−n−v₂(n!)≥2n+1,

and degree at most6n. These bounds tend to infinity even on a slightly larger disk, for example any radius 2^ε with 0<ε<1/3. The two maps

    t↦(4t,s(t)),   t↦(4t,−s(t)),  |t|≤1,

are closed analytic disks defined over Q₂, centered at b₊ and b₋=(0,−1). They are admissible affinoid domains of the curve: the inverse image of |x|≤1/4 splits into these two components by the factorization y²−f_a(4t)=(y−s)(y+s), with 2s invertible in the affinoid algebra over Q₂.

Reciprocity (x,y)↦(1/x,y/x³) gives two analogous admissible closed disks centered at ∞₊ and ∞₋. For a finite point with nonintegral x, its reciprocal coordinate is integral and the preceding exclusions apply. Thus these four disks exhaust C_a(Q₂). The assertion is about rational points; it does not claim that four disks cover every geometric point of the analytification.

## 3. Exact constancy on each whole disk

The precise input is L. A. Betts, *Local constancy of pro-unipotent Kummer maps*, arXiv:2203.03701v2, Section2, Lemma2.2 and the immediately following proof of Theorem1.1:

https://arxiv.org/html/2203.03701v2#S2

That lemma supplies a Galois-invariant prime-to-residue-characteristic path between any two rational points of a closed analytic polydisc. The following proof restricts algebraic covers to the analytic domain and transfers this path to the algebraic curve; composition then identifies the Kummer torsors. Consequently every Q_p-unipotent Kummer map, p≠2, is constant on each entire disk in Section2. An unspecified neighborhood-local-constancy statement alone would not suffice here.

It remains to show that the residual classes of all four disk centers vanish.

## 4. The zero-abelian central fiber is unambiguous

The rationalized p-adic abelian Kummer map of J(C_a)(Q₂) is zero. The local compact group has an open pro-2 subgroup, on which multiplication by p is invertible; its p-adic completion is finite and vanishes after rationalization. The same observation shows that local p-power torsion is finite, hence

    H⁰(Q₂,H)=0.

For the central extension in Section1, the nonabelian cohomology sequence therefore identifies the fiber over the zero abelian class injectively with H¹(Q₂,R). Every point class lies in this fiber, so each has a unique central cohomology class. This statement also follows directly by gauging away its abelian cocycle; two resulting central representatives differ only by a coboundary because H⁰(H)=0.

## 5. The finite centers and the transported infinity action

The involution g₁(x,y)=(−x,y) fixes both b₊ and b₋. On the two elliptic abelian factors it acts by (+1,−1). Thus it acts by −1 on the surviving mixed symmetric-square center R. Equivariance and uniqueness of the central class imply

    j_R(b₋)=−j_R(b₋),

so j_R(b₋)=0. The basepoint b₊ has class zero by definition.

Because the path torsor from b₊ to b₋ is trivial as a Galois torsor, choose a G_Q₂-invariant U_R path u between them. Consider g₂(x,y)=(−x,−y). This sends b₊ to b₋ and fixes each infinity point: in the infinity coordinates t=1/x and z=y/x³ it acts by (t,z)↦(−t,z).

Transport g₂ back to the basepoint b₊ along u. This defines a Galois-equivariant automorphism φ of U_R. Its action on R is still −1: the hyperelliptic involution acts by −1 in degree one and hence by +1 in degree two, while inner basepoint transport acts trivially on the center.

For an infinity point z, applying g₂ to paths b₊→z gives paths b₋→z. Composing with the fixed path u identifies the transformed torsor with the original torsor b₊→z. This identification is Galois-equivariant and semilinear for φ. Hence its cohomology class is fixed by φ. In the unique central fiber of Section4, φ acts by −1, so

    j_R(z)=−j_R(z)=0.

No order-two assertion about the transported automorphism is needed. Its action on the central class and the fixed-path equivariance suffice.

All four center classes are now zero. Constancy on the four disks proves (1).

## 6. The joint actual image and global consequences

The two previously established independent Tate-height coordinates are identically zero at2 when a≡3 modulo8. On H¹(Q₂,Q_p(1)), evaluation by the cyclotomic character is a nonzero multiple log_p(2) of the valuation coordinate, so the two independent zero height values give zero Tate class. The ordinary fiber-product gluing U₂=U_T×_H U_R, with H⁰(H)=0, then gives the joint same-point statement (2).

This removes the dyadic valuation restriction from the earlier full-equality applications. In the prime-five theorem one may replace a≡3 modulo16 by a≡3 modulo8, retaining rank one and the requirement that every odd prime dividing a−3 is3 modulo4. The a=−5 CM member is handled separately by the already proved norm-one-torus obstruction. The same weakening applies to the prime-thirteen theorem, retaining its scalar residue conditions a≡9 modulo13 and a≠74 modulo169 and its other global hypotheses.

Two new unconditional examples fall in the previously omitted dyadic valuation-three case. The established quadratic rank pattern a=3−8n² applies to n=11 and n=3, because 11,241=2·11²−1 and 3,17=2·3²−1 are prime and n≡3 modulo8. It gives

    a=−965 at p=5,   A=−8·11²,
    a=−69 at p=13,  A=−8·3².

Their only odd primes dividing A are nonsplit in Q(i), and v₂(A)=3. The second parameter is9 modulo13 and not74 modulo169. Thus the respective full restricted depth-two sets and rational-point sets consist of exactly the four rational endpoints. No infinitude of rank-one parameters is asserted.

The companion checker verifies the local congruences, binomial coefficient bounds, involution action in the infinity chart, and arithmetic examples. The Galois-path and central-fiber arguments are the mathematical proof; finite checks do not replace them.
