# Independent review of the four-or-twelve scalar classification

Baseline: uniform_endpoint_families.md, reviewed at commit 8a97b6c49cf056e47316c1ada9743088fc5f3b49.

The endpoint coefficients were first derived by expanding the regularized finite and singular heights. An independent derivation then used the exact z=x² pullback primitives V,W,K,R,T. Both give
kappa=1−Z+alpha(1−ell),
b=(aZ−1−2a)/4+alpha(a ell/4−1/4−a/3),
with both y branches handled explicitly.

The coefficient bound v_p(c_n)≥−2 floor(log_p(2n)) was checked term by term in that primitive expression. For p≥7 it gives a restricted integral tail after rescaling z=p²w. The contraction is valid on the entire residue disk. In the only cases where kappa can have positive valuation, b≡4 is a square unit, so the unique z-root has the squareclass of −kappa. This proves the exact count and multiplicities, not just a numerical approximation.

Independent exact group-law arithmetic verified every omitted-lift residue at 7 and 11. The three twelve-zero examples were computed twice: first using the minimal sufficient formal terms, then by independent coefficient generation through degree sixteen. Both routes agree. The complete checker was rerun after consolidation and passes. Its output is recorded separately.

The finite-field enumeration, together with Hasse and the additional points at ±sqrt(−1) for p≡1 mod4, verifies that the classification covers every four-point good reduction in this family, but not other residue-disk layouts.

The examples' additional points are described as nonendpoint, not automatically nonrational. Their rank-one condition is not certified. Four-zero full-depth-two consequences retain the separate rank, local-target and Mordell–Weil-image assumptions. Twelve scalar zeros give only a conditional upper bound of twelve for that restricted depth-two set, not proof of membership.
