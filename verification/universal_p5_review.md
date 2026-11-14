# Independent review of the universal five-adic residual theorem

## Outcome

The mathematical proof and arithmetic certificate pass independent review. For every a∈5Z₅, with b=(a+5)/5 and the specified orientation and outer-first convention,

    X_a=(1/i)∫_(−i,0)^(i,0)(dx/(2y))(x dx/(2y))=5(a+5)U(b),

where U∈Z₅⟨b⟩ and U≡3 modulo5 coefficientwise. Thus the only zero on this parameter disk is a=−5, and v₅(X_a)=1+v₅(a+5) away from that point.

The review covers the final prose in proofs/universal_five_adic_residual.md, its uniform analytic argument, the complete finite certificate, and the full-depth-two corollary with its stated hypotheses. It does not replace those hypotheses by scalar sufficiency.

## Mathematical checks

1. The endpoint-regular Frobenius lift is valid. H is obtained in the degree-thirty quotient by f_a⁵, with derivative invertible modulo5. Exact monic division gives f_a(H)=f_a⁵V and H′=f_a⁴P. The latter divisibility follows from differentiation and invertibility of f′_a(H) modulo f_a⁴. The lift fixes W± exactly by uniqueness of the simple branch root in its residue disk.

2. The five affine differentials are retained. The extra puncture direction is not silently omitted. Hyperelliptic symmetry kills every single integral, parity closes the six-variable cross system, and integration by parts gives precisely the normalized correction T(K_kB_j−K_jm_k). The differential factor2, path orientation, and conversion X=I_01/i agree with the separately audited fixed-parameter computation.

3. Formal parameter lifting starts at the exact a=−5 solution and uses v=a+5. It does not incorrectly assert that x⁵ is a root over the formal ring modulo5. The implicit derivative is a Z₅-unit at v=0, so H,V,P have integral v-coefficients. Substitution v=5b gives the degree-d valuation gain at least d. The independent divisibilities P,V−1∈5Z₅⟨b⟩ give the maximum bounds in equations (6)–(8).

4. The principal-part reduction loses at most floor(log₅(D−2)). Its parameter-dependent inverse-square-root factors are integral with the same parameter-degree gain, so they do not introduce a second horizontal denominator loss. The bounds max(d,n+1)−L_n and max(d,n+m+2)−L_n−L_m−J_(n+m) are therefore valid coefficientwise.

5. The infinite sums converge in the Tate algebra. The degree-at-least-sixteen coefficients of M and c lie in125Z₅ and tend to zero. This is a Gauss-norm conclusion, not a pointwise conclusion. The fixed-computation certificate retains theoretical D*=2868,L*=4,J*=5 despite smaller modularly trimmed degrees. Finite errors are at least22 digits for M and13 for c; infinite errors are at least17 and7 respectively.

6. The interpolation step is rigorous specifically because of the monic remainder. For Q(b)=∏_(j=0)^15(b−j), every remainder of b^d has integral coefficients. The remainder operator extends continuously to restricted series and does not increase the Gauss norm. The analytic tail in125Z₅⟨b⟩ consequently contributes only a125-integral remainder. It is not treated as an arbitrary pointwise O(125) error. Seven-digit sampled errors lose at most v₅(15!)=3 under interpolation, leaving four coefficient digits. This proves the claimed coefficientwise congruences modulo125.

7. The interpolated M and c have integral coefficients; together with the high-degree bound this proves their integrality in Z₅⟨b⟩. Modulo5 the cross system is I−K with K_50=2 and K²=0. Hence its inverse exists over the Tate algebra itself. The polynomial identity Az=c modulo125 gives X_(5b−5)=75b+125G(b) coefficientwise.

8. The exact automorphism at a=−5 is defined over the unramified quadratic extension with c²=−2. The cleared sextic identity and its holomorphic pullback matrix of determinant1 check exactly. It exchanges the endpoints; zero single periods and shuffle make reversal act by−1. Coleman base change and functoriality therefore give X_−5=0 exactly. Thus G(0)=0, division by b stays in the restricted integral series ring, and the stated unit factorization follows. Vanishing of this coordinate alone is not interpreted as vanishing of the full residual class. The pre-existing CM norm-one-torus argument is separate and already handles full membership there.

## Independent arithmetic reproduction

All sixteen parameters a=5b−5, b=0,…,15, were recomputed using the separately written original independent Frobenius implementation, changing only its parameter literals in memory. For every parameter, all25 Frobenius entries, all6 normalized correction entries, and all6 solved periods agreed with the supplied samples modulo5⁷.

The review then independently reconstructed exact rational Lagrange interpolation using Fraction arithmetic, rather than reusing the author's Newton interpolation implementation. Every coefficient was checked to be5-integral. Every reconstructed M and c polynomial agreed with the universal JSON modulo125.

Finally, direct polynomial arithmetic independently reconstructed all36 system-matrix entries and verified all6 identities Az=c modulo125. This is an identity of polynomials, not a comparison at the sixteen nodes. The first solution polynomial is exactly75b. The supplied standalone standard-library checker was also run and passed, including the exact CM sextic identity, nilpotent matrix reduction, denominator bounds, displayed prime examples, and primitive modulo9 obstruction for a=35.

The audited numerical sample JSON had SHA256 3f1475850fbc508848b83ab0f40c9fcd1e7389a07542cbf2243ad607d95551b1. Replacing only its source-reference metadata with the repository proof path gives the published sample JSON SHA256 d25752c699d7652d01e4a1e93b50669db9360b7f12e2e2443e3537fb7adb0c80; all numerical fields are unchanged. The audited universal-polynomial JSON SHA256 is cc1125e82abe33315ddeb1b727f7eaf45f8644214ddf3671725ab1fbf7f51d0c.

## Global corollary and examples

The six-disk scalar theorem was separately checked at all orders, including the degree-five integration denominators. Endpoint disks satisfy rho/(alpha*x²)∈1+5Z₅; Weierstrass disks satisfy rho/(alpha*y²)≡−2/A² modulo5. These isolate exactly the six scalar centers.

For integral a divisible by5 with a≡3 modulo16, rank E_a(Q)=1, and every odd prime divisor of a−3 congruent to3 modulo4, the established local theorems make the actual residual target zero. Non-CM is automatic: v₂(a+1)=2, and any odd divisor of a+1 gives a negative j-valuation; the only alternatives a=3,−5 violate the simultaneous hypotheses. The uniform nonzero period then removes W±, proving the stated four-point full-depth-two and rational-point equality under the established Selmer convention.

The a=35 rank certificate is independently valid. The E descent image contains classes−1 and−2, represented by (−4,24) and rational two-torsion, and is supported on{±1,±2}; its size is4. The isogenous E′ image is supported on{1,2,3,6}; class2 occurs. The class3 quartic has no primitive solution overQ₃, since modulo3 one of U,V must be divisible by3 and then the right side has valuation exactly1. Thus class3 and, by group closure, class6 are absent, and the image size is2. The standard two-isogeny formula gives rank1. All remaining full-equality hypotheses hold because a−3=32.

No infinitude of the rank-one arithmetic subfamily is asserted. Parameters with nonzero residual targets are not classified by the holomorphic nonvanishing theorem alone.

## Final status

No mathematical defect remains in the reviewed proof or certificate. One wording refinement was requested and applied so that the exceptional parameter is described as a zero of this coordinate, without asserting anything unintended about other coordinates.
