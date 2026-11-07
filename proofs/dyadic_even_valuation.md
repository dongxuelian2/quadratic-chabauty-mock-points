# Dyadic residual vanishing for even v₂(a−3)≥4

Status: independently reviewed mathematical result. This extends the existing odd-valuation theorem; its common Q₈-to-cohomology argument is recalled below.

## 1. The local elliptic lemma

Let B∈Z₂× and c∈4Z₂, and consider

    E: y²=x³+cx²−Bx.

For every odd coefficient prime p, wild inertia acts absolutely irreducibly on V_pE, and

    H¹(Q₂,Sym²V_pE)=0.

The invariants are

    c₄=16(c²+3B),   Δ=16B²(c²+4B).

Thus v₂(c₄)=4, v₂(Δ)=6, and v₂(j)=6. The elliptic curve has potentially good reduction.

Its third division polynomial is

    ψ_c(x)=3x⁴+4cx³−6Bx²−B².                 (1)

We prove that its splitting field over K₀=Q₂^nr is biquadratic and that ψ_c is irreducible over K₀. The field K₀ is henselian, has value group Z and algebraically closed residue field F₂bar.

## 2. A biquadratic splitting field for c=0

Choose a primitive cube root ζ∈K₀ and put s=1+2ζ. Then s²=−3. Choose u,v in an algebraic closure with

    u²=−Bζ²/s,   v²=Bζ/s,
    t=uv,        α=u+v.                     (2)

One has

    u²+v²=B,   3t²=B²,   α²=B+2t.

We first verify that L=K₀(u,v) has degree four over K₀.

If an odd rational 2-adic unit D satisfies D≡1 modulo 4, it is a square in K₀. Indeed, solve

    X²−X+(1−D)/4=0

by Hensel's lemma: the residue field is algebraically closed and the derivative is odd. Then (2X−1)²=D. Consequently the squareclass of every B∈Z₂× in K₀ is either [1] or [−1].

Neither −1, s nor −s is a square in K₀. Each has residue 1, but its difference from 1 has valuation exactly one. If a unit square w² has residue 1, then w has residue 1, so w=1+2z and w²−1=4(z+z²), which has valuation at least two. For −s use −s−1=−2(1+ζ)=2ζ².

The unit ζ itself is a square, since (ζ²)²=ζ. Hence [v²]=[B/s] is either [s] or [−s], and is nontrivial. Moreover

    [u²]/[v²]=[−ζ]=[−1]

is nontrivial, and [u²] is the other of [s],[−s]. Thus [u²] and [v²] are independent squareclasses. This proves [L:K₀]=4, with Galois group V₄.

The four conjugates of α are

    u+v,  u−v,  −u+v,  −u−v,

and their product polynomial is

    x⁴−2Bx²−B²/3 = ψ₀(x)/3.

All four are units. More explicitly, in the residue field bar(u)=bar(ζ), bar(v)=bar(ζ)², and hence bar(u±v)=1. The differences between any two distinct roots are twice one of the units u, v, u+v or u−v. Every such difference therefore has valuation exactly one.

## 3. Hensel deformation to every c∈4Z₂

Using α²=B+2t and 3t²=B², exact expansion gives

    ψ_c(α+2z)/16
      =3z⁴+(6α+2c)z³
        +(3B+9t+3cα)z²
        +(3αt+3cα²/2)z+cα³/4.               (3)

All coefficients are integral in L. Since bar(B)=bar(α)=bar(t)=1 and c∈4Z₂, its reduction is

    z⁴+z+bar(c/4).                           (4)

This polynomial has derivative 1. Its four distinct roots in F₂bar therefore lift to four roots z∈L of (3), by Hensel's lemma. Consequently ψ_c splits in L.

For any root x=α+2z and any nonidentity σ∈Gal(L/K₀), the unperturbed root difference satisfies

    v₂(σα−α)=1.

The automorphism σ acts trivially on the residue field, because that field is already algebraically closed over the residue field of K₀. Therefore v₂(σz−z)>0 and

    v₂(2σz−2z)>1.

The two contributions to σx−x have different valuations and cannot cancel. Thus σx≠x for every nonidentity σ. Each root of ψ_c has orbit four, so ψ_c is irreducible over K₀ and its splitting field is exactly L.

This step does not assume that the Hensel lifts themselves are invariant. Their residues are invariant, which is precisely the strict valuation bound required.

## 4. Wild inertia and cohomology

Inertia at 2 fixes μ₃, so its image on E[3] lies in SL₂(F₃). Its projective action on the four 3-torsion lines is the Galois group V₄ just computed. The inverse image of V₄ in SL₂(F₃) is Q₈. A subgroup surjecting onto V₄ cannot have order four because SL₂(F₃) has only one involution; it must be Q₈. Since the tame inertia quotient has odd-order finite quotients, the wild inertia image on E[3] is also Q₈.

Potential good reduction gives a common finite wild inertia action through origin-preserving automorphisms of a geometric good elliptic special fiber. This action is faithfully realized on every odd-p Tate module: a nontrivial elliptic automorphism cannot act trivially on all p-power torsion. Its finite 2-group image acts faithfully already on E[3], because the congruence kernel inside GL₂(Z₃) is pro-3. Thus the common wild image is Q₈.

A faithful two-dimensional characteristic-zero representation of Q₈ is absolutely irreducible: a reducible representation would split into two characters and have abelian image. Hence ad⁰(V_pE) has no wild-inertia invariants. The determinant character is unramified at 2, so the same holds for

    R=Sym²V_pE≅ad⁰(V_pE)⊗Q_p(1).

Let P₂ be wild inertia and N the kernel of its finite action on R. Then H¹(N,R)=Hom_cont(N,R)=0 because N is pro-2, while any compact subgroup of the additive p-adic vector space is pro-p. Finite-group averaging gives H¹(P₂/N,R)=0. Two applications of inflation-restriction, using R^{P₂}=0, give H¹(Q₂,R)=0.

This includes p=3 and does not require an assumption about ordinary reduction or a genus-two stable model.

## 5. Normalization of the reciprocal family

For E_a:Y²=X³+A X²−A X write A=2^nB, B odd.

- If n=4k≥4, scale X=2^{2k}x and Y=2^{3k}y. The equation becomes y²=x³+2^{2k}B x²−Bx, with c∈4Z₂.
- If n=4k+2≥6, first twist by 2, giving Y²=X³+2A X²−4A X, then scale X=2^{2k+2}x and Y=2^{3k+3}y. The equation becomes y²=x³+2^{2k+1}B x²−Bx, again with c∈4Z₂. A quadratic twist does not change Sym²V.

Therefore every even n≥4 satisfies the claimed residual cohomology vanishing. Combining with the prior odd-n theorem gives

    H¹(Q₂,Sym²V_pE_a)=0

for every n=v₂(a−3)≥4 and every odd p. For integral a this is precisely the congruence subfamily a≡3 modulo 16, excluding a=3. With the independently established two Tate coordinates and their dyadic vanishing, the full actual joint image is Ξ₂={(0,0)} throughout this subfamily.

The case n=3 is not covered by either lemma and remains unclaimed.

## 6. Audit and sources

The independent audit verified all squareclass cases, all six root-difference valuations, the exact expansion (3), reduction (4), the no-stabilizer argument, and both scaling/twist cases. The exact expansion was independently checked with SymPy modulo α²=B+2t and 3t²=B².

For standard background and the fully spelled-out common-special-fiber argument, see the companion [odd-valuation proof](dyadic_residual_vanishing.md). In particular: Silverman, *The Arithmetic of Elliptic Curves*, VII.5.5 (potential good reduction), VII.4.1 and VII.7.1/7.3 (torsion and finite inertia); and elementary inflation-restriction as explicitly used above. No specialized dyadic reduction classification is invoked.
