# Second-height exclusion of endpoint bifurcations

## 1. Statements

Retain the reciprocal family C_a, first elliptic quotient E_a, constants ell=L(P), Z=ζ(P), alpha=λ(P)/ell², and fixed complements of uniform_endpoint_families.md.

For odd a in either omitted lift
p=7, a≡46 mod49, or p=11, a≡24 mod121,
the second-model scalar rho* defined below has exactly the four rational endpoint zeros in C_a(Q_p). In particular, all eight extra first-height zeros, when present, fail the zero second-height condition.

If also a≡3 mod8, rank E_a(Q)=1 and the second actual local-image target is {0}, then C_a(Q_p)₂=C_a(Q) consists exactly of (0,±1) and infinity_±, in the stated Mordell–Weil-abelian-image, actual-local-image convention.

Combining with the earlier first-height theorem removes the omitted-lift exceptions under those arithmetic assumptions: the full conclusion holds for all a≡4 mod7 at7, or all a≡2 mod11 at11. A rank-certified example is a=−14974109 at7, where the first scalar has twelve zeros but the full restricted depth-two set has four.

## 2. Second model and exact endpoint constants

Set A=a−3, c=(a+1)/2,
u=(x+1)/(x−1), v=4y/(x−1)³.
Then v²=c(u⁶+1)+(8−c)(u⁴+u²). Its identical quotients are
E':Y²=T³−2AT²+A(A+4)T,
F1=(c(1+u²),cv), F2=(c(1+u^(-2)),cv/u³).
Use dζ'=−(T−a−1)ω', dλ'=−2ζ'ω' and the compatible coefficient alpha'=2alpha. Thus
rho*=λ'(F1)−λ'(F2)−2log_p u−2alpha L'(F1)²+2alpha L'(F2)².

The two-isogeny φ(X,Y)=(X+A−A/X,Y(1+A/X²)) satisfies φ*ω'=ω and
φ*((T−a−1)ω')=2(X−2)ω−d(Y/X).
Consequently ζ'(φ(Q))=2ζ(Q)+Y(Q)/X(Q): derivatives agree and oddness removes the integration constant.

For R=(a+1,2(a+1)) on E', direct doubling has tangent slope3 and gives 2R=(1,a−2)=φ(P). Also D'log(2Y)(R)=6. Duplication therefore gives
ζ'(2R)=2ζ'(R)+3=2Z+1,
so exactly
L'(R)=ell/2, ζ'(R)=Z−1.
The complement compatibility and alpha'=2alpha use polarized isogeny functoriality, not an ordinary or unit-root assumption.

## 3. Exact integrated formula

On either finite endpoint disk, write y=ε/q(x), ε=±1,
q(x)=(1+ax²+ax⁴+x⁶)^(-1/2)∈Z_p[[x]].
Define zero-constant primitives
J=integral_0^x q(t)dt, I=integral_0^x t q(t)dt,
U+=(a+1)integral_0^x t(t+1)(t−1)^(-2)q(t)dt,
U−=(a+1)integral_0^x t(t−1)(t+1)^(-2)q(t)dt.

Direct pullback gives
F1*ω'=−(x+1)dx/(2y), F2*ω'=(x−1)dx/(2y).
Their values at zero are −εR and εR. Hence
L'(F1)=−ε(ell+I+J)/2, L'(F2)=ε(ell+I−J)/2,
ζ'(F1)=ε(1−Z+U+), ζ'(F2)=ε(Z−1+U−).

Integrating yields the exact identity
rho*=2(1−Z)J−4 integral_0^x dt/(1−t²)
 + integral_0^x q(t)[(t+1)U+(t)+(t−1)U−(t)]dt
 −2alpha(ell+I)J.                                      (1)
The endpoint constant is zero because its quotient images are negatives. The formula is independent of ε. In particular,
s=rho*'(0)=−2(1+Z+alpha ell).                           (2)
The cubic coefficient is [a(Z+alpha ell)−3alpha−3]/3, an additional check.

## 4. Entire-series domination

In the omitted lifts, v_p(ell)=1 and Z,alpha are integral, with Z≡4 mod7 or Z≡5 mod11. Thus s≡4 mod7 or s≡10 mod11, respectively.

The second scalar is odd in old x: x↦−x sends (u,v) to (1/u,−v/u³), which negates rho*. Write
rho*=s x+Σ_(n≥3 odd)d_n x^n.
Every coefficient satisfies
v_p(d_n)≥−2 floor(log_p n).
Indeed all numerator series in (1) are integral; each integral introduces a denominator at most n, and at most two integrations or products of single integrals occur. All constants are integral. For p≥7 and n≥3,
n−1−2 floor(log_p n)≥2,
with the bound tending to infinity. Therefore the entire convergent series satisfies
rho*(x)/x∈s+p²Z_p for every nonzero x∈pZ_p.              (3)
It cannot vanish, and v_p(rho*(x))=v_p(x).

Old reciprocity (x,y)↦(1/x,y/x³) sends (u,v)↦(−u,−v). The second scalar is INVARIANT under this old reciprocity, transferring (3) to both infinity disks. The four endpoint disks exhaust the reduction in these classes. Thus the second scalar alone has exactly four zeros.

## 5. Targets and actual depth-two containment

For a≡3 mod8, the published exact local-target theorem gives second target {0} if for each odd q dividing a+1 either v_q(a+1)=1, or v_q(a+1) is odd and (2/q)=−1. Squarefree odd part of a+1 is a simpler sufficient condition. The first actual target is also {0} under a≡3 mod8.

For the new second-model argument, the rational basepoint is (u,v)=(−1,−4). It has nonzero v and is away from u=0,infinity. Thus PROOF.md Theorem18 applies directly under rank one: no endpoint-basepoint continuation is needed for this second-height upper inclusion. The quotient curves are good at the primes in question, and the isogeny gives rank one for E'. Rational endpoints give the reverse inclusion.

Outside the omitted lifts, the earlier first scalar already isolates the four endpoints. Inside, the second scalar does so. This proves the full uniform p7/p11 conclusion in Section1, retaining all rank, congruence and actual-target assumptions.

## 6. Rank-certified twelve-versus-four example

Let r=467941, q=8r−1=3743527, a=3−32r=−14974109, p=7.
Complete trial division proves both primes, with square-root bounds684 and1934. They satisfy r≡5 mod8, a≡3 mod8, a≡242 mod343 and a+1=−4q. The existing elementary prime-pattern theorem proves rank E_a(Q)=1; the actual local targets are both {0}.

Exact arithmetic gives, modulo7,
ell/7=6, Z=4, λ(P)/49=3, alpha=3, b=4, s=4,
and κ≡294=6·49 mod343.
Hence v7(κ)=2 and −κ/49≡1 is square. The established scalar classification gives twelve first-height zeros. At the additional finite zeros x/7≡±3 mod7, while (3) gives rho*(x)/7≡±2 mod7. All four finite extras fail the zero actual target; reciprocity excludes the four infinity extras.

Consequently C_{−14974109}(Q_7)₂=C_{−14974109}(Q) is exactly the four rational endpoints, despite twelve first-scalar zeros. In this rank-certified example the excluded eight extras are therefore nonrational.

The checker determines κ modulo p³ with the exact tripling parameter, ell through t³, ζ−1/t through t, B through t⁴ and the convergent logarithm. The omitted ell, primitive and height terms have valuations at least5,3,6; after division by ell², κ remains determined modulo p³. An independent formal recursion through degree20 reproduces all residues.

## 7. Useful necessary tests for nonzero targets

If the first scalar has twelve zeros and v_p(κ)=2n, each extra point has local endpoint coordinate of valuation n; its second scalar also has valuation n by (3). Thus all eight are excluded if the second target has no nonzero element of that valuation.

More precisely, for an extra point to realize a target w it is necessary that
b w²/(−s²κ)∈1+p²Z_p.
This follows from x²/(−κ/b)∈1+p²Z_p and rho*/(s x)∈1+p²Z_p. Failure of this finite residue test excludes that target. Neither test asserts sufficiency for full depth-two membership.
