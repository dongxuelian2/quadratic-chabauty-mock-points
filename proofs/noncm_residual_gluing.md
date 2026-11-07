# Non-CM residual Selmer obstruction and exact depth-two gluing

## Scope and notation

Let C=C_a: y²=x⁶+a x⁴+a x²+1, a rational and different from -1,3. Let E: Y²=X³+(a-3)X²-(a-3)X be geometrically non-CM, with rank E(Q)=1. Put b=(0,1), P=(1,1), T=(0,0), V=V_pE, H=V_1 direct-sum V_2, using the quotient maps f1=(1+x²,y), f2=(1+x^-2,y/x³).

Fix an odd good prime p=1 modulo 4, and W_±=(±i,0). Let S exclude p and contain every bad prime. All sets here use the repository's Mordell-Weil abelian-image and actual-local-image convention. In particular, global abelian classes are restricted to E(Q) tensor Q_p in each factor; no identification with the unrestricted Bloch-Kato abelian Selmer group is assumed.

For U2=U2(C,b), write its center as

    Z=A direct-sum R,  A=Q_p(1)^2,  R=Sym² V.
    U_T=U2/R,         U_R=U2/A.

This follows from the exterior-square decomposition for V tensor Q_p² and the surface relation, which removes one of the three determinant summands. Both quotients have abelianization H.

The result below is an exact structural criterion. It does not evaluate the remaining local discrepancy or assert general exclusion of W_±.

## 1. A canonical reference and its local discrepancy

The rational involution g(x,y)=(-x,y) fixes b. It acts by +1 on V1, -1 on V2, and -1 on R. Consequently the +1 eigenspace of Lie(U_R) maps isomorphically to V1: average any lift for surjectivity; the kernel R has no +1 eigenspace. Its bracket is central and +1-invariant, hence zero. Exponentiation yields a canonical Galois-equivariant additive subgroup section

    s: V1 -> U_R.

Set a0=(kappa_E(-P),0) and gamma=s_*kappa_E(-P). This is a global crystalline-at-p class. Its abelian image is a0.

The images of b are (P,O), and those of W_± are (T,T). Rational torsion has zero rationalized Kummer class. Thus both W_± have local abelian class loc_p(a0).

For G_Q and G_Qp, H^0(G,H)=0; locally this follows from finiteness of E(Q_p)[p^infinity]. Central cohomology therefore acts freely and transitively on a nonempty fiber. Define the unique discrepancy by

    j_R,p(W_±)=delta_p(W_±) * gamma_p.

It belongs to H_f^1(Q_p,R). Here ordinary H^0-vanishing proves uniqueness, but not the finite condition. For the latter, twist by the crystalline reference torsor. The twisted Lie extension is crystalline; exactness of D_cris makes the map on B_cris-valued invariants surjective onto the abelian invariants. Hence a central class taking one crystalline lift to another must itself be crystalline.

Since g fixes gamma and negates R,

    delta_p(W_-)=-delta_p(W_+).

The local finite space has dimension two: the Hodge-Tate weights of R are 0,-1,-2, and H^0(Q_p,R)=0 by good-reduction purity.

## 2. Unconditional strict global vanishing

The Weil pairing identifies R^*(1)=ad^0 V. Newton–Thorne, Theorem B(2), proves H_f^1(Q,ad V)=0 for non-CM E, without additional residual-image hypotheses. Therefore the trace-zero summand has zero finite Selmer group.

The global finite-Selmer dimension formula gives

    h_f(R)-h_f(R^*(1))
      =h^0(R)-h^0(R^*(1))+dim(D_dR(R)/F^0)-dim(R^(c=1))
      =0-0+2-2=0.

Complex conjugation has eigenvalues +1,-1 on V; its +1 eigenspace on R is two-dimensional. Thus

    H_f^1(Q,R)=0.

This is a consequence of a proved theorem, not an assumed Bloch-Kato conjecture. Sources:
- [Newton–Thorne, arXiv:1912.11265v3, Theorem B(2)](https://arxiv.org/html/1912.11265v3).
- [Bellaïche, Introduction to Bloch–Kato, Proposition 2.7 and Theorem 2.2, printed pages 23 and 31](https://virtualmath1.stanford.edu/~conrad/BSDseminar/refs/BKintro.pdf).

For every finite q!=p, H_f^1(Q_q,R)=0. Indeed its dimension equals h^0(Q_q,R). In the potentially good case, pass to a good-reduction extension and use nonzero Frobenius weight. In the potentially multiplicative case, pass to a Tate-curve extension. Inertia-invariants in Sym²V are the line Q_p(2), whose Frobenius eigenvalue is not one. Neither case has invariants.

Also H^1(Q_q,V)=0: V and its Tate dual V^*(1)=V have no local invariants, so local duality and the q!=p Euler characteristic give the assertion.

IMPORTANT: H_f^1(Q_q,R)=0 does not imply H^1(Q_q,R)=0 at a good prime. The latter can be nonzero.

## 3. Every relaxed residual class is determined by its bad-prime restrictions

Let H_f,S^1(Q,R) impose finite conditions away from S, including p, and allow all local classes at S. Localization gives an isomorphism

    lambda_S: H_f,S^1(Q,R) -> direct-sum_(q in S) H^1(Q_q,R).

Injectivity follows because the kernel is H_f^1(Q,R)=0. For surjectivity use the general Selmer dimension formula: the dual local structure is zero at S and finite elsewhere, so its global group is contained in the zero group H_f^1(Q,ad^0 V). Relaxing at q increases the dimension by h^1(Q_q,R), since its finite subgroup was zero. The source dimension is therefore the target dimension, proving surjectivity.

At q in S every U_R class has zero abelian projection. Since H^0(Q_q,H)=0, identify this fiber with H^1(Q_q,R). Let r_q be the corresponding curve map, and Delta_q its actual image. These images are finite by local finiteness of the proper-curve unipotent Kummer map (Kim–Tamagawa; see also Betts, arXiv:2203.03701). The reference gamma has trivial restriction at q, because H^1(Q_q,V)=0.

Define

    Theta_p=loc_p composed with lambda_S^-1,
    Omega_R,p=Theta_p(product_(q in S) Delta_q).

This is a finite subset of the two-dimensional local finite space. It is not the localization of the entire relaxed Selmer vector space.

Then exactly

    W_± belongs to C(Q_p)_(U_R)
       iff delta_p(W_±) belongs to Omega_R,p.

For the proof, rank one makes localization injective on E(Q) tensor Q_p, since the logarithm of any nontorsion generator is nonzero. Thus any admissible global lift of W_± has abelian class a0, even if P itself is torsion. Its unique difference from gamma is a class alpha in H_f,S^1(Q,R). Actual conditions say alpha_q in Delta_q and alpha_p=delta_p(W_±). The localization isomorphism proves both directions.

Failure of this criterion excludes full depth two. Passing it alone does not establish full membership.

## 4. Which primes can contribute?

At a potentially multiplicative q!=p, H^1(Q_q,R)=0. On a Tate-curve extension any endomorphism commuting with nonzero inertia monodromy has shape cI+dN. Commutation with Frobenius forces d=0. Thus H^0(Q_q,ad^0 V)=0; local duality and the Euler characteristic, together with H^0(Q_q,R)=0, prove the claim.

For our E,

    Delta=16(a-3)^3(a+1),
    c4=16(a-3)a,
    j=256a³/(a+1).

At an odd integral prime with v_q(a+1)>0 the reduction is multiplicative. At an odd denominator prime, v_q(j)=2v_q(a)<0, so it is potentially multiplicative. Both have zero H^1(Q_q,R).

At good primes the actual local image is unramified and therefore zero, although full H^1(Q_q,R) need not vanish. Hence the only possible nonzero ACTUAL residual contributions are from 2 and odd q with v_q(a-3)>0. If S was enlarged by good primes, their actual Delta_q is {0}; no vanishing of their full H^1 is asserted.

Odd denominator primes thus introduce no Sym² residual coordinate, while their scalar-height corrections remain as in rational_denominator_targets.md.

## 5. Ordinary and crystalline gluing

There is a group isomorphism

    U2 = U_T fiber-product_over_H U_R.

Its kernel is A intersect R=0. To prove surjectivity, lift a U_T element to U2, then adjust its U_R component by R.

For any of our global or local Galois groups G, H^0(G,H)=0 implies

    H^1(G,U2)
      = H^1(G,U_T) fiber-product_over_H^1(G,H) H^1(G,U_R).

Surjectivity: align abelian cocycles using a gauge lifting the abelian coboundary, then pair the cocycles. Injectivity: two quotient gauges relating the same pair have abelian images differing by a G-invariant element of H; it is zero, so the gauges themselves pair in the fiber product.

At p the same assertion holds with H_f^1. To verify this extra claim, write crystalline quotient cocycles, with the same abelian cocycle, as x_T^-1 g(x_T) and x_R^-1 g(x_R) over B_cris. Their abelian trivializations differ by h in D_cris(H), which need not be zero. Good reduction makes Lie(U_T) crystalline. Exactness of D_cris and exponentiation imply surjectivity

    U_T(B_cris)^G -> H(B_cris)^G.

Multiply x_T on the left by an invariant lift of the required difference. This leaves its coboundary unchanged and aligns the abelian trivializations. They now pair to a B_cris trivialization of the U2 cocycle, proving crystallinity. Ordinary H^0-vanishing alone would not justify this step.

## 6. Exact full-depth-two criterion: retain joint actual images

Identify the zero-abelian U_T fiber at q!=p with H^1(Q_q,A), and denote its curve map by t_q. Define the finite joint image

    Xi_q={(t_q(z),r_q(z)): z in C(Q_q)}.

It need not be the product of its two projections.

Let T_p(W) be the set of global U_T classes unramified outside S and p, with abelian projection a0 and p-localization j_T,p(W). This definition does not assume that the two existing scalar equations are sufficient to produce a global Tate lift.

Then W=W_± belongs to full C(Q_p)_2 exactly when there exist t in T_p(W) and (tau_q,rho_q) in Xi_q at each q in S satisfying

    loc_q(t)=tau_q for each q in S,
    delta_p(W)=Theta_p((rho_q)_q).

Necessity follows by projecting a full admissible class: both quotient conditions must use the SAME local point at each q.

Conversely, set alpha=lambda_S^-1((rho_q)) and r=alpha*gamma. The classes t and r have the same global abelian class and glue uniquely. Crystalline gluing makes the full class finite at p. At p and at every q in S, injectivity of local gluing identifies it with the required local curve class. At good primes outside S and p, unramified U2 cohomology is trivial because no graded Frobenius eigenvalue is one. Thus all actual local conditions hold.

At primes where H^1(Q_q,R)=0, Xi_q has form {(t_q(z),0)}. There is no further residual compatibility there, but the Tate condition remains.

## 7. No extra Artin–Tate central quotient

For every finite extension L/Q, geometric non-CM and Faltings imply End_(G_L)(V)=Q_p. A G_L-equivariant map Sym²V -> Q_p(1) gives a symmetric invariant pairing. Write it as <Bu,v> using the Weil pairing. Equivariance forces B scalar, making this pairing alternating and hence zero. Trivializing an Artin representation M over a finite extension gives Hom_G(R,M(1))=0. Purity excludes other Tate twists.

Thus A exhausts the Artin–Tate central quotient. This does not rule out non-Tate generalized heights.

## Unresolved computations

No value or nonvanishing proof for delta_p(i,0) is supplied. The surviving joint bad-prime images Xi_q, and the relevant global Tate lift, are not computed. Consequently this theorem proves neither general non-CM exclusion nor sufficiency of the two scalar-height equations. It isolates the full residual problem and proves that its relaxed global lifting is uniquely controlled by finitely many bad local coordinates.
