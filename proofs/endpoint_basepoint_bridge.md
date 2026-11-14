# The endpoint-basepoint bridge by a double twist of the finite path algebra

This is an isolated proof of the basepoint extension needed for the prime-3 disk calculation. It does not use approximation of a rational basepoint by rational curve points. It does not infer regularity merely from regularity in one variable.

## Lemma: joint regularity of the correspondence mixed extension

Let C/K be a smooth proper geometrically connected curve with a K-rational point a. Fix a Galois-equivariant correspondence functional

\[
 \xi_Z:A[2]\longrightarrow\mathbf Q_p(1)
\]

as in Balakrishnan–Dogra I, Definition 5.3, with nonzero restriction to the commutator quotient. Let A_Z(b,z) denote their corresponding mixed extension, using the full proper curve. For a place v of K, put

\[
 H_v(b,z)=h_v(A_Z(b,z)).
\]

At a place above p of good reduction, with fixed height splitting, H_v is jointly locally analytic on C(K_v)×C(K_v). At a place away from p it is jointly locally constant. In particular, these statements hold when either argument is an endpoint in any chosen affine model of C.

### Proof, including the moving-basepoint quotient

Let

\[
 A_2(a)=\mathbf Q_p[[\pi_1(\overline C,a)]]/I^3,
 \qquad A[2]=I^2/I^3,
 \qquad K_Z=\ker(\xi_Z)\subset A[2].
\]

The completed group algebra here means precisely the rational augmentation quotient in Definition 5.1; only its finite-dimensional quotient is used. Write

\[
 M=A_2(a)/K_Z.
\]

This is the pushout called A_Z(a) in Definition 5.3. Its graded pieces are \(\mathbf Q_p,V,\mathbf Q_p(1)\), and its rank is \(2g+2\).

The truncated algebra admits commuting left and right multiplication actions. With source and target factors ordered explicitly, use

\[
 (g_b,g_z)\cdot m=g_z\,m\,g_b^{-1}. \tag{1}
\]

Every group element has augmentation 1. If \(k\in I^2/I^3\), then

\[
 (1+i)k(1+j)=k\pmod{I^3},\qquad i,j\in I.
\]

Thus both actions fix A[2] pointwise, preserve K_Z, and descend to M. They also preserve its filtration and induce the identity on each graded piece. The actions factor through the finite-step unipotent group U_2(a). They are Galois-equivariant because multiplication, the filtration, and \(\xi_Z\) are Galois-equivariant. This supplies a **fixed** filtered Galois representation M with an algebraic U_2(a)×U_2(a) action.

For any b,z, take the two fixed-basepoint torsors P(a,b) and P(a,z), and double-twist M by their product using (1). The result is canonically A_Z(b,z), not merely a mixed extension attached to P(b,z) using an unrelated fixed module. To verify this, choose geometric paths \(p_b:a\to b\), \(p_z:a\to z\). The map

\[
 \gamma\longmapsto p_z\circ\gamma\circ p_b^{-1}
\]

identifies the group-algebra path module at (a,a) with the module of paths from b to z. Under Galois, this identification changes by

\[
 m\longmapsto c_z(\sigma)\,\sigma(m)\,c_b(\sigma)^{-1},
\]

which is exactly the double-twist descent law. Changing either chosen geometric path changes the trivialization by (1), so the construction is independent of these choices.

It remains important that the functional defining the quotient has not changed with b. Transport of loop algebras from a to b is conjugation by \(p_b\). Any ambiguity in this transport is inner conjugation, which acts trivially on I²/I³. Therefore A[2] is canonically identified across basepoints, and \(\xi_Z\), defined by the fixed correspondence class, is carried to the same functional. Taking the quotient by K_Z hence commutes with transport and twisting. Equivalently, this is the explicit two-variable form of the last observation following Definition 5.3: the quotient may be taken after twisting because the action on A[2] is trivial. The resulting module is exactly the published Definition 5.2 path module, pushed out by the published Definition 5.3 functional.

The fixed double action gives an algebraic twisting map

\[
 H^1(G_v,U_2(a))\times H^1(G_v,U_2(a))
 \longrightarrow
 H^1(G_v,U(\mathbf Q_p,V,\mathbf Q_p(1))). \tag{2}
\]

As in Section 5.1, one first maps into the filtered automorphism group of M, and then uses the Galois-equivariant bitorsor of graded-compatible splittings to identify its classes with mixed extensions. This is the same algebraic twisting argument as there, with U_2 replaced by U_2×U_2. At a good p-adic place, the representation and actions are crystalline, and (2) restricts to finite/crystalline classes. The map (b,z) into its source is the product of two ordinary fixed-basepoint local Kummer maps. Those maps are locally analytic. The crystalline local height on the target is algebraic by Balakrishnan–Dogra I, Lemma 4.8. Their composite is H_v(b,z), proving joint local analyticity.

Away from p, each fixed-basepoint local Kummer map is locally constant. The product, its double twist, and its scalar height are therefore locally constant. This proves the lemma. ∎

## Corollary: extension of the local height comparison in both endpoints

Use the bielliptic correspondence and sign conventions of Theorem 18 of the manuscript. On the generic open set of pairs (b,z), its comparison formula is

\[
 H_v(b,z)=r_v(z)-r_v(b),
 \qquad
 r_v=\lambda_{1,v}\circ\phi_1-\lambda_{2,v}\circ\phi_2
      -2\chi_v(x). \tag{3}
\]

The right side extends across x=0 and infinity by cancellation of its logarithmic singularities; this cancellation was proved explicitly in Theorem 18. The left side extends by the lemma above. For each local field, the generic open set of pairs is dense in the product of the local curves. Hence (3) holds at endpoint basepoints as well.

The comparison on this generic open set is a local statement about local points and local divisor heights. It does not require b or z to be K-rational. Thus this density argument does not assume a supply of rational curve points near b. It uses local points only.

## Global quadratic correction at an endpoint

There is a separate issue from scalar local continuity: the global correction must agree with the intended Mordell–Weil quadratic form at the endpoint. This can be checked using the adjacent extension classes, without defining a divisor height at colliding supports.

Let S=C×C. The finite path-module construction above gives filtered lisse families on all of S. Its two adjacent extensions are therefore lisse everywhere. The maps

\[
 (b,z)\longmapsto[z-b]\in J(C),
 \qquad
 (b,z)\longmapsto[D_Z(b,z)]\in J(C)
\]

are algebraic on all of S. For this correspondence,

\[
 D_Z(b,z)=D_\infty-D_0+g_1z-g_2z+g_1b-g_2b.
\]

Their Kummer extensions form lisse families on S as well, obtained by pulling back the universal Kummer extension on J(C). To compare them with the two adjacent extensions of A_Z(b,z), take the function field \(F=K(S)=K(C\times C)\), with b and z its two generic points on \(C_F\). Apply the purely étale cycle/path construction of Balakrishnan–Dogra I, Theorem 6.3, over F. Section 6.3 works over a characteristic-zero field, and its construction uses cycle classes, exact sequences, pullbacks, and pushouts; it does not require a local height or a number-field specialization at this stage. The generic points satisfy the required generic support conditions. The theorem therefore gives a \(G_F\)-equivariant isomorphism of the generic adjacent extensions, with the same duality and sign convention used in Theorem 18.

Both sides of each adjacent-extension comparison are already lisse on the whole normal connected variety S. The natural homomorphism \(G_F\to\pi_1(S)\) is surjective, so an intertwiner of their generic \(G_F\)-representations is an intertwiner of their \(\pi_1(S)\)-representations. The generic isomorphism consequently extends uniquely to an isomorphism on all of S. This proves the comparison at endpoint pairs without assuming a relative version of the mixed-extension comparison or density of rational points. Only the adjacent extensions are extended this way; no mixed extension of divisors with disjoint supports is asserted to exist at a collision.

The global height factors bilinearly through the two adjacent extensions, as established in Section 4.3.3 of the same source. Consequently its quadratic correction at every rational b is the pairing of the two displayed divisor classes. Their exact pullback identity is

\[
 D_Z(b,z)=-\phi_1^*T_1+\phi_2^*T_2+\operatorname{div}(x),
 \qquad
 T_i=(-P_i)+(-B_i)-2O_i,
\]

where \(P_i=\phi_i(z)\), \(B_i=\phi_i(b)\). This is an identity of divisors with multiplicities at the endpoint fibers too. The principal term is zero on divisor classes. Projection and bilinearity therefore give

\[
 h_1(P_1)-h_1(B_1)-h_2(P_2)+h_2(B_2). \tag{4}
\]

In particular, when b=(0,1), one has \(B_1=P\), \(B_2=O\), and \([T_2]=-[P_2]\). There is no undefined height at O: h_2(O)=0 is the global quadratic height of the zero class.

For clarity, (4) determines the correction on the entire Mordell–Weil vector space, not by interpolation on rational curve points. If \(a_i=P_i-B_i\), it is the polynomial

\[
 h_1(a_1)+2\langle a_1,B_1\rangle_{h_1}
 -h_2(a_2)-2\langle a_2,B_2\rangle_{h_2}.
\]

Since each elliptic curve has rank one, localization identifies this with F(z)−F(b), where
\(F=\alpha_1L_1^2\circ\phi_1-\alpha_2L_2^2\circ\phi_2\), exactly as in the manuscript.

## Consequence for Theorem 18 and the prime-3 result

Proposition 5.5 of Balakrishnan–Dogra I allows any K-rational smooth basepoint. Apply it at the endpoint b, using (3) for the local scalar comparison and (4) for the global correction. The same basepoint cancellation as in Theorem 18 yields its actual-local-image containment without excluding endpoint basepoints.

For the original reciprocal curve, at b=(0,1) the endpoint values are r_3(b)=h_3(P) and F(b)=h_3(P), while all actual away-from-3 images are zero. Thus the first necessary condition is exactly ρ_3=0. The established second-model containment gives ρ_3^*=0. The uniform disk proof shows their intersection is precisely

\[
 \{(0,1),(0,-1),\infty_+,\infty_-\}.
\]

All four points are rational and hence are in the Mordell–Weil-restricted, actual-local-image depth-two set. Therefore, with that convention,

\[
 C(\mathbf Q_3)_2=C(\mathbf Q)
 =\{(0,1),(0,-1),\infty_+,\infty_-\}.
\]

This proof has received independent review. The conclusion concerns the specified Mordell–Weil-restricted convention, not a relaxed Selmer convention.

## Exact source locations

- Balakrishnan–Dogra I, Definitions 5.1–5.3: finite augmentation path modules, twisting, and pushout by a correspondence functional. The text following Definition 5.3 explicitly permits performing the pushout after twisting because the action on A[2] is trivial.
- Lemma 4.8: algebraicity of the crystalline local height.
- Proposition 5.5: the global height condition for any rational basepoint.
- Section 4.3.3: factorization of the global height through adjacent extension classes.
- Theorem 6.3: the natural path/cycle mixed-extension comparison; Lemma 7.7 supplies the generic bielliptic local formula and is not itself claimed to cover endpoint basepoints.

All are in https://arxiv.org/html/1601.00388 . The double-twist construction and the extension across the endpoint are supplied explicitly above.
