# Independent review: certified residual nonvanishing at a=-605, p=5

## Outcome

Approved mathematically and computationally. Two independently written original Python implementations were read and executed. They agree on the entire 5-by-5 Frobenius matrix and six cross periods modulo 5^7, not merely on a leading digit. No downloaded research code or external numerical backend was executed.

The normalized period X=(integral nu_0 nu_1)/i is 21625 modulo78125. The equivalent monic-model period is J_5(-608)=48500 modulo78125, of valuation exactly3. The reported precision is rigorous, not inferred from stabilization.

## Mathematical audit

The regular endpoint Frobenius lift exists uniquely by Hensel lifting in Z5[x]/(f^5). Its derivative and polynomial quotient identities hold, it is overconvergent, and it fixes both finite Weierstrass points. Horizontal primitives have the form yK and vanish at both endpoints. The outer-first integration-by-parts formula, its factor1/2, and the endpoint functional divided by i were checked.

The affine computation retains all five basis forms, including the extra affine direction. Parity reduces the actual system to six cross coordinates; no other double periods are discarded without proof. The desired holomorphic coordinate descends to the proper residual quotient by the previously audited bar/Hodge argument.

## Precision audit

For coefficient precision N=30 and cutoff T=20, retain THEORETICAL degree D*=2868, horizontal loss L*=4 and integration loss J*=5, even though modular coefficient trimming leaves degree698 in this run.

The full checked horizontal congruence, together with the principal-part reduction bound, certifies finite K,m error at least22 digits and finite correction-vector error at least13 digits. All additional finite modular evaluation errors are weaker than this.

For the infinite tails, the nth Frobenius coefficient has valuation at least n+1 and degree at most132+144n. Its reduced coefficients lose at most floor(log5(130+144n)). The full correction tail is at least O(5^7), and the Frobenius-matrix tail is O(5^17). The stronger correction-tail O(5^8) also follows from (130+144s)^2(260+144s)<5^(s-5) for s>=20, but only seven digits are reported.

Both scripts verify integrality and unit determinant of the six-equation solve. Consequently inversion preserves the certified final precision. The independently checked JSON witness also satisfies A X=C modulo78125.

## Consequence and limits

The nonzero holomorphic period forces the full residual discrepancy delta_5(W) to be nonzero. For a=-605, the already certified rank-one hypothesis, non-CM condition and zero actual residual target imply that BOTH (i,0) and (-i,0) are absent from the specified full depth-two set.

This is not an equality determining the entire C(Q5)_2, does not classify other non-Weierstrass points, and does not compute the general transport Theta_p or the discrepancy at every prime.
