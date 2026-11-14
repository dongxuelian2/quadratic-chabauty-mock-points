# Full prime-13 equality with a nonzero second scalar target

Status: the exact disk-image statement, contraction proof, target criterion and rank extension have passed independent mathematical review. This result does not identify scalar membership with full Selmer membership.

## 1. The remaining Weierstrass lift

Retain the reciprocal family and compatible scalar normalizations from [the critical-lift continuation](prime13_critical_lift.md):

    C_a: y²=x⁶+a x⁴+a x²+1,
    E_a: Y²=X³+(a−3)X²−(a−3)X,
    A=a−3, alpha=λ(P)/L(P)², P=(1,1).

Suppose a is an odd integer with

    a≡1426 modulo2197.                            (1)

The established exact constants give alpha≡8 modulo13. The first scalar rho has unit endpoint quadratic coefficient kappa≡alpha−4≡4, so it isolates the four endpoint centers in their entire residue disks. Only the two Weierstrass disks require another scalar condition.

For W=(r,0), r²=−1, use y∈13Z₁₃ as parameter. The second scalar rho* is even, has constant zero, and has quadratic coefficient

    beta=2r(2+alpha)/A².

Since A≡6 and alpha≡8 modulo13, beta≡2r is10 or3 modulo13. Both residues are nonzero squares. The previously proved whole-series estimate is

    v₁₃([y^n]rho*)≥−2floor(log₁₃n),
    n−2−2floor(log₁₃n)≥2 for even n≥4.

In particular beta is a square unit of Z₁₃ and every noncentral point in this disk has

    v₁₃(rho*)=2v₁₃(y)∈{2,4,6,…}.                (2)

## 2. Exact image of each Weierstrass disk

There is a sharper statement than (2): on either entire Weierstrass residue disk,

    rho*(disk)={13²z²:z∈Z₁₃}.                    (3)

To prove it, put y=13z. The coefficient bounds, including their growth to infinity, give the restricted series identity

    rho*(13z)=13² beta z² S(z),
    S∈1+13²Z₁₃⟨z⟩.

The binomial square root V=S^(1/2) belongs to1+13²Z₁₃⟨z⟩. The map T(z)=zV(z) is a bijection of Z₁₃. Indeed T(z)−z has integral restricted-series coefficients divisible by13², so its difference at two arguments has absolute value at most13^(-2) times their distance. For every w∈Z₁₃, solving T(z)=w is therefore a contraction iteration z↦w−(T(z)−z) on the complete space Z₁₃, with a unique solution. Since beta is a square unit, multiplication by its square root preserves Z₁₃. This proves (3).

The sole preimage of zero in this disk is its center. Equation (3) describes the second scalar alone; it makes no assertion that every such point also satisfies the first scalar condition.

## 3. A finite nonzero-target criterion

Let Omega* be the actual global second scalar target at13. It always contains zero. Under (1), the two necessary conditions

    rho(z)=0,  rho*(z)∈Omega*

have exactly the six centers if

    Omega* ∩ {13²z²:z∈Z₁₃}={0}.                 (4)

Indeed the first condition isolates the endpoints. On either W disk, (3) and (4) force rho*=0, whose only solution is the center. Conversely all six centers satisfy both scalar conditions.

Several sufficient conditions for (4) are convenient:

- no nonzero element of Omega* has positive even valuation;
- in particular every nonzero element has valuation one;
- more restrictively, Omega*∩13²Z₁₃={0}.

Positive even-valuation targets with nonsquare unit part are harmless too, by (3). The condition must be checked on the complete global Minkowski sum, not separately on each local image: cancellation between local contributions can raise valuation.

Here is an exact first-digit test. Suppose the finite local coefficient sets C_q are contained in Z_(13), and the actual target is

    Omega*={sum_q c_q log₁₃(q):c_q∈C_q},

with q≠13. Define

    F(q)=((q¹²−1)/13)/12 modulo13.

If every coefficient tuple other than the all-zero tuple satisfies

    sum_q c_q F(q)≠0 modulo13,                    (5)

then every nonzero target has valuation exactly one, so (4) holds. This is a finite arithmetic test of the global target, including all potential cancellations. To see it, use log₁₃(q)≡13F(q) modulo13². The condition itself shows that every nonzero tuple gives a nonzero value.

There is also an exact terminating rational-arithmetic test for (4), without any first-digit assumption. For a target t=sum c_q log₁₃(q), choose a positive integer D clearing all coefficient denominators, and form

    R=product_q q^(D c_q)∈Q_(>0).

The all-zero tuple gives t=0. Otherwise unique prime factorization gives R≠1; as R is positive, R¹²−1≠0. Put

    e=v₁₃(R¹²−1), d=v₁₃(D), D₀=D/13^d.

Every q is a13-adic unit, so e≥1. The convergent logarithm identity

    t=log₁₃(1+(R¹²−1))/(12D)

shows exactly that

    v₁₃(t)=e−d,
    13^(d−e)t ≡ ((R¹²−1)/13^e)/(12D₀) modulo13. (5a)

Indeed all higher terms of log(1+z) have strictly higher valuation than z when v₁₃(z)≥1. Thus t lies in the forbidden nonzero set13²(Z₁₃)² precisely when e−d is positive even and the nonzero unit in (5a) is a square modulo13. Rational numerator and denominator arithmetic computes both tests in finitely many steps. The nonzero tuple cannot conceal an exact zero logarithmic combination. This test includes cancellations between different primes and permits nonzero targets of positive even valuation with nonsquare unit part.

## 4. Full depth-two consequence

Assume in addition to (1) that

- a≡3 modulo8;
- rank E_a(Q)=1;
- every odd prime dividing A is3 modulo4;
- condition (4) holds for the actual second target.

Then, in the established Mordell–Weil-abelian-image and actual-local-image convention,

    C_a(Q₁₃)₂=C_a(Q)={(0,1),(0,−1),∞₊,∞₋}.       (6)

The exact first actual target is zero. The two scalar containments and Section3 give the six-center upper bound. The odd-prime residual theorem and [the actual dyadic theorem](dyadic_actual_images.md) make the actual residual target zero. The [uniform13-adic residual period](universal_thirteen_adic_residual.md) is nonzero throughout a≡9 modulo13 and therefore excludes W± by the exact residual comparison. The parameters here are geometrically non-CM by the existing j-denominator argument. Rational endpoints supply the reverse inclusion.

Thus (6) can hold even when the actual second scalar target is nonzero. No scalar-sufficiency implication is used.

There is also an effective bound when (4) fails. Let N be the number of distinct nonzero targets in Omega*∩13²(Z₁₃)². Each such target has exactly two preimages in each W disk, by the bijection T and the two square roots of a nonzero square. Zero has just the center as preimage. The joint scalar conditions therefore leave at most6+4N candidates. Retaining all the hypotheses of this section except (4), the residual period removes the two W centers and gives

    #C_a(Q₁₃)₂≤4+4N.                              (6a)

This is an upper bound, not an assertion that every scalar candidate belongs to the full set. The exact rational test (5a) computes N finitely. Different rational coefficient vectors on distinct primes give different logarithmic values: their difference could vanish only if the corresponding positive rational product were1, which unique prime factorization excludes.

## 5. A rank-one extension with a nonsplit square factor

The following elementary extension of [the checkable rank patterns](checkable_rank_patterns.md) supplies examples with nonzero second target.

**Rank theorem.** Let r and s be odd primes, r≡3 or5 modulo8, and suppose

    8r−1=m²s,

where m is a positive odd integer and every prime q dividing m satisfies (2/q)=−1. Set A=−32r. Then the two-isogeny descent images have sizes2 and4, and E_A(Q) has rank one.

The first image is unchanged from the linear prime-pattern proof:

    delta(E_A(Q))={1,2r}.

Its squareclass candidates are ±1,±2,±r,±2r. The negative classes are impossible over R. The d=2 quartic is impossible by the same bounded2-adic calculation for r≡3 or5 modulo8. The rational two-torsion class2r and group closure exclude r and give the displayed equality.

The isogenous curve has

    E'_A:Y²=X³+64r X²+128r m²s X.

First note s≡7 modulo8, because m²≡1 modulo8. Hence (2/s)=1, so s cannot divide m under the hypothesis. Also r cannot divide m²s=8r−1.

Fix q|m and let e=v_q(m). The coefficient c'=64r is a q-adic unit, b'=128r m²s has valuation2e, and

    (c'/q)=(r/q)=(2/q)=−1,

because8r≡1 moduloq. Suppose a nonzero rational point has odd j=v_q(X). If j<0, X³ has uniquely least, odd valuation3j. If 0<j<2e, the term c'X² has uniquely least valuation2j, and its unit squareclass is the nonsquare c'. If j>2e, b'X has uniquely least, odd valuation2e+j. Equality j=2e is impossible for odd j. Every case is impossible. Thus q never occurs in a descent squareclass on E'_A.

After removing all primes dividing m, the second image is supported on −1,2,r,s. Its two-torsion class is2rs. Multiplication by that class reduces to an odd representative among ±1,±r,±s,±rs. The old bounded2-adic quartic argument uses only v₂(c')=6 and v₂(b')=7 and forces any soluble odd representative to be1 modulo8. Since r≡3 or5 and s≡7 modulo8, only1 and−s survive. Restoring the torsion translates gives the upper bound

    delta'(E'_A(Q))⊂{1,−s,2rs,−2r}.

The rational points (A,2A) and (A+4,2(A+4)) have squareclasses−2r and−s, respectively, and generate all four classes. The two-isogeny rank identity gives

    2^rank=2·4/4=2.

This proof uses actual descent images, with local obstructions for the upper bounds and explicit points for the lower bounds. No analytic-rank oracle or unproved solubility assertion occurs.

## 6. A rank-certified family with a nonzero target

In the rank theorem, now assume r≡3 modulo8 and a=3−32r satisfies (1). Write m=product_q q^e_q. The odd-prime support of A is just r≡3 modulo4. Since

    a+1=−4m²s,

the exact local-target theorem gives

    Omega*={sum_(q|m) epsilon_q e_q log₁₃(q):
             epsilon_q∈{−1,0,1}}.                (7)

The prime s has multiplicity one and contributes zero. Each q|m is nonsplit for2 and has even multiplicity2e_q, so contributes exactly0 and±e_q log₁₃(q). No q here equals13, because a≡9 modulo13.

Apply the exact rational test (5a) to all3^(number of prime factors of m) tuples in (7); here D=1. If no nonzero tuple has positive even valuation and square leading unit, (6) follows. This gives a rank-certified full-equality family with a finite elementary arithmetic condition.

The simpler test that every nonzero epsilon vector has sum epsilon_q e_q F(q) nonzero modulo13 also suffices. For m=q^e, it is enough that13 does not divide e and q¹² is not1 modulo169. If m>1, (7) is genuinely nonzero: its single-prime contribution e_q log₁₃(q) is nonzero.

## 7. Explicit nonzero-target examples

Complete trial division verifies

    r=1255747, s=401839, m=5,
    8r−1=25s,
    a=−40183901≡1426 modulo2197.

Here r≡3 modulo8, s≡7 modulo8, and (2/5)=−1. The rank theorem applies. The second target is exactly

    Omega*={0,±log₁₃(5)},
    log₁₃(5)/13≡12 modulo13.

Its nonzero values have valuation one. All residual targets are zero, so (6) holds unconditionally although the second scalar target is nonzero.

A second independently found example is

    r=5930963, s=5271967, m=3,
    8r−1=9s,
    a=−189790813≡1426 modulo2197.

Here Omega*={0,±log₁₃(3)} and log₁₃(3)/13≡5 modulo13, so the same conclusion holds.

A third example genuinely uses the squareclass test rather than odd valuation:

    r=270643099, s=5997631, m=19,
    8r−1=19²s,
    a=−8660579165≡1426 modulo2197.

Complete trial division proves r and s prime. All rank and residual conditions still hold, and Omega*={0,±log₁₃(19)}. Exact rational arithmetic gives

    v₁₃(log₁₃(19))=2,
    log₁₃(19)/169≡5 modulo13.

The residues5 and−5=8 are both nonsquares modulo13. Hence neither nonzero target belongs to13²(Z₁₃)², and (6) follows despite nonzero targets of positive even valuation. This example is not covered by the simpler valuation-one filter.

The companion standard-library checker verifies complete primality tests, congruences, rank-pattern identities and exact target signatures for all three examples. No infinitude of the arithmetic family is asserted.
