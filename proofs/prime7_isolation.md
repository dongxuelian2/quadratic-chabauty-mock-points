# One scalar height suffices at 7, with an explicit parameter neighborhood

Status: independently reviewed research proof. The exact rational certificate is `../scripts/check_prime7.py`. This note uses the established actual-local-image containment and endpoint-basepoint bridge, not a claim that arbitrary scalar height conditions characterize the unrestricted Selmer set.

## 1. Result

For odd a let

\[
 C_a:y^2=x^6+ax^4+ax^2+1,\qquad
 E_a:Y^2=X^3+AX^2-AX,\quad A=a-3,\quad P=(1,1).
\]

Use the fixed complement \(W=\mathbf Q_7[(X-2)\omega]\), with \(\omega=dX/(2Y)\), the normalized cyclotomic local height, and

\[
 \ell=L(P),\quad h=\lambda(P),\quad Z=\zeta(P),\quad
 \alpha=h/\ell^2,\qquad
 d\zeta=-(X-2)\omega,\quad d\lambda=-2\zeta\omega.
\]

The odd primitive \(\zeta\) is normalized by \(\zeta(t)=t^{-1}+O(t)\) at the origin. The away-from-7 heights of P vanish for every odd a, so h is also its global height. Define the usual first bielliptic height

\[
 \rho_a=\lambda(f_1)-\lambda(f_2)-2\log_7x
               -\alpha L(f_1)^2+\alpha L(f_2)^2,
\]

where \(f_1=(1+x^2,y)\), \(f_2=(1+x^{-2},y/x^3)\), with continuous extensions at the endpoints.

**Theorem.** Every odd integer

\[
 a\equiv-5\pmod{343}
\]

satisfies

\[
 \{z\in C_a(\mathbf Q_7):\rho_a(z)=0\}
       =\{(0,1),(0,-1),\infty_+,\infty_-\}. \tag{1}
\]

Consequently, if in addition \(a\equiv3\pmod8\) and \(\operatorname{rank}E_a(\mathbf Q)=1\), then for the established Mordell–Weil-restricted, actual-local-image convention,

\[
 C_a(\mathbf Q_7)_2=C_a(\mathbf Q)
       =\{(0,1),(0,-1),\infty_+,\infty_-\}. \tag{2}
\]

Equivalently, a sufficient combined parameter progression is \(a\equiv-5\pmod{2744}\), together with rank one. No restriction on the prime multiplicities of a+1 is needed. In particular the already rank-certified a=−5 is an unconditional example at the second prime p=7.

The chosen complement need not be unit-root. Indeed E_{−5} is supersingular at 7. The double-integral local height is defined for this complement, and changing compatible elliptic splittings cancels between the local height and the global quadratic correction in \(\rho_a\).

## 2. Exact constants at a=−5

Put \(E:Y^2=X^3-8X^2+8X\). Exact rational doubling gives

\[
 4P=\left(\frac{5166529}{753424},
               -\frac{695062943}{653972032}\right),\qquad
 t_4=-X(4P)/Y(4P)=\frac{1972964}{305791}.
\]

Thus \(v_7(t_4)=1\). The fourth division polynomial at P is \(\psi_4(P)=868\), also of valuation one. The formal series are

\[
 L(t)=t+O(t^3),\quad
 \zeta(t)=t^{-1}+2t+O(t^3),\quad
 \lambda(t)=-2\log_7t-2B(t),\quad B(t)=-3t^2+\cdots.
\]

For a good integral model and integral complement, the general coefficient bound already proved by double integration is

\[
 v_7([t^{2k}]B)\ge-v_7(2k)-\lfloor\log_7(2k-1)\rfloor. \tag{3}
\]

For t in \(7\mathbf Z_7\), every term k≥2 has valuation at least 4. This follows directly for k=2,3, and for k≥4 from bounding each of the two denominator losses by k−2. The bounds tend to infinity. Therefore

\[
 B(t_4)\equiv-3t_4^2\pmod{7^3}.
\]

The analogous single-integration bounds give \(L(t_4)-t_4\in7^3\mathbf Z_7\) and \(\zeta(t_4)-1/t_4\in7\mathbf Z_7\).

Multiplication gives

\[
 \ell=L(t_4)/4,\qquad
 h=\frac{2}{16}\left(\log_7\frac{\psi_4(P)}{t_4}-B(t_4)\right),
\]

\[
 Z=\frac{\zeta(t_4)}4-\frac{D\log\psi_4(P)}{16},\qquad D=d/\omega.
\]

All entries in the following table are exact residues of rational expressions, not unbounded numerical approximations:

| quantity | residue |
|---|---|
| t_4/7 modulo 7 | 6 |
| ψ_4(P)/t_4 modulo 343 | 79 |
| log_7(ψ_4(P)/t_4) modulo 343 | 49 |
| −3t_4² modulo 343 | 196 |
| 1/(4t_4) − Dlogψ_4(P)/16 | exactly 183/2273 |

For the logarithm row, if U is a 7-adic unit and e=U^6−1, then

\[
 \log_7U\equiv(e-e^2/2)/6\pmod{343}.
\]

Indeed the full remaining logarithm tail has valuation at least three. These identities yield

\[
 \boxed{\ell/7\equiv5,\quad h/49\equiv4,\quad
             \alpha\equiv1,\quad Z\equiv3\pmod7.} \tag{4}
\]

In particular \(v_7(\ell)=1\), \(v_7(h)=2\), and \(\alpha,Z\in\mathbf Z_7\).

## 3. Uniform isolation of the four endpoint disks

For either branch \(y=\varepsilon\sqrt{1+ax^2+ax^4+x^6}\) on x in \(7\mathbf Z_7\), put

\[
 I=\int_0^x t/y(t)\,dt,\qquad J=\int_0^x dt/y(t).
\]

The integral even-series estimates give, uniformly on this entire disk,

\[
 I/x^2\equiv\varepsilon/2,\qquad J/x\equiv\varepsilon\pmod7.
\]

The first finite height has

\[
 (\lambda(f_1)-h)/x^2\equiv-Z\pmod7.
\]

To justify the complete remainder, differentiate twice using \(d\lambda=-2\zeta\omega\). The finite-point term beyond its quadratic coefficient is a nested integral of integral even power series; after evaluation and division by x² its terms have valuations at least one. The coefficient denominators have the same form as (3). No truncation without a tail estimate is being used.

The second elliptic image has formal parameter \(t_2=-x(1+x^2)/y\). Its regularized contribution is

\[
 S=-\lambda(f_2)-2\log_7x
   =2\log_7((1+x^2)/y)+2B(t_2).
\]

For general a the quadratic coefficient of B is \((a-1)/2\), whereas that of the first logarithmic term is 2−a. Thus

\[
 S/x^2\equiv(2-a)+(a-1)=1\pmod7.
\]

Again (3) bounds the entire higher B-series, and the logarithm of the even analytic unit has integral higher coefficients after evaluation on \(7\mathbf Z_7\).

Since \(L(f_1)=\varepsilon\ell+I\), \(L(f_2)=-J\), and \(h=\alpha\ell^2\), it follows that

\[
 \frac{\rho_a(x)}{x^2}
       \equiv1-Z+\alpha(1-\ell)\pmod7. \tag{5}
\]

Whenever (4) holds the right side is 6. Hence the only first-height zero in either x=0 disk is its rational center. Reciprocal antisymmetry gives the same assertion at infinity.

## 4. Uniform exclusion of all four Weierstrass disks

At a=−5, the remaining four rational residue disks are centered at

\[
 W=(r,0),\qquad r\in\{1+\sqrt2,1-\sqrt2,-1+\sqrt2,-1-\sqrt2\}.
\]

The first height at a Weierstrass point is exactly

\[
 \rho_a(W)=-\log_7r. \tag{6}
\]

Take \(\sqrt2\equiv10\pmod{49}\). The four r-residues modulo 49 are 9,11,38,40. Their sixth powers modulo 49 are respectively 36,15,15,36. Thus

\[
 v_7(\rho_{-5}(W))=1. \tag{7}
\]

A Weierstrass residue disk has uniformizer y in \(7\mathbf Z_7\), with x=x(y²) an integral even analytic series and x(0)=r. Each elliptic image at W is nonzero two-torsion. Its elliptic logarithm is zero, and its odd primitive ζ is zero: inversion negates ζ and fixes the two-torsion point. The pullbacks of the invariant and second-kind differentials are integral analytic differentials on this disk, since the corresponding roots of the good elliptic cubic are simple.

Consequently the logarithms of the two elliptic images lie in \(y\mathbf Z_7\) after evaluation. Integrating the integral differential for ζ from its zero constant and then integrating \(d\lambda=-2\zeta\omega\) gives local-height variations in \(y^2\mathbf Z_7\). The exact integration denominator bounds are (3), and after evaluation on y in \(7\mathbf Z_7\) all terms divided by y² are integral. Also \(\log_7(x/r)\in y^2\mathbf Z_7\). Since α is integral, the global quadratic corrections vary in the same module. Hence, uniformly,

\[
 \rho_a(y)-\rho_a(W)\in y^2\mathbf Z_7\subset49\mathbf Z_7. \tag{8}
\]

Equations (7)–(8) exclude the entire disk, not just its center.

## 5. Parameter continuity at precision 7³

The constants (4) and the Weierstrass condition (7) persist for every odd \(a\equiv-5\pmod{343}\). Here is a quantitative justification that avoids continuity claims about a unit-root splitting.

More generally suppose \(a\equiv-5\pmod{7^M}\), M≥3. The fourth-division formulas at P have integral polynomial numerators:

\[
 X(4P)=\Phi_4/\psi_4^2,\quad
 Y(4P)=\Omega_4/\psi_4^3,\quad
 t_4=-\Phi_4\psi_4/\Omega_4.
\]

At a=−5 both Φ_4 and Ω_4 are units, while ψ_4 and t_4 have valuation one. Polynomial congruence preserves these facts, and gives

\[
 \Delta t_4\in7^M\mathbf Z_7,\qquad
 \Delta(\psi_4/t_4)=\Delta(-\Omega_4/\Phi_4)
                         \in7^M\mathbf Z_7.
\]

The integral formal-series numerators and their proven integration denominator bounds then give

\[
 \Delta L(t_4)\in7^M\mathbf Z_7,\quad
 \Delta B(t_4)\in7^{M+1}\mathbf Z_7,\quad
 \Delta\zeta(t_4)\in7^{M-2}\mathbf Z_7.
\]

For ζ the possible loss of two powers is only the variation of 1/t. For B the lowest exponent comes from varying the quadratic term; each higher-term bound is at least M+1 and tends to infinity. The logarithm of the unit ψ_4/t_4 varies in \(7^M\mathbf Z_7\).

Finally \(D\log\psi_4(P)\) is an integral-polynomial numerator divided by ψ_4(P), so its variation lies in \(7^{M-2}\mathbf Z_7\). Division by 4 or 16 loses no 7-adic precision. Therefore

\[
 \Delta\ell\in7^M\mathbf Z_7,\qquad
 \Delta h\in7^M\mathbf Z_7,\qquad
 \Delta Z\in7^{M-2}\mathbf Z_7.
\]

For M=3, this preserves the residues of ℓ/7, h/49 and Z in (4), hence also that of α=(h/49)/(ℓ/7)².

The four nontrivial Weierstrass centers are the simple roots of

\[
 x^4+(a-1)x^2+1.
\]

Hensel's lemma gives roots congruent modulo 343 to their four a=−5 counterparts. Their logarithms are therefore congruent modulo 343, preserving (7). The estimates in Sections 3–4 use only good reduction, these certified constants, and integral model coefficients, so they apply throughout the neighborhood.

Modulo 7 every curve in this neighborhood has precisely the six affine points

\[
 (0,1),(0,-1),(2,0),(3,0),(4,0),(5,0),
\]

and the two points at infinity. The model is smooth, so these eight disks exhaust \(C_a(\mathbf Q_7)\). Sections 3–4 prove (1). The four endpoints themselves have ρ=0 by h=αℓ² and reciprocal symmetry.

## 6. Arithmetic consequence and exact limitations

When \(a\equiv3\pmod8\), the established local-target theorem proves that the first actual away-from-p target is {0} for every odd good p. This theorem covers every bad-prime pattern and does not require any condition on multiplicities in a+1. Under rank one, the actual-target containment and endpoint-basepoint bridge therefore put the full restricted depth-two set inside (1). The four rational endpoints provide the reverse inclusion, proving (2).

This is a second-prime theorem, not an all-prime theorem. In fact at every good prime p≡1 modulo 4, both scalar heights vanish at (±i,0) for every reciprocal parameter a: the two quotient images agree and are two-torsion, while the coordinate change sends x=±i to u=∓i. Thus neither a=-5 nor a=-157469 can have a two-scalar intersection of only the four rational endpoints at p=5. Extra non-scalar directions can still exclude these points from the full depth-two set; passing the two scalar tests never proves full membership.

No rank assertion is made for additional parameters in the 2744 progression. The parameter a=-157469 is not eligible for this prime-7 result: 7 divides a−3, so 7 is bad for that curve.

Dependencies: the local-height double-integral formula and division identities from the existing prime-3 certificate; the established monic actual-target containment and endpoint-basepoint bridge; `../proofs/reciprocal_local_targets.md` for the exact first target. The script is a finite exact-arithmetic reproduction of the constants; Sections 3–5 supply all-orders analytic and parameter-continuity proofs.
