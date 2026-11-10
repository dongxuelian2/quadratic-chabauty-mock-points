# A broader five-adic rational-point theorem and Selmer dichotomy

Let a be an integer with a≡3 modulo 8, 5 dividing a, and rank E_a(Q)=1, where E_a:Y²=X³+(a−3)X²−(a−3)X. Use the established Mordell–Weil abelian-image and actual-local-image convention.

Then C_a(Q)={(0,1),(0,−1),∞₊,∞₋}. Moreover C_a(Q₅)₂ is exactly either this four-point set or this set together with both W±=(±i,0). No restriction on the odd prime factors of a−3, or on v₂(a−3) beyond the stated congruence, is needed for these conclusions.

**Proof.** The exact local-target theorem proves w_q≡0 at every odd q≠5 for integral a and w₂≡0 when a≡3 modulo 8. Thus the entire actual first scalar target is {0}. The uniform six-disk theorem for odd integral a divisible by 5 proves that the zero set of this scalar is precisely the four rational endpoints and W±. Scalar containment gives the same six-point upper bound for the full restricted depth-two set, while rational-point containment supplies the four endpoints. Since i is not rational, neither W± is a rational point, proving the rational-point equality. The Q-automorphism g(x,y)=(−x,y) fixes the chosen basepoint (0,1), commutes with localization, preserves crystalline and actual-local Selmer conditions, and exchanges W±. Hence either both or neither belong to the full set, proving the dichotomy.

Except at a=−5 these parameters are automatically geometrically non-CM. Indeed v₂(a+1)=2 and j(E_a)=256a³/(a+1), with gcd(a,a+1)=1. If a+1 has an odd prime divisor, j has negative valuation there and cannot be a CM j-invariant. Otherwise a+1=±4, giving a=3 or −5; the first is excluded by 5 dividing a. The existing CM norm-one-torus theorem already resolves a=−5 in favor of four points.

For every remaining parameter, the exact integral-family gluing theorem applies already under a≡3 modulo 8, including v₂(a−3)=3. Consequently the six-point alternative occurs exactly when δ₅(W₊) belongs to Ω_R, the finite target transported from the actual residual bad-prime images. The uniform period theorem proves δ₅(W₊)≠0 because a≠−5. The [actual dyadic-image theorem](dyadic_actual_images.md) gives Xi₂={(0,0)} throughout this congruence family. Therefore any six-point case would require a nonzero actual odd residual target. This observation is not a calculation of Ω_R and does not exclude the six-point alternative when split odd primes dividing a−3 contribute.

The stronger endpoint-only theorem follows when those actual residual targets vanish, but that additional hypothesis is not used in the rational-point theorem or the four-versus-six dichotomy above.

**Independent review.** The first-target scope was checked directly in reciprocal_local_targets.md; the six-disk theorem, uniform period theorem, involution argument, CM exception, and applicability of the integral gluing theorem were checked separately. No full membership is inferred from scalar membership alone.
