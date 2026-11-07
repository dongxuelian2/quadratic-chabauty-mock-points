# Quadratic Chabauty: Mock Rational Points

Research target: explain extra candidates for genus-two curves over the rationals whose Jacobians have Mordell–Weil rank two, starting from [ICM 2026, Problem 6.4](https://doi.org/10.1137/25M1805011).

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

The original example points were already observed by Finnerty. These arguments prove exact membership and exclusion rather than identify points from finite-precision approximations; the underlying logarithm-kernel technique is credited to Bianchi. No unverified priority claim is made.

## Open question

The positive membership results concern explicitly defined single-height candidate sets, not a characterization of the full depth-two Chabauty–Kim set. The exclusion results do transfer to the full set when the standard coarse target is used, by the known containment detailed in PROOF.md. A second correspondence now excludes the eight-point locus above. Full-depth-two membership of (±i,0) and (±1,±2√−2), and any remaining correspondence conditions, is unresolved. The general classification of non-Weierstrass candidates remains open.

## Checking the algebra

The proofs do not require numerical p-adic computation. Optional exact polynomial checks, using Python and SymPy:

```sh
python scripts/check_identities.py
```

This verifies the derivative cancellation, reciprocal identities, discriminants, factorization, the descent witness, and the rational-power identities used in the factor classification, the simultaneous-three-torsion resultant, the exact local-visibility certificate, the dihedral-field norm identities, and the six-torsion second-height calculation. It is not a substitute for the mathematical proofs.
