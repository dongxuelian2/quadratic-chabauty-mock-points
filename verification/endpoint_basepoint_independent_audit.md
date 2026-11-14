# Independent audit of the endpoint-basepoint bridge

Reviewed on 2026-11-07, after the separate analytic audit in `../verification/prime3_independent_audit.md`. Primary artifact: `../proofs/endpoint_basepoint_bridge.md`, not the earlier incomplete candidate. Pre-publication reviewed proof SHA-256 (publication changes only relative links and review-status prose): `2d865db2424a42a7f4227086b10080335cbf738eadf7ff7ffa5d9b041a783343`.

## Verdict

**The bridge is mathematically sound, with the generic-field justification below making its adjacent-extension comparison precise.** I find no remaining endpoint-basepoint obstruction to combining this bridge with the audited prime-3 disk isolation. The conclusion is for the stated Mordell–Weil-restricted, actual-local-image depth-two convention only.

The original proof correctly retains the nonzero linear correction at the endpoint. Its double-twist construction is a construction on the whole proper curve, not an attempted continuation of a punctured-curve path torsor.

## 1. The double twist is an actual representation

Put \(A=A_2(a)\), so \(I^3=0\), and \(K_Z=\ker\xi_Z\subset I^2\). Every group-like element is \(1+i\), with \(i\in I\). For \(k\in I^2\), both \(ik\) and \(ki\) vanish. Consequently left multiplication and inverse right multiplication fix \(I^2\), preserve \(K_Z\), and act on \(M=A/K_Z\).

The order of the right factor is correct. Applying \((g_b',g_z')\) and then \((g_b,g_z)\) sends \(m\) to

\[
g_zg_z'm(g_b')^{-1}g_b^{-1}
=(g_zg_z')m(g_bg_b')^{-1}.
\]

Thus this is a homomorphism from the product group, not an antihomomorphism. It preserves the filtration and is trivial on its graded pieces. It is Galois equivariant.

Choose paths \(p_b:a\to b\), \(p_z:a\to z\). The coordinate map \(m\mapsto p_zmp_b^{-1}\) identifies loops at \(a\) with paths from \(b\) to \(z\). If \(c_b(\sigma)=p_b^{-1}\sigma(p_b)\) and similarly for \(c_z\), the transported Galois action is exactly

\[
m\longmapsto c_z(\sigma)\sigma(m)c_b(\sigma)^{-1}.
\]

This proves the claimed identification of the double twist with the path module, including its source endpoint. It does not merely compare two unrelated modules using a common torsor. Ambiguities in transport are inner conjugations, which are trivial on \(I^2/I^3\), so the fixed functional really does transport canonically.

## 2. Joint local regularity and local comparison

The two fixed-basepoint Kummer maps followed by this algebraic double action give the required family of mixed-extension classes. At a good p-adic place, all representations and relevant torsors are crystalline; composition with the algebraic crystalline height is locally analytic. Away from p, the two Kummer maps are locally constant, so their image under any well-defined twisting and height map is locally constant.

The generic local comparison is an equality on a Zariski-open subset of the two-variable local space. Its complement has no local interior. Both sides have continuous extensions, including the explicitly regularized endpoint values of \(r_v\). Density therefore extends the equality to every pair. No sequence of rational curve points, or assumption about their abundance, occurs.

The source checks used here are Balakrishnan–Dogra I, Definitions 5.1–5.3 and the algebraic twisting discussion, Lemma 4.8, and Proposition 5.5. The first supplies the finite path-module pushout, the second the algebraic crystalline height, and the last permits arbitrary smooth rational basepoints. Source: <https://arxiv.org/html/1601.00388>.

## 3. Precise generic-field proof of the adjacent-extension step

The only delicate expository step in the submitted bridge is promoting the comparison of adjacent extensions to a comparison over all of \(S=C\times C\). Merely knowing separately chosen isomorphisms at many rational fibers would not prove this. The following argument does.

Let \(F=K(S)\). The two projections of the generic point of \(S\) define \(F\)-rational points \(b_\eta,z_\eta\) of \(C_F\); they satisfy all generic support-separation conditions. Apply the cycle/path comparison to these points over \(F\).

This is legitimate: the geometric construction is over a characteristic-zero field, and its proof uses étale cohomology, cycle classes, exact sequences, and pushouts. It does not require a number-field height or a finite arithmetic place. Section 6.3 explicitly states the characteristic-zero-field setting for its input comparison. Theorem 6.3 then gives the corresponding comparison of the adjacent Galois extensions at this generic point, with its fixed graded identifications and duality conventions.

Both adjacent path-module extensions are already lisse on all of \(S\), by the fixed double-twist construction. Both proposed Kummer extensions are also lisse there: they are pullbacks, under the two globally defined divisor-class maps to \(J(C)\), of the universal Kummer extensions. Since \(S\) is normal and integral, the natural map

\[
G_F\longrightarrow\pi_1(S)
\]

is surjective. An intertwiner of their generic representations is consequently an intertwiner of their \(\pi_1(S)\)-representations. The generic comparison therefore extends uniquely to \(S\), including all endpoint and diagonal fibers. This argument does not need a separately assumed relative version of the full mixed-extension theorem at colliding supports.

The revised bridge now includes this generic-field argument; I inspected the insertion. It proves the needed family step and leaves no additional hypothesis at that point.

## 4. Endpoint global correction: the linear term is essential

For \(a=(0,1)\), the divisor-class value at the diagonal is

\[
[D_Z(a,a)]=2[a-\iota a],
\]

because \(D_\infty-D_0\) is principal. Thus the lower extension does **not** become zero merely because the second elliptic image is the origin.

Writing \(q_1=P_1-P\) and \(q_2=P_2\), the global correction is

\[
h_1(q_1)+2\langle q_1,P\rangle-h_2(q_2)
=h_1(P_1)-h_1(P)-h_2(P_2).
\]

The submitted proof includes this term correctly. The specialized divisor identity also holds with the correct multiplicities: \(\phi_1^*(-P)=2\iota a\), while \(\phi_2^*O=D_0\). Inserting these in the stated pullback identity yields exactly the endpoint divisor, so no missing factor of two or principal correction arises.

On the rank-one elliptic factors, the displayed polynomial is \(F(z)-F(a)\) on the entire Mordell–Weil vector space. This is not an interpolation based on the finite rational-point set. Its endpoint constant is \(F(a)=h_3(P)\), equal to the regularized local value \(r_3(a)\). The actual away-from-3 values are zero. The cancellation therefore gives precisely \(\rho_3=0\), with no extra target constant.

## 5. Result after combination

The bridge supplies the first actual-target necessary condition at the rational endpoint basepoint. The already established second-model construction supplies the second condition. The independently audited uniform analysis gives their intersection as the four rational points, and rational-point containment gives the reverse inclusion. Hence the combined argument proves

\[
C(\mathbf Q_3)_2=C(\mathbf Q)
=\{(0,1),(0,-1),\infty_+,\infty_-\}
\]

for the specified restricted Selmer convention. This audit does not assert the analogous result for an unrestricted Bloch–Kato abelian-image convention, or at every other prime. No repository or published manuscript was changed.
