# Verification of the uniform endpoint-only families

## Sources and integration

The companion proof consolidates the complete prime-19 argument with the independently reviewed broadened prime-7/prime-11 arguments.

The integration makes the branch sign explicit throughout, uses a family-wide title, corrects the script dependency description to require SymPy, and removes dependence on a working-directory-relative sibling import. The checker is standalone.

## Independent review of the 7 and 11 families

The review confirmed:
1. Independent exact doubling gives the stated psi4, U and primitive rational expressions. Direct group-law checks covered all eleven residue lifts and parameters a=2+11^s for 1≤s≤6.
2. The first height digit is (U^10−1)/11≡9+k for a=2+11k modulo121; the omitted lift is exactly a≡24 modulo121.
3. The denominators are units, v11(ell)=v11(a−2), Z is integral, and the asserted lifts have v11(h)=1. No parameter-continuity assertion is needed.
4. Independent tripling over all seven lifts verifies the p7 formulas and digit 6(1+k). The omitted lift is exactly a≡46 modulo49.
5. Factored-alpha endpoint domination is valid for arbitrary negative alpha valuation. Integration bounds concern evaluated series; finite coefficients need not be integral.
6. The multiplication normalization is lambda(mP)=m²lambda(P)−2log psi_m(P), with zeta(P)=zeta(mP)/m−Dlog psi_m(P)/m².
7. Full-set assertions retain rank one, the actual first target {0}, the endpoint-basepoint containment and the Mordell–Weil abelian-image convention.

The review requested that the negative branch be displayed literally: I=L(f1)−epsilon ell and cross term −2epsilon ell I/x². This correction is implemented in Section 3 of the consolidated proof. It does not alter any valuation.

## Independent review of the 19 family

A separate check of the complete proof verified:
- The formal equation u=t²(1+Au−Au²), integral even differentials and single-/double-integration denominator bounds.
- Exact tripling and both rational cancellations, now additionally verified as generic symbolic identities in the consolidated checker.
- For arbitrary s=v19(a)≥1, t3 has valuation s, ell/a≡1/6, U≡8 mod361, h/19≡17 and Z∈19^s Z19.
- 8^18≡172 mod361 and the logarithm tail bound v((U^18−1)^k/k)≥2 for every k≥2.
- The sign-correct endpoint identity and strict domination after dividing by alpha, including s>1.
- Complete disk exhaustion; the nonzero sixth powers are 1,7,11 and 2,8,12 are nonsquares.
- The exact first target and rank-one containment dependencies, with rational reverse inclusion.
- Prime-pair example a=−17309 and quadratic example a=−3474245 satisfy all rank-pattern assumptions. Their primes are certified by complete trial division, not probable-prime tests.

## Reproducible checking

Run python scripts/check_endpoint_families.py with SymPy installed. The exact run is saved in endpoint_families_output.txt. It checks generic rational identities, all lifts at 7 and 11, exhaustive finite-field counts, all listed prime-pattern prerequisites, the exact p11 certificate, and p19 tests including valuations 1,2,3,5. These samples are supplemental; the all-parameter statements come from identities and the full-series proof.

No finite truncation is used to prove an exact zero. No infinitude theorem, unrestricted Bloch–Kato identification, or failure at the omitted lifts is asserted. The prior special cases remain valid.
