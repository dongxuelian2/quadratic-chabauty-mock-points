# Exact scalar classification in all four-residue-disk cases

Retain the normalization of uniform_endpoint_families.md:
C_a:y²=x⁶+a x⁴+a x²+1, E_a:Y²=X³+(a−3)X²−(a−3)X,
P=(1,1), ell=L(P), h=λ(P), Z=ζ(P), alpha=h/ell², dζ=−(X−2)ω.
The first scalar height is rho=λ(f1)−λ(f2)−2log_p(x)−alpha L(f1)²+alpha L(f2)².

## Theorem

Let a be odd. For (p,a mod p)=(7,4) or (11,2), put
κ=1−Z+alpha(1−ell).
The scalar height has exactly twelve distinct zeros in C_a(Q_p) if
0≠κ∈p²Z_p and −κ is a square in Q_p.
In every other case it has exactly four zeros, the rational endpoints.

Equivalently the twelve-zero criterion is that v_p(κ) is even and at least two, with −κ/p^v_p(κ) a quadratic residue modulo p. Its eight additional zeros consist of two noncentral points in each of the four endpoint disks. They are nonendpoint, not asserted nonrational. If κ=0, each endpoint has multiplicity four and there are no additional zeros. Otherwise each endpoint has multiplicity two, and every additional zero is simple.

The twelve-zero alternative requires a≡242 mod343 at 7 or a≡508 mod1331 at 11. These congruences alone are not sufficient.

Together with the previous prime-19 theorem, this classifies the first scalar zero set in every odd-good-prime case of this family whose reduction has exactly four rational points. Those cases are precisely (7,4),(11,2),(19,0). This is not a classification for all primes and residue-disk counts, or for the full depth-two set.

## 1. Reduction to omitted lifts

Outside a≡46 mod49 at 7 and a≡24 mod121 at 11, the existing uniform theorem gives four zeros, v_p(ell)=s≥1, v_p(h)=1, integral Z and v_p(alpha)=1−2s<0. Then v_p(κ)=1−2s<0 since 1−ell is a unit, so the new criterion correctly fails.

In the omitted lifts v_p(ell)=1, h∈p²Z_p and Z,alpha∈Z_p. These statements allow h=0. Write a=46+49j at 7 or a=24+121j at 11.

## 2. Exact endpoint series, including both signs

Put z=x² and
q(z)=(1+az+az²+z³)^(-1/2)=Σ q_n z^n∈Z_p[[z]].
For y=ε/q(x²), ε=±1, define
V(z)=integral_0^z q(u)du,
W(z)=(1/2)integral_0^z(1−u)q(u)du,
K(z)=Σ q_n z^n/(2n+1),
R(z)=Σ(q_(n+1)−q_n)z^n/(2n+1).
The exact pullback identities give
L(f1)=ε(ell+V/2), L(f2)=−εxK,
ζ(f1)=ε(Z+W), ζ(f2)=ε(−1/x+xR).
For the last identity, differentiation gives f2*(dζ)=(x^(-2)−1)dx/y; the integration constant is zero since ζ and t2=−x(1+x²)/y are odd in x.

Let T(0)=0 and T'(z)=(q−1)/z−(Z+W+R)q. Then
rho=T(z)+alpha[zK(z)²−ell V(z)−V(z)²/4].                 (1)
Indeed d(λ(f1)−h)/dz=−(Z+W)q. For S=−λ(f2)−2log_p x, one has S'=(q−1)/z−Rq and S(0)=0, since log_p(±1)=0 and the regular formal height vanishes at the origin. The constant h cancels alpha ell². Thus (1) is independent of ε.

Write rho=Σ_(n≥1)c_n z^n and F(z)=rho/z. Direct coefficient calculation gives
F(z)=κ+bz+Σ_(n≥3)c_n z^(n−1),
b=(aZ−1−2a)/4+alpha(a ell/4−1/4−a/3).                 (2)
For verification, q1=−a/2, q2=3a²/8−a/2, R0=q1−1, R1=(q2−q1)/3 and W1=1/2. These yield
c1=q1−Z−R0+alpha(1−ell),
c2=(q2−Zq1−1/2−R1−R0q1)/2+alpha(2q1/3−ell q1/2−1/4),
which simplify to κ and b.

## 3. All-orders bound and contraction

In the integral case under consideration, every coefficient satisfies
v_p(c_n)≥−2 floor(log_p(2n)).                            (3)
Each coefficient of V,W,K,R has at most one integration denominator of size at most 2n when contributing to z^n. Multiplication or the further integration in T introduces at most one more such denominator. The numerator coefficients and alpha,ell,Z are integral, while 2 and4 are units. Thus (3) holds term by term and is preserved by sums.

For p≥7 and n≥3,
2(n−2)−2 floor(log_p(2n))≥2,
since 2n<7^(n−2); the lower bound tends to infinity. Consequently
[F(p²w)−κ]/p²=bw+p²w²H(w), H∈Z_p⟨w⟩.                (4)
This controls the entire convergent tail on z∈p²Z_p.

If b is a unit, w↦w+p²b^(-1)w²H(w) is an isometric bijection of Z_p: for every prescribed c, the map w↦c−p²b^(-1)w²H(w) is a contraction. Integral restricted power series are 1-Lipschitz. Hence F has no zero in p²Z_p if κ∉p²Z_p, and exactly one zero z0 there if κ∈p²Z_p. If κ=0 this is z0=0. Otherwise
z0/(−κ/b)∈1+p²Z_p.                                    (5)
When b is a square unit, z0 is a nonzero square precisely when −κ is a square. This gives two additional x-values on each finite disk. Formula (4) shows F'(z0) is a unit, making the extra x-roots simple. If κ=0, rho=b x⁴+O(x⁶), so the endpoint multiplicity is four.

## 4. Critical congruences

For p=7 use m=3 and
ψ=a(4−a), U=(3a⁴−20a³+40a²−64)/(a²−8), t=ψ/U,
Zpr=−a(3a−8)/(3(a²−8)).
For p=11 use m=4 and
ψ=−4(a−2)(a²−2a−4),
D=a⁴−8a³+24a²−16a−32,
N=a⁸−8a⁷−8a⁶+224a⁵−672a⁴+640a³−512a+1024,
U=−N/D, t=ψ/U, Zpr=−(a³−2a²−8)/D.
The multiplication identities are
ell=L(t)/m, h=(2/m²)(log_p U−B(t)), Z=Zpr+(ζ(t)−1/t)/m.

For v_p(t)=1 the needed evaluated expansions are
L(t)=t+(a−3)t³/3+O(p⁵),
ζ(t)=1/t+2t+(a−3)t³+O(p⁵),
B(t)=(a−1)t²/2+[(a−3)²+(a−3)]t⁴/4+O(p⁶).
The integral formal differential and single-/double-integration bounds in the preceding uniform proof justify every remainder at p=7,11.

For a=46+49j or a=24+121j, exact reduction modulo p gives:
- p=7: ell/p=6, Z=4, h/p²=j+6, alpha=j+6, κ=j+3.
- p=11: ell/p=6, Z=5, h/p²=4j+7, alpha=5j+6, κ=5j+2.

To check these rows, compute e=U^(p−1)−1 modulo p³. In the omitted lifts e∈p²Z_p, so log_p U≡e/(p−1) mod p³. The rational denominators remain units, and the displayed quantities depend only on a modulo p³. Exhausting all j modulo p proves the rows for the whole lifts, not merely sample parameters.

Thus κ can lie in pZ_p only when j≡4 mod p. Substitution in (2) gives b≡4 mod p in both cases, a square unit. If κ is a unit, (4) already excludes a root without requiring b to be a unit. If v_p(κ)=1, (4) again excludes roots. If κ∈p²Z_p, apply (5).

The four residue disks exhaust the curve. Reciprocal antisymmetry rho(1/x,y/x³)=−rho(x,y) transfers the same count to both infinity disks, proving the theorem.

## 5. Exact twelve-zero examples

At p=11, a=12487, exact computation gives
ell/11≡6, Z≡5, alpha≡4, b≡4 modulo11,
v11(h)=2, κ≡726=6·121 mod1331.
Thus −κ/121≡5 is a square modulo11, and there are exactly twelve scalar zeros. The additional finite-disk roots satisfy x/11≡±2 mod11; at infinity, (1/x)/11≡±2 mod11.

For rigorously sufficient precision, compute ell modulo p⁴ from (t+(a−3)t³/3)/4, Z modulo p³ from Zpr+2t/4, and h modulo p⁵ from
(2/16)[(e−e²/2)/10−(a−1)t²/2−((a−3)²+(a−3))t⁴/4],
where e=U^10−1 modulo p⁵. Here e has valuation at least two. Omitted logarithm and B terms have valuation at least six. Omitted ell and Z terms have valuations at least five and three. Since ell has valuation one and h at least two, division by ell² still determines alpha and κ modulo p³. Independent formal-coefficient generation through degree sixteen gives the same result.

Direct computation also verifies a=656691≡3 mod8 at p=11 with the same κ residue, and a=17735 at p=7 with κ≡294=6·49 mod343, where −κ/49≡1. These are scalar examples only: no rank-one certificate, nonrationality claim, or full depth-two membership is asserted for them.

## 6. Exhaustive scope and full-depth-two consequence

For good odd p, J(C_a) is isogenous to E_a² over F_p. Thus #C_a(F_p)=p+1−2t_p(E_a). Count four and Hasse imply p≤11+4sqrt(7)<23. For p≡1 mod4 the two extra rational Weierstrass points (±sqrt(−1),0) preclude count four. Enumerating all good residues for p=3,7,11,19 leaves exactly (7,4),(11,2),(19,0). The preceding prime-19 theorem always gives four scalar zeros.

If also a≡3 mod8 and rank E_a(Q)=1, a four-zero scalar case gives C_a(Q_p)₂=C_a(Q) equal to the four endpoints, using the established Mordell–Weil-abelian-image, actual-local-image containment and rational reverse inclusion. A twelve-zero scalar case gives only an upper bound of twelve for that restricted depth-two set under the same arithmetic hypotheses. Passing this one scalar equation does not prove full depth-two membership.
