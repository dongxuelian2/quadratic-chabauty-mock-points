# The complete rational-CM Weierstrass subcase

## Statement

Write

    C_a: y²=x⁶+a x⁴+a x²+1,
    E_a: Y²=X³+(a−3)X²−(a−3)X,
    a∈Q\{−1,3}.

The maps `(1+x²,y)` and `(1+x⁻²,y/x³)` induce an isogeny
`Jac(C_a) → E_a²`. Use the same Mordell–Weil abelian-image and
actual-local-image depth-two convention as in PROOF.md Section 13.

**Theorem.** The rational parameters for which `E_a` has geometric complex
multiplication are exactly

    0, −3/2, −15/16, −5, 15, −33, 255.

The parameter 0 has elliptic rank zero. Each of the other six has elliptic
rank one and Jacobian rank two. For each of these six curves, at every odd
prime of good reduction, **every locally visible Weierstrass point is
excluded from the full restricted depth-two set**.

This closes the Weierstrass-point question on the entire rational-CM
subclass of this reciprocal family. It does not classify non-Weierstrass
local points, prove a full endpoint-only equality at every prime, or settle
the non-CM residual transport problem.

The four new parameters are treated below by explicit algebraic torus
quotients. The cases −5 and 15 use the already proved torus arguments in
PROOF.md Section 15 and `cm15_torus_exclusion.md`. The treatment of the
CM field Q(√−7) permits nonzero actual targets at split bad primes; it does
not assume that its global S-unit space vanishes.

## 1. Why the parameter list is complete

Direct invariant calculation gives

    j(E_a)=256a³/(a+1).

The thirteen rational singular moduli are the entries of Table 1 of
Bilu–Luca–Masser, *Collinear CM-points*, arXiv:1503.08378, Section 5.
Substitution in `256a³−j(a+1)` gives the following rational roots; a=3 is
discarded because the original elliptic curve is singular.

| CM order discriminant | j | admissible rational a | rank E_a(Q) |
|---|---:|---:|---:|
| −3 | 0 | 0 | 0 |
| −4 | 1728 | −3/2 | 1 |
| −7 | −3375 | −15/16 | 1 |
| −8 | 8000 | −5 | 1 |
| −12 | 54000 | 15 | 1 |
| −16 | 287496 | −33 | 1 |
| −28 | 16581375 | 255 | 1 |

For the other six singular moduli, the primitive cubics and a prime at
which they have no root are:

| j | primitive cubic | prime |
|---:|---|---:|
| −32768 | a³+128a+128 | 3 |
| −884736 | a³+3456a+3456 | 5 |
| −12288000 | a³+48000a+48000 | 7 |
| −884736000 | a³+3456000a+3456000 | 11 |
| −147197952000 | a³+574992000a+574992000 | 17 |
| −262537412640768000 | a³+1025536768128000a+1025536768128000 | 41 |

The leading coefficient is a unit at each listed prime, so the root tests
prove irreducibility over Q. At j=0 the cubic is 256a³. At j=1728 it is
`64(a−3)(2a+3)²`, with the double root −3/2 and discarded singular
root 3. For the other factored cubics in the first table, the remaining
quadratic factors have nonsquare discriminants. These are
exact small arithmetic checks, not a search over bounded rational
parameters. The companion script verifies every factor and residue test.

## 2. Rank certificates

For `E(A,B): v²=u³+A u²+B u`, use classical two-isogeny descent:

    E'(A,B): v²=u³−2A u²+(A²−4B)u,
    2^rank E(Q)=|im δ_E| |im δ_E'|/4.

Here δ sends a nonzero u-coordinate to its squareclass, and the rational
two-torsion point to B. A candidate squarefree d dividing B requires a
primitive integral solution of

    N²=d U⁴+A U²V²+(B/d)V⁴.                  (1)

The already established elementary proofs cover a=−5 and a=15. The
remaining certificates are as follows.

For a=−3/2, the change `(u,v)=(4X−6,8Y)` identifies E_a with

    E_6: v²=u³−36u.

For a=−33, the rational two-isogeny

    (u,v)=((X−12+36/X)/4, Y(1−36/X²)/8)       (2)

maps E_a to E_6. The descent images for E_6 and its two-isogenous curve
`v²=u³+144u` have sizes 8 and 1. On E_6, the classes −1, 3 and 2 are
witnessed by `(0,0)`, `(12,36)` and `(18,72)`, and generate all eight
possible classes. On the isogenous curve negative classes are impossible
over R. The classes 2, 3 and 6 are impossible: for d=2, (1) has odd
2-adic valuation (one when U is odd, three otherwise); for d=3 or 6 its
3-adic valuation is one, because a primitive pair has
`U⁴+V⁴ != 0 mod3`. Thus rank E_6(Q)=1.

For a=−15/16, `(u,v)=(16X,64Y)` gives E(−63,1008). For a=255 use
E(252,−252) directly. Their exact descent images are

| curve (A,B) | descent image |
|---|---|
| (−63,1008) | {1,7} |
| (126,−63) | {1,−7,−3,21} |
| (252,−252) | {1,−7,2,−14} |
| (−504,64512) | {1,7} |

The lower bounds use the two-torsion points and respectively
`(−75,540)` on E(126,−63), and `(18,288)` on E(252,−252).
The points `(21,252)` and `(−14,224)` give the other displayed nontrivial
classes directly. For the upper bounds it is enough, by group closure,
to exclude these coset representatives:

| curve (A,B) | excluded d and modulus |
|---|---|
| (−63,1008) | 2 modulo16; 3 modulo9; 6 modulo16; negative classes over R |
| (126,−63) | −1 modulo16 |
| (252,−252) | −1 modulo16; 3 modulo16; −3 modulo32 |
| (−504,64512) | 2 modulo27; 3 modulo9; 6 modulo9; negative classes over R |

In each finite test, primitive pairs modulo q^k are covered by `V=1`
and arbitrary U, together with `U=1` and q dividing V: division by the
unit coordinate divides N by its square. None of the resulting residues
is a square. This proves each obstruction for all primitive integers;
the script exhausts at most 32 residues per chart. The real exclusions
hold because the quadratic factor `u²+A u+B` is positive everywhere.
The descent formula gives rank one in both cases.

For a=0 the same method gives descent images {1,3} and {1,−3}, of sizes
2 and 2. The first curve has no negative u-coordinate and the additional
class −1 on its two-isogenous curve is excluded modulo16. Hence its rank
is zero.

The point `(1,1)` is nontorsion in each of the six rank-one cases. In the
new cases this follows either from (2), where it maps to
`(25/4,−35/8)=2(12,36)` on E_6, or from a nonintegral coordinate of its
double on an integral short equation, by Nagell–Lutz. For a=−3/2 its
image `(−2,8)` differs from ±(12,36) by two-torsion. Thus the rational
abelian-image localization is injective in both factors at every good
prime: the p-adic logarithm of a nontorsion rational elliptic point is
nonzero. This is precisely the injectivity needed below, and makes no
claim about unrestricted global Bloch–Kato groups.

## 3. A rational-target lemma for imaginary norm-one tori

This is the step that treats nonzero actual targets.

Let K be imaginary quadratic and `T=Res^1_(K/Q) G_m`. Suppose a quotient
of the depth-two group has center `V_pT=Q_p(1)χ_K`, and suppose an
algebraic point W and a global reference class γ have the same abelian
class. Assume the reference is crystalline at p and unramified away from
a finite set S and p. Suppose the local difference at p is the Kummer
class of an algebraic element t in a splitting field, with t a p-adic
unit in every component used in the comparison.

Assume that every actual away-from-p central coordinate, measured from
γ, has rational normalized valuation after splitting T. This holds for
the algebraic torus bundles below: Betts, *The motivic anabelian geometry
of local heights on abelian varieties*, Theorem 1.1.6, identifies this
Kummer coordinate with the **Q-valued** Néron log-metric. A rational
basepoint not over the abelian origin causes no change: translate the
abelian variety and line bundle. Subtracting a proper reference path
also preserves rationality. The proper elliptic reference paths used
below have neutral away-from-p localization, because
`H¹(Q_q,V_pE)=0` for q≠p.

The same Néron log-metric is locally constant. The morphism from the
proper curve is defined at its coordinate endpoints too, and C(Q_q)
is compact. Hence each actual local image is finite, and the joint
target over the finite set S is finite. The lemma below needs only
the rationality of these values, but this also justifies the finite-target
description without an additional hypothesis.

**Lemma.** If t has a complex embedding with `|t| != 1`, it cannot be
the local difference of any admissible global class with those actual
local conditions.

**Proof.** A putative global difference α belongs to

    H¹_(f,S)(Q,V_pT)=(O_K[S_K^-1]^×⊗Q_p)^−.   (3)

Finite class groups contribute no Q_p-cohomology, and the crystalline
condition removes valuations at primes above p. Choose norm-one S-units
`u_1,...,u_r` forming a Q-basis of the minus space before tensoring with
Q_p. Such a basis can be obtained from ratios π/bar(π), after raising
split prime ideals to principal powers. At nonsplit primes the
anti-invariant valuation direction is zero. Ordinary units of K are
finite, so the valuation map on the norm-one S-unit space is injective.

Write `α=sum c_j κ(u_j)` with c_j∈Q_p. Take one prime above each split
prime in S. The corresponding valuation matrix B has integer entries
and full column rank over Q. The actual local conditions give

    Bc=v,             v∈Q^r.                 (4)

If more valuation rows are retained, the same conclusion uses any
full-rank minor, or a rational left inverse. Hence **every c_j is
rational**. The conclusion would be false for an arbitrary element of
the Q_p-span without the actual local conditions.

Clear denominators by N>0 and put `u=product u_j^(Nc_j)`. Then u∈K^×,
`u bar(u)=1`, and u is a unit at primes above p. Equality of the local
classes gives

    log_p(t^N/u)=0

after a finite splitting extension. The kernel of the logarithm on
local units consists of roots of unity, so the algebraic number t^N/u
is a root of unity. Every complex embedding of the imaginary-quadratic
norm-one number u has absolute value one. Every complex embedding of a
root of unity does too. This contradicts `|t| != 1`. ∎

The lemma simultaneously separates t from the entire actual finite
target. It needs neither vanishing of (3) nor localization injectivity
on an enlarged Q_p-vector space. It is special to an Artin–Tate central
quotient; it does not solve the non-CM Sym² transport problem.

If the norm-one S-unit space in (3) is zero, a simpler version applies:
any t which is a local unit and is not a root of unity gives exclusion,
without an archimedean absolute-value condition. We use this version
for the four extra Weierstrass points on C_(−3/2).

## 4. The geometric torus construction and reference fibers

All new constructions have two rational maps `h1,h2:C→E` with
independent holomorphic pullbacks, and an endomorphism η over K with

    bar(η)=−η,       η†=−η.

Put `D=E×E`, `M=O_E(O)`, `m±(R,S)=R±ηS` and

    L=m+*M ⊗ (m−*M)^−1.

Conjugation interchanges the two factors. Combining this interchange
with inversion on fibers descends L^× to a T-torsor X over D. If σ is
the ratio of the canonical sections of M and

    div(g)=(h1+ηh2)*(O)−(h1−ηh2)*(O),
    bar(g)=g^−1,

then `σ/g` is an everywhere nonvanishing section on C and gives a
morphism `C→X` defined over Q. Its induced unipotent quotient has center V_pT.
The Chern-class matrix is

    [[0,2η],[-2η,0]],

which is nonzero. The independent h1,h2 induce an isogeny on the
Jacobian, so this is a detecting quotient of full depth two.

For clarity the reference is constructed using proper curves. Along
`E×{O}`, the two factors of L are identical, giving a section e1. Along
`{T0}×E` with T0 two-torsion, use the symmetric linearization of M,
since m−=−m+. Its fiber sign is +1 at a nonzero two-torsion image and
−1 at O. The latter sign follows from the odd parameter `t=−u/v` and
the frame `t^−1` of M at O. These sections are defined over Q after
torus descent, and give global reference paths through one or two
proper elliptic curves.

Both W± have rational torsion images in D. The rank-one calculation
makes their admissible global abelian image equal to that of the
reference. Central cohomology acts freely because `H⁰(Q_p,V_pD)=0`.
A central difference between crystalline lifts is crystalline: twist
by the crystalline reference and apply exactness of D_cris to the
resulting Lie extension, exactly as in the previously proved torus
argument. Thus (3) applies to a hypothetical full-depth-two lift.

At a common origin fiber, σ cannot be replaced by 1. Its value is the
limit `t(h1+ηh2)/t(h1−ηh2)`. The limits below include the exceptional
third-order case for a=−33.

## 5. The two curves with CM field Q(i)

### 5.1. The rational parameter a=−3/2

Use E_6 and η(u,v)=(−u,iv), together with

    h1=(4x²−2,8y),        h2=(4/x²−2,8y/x³),
    g=(x²+ix−1)/(x²−ix−1).                    (5)

Both maps have degree two. The equation for equality of the two
u-coordinates in h1 and ηh2 is `x⁴−x²+1=0`. Modulo the numerator
quadratic of g one has `x³=−i`, so ηh2=−h1; modulo its denominator one
has `x³=i`, so ηh2=h1. These four roots are distinct, non-Weierstrass,
and not poles of either map. Each gives two simple points in the
appropriate origin fiber. The map degrees are four: their sum is
eight by the parallelogram identity, and x↦−x exchanges the maps.
This accounts for every origin point and proves the divisor identity.

At b=(0,1), `h(b)=((-2,8),O)` and g(b)=1. At W=(i,0), both images are
`T_−=(-6,0)`, while ηT_−=`T_+=(6,0)`; the common m± image is the
nonzero two-torsion point `(0,0)`. Hence σ(W)=1. The proper reference
through `(T_−,O)` has terminal coordinate +1, so its relative torus
value is

    t_W=1/g(i)=1/3.                           (6)

For W_− it is the inverse. Only 2 and 3 are bad, and neither splits in
Q(i); therefore the global space (3) is zero. Alternatively (6)
satisfies the general lemma.

The other four Weierstrass points have x=±√2 and x=±1/√2. Their h1,h2
images are `(T_+,T_0)` or `(T_0,T_+)`, with `T_0=(0,0)`, and the
common m± image is nonzero two-torsion. Again σ=1 and the proper
reference has coordinate +1. Evaluation of (5) gives, up to inversion,

    t=(-1+2√−2)/3.                            (7)

Its trace is −2/3, so it is not an algebraic integer and cannot be a
root of unity. It is a unit at every p≠2,3. The zero-global-space
version of the lemma excludes these four points at every good odd
prime where they are visible, including primes at which i is not in
Q_p. In that case compare after the quadratic splitting extension;
restriction is injective in Q_p-cohomology.

### 5.2. The integer parameter a=−33

Compose the original quotients with (2). Explicitly, writing the
v-coordinate as its displayed coefficient times y,

    h1u=(x²−5)²/[4(x²+1)],
    h1v=(x²−5)(x²+7)y/[8(x²+1)²],
    h2u=(5x²−1)²/[4x²(x²+1)],
    h2v=−(5x²−1)(7x²+1)y/[8x³(x²+1)²],
    g=(x−i)(x²+4ix−1)/[(x+i)(x²−4ix−1)].     (8)

Here h1,h2 have degree four, and h1±ηh2 have degree eight. The finite
non-pole equality of u-coordinates has numerator `x⁴+14x²+1`.
The factor `x²+4ix−1` gives the plus origin fiber and its conjugate
gives the minus origin fiber, each contributing four simple points.
The two Weierstrass points W± map to (O,O). The plus map has orders
3 and 1 at W+ and W−; the minus map has orders 1 and 3. Thus each
fiber has total degree eight, and the divisor of (8) is exactly the
required difference. Notice that the factor `(x−i)/(x+i)` has divisor
`2W+−2W−` on C.

Here is the full exceptional limit. Put `F=x⁶−33x⁴−33x²+1` and
`c=1/F'(i)`. In the local parameter y at W+,

    x−i=c y²+O(y⁴),
    (h1±ηh2)*ω=2(x∓i)dx/y,
    t(h1+ηh2)=(4/3)c²y³+O(y⁵),
    t(h1−ηh2)=8ic y+O(y³).

Therefore

    σ=(x−i)/(6i)+O((x−i)²),
    g=−3(x−i)/(2i)+O((x−i)²),
    (σ/g)(W+)=−1/9.                           (9)

At b the lifted fiber coordinate is −1. The proper section −e1 on
E×{O} goes directly from h1(b) to (O,O), with terminal coordinate −1.
Dividing (9) by that reference gives

    t_W=1/9,                                  (10)

with inverse at W−. The bad primes are again only 2 and 3. Thus both
points are excluded at every visible good prime.

## 6. The CM field Q(√−7), including nonzero target directions

Put s=√−7 and use the short curve

    E: v²=z³−315z+2646.

Let

    k=z³−21z²−189z+2457,
    U=(z⁷−42z⁶+3087z⁵+15876z⁴−1972593z³
          +29172150z²−208289151z+924173712)/k².

The endomorphism is

    η(z,v)=(u(z),w(z)v),
    u=−U/7,            w=−U'/(7s).            (11)

Exact substitution verifies the curve equation and `u'=s w`. The map
fixes O and has degree seven, so it is an endomorphism with
`η²=[−7]`, conjugate −η and Rosati dual −η. The kernel polynomial k
is also the rational cubic factor of the seventh division polynomial;
(11) can be reconstructed directly by Vélu's formula. On the
quadratic twist `E_d:v²=z³−315d²z+2646d³`, replace u(z) by d u(z/d)
and w(z) by w(z/d).

### 6.1. The rational parameter a=−15/16

Use E with

    h1=(16x²−5,64y),        h2=(16/x²−5,64y/x³).

Define

    P_s=(7x³+6s x²−8s)(43x⁴+13s x³−54x²−8s x+8),
    g=P_s/P_(-s).                              (12)

The numerator of `h1z−u(h2z)` is, up to a nonzero constant,

    (x²+1) P_s P_(-s).

The ratio `η(h2)_v/h1v` is −1 at every root of P_s and +1 at every
root of P_(-s). Neither polynomial has repeated roots, shares a root
with the other, a Weierstrass root or a pole, or vanishes at x=±s.
These assertions are exact polynomial gcd and remainder identities
over Q(s), verified by the script. Thus each contributes fourteen
simple origin points. W± are common simple origins, giving exactly
sixteen points in each fiber; the parallelogram identity and the
x↦−x involution prove that sixteen is the map degree. This establishes
the complete divisor identity for (12).

At b one has g(b)=−1. At W both elliptic images are `T=(-21,0)`,
and ηT=T. The terminal m± image is O, so the section ratio is the
nontrivial limit `(i−s)/(i+s)`. The proper reference via `(T,O)` has
terminal coordinate +1, by the origin-fiber sign explained in Section
4. With r=s/i, r²=7, the resulting relative value is

    t_W=(431−160r)/81,
    81t_W²−862t_W+81=0.                       (13)

For example `(P_s/P_(-s))(i)=−(604+209r)/243`; inserting the section
ratio gives (13). Its conjugate is its inverse. It has a real embedding
with absolute value different from one and is a unit away from 3.

### 6.2. The integer parameter a=255

Use E_8 and the rational two-isogeny from E_255. The two maps are

    h1z=(x⁴+86x²−167)/(x²+1),
    h1v=(x⁴+2x²+253)y/(x²+1)²,
    h2z=−(167x⁴−86x²−1)/[x²(x²+1)],
    h2v=(253x⁴+2x²+1)y/[x³(x²+1)²].

Use the d=8 version of (11). An explicit primitive polynomial for the
divisor function is

    P_s = 42453593 x¹³ + 62753181 s x¹² − 271681298 x¹¹
          − 72395730 s x¹⁰ + 75687395 x⁹ + 2718759 s x⁸
          + 14565684 x⁷ + 1712724 s x⁶ − 478065 x⁵
          − 31205 s x⁴ − 7938 x³ − 610 s x² + 21x+s,
    g=P_s/P_(-s).                              (14)

The numerator of `h1z−η(h2)z` is proportional to

    (x⁴+254x²+1) P_s P_(-s).

Each root of P_s is a simple plus-origin x-coordinate, and each root
of P_(-s) a simple minus-origin x-coordinate. The sign of the
v-coordinate ratio is respectively −1 and +1. The four roots of the
displayed quartic are common Weierstrass origins. The two W± are
additional common origins at poles of h1,h2, and must be added rather
than read from the numerator of the coordinate difference. Both map
to (O,O), and both plus and minus maps have nonzero differential there.
This gives `26+4+2=32` simple points in each fiber, which is the exact
degree by the parallelogram argument. The script checks the required
coprimality, derivative and sign identities; this degree count proves
that no exceptional-chart origins are omitted.

At b, g(b)=−1. The proper reference is the section −e1 directly to
(O,O), so its terminal coordinate is −1. At W the section ratio is
`(i−s)/(i+s)`. Consequently

    t_W=(364961−137920r)/6561,
    6561t_W²−729922t_W+6561=0,                 (15)

where r=s/i and r²=7. An intermediate exact value is
`g(i)=(494404+186719r)/19683`. Again the other embedding or the other
Weierstrass point gives the inverse; both real absolute values differ
from one. The value is a unit away from 3.

### 6.3. The actual target comparison

The four curves in Sections 5–6 have good reduction outside {2,3,7}
(7 is unnecessary in Section 5). This follows from their exact
sextic discriminants and the displayed elliptic equations. A visible
W requires p≡1 mod4; such a good prime never equals 2,3 or7.

In Q(√−7), the prime 2 **splits**. Hence the space (3) can be nonzero;
discarding it would invalidate the proof. The local Néron-metric
rationality and the valuation-matrix argument in Section 3 apply to
the actual conditions at every bad prime, including 2. Equations (13)
and (15) then exclude W from **all** their allowed rational S-unit
combinations. This is an exact finite-target separation proof, with no
uncomputed p-adic transport constant and no assumption that the
allowed target is zero.

## 7. The other Weierstrass points and completion of the theorem

For integral a∈{−5,15,−33,255}, the sextic is monic with constant term
1. The established first-height unit obstruction says that a surviving
Weierstrass point must have root-of-unity x-coordinate. The only such
roots are ±i. Indeed the other squared coordinates satisfy

    z²+(a−1)z+1=0,

whose real trace `1−a` has absolute value greater than 2 in these four
cases. Thus the other four points are already excluded by a scalar
necessary condition, and hence from full depth two. Sections 5–6 and
the two earlier CM torus proofs exclude the remaining pair.

For a=−15/16, put Y=4y to use the integral model
`Y²=16x⁶−15x⁴−15x²+16`; its equal leading and constant coefficients
are units at every odd prime. Thus the established first-height
root-power criterion applies without extending its integral-model
hypotheses. The other four squared coordinates have complex absolute
value one and trace 31/16. The general root-power criterion from
PROOF.md applies: a first-height target equality with rational
prime-log coefficients would force some positive power of x to be a
rational number, up to a root of unity. Taking complex absolute values
makes x itself a root of unity. Then `x²+x⁻²=31/16` would be a
rational algebraic integer, a contradiction. This argument does not
need a monic-unit hypothesis or a zero dyadic target. The two W points
are handled by (13).

For a=−3/2, equations (6) and (7) handle all six Weierstrass points
directly. All six parameters have rank one by Section 2; their
Jacobians therefore have rank two. This proves every assertion of the
theorem.

## 8. Verification and provenance

Run

    python scripts/check_rational_cm_packet.py

The checker verifies rational-CM completeness against the thirteen
known singular moduli; the finite congruence obstructions and rational
rank witnesses; all four new elliptic maps; the degree-seven CM
endomorphism; the full polynomial fiber decompositions and signs;
the exceptional a=−33 limit; the exact reference-relative values;
and the non-root-of-unity/absolute-value tests. The cohomological
actual-target argument and the origin-fiber degree counts are proved
above and are not replaced by that finite computation.

Primary sources used here:

- Yuri Bilu, Florian Luca and David Masser, *Collinear CM-points*,
  Algebra & Number Theory 11 (2017), Section 5, Table 1:
  https://arxiv.org/abs/1503.08378 . This supplies the standard complete
  rational-singular-modulus list, not a novelty claim for that list.
- L. Alexander Betts, *The motivic anabelian geometry of local heights
  on abelian varieties*, Memoirs AMS 302 (2024), no. 1518, Theorem
  1.1.6 and Section 3 (especially the valuation normalization):
  https://arxiv.org/abs/1706.04850 and
  https://doi.org/10.1090/memo/1518 . The normalized actual local
  Kummer metric is rational valued. The original paper was checked,
  including its line-bundle rather than punctured-elliptic scope.
- The existing two-isogeny descent and torus references in PROOF.md
  apply with the explicit maps and signs proved here. The new global
  argument uses actual local rationality to restrict coefficients to
  Q; it makes no assertion of general p-adic regulator injectivity.

The complete rational-CM Weierstrass conclusion is established here.
The non-CM example a=−157469,p=5 still requires comparison with
`{0,±Θ_5(e_37)}` in a non-Artin–Tate residual representation; the
imaginary S-unit proof above does not transfer to that representation.
