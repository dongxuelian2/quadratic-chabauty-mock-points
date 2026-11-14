# Exact isolation of the two height conditions at 3

## Status and scope

This note proves, with uniform estimates on all eight residue disks, that the intersection of the two actual-target height-zero conditions on

\[
 C:y^2=x^6-5x^4-5x^2+1
\]

is exactly

\[
 \{(0,1),(0,-1),\infty_+,\infty_-\}. \tag{A}
\]

The endpoint-basepoint containment needed for the first model is proved separately in [the endpoint bridge](endpoint_basepoint_bridge.md). Together with the second-model containment in PROOF.md, both height conditions are necessary for the Mordell–Weil-restricted, actual-local-image depth-two set. Rational-point containment therefore upgrades (A) to exact equality of that depth-two set with the four rational points. Both this disk argument and the separate bridge have passed independent review.

No assertion is made for a relaxed Selmer convention with arbitrary abelian Bloch–Kato classes.

## 1. Exact constants and splittings

Use

\[
 E:Y^2=X^3-8X^2+8X,\quad P=(1,1),\quad
 \omega=dX/(2Y),\quad W=\mathbf Q_3[(X-2)\omega].
\]

Put \(h=h_3(P)\), \(\ell=L(P)\), and \(\alpha=h/\ell^2\). The companion certificate proves

\[
 h\equiv2\pmod3. \tag{1}
\]

Let \(\zeta\) be the odd Coleman primitive with

\[
 d\zeta=-(X-2)\omega,\qquad
 \zeta(t)=t^{-1}+2t-8t^3+\cdots,\qquad
 d\lambda=-2\zeta\omega.
\]

Write \(Z=\zeta(P)\). There are exact valuation certificates

\[
 v_3(\ell)=1,\quad \ell/3\equiv2\pmod3,
 \qquad v_3(Z)=-1,\quad3Z\equiv1\pmod3. \tag{2}
\]

Indeed, with \(Q=3P\) and \(t_Q=-765/5311\), the differential expansion \(\omega=(1-8t^2+\cdots)dt\) and its integral coefficient bounds give

\[
 \ell=L(Q)/3=t_Q/3+O(3^4),\qquad
 \ell/3=-85/5311+O(3^3).
\]

Differentiating the division-polynomial multiplication identity gives

\[
 Z=\frac{\zeta(Q)}3-
    \frac{(D\log\psi_3)(P)}9,
 \qquad D=\frac d\omega.
\]

Here \((D\log\psi_3)(P)=-8/15\), while
\(\zeta(Q)=1/t_Q+O(3^2)\), so

\[
 Z=\frac1{3t_Q}+\frac8{135}+O(3)
  =-\frac{115}{51}+O(3).
\]

This proves (2), hence \(v_3(\alpha)=-2\).

For the second model use

\[
 C^*:v^2=-2u^6+10u^4+10u^2-2,
 \quad u=(x+1)/(x-1),\quad v=4y/(x-1)^3.
\]

Its identical quotients can be written

\[
 E':Y^2=Z_1^3+16Z_1^2+32Z_1,
 \qquad \omega'=dZ_1/(2Y),
 \qquad W'=\mathbf Q_3[(Z_1+4)\omega'].
\]

Choose \(s^2=-2\) in \(\mathbf Z_3^\times\). The twist isomorphism
\(\psi(X,Y)=(-2X,-2sY)\) transports the splittings. For
\(Q_\varepsilon=\psi(\varepsilon P)=(-2,-2\varepsilon s)\), \(\varepsilon\in\{1,-1\}\),

\[
 L'(Q_\varepsilon)=\varepsilon\ell/s,
 \quad\lambda'(Q_\varepsilon)=h+\log_3(2),
 \quad\zeta'(Q_\varepsilon)=\varepsilon sZ. \tag{3}
\]

The last identity follows by differentiating
\(\lambda'\circ\psi=\lambda+\log_3(2)\) and using
\(\psi^*\omega'=\omega/s\). Also

\[
 \alpha'=\frac{2h}{\ell^2},\qquad v_3(\alpha')=-2. \tag{4}
\]

## 2. Uniform integral estimates

All statements in this section hold for every \(z\in3\mathbf Z_3\), not just for a finite list of test values. Analytic functions are evaluated on that entire disk.

### Even regular functions

Suppose \(a(z),b(z)\in\mathbf Z_3[[z^2]]\). Define zero-constant primitives

\[
 I(z)=\int_0^z t a(t)dt,
 \qquad J(z)=\int_0^z a(t)dt.
\]

Coefficientwise integration gives

\[
 I(z)/z^2\in\mathbf Z_3,
 \qquad J(z)/z\in a(0)+3\mathbf Z_3. \tag{5}
\]

The first assertion uses
\(2k-2-v_3(2k)\ge0\) for \(k\ge1\). The second uses
\(2k-v_3(2k+1)\ge1\) for \(k\ge1\).

For a nested integral

\[
 D(z)=\int_0^z t b(t)\left(\int_0^t q a(q)dq\right)dt,
\]

one has

\[
 D(z)/z^2\in9\mathbf Z_3. \tag{6}
\]

To see this uniformly, the coefficient of \(z^{2n}\), \(n\ge2\), has valuation at least

\[
 -v_3(2n)-\lfloor\log_3(2n-2)\rfloor.
\]

After dividing its value by \(z^2\), the valuation is at least

\[
 2n-2-v_3(2n)-\lfloor\log_3(2n-2)\rfloor\ge2.
\]

For \(n=2\) this is direct; for \(n\ge3\), each subtracted term is at most \(n-2\). These coefficient estimates tend to infinity, so they prove convergence and the bound on the whole series.

### The singular height at the origin

For \(E\), write
\(\lambda(t)=-2\log_3t-2B_E(t)\), and for \(E'\) write
\(\lambda'(t)=-2\log_3t-2B_{E'}(t)\), with the normalizations in the companion certificate.
The same integral construction gives, for either curve,

\[
 v_3([t^{2k}]B)\ge-v_3(2k)-\lfloor\log_3(2k-1)\rfloor.
\]

The quadratic coefficients are \(-3\) and \(6\), respectively. Therefore

\[
 B(t)/t^2\in3\mathbf Z_3
 \quad\text{for every }t\in3\mathbf Z_3. \tag{7}
\]

For \(k\ge2\), the relevant valuation is bounded below by
\(2k-2-v_3(2k)-\lfloor\log_3(2k-1)\rfloor\ge1\).
The case \(k=2\) is immediate; for \(k\ge3\) one may use bounds \(k-2\) and \(k-1\) for the two subtracted terms.

If \(A(z)\) is an even integral analytic unit, then

\[
 \log_3(A(z)/A(0))/z^2\in\mathbf Z_3. \tag{8}
\]

Indeed \(A(z)/A(0)=1+z^2r(z)\) with integral \(r\), and every term of its logarithm divided by \(z^2\) is integral. These estimates also cover the value at zero by analytic continuation.

### Finite-point height variation

Suppose a map from the disk to one of the elliptic curves has pullback differential \(z a(z)dz\), and pullback second-kind differential \(z b(z)dz\), with \(a,b\) even and integral. If its endpoint primitive is \(\zeta_0\), then

\[
 \lambda(z)-\lambda(0)=-2\zeta_0 I(z)-2D(z).
\]

Equations (5) and (6) show

\[
 \frac{\lambda(z)-\lambda(0)}{z^2}\in3^{-1}\mathbf Z_3
 \quad\text{when }v_3(\zeta_0)=-1. \tag{9}
\]

In particular the variation belongs to \(3\mathbf Z_3\) throughout the disk. This is the required all-orders estimate; a bound on the derivative at the center alone would not suffice.

## 3. The first height isolates the rational endpoint disks

For \(x\in3\mathbf Z_3\), choose either sign of
\(y(x)=\varepsilon\sqrt{1-5x^2-5x^4+x^6}\). It is an even integral analytic unit, with \(y(0)=\varepsilon\).
The quotient maps are

\[
 f_1=(1+x^2,y),\qquad f_2=(1+x^{-2},y/x^3),
\]

and

\[
 f_1^*\omega=(x/y)dx,\qquad f_2^*\omega=-dx/y.
\]

Set

\[
 I(x)=\int_0^x t/y(t)dt,
 \qquad J(x)=\int_0^x dt/y(t).
\]

Then
\(L(f_1)=\varepsilon\ell+I\), \(L(f_2)=-J\), and
\(J/x\in\varepsilon+3\mathbf Z_3\).
The formal parameter of \(f_2\) is

\[
 t_2=-x(1+x^2)/y.
\]

Its singularity cancels the explicit logarithm, leaving

\[
 S(x):=-\lambda(f_2)-2\log_3x
      =2\log_3((1+x^2)/y)+2B_E(t_2).
\]

Equations (7) and (8) give \(S(x)/x^2\in\mathbf Z_3\). The first finite point is \(\varepsilon P\), so (9) gives
\((\lambda(f_1)-h)/x^2\in3^{-1}\mathbf Z_3\).
Since \(h-\alpha\ell^2=0\), the first height satisfies

\[
 \begin{aligned}
 \rho(x)/x^2
  ={}&\frac{\lambda(f_1)-h+S(x)}{x^2}
     -\alpha\frac{2\varepsilon\ell I+I^2}{x^2}
     +\alpha\left(\frac Jx\right)^2\\
  \in{}&3^{-1}\mathbf Z_3+\alpha(1+3\mathbf Z_3).
 \end{aligned}
\]

Because \(v_3(\alpha)=-2\), this cannot vanish. More precisely,

\[
 \boxed{\rho(x)/(\alpha x^2)\in1+3\mathbf Z_3
       \quad(0\ne x\in3\mathbf Z_3).} \tag{10}
\]

Thus the only height-zero point in either endpoint disk is \((0,\varepsilon)\). Reciprocal antisymmetry of \(\rho\) gives the corresponding uniqueness in each disk at infinity.

## 4. The second height excludes the other four disks

Now let \(u\in3\mathbf Z_3\), and choose

\[
 v(u)=\varepsilon s\sqrt{1-5u^2-5u^4+u^6}.
\]

The quotient maps to \(E'\) are

\[
 F_1=(-2(1+u^2),-2v),\qquad
 F_2=(-2(1+u^{-2}),-2v/u^3).
\]

Their differential pullbacks are \((u/v)du\) and \(-du/v\). Put

\[
 I(u)=\int_0^u t/v(t)dt,
 \qquad J(u)=\int_0^u dt/v(t).
\]

Then

\[
 L'(F_1)=\varepsilon\ell/s+I,
 \quad L'(F_2)=-J,
 \quad I\in u^2\mathbf Z_3,
 \quad J/u\in1/(\varepsilon s)+3\mathbf Z_3. \tag{11}
\]

As before the singular contribution has the form

\[
 S'(u)=2\log_3((1+u^2)/v)+2B_{E'}(-u(1+u^2)/v),
\]

so

\[
 S'(0)=-\log_3(2),\qquad S'(u)-S'(0)\in u^2\mathbf Z_3.
\]

By (3) and (9), the finite-height variation is in \(3\mathbf Z_3\). The terms
\(\alpha'(2\varepsilon\ell I/s+I^2)\) also lie in \(3\mathbf Z_3\), by (2), (4), and (11). Finally

\[
 \alpha'J^2\equiv\alpha'\frac{u^2}{s^2}
     =-h\frac{u^2}{\ell^2}\pmod3.
\]

The endpoint height is \(2h\), hence on the entire disk

\[
 \boxed{\rho^*(u)\equiv h\left(2-(u/\ell)^2\right)\pmod3.} \tag{12}
\]

Here \(u/\ell\in\mathbf Z_3\). Since \(h\) is a unit and 2 is not a square in \(\mathbf F_3\), the value in (12) is nonzero for every \(u\in3\mathbf Z_3\). Thus the second height has no zero in either disk above \(u=0\); reciprocal antisymmetry excludes its two infinity disks. These correspond exactly to the four original disks with \(x\equiv\pm1\pmod3\).

## 5. Actual targets and coverage

The second-model actual target is \(\{0\}\), as proved in Proposition 16 of the manuscript. The first-model actual target is also \(\{0\}\), as follows directly.

At 2 there are no points with \(x\in\mathbf Z_2^\times\), since
\(x^6-5x^4-5x^2+1\equiv8\pmod{16}\). If \(k=v_2(x)>0\), then \(f_1\) is integral and nonsingular on the minimal displayed elliptic model: its X-coordinate is odd, and the X-derivative of the Weierstrass equation is odd. Its local height is zero. The second image has X-valuation \(-2k\) and local height \(2k\log_3(2)\), exactly canceled by the term \(2\log_3|x|_2\). Negative k follows by reciprocity, and the endpoints by continuity. At every odd prime other than 3, good reduction gives the same integral/nonintegral cancellation. Hence all actual local images are zero.

Over \(\mathbf F_3\), the curve has exactly the six affine points with \(x\in\{0,1,-1\}\), \(y\in\{1,-1\}\), and its two rational points at infinity. The model is smooth. Thus its eight residue disks exhaust \(C(\mathbf Q_3)\).

All four rational endpoints lie in both height-zero sets directly. For the first height, the value at \((0,\varepsilon)\) is \(h-\alpha\ell^2=0\), and reciprocity gives zero at infinity. Their second-model coordinates have \(u=-1\) and \(u=1\), respectively. At \(u=1\) the elliptic images coincide; at \(u=-1\) they differ by negation. Evenness of the local heights, equality of the squared logarithms, and \(\log_3(\pm1)=0\) therefore give \(\rho^*=0\). Together with Sections 3 and 4, this proves the asserted intersection (A), including both inclusions without invoking the endpoint-basepoint bridge.

By the endpoint-basepoint bridge, every point in the Mordell–Weil-restricted, actual-local-image depth-two set lies in that intersection. Conversely all four points in (A) are rational, so their global Kummer classes satisfy the required conditions. This gives exact equality of the full restricted depth-two set with (A), not merely an upper bound.

## Source and verification

The analytic local-height identity used here is Balakrishnan–Besser, Theorem 4.1, https://arxiv.org/html/1201.6016#S4 . The companion height certificate proves the exact nonvanishing and identifies the CM unit-root splitting. The script `../scripts/check_prime3_height.py` verifies the finite exact constants and representative coefficient inequalities; the uniform estimates for every series coefficient are proved above.

