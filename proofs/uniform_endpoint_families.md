# Uniform endpoint-only families at 7, 11 and 19

This consolidates the complete prime-19 proof and the independently reviewed broadenings at 7 and 11. It makes the branch sign explicit in the common endpoint argument. The exact checker is ../scripts/check_endpoint_families.py. The scope is the Mordell–Weil-abelian-image, actual-local-image depth-two convention already specified in PROOF.md, not an unrestricted Bloch–Kato identification.

## 1. Statements

Let a be an odd integer and
C_a: y²=x⁶+a x⁴+a x²+1,
E_a: Y²=X³+AX²−AX, A=a−3, P=(1,1).
Use ω=dX/(2Y), the integral complement (X−2)ω, the compatible odd primitive ζ with dζ=−(X−2)ω, and the normalized height λ. Set ell=L(P), h=λ(P), Z=ζ(P), alpha=h/ell². Nonvanishing of ell is proved below for every asserted parameter.

Let f1=(1+x²,y), f2=(1+x⁻²,y/x³), and
rho=λ(f1)−λ(f2)−2log_p(x)−alpha L(f1)²+alpha L(f2)²,
with continuous endpoint extensions.

**Uniform scalar theorem.** The zero set of rho in C_a(Q_p) consists exactly of (0,±1) and the two infinity points in each of the following cases:
- p=7, a≡4 mod7 and a not≡46 mod49.
- p=11, a≡2 mod11 and a not≡24 mod121.
- p=19, a≡0 mod19.

The omitted lifts at 7 and 11 are unresolved by this leading-digit argument; no failure of equality is asserted there.

**Full restricted depth-two consequence.** In any of these cases, if a≡3 mod8 and rank E_a(Q)=1, then C_a(Q_p)₂=C_a(Q) consists of the same four endpoints. These are sufficient conditions. No infinitude of rank-one parameters or general classification is claimed.

Rank-certified examples include a=−605 at 7 (previously established), a=−18269 at 11, and a=−17309, −3474245 at 19. Section 6 supplies their arithmetic certificates.

## 2. Uniform formal estimates

All the models above have good reduction: (a+1)(a−3) is a unit. Put t=−X/Y and u=1/X. The equation
u=t²(1+Au−Au²)
gives u=t²v(t), v∈1+t² Z_p[[t²]]. Consequently ω/dt=tu'/(2u) is an integral even series with constant 1; −(X−2)ω/dt has leading term −t⁻² and integral even regular coefficients.

Single integration gives coefficient bounds −v_p(n) for the odd degree n terms of L and ζ−1/t. The compatible height is
λ(t)=−2log_p(t)−2B(t),
where B'=ζ(ω/dt)−1/t. For every even n≥2,
v_p([t^n]B)≥−v_p(n)−floor(log_p(n−1)).
For p≥7 and n≥4 the sum of these losses is at most n−2. For n=2 it is zero. Similarly n s−v_p(n)≥3s for odd n≥3 and s≥1. Thus, for v_p(t)=s≥1,
L(t)−t∈p^(3s) Z_p, ζ(t)−1/t∈p^s Z_p, B(t)∈p^(2s) Z_p.
All lower bounds tend to infinity, so these are estimates for entire convergent series, not just truncations.

The same reasoning controls single and nested integrations of integral endpoint differentials. In a twice integrated even degree n≥4 term the denominator loss is at most v_p(n)+floor(log_p(n−2)); after evaluating on x∈pZ_p and dividing by x² this is integral. This statement concerns evaluated series; it does not claim integral coefficients for B or all primitives.

## 3. A common endpoint domination lemma

Suppose ell∈pZ_p is nonzero, Z∈Z_p and v_p(alpha)<0. On the branch
y=ε sqrt(1+a x²+a x⁴+x⁶), ε=±1, x∈pZ_p,
write
I=integral from 0 to x of t/y(t) dt, J=integral from 0 to x of dt/y(t).
Then
L(f1)=εell+I, L(f2)=−J,
I/x²∈Z_p, J/x∈ε+pZ_p, I²/x²∈p²Z_p.

The pullbacks are f1*ω=x dx/y, d(ζ∘f1)=(1−x²)x dx/y and d(λ∘f1)=−2(ζ∘f1)x dx/y. Since ζ(f1(0))=εZ is integral, the estimates in Section 2 give
(λ(f1)−h)/x²∈Z_p.
For t2=−x(1+x²)/y, regularization gives
S=−λ(f2)−2log_p x=2log_p((1+x²)/y)+2B(t2).
Here log_p(−1)=0; (1+x²)/y is ε times 1+O(x²), and t2/x is an integral unit. Thus S/x²∈Z_p. Set H=((λ(f1)−h)+S)/x².

The exact identity, with both branch signs explicit, is
rho/(alpha x²)=H/alpha+(J/x)²−2εell(I/x²)−I²/x².
It belongs to 1+pZ_p for x≠0. Thus rho has no noncentral zero on either finite endpoint disk; its central value is zero since h=alpha ell². Reciprocal antisymmetry gives the same result at infinity.

The unfactored cross term alpha ell need not be integral. Factoring alpha is essential when its valuation is smaller than −1; the only required smallness is ell∈pZ_p.

## 4. Tripling and the families at 7 and 19

Put ψ=a(4−a), N=a²−8, Q=3a⁴−20a³+40a²−64.
Exact addition gives
2P=((a−2)²/4,−(a−2)(a²−2a−4)/8),
3P=(N²/ψ²,−NQ/ψ³),
t3=ψN/Q, U=ψ/t3=Q/N.
These are rational identities; the checker verifies their polynomial cross-multiplications. Also ψ3(P)=ψ and Dψ3(P)=24 for D=d/ω. Multiplication gives
ell=L(t3)/3,
h=(2/9)(log_p U−B(t3)),
Z=ζ(t3)/3−8/(3ψ).
The apparent poles cancel exactly:
Zprincipal=1/(3t3)−8/(3ψ)=−a(3a−8)/(3(a²−8)).

At p=7, a≡4 mod7, N and Q are units and s=v7(a−4)≥1. Oddness excludes a=4. Hence v7(ell)=s and Z is integral. Since U(4)=8 and U'(4)=8, writing a=4+7k mod49 gives
U≡8+56k mod49, (U⁶−1)/7≡6(1+k) mod7.
All remaining logarithm terms and B(t3) are in49 Z7. Therefore v7(h)=1 unless k≡6 mod7, namely the omitted class a≡46 mod49. On the asserted locus v7(alpha)=1−2s<0.

At p=19, let s=v19(a)≥1, finite because a is odd. N and Q are units, v19(t3)=s, t3/a≡1/2 mod19 and ell/a≡1/6 mod19. The exact identity
U−8=a²(3a−8)(a−4)/(a²−8)
implies U≡8 mod361 for the whole progression, even when s is arbitrarily large. Since 8^18≡172=1+9·19 mod361,
log_19(U)/19≡10 mod19, h/19≡17 mod19.
All omitted logarithm terms and B(t3) have valuation at least two. The principal-part formula and the formal tail show Z∈19^s Z19. Hence v19(ell)=s, v19(h)=1, and v19(alpha)=1−2s<0 uniformly.

Both families satisfy the common lemma.

## 5. Quadrupling and the family at 11

Let
D=a⁴−8a³+24a²−16a−32,
N4=a⁸−8a⁷−8a⁶+224a⁵−672a⁴+640a³−512a+1024.
Exact doubling twice gives
ψ4=−4(a−2)(a²−2a−4), U=ψ4/t4=−N4/D,
Zprincipal=1/(4t4)−Dlog(ψ4)/16=−(a³−2a²−8)/D,
where t4=−X(4P)/Y(4P).
The checker verifies these rational identities symbolically, including the derivative quotient. The multiplication identities are
ell=L(t4)/4,
h=(2/16)(log_11 U−B(t4)),
Z=ζ(t4)/4−Dlog(ψ4)/16.

For a≡2 mod11, D and N4 are units, s=v11(a−2)≥1 and v11(t4)=s. Oddness excludes a=2. Thus v11(ell)=s and Z is integral. Since U(2)=16 and U'(2)=−16, writing a=2+11k mod121 gives
U≡16−176k mod121, (U^10−1)/11≡9+k mod11.
The higher logarithm terms and B(t4) are in121 Z11. Therefore h has valuation one except at k≡2 mod11, namely the omitted a≡24 mod121. On the asserted locus v11(alpha)=1−2s<0, and Section 3 applies.

For the rank-certified a=−18269 one has s=2 and exact constants
t4=−2718621001809760145725766425220/12413902554450543099975932989931009,
ψ4=24394919938180,
Zprincipal=6098062471839/111442095678080129.
They give ell/121≡9, h/11≡3, Z≡5 and 1331alpha≡9 mod11. This illustrates why allowing alpha valuation −3 matters; the family does not require s=2.

## 6. Disk exhaustion, arithmetic and full depth two

Direct exhaustive finite-field counts give only affine (0,±1), plus the two infinity points, in each residue case (p,a)=(7,4),(11,2),(19,0). At 19 one can see this directly: the nonzero sixth powers are 1,7,11, and their translates 2,8,12 are nonsquares. Smoothness makes these four disks exhaustive. Section 3 therefore proves each scalar theorem.

For odd a≡3 mod8 the first actual away-from-p target is {0}, without multiplicity restrictions on a+1; see reciprocal_local_targets.md. Under rank one the established endpoint_basepoint_bridge.md and monic actual-target containment put the full restricted depth-two set inside this scalar set. Rational endpoints supply the reverse inclusion. This is a containment argument followed by rational-point inclusion, not a claim that passing scalar tests is sufficient in general.

The rank theorem in checkable_rank_patterns.md applies when A=−32r, r and 8r−1 are prime and r≡3 or5 mod8. It gives:
- p=7: r=19, q=151, a=−605.
- p=11: r=571, q=4567, a=−18269.
- p=19: r=541, q=4327, a=−17309.

The quadratic rank pattern applies to n=659, D=2n²−1=868561, both prime with n≡3 mod8; a=3−8n²=−3474245 supplies a second p=19 example. All four parameters are 3 mod8. The checker proves the listed primalities by complete trial division.

For p=19 the combined congruence is a≡19 mod152, conditional on rank one. Explicit sufficient arithmetic subfamilies are the existing linear rank pattern with r≡9 mod19, or the existing quadratic rank pattern with n≡±6 mod19. The latter still requires all hypotheses of that rank theorem, including oddness of n; the congruence alone does not prove rank.

No assertion of infinitely many prime-pattern parameters, unrestricted Selmer identification, or general non-Weierstrass classification follows.
