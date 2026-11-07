# Independent audit of the prime-7 one-height family

Reviewed on 2026-11-07. Scope: `../proofs/prime7_isolation.md` and `../scripts/check_prime7.py`. The actual-local-image containment, endpoint-basepoint bridge, and first-target theorem in `../proofs/reciprocal_local_targets.md` are the stated existing inputs. This audit checks their application here rather than purporting to reprove the entire nonabelian comparison.

## Verdict

**Pass.** The scalar isolation theorem holds as stated for every odd integer a congruent to −5 modulo 343. The quantitative M=3 argument, all eight residue disks, primitive normalization, and all-orders estimates are sufficient. I found no mathematical correction or additional arithmetic hypothesis needed.

With the existing containment and bridge, a congruent to 3 modulo 8 and rank E_a(Q)=1 give the claimed equality for the **Mordell–Weil-restricted, actual-local-image** depth-two set. No condition on odd prime multiplicities of a+1 is required, because only the first scalar condition is used. No conclusion about an unrestricted abelian Bloch–Kato Selmer convention or infinitely many rank-one parameters follows.

The submitted checker passes. The separate standard-library checker `../scripts/check_prime7_independent.py` also passes. It uses successive doubling and composite division functions, not the author's fourth-division polynomial implementation, and compares certificates through 4P and 8P. The source proof and checker have not been modified; this records the completed independent review.

## 1. Splitting, normalization, and exact constants

The classes of omega and X omega form the usual de Rham basis, so [(X−2)omega] is a complement at every parameter under consideration. A one-dimensional complement is isotropic. The good-reduction double-integral height does not require ordinarity or a unit-root splitting. Indeed #E_{−5}(F_7)=8, hence its trace is zero and it is supersingular.

For A=a−3 and T=t², write X=t^(−2)U(T). Direct substitution gives

    U² − (1−A T)U − A T² = 0,
    omega = w(t)dt,  w = 1 − T U'/U.

The derivative of the first equation with respect to U at (U,T)=(1,0) is 1. Thus all coefficients of U and w are integral polynomials in A. In particular,

    X = t^(−2) − A + A t² + ...,
    w = 1 + A t² + ...,
    zeta = 1/t + 2t + ...,
    B = ((A+2)/2)t² + ... = ((a−1)/2)t² + ... .

This verifies the complement-dependent quadratic coefficient, including B_2=−3 at a=−5.

With lambda=−2 log(t)−2B and D=d/omega, differentiating

    lambda(nP) = n² lambda(P) − 2 log(psi_n(P))

gives exactly

    zeta(P) = zeta(nP)/n − D log(psi_n)(P)/n².

There is no sign or factor-of-two error. The division-function identity has the same form for this non-unit-root complement; adding a multiple of L² preserves it.

The exact submitted 4P, t_4, and psi_4(P)=868 are correct. Their residues give

    t_4/7 = 6 mod 7,
    psi_4/t_4 = 79 mod 343,
    log_7(psi_4/t_4) = 49 mod 343,
    B(t_4) = 196 mod 343,
    1/(4t_4) − D log(psi_4)(P)/16 = 183/2273.

Hence ell/7=5, h/49=4, alpha=1, and Z=3 modulo 7. In particular P is nontorsion throughout the neighborhood: its elliptic logarithm is nonzero.

The independent checker constructs psi_4 and psi_8 recursively from

    psi_(2n)(P) = 2Y(nP) psi_n(P)^4,
    D log(psi_(2n))(P)
      = n g'(X(nP))/Y(nP) + 4 D log(psi_n)(P).

The 4P and 8P calculations agree modulo 7^6. At a=−5 they give

    (ell,h,Z) = (48839,5684,27107) mod 7^6.

The same independently checked leading residues hold for a=−5+686k, 0<=k<=6. These samples cover every next 7-adic parameter digit while retaining oddness; the proof for all parameters is the quantitative argument below, not the samples.

## 2. All-orders estimates

Write the regular part of −(X−2)w as sum a_(2j)t^(2j), with integral coefficients, and w=sum w_(2j)t^(2j). Then

    [t^(2k)]B = (1/(2k)) [w_(2k)
       + sum_(j=0)^(k−1) a_(2j) w_(2k−2j−2)/(2j+1)].

This proves the advertised coefficient lower bound

    v_7([t^(2k)]B) >= −v_7(2k) − floor(log_7(2k−1)).

At v_7(t)>=1 the terms with k>=2 have valuation at least 4. For k=2,3 this is immediate. For k>=4 each denominator loss is at most k−2. The actual lower bounds tend to infinity because the losses grow only logarithmically. Thus B(t_4)=−3t_4² modulo 343 is an estimate on the whole series. The single integrals likewise give L(t_4)=t_4 modulo 343 and zeta(t_4)=1/t_4 modulo 7.

For a unit U, e=U^6−1 lies in 7Z_7. Every omitted term e^n/n with n>=3 has valuation n−v_7(n)>=3, tending to infinity. Therefore the submitted two-term logarithm certificate modulo 343 is justified even when v_7(e)=1.

For the independent modulo-7^6 check, B is retained through t^12, L through t^13, zeta through t^11, and log(1+e) through e^8. All omitted terms have valuation at least 8. For B, at k>=7 the two losses are each at most k−4, giving a lower bound 8. For the single integrals the omitted exponents are at least 13; n−v_7(n)>=8. For the logarithm n>=9 gives n−v_7(n)>=8. These bounds tend to infinity, and division by 4, 8, 16, or 64 loses no precision at 7.

## 3. Endpoint disks

On either branch y=epsilon sqrt(1+a x²+a x⁴+x⁶), x in 7Z_7, all even-series coefficients of 1/y are integral. Coefficientwise integration shows

    I/x² = epsilon/2 mod 7,    J/x = epsilon mod 7.

The initial primitive at the finite image is epsilon Z and the invariant differential begins epsilon x dx. Consequently the quadratic height coefficient is −Z, independent of the branch sign. The higher finite-height terms are nested integrals of x times integral even series. Their individual degree-2n denominators are bounded by

    v_7(2n) + floor(log_7(2n−2)),  n>=2.

After evaluation and division by x², all these terms lie in 7Z_7, uniformly on the whole disk. The part proportional to Z has the same bound since Z is integral.

For the singular image t_2=−x(1+x²)/y, the logarithmic singularity cancels. The quadratic coefficients of the resulting two terms are 2−a and a−1, summing to 1. The higher B terms divided by x² lie in 49Z_7. For a logarithm of an integral even unit, write its normalized argument as 1+x²r(x²); the n-th log term divided by x² has valuation at least 2n−2−v_7(n). This controls the entire logarithm tail.

Since L(f_1)=epsilon ell+I and L(f_2)=−J, the full coefficient is

    rho(x)/x² = 1−Z+alpha(1−ell) = 6 mod 7.

Every nonzero x in the disk therefore gives a nonzero height. The centers have height zero because h=alpha ell². Reciprocity exchanges the two endpoint charts and negates rho, proving exactly the same isolation at infinity.

## 4. Four Weierstrass disks

The center formula rho(W)=−log_7(r) is the existing exact two-torsion formula specialized to a_0=a_6=1. It is independent of the splitting, since both elliptic logarithms vanish there. At a=−5 the roots modulo 49 are exactly 9,11,38,40, and their sixth powers are 36,15,15,36. Each r^6−1 has valuation one, so v_7(log_7 r)=1.

Here is the explicit integrality behind the uniform disk bound. If F(x)=x⁶+a x⁴+a x²+1, then F'(r) is a unit. Thus x=x(y²) has integral coefficients and

    f_1^*omega = (2x/F'(x))dy,
    f_2^*omega = (−2/F'(x))dy.

Both are integral even power series times dy. The corresponding second-kind pullbacks have the same property, because both image X-coordinates are integral. The elliptic images at the center are nonzero two-torsion; L and the odd primitive zeta both vanish there.

A single integral of an integral even power series, evaluated at y in 7Z_7, lies in yZ_7. The double integral has the same coefficient-denominator bound as B above, starting at y², and its value lies in y²Z_7. Thus both local heights vary in y²Z_7. The alpha L² terms and log(x/r) also vary in y²Z_7 because alpha is integral and x/r=1+y² times an integral series. Therefore

    rho(y)−rho(W) is in y²Z_7, hence in 49Z_7.

A center of valuation one cannot be canceled by this variation anywhere in its residue disk. This argument covers each entire disk and does not rely merely on a derivative at its center.

## 5. Parameter precision and complete coverage

All formal numerators above are integral polynomials in A. The division formulas have integral polynomial numerators at P and denominators that are units except for the stated psi_4 factor. At a=−5, Phi_4 and Omega_4 are units, while psi_4 and t_4 have valuation one. If delta a is in 7^M Z_7, M>=3, the same facts persist, and

    delta t_4 is in 7^M Z_7,
    delta(psi_4/t_4)=delta(−Omega_4/Phi_4) is in 7^M Z_7.

For a coefficient with denominator loss d, changing its integral-polynomial numerator costs no more than d powers of 7. Changing t^n costs at most the bound

    v_7(t^n−t_0^n) >= M+n−1.

Applying this termwise, with the single/double integration bounds and convergent tails, proves delta L in 7^M Z_7 and delta B in 7^(M+1) Z_7. The sole worse term in delta zeta is delta(1/t), which lies in 7^(M−2) Z_7. The integral-numerator rational expression D log(psi_4)(P) has a denominator of valuation one, so its difference also lies in 7^(M−2) Z_7. Finally log is 1-Lipschitz on units with a fixed residue modulo 7.

It follows that delta ell,delta h lie in 7^M Z_7 and delta Z lies in 7^(M−2) Z_7. At M=3 these are exactly the precisions needed to preserve ell/7, h/49, and Z modulo 7. The proof therefore certifies 343, not merely an unspecified open neighborhood. It does not assume continuity of a unit-root complement.

Hensel lifting preserves the four simple quartic roots modulo 343 and therefore preserves their logarithm valuations. Good reduction persists: the sextic discriminant is −64(a−3)^6(a+1)^2, a 7-adic unit here. Modulo 7,

    F=(x−3)(x−2)(x+2)(x+3)(x²+1),

and the affine rational points are exactly (0,±1),(2,0),(3,0),(4,0),(5,0). Together with the two infinity points they give all eight disks of the smooth proper curve. No disk or exceptional point is missing.

## 6. Arithmetic consequence and the limitation at p=1 modulo 4

For odd a, P is nonsingular on the displayed integral model at every finite prime: at odd primes its Y-derivative is a unit, and at 2 its X-derivative is a, which is odd. The normalized away-from-7 heights of P vanish, so the local h used here equals its global height. Under rank one, its nonzero logarithm provides the required global quadratic coefficient.

For a=3 modulo 8, the established first-target theorem gives target {0} at every away-from-7 place, without restrictions on a+1. Applying the existing endpoint-basepoint bridge and actual-target containment therefore gives the full restricted conclusion from this one scalar zero set. The Chinese remainder combination is precisely a=−5 modulo 2744. The already certified rank-one parameter a=−5 is thus a full example at 7 as well as at 3.

The stated obstruction to an all-prime *two-scalar* theorem is also exact. At every good p=1 modulo 4, the points (±i,0) exist on every nonsingular reciprocal curve. Both first quotient images are (0,0), so their local heights agree, their elliptic logarithms vanish, and log_p(±i)=0. In the second model u=(x+1)/(x−1), these points have u=∓i and v=0; both second quotient images are again (0,0). Consequently both scalar functions vanish exactly, not just to a computed precision. In particular p=5 is good for both a=−5 and a=−157469 and prevents their two-scalar intersection from consisting of only the endpoints. This does not imply full depth-two membership, and the submitted proof correctly keeps that distinction.
