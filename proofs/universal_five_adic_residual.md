# A uniform five-adic residual period with one exact zero

Status: independently audited mathematical argument and arithmetic certificate. Sixteen seven-digit Frobenius computations were reproduced with two separately written implementations. The parameter-degree bounds, monic-remainder interpolation argument, polynomial system, and exact symmetry at the exceptional parameter were independently checked. No inference from pointwise numerical sampling is used.

## 1. Uniform theorem

For a∈5Z₅ let

    C_a: y²=f_a(x)=x⁶+a x⁴+a x²+1,
    W₋=(−i,0), W₊=(i,0), i²=−1,
    ν_j=x^j dx/(2y),  0≤j≤4.

Use the canonical Frobenius-invariant Coleman path and the outer-first word convention. Define

    X_a=(1/i)∫_(W₋)^(W₊) ν₀ν₁,
    b=(a+5)/5.

**Theorem.** There is U∈Z₅⟨b⟩ with U≡3 modulo 5 coefficientwise such that

    X_a=5(a+5)U(b).                                 (1)

Consequently X_a vanishes exactly at a=−5. For every other a∈5Z₅,

    v₅(X_a)=1+v₅(a+5).                              (2)

Here Z₅⟨b⟩ is the restricted power-series ring, whose coefficients tend to zero 5-adically. Congruences in this ring are coefficientwise, or equivalently in its Gauss norm. This is stronger than a congruence checked only at integer values of b.

The theorem requires no rationality or rank hypothesis. At a=−5, this theorem asserts vanishing only of the holomorphic coordinate; it does not follow that the full residual class vanishes. The earlier norm-one-torus argument already excludes W± from the full depth-two set for that CM curve, including at 5.

## 2. The fiberwise Frobenius equation

We use the regular-endpoint Frobenius construction and normalization from the [certified a=−605 period proof](five_adic_residual_certificate.md). For each a∈5Z₅, H is the unique degree-at-most-29 representative satisfying

    f_a(H)=0 in Z₅[x]/(f_a⁵),   H≡x⁵ modulo 5.

Write exactly

    f_a(H)=f_a⁵ V,  V≡1 modulo 5,
    P=H′/f_a⁴,  P≡0 modulo 5.

Both divisions are monic. The lift φ(x)=H, φ(y)=y⁵ sqrt(V) is regular at W± and fixes them. Put

    B_j=H^j f_a² P V^(−1/2),
    B_{j,n}=binom(−1/2,n)H^j f_a²P(V−1)^n.

Every B_{j,n} is a polynomial in x with coefficient valuation at least n+1 and degree at most D_n=132+144n. Horizontal reduction gives

    B_{j,n}=2f_a K′_{j,n}+f′_a K_{j,n}+m_{j,n},
    deg(m_{j,n})≤4.

Its denominator loss is at most

    L_n=floor(log₅(130+144n)).                       (3)

This bounds both K and m, as proved by integrating the high-pole principal part at infinity in the earlier certificate. Sum over n and write m_j=Σ_k M_jk x^k. All primitives yK_j vanish at W±.

The single Coleman integrals of all five ν_j between W± vanish, including the third-kind direction. Parity leaves the six double periods, in order

    (0,1), (0,3), (2,1), (2,3), (4,1), (4,3).

Let z be their vector after division by i. With M_e on indices (0,2,4) and M_o on (1,3), the exact equation is

    A z=c,   A=I₆−M_e⊗M_o.                         (4)

For an even polynomial g=Σ g_2k x^(2k), put

    T(g)=Σ g_2k(−1)^k/(2k+1).

The exact normalized correction is

    c_jk=T(K_k B_j−K_j m_k).                        (5)

No uncomputed boundary term or logarithm appears. The first coordinate of z is X_a.

## 3. Integral formal parameter coefficients

Set v=a+5, so a=−5+v and later v=5b. First work formally over Z₅[[v]]. At v=0 start from the exact a=−5 Hensel solution H₀, not from x⁵ as a putative root over the formal coefficient ring. In the finite free quotient by f_a⁵, the derivative of the equation for H at v=0 is multiplication by f′_−5(H₀). Its reduction modulo 5 is the unit x²⁵ in F₅[x]/(x³⁰+1). Thus its determinant is a 5-adic unit, and successive formal lifting in v gives H with integral v-coefficients.

Monic polynomial divisions show that V and P also have integral v-coefficients. Substituting v=5b shows that their b-degree-d coefficients have valuation at least d. They are restricted analytic functions of b. The same is true of H^j f_a² and of the inverse square-root series at infinity used in horizontal reduction.

Independently, the Gauss valuations of P and V−1 are at least one, since their reductions modulo 5 are zero for the whole b-family. Therefore

    v₅([b^d]B_{j,n})≥max(d,n+1).                   (6)

The horizontal operator has loss L_n. In its explicit principal-part formula, parameter coefficients of the infinity inverse square root gain their b-degree, and the only denominators are the integration integers bounded by D_n−2. Consequently

    v₅([b^d]K_{j,n}), v₅([b^d]m_{j,n})
        ≥max(d,n+1)−L_n.                           (7)

For a bilinear term of (5) with indices n,m and s=n+m, the polynomial integration has loss at most

    J_s=floor(log₅(260+144s)).

The convolution inequality max(d₁,n+1)+max(d₂,m+1)≥max(d₁+d₂,s+2) then gives

    v₅([b^d]c_(n,m))
        ≥max(d,s+2)−L_n−L_m−J_s.                   (8)

All these bounds are uniform in the x-coefficients. The Gauss bounds tend to infinity with n or s, so the infinite sums define M and c in Q₅⟨b⟩. This also justifies passage between their convergent sums and coefficient extraction.

## 4. Why only sixteen parameter coefficients matter

The previous all-orders estimates give matrix tails of valuation at least 17 for n≥20, and correction tails of valuation at least seven for s≥20. These are Gauss-norm estimates over the parameter ring as well: their proof uses only degrees, integrality, and (3), (7), (8).

For completeness the correction bound is s+2−L_n−L_m−J_s. With L_s=floor(log₅(130+144s)), it is at least s+2−2L_s−J_s. For s≥20, set

    P(s)=(130+144s)²(260+144s).

One has P(20)=28448714000<5¹⁵ and P(s+1)/P(s)≤(21/20)³<5, proving 2L_s+J_s≤s−6 and in fact a tail of valuation at least eight. Seven suffices throughout.

For s<20, use the conservative bounds L_n,L_m≤4 and J_s≤5. Equation (8) shows that every b-degree d≥16 coefficient of c has valuation at least d−13≥3. Equation (7) gives the same conclusion for M, with a stronger bound. Combining finite and infinite terms proves

    M mod125 and c mod125 are polynomials in b
    of degree at most fifteen.                     (9)

At this stage their low coefficients need not yet be assumed integral. Their integrality will be certified below. Assertion (9) means precisely that their high-degree coefficients lie in 125Z₅ and tend to zero, not merely that some pointwise polynomial happens to agree at sample values.

## 5. Rigorous interpolation through a monic remainder

Let

    Q(b)=∏_(j=0)^15(b−j).

Euclidean remainder modulo this monic integral polynomial is Gauss-norm nonincreasing on Z₅[b]. Indeed each remainder of b^d has integral coefficients. It therefore extends continuously to restricted power series, giving an integral remainder of degree at most fifteen and preserving evaluations at j=0,…,15.

For any entry F of M or c, its terms of degree at least sixteen lie in 125Z₅⟨b⟩ by (9). Their remainder is consequently still in 125Z₅[b]. Thus

    rem_Q(F)≡F modulo125 coefficientwise.           (10)

This monic-remainder step is essential. Direct interpolation of a pointwise O(125) error would not justify (10), since interpolation denominators can lose powers of five.

For each b=0,…,15, the exact same twenty-term, coefficient-precision-thirty Frobenius computation gives M and c modulo 5⁷. Its uniform certified bounds are D*=2868, L*=4, J*=5; finite M error at least 22, finite c error at least 13, and infinite tails at least 17 and seven respectively. The complete sixteen input certificates are saved in [universal_p5_samples.json](../verification/universal_p5_samples.json). Every M entry, c entry, and period was reproduced modulo 5⁷ with the separate independent implementation.

Lagrange interpolation at these sixteen integer nodes has denominator j!(15−j)! in its j-th basis polynomial. Its 5-valuation is at most v₅(15!)=3. Hence seven-digit input errors change each interpolated coefficient by at least 5⁴. The resulting rational interpolation therefore computes rem_Q(F) modulo 5⁴, and by (10) computes the entire F coefficientwise modulo125.

All resulting rational interpolant coefficients are 5-integral. Together with (9), (10), this proves M,c∈Z₅⟨b⟩, rather than assuming their integrality from values at integer points.

## 6. The small universal polynomial certificate

All entries in this section are polynomials modulo125. In the original indices 0,…,4 the matrix is

    M =
    [85+65b+100b², 0,             50+75b, 0,            80+50b+100b²]
    [0,             85+65b+100b², 0,      40+25b+50b², 0]
    [110+15b,       0,             5,      0,            50+100b+100b²]
    [0,             63+75b+25b²,  0,      40+60b+25b², 0]
    [119+50b+100b², 0,             100+25b²,0,            40+60b+25b²].

The normalized right side is

    c=[25,
       5+100b+25b²,
       25b²,
       43+60b+75b²,
       66+50b+75b²,
       49+115b+75b²].

Modulo5, the only nonzero entries of M are M_31=3 and M_40=4, with zero-based indices. Thus A=I₆−K modulo5, where K has its sole nonzero entry K_50=2 and K²=0. In particular A is invertible over Z₅⟨b⟩: its inverse is obtained from a constant inverse modulo5 by a convergent geometric series. No pointwise determinant criterion is substituted for invertibility over the Tate algebra.

Direct polynomial multiplication verifies A z=c modulo125 for

    z=[75b,
       70+75b+75b²,
       100+25b²,
       43+10b,
       66+100b+100b²,
       94+120b+50b²].                              (11)

The first coordinate therefore gives the coefficientwise statement

    X_(5b−5)=75b+125G(b),  G∈Z₅⟨b⟩.              (12)

The standard-library checker reconstructs the rational interpolation from all sixteen sample files, checks its integrality, verifies every displayed polynomial, reconstructs all thirty-six entries of A, and checks all six equations in (11). The companion JSON records the universal polynomials.

## 7. The exact zero at a=−5

On C_−5, put c²=−2 in the unramified quadratic extension of Q₅. The map

    F(x,y)=((x+1)/(x−1), 4y/[c(x−1)³])

is an automorphism of the smooth projective curve. The exact sextic identity is

    (x−1)⁶ f_−5((x+1)/(x−1))=−8f_−5(x).

It interchanges W₋ and W₊. On ω₀=dx/y and ω₁=x dx/y its pullback matrix is

    (c/2) [ 1  −1 ]
          [−1  −1 ],

of determinant one. All single periods between the Weierstrass endpoints are zero. Shuffle therefore makes the two-letter holomorphic period alternating, so the pullback acts on it by this determinant, namely +1. But functoriality and reversal of the two endpoints act by −1. Consequently the period equals its negative and is exactly zero in characteristic zero. Coleman functoriality can be applied after the unramified base change, and the equality descends to Q₅.

Thus X_−5=0 exactly, not merely to seven digits. In (12) it follows that G(0)=0. Shifting the restricted series gives G(b)=bH(b) with H∈Z₅⟨b⟩. Hence

    X_(5b−5)=25b(3+5H(b)),

which is (1), with U=3+5H. Its unit factor proves the exact zero classification and valuation formula (2).

## 8. Full depth-two consequences with exact hypotheses

The previously independently proved [six-disk theorem](five_adic_disk_isolation.md) states that for every odd integer a divisible by5 the first scalar height has exactly the four rational endpoint zeros and W±. It is a whole-disk statement, not a finite numerical zero search.

Suppose now that

- a is an integer divisible by5 and a≡3 modulo16;
- E_a(Q) has rank one;
- every odd prime dividing a−3 is congruent to3 modulo4.

Then a≠−5. The dyadic theorem and the exact odd bad-prime theorem give zero actual residual target. Also E_a is automatically geometrically non-CM: j(E_a)=256a³/(a+1), gcd(a,a+1)=1, and v₂(a+1)=2. An odd divisor of a+1 gives negative j-valuation. If none exists, a+1=±4, so a=3 or−5; both are excluded by the stated congruences.

The established actual-target scalar containment puts the full restricted depth-two set inside those six centers. The joint residual criterion and (1) exclude W±. The rational endpoints give the reverse inclusion. Thus, under the same Mordell–Weil-abelian-image and actual-local-image convention,

    C_a(Q₅)₂=C_a(Q)
      ={(0,1),(0,−1),∞₊,∞₋}.                      (13)

Unlike the earlier 5³⁰-neighborhood corollary, no proximity to −605 beyond divisibility by5 is required.

An elementary unconditional certificate applies to each parameter a=3−32r for which r and 8r−1 are prime and r≡19 modulo40. The previous two-isogeny rank theorem gives rank one; the residue conditions give all other hypotheses above. Examples are

    r=19,619,859,1699,2179,3019,4219,5059,
    a=−605,−19805,−27485,−54365,−69725,−96605,−135005,−161885.

The checker proves primality of the displayed integers by complete trial division. No infinitude of these simultaneous-prime patterns or rank-one parameters is asserted. Other parameters with nonzero residual targets are not classified by (1) alone.

There is also a simple positive example, a=35. Its elliptic quotient and two-isogenous curve are

    E: Y²=X³+32X²−32X,
    E′: Y²=X³−64X²+1152X.

For E, the two-isogeny descent image is supported on {±1,±2}; the point (−4,24) gives class −1 and (0,0) gives class −2, so all four occur. For E′, negative X makes the right side negative. The image is therefore contained in {1,2,3,6}, and its two-torsion point supplies class2. Class3 would require a primitive solution of

    N²=3U⁴−64U²V²+384V⁴.

Modulo3, both U,V being units is impossible. If either is divisible by3 and the other is a unit, the right side has valuation exactly one, also impossible for a square. Thus class3 is absent, and class6 is absent by multiplication with the known class2. The two descent images have sizes4 and2, so the standard formula 2^rank=4·2/4 proves rank E(Q)=1. Now a−3=32 has no odd prime divisors, a≡3 modulo16, and 5 divides a. Equation (13) therefore applies to a=35 unconditionally.

## 9. Reproduction and scope of the checks

- [compute_p5_parameter_periods.py](../scripts/compute_p5_parameter_periods.py) contains the parameterized version of the audited original computation. Its sixteen inputs are a=5b−5 for b=0,…,15, with T=20 and N=30.
- [universal_p5_samples.json](../verification/universal_p5_samples.json) records all sixteen seven-digit M, c, and solution certificates.
- [universal_p5_polynomials.json](../verification/universal_p5_polynomials.json) records the coefficientwise universal polynomials modulo125.
- [check_universal_p5_residual.py](../scripts/check_universal_p5_residual.py) independently reconstructs interpolation and checks the universal polynomial equations, nilpotent mod5 reduction, denominator losses, parameter data, and arithmetic examples.

The finite checker verifies arithmetic identities. Sections 3–5 prove why those identities certify the entire analytic parameter family; Section 7 supplies the exact, rather than numerical, exceptional zero. The full-set corollary separately uses the already established rank, local-image, scalar-containment, and residual comparison theorems.

Reproduce the sixteen samples from the repository root with:

    python scripts/compute_p5_parameter_periods.py --output verification/universal_p5_samples.json

Check the published arithmetic certificate with:

    python scripts/check_universal_p5_residual.py

The parameter computation imports the already published scripts/compute_p5_residual.py; it uses the same original polynomial arithmetic and all identity checks. The standard-library checker does not need SymPy.
