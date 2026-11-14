# Independent audit of the 11-adic isolation certificate

Status: completed independent mathematical audit.

## Verdict

The normalized constants, two polynomial congruences, residue-disk coverage, and upgrade using the already reviewed rank, local-target, and endpoint-basepoint results check out. The certificate `../scripts/check_prime11.py` passes. I also recomputed the P, Q, and R constants independently using division-polynomial expressions for X(5T), rather than the certificate's repeated group-addition implementation.

The initial endpoint-proof wording was corrected during this audit: regularized local-height coefficients need not be coefficientwise 11-integral, whereas the required evaluated all-orders integrality is true. I checked and accept the revised endpoint paragraph. There is no remaining blocking gap in the proof, conditional only on the already reviewed dependencies.

## Exact independent computations

For psi_3=q, psi_4=4YH, and psi_5=f, the recurrence gives

    X(5T) = X - 8 g q H (f - 4H^2) / f^2,
    Y(5T) = (Y/5) dX(5T)/dX.

Exact rational differentiation of these expressions, followed by t=-X/Y, gives:

- P: v11(t(5P))=1; t(5P)/55=1 mod 11; V_P=23 mod 121; zeta(P)=1 mod 11.
- Q: v11(t(5Q))=2; V_Q=45 mod 121; zeta'(Q)/s=10 mod 11.
- R: using X(2R)=(X(R)^2+A)^2/(4g(X(R))) and the five-fold formula, v11(t(10R))=2; t(10R)/(1210s)=4 mod 11; zeta(R)/s=109 mod 121.

The logarithm residues of V_P and V_Q divided by 11 are 2 and 4. Division by 25 therefore gives h/11=8 and lambda'(Q)/11=5. Also d=37 mod 121, so log_11(d)/11=10. Consequently

    11 alpha = 8,
    K/11 = 6,
    C = 4,
    D/11 = -4(10+8*4) = 8 mod 11.

The primitive multiplication identity is

    zeta(T)=zeta(nT)/n - (D log psi_n)(T)/n^2.

Applying it with n=2 and then n=5 gives precisely the divisors 10, 50, and 4 in equation (13). For psi_2=2Y, (D log psi_2)(R)/s=g'(X(R))/(d Ybar(R)), as used in the script.

## Local signs and leading terms

At u=0 and v=s, the original quotient points are -R and R. Their differentials are -(1+u)du/v and -(1-u)du/v. Thus their logarithms are -r-J-I and r-J+I exactly, and their quadratic correction is -4 alpha J(r+I).

For H=lambda(f1)-lambda(f2)-2 log x, evenness of lambda and reciprocity show that H is odd in u. At zero,

    H'(0) = -4 zeta(R)/s - 4.

Since J=u/s+O(p^3), I=u^2/(2s)+O(p^4), v_p(alpha)=-1, and v_p(r)>=2, the surviving cubic is exactly -2 alpha u^3/d. These checks give

    rho(pT)/p^2 = T(D/p-C T^2) mod p.

The second-model singular parameter is t=-u(1+u^2)/v. Consequently the constant of -lambda'(F2)-2 log u is -log d, not +log d. Its finite logarithms are m+I and -J, giving

    rho*(pT)/p = K/p+C T^2 mod p.

The branch v -> -v changes neither height.

## All-orders estimates

For a finite-point local-height composition on one of these disks, all differentiated numerators are integral. A single primitive has degree-n coefficient valuation at least -v_p(n); a nested primitive has valuation at least

    -v_p(n)-floor(log_p(n-1)).

The initial primitive values are integral: for R this follows from zeta(R)/s+1 in p Z_p. Oddness removes even degrees of H. For every p>=5 and n>=3,

    n-v_p(n)-floor(log_p(n-1)) >= 3,

and this lower bound tends to infinity. Therefore the full nonlinear part of H(pT), not only a fixed truncation, lies in p^3 Z_p.

The error terms of J and I stated above follow from the same single-integration bounds. In fact their induced error in -4 alpha J(r+I) is at least p^4. For the second height, finite-point and regularized singular variations lie in u^2 Z_p as evaluated functions on u in p Z_p. Also alpha*m*I and alpha*I^2 lie in p^3 Z_p. The full error after retaining K+2 alpha u^2/d is therefore in p^2 Z_p, as required.

For formal t with v_p(t)=h>=1, the formal logarithm error after t has valuation at least 3h, the primitive error after 1/t has valuation at least h, and B(t) has valuation at least 2h. These estimates justify every discarded term in the P, Q, and R constant computations. In particular the error in zeta(R)/s after the principal rational expression is in 11^2 Z_11.

## Endpoint wording repair

The revised main proof now correctly uses evaluated rather than coefficientwise integrality. A detailed formulation of that accepted correction is:

“Writing lambda(t)=-2 log_p(t)-2B(t), the coefficient bound v_p([t^(2k)]B)>=-v_p(2k)-floor(log_p(2k-1)) implies B(t)/t^2 in Z_p for t in p Z_p, p>=5. The finite-point primitive at P is integral, and the regularized local-height variation divided by x^2 is therefore integral on the endpoint disk.”

Indeed the displayed coefficient bound gives

    2k-2-v_p(2k)-floor(log_p(2k-1)) >= 0.

It is not legitimate to claim coefficientwise integrality: for this E and complement, the coefficient of t^12 in B has 11-adic valuation -1, and the coefficient of t^22 has valuation -2.

With the evaluated estimate, the endpoint argument is complete. The nonquadratic local variation divided by x^2 is integral. The cross term alpha*ell*I/x^2 is integral because v_p(alpha)=-1 and v_p(ell)=1; alpha*I^2/x^2 has valuation at least one. Finally (J/x)^2 is in 1+p Z_p. Hence rho(x)/(alpha*x^2) is in 1+p Z_p whenever x is nonzero in p Z_p. The center is a zero because h=alpha*ell^2. Reciprocity treats infinity.

## Eight disks and final implication

At p=11, a=7, A=4, and d=4 modulo 11. The genus-two discriminant is -64(a-3)^6(a+1)^2, a unit; both elliptic discriminants are units. The exact affine reduction is

    (0,1), (0,10), (1,4), (1,7), (10,4), (10,7),

with two distinct smooth infinity points. Proper good reduction therefore gives exactly the asserted eight Q_11 residue disks.

The u=0 disks are the x=-1 disks; u=infinity gives x=1. The involution (u,v)->(1/u,v/u^3) corresponds to (x,y)->(-x,-y). It preserves rho and negates rho*, so no disk is omitted. Both branches are covered by evenness of local heights and squared logarithms.

For F=T(8-4T^2), G=6+4T^2, F+TG=3T and G(0)=6. Thus no common residue root exists. The four rational endpoints also satisfy rho*=0 because at u=+/-1 the two elliptic quotient points agree up to sign.

The local-target theorem is stated for arbitrary odd good p, not only p=3. Since a=3 mod 8 and a+1=-4*39367 has squarefree odd part, it supplies both actual targets {0} at p=11. The reviewed rank-one certificate and general endpoint-basepoint/actual-target containments then give the claimed full Mordell-Weil-restricted equality. This audit does not extend that conclusion to the unrestricted abelian Bloch-Kato convention.
