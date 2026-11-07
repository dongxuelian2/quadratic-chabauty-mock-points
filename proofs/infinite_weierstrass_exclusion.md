# Exact first-height criterion and an infinite non-CM exclusion family

## Scope

Write a=M/D in lowest terms, D>0, a!=-1,3. An eligible prime in this note means an odd p with

    p does not divide D(M-3D)(M+D).

Thus the displayed curve C_a and its elliptic quotients have good reduction. The statements concern all local Weierstrass points at every such prime, not all non-Weierstrass points. Full depth two uses the Mordell-Weil-restricted, actual-local-image convention of the manuscript.

## 1. The first-height containment extends to rational a

Replace y by y'=Dy. The integral equation becomes

    (y')²=D²x⁶+MDx⁴+MDx²+D².

Both displayed elliptic quotients of this model are the same scaling (X,Y)->(D²X,D³Y) of the original untranslated elliptic quotient. Translating the latter's X-coordinate by one gives E_a: Y²=X³+(a-3)X²-(a-3)X.

The local-height change under the common scaling is the same in both elliptic factors, and cancels in their difference at every place. Under the compatible invariant-differential scaling the logarithms are multiplied by the same nonzero factor, while alpha=h(P)/L(P)² changes by its inverse square. Hence alpha L² is unchanged. The coordinate x is unchanged.

Therefore the function rho_p and every actual local function w_q agree with those on the original rational-coefficient model, provided the TRUE global height is used. In particular one must retain h_p(P)=lambda_p(P)+(1/2)log_p(D) under the dyadic hypothesis of Theorem 32.

Apply Theorem 18 and the proved endpoint-basepoint bridge to the integral model. If E_a has rank one, then

    C_a(Q_p)_2 is contained in {z: rho_p(z) in Omega_p},
    Omega_p=sum_(q!=p) w_q(C_a(Q_q)).

No new endpoint or rational-basepoint density assumption is needed.

## 2. Rational independence of the prime logarithms

For finitely many distinct rational primes q!=p, the numbers log_p(q) are linearly independent over Q. Indeed, clear denominators in any rational relation to obtain log_p(r)=0 for a positive rational r supported on these primes. Its p-adic valuation is zero, so r is a root of unity. A positive rational root of unity is 1, and unique factorization forces all exponents to vanish.

This is Q-linear independence, not Q_p-linear independence. All local target coefficients under discussion are rational, so the former is exactly what is required. Consequently zero belongs to a sum of these actual local images if and only if each individual local coefficient image contains zero.

## 3. Exact first-height test for W_±=(±i,0)

Assume a belongs to Z_2 and a=3 modulo 8. At p=1 modulo 4, both points are visible and rho_p(W_±)=0: the two elliptic images are the same two-torsion point, their logarithms vanish, and log_p(i)=0.

At locally integral odd primes the first actual target is zero. The dyadic target is zero under the stated congruence. At an odd denominator prime q, put m=-v_q(a)>0 and beta=q^m a. By Theorem 32 its first local image contains zero exactly when

    q=1 modulo 4,
    OR m is even and (q!=3 OR (beta/q)=-1).

Thus W_± pass the first-height candidate condition if and only if this displayed test holds at EVERY denominator prime.

Failure at even one denominator prime excludes both points from full depth two. Passing all tests proves only membership in the first-height candidate set, not full membership. In particular, a denominator prime q=3 modulo 4 of odd multiplicity always excludes the pair. The exceptional q=3, even multiplicity, square-beta failure must not be omitted.

The same obstruction excludes every locally visible point with x=±1. At x=1 the two elliptic images coincide; at x=-1 they are negatives. Symmetry of the local height and the squared logarithm, together with log_p(-1)=0, again gives rho_p=0. These four points have y=±sqrt(2(a+1)). This is an actual exclusion of non-Weierstrass points whenever a denominator target omits zero.

## 4. The other four Weierstrass points for -1<a<3

Suppose a is rational, nonintegral, and -1<a<3. The factorization is

    x⁶+a x⁴+a x²+1=(x²+1)(x⁴+(a-1)x²+1).

For a root r of the quartic put u=r². It satisfies

    u²+(a-1)u+1=0.

Since |a-1|<2, its complex roots are conjugate and both have absolute value one.

At every eligible prime admitting W=(r,0), the two-torsion identity gives rho_p(W)=-(1/2)log_p(u). If it equals an actual target sum with rational coefficients c_q, choose a positive integer d with all 2dc_q integral. Then

    u^d * product_(q!=p) q^(2dc_q)

has p-adic logarithm zero. It is a p-adic unit, since r is a unit at every eligible prime. Hence this algebraic number is a root of unity.

Take any complex embedding. Since |u|=1, the positive rational factor product q^(2dc_q) has absolute value one, so it equals one. Therefore u is a root of unity. But u+u^-1=1-a is then a rational algebraic integer, and hence an integer. This contradicts the assumed nonintegrality of a.

Thus ALL FOUR quartic Weierstrass points fail the first-height condition whenever locally visible. This conclusion is independent of the target values and of the global-height denominator correction. If rank E_a(Q)=1, it excludes those points from full depth two.

## 5. An unconditional infinite non-CM family with no Weierstrass members

Use Zywina's construction with K=Q and the quadratic extension Q(i), that is source twist parameter -1. Rename its two S-integers m,b and put

    a=(3b-5m)/(b+m).

Theorem 1.5 and Section 4 produce infinitely many parameters in (-1,3), with rank E_a(Q)=1 and infinitely many geometric genus-two isomorphism classes, as established in Theorem 33. The source's dyadic conditions give a=3 modulo 8.

Let q2 be the distinguished prime outside S generated by m+b. Zywina's Lemma 3.8 proves it is inert in Q(i), so q2=3 modulo 4. The distinct prime-ideal conditions give

    v_q2(m)=0,  v_q2(m+b)=1.
    3b-5m = 3(m+b)-8m is a q2-adic unit.

Therefore v_q2(a)=-1. In particular a is nonintegral, and Section 3 excludes W_± at every eligible prime where they are visible. Section 4 excludes the other four Weierstrass points at all eligible primes where they are visible. We conclude:

    C_a(Q_p)_2 contains no Weierstrass point
    for every eligible odd p.

The four points with x=±1 are likewise excluded whenever locally visible. Thus the result excludes a ten-point geometric packet: all six Weierstrass points and these four non-Weierstrass symmetry points.

Moreover j(E_a)=256a³/(a+1) has q2-valuation -2. A CM j-invariant is an algebraic integer, so every curve in this family is geometrically non-CM. No removal of an unspecified finite CM subfamily is needed. Since J_a is isogenous to E_a², its rational rank is two.

The same initial choice in Theorem 33 can prescribe any eligible fixed odd prime neighborhood v_p(a+5)>=N. The infinite family still has second target Omega*={0}. It is the nonzero first denominator target, not a nonvanishing assertion about the Sym² discrepancy, that excludes the pair.

Source: D. Zywina, [Rank one elliptic curves and rank stability, arXiv:2505.16960v1](https://arxiv.org/html/2505.16960v1), Theorem 1.5, Lemma 3.8, the prime-ideal identities (3.13), and Section 4. Rank/isogeny transfer and geometric distinctness are detailed in infinite_zero_second_target.md.

## Limits

This supplies actual full-depth-two exclusions for every Weierstrass point in an unconditional infinite non-CM family. It does not identify all non-Weierstrass members, prove an infinite family of endpoint-only full-depth-two equalities, or compute delta_p(i,0) in the residual quotient. No conclusion is asserted here at primes outside the explicit eligible set.
