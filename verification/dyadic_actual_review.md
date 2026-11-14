# Independent review of the actual dyadic image theorem

## Outcome and scope

The proof in [dyadic_actual_images.md](../proofs/dyadic_actual_images.md) passes independent review. For every smooth reciprocal curve with a∈Z₂, a≡3 modulo8, and every odd coefficient prime p, the actual residual image is zero. Together with the previously established two independent Tate coordinates, its same-point joint image is Xi₂={(0,0)}.

The conclusion concerns actual point images. It does not assert H¹(Q₂,Sym²V_pE_a)=0. No global rank, rationality of a, geometric non-CM hypothesis, or restriction v₂(a−3)≥4 is used. The singular parameter a=3 is explicitly excluded.

## Explicit domains and the primary path lemma

I checked the residue exclusions: unit x gives f_a(x)≡8 modulo16, and v₂(x)=1 gives f_a(x)≡5 modulo8. Hence integral rational points have x∈4Z₂. The binomial square root of f_a(4t) is overconvergent: its n-th term has valuation at least 3n−v₂(n!)≥2n+1 and degree at most6n. The two graphs are admissible affinoid closed disks because 2s(t) is invertible over Q₂. Reciprocity supplies the other two disks. These four domains exhaust rational points, without asserting a cover of every geometric point.

I independently opened the primary source, L. A. Betts, *Local constancy of pro-unipotent Kummer maps*, [arXiv:2203.03701v2, Section2, Lemma2.2 and the following proof of Theorem1.1](https://arxiv.org/html/2203.03701v2#S2). It supplies a Galois-fixed prime-to-residue-characteristic path on a whole closed polydisc and explicitly transfers that path to the algebraic curve and its unipotent Kummer torsors. This is exactly the whole-disk statement required here, not merely unspecified neighborhood-local constancy.

## Central fiber and endpoint transport

The rationalized odd-p abelian Kummer map at2 is zero: the local Jacobian has an open pro-2 subgroup, and its p-adic completion is finite. Finite local p-power torsion gives H⁰(Q₂,H)=0. The nonabelian cohomology sequence therefore identifies the zero-abelian fiber injectively with H¹(Q₂,R); each point has a unique central class.

The basepoint-preserving involution g₁=(-x,y) fixes the other finite center and acts by−1 on R, forcing that center's class to zero. Its path torsor is therefore trivial, so a Galois-invariant U_R path between the two finite centers exists.

The transported action of g₂=(-x,-y) at infinity was checked independently. In the infinity chart (t,z)=(1/x,y/x³), g₂ acts as(-t,z), fixing each infinity center. Applying g₂ to a path and composing with the fixed path between finite centers gives a Galois-equivariant semilinear self-isomorphism of the original infinity path torsor. The transported group automorphism acts by−1 on R, since hyperelliptic inversion acts by+1 in degree two and inner transport acts trivially on the center. Naturality of the injective central-fiber map then forces each infinity class to equal its negative and hence to vanish. No unsupported assertion that the transported automorphism has order two is needed.

All four disk centers thus have residual class zero, and exact disk constancy proves the actual-image theorem. The established zero Tate coordinates and ordinary fiber-product gluing with H⁰(H)=0 prove the joint-image assertion.

## Arithmetic consequences and executable checks

The weakening from a≡3 modulo16 to a≡3 modulo8 in the stated full-set applications is valid while retaining their rank, odd-prime and scalar hypotheses. It is not a blanket removal of the residual-target conditions. The known CM parameter a=−5 remains governed by its separate norm-one-torus argument.

The valuation-three examples a=−965 at5 and a=−69 at13 satisfy the cited quadratic rank pattern: n=11 or3, respectively, and n and 2n²−1 are prime. Their odd residual support is nonsplit; a=−69 has the required noncritical prime-13 residue. These arithmetic claims were independently checked.

The standalone [checker](../scripts/check_dyadic_actual_images.py) was run and passed. It checks complete residue exclusions, binomial bounds, the infinity-chart involution, and the example arithmetic. The whole-series, Galois-path and central-fiber arguments are proved in the text and are not inferred from finite testing.

Related established results are [the reciprocal local targets](../proofs/reciprocal_local_targets.md), [the uniform five-adic theorem](../proofs/universal_five_adic_residual.md), and [the uniform thirteen-adic theorem](../proofs/universal_thirteen_adic_residual.md).

## Final status

The final proof and executable checks have no outstanding mathematical defect. The distinct ambient n=3 cohomology classification is not used or included in this review.
