# Independent audit of the small-disk classification

Reviewed on 2026-11-07. Scope: `../proofs/small_disk_classification.md` and `../scripts/check_small_disks.py`, after the opening hypothesis was clarified to say that a is an odd integer.

**Verdict: pass.** The finite-field computation, cutoff, special centers, and limitation of the conclusion are correct. The submitted exhaustive checker passes. No rank or height-isolation assertion follows just from this classification.

The two elliptic quotient maps induce the usual degree-four isogeny from J(C_a) to E_a squared. At an odd good prime they therefore give

    #C_a(F_p) = p+1−2t_p = 2#E_a(F_p)−p−1.

Hasse's bound implies p+1−4sqrt(p)<=8 if #C_a(F_p)<=8. Solving this inequality gives sqrt(p)<=2+sqrt(11), hence p<=15+4sqrt(11)<29. This is a bound on the small-disk layout only.

At p=1 modulo 4 the two Q_p-visible points (±i,0) have exactly zero values for both scalar functions: each quotient pair agrees at two-torsion and log_p(±i)=0; the second coordinates are u=∓i. For odd a, each first local actual image contains zero, witnessed by an endpoint because P is integral and nonsingular at every finite prime. Each second local actual image contains zero, witnessed by the rational points u=±1, v=±4, where the two images agree up to sign. Therefore both global targets contain zero and these two additional points pass both scalar conditions. This establishes only the scalar obstruction, not full-depth-two membership.

The odd-a hypothesis is relevant to this actual-target assertion. Exact scalar vanishing at ±i is more general, but one cannot infer that the first refined target contains zero for arbitrary even parameters. The current clarified statement makes the necessary distinction.

The remaining primes below 29 are precisely 3,7,11,19,23. Exhaustive point counting gives exactly these eight rows with at most eight disks:

    (p,a mod p,#C) =
    (3,1,8), (7,2,8), (7,4,4), (11,1,8),
    (11,2,4), (11,7,8), (19,0,4), (23,20,8).

The four nonendpoint centers are exactly the ones listed in the source. At p=23 they have x=3,8,15,20 and y=0. At p=11 the two eight-disk rows have x=±1 and y=±2 or ±4 respectively. At p=19 there is only the four-disk row, not an exactly-eight-disk row. Smoothness guarantees that these points give full residue disks. The discriminant −64(a−3)^6(a+1)^2 also verifies the stated good-model criterion.

Nothing here excludes a more-than-eight-disk analytic argument, a non-scalar obstruction, or a full-depth-two result at a larger prime. This records the completed independent review.

## Independent audit of the four-disk extension a=−605

Additional reviewed artifacts: `../proofs/prime7_four_disk_family.md` and `../scripts/check_prime7_four_disks.py`. I read the complete actual proof after the independent computation below, checked that its statements agree with these estimates, and ran its checker successfully. **The four-disk extension passes without correction.** It uses the same integral complement [(X−2)omega]. At a=−605, direct rational addition gives

    3P = (133968444289/135751718025,
           148737027213396287/50017041747721125),
    t_3 = −134857133565/406366445311,
    psi_3(P) = a(4−a) = −368445,
    psi_3(P)/t_3 = 406366445311/366017,
    1/(3t_3)−8/(3psi_3(P)) = −1102915/1098051.

The third division polynomial has derivative D psi_3(P)=24, so the last expression is exactly the principal contribution to zeta(P). The formal tails give

    ell/7 = 4 mod 7,
    h/7 = 5 mod 7,
    Z in Z_7 (indeed Z=4 mod 7),
    7alpha = 6 mod 7.

For the height computation, psi_3/t_3=36 modulo 49, and log(U)=(U^6−1)/6 modulo 49. The B contribution has valuation at least two, so h=(2/9)log(U) modulo 49. This proves v_7(h)=1 rather than merely detecting numerical nonzero digits.

On an endpoint disk, the term alpha(J/x)^2 in rho/x² has valuation −1. Every other term is integral: the cross term alpha ell has valuation zero, alpha I²/x² has valuation at least one, and the finite and regularized singular local-height quotients are integral. Consequently

    7rho(x)/x² = 6 mod 7

uniformly for nonzero x in 7Z_7. Reciprocity handles infinity. Since a=4 modulo 7 gives only four disks, this proves first-height isolation.

The same quantitative division-formula argument with n=3 shows that a congruent to −605 modulo 49 preserves v_7(ell)=v_7(h)=1 and Z in Z_7. Here delta h,delta ell lie in 49Z_7, while delta Z lies in Z_7; preserving the exact residue of Z is unnecessary. Thus every odd a=−605 modulo 49 has the same scalar isolation. Adding a=3 modulo 8 and rank one supplies the full restricted conclusion by the existing first-target theorem and bridge. The combined progression is a=−605 modulo 392.

I additionally checked the arithmetic leading residues for a=−605+98k, 0<=k<=6. The quantitative proof, not these seven samples, establishes the full neighborhood.

The concrete unconditional example also has the asserted rank certificate. The prime-pair theorem is Theorem 1 of `../proofs/checkable_rank_patterns.md`. Here A=−608=−32·19, q=8·19−1=151, and 19=3 modulo 8; both 19 and 151 are prime. The short descent proof specializes to

    delta(E(Q)) = {1,38},
    delta'(E'(Q)) = {1,−38,−151,5738}.

I checked this specialization directly against that proof. Negative first-image classes are impossible over the reals; the d=2 quartic is obstructed modulo 8 after the stated scaling, and the torsion class 38 also excludes d=19. On the second curve, multiplication by the torsion class 5738 reduces the candidates to odd signed divisors of 19·151. The local argument requires such an odd class to be 1 modulo 8, leaving only 1 and −151. Restoring the torsion class gives the four displayed possibilities. The rational points (A,2A) and (A+4,2(A+4)) realize −38 and −151, so the upper bound is attained. The standard two-isogeny formula then gives 2^rank=(2·4)/4=2.

Finally −605=3 modulo 8. Thus the actual artifact's unconditional conclusion for C_{−605} at 7 follows from this rank-one certificate and the already established first-target and endpoint-basepoint results. Its conditional progression a=−605 modulo 392 makes no unsupported claim of infinitely many rank-one parameters. This records the completed independent review.
