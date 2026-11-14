# Independent audit of the general 3-adic family criterion

Status: independent mathematical audit, completed. This audit checks the general analytic criterion, the exact away-from-3 target calculation, and the rank-one certificate for a=-157469.

## Audited files

- `../proofs/general_prime3_criterion.md`
- `../proofs/reciprocal_local_targets.md`
- `../proofs/rank_one_parameter_157469.md`, its rank certificate and complete obstruction output.
- The existing base height, disk-isolation and endpoint-basepoint bridge certificates, for their stated dependencies and conventions.

## Result

No substantive gap was found in the analytic criterion or the exact local-target formulas. Subject to the already established actual-local-image containment and endpoint-basepoint bridge, the following sufficient family statement is supported:

Let a be an integer with a congruent to -5 modulo 8 times 3^6. If E_a has rational rank one, and 3 does not divide v_q(a+1) for every odd prime q dividing a+1, then the Mordell–Weil-restricted, actual-local-image depth-two set at 3 is exactly the four rational endpoints. The odd primes in this test automatically satisfy q >= 5.

The rank hypothesis remains an independent arithmetic requirement. Neither 3-adic parameter continuity nor the local-target result proves it. The multiplicity condition is sufficient, not necessary.

## Analytic checks

1. The degree-two isogeny, pullback of the invariant differential and the complement relation are correct. With A=a-3, the latter is the exact differential identity

   phi*((Z-a-1) omega') = 2(X-2) omega - d(Y/X).

   Thus compatible global heights satisfy h'(phi(P))=2h(P), giving alpha'=2alpha. The fixed complements need not remain unit-root complements; the change of splitting cancels between the local height and its quadratic correction.

2. The formal quadratic coefficients are (a-1)/2 and (7-a)/2. Their divisibility by 3, together with the displayed coefficient bounds, proves B(t)/t^2 lies in 3 Z_3 on the entire formal disk. The integration bounds used in the finite-point terms control all coefficients, not only the leading term.

3. On the original endpoint disks, the normalized first-height value rho/(alpha x^2) belongs to 1+3 Z_3. Hence its nonzero values have the exact even nonnegative valuation and residue excluded by T1. Reciprocal antisymmetry requires the use of both Omega and -Omega. For symmetric actual targets, the stated simplification of T1 is correct.

4. On the transformed endpoint disks, the singular regularization has constant -log_3(d), where d=(a+1)/2 in the criterion. Therefore the constant K and the congruence rho* = K+C(u/3)^2 modulo 3 are correctly normalized. If K=C is a unit modulo 3, both possible square residues give a unit. T2 excludes these values at both zero and infinity; no symmetrization of T2 is needed.

5. The continuity lemma has adequate conservative losses. In particular, psi_3/t = -Omega_3/Phi_3 is a unit analytic ratio, so its difference is divisible by 3^M without dividing by the small psi_3 separately. The change in 1/t has valuation at least M-4; differentiating the multiplication identity introduces at most two further powers of 3. Thus the claimed losses M-1, M-2 and M-6 are sufficient at M=6. The entire convergent formal tails obey these bounds.

6. At the CM specialization, the twist formulas give m_0=ell_0/s_0, zeta'_0=s_0 zeta_0 and lambda'(Q_0)=h_0+log_3(2). Consequently K_0=2h_0 and C=1 modulo 3. The continuity argument preserves every part of H throughout the stated progression.

7. The first endpoint P has zero away-from-3 displayed local heights because it is integral nonsingular at every prime. This certifies h=lambda_3(P); it is not used to infer that an entire actual target is zero. The note maintains this distinction correctly.

## Local-target checks

1. For q dividing a-3, the common scaling gives reduction types good, III, I0* and III* as the residual valuation is 0, 1, 2 or 3. The respective nonidentity component corrections are uniform within each type. Thus the paired unit-coordinate images have equal heights. The argument uses component-height corrections rather than incorrectly relying on coordinate valuations alone. The stated odd-residue-characteristic argument also accommodates q=3, although this is not needed for the sufficient p=3 family.

2. For q dividing a+1, both displayed addition identities for X(P1+P2) and X(P1-P2) were independently checked algebraically. The relevant sum or difference reduces to the nonsingular point (0,0) of Y^2=X(X-2)^2. Hence the two multiplicative component classes differ by at most sign and have equal heights. This proves the first local target is zero.

3. The nodal duplication lemma is correct. At h>m and h=m, direct duplication gives the saturated height -m/2. For 0<h<m the next valuation is 2 min(h,m-h), except at 2h=m where extra numerator cancellation puts the next point in the already treated saturated region. The rational candidate height satisfies the required functional equation there as well. If no iterate reaches that region, compactness and local constancy give a finite discrepancy image; multiplication by 4 cannot keep a nonzero characteristic-zero discrepancy in a finite set. No false p-adic growth assertion is used.

4. The second local target coefficients are therefore exactly the stated 0 and signed 2k(m-k)/m values, with saturation m/2. The split/nonsplit restrictions and the even-m conic argument establish attainability, not just an upper bound. The conic always has a solution with nonzero r; its nonzero derivative lifts it to the full equation.

5. At 2, a congruent to 3 modulo 8 rules out unit x in the original model. In the transformed model every local point has unit u, valuation 2 for v, and the two quotient images are nonsingular after the common scaling Z=4z, Y=8w. Their equal model corrections cancel. Thus both 2-adic local targets are zero.

6. Every second-target coefficient has denominator dividing 2m. If 3 does not divide m, it is 3-integral. Since log_3(q) belongs to 3 Z_3 for q not equal to 3, the finite sum of all local images lies in 3 Z_3. The first target is zero under the congruence at 2. These are genuine arithmetic target certifications, independent of the analytic continuity argument.

## Resolved presentation correction

The local-target author has applied the requested scope clarification: the “exact weaker second-target-zero condition” now explicitly retains a congruent to 3 modulo 8. The unrestricted prime-2 target is not claimed to have been classified.

The notation differs between the two notes: the local-target note's c is the analytic criterion's d, and the local-target note's d is c times the analytic criterion's b. All checked formulas are consistent after this substitution.


## Sharpened second-target criterion

The subsequently added equivalence is also correct. Under a congruent to 1 modulo 3 and 3 modulo 8, the entire second actual target lies in 3 Z_3 if and only if

    v_3(v_q(a+1)) < v_3(q^2-1)

for every odd split prime q dividing a+1, where split means that 2 is a square modulo q. Nonsplit contributions are zero or integral multiples of log_3(q), and are always safe. For a split prime and m=v_q(a+1), all coefficient valuations are at least -v_3(m). If 3 divides m, the attained k=1 coefficient has exactly that valuation. Finally v_3(log_3(q))=v_3(q^2-1), and each individual local image occurs in the global Minkowski target by choosing zero at all other primes.

This is an exact criterion for the stronger statement Omega' contained in 3 Z_3. It is not asserted necessary for T2, which additionally permits targets of negative valuation.

## Independent rank audit for a=-157469

The rank-one certificate passes independent review.

1. The support argument includes every signed squareclass supported on B, including the prime 39367 for E'. The quartic equation N^2=dU^4+AU^2V^2+(B/d)V^4 follows from X=d(U/V)^2 with coprime U,V. The special torsion and origin classes are included. The real-place exclusions are valid.
2. Both primitive projective charts in the original certificate exhaust every possible primitive local pair. The use of square residues modulo q^k is only a necessary condition, which is exactly what is required for the upper bound. No global solubility claim is made for surviving quartics.
3. The separate script `../scripts/check_rank_one_independent.py` rechecks every recorded finite obstruction by enumerating all primitive residue pairs (U,V), rather than using the original chart implementation. All exclusions pass. The survivor bounds are 2 and 4; the standard two-isogeny descent identity therefore gives rank at most one.
4. The same independent script computes 3P by the rational group law and verifies v_3(t(3P))=2 and t(3P)/9=2 modulo 3. The formal logarithm has strictly higher-valuation remaining terms, so L(P) is nonzero of valuation one. This proves rank at least one independently of the numerical height residue certificate.
5. Trial division verifies that 39367 is prime. Since a+1=-4 times 39367 and a is 3 modulo 8, the exact local-target theorem gives both actual targets equal to zero. The progression a=-5-27 times (8 times 3^6) supplies H.

Consequently this is a second fully certified parameter, not merely a local analytic example. With the stated restricted Selmer convention and the existing containment/endpoint bridge,

    C_{-157469}(Q_3)_2 = C_{-157469}(Q) = {(0,1),(0,-1), infinity_+, infinity_-}.

Independent run output:

    E: every recorded obstruction independently verified on all primitive residue pairs.
    Eprime: every recorded obstruction independently verified on all primitive residue pairs.
    Direct group law: v3(t(3P))=2 and t(3P)/9=2 mod3, proving nonzero formal logarithm.
    INDEPENDENT RANK CHECK PASS: rank upper bound 1 and rank lower bound 1.
