# Independent review of the uniform thirteen-adic residual theorem

## Outcome

The final proof in proofs/universal_thirteen_adic_residual.md and its arithmetic certificates pass independent review. For every a=9+13b with b∈Z₁₃, the normalized holomorphic period satisfies the coefficientwise analytic congruence

    X_a≡13²(9+10b+5b²) modulo13³.

The discriminant −80≡−2 is nonsquare modulo 13, so v₁₃(X_a)=2 for every Q₁₃-valued parameter in this disk. The quadratic is not described as a unit of the whole Tate algebra: it has geometric roots over an unramified quadratic extension. This distinction is retained correctly.

## Independent numerical and polynomial reproduction

All twelve parameters a=9+13b, b=0,…,11, were recomputed using an independent adaptation of the separately written Frobenius implementation. The adaptation used a separately implemented polynomial extended-Euclidean inverse modulo 13, rather than the author's SymPy seed inversion. For every parameter, all 25 Frobenius entries, all 6 normalized correction entries, and all 6 solved periods agree with the supplied samples modulo13⁵.

A separate exact Fraction-based Lagrange interpolation reconstructed all 31 matrix and correction polynomials. Their coefficients are 13-integral, and their residues agree with the universal polynomial JSON modulo13³. Direct polynomial arithmetic independently reconstructed the complete six-by-six system and verified all six equations Az=c modulo13³. This was a coefficientwise polynomial check, not a comparison only at sample points. The first solution polynomial is [1521,1690,845]=169[9,10,5]. Its nonvanishing at all 13 residue classes was also checked independently.

The published standalone standard-library checker was run successfully. A separate exact rational calculation verified all thirteen U, logarithm, and height residues in the scalar argument. The publication sample JSON differs from the original only in status/proof-reference metadata; all numerical entries are identical.

Published sample SHA256: e16c006742bdf7f15ca5818498ec7690eda5a3509dbdbf2b1aba5f197edee8d7.

Published polynomial SHA256: 830a66e843531633177eeb15a7d64dabea4e39f0ba25ad90dd822f5f33aae0e6.

## Analytic and precision checks

For monic degree-six f with squarefree reduction, the Hensel derivative is a unit in the quotient by f^p. The general inverse is required; the special p=5 shortcut is not reused. Exact differentiation and monic division give H′=f^(p−1)P with deg P≤4 and P divisible by p. The pullback exponent f^((p−1)/2), degree bound D_n=27p−3+(30p−6)n, endpoint fixing, and correction formula all check.

At 13, twelve binomial terms and coefficient precision 24 use theoretical D*=4572,L*=J*=3, regardless of effective modular degrees. The scaled horizontal congruence certifies finite M error 18 and finite correction error 12. For omitted terms, the matrix tail is at least 10 digits. The exact inequality (346+384·12)²(692+384·12)=130073214800<13¹⁰ and the successive ratio bound give a correction tail of at least 5 digits for every s≥12. These are uniform whole-series bounds.

Formal lifting in v=a−9 starts at the exact a=9 solution. Integral v-coefficients give the parameter-degree gain after v=13b. Together with P,V−1 divisible by 13, this proves the max(d,n+1) bounds and their bilinear correction version. Every coefficient of degree at least 12 in M,c lies in13³, while the infinite tails have stronger Gauss bounds.

The monic remainder modulo ∏_{j=0}^{11}(b−j) is Gauss-norm nonincreasing on restricted integral series. It preserves the13³-integral high-degree tail. The twelve interpolation denominators are 13-units, so five-digit sampled errors lose no digits. Consequently the interpolation certifies the full coefficientwise congruences, not merely values at twelve nodes.

The interpolated low coefficients and the tail bound prove M,c integral in the parameter Tate algebra. Their constant reduction modulo 13 gives cross-system determinant 11, so inversion is valid over that algebra itself. All five affine cohomology directions, including the puncture direction, remain in the calculation. Hyperelliptic oddness, parity, and shuffle justify the six-variable system and all primitive endpoint terms vanish.

## Scalar and global checks

The final scalar proof uses exact quintuple identities rather than truncated division at a point with an uncontrolled denominator. The formula

    1/(5t₅)−Dlogψ₅(P)/25=−R/(5N)

makes the primitive constant integral even when v₁₃(ψ₅(P)) is arbitrarily large. The proof that ψ₅(P)≠0 for integer parameters, via its value 2 modulo 3 on every integer residue class, is valid. N,Q are units on the specified 13-adic disk.

The exact residues U≡56+52b modulo169, log₁₃(U)/13≡8+b, h/13≡10−2b, and Z≡5 check. Thus outside a≡74 modulo169 the global scalar coefficient has negative valuation and the complete single-/double-primitive estimates isolate exactly six centers. The omitted lift is correctly left undecided by this argument. The entire curve reduction consists of the six displayed points, so no residue disk is missed.

The full four-point theorem retains the rank-one, a≡3 modulo16, and nonsplit odd-prime hypotheses required to make the actual residual target zero. Uniform holomorphic nonvanishing then removes W±; rational containment supplies the four endpoints. No membership is inferred from scalar vanishing alone. The a=35 rank-one example is covered by the independently reviewed two-isogeny descent certificate, giving full equality at both 5 and 13. The weaker rational-point theorem and four-versus-six Selmer dichotomy under a≡3 modulo8 are also valid.

## Final status

The generalized-prime implementation, whole analytic proof, scalar normalization, and exact arithmetic certificate have no outstanding mathematical defect. The result is certified only for the stated p=13 residue disk and numerical parameters, as enforced by the publication interface.
