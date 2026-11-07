# Independent review: dyadic residual vanishing

## Outcome

Approved after independent rederivation and final artifact review. One bibliographic correction was required: Silverman's printed pages are 195, 197, and 201–202. This correction is incorporated in the proof.

## Checks

- Recomputed the Weierstrass invariants and the exact third-division-polynomial substitution.
- Checked that each lower coefficient has valuation exactly 3/2 for every odd B and every c divisible by 8, giving root valuation 3/8 and inertia transitivity on all four 3-torsion lines.
- Verified the subgroup argument inside SL2(F3): transitivity forces the quaternion wild-inertia image.
- Checked transport through the common good special fiber, faithfulness on all odd-p Tate modules, and absolute irreducibility, including coefficient prime 3.
- Verified both the local-duality proof and the alternative direct wild-inertia inflation-restriction proof.
- Verified scaling for n=4k+1 and quadratic twisting plus scaling for n=4k+3, covering every odd n>=5. Sym² is unchanged by the twist.
- Ran the exact symbolic checker successfully. A separate standard-library checker also passed 544 rational polynomial expansions, exhaustive subgroup checks, and scaling checks for odd n from 5 through 39.
- Opened both cited reference PDFs and checked the relevant statements. The specialized argument is explicit in the proof rather than delegated to a reference.

## Limits

The local cohomology result needs neither a rank-one nor a non-CM assumption. The full depth-two membership equivalence still uses Theorem37's global hypotheses and its stated Selmer convention. The joint-image conclusion also uses the previously audited independence and vanishing of the two Tate-height coordinates.

The cases n=3 and even n are not proved here. The discrepancy delta_p(W) and global transport Theta_p are not evaluated. A target {0,±Theta_p(e_37)} has at most three elements, since injectivity of Theta_p has not been established. No general classification, new pair exclusion, or rank claim for unverified parameters follows merely from this local result.
