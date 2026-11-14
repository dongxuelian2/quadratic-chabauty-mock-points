# Vanishing of the dyadic residual cohomology for odd v₂(a−3)≥5

Status: independently reviewed mathematical result. This proves the dyadic residual and joint-image conclusion through elliptic wild inertia, without importing the odd-prime stable-chart formulas into residue characteristic 2.

## 1. Main conclusion

Let a be an integer with a≡3 modulo 8, a≠3, and put

    n=v₂(a−3).

Suppose n is odd and n≥5. For every odd coefficient prime p, set

    E_a: Y²=X³+(a−3)X²−(a−3)X,
    V=V_p(E_a),    R=Sym² V.

Then

    H¹(Q₂,R)=0.                                      (1)

In particular its actual residual local image Δ₂ is {0}. Combining this with the established independence of the two Tate height coordinates and the established identities w₂=w₂*=0 for integral a≡3 modulo 8 gives

    Ξ₂={(0,0)}.                                      (2)

Neither rank one nor non-CM is needed for the local vanishing. Those hypotheses are retained when (1)–(2) are used in the global non-CM residual-gluing theorem.

This covers a=−605, −1373, −157469, all of which have n=5. It also covers every odd n≥5, not only n=5. Nothing here asserts (1) for n=3 or for even n.

## 2. A local elliptic lemma

**Lemma.** Let B∈Z₂× and c∈8Z₂, and let

    F_{B,c}: y²=x³+c x²−2B x.

The wild inertia image on every odd-p Tate module V_p(F_{B,c}) is absolutely irreducible. In fact the common wild inertia automorphism group on a potentially good special fiber is quaternion of order eight. Consequently

    End_{G_Q₂}(V_p(F_{B,c}))=Q_p.

We prove all assertions, including the passage from the 3-torsion calculation to arbitrary odd p.

### 2.1. Potentially good reduction

The standard Weierstrass invariants are

    c₄=16(c²+6B),
    Δ=64B²(c²+8B).

Because B is odd and c∈8Z₂,

    v₂(c₄)=5,   v₂(Δ)=9,   v₂(j)=6.

The elliptic potential-good-reduction criterion therefore gives good reduction after a finite extension. This only concerns the elliptic curve; no potential-good claim is made for the genus-two curve.

### 2.2. An exact Newton polygon for the four 3-torsion lines

The third division polynomial is

    ψ₃(x)=3x⁴+4c x³−12B x²−4B².                     (3)

Let K₀ be the maximal unramified extension of Q₂ inside an algebraic closure, and let r²=2B. Then v₂(r)=1/2 and [K₀(r):K₀]=2. The field K₀ is henselian, so the usual Newton-polygon conclusions apply; completing it gives the same valuation argument if desired.

Substitute

    x=r+2B+2B w,
    P(w)=ψ₃(r+2B+2B w)/(16B²).

Using r²=2B, the exact coefficients P=Σ C_j w^j are

    C₄=3B²,
    C₃=12B²+2Bc+6Br,
    C₂=18B²+6Bc+18Br+6B+3cr,
    C₁=12B²+6Bc+18Br+12B+6cr+3c,
    C₀=3B²+2Bc+6Br+6B+3cr+3c−1+(cr)/(2B).          (4)

Every C_j for 0≤j≤3 has valuation EXACTLY 3/2, whereas C₄ is a unit. Here is a coefficientwise check:

- C₃ has r-coefficient 6B of valuation one; its remaining part is divisible by 4.
- C₂ has r-coefficient 18B+3c of valuation one; its remaining part is 6B(3B+1)+6Bc, divisible by 4.
- C₁ has r-coefficient 18B+6c of valuation one; its remaining part is 12B(B+1)+6Bc+3c, divisible by 8.
- C₀ has r-coefficient 6B+3c+c/(2B) of valuation one. Its remaining part is 3B²+6B−1+2Bc+3c, divisible by 4, since B is odd.

The integer-valuation and half-integer-valuation parts cannot cancel. Thus the lower Newton polygon has just the segment from (0,3/2) to (4,0), and every root w has valuation 3/8.

If x is any root of ψ₃, then K₀(r,x)=K₀(r,w) has ramification degree at least four over K₀(r): its value group contains 3/8, whereas K₀(r) has value group (1/2)Z. Therefore

    [K₀(r,x):K₀]≥8.

Adjoining r has degree at most two, while x satisfies the degree-four polynomial (3). The opposite upper bound is eight, and hence

    [K₀(x):K₀]=4.

Thus ψ₃ is irreducible over K₀. Equivalently, inertia acts transitively on the four one-dimensional subspaces of F[3], whose x-coordinates are the four roots of ψ₃.

For the main n=5 specialization c=8B, (4) becomes the particularly simple identity

    P(w)=3B²w⁴+(28B²+6Br)w³
         +(66B²+42Br+6B)w²
         +(60B²+66Br+36B)w
         +19B²+30Br+30B+4r−1.                       (5)

The supplied exact symbolic script verifies (4) and (5). The proof of the Newton polygon is the parity argument above, not a numerical experiment.

### 2.3. The inertia image on F[3]

Inertia at 2 fixes μ₃, so its determinant on F[3] is one. Its image therefore lies in SL₂(F₃), whose projective quotient is PSL₂(F₃)≅A₄ acting on the four lines of F₃².

A transitive subgroup of A₄ has order divisible by four, hence is V₄ or A₄. It therefore contains the normal Klein four subgroup. The inverse image of this Klein four subgroup in SL₂(F₃) is Q₈. The inertia image contains Q₈: a subgroup surjecting onto V₄ cannot have order four, since SL₂(F₃) has only one involution, namely −I, and its subgroups of order four are cyclic.

The quotient of inertia by wild inertia has odd-order finite quotients at residue characteristic 2. Consequently the wild inertia image contains this full 2-Sylow subgroup Q₈. It is exactly Q₈ on F[3].

### 2.4. Why the same conclusion holds for every odd coefficient prime

Choose a finite Galois extension over which F has good reduction. Inertia then acts, fixing the origin, through a finite automorphism group of the geometric good special fiber \bar F. Smooth proper base change identifies its action on every prime-to-2 Tate module with the original inertia action.

The action of Aut(\bar F) on T_p(\bar F) is faithful for every p≠2. Indeed, a nonzero endomorphism of an elliptic curve is an isogeny of finite degree; if α−1 annihilates all p-power torsion, it must be zero. Thus every odd-p Tate module faithfully realizes the same finite inertia automorphism group.

The wild inertia automorphism group is a finite 2-group. Its action on \bar F[3] is faithful: the kernel, viewed inside GL₂(Z₃), lies in the pro-3 group 1+3M₂(Z₃), which contains no nontrivial finite 2-subgroup. Section 2.3 therefore identifies this automorphism group with Q₈.

For any odd p, its faithful two-dimensional characteristic-zero representation is absolutely irreducible. Otherwise, after extending scalars, Maschke's theorem would split it as two one-dimensional characters; its image would then be abelian, contradicting faithfulness to Q₈. Schur's lemma now gives

    End_{wild inertia}(V_p(F))=Q_p,

and hence End_{G_Q₂}(V_p(F))=Q_p. This argument includes p=3. It does not assume that reducing an arbitrary p-adic representation modulo p preserves irreducibility; the only finite-torsion calculation used is the prime-to-2 level-three calculation, transported through the common good special fiber.

## 3. Deduction of H¹(Q₂,Sym²V)=0

For an elliptic Tate module det V=Q_p(1), and

    R=Sym²V≅ad⁰(V)⊗Q_p(1),
    R*(1)≅ad⁰(V).

The p-adic cyclotomic character is unramified at 2 when p is odd. Thus R and ad⁰(V) have the same wild inertia action. The absolute irreducibility proved above implies

    H⁰(Q₂,R)=0,
    H⁰(Q₂,R*(1))=H⁰(Q₂,ad⁰V)=0.

For a p-adic representation over a local field of residue characteristic different from p, the local Euler-characteristic formula and Tate duality give

    dim H¹(Q₂,R)=dim H⁰(Q₂,R)+dim H⁰(Q₂,R*(1)).

Both terms vanish. This proves (1) for the elliptic curves in the lemma, with no appeal to a stable model of C.

There is also a direct proof avoiding local duality. Let P₂ denote wild inertia and N the kernel of its finite action on R. Then N is pro-2, acts trivially on R, and H¹(N,R)=Hom_cont(N,R)=0: the image of a continuous homomorphism would be a compact pro-2 subgroup of the additive p-adic vector space, hence also pro-p, hence trivial. The finite quotient P₂/N has zero positive-degree R-cohomology by averaging. Inflation-restriction therefore gives H¹(P₂,R)=0. Since R^{P₂}=0, applying inflation-restriction once more, now to P₂ normal in G_Q₂, gives H¹(Q₂,R)=0. Thus neither purity nor the Euler-characteristic formula is necessary for the vanishing.

## 4. Application to the reciprocal family

Write A=a−3=2^nB, B odd.

If n=4k+1≥5, so k≥1, the coordinate scaling

    X=2^{2k}x,   Y=2^{3k}y

transforms E_a into

    y²=x³+2^{2k+1}B x²−2B x.

Its x² coefficient belongs to 8Z₂, so the lemma applies.

If n=4k+3≥7, first take the quadratic twist of E_a by 2:

    Y²=X³+2A X²−4A X.

Then scale X=2^{2k+2}x, Y=2^{3k+3}y. The result is

    y²=x³+2^{2k+2}B x²−2B x,

whose x² coefficient again lies in 8Z₂. The Sym² representation is unchanged by a quadratic twist, because the square of the twisting character is trivial. Hence the same local cohomology vanishing holds for the original E_a.

These two cases cover every odd n≥5.

## 5. Actual joint image and examples

Use the two independent Tate center coordinates established by the reciprocal height constructions. At 2 their actual local height functions vanish identically for integral a≡3 modulo 8. The first vanishing follows from the absence of unit-x points and integral/formal cancellation; the second follows on the nonmonic reciprocal model, where every local point has unit u and the paired elliptic heights agree. Independence of these two coordinates identifies the actual Tate local image with {0}.

Since H¹(Q₂,R)=0, the residual coordinate is also zero for every point. Thus the SAME-POINT joint image is exactly Ξ₂={(0,0)}, proving (2).

Combined with the exact odd-prime residual images already established:

- a=−605: a−3=−32·19, and 19≡3 modulo 4. All actual residual local images, including the dyadic one, are zero.
- a=−1373: a−3=−32·43, and 43≡3 modulo 4. Again all actual residual local images are zero.
- a=−157469: a−3=−32·7·19·37. The only possibly nonzero actual residual image is the already computed Δ₃₇={0,±e₃₇}, with e₃₇≠0. At 2 the entire residual cohomology group is zero.

The first two conclusions reduce the residual global comparison to δ_p(W)=0, but this note does not evaluate δ_p(W), prove it is nonzero, or assert a new full-depth-two exclusion from that reduction alone. The third leaves precisely the three odd-prime residual choices at 37 in the established global comparison.

## 6. Scope and sources

The following standard sources suffice for the background results. The specialized Newton-polygon, finite-group, faithful-special-fiber, and scaling arguments are supplied explicitly above.

- J. H. Silverman, *The Arithmetic of Elliptic Curves*, second edition, Proposition VII.5.5: integral j is equivalent to potential good reduction. Proposition VII.4.1 and Theorem VII.7.1 give the prime-to-residue-characteristic torsion and Tate-module reduction facts; Corollary VII.7.3 gives the finite-inertia criterion. The common special-fiber action used here is the descent action on the unique good elliptic model after a finite Galois extension, followed by prime-to-2 torsion reduction. [Verified text](https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf), printed pp. 195, 197, 201–202.
- J. S. Milne, *Arithmetic Duality Theorems*, second edition, I.2, Corollary 2.3 and Theorem 2.8: local duality and Euler characteristic, with the p-adic vector-space versions obtained from stable lattices and finite quotients. I.2, Lemma 2.9 explicitly uses the vanishing of positive-degree cohomology of wild inertia on prime-to-residue-characteristic finite modules. [Author's text](https://www.jmilne.org/math/Books/ADTnot.pdf), printed pp. 28, 31–32. The final paragraph of Section 3 gives the direct wild-inertia proof instead.

This is not a dyadic stable-reduction classification of the genus-two curve. It avoids that harder problem by proving the full local residual cohomology is zero in the stated subfamily. The cases n=3 and even n remain outside the theorem. No odd-prime cluster or neck formula is used at 2.
