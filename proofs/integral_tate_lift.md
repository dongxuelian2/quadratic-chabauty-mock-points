# A unique compatible Tate lift for the integral reciprocal family

Assume a is an integer, a!= -1,3, a=3 modulo 8, E_a geometrically non-CM with rational rank one. Let p be an odd good prime congruent to 1 modulo 4. Use b=(0,1), W_±=(±i,0), H=V_p(E)^2, A=Q_p(1)^2, R=Sym²V_p(E), and the MW-restricted actual-local convention. Let S contain 2 and every bad prime, but not p. Put U_T=U2/R, with center A, as in Theorem 34. Set a0=(kappa(-P),0), P=(1,1).

## A. Global Tate lift exists

The central extension A -> U_T -> H attaches to a0 an obstruction in H²(G_Q,S∪p,A). Every local obstruction is zero: at p the actual path to W_+ supplies a lift; at q in S the abelian class is zero because H¹(Q_q,V_pE)=0, so the neutral U_T class supplies a lift. Real cohomology in positive degree vanishes for odd p.

The localization map H²(G_Q,S∪p,Q_p(1)) -> direct-sum_(q in S∪p) H²(Q_q,Q_p(1)) is injective. This follows from Kummer theory and the global Brauer injection; the localized integer ring Z[1/(p product S)] has trivial ideal class group. At finite p-power level there is no Picard contribution; passage to p-adic Tate modules and then rational coefficients retains injectivity. Thus the obstruction vanishes and a global Tate lift t exists.

The central fiber is a free H¹(G_Q,S∪p,A)-torsor, since H⁰(G_Q,H)=0. Localization of this central group at p is surjective: for each Q_p(1) factor the classes of p and 2 have respectively nonzero valuation and nonzero unit logarithm; log_p(2)!=0. Thus adjust t centrally until its p-local class equals j_T,p(W_+). This produces a crystalline global Tate lift, without imposing bad-local actual conditions yet.

## B. Unique lift with zero bad-local coordinates

Kummer theory identifies H_f,S¹(Q,Q_p(1)) with O_Q,S^× tensor Q_p. Its valuation map to direct-sum_(q in S) H¹(Q_q,Q_p(1)) is an isomorphism: the latter local spaces are each one-dimensional and the generators q∈S give the coordinate basis. Crystallinity at p excludes the p valuation.

The same statement holds twice for A. Hence centrally adjust the crystalline lift by a unique H_f,S¹(Q,A) class to kill every bad-local Tate class. Call the result t_zero. It is crystalline, has abelian class a0 and is neutral at every q∈S. It is unique: a difference preserving those properties lies in H_f¹(Q,A)=0.

## C. The two correspondences form a basis of A*

The involution g(x,y)=(-x,y) acts on the two elliptic factors by diag(1,-1). The second-model involution (u,v)->(-u,v), under u=(x+1)/(x-1), v=4y/(x-1)^3, is (x,y)->(1/x,-y/x^3). It acts on the quotient factors by minus the exchange matrix.

Taking each graph difference with its hyperelliptic partner therefore gives, up to nonzero rational factors, the trace-zero Rosati-symmetric matrices diag(1,-1) and exchange. These are independent. The two rational Tate central directions are precisely the trace-zero symmetric multiplicity-space forms; hence these two correspondence functionals are a basis of Hom(A,Q_p(1)).

On H_f¹(Q_p,A), their local height maps form an isomorphism to Q_p²: local height on a central Q_p(1) change is the cyclotomic logarithm, which is nonzero and is an isomorphism on the one-dimensional finite local Kummer space. Compatible height splittings alter no such linear independence.

## D. Comparison with both Weierstrass points

For any global U_T torsor t above a0 that is crystalline at p, twist the fixed path module A_Z(b) by t. This construction applies to arbitrary torsors, not only point torsors: see Balakrishnan–Dogra I, Definition 5.3 and Section 5.2. Its adjacent classes are the abelian class and the fixed-basepoint affine linear expression in that class. Section 4.3.3 makes the sum of local heights depend only on these adjacent classes.

Theorem 18 and the endpoint-basepoint bridge identify the resulting bilinear Mordell-Weil expression as F(W)-F(b), with the necessary basepoint linear correction. This is an identity of divisor-class forms, not interpolation on rational curve points. For t_zero every away-from-p class is neutral, so its local mixed-extension height equals H_v(b,b)=0. Hence

    H_p(t_zero)=F(W)-F(b).

For the actual local point W, the local comparison is

    H_p(j_T,p(W))=r_p(W)-r_p(b).

Subtracting gives rho_p(W)-rho_p(b). Both scalar functions vanish at W_±. For both correspondences rho_p(b)=sum_(q!=p) w_q(b)=0: the first endpoint value is zero because P is integral nonsingular at every away-from-p place under a=3 modulo 8; the second basepoint has coordinate u=-1, where the paired elliptic images are negatives and their height difference is zero.

Thus both local heights agree for t_zero and W. Equivalently, for the first correspondence the global value is -h_p(P) and the local point value is -lambda_p(P), equal in this integral family; for the second correspondence both values are zero.

The two local classes have the same abelian projection and are crystalline. Their central difference is therefore in H_f^1(Q_p,A), by the crystalline central-fiber exactness proved in the residual-gluing theorem. Section 4.3.3 of Balakrishnan–Dogra I gives the central-translation formula: the height changes by the local cyclotomic character paired with the corresponding central pushout, namely chi_p cup xi_(Z,*)(d). The two basis functionals from Section C therefore detect the difference injectively. It is zero, so

    (t_zero)_p=j_T,p(W_+) = j_T,p(W_-).

This is a sufficiency proof for this particular Tate fiber. It does not assume arbitrary scalar-height equations are sufficient for global lifting.

## E. Actual joint compatibility

At every odd q | a-3, Theorem 36 proves Xi_q={(0,r):r∈Delta_q}. At 2 the two local scalar functions are identically zero for a=3 modulo 8. Their basepoint values also vanish, so the two independent correspondence functionals annihilate the actual Tate Kummer coordinate. Since H¹(Q_2,Q_p(1)) is one-dimensional and log_p(2)!=0, the full Tate coordinate is zero. Thus every actual residual value at 2 is achieved jointly with zero Tate coordinate.

At odd q | a+1, the residual space H¹(Q_q,R) is zero. Its sole residual value is achieved at b, whose full local Kummer class is neutral. At all good primes the actual class is neutral. These observations retain SAME-POINT joint compatibility at every prime; no product of unrelated target sets is substituted.

By Theorem 34's exact full gluing, the existence of t_zero now proves

    W_±∈C_a(Q_p)_2 iff delta_p(W_±)∈Omega_R,p.

Thus for this integral congruence family the Tate lift and joint-image quantifier are fully discharged. The right side still requires computing the dyadic residual image and the global transport/comparison.

Using Theorem 36, Omega_R,p is the transport under Theta_p of the dyadic actual image and the explicit finite split-prime images at odd q | a-3, q=1 modulo 4. All other odd factors are zero. No nonvanishing of delta_p, no numerical evaluation of Theta_p, and no general exclusion or membership claim follows without those remaining computations.

## Sources and scope

The global Brauer injection follows from the Albert–Brauer–Hasse–Noether exact sequence and finite-level Kummer theory. See J. S. Milne, [Class Field Theory](https://www.jmilne.org/math/CourseNotes/CFT.pdf), Chapter IV, Remark 2.14(e). For the inverse-limit step, finite H^1 groups satisfy Mittag–Leffler, so no derived-limit kernel is introduced.

The arbitrary-torsor twisting and central-height translation are in J. S. Balakrishnan and N. Dogra, [Quadratic Chabauty and rational points I](https://arxiv.org/pdf/1601.00388), Definition 5.3 and Sections 4.3.3, 5.2. The local scalar comparisons and their endpoint extension are the previously proved repository results.

No unrestricted Bloch–Kato/Mordell-Weil identification is assumed. Rank one is retained, and no vanishing of the unknown dyadic residual image or local discrepancy is inferred.
