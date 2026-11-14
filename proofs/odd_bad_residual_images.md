# Exact residual images at odd primes dividing a−3

This supplements [the non-CM residual-gluing theorem](noncm_residual_gluing.md). The local calculation does not require rank one or non-CM; those hypotheses are used only when applying the global criterion.

## 1. Notation and exact statement

Let a be rational, a≠−1,3, and let q be an odd prime with

    n = v_q(a−3) > 0.

Let p≠q be the coefficient prime. Put A=a−3 and

    C: y²=(x²+1)[(x²+1)²+A x²],
    E: Y²=X³+A X²−A X,
    f₁=(1+x²,y),  f₂=(1+x⁻²,y/x³).

Use basepoint b=(0,1). Write H=V_p(E)⊕V_p(E) for the abelian quotient, and write the depth-two center as

    Z(U₂)=T⊕R,  T≅Q_p(1)²,  R=Sym² V_p(E),

using the two elliptic factors. Let U_T=U₂/R and U_R=U₂/T. At q≠p, H⁰(Q_q,H)=H¹(Q_q,H)=0, so the central maps identify H¹(Q_q,U_T) with H¹(Q_q,T), and H¹(Q_q,U_R) with H¹(Q_q,R). Denote the two coordinates of the local Kummer map by t_q(z), r_q(z). In the canonical reference convention of the residual-gluing theorem, γ_q=0, so r_q is also its residual coordinate. A different reference requires the corresponding translation.

Define the actual residual image and SAME-POINT joint image by

    Δ_q={r_q(z):z∈C(Q_q)},
    Ξ_q={(t_q(z),r_q(z)):z∈C(Q_q)}.

**Theorem.**

1. If q≡3 modulo 4, then Δ_q={0} and Ξ_q={(0,0)}.
2. If q≡1 modulo 4, choose i∈Q_q with i²=−1 and put

       e_q = r_q((i,0)).

   Then e_q is NONZERO and

       Δ_q = {0, ±e_q} ∪ { ±(4k/n)e_q : k∈Z, 1≤k<n/4 },
       Ξ_q = { (0,δ) : δ∈Δ_q }.

Changing i to −i negates e_q and leaves these sets unchanged. This is an exact finite image, including attainability of every listed value, not just a containing line. The endpoint normalization by e_q removes any convention-dependent common sign or nonzero scaling in the comparison between monodromy and local cohomology.

For example, n=1,2,3,4 all give {0,±e_q}; n=5 gives {0,±(4/5)e_q,±e_q}; n=8 gives {0,±(1/2)e_q,±e_q}.

## 2. Stable reduction, including the node lengths

Work over a finite extension L/Q_q containing i and π with π⁴=A. Keep valuations normalized by v(q)=1; thus v(π)=n/4. Since q is odd, the extension needed for these coordinates is tame, even when q=3.

The six branch points form two clusters of three, around x=i and x=−i. Each cluster has depth n/2. One way to see the exact depth is to write s=x²+1. The two other roots near each root of s=0 solve s²+A x²=0; the derivative of x↦x²+1 at ±i is a unit. Their s-valuations are n/2, and their pairwise differences also have valuation n/2 because 2 is a unit. Thus each cluster has three distinct first-order normalized roots.

There are explicit elliptic charts:

    Z=(x²+1)/π²,   W=y/π³.

Substitution gives the EXACT equation

    W²=Z³−Z+π² Z²,       x²=−1+π² Z.                 (1)

Modulo the maximal ideal, the second equation splits into x=i and x=−i. Each resulting component is the smooth elliptic curve

    E₀: W²=Z³−Z.

It is smooth in every odd residue characteristic, including 3.

The central chart has the coordinate z=y/(x²+1). Its reduced normalization is the rational curve

    z²=x²+1.

Its two attaching points are (x,z)=(i,0),(−i,0). The basepoint b has z=1, so lies on this central component away from either attaching point. Let t=−Z/W be the parameter at the origin of either elliptic component. On each overlap the coordinates satisfy the EXACT identity

    z t = −π.                                         (2)

To check the node chart rather than merely its generic-fiber identity, write the formal elliptic coordinate as Z=t⁻² U(t²), where U is an integral unit series. Equation (1) becomes

    x²=−1+z² U(t²),   zt=−π.

The derivative with respect to x at ±i is a unit, so x is an integral analytic function of z,t on each node chart. Thus each neck is an ordinary node with smoothing parameter π, hence length n/4 in the chosen valuation normalization. These elliptic charts, the normalized central rational chart, and the two node charts are the standard semistable model obtained by separating the two branch clusters in the admissible double cover. They have no further branch collisions or positive-genus components.

The central rational component has valency two and contracts in the stable model. The resulting stable fiber consists of two elliptic curves meeting at one node, and its reduction graph is a single interval of length n/2. Its midpoint is the retraction of the contracted central component, in particular of b. Equivalently, the two lengths n/4 add on contracting the valency-two vertex.

This proves in particular that C is NOT potentially good at q. Good reduction of E after a finite extension does not imply good reduction of C; here the geometric stable fiber remains reducible.

## 3. The separating class is entirely in R, and is nonzero

On the component x=i, the second quotient map has limiting relation

    f₂ = ι ∘ f₁,      ι(Z,W)=(−Z,iW).

On x=−i it has relation f₂=−ι∘f₁. These follow directly from

    X(f₂)=X(f₁)/x²,   Y(f₂)=Y(f₁)/x³.

The automorphism ι of E₀ has ι²=[−1] and degree one; on V=V_p(E₀) its trace is zero and determinant one.

The abelian homology of the stable curve is the direct sum of the homology of its two elliptic components. Under the two quotient maps its component inclusions become

    u ↦ (u,ιu),       v ↦ (v,−ιv)                      (3)

in V⊕V. Choose a symplectic basis e,f of V. The symplectic class ω₊ of the first component maps in ∧²(V⊕V) to

    ω₁ + ω₂ + B_ι,
    B_ι = e⊗ιf − f⊗ιe.

The other component maps to ω₁+ω₂−B_ι. The total surface relation maps to 2(ω₁+ω₂), which vanishes in the depth-two center. Consequently the separating class ω₊ maps there to B_ι, and ω₋ maps to −B_ι.

The tensor B_ι is symmetric. Indeed if

    ιe=a e+c f,   ιf=b e−a f,

then

    B_ι=b e⊗e−a(e⊗f+f⊗e)−c f⊗f.

It is nonzero because ι is nonzero. Thus the node class belongs entirely to the Sym² summand R. Its projection to BOTH Tate summands T is zero. This statement is stronger than observing that the two scalar height differences have zero local targets: it identifies the full central direction geometrically.

The usual choice of whether to embed ∧²V in V⊗V with a factor 1/2 changes only a common nonzero scalar, not purity in R, nonvanishing, or any ratios in the theorem.

## 4. The graph Kummer map and nonvanishing

The precise external input is the local graph description of the unipotent Kummer map in:

L. Alexander Betts and Netan Dogra, “The local theory of unipotent Kummer maps and refined Selmer schemes,” arXiv:1909.05734v2.

Relevant locations:

- Theorem 1.1.2 and Theorem 6.1.1: comparison with the reduction-graph Kummer map.
- Theorem 8.0.2 and Corollary 8.2.1: its degree-two graph formula.
- Lemma 8.2.2: explicitly the SAME reciprocal genus-two family with two elliptic components joined at one point; its Sym² quotient is affine along the stable edge.

Verified source: https://arxiv.org/html/1909.05734v2#S8.SS2 . The theorem/lemma numbering is that of v2.

In the present single-edge tree there is no graph homology. The degree-two graph formula has only the two component symplectic classes as its endpoint charges. Their sum is zero, so the Kummer map, based at the midpoint, is a linear function of signed distance, with direction the separating class ω₊. By Section 3 this direction is nonzero and lies wholly in R. Therefore t_q vanishes, and r_q varies nontrivially and linearly with signed position along the interval.

For clarity, the nonvanishing does not follow merely from the existence of the unspecified linear map in Lemma 8.2.2. It follows from the explicit nonzero node class above and the degree-two graph formula. Equivalently, after split semistable base change the separating Dehn twist acts trivially on the depth-two GROUP (conjugation by a weight-two loop only affects weight three), while its action on a path crossing the annulus contributes the weight-two separating loop. On tame inertia the latter is its signed-distance coefficient times ω₊ times the tame character. A nonzero such term cannot be a coboundary because inertia acts trivially on the central representation after this base change.

Restriction of H¹(Q_q,R) to H¹(L,R) is injective: its kernel is a cohomology group of a finite group with characteristic-zero coefficients, hence zero. The same applies to T. Thus conclusions computed after split stable base change descend without losing a nonzero class.

This establishes that, when i is Q_q-rational, the class e_q at the first elliptic endpoint is nonzero. Relative to e_q, a point at signed distance u from the midpoint has residual coordinate

    (u/(n/4)) e_q.                                    (4)

This ratio is invariant under extension of the local field and under any common metric/cohomology normalization.

## 5. Q_q-rational retractions: nonsplit case

If q≡3 modulo 4, the nontrivial unramified automorphism of Q_q(i)/Q_q exchanges the two root clusters and the two elliptic components. It acts on their stable interval by reflection. Its unique fixed point is the midpoint.

The retraction of every Q_q-rational point is Galois fixed, so every such point retracts to the midpoint, exactly as b does. The graph Kummer map is therefore zero there. Injectivity under finite extension gives r_q=t_q=0 over Q_q. This proves the nonsplit case, without incorrectly claiming that H¹(Q_q,R) itself always vanishes.

One can also see the retraction directly: x²+1 has unit value for integral x, because −1 is a nonsquare modulo q; nonintegral x lies in the central infinity chart. Thus no rational point enters either cluster neck.

## 6. Q_q-rational retractions: split case and attainability

Suppose q≡1 modulo 4 and fix i∈Q_q. Outside the two cluster disks, including the endpoint and infinity disks, every rational point retracts to the midpoint.

Inside the cluster near εi, ε∈{+1,−1}, put

    r=v_q(x²+1)>0.

If 0<r<n/2, the factor (x²+1)² is strictly dominant over A x² in the second factor of the curve equation. Hence

    v_q(y²)=3r.

A Q_q-point therefore requires r even: r=2k. The central coordinate z=y/(x²+1) then has valuation k. Equation (2) shows that the signed distance from the midpoint is εk. Thus

    1≤k<n/4,      r_q(z)=ε(4k/n)e_q.

If r≥n/2, the point lies on the elliptic side of the neck and retracts to its endpoint, giving εe_q. This includes the exact branch point (εi,0); no assumption about the unit part of A is needed.

Every intermediate value occurs. Given an integer k with 1≤k<n/4, choose x∈Q_q satisfying

    x²+1=q^{2k},     x≡i modulo q.

Such an x exists by Hensel's lemma, since i is a simple root of x²+1 modulo q. Then

    y²=q^{6k}(1+A x²/q^{4k}).

The expression in parentheses belongs to 1+q Z_q because n>4k, and is a square by Hensel's lemma. Thus this gives an actual Q_q-point with the required intermediate distance. Replacing x by −x gives the opposite value. The zero value is attained at b, and ±e_q are attained at (±i,0).

This proves the exact image and its surjectivity. Since the Tate coordinate is zero for every point, the stated same-point joint image follows without replacing an actual joint image by a product of independently chosen projections.

## 7. Consequences and remaining scope

For a=−157469, one has

    a−3=−32·7·19·37.

The odd residual images at 7 and 19 are zero. The odd residual image at 37 is exactly {0,±e_37}, with e_37 nonzero. Hence only q=37 and the still-separate q=2 analysis can contribute residual local choices for this parameter. This is a genuine nonzero residual target that is invisible to the two Tate height conditions.

For a=−605, a−3=−32·19, so every odd residual bad-prime image is zero. Likewise a=−1373 has a−3=−32·43, and again every odd residual bad-prime image is zero.

At odd q dividing a+1, E is potentially multiplicative and the previously established local cohomology calculation gives H¹(Q_q,R)=0. Thus its residual image is zero, although the Tate local condition must still be imposed. At good primes the actual full Kummer image is unramified and trivial; this does NOT assert vanishing of the entire local H¹(Q_q,R).

The prime 2 is not covered by this proof. The explicit stable-chart argument uses 2 as a unit, and the wild stable reduction and rational retractions at 2 require a separate calculation. Nor does this note compute the global map Θ_p or the local residual value δ_p(W). The theorem supplies the exact odd bad-prime residual choices and their joint compatibility; it does not by itself decide the resulting global comparison.

## 8. Exact classification of odd good-reduction primes

For any rational a≠−1,3 and odd q, C_a has good reduction over Q_q if and only if

    a∈Z_q and a modq is neither −1 nor 3.

The sufficient direction is the smooth displayed model, whose sextic discriminant is −64(a−3)⁶(a+1)². For necessity, the elliptic quotient has

    j(E_a)=256 a³/(a+1).

If v_q(a)<0, then v_q(j)=2v_q(a)<0. If a≡−1 modulo q, then v_q(j)=−v_q(a+1)<0. In either case E is not potentially good. Good reduction of C would give good reduction of its Jacobian and hence of its elliptic isogeny factors, a contradiction. Finally, if a≡3 modulo q, Sections 2–3 give a reducible geometric stable fiber with two elliptic components; this persists under finite extension, so C is not potentially good and in particular not good.

Thus restricting an argument to the displayed good odd primes loses no odd prime at which the abstract curve actually has good reduction.
