# Quadratic Chabauty: Mock Rational Points

Research target: explain extra candidates for genus-two curves over the rationals whose Jacobians have Mordell–Weil rank two, starting from [ICM 2026, Problem 6.4](https://doi.org/10.1137/25M1805011).

## Complete rational-CM Weierstrass subcase

The reciprocal family has exactly seven rational parameters with CM elliptic quotient: 0, −3/2, −15/16, −5, 15, −33 and 255. The parameter 0 has Jacobian rank zero; the other six have rank two. For all six rank-two curves, every locally visible Weierstrass point is excluded from the full restricted depth-two set at every odd good prime. The [complete proof](proofs/rational_cm_weierstrass_classification.md) combines the two earlier CM examples with four explicit new torus quotients and elementary rank certificates.

The new comparison also handles potentially nonzero targets in the CM field Q(√−7): actual local Néron metrics force rational S-unit coefficients, and an algebraic logarithm/complex-absolute-value argument separates the candidate from the entire allowed target. This settles a complete finite arithmetic subclass; the non-CM transported Sym² targets and non-Weierstrass classification remain open. Run `python scripts/check_rational_cm_packet.py` for the exact algebra.

## Established here

[PROOF.md](PROOF.md) gives complete arguments for:

- An exact root-of-unity test for Weierstrass points in a specified bielliptic height-candidate set. Once the rational local-height target coefficients are fixed, membership is independent of the good prime except for local visibility.
- A complete rational-factor classification of the Weierstrass part of that height-candidate set: factor the cubic in x² over the rationals, retain only the explicit degree-one, degree-two, or pure-cubic cases, and compare one valuation vector per retained factor with the target. In particular, an irreducible cubic with either middle coefficient nonzero excludes every Weierstrass point at every eligible prime, without a monic-unit assumption.
- A unit obstruction: for a monic even sextic with constant term ±1, a surviving Weierstrass point must have root-of-unity x-coordinate.
- A reciprocal-symmetry mechanism giving non-Weierstrass algebraic candidates on y²=x⁶+a x⁴+a x²+1, whenever the common elliptic quotient has rank one. For odd a, these also pass the actual local-image target for this height function.
- An unconditional rank-two case, y²=x⁶−5x⁴−5x²+1: exact occurrence of (±i,0) and (±1,±2√−2) at their splitting primes, and all-prime exclusion of the other four Weierstrass points. The rank proof uses elementary two-isogeny descent.
- A simultaneous-three-torsion mechanism and its complete parameter classification in the reciprocal family. On the rank-two example, the eight points with 3x⁴−2x²+3=0 are additional exact non-Weierstrass height candidates. A finite-field criterion decides visibility, with an exact Hensel certificate at p=67.
- An exact second-correspondence obstruction for those eight points: a rational change of bielliptic model makes both elliptic images order six, and the second height is −⅓logₚ(t), where t²+10t+1=0. The algebraic-unit obstruction proves that all eight are excluded from the full depth-two set at every eligible prime, despite passing the first height test.
- A degree-eight dihedral coordinate field for the eight-point locus. Local visibility occurs exactly at completely split primes, of natural density 1/8. This density concerns the first-height candidates, not full-depth-two membership.
- Genuine depth-two exclusions: the standard coarse height set contains the full Chabauty–Kim set, so the Weierstrass exclusions transfer to depth two. The four excluded Weierstrass points on the rank-two example are therefore absent from the full depth-two set.

- Exact second heights for the remaining six: the four points with x=±1 have values ±2hₚ(P) for a specified rational CM elliptic point, while (±i,0) give zero. The actual second local target is {0}; CM height nonvanishing excludes the four from this refined height set for visible p≥5. A graph-correspondence proof now establishes full-depth-two containment in this nonmonic actual target, including its endpoints, and upgrades these to four further depth-two exclusions.

- An explicit anti-CM torus obstruction excludes the remaining pair (±i,0). The proof constructs the global lift and compares its local fiber directly, rather than inferring full membership from scalar heights or assuming elliptic-height nonvanishing at inert primes.

The original example points were already observed by Finnerty. These arguments prove exact membership and exclusion rather than identify points from finite-precision approximations; the underlying logarithm-kernel technique is credited to Bianchi. No unverified priority claim is made.

Depth-two statements here use the Mordell–Weil abelian-image condition of Balakrishnan–Dogra Definition 2.2. They do not identify an unrestricted global Bloch–Kato group with Mordell–Weil points merely from the rank.

## Complete special case at p=3

For y²=x⁶−5x⁴−5x²+1, Theorem 21 proves C(Q₃)₂=C(Q)={(0,±1),∞±}, in the explicitly stated Mordell–Weil-restricted, actual-local-image convention. The proof combines an exact h₃(P)≡2 mod3 certificate, uniform estimates over all eight residue disks, and an endpoint-basepoint mixed-extension bridge. Both analytic and bridge arguments received independent review. Full proofs are in [proofs/](proofs), with reports in [verification/](verification).

## General sufficient family criterion

Theorem 22 extends the p=3 argument to C_a:y²=x⁶+a x⁴+a x²+1 with a≡−5 mod5832, subject to an independently verified rank-one elliptic quotient and an explicit prime-factor valuation condition. A squarefree odd part of |a+1| is a simple sufficient target condition. The full exact local-target formula, including nonzero-target cases, is proved in [proofs/reciprocal_local_targets.md](proofs/reciprocal_local_targets.md).

Theorem 23 verifies every hypothesis for a=−157469, proving another exact equality C_a(Q₃)₂=C_a(Q)={(0,±1),∞±}. The rank certificate is elementary two-isogeny descent, with a separate exhaustive primitive-pair checker. The family theorem does not assert infinitely many rank-one parameters or solve the general classification problem.

## Rank certificates and primes 7 and 11

Theorem 24 replaces the rank assumption on two explicit subfamilies by prime-factor and congruence tests, with ten exact examples. It makes no infinitude claim. Theorem 25 proves first-height isolation in two p=7 parameter neighborhoods, yielding full restricted depth-two equality once rank one and the stated mod 8 condition hold. Verified members include a=−5, −2033309 and −605; no a+1 multiplicity condition is needed at 7.

Theorem 26 also proves full equality for a=−157469 at p=11. Its first height has eight zeros, and the second removes the four nonrational centers. All proofs have independent audits and full-series bounds. The small-disk supplement precisely limits the present method; it is not a classification at every prime.

## Uniform endpoint-only families

Theorem 27 broadens the four-disk argument to odd a≡4 mod7 excluding 46 mod49, odd a≡2 mod11 excluding 24 mod121, and every odd a divisible by 19. In each locus the first scalar height has only the four endpoint zeros. With a≡3 mod8 and rank one, these are also the full restricted depth-two sets. The excluded lifts are not claimed to fail.

Exact rank certificates give a=−18269 at 11 and a=−17309, −3474245 at 19. Full proof and review accompany the standalone SymPy checker scripts/check_endpoint_families.py. These integral endpoint criteria assert neither infinitude in their parameter loci nor a complete general classification.

## Infinitely many rational rank-two members

Theorem 28 transfers Zywina's existing rank-one specialization theorem to this reciprocal family through an explicit two-isogeny and Möbius change of parameter. It proves infinitely many rational a∈(−1,3) with elliptic rank one and Jacobian rank two, including infinitely many geometric curve isomorphism classes.

This is not an infinitude theorem for integral parameters or for full depth-two endpoint equalities. Denominator-prime local targets remain a separate issue. See [the proof and source](proofs/rational_rank_infinitude.md).

## Exact four-or-twelve scalar classification

Theorem 29 completes the first-height zero classification in every case with four rational reduction points. At 7 and 11 an explicit p-adic squareclass criterion decides whether there are four or twelve zeros; at 19 there are always four. The proof controls all series terms and includes exact twelve-zero examples.

These additional zeros are not asserted to lie in the full depth-two set. Full-set conclusions retain the separate rank and local-target assumptions. See [the criterion and proof](proofs/endpoint_bifurcation.md) and scripts/check_endpoint_bifurcation.py.

## Eight scalar extras excluded from full depth two

Theorem 30 evaluates the second height on the previously omitted endpoint lifts. Its unit linear term excludes every noncentral second-height zero. Under rank one, a≡3 mod8 and zero second actual target, the full endpoint conclusion now holds throughout a≡4 mod7 and a≡2 mod11.

For the rank-certified curve a=−14974109 at7, the first scalar has twelve zeros, but the second removes all eight extras and the full restricted depth-two set is exactly the four rational endpoints. The [complete proof](proofs/second_height_endpoint_exclusion.md) and independent degree20 checks establish this beyond a first-height candidate calculation.

## A second non-scalar CM obstruction

Theorem 31 proves that the locally visible pair (±i,0) on a=15 is excluded from full depth two at every p≡1 mod4, despite vanishing in both earlier scalar expressions. An explicit norm-one-torus quotient detects the nonzero Kummer class of −7+4sqrt(3).

The proof includes a rank certificate, exact degree-three CM map, complete fiber-divisor calculation and the corrected proper-reference sign. It treats both split and inert CM primes. This is a second unconditional example, not a general non-CM classification. See [the proof](proofs/cm15_torus_exclusion.md).

## Scope and open questions

The positive membership results concern explicitly defined single-height candidate sets, not general characterizations of the full depth-two Chabauty–Kim set. Theorem 21 separately gives a complete characterization for this specific curve at p=3. The exclusion results do transfer to the full set when the standard coarse target is used, by the known containment detailed in PROOF.md. A second correspondence now excludes the eight-point locus above. The four points (±1,±2√−2) are now excluded from depth two for visible p≥5 by the proved nonmonic refined-target containment. The independent exact prime-3 certificate now covers p=3 as well. The two points (±i,0) pass both earlier scalar height tests but are now excluded at every visible odd prime by an explicit norm-one-torus quotient. A global reference path is constructed using two proper elliptic curves; its local discrepancy is the nonzero Kummer class of a unit built from 1+√2. This covers both split and inert CM primes. Together, all fourteen specified nonrational first-height candidates are excluded at every odd prime whenever locally visible. The general classification of non-Weierstrass candidates remains open.

## Checking the algebra

The proofs do not require numerical p-adic computation. Optional exact polynomial checks, using Python and SymPy:

```sh
python scripts/check_identities.py
```

This verifies the derivative cancellation, reciprocal identities, discriminants, factorization, the descent witness, and the rational-power identities used in the factor classification, the simultaneous-three-torsion resultant, the exact local-visibility certificate, the dihedral-field norm identities, and the six-torsion second-height calculation, the CM isogeny/twist maps, the remaining local-target arithmetic, and the anti-CM divisor factors and exact nontrivial-unit values. It is not a substitute for the mathematical proofs.


Additional exact prime-3 checks (standard library only):

```sh
python scripts/check_prime3_height.py
python scripts/check_prime3_six_multiple.py
```

These scripts include independently derived 3P and 6P certificates. The proofs provide the bounds for every omitted term; zero or nonzero claims are not inferred from unexplained finite precision.


General-family and new-rank certificates (standard library only):

```sh
python scripts/check_general_prime3.py
python scripts/check_rank_one_parameter.py
python scripts/check_rank_one_independent.py
```

The rank checker reads the included `verification/rank_one_obstructions.txt`. The general analytic checks alone do not certify rank or actual local targets; those are separate proofs.


Further exact checks (standard library only):

```sh
python scripts/check_rank_patterns.py
python scripts/check_rank_patterns_independent.py
python scripts/check_prime7.py
python scripts/check_prime7_independent.py
python scripts/check_prime7_four_disks.py
python scripts/check_prime11.py
python scripts/check_small_disks.py
```

The scripts supplement the proofs; finite residues alone are not used to assert analytic identities.

## Rational denominator targets

Theorem 32 computes both actual local targets at every odd denominator prime: the second vanishes, while the first can exclude zero. It also proves the necessary +(1/2)log_p(D) correction to the global point height. See [proof](proofs/rational_denominator_targets.md), [independent review](verification/rational_denominator_review.md), and [exact checks](scripts/check_rational_denominators.py). This does not assert general full-depth-two membership.

Theorem 33 strengthens rational rank-one infinitude: infinitely many geometrically different curves also have zero second actual target at every good odd prime. A prescribed neighborhood a near -5 at any fixed odd p can be imposed. See [proof](proofs/infinite_zero_second_target.md), [review](verification/infinite_second_target_review.md), and [checks](scripts/check_infinite_second_target.py). First targets, denominator height shifts and full-depth-two conditions remain unresolved in general.

## General non-CM depth-two structure

Theorem 34 proves unconditional strict Sym² Selmer vanishing, an isomorphism from relaxed residual classes to their bad-prime restrictions, and exact ordinary/crystalline gluing of the Tate and residual quotients. The resulting full criterion retains joint same-point local images and a compatible global Tate lift. See [proof](proofs/noncm_residual_gluing.md) and [independent audit](verification/noncm_residual_gluing_review.md). The residual discrepancy and surviving joint images remain to be computed; general non-CM membership is not claimed solved.

## Actual exclusions for infinitely many non-CM curves

Theorem 35 excludes all six Weierstrass points and four x=±1 symmetry points, whenever locally visible, for an unconditional infinite rank-two genus-two family at every explicitly eligible odd prime. The key is a distinguished denominator prime with a nonzero first actual target, together with an archimedean argument for the other four Weierstrass points. See [proof](proofs/infinite_weierstrass_exclusion.md), [review](verification/weierstrass_exclusion_review.md), and [checks](scripts/check_weierstrass_exclusion.py). This does not compute the residual Sym² class or classify all other local points.

## Exact odd residual local images

Theorem 36 computes the actual Sym² and joint Tate/Sym² images at every odd prime dividing a-3. Primes 3 modulo4 contribute zero; primes1 modulo4 contribute an explicit finite nonzero segment with coefficients determined by v_q(a-3). The full Tate projection vanishes there. See [proof](proofs/odd_bad_residual_images.md), [independent review](verification/odd_bad_residual_review.md), and [checks](scripts/check_odd_bad_residual.py).

The stable model also classifies all odd good-reduction primes. Thus Theorem35's infinite-family ten-point exclusions hold at every odd good prime. The actual dyadic image is now settled below; the general global residual comparison remains unresolved.

## Compatible Tate lifting is settled for the integral family

Theorem37 proves that, for integral a=3 modulo8 with non-CM rank-one quotient and odd good p=1 modulo4, the common Tate class of (±i,0) has a unique compatible global lift with zero bad-local coordinates. Full depth-two membership of the pair is therefore equivalent to the residual Sym² finite-target criterion. See [proof](proofs/integral_tate_lift.md) and [independent audit](verification/integral_tate_lift_review.md). The actual dyadic image is zero throughout this family, as recorded below; nonzero transported odd residual targets remain to be compared.

## Dyadic residual cohomology vanishes for odd v₂(a−3)≥5

Theorem38 proves H¹(Q₂,Sym²Vp(E_a))=0 for every odd p in this integral subfamily, with no rank or non-CM hypothesis for the local result. Together with the two zero Tate coordinates, the entire actual dyadic joint image is {(0,0)}. See [proof](proofs/dyadic_residual_vanishing.md), [checks](scripts/check_dyadic_residual.py), and [independent audit](verification/dyadic_residual_review.md).

Combined with Theorems36–37 under their global hypotheses, this leaves only the explicit odd residual targets. For a=-605 the pair criterion is δp(W)=0; for a=-157469 the target has at most three values, {0,±Θp(e37)}. The five-adic period theorem below now excludes the pair for −605. Theorem39 settles even dyadic valuations, and the subsequent actual-image theorem also covers v₂(a−3)=3.

## All dyadic valuations at least four, and a global discrepancy class

Theorem39 extends dyadic residual vanishing to every v₂(a−3)≥4, equivalently the integral subfamily a≡3 modulo16 (a≠3). The even case uses an exact biquadratic splitting-field and Hensel-deformation proof, independently checked. See [proof](proofs/dyadic_even_valuation.md), [checker](scripts/check_dyadic_even.py), and [audit](verification/dyadic_even_review.md).

Theorem40 constructs a global class ηp in the quadratic twist Sym²Vp(E)⊗χ₋₄ whose p-localization is δp(W). For −605, ηp is provably nonzero because it is ramified at19. Its localization at5 is now also proved nonzero by the period certificate below. Full membership at other eligible primes retains the criterion locp(ηp)=0. A dimension argument rules out blanket localization injectivity for parameters with at least two odd prime factors of a−3. See [proof](proofs/twisted_discrepancy_descent.md) and [audit](verification/twisted_discrepancy_review.md).

## Uniform periods and the actual dyadic image

The [actual dyadic-image theorem](proofs/dyadic_actual_images.md) gives Xi₂={(0,0)} throughout a≡3 modulo8, including v₂(a−3)=3. It does not claim that the whole local cohomology group vanishes in that case.

The [uniform five-adic theorem](proofs/universal_five_adic_residual.md) gives the exact factorization X_a=5(a+5)U((a+5)/5), with U≡3 modulo5. Its only zero is a=−5, already handled by the CM torus argument. The regular Frobenius calculation for −605 has been recomputed: the first normalized coordinate is21625 modulo5⁷, of valuation3. For integral a≡3 modulo8 with 5|a and rank E_a(Q)=1, the [Selmer dichotomy](proofs/five_adic_selmer_dichotomy.md) proves exactly four rational points and either four or six full depth-two points. There are exactly four when every odd prime dividing a−3 is3 modulo4.

The prime-thirteen results also include the [critical lift](proofs/prime13_critical_lift.md) and [nonzero second scalar targets](proofs/prime13_nonzero_second_targets.md). These scalar-target results do not evaluate the general nonzero transported Sym² target.

## A degree-ten reduction for the remaining adjoint computation

For the actual nonzero-target example a=−157469, the [quintic-reduction theorem](proofs/adjoint_quintic_reduction.md) identifies unrestricted S-ramified H¹(Q,ad⁰(E[5])) with the anti-invariant mod-five ray-class characters of an explicit degree-ten field. It uses a five-point module and the published Fernández–Lario modular resolvent, avoiding construction of the degree-120 projective splitting field.

Run `python scripts/check_adjoint_quintic.py` for the exact representation and field identities. The optional PARI script `scripts/compute_adjoint_ray.gp` and Hecke/Nemo alternative `scripts/compute_adjoint_ray.jl` attempt the ray-class computation. Both check the exact field and involution; the Hecke route uses sparse relations and automorphisms, and requires unconditional class and unit certification before labeling the ray dimension certified. No degree-ten dimension has yet been certified. Propagated finite/crystalline local conditions, δ₅(W) versus {0,±Θ₅(e₃₇)}, and the original general problem remain unresolved.

For Hecke 0.41.1, `ADJOINT_LARGE_PRIME_FIX=1` enables a version-checked
workaround for mismatched large-prime cache keys and a duplicate-base
quotient error. Installed package files are not changed.
`scripts/check_hecke_large_prime.jl` reproduces the cache miss, then checks
the repaired principal-ideal relation and cancellation of repeated bases.

Long runs can set `ADJOINT_FACTOR_BOUND` and
`ADJOINT_RELATION_CHECKPOINT=build/adjoint.relations`. The latter writes
exact factored elements atomically before expensive lattice-index work,
after each 256 additional relations or the first full-rank observation.
Resume with `ADJOINT_RELATION_RESUME=build/adjoint.relations`; the field
and discriminant are checked and every saved element is re-factored.
The saved bound must match any explicitly supplied bound. Saved rank and
index values are never accepted as a class-group certificate.
`scripts/check_hecke_relation_checkpoint.jl` checks a round trip on
Q(sqrt(5)) and completes an unconditional class-group calculation after
restoration. These changes improve reproducibility of the remaining
calculation; they do not establish its dimension or the local target test.
