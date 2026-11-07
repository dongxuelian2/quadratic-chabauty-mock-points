# Quadratic Chabauty: Mock Rational Points

Research target: explain extra candidates for genus-two curves over the rationals whose Jacobians have Mordell–Weil rank two, starting from [ICM 2026, Problem 6.4](https://doi.org/10.1137/25M1805011).

## Established here

[PROOF.md](PROOF.md) gives complete arguments for:

- An exact root-of-unity test for Weierstrass points in a specified bielliptic height-candidate set. Once the rational local-height target coefficients are fixed, membership is independent of the good prime except for local visibility.
- A complete rational-factor classification of the Weierstrass part of that height-candidate set: factor the cubic in x² over the rationals, retain only the explicit degree-one, degree-two, or pure-cubic cases, and compare one valuation vector per retained factor with the target. In particular, an irreducible cubic with either middle coefficient nonzero excludes every Weierstrass point at every eligible prime, without a monic-unit assumption.
- A unit obstruction: for a monic even sextic with constant term ±1, a surviving Weierstrass point must have root-of-unity x-coordinate.
- A reciprocal-symmetry mechanism giving non-Weierstrass algebraic candidates on y²=x⁶+a x⁴+a x²+1, whenever the common elliptic quotient has rank one. For odd a, these also pass the actual local-image target for this height function.
- An unconditional rank-two case, y²=x⁶−5x⁴−5x²+1: exact occurrence of (±i,0) and (±1,±2√−2) at their splitting primes, and all-prime exclusion of the other four Weierstrass points. The rank proof uses elementary two-isogeny descent.

The example points were already observed by Finnerty. These arguments prove exact membership and exclusion rather than identify points from finite-precision approximations; the underlying logarithm-kernel technique is credited to Bianchi. No unverified priority claim is made.

## Open question

The results concern explicitly defined single-height candidate sets, not a characterization of the full depth-two Chabauty–Kim set. Additional independent correspondences, especially for a Jacobian isogenous to an elliptic square, remain to be analyzed. The general classification of non-Weierstrass candidates remains open.

## Checking the algebra

The proofs do not require numerical p-adic computation. Optional exact polynomial checks, using Python and SymPy:

```sh
python scripts/check_identities.py
```

This verifies the derivative cancellation, reciprocal identities, discriminants, factorization, the descent witness, and the rational-power identities used in the factor classification. It is not a substitute for the mathematical proofs.
