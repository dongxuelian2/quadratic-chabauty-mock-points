# The Weierstrass discrepancy as a global quadratic-twisted class

Status: independently reviewed mathematical result. This supplies a nonzero GLOBAL class and an exact localization interpretation. It does not assert nonvanishing of its localization at the coefficient prime.

## 1. Statement and conventions

Let

    C_a: y²=x⁶+a x⁴+a x²+1,
    E_a: Y²=X³+(a−3)X²−(a−3)X,
    b=(0,1),  P=(1,1),  T=(0,0),

where a∈Q and a≠−1,3. Let p be an odd good-reduction prime for C, with p≡1 modulo 4. Put V=V_pE and R=Sym²V. Use the quotient maps

    f₁=(1+x²,y),   f₂=(1+x⁻²,y/x³).

For the depth-two unipotent group based at b, put

    U_R=U₂/Q_p(1)²,   H=V₁⊕V₂.

Its center is R. We use exactly the quotient identification and canonical reference of the non-CM residual-gluing theorem. The local construction below does not require rank one or non-CM. These assumptions are needed only when applying the established global Chabauty–Kim criterion or the dimension observation in Section 7.

Fix K=Q(i) inside an algebraic closure of Q, and let χ=χ₋₄ be its quadratic character. Fix an embedding K→Q_p, carrying i to the chosen square root i_p. Write

    W₊=(i,0),   W₋=(−i,0),   B=R⊗Q_p(χ).

The symbol B here denotes a representation, not the odd integer used in the dyadic proof.

**Theorem.** There is a canonically determined class, after the stated choice of i and of the trivialization of χ over K,

    η_p ∈ H¹(Q,B),

with the following properties.

1. Under restriction to K, η_p is the unique central difference between the global U_R Kummer class of W₊ and the canonical global reference γ restricted to K.
2. At the chosen split place over p, the identification B|G_Qp=R carries loc_p(η_p) to δ_p(W₊). At the other split place the value is its negative. The class is crystalline at p.
3. For every odd q with n=v_q(a−3)>0, the restriction of η_p to Q_q(i) is nonzero and ramified. If q≡3 modulo 4, this is an unramified quadratic local extension, and loc_q(η_p) itself is a nonzero ramified B-valued class over Q_q.
4. In particular, η_p is globally nonzero whenever a−3 has an odd prime divisor of positive valuation. For a=−605, its nonzero ramification at q=19 proves η_p≠0 for every odd good p≡1 modulo 4.

Replacing i by −i changes the sign of η_p and δ_p, without affecting vanishing or nonvanishing. No additional choice of an étale path is made in this construction.

The nonzero class η_p belongs to a QUADRATIC TWIST of the residual representation. The proved vanishing H_f¹(Q,R)=0 for non-CM E does not apply to H¹(Q,B).

## 2. The canonical global reference

The involution

    g(x,y)=(-x,y)

is defined over Q and fixes b. On H it acts by +1 on V₁ and −1 on V₂; on R it acts by −1. The +1 eigenspace of Lie(U_R) therefore maps isomorphically onto V₁. Its bracket is central and +1 invariant, so is zero. Exponentiation gives the canonical G_Q-equivariant subgroup section

    s:V₁→U_R.

Let

    a₀=(κ_E(−P),0),   γ=s_*κ_E(−P)∈H¹(Q,U_R).

Then gγ=γ. The section and γ are defined over Q, not chosen separately over K or Q_p.

For any number field F, H⁰(F,V)=0 because E(F)[p^∞] is finite. The same holds for every finite local extension of Q_ℓ, including ℓ=p. Hence H⁰(F,H)=0 for all global and local fields used here.

For a central extension with kernel R, H¹(F,R) acts transitively on each nonempty fiber over a fixed abelian H¹(F,H) class; the stabilizer is the image of H⁰(F,H). Thus these fibers are torsors under H¹(F,R) in the present situation. This proves uniqueness of every central difference used below, and ensures that restriction and automorphisms preserve those differences.

The images of b under the two quotient maps are (P,O), whereas the images of both W₊ and W₋ are (T,T). Since T is torsion, its rationalized Kummer class is zero. Both global U_R Kummer classes over K consequently have abelian image res_K(a₀).

There are unique α₊,α₋∈H¹(K,R) satisfying

    j_R,K(W₊)=α₊*γ_K,
    j_R,K(W₋)=α₋*γ_K.                         (1)

The star denotes the central cohomology action, not a choice of cocycle representative.

## 3. Exact quadratic descent

Let c denote the nontrivial element of Gal(K/Q), acting on H¹(K,R) through the Q-structure on R. This action is independent of the chosen lift of c to G_Q. Galois functoriality of point Kummer classes and the fact that γ is defined over Q give

    c(α₊)=α₋.

Geometric functoriality under g gives the same endpoint exchange, but g acts by −1 on R and fixes γ. Therefore

    α₋=−α₊,   c(α₊)=−α₊.                    (2)

These are two different actions with the same endpoint effect: c is arithmetic conjugation, whereas g is an automorphism of the curve. Their comparison is what proves the anti-invariance. Merely observing W₋=c(W₊) would not prove (2).

Choose a basis eχ of Q_p(χ). It identifies B|G_K with R by r⊗eχ↦r. Under this identification, invariance of a B-valued K-cohomology class under Gal(K/Q) is exactly anti-invariance of its R-valued class. Inflation-restriction yields

    H¹(Q,B) ≅ H¹(K,B)^{Gal(K/Q)}
             ≅ H¹(K,R)^{c=−1}.             (3)

Indeed the kernel and obstruction in inflation-restriction are positive-degree cohomology groups of the finite group Gal(K/Q) with Q_p-vector-space coefficients; they vanish by averaging. This argument does not require a conjectural Selmer vanishing. In fact p is odd here, although averaging in Q_p would work in characteristic zero even without that restriction.

Define η_p to be the unique class corresponding to α₊ under (3). This proves the claimed global existence and uniqueness. Changing eχ changes the displayed scalar normalization; fixing it as above makes (3) and all local identifications precise. The zero/nonzero statements are intrinsic.

## 4. Crystalline split-p localization

Because p splits in K, the chosen embedding K→Q_p identifies one completion K_v with Q_p and trivializes χ locally. Restricting (1) to that completion gives

    j_R,p(W₊)=loc_p(η_p)*γ_p.

The definition and uniqueness of the discrepancy in the residual-gluing theorem therefore give

    loc_p(η_p)=δ_p(W₊).                     (4)

At the conjugate completion the same argument gives −δ_p(W₊).

Good reduction of C at p makes the local curve torsor crystalline, and the Kummer class γ_p is crystalline. Their unique central difference is crystalline. One must use the crystalline central-difference argument here, not just ordinary H⁰-vanishing: twist by the crystalline reference torsor; its Lie extension is crystalline, and exactness of D_cris makes invariant B_cris-valued lifts surjective over the abelian invariants. Consequently a central class taking one crystalline lift to another belongs to H_f¹(Q_p,R). This is the same argument proved in the residual-gluing theorem, now applied to (1).

Thus η_p lies in the Selmer group with finite condition at p and relaxed conditions at a finite bad-prime set. It is unramified at all but finitely many primes, as is automatic from its construction from global geometric Kummer classes. At good primes away from 2 and p the actual local curve class and reference are both zero, so its restriction is zero there.

## 5. Base change of the odd-prime endpoint computation

Fix an odd q with n=v_q(a−3)>0. Such a q is not the good coefficient prime p. Set F=Q_q(i), viewed as a chosen completion of K. It is Q_q when q≡1 modulo 4 and the unramified quadratic extension when q≡3 modulo 4.

The previously established odd-prime stable-model proof extends to F without alteration. We spell out the relevant steps to exclude a hidden dependence on the residue field being prime.

Put A=a−3 and choose a finite extension L/F with π⁴=A. Normalize valuation by v(q)=1, also after extension. The elliptic charts are

    Z=(x²+1)/π²,   W=y/π³,
    W²=Z³−Z+π²Z²,   x²=−1+π²Z.              (5)

Since 2 is a unit and i∈F, their reductions are the two smooth elliptic components E₀:W²=Z³−Z at x=±i. The central rational chart has z=y/(x²+1), reduction z²=x²+1, and overlaps satisfying

    zt=−π,   t=−Z/W.                        (6)

Each neck has length n/4. Contracting the middle valency-two rational component gives one stable edge of length n/2, with b retracting to its midpoint. The points W₊ and W₋ retract to the two opposite elliptic endpoints.

All these statements use only odd residue characteristic, the unit derivative 2i, and the valuation of A. Passing from Q_q to its unramified quadratic extension does not change the normalized lengths. The elliptic equation in (5) is smooth even in residue characteristic 3.

On the two elliptic components the quotient maps satisfy f₂=±ιf₁, where

    ι(Z,W)=(−Z,iW),   ι²=−1.

The component homology inclusions into V⊕V are u↦(u,±ιu). If e,f form a symplectic basis of V, the two component symplectic classes map to

    ω₁+ω₂±Sι,
    Sι=e⊗ιf−f⊗ιe∈Sym²V.

The full surface relation kills 2(ω₁+ω₂). The tensor Sι is symmetric and nonzero because tr(ι)=0 and ι≠0. Hence the separating node class is nonzero and entirely in R, with zero projection to both Tate-center directions.

The Betts–Dogra degree-two graph Kummer formula on this tree is linear in signed distance from the midpoint with nonzero direction Sι. Therefore

    e_F := j_R,F(W₊) ∈ H¹(F,R)

is nonzero, and j_R,F(W₋)=−e_F. Here H¹(F,V)=0 for p≠q: V has no invariants and neither does its Tate dual, so local duality and Euler characteristic give the vanishing. Thus γ_F=0, and these are exactly the central differences in (1), not differences with an unaccounted reference translation.

For the stronger ramification assertion, after the split semistable extension L the representation R is unramified: the Jacobian has good reduction because the stable fiber is of compact type. On tame inertia the path from the midpoint to the endpoint contributes a nonzero multiple of Sι times the p-adic tame character. This cannot be a coboundary because inertia acts trivially on R there. Therefore the endpoint class is nonzero on inertia over L, hence ramified over F. This is the same nonvanishing justification used in the audited odd-prime theorem; it is not inferred solely from an unspecified affine map.

For q≡3 modulo 4, restriction of loc_q(η_p) to F identifies with e_F by (1) and (3). A zero or unramified class over Q_q restricts to a zero or unramified class over an unramified extension. Since e_F is nonzero and ramified, loc_q(η_p) is nonzero and ramified. Equivalently, finite-extension restriction is injective in characteristic-zero H¹, and the explicit inertia computation gives the stronger ramification conclusion.

There is no contradiction with Δ_q={0} for Q_q-rational points in the untwisted theorem. Such points retract to the midpoint, while W₊ is not Q_q-rational. Moreover, η_p has coefficients R⊗χ, not R. Over F, both W₊ and W₋ are rational and lie at the two endpoints.

Source for the graph comparison and degree-two formula: Betts–Dogra, arXiv:1909.05734v2, Theorems 1.1.2, 6.1.1 and 8.0.2, Corollary 8.2.1, and Lemma 8.2.2. The last lemma treats this exact reciprocal family; nonzero slope additionally uses the separating-class calculation above. https://arxiv.org/html/1909.05734v2#S8.SS2

## 6. The example a=−605 and the exact remaining obstruction

Here

    a−3=−32·19.

Since 19≡3 modulo 4, F=Q₁₉(i) is unramified quadratic, and n=1. The stable edge has length 1/2; W₊ is at distance 1/4 from the midpoint. Section 5 proves

    res_F(loc₁₉ η_p)=e_F≠0,

with nonzero tame-inertia restriction after the stable extension. Thus η_p is globally nonzero for every odd good p≡1 modulo 4. No numerical p-adic computation is needed.

For example p=5 is a good split prime: a≡0 modulo 5, different from −1 and 3. Hence η₅≠0 globally and δ₅(W₊)=loc₅(η₅), but this note does not decide whether the latter is zero.

The original actual residual targets over Q are all zero for a=−605: the dyadic theorem applies because v₂(a−3)=5, the odd bad prime 19 is nonsplit, and all other actual residual images vanish by the established good/potentially multiplicative cases. Consequently the original residual membership condition for W₊ is exactly

    δ_p(W₊)=0  ⇔  loc_p(η_p)=0.               (7)

Global nonvanishing of η_p does NOT imply the negation of (7). A global class can be ramified at 19 and vanish on G_Qp. The localization map is not known to be injective on the relevant relaxed twisted Selmer group, and the untwisted Newton–Thorne vanishing does not supply this missing injectivity.

Concretely, if S contains the bad primes, the remaining problem is whether this explicitly characterized nonzero class lies in

    ker[H¹_{f,S}(Q,R⊗χ₋₄) → H_f¹(Q_p,R)].

To prove exclusion one needs either a rigorous nonzero crystalline-period / iterated-integral evaluation of η_p at p, or a theorem proving that this particular class is not in that kernel. For a=−605, Theorem37 has already settled the Tate lift and joint-image compatibility, so full membership is exactly equivalent to loc_p(η_p)=0. Neither vanishing nor nonvanishing follows from the symmetries or ramification alone.

The local symmetry g only proves δ_p(W₋)=−δ_p(W₊). It does not fix either point, so it does not force δ_p(W₊)=0.

## 7. Why blanket relaxed-localization injectivity is often impossible

This observation is separate from the descent theorem. Assume E is geometrically non-CM, retain p split and good, and let S exclude p and contain all bad primes. Put B=R⊗χ₋₄ and B^∨(1)=ad⁰(V)⊗χ₋₄.

Both global invariant spaces vanish: after restricting to K, geometric non-CM and Faltings give End_{G_K}(V)=Q_p, whose trace-zero part is zero; purity gives the corresponding statement for R. The local tangent dimension is dim t_B=2, while complex conjugation has a one-dimensional +1 eigenspace on B (the quadratic twist reverses the +1 dimension 2 and −1 dimension 1 of R).

At q≠p the finite local subgroup H_f¹(Q_q,B) is zero. Indeed after a finite extension killing χ, E is either good or a Tate curve; the invariant weight or the Tate inertia line excludes eigenvalue 1, as in the untwisted proof. The general Selmer dimension formula, with the dual local condition strict at S, therefore gives

    dim H¹_{f,S}(Q,B)
      = 1 + Σ_{q∈S} dim H¹(Q_q,B)
          + dim H¹_{dual-strict-S}(Q,B^∨(1)).       (8)

No vanishing of the last term is asserted. Every distinct odd q with v_q(a−3)>0 contributes at least one to the sum by Section 5. If there are at least two such primes, the source in (8) has dimension at least three, whereas H_f¹(Q_p,B) has dimension two. Thus localization on the whole relaxed group CANNOT be injective in that case. This does not decide localization on the distinguished line Q_pη_p.

For a=−605 there is only one such odd prime, so this dimension bound alone neither proves nor disproves injectivity. In all cases the mathematically relevant question is the specific value loc_p(η_p), not a presumed general local-global principle.

The dimension formula is the same Poitou–Tate/Bloch–Kato formula used in the residual-gluing theorem; see Bellaïche, *An Introduction to the Conjecture of Bloch and Kato*, Theorem 2.2 and Proposition 2.7 (change of local conditions). https://virtualmath1.stanford.edu/~conrad/BSDseminar/refs/BKintro.pdf

## 8. Established versus unresolved

Established unconditionally here: the canonical twisted global class; exact split-p localization; nonzero bad-prime ramification; global nonvanishing for −605; and the dimension obstruction to blanket injectivity when there are at least two odd primes dividing a−3.

Unresolved: nonvanishing or vanishing of δ_p(i,0), including a=−605, p=5. No first-height test is substituted for this residual computation, and no local nonvanishing is inferred from global nonvanishing.
