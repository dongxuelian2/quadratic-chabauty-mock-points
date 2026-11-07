# The two remaining prime-13 scalar lifts and their second-height exclusion

Status: the coefficient identities, all-orders estimates, target conditions and arithmetic examples have passed independent review. This is a continuation of the uniform prime-13 period theorem; it makes no unproved scalar-sufficiency assertion.

## 1. Local analytic statements

Let a be an odd integer with a≡9 modulo13. Retain the fixed compatible elliptic complements and the first and second scalar heights rho,rho* from the earlier proofs. Put

    A=a−3, P=(1,1) on E_a:Y²=X³+AX²−AX,
    ell=L(P), h=λ(P), Z=ζ(P), alpha=h/ell².

Then:

1. The first scalar alone has exactly six zeros unless possibly

       a≡581 or1426 modulo2197.                    (1)

   These are the four rational endpoints (0,±1),∞± and W±=(±i,0).

2. For every odd integer a≡9 modulo13, with no omitted lift, the simultaneous zero set rho=rho*=0 consists exactly of those six centers.

These are local analytic statements and do not require a rank or away-from-13 target hypothesis. The two residue classes in (1) are exceptions to the first-scalar proof, not assertions that extra zeros exist there.

## 2. Constants in the previously omitted lift

The earlier prime-13 argument already gives six first-scalar centers unless a≡74 modulo169. Consider this remaining class. The exact quintuple formulas from that proof give uniformly

    ψ₅(P)/13≡12,  N≡9,  Q≡3,
    t₅/13≡3,  ell/13≡11,  Z≡5 modulo13.           (2)

In particular v₁₃(ell)=1. The previous height congruence h/13≡10−2b, b=(a−9)/13, vanishes because b≡5. Thus h∈13²Z₁₃ and alpha is integral.

There is a finer exact congruence. Write a=74+169c. The formal local height has

    B(t)=(a−1)t²/2+O(t⁴),

with the established entire-series denominator bounds. For t=t₅ of valuation one, all omitted terms have valuation at least four. If U=ψ₅(P)/t₅ and e=U¹²−1, then e∈13²Z₁₃ throughout this critical lift and

    log₁₃(U)≡e/12 modulo13³.

The omitted logarithm terms have valuation at least four. Exact evaluation at a=74, together with U′/U≡1 modulo13, gives

    log₁₃(U)/169≡12+c,
    B(t₅)/169≡10,
    alpha≡12+6c modulo13.                         (3)

The last equation uses h=(2/25)(log(U)−B(t₅)) and ell/13≡11. Variation by169c affects log(U) by169c·U′/U modulo13³; all quadratic parameter terms have valuation at least four. Hence (3) holds throughout each full congruence class, not just at the thirteen tested integers.

## 3. Endpoint disks

At either finite endpoint disk, with x as parameter, the first scalar has exact quadratic coefficient

    kappa=1−Z+alpha(1−ell).

When alpha and Z are integral, the established single- and double-integration bounds give

    rho(x)/x²∈kappa+13²Z₁₃  for x∈13Z₁₃, x≠0.

In the present lift kappa≡alpha−4 modulo13. By (3) it is a unit unless c≡3, namely a≡581 modulo2197.

The second scalar has exact linear slope

    s=−2(1+Z+alpha·ell)≡1 modulo13.                 (4)

Its integrated endpoint formula is the one proved in second_height_endpoint_exclusion.md, in the same compatible splitting. It is odd in x. Every coefficient d_n satisfies v₁₃(d_n)≥−2floor(log₁₃ n). For odd n≥3,

    n−1−2floor(log₁₃ n)≥2,

with the bound tending to infinity. Below degree13 this is immediate; above it use floor(log₁₃ n)≤n/13, which follows from 13^k≥13k. Therefore rho*(x)/x∈s+13²Z₁₃ throughout each punctured endpoint disk. It never vanishes. Old reciprocity preserves rho*, giving the same assertion at both infinity endpoints.

Thus the second zero condition always isolates the four endpoint centers in the whole previously omitted lift.

## 4. Exact Weierstrass quadratic coefficients

Let W=(r,0), r²=−1. Since f′(r)=−2rA is a unit, the disk is parametrized by y∈13Z₁₃, with x(y)∈r+y²Z₁₃[[y²]]. Both quotient logarithms and odd primitives vanish at their common two-torsion center.

For the first pair, the logarithm slopes are

    l₁=−1/A,  l₂=−r/A.

The primitive satisfies dζ=−(X−2)ω, so at X=0 the quadratic local-height coefficient is −2l_j². The local-height difference contributes −4/A², the term −2log(x) contributes −1/A, and the global quadratic correction contributes −2alpha/A². Hence

    [y²]rho=−(a+1+2alpha)/A².                      (5)

Modulo13 this is a unit unless alpha≡8. Equation (3) shows that this can happen only at c≡8, namely a≡1426 modulo2197.

For the second pair, put u=(x+1)/(x−1), v=4y/(x−1)³, c₀=(a+1)/2. Its elliptic model is

    E′:Y²=T³−2AT²+A(A+4)T,
    F₁=(c₀(1+u²),c₀v), F₂=(c₀(1+u⁻²),c₀v/u³).

The compatible data are dζ′=−(T−a−1)ω′ and alpha′=2alpha. Direct pullback gives

    F₁*ω′=−(x+1)dx/(2y),
    F₂*ω′=(x−1)dx/(2y).

Their y-slopes are l₁′=(1−r)/(2A) and l₂′=−(1+r)/(2A), whose squared difference is −r/A². The local-height difference contributes (a+1)r/A², −2log(u) contributes −r/A, and the global quadratic correction contributes 2alpha r/A². Therefore

    [y²]rho*=2r(2+alpha)/A².                       (6)

The two coefficients (5) and (6) cannot both vanish modulo13. If the second vanishes, alpha≡−2, and the numerator of the first becomes a−3=A, a unit.

## 5. Entire Weierstrass disks, not just quadratic terms

All quotient-coordinate and pulled-back differential series on this disk are integral: x, x−1, x+1 and A are units. The single primitives start at zero. The two heights, products of logarithms and explicit logarithms therefore satisfy the common bound

    v₁₃([y^n]rho), v₁₃([y^n]rho*)≥−2floor(log₁₃ n).

Both scalars are even in y and have zero constant. For every even n≥4,

    n−2−2floor(log₁₃ n)≥2,

and the bound tends to infinity, by the same elementary inequality used in Section3. Thus, after division by y², both complete higher tails lie in13²Z₁₃. The unit among (5) and (6) excludes every noncentral point from the simultaneous zero locus. No truncated Taylor test is being used.

The first scalar alone isolates W when (5) is a unit. Combining this with Section3 and the previously proved noncritical case proves statement1. The second scalar handles all endpoint disks in the critical case, and (5)–(6) handle both W disks, proving statement2. All six centers satisfy both zero conditions. The smooth reduction has exactly those six disks, so none are omitted.

## 6. Exact actual-target hypotheses

Now suppose a≡3 modulo8 and rank E_a(Q)=1. The actual first scalar target is {0}. The second actual target is {0} precisely when each odd prime q dividing a+1 satisfies

    m=v_q(a+1)=1,
    or m is odd and (2/q)=−1.                      (7)

In particular, a squarefree odd part of a+1 suffices. Here q≠13 because a≡9 modulo13. The exact local theorem gives, after multiplication by log₁₃(q):

- if (2/q)=1: coefficients0 and ±2k(m−k)/m, 1≤k≤floor(m/2);
- if (2/q)=−1 and m odd: only0;
- if (2/q)=−1 and m even: coefficients0 and ±m/2.

Each local image contains zero, and log₁₃(q) is nonzero. Hence the global Minkowski sum is {0} exactly under (7). This condition does not follow from the splitting behavior of primes dividing a−3.

For example a=4299 lies in the critical class and satisfies a≡3 modulo8, with a−3=8·3·179 and both odd factors3 modulo4. Nevertheless a+1=4·5²·43 gives the nonzero second target ±log₁₃5. No rank is asserted for that example. Rank one does not imply (7) either: the already certified a=−1373 has a+1=−4·7³ and nonzero second values ±(4/3)log₁₃7, although that parameter is outside the present prime-13 disk.

## 7. Full depth-two consequence

Assume

- a is an integer with a≡3 modulo8 and a≡9 modulo13;
- E_a(Q) has rank one;
- every odd prime dividing a−3 is3 modulo4;
- if a≡581 or1426 modulo2197, condition (7) holds.

Then, under the established Mordell–Weil-abelian-image and actual-local-image convention,

    C_a(Q₁₃)₂=C_a(Q)
       ={(0,1),(0,−1),∞₊,∞₋}.                     (8)

Outside the two fine classes, the first scalar alone gives the six-point upper bound, with no second-target assumption. In the two classes, (7) and the two independently justified scalar containments give the simultaneous-zero upper bound. For the second containment the transformed basepoint is (u,v)=(−1,−4), away from the coordinate endpoints, so the direct comparison theorem applies.

The actual dyadic image is zero by the separately proved four-disk theorem for every a≡3 modulo8. The odd-prime condition makes every other residual target zero. These parameters are geometrically non-CM by the j-invariant denominator argument; the only possible integral exceptions a=3,−5 do not occur in this prime-13 residue class. The uniform prime-13 period has valuation exactly two, so the exact residual comparison excludes W±. Rational-point containment gives the reverse inclusion in (8).

No claim that scalar membership is sufficient for full membership is made. Without the zero residual-target hypothesis, the scalar arguments prove the rational-point equality and at most the corresponding four-versus-six full-set dichotomy, not necessarily the four-point full set.

## 8. Unconditional examples in both fine classes

The established prime-pattern rank theorem applies when r and 8r−1 are prime and r≡3 modulo8, for a=3−32r. Exact trial division verifies

    r=326923, 8r−1=2615383, a=−10461533≡581 modulo2197;
    r=95731,  8r−1=765847,  a=−3063389≡1426 modulo2197.

In both cases a≡3 modulo16, the only odd residual prime is r≡3 modulo4, and a+1=−4 times a prime gives (7). Thus (8) applies unconditionally in both remaining quadratic-degeneracy classes. This does not assert that either example actually has extra first-height zeros; it shows that the second-height proof covers both exceptional leading-coefficient patterns. No infinitude is asserted.

The smaller example a=−1505885, from primes47059 and376471, lies in the earlier critical class modulo169 but has residue1257 modulo2197. The refined first-scalar theorem already covers it without a second-target assumption.
