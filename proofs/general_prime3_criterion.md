# A finite valuation criterion for two-height isolation in the reciprocal family

Status: independently reviewed research proof. This note proves a general, finite-constant criterion and an explicit parameter neighborhood in which its analytic hypotheses hold. It does not assert rank one, zero local targets, or infinitely many full examples in that neighborhood. The depth-two consequence uses the Mordell–Weil-restricted, actual-local-image convention and the endpoint-basepoint bridge already proved separately.

## 1. The two elliptic quotients for a general parameter

Let a be an odd integer, a ≡ 1 (mod 3), with a ≠ −1,3, and put

\[
 A=a-3,\qquad d=(a+1)/2,\qquad b=(15-a)/(a+1).
\]

Use the shifted first quotient

\[
 E_a:Y^2=X^3+AX^2-AX,\qquad P=(1,1),\qquad \omega=dX/(2Y).
\]

The two maps from \(C_a:y^2=x^6+ax^4+ax^2+1\) are

\[
 f_1=(1+x^2,y),\qquad f_2=(1+x^{-2},y/x^3).
\]

The rational change of variables

\[
 u=(x+1)/(x-1),\qquad v=4y/(x-1)^3
\]

gives the reciprocal, nonmonic model

\[
 C_a^*:v^2=d(u^6+bu^4+bu^2+1).
\]

Its identical elliptic quotients, after shifting the quotient coordinate, are

\[
 E_a':Y^2=Z^3-2AZ^2+A(A+4)Z,
\]

with maps

\[
 F_1=(d(1+u^2),dv),\qquad F_2=(d(1+u^{-2}),dv/u^3).
\]

The isogeny

\[
 \phi:E_a\longrightarrow E_a',\qquad
 (X,Y)\longmapsto (X+A-A/X,\;Y(1+A/X^2))
\]

has degree two and satisfies \(\phi^*\omega'=\omega\). In particular
\(\phi(P)=(1,a-2)\). These assertions hold for every nonsingular parameter, not only the CM parameter a=−5.

Choose the complements

\[
 W=\mathbf Q_3[(X-2)\omega],\qquad
 W'=\mathbf Q_3[(Z-a-1)\omega'].
\]

They are compatible. Indeed,

\[
 d(Y/X)=(X+A/X)\omega,
\]

and therefore

\[
 \phi^*((Z-a-1)\omega')=2(X-2)\omega-d(Y/X).
\]

For compatible global heights, isogeny functoriality gives

\[
 h'(\phi(P))=2h(P),\qquad L'(\phi(P))=L(P),
 \qquad \alpha'=2\alpha,
 \quad \alpha=h(P)/L(P)^2. \tag{1}
\]

The heights need not be unit-root heights away from a=−5. This causes no change in either quadratic Chabauty function: changing an elliptic height splitting adds the same constant multiple of \(L^2\) to its local height and its global quadratic correction, and the two changes cancel in \(\lambda-\alpha L^2\).

All three curves have good reduction at 3. The first genus-two curve has exactly eight rational residue disks: two each above x=0, x=1, x=−1 and infinity. The last four are the u=0 and u=infinity disks of the second model. Since d ≡ 1 (mod 3), choose \(s\in\mathbf Z_3^\times\) with \(s^2=d\), and put

\[
 Q=(d,ds)\in E_a'(\mathbf Q_3).
\]

Changing s to −s changes the signs of logarithms and odd primitives but changes none of the criteria below.

## 2. The finitely many constants to certify

Use the normalized local heights and the odd primitives

\[
 d\zeta=-(X-2)\omega,\quad d\lambda=-2\zeta\omega,
 \qquad
 d\zeta'=-(Z-a-1)\omega',\quad d\lambda'=-2\zeta'\omega'.
\]

Set

\[
 \ell=L(P),\quad h=\lambda(P),\quad Z=\zeta(P),\quad
 m=L'(Q),\quad Z'=\zeta'(Q),
\]

\[
 \alpha=h/\ell^2,\qquad
 K=\lambda'(Q)-\log_3d-2\alpha m^2,
 \qquad C=18\alpha/d. \tag{2}
\]

Here h equals the global height of P. In the original integral model P is (0,1), so it is nonsingular at every odd prime by the derivative with respect to Y, and at 2 by the derivative with respect to X, namely −a. The normalized away-from-3 local heights are consequently zero. This observation applies to P only; it does **not** prove that either curve's whole actual-local-image target is zero.

The finite analytic certificate is

\[
 v_3(\ell)=1,\quad v_3(h)=0,\quad
 v_3(Z)\ge-1,\quad v_3(m)\ge1,\quad v_3(Z')\ge-1,
 \quad K\equiv C\not\equiv0\pmod3. \tag{H}
\]

The last congruence includes \(K\in\mathbf Z_3\). Under the other hypotheses C is already a unit, since \(v_3(\alpha)=-2\).

Let \(\Omega,\Omega'\subset\mathbf Q_3\) be the finite targets used for the two height conditions, with \(0\in\Omega\cap\Omega'\). Impose the following explicit tests:

- **First-target test.** No nonzero \(w\in\Omega\cup(-\Omega)\) has both \(v_3(w)=2n\ge0\) and
  \[
  3^{-2n}w/(9\alpha)\equiv1\pmod3. \tag{T1}
  \]
- **Second-target test.** Every integral element of \(\Omega'\) lies in \(3\mathbf Z_3\):
  \[
  \Omega'\cap\mathbf Z_3\subseteq3\mathbf Z_3. \tag{T2}
  \]

Elements of negative valuation automatically satisfy the needed exclusions. In (T1), odd valuations are automatically excluded; at an even nonnegative valuation the displayed residue must be the nonsquare 2. These are finite valuation and residue tests, not assertions about zero sets of analytic functions. In particular \(\Omega=\Omega'=\{0\}\) satisfies both tests.

## 3. General two-height theorem

**Theorem.** Suppose (H), (T1), and (T2) hold. Then

\[
 \{z\in C_a(\mathbf Q_3):\rho_a(z)\in\Omega,
       \ \rho_a^*(z)\in\Omega'\}
 =\{(0,1),(0,-1),\infty_+,\infty_-\}. \tag{3}
\]

The definition of \(\rho_a^*\) uses the second model and \(\alpha'=2\alpha\). If, in addition, \(E_a(\mathbf Q)\) has rank one and \(\Omega,\Omega'\) are valid actual-local-image targets (or supersets of them), the actual-target containment and endpoint-basepoint bridge imply

\[
 C_a(\mathbf Q_3)_2=C_a(\mathbf Q)
 =\{(0,1),(0,-1),\infty_+,\infty_-\} \tag{4}
\]

for the stated restricted Selmer convention.

### Proof: uniform estimates, not only Taylor leading terms

For either elliptic curve write \(\lambda(t)=-2\log_3t-2B(t)\). The formal coefficients are obtained by integrating integral even series. Uniformly for t ∈ 3 Z_3,

\[
 B(t)/t^2\in3\mathbf Z_3. \tag{5}
\]

For completeness, for a model \(Y^2=X^3+A_2X^2+A_4X\) and complement \((X+c)\omega\), the coefficient of t² in B is \((A_2-c)/2\). In our two models these coefficients are \((a-1)/2\) and \((7-a)/2\), respectively, and both are divisible by 3. For all k ≥ 2 the coefficient bound is

\[
 v_3([t^{2k}]B)\ge-v_3(2k)-\lfloor\log_3(2k-1)\rfloor.
\]

Thus, after division by t², every such term has valuation at least
\(2k-2-v_3(2k)-\lfloor\log_3(2k-1)\rfloor\ge1\), tending to infinity. This proves (5) for the whole series.

If a(z), b(z) are integral even power series and z ∈ 3 Z_3, coefficientwise integration gives

\[
 z^{-2}\int_0^z t a(t)dt\in\mathbf Z_3,
 \qquad z^{-1}\int_0^z a(t)dt\in a(0)+3\mathbf Z_3,
\]

\[
 z^{-2}\int_0^z t b(t)\left(\int_0^t q a(q)dq\right)dt
 \in9\mathbf Z_3. \tag{6}
\]

The first bound follows from \(2k-2-v_3(2k)\ge0\); the second from \(2k-v_3(2k+1)\ge1\) for k ≥ 1. For the nested integral, its coefficient of z^(2n), n ≥ 2, has valuation at least \(-v_3(2n)-\lfloor\log_3(2n-2)\rfloor\); after division by z² the bound is at least 2 and tends to infinity. An even integral unit U also satisfies \(\log_3(U(z)/U(0))/z^2\in\mathbf Z_3\).

On either x=0 disk, let \(y(x)=\varepsilon\sqrt{1+ax^2+ax^4+x^6}\), and define

\[
 I=\int_0^x t/y(t)dt,\qquad J=\int_0^x dt/y(t).
\]

The logarithms are \(\varepsilon\ell+I\) and −J. The finite-height variation divided by x² belongs to \(3^{-1}\mathbf Z_3\), by (6) and \(v_3(Z)\ge-1\). The singular second height cancels the explicit logarithm because its parameter is \(-x(1+x^2)/y\). Its regularized variation divided by x² is integral by (5). Hence

\[
 \rho_a(x)/x^2\in3^{-1}\mathbf Z_3+\alpha(1+3\mathbf Z_3),
\]

and therefore

\[
 \frac{\rho_a(x)}{\alpha x^2}\in1+3\mathbf Z_3
 \qquad(0\ne x\in3\mathbf Z_3). \tag{7}
\]

Indeed, \(2\ell I\alpha/x^2\) has valuation at least −1, \(I^2\alpha/x^2\) has valuation at least 0, and \((J/x)^2\in1+3\mathbf Z_3\). Thus every nonzero value in either disk has nonnegative even valuation and leading residue prescribed in (T1). Its value cannot be in \(\Omega\). At x=0 it is zero. Reciprocity gives the identical conclusion at infinity, using the symmetrization in (T1).

Actual reciprocal local-image targets are symmetric, because reciprocity negates each local contribution. Thus the symmetrization in (T1) makes no change for actual targets.

On either u=0 disk, put \(v(u)=\varepsilon s\sqrt{1+bu^2+bu^4+u^6}\). The pullbacks of \(\omega'\) are \((u/v)du\) and \(-du/v\). With I and J defined as before using v in place of y, the logarithms are \(\varepsilon m+I\) and −J. The finite-height variation belongs to \(3\mathbf Z_3\), since \(v_3(Z')\ge-1\). The variation of the singular regularized height is in u² Z_3, its constant being \(-\log_3d\). Also

\[
 \alpha'(2\varepsilon mI+I^2)\in3\mathbf Z_3,
 \qquad
 \alpha'J^2\equiv(2\alpha/d)u^2\pmod3.
\]

It follows uniformly on the entire disk that

\[
 \rho_a^*(u)\equiv K+C(u/3)^2\pmod3. \tag{8}
\]

Under (H), the right side has residues C and 2C and never vanishes. Every second-height value on these disks is a unit. Reciprocity gives the same conclusion at u=infinity, so (T2) excludes all four disks corresponding to x ≡ ±1 (mod 3).

Finally the four listed endpoints have first height zero. In the second model their u-coordinates are ±1; the two elliptic images then agree or are negatives. Even local heights, squared logarithms and \(\log_3(\pm1)=0\) give second height zero. Since both targets contain zero, these four points lie in the intersection. This proves (3). Rank one and the established containment give the upper inclusion in (4); global Kummer classes of rational points give the reverse inclusion. ∎

**Simplification for symmetric actual targets.** Since −1 is a nonsquare in Q_3, a symmetric target containing a nonzero element of even nonnegative valuation necessarily violates (T1): exactly one of w and −w has the allowed square residue. Thus, for symmetric targets, (T1) is equivalent to saying that every nonzero target has either negative valuation or odd valuation. This is still more general than requiring the target to be zero.

## 4. An explicit parameter neighborhood for the analytic certificate

**Proposition.** Every odd integer

\[
 a\equiv-5\pmod{3^6} \tag{9}
\]

satisfies (H), using the complements above. More precisely,

\[
 \ell/3\equiv2,\qquad h\equiv2,\qquad
 9\alpha\equiv2,\qquad K\equiv C\equiv1\pmod3,
\]

and \(v_3(m)=1\), \(v_3(Z)=v_3(Z')=-1\). In particular P is nontorsion for every such parameter. This proposition makes no rank-one or local-target assertion.

### A quantitative continuity lemma

Consider two good integral models \(Y^2=X^3+A_2X^2+A_4X\), integral complements \((X+c)\omega\), and integral points R with unit Y-coordinate. Suppose all coefficients and point coordinates agree modulo \(3^M\), M ≥ 6. Suppose, at the first specialization, \(v_3(t(3R))=2\), the numerator \(\Phi_3\) of X(3R) is a unit, and the numerator \(\Omega_3\) of Y(3R) is a unit. Here

\[
 X(3R)=\Phi_3/\psi_3^2,\quad
 Y(3R)=\Omega_3/\psi_3^3,\quad
 t(3R)=-\Phi_3\psi_3/\Omega_3.
\]

Then the second specialization has the same unit and valuation properties, and the differences of its normalized constants satisfy

\[
 \Delta L(R)\in3^{M-1}\mathbf Z_3,
 \quad\Delta\lambda(R)\in3^{M-2}\mathbf Z_3,
 \quad\Delta\zeta(R)\in3^{M-6}\mathbf Z_3. \tag{10}
\]

To prove this, all division-polynomial numerators are integral polynomials in the coefficients and point coordinates; the displayed unit denominators show \(\Delta t(3R)\in3^M\mathbf Z_3\) and \(\Delta(\psi_3/t(3R))\in3^M\mathbf Z_3\). In particular both t-values have valuation 2 and both ψ_3-values have valuation 2.

The formal logarithm coefficients have denominators 2k+1, the primitive coefficients have the same denominators, and the double primitive B has the coefficient bounds proved above. Their numerators are integral polynomials in the coefficients. At t of valuation 2, these bounds, together with \(\Delta t\in3^M\mathbf Z_3\), give

\[
 \Delta L(t)\in3^M\mathbf Z_3,
 \quad \Delta B(t)\in3^{M+2}\mathbf Z_3,
 \quad\Delta\zeta(t)\in3^{M-4}\mathbf Z_3.
\]

For the last estimate the possible loss of four powers of 3 comes only from \(\Delta(1/t)\). For B the lowest possible bound comes from its quadratic term; for higher terms the exponent bounds increase without limit, so these are bounds for the full convergent series. The logarithm of the unit \(\psi_3/t\) changes by an element of \(3^M\mathbf Z_3\).

Now use the exact multiplication identities

\[
 L(R)=L(3R)/3,
\]

\[
 \lambda(R)=\frac{2}{9}
  \left(\log_3\frac{\psi_3(R)}{t(3R)}-B(t(3R))\right),
\]

\[
 \zeta(R)=\frac{\zeta(3R)}3
     -\frac{(D\log\psi_3)(R)}9,
 \qquad D=d/\omega. \tag{11}
\]

The numerator of \(D\log\psi_3\) is an integral polynomial, and its denominator ψ_3 has valuation 2. Thus its variation has valuation at least M−4; division by 9 loses at most two further powers. These observations prove (10). They deliberately use a conservative bound; M=6 is sufficient, not asserted minimal. No theorem about variation of unit-root splittings is needed.

### Application at the CM specialization

At a_0=−5, the exact companion certificate proves

\[
 \ell_0/3\equiv2,\quad h_0\equiv2,\quad
 v_3(Z_0)=-1,\quad v_3(t(3P))=2.
\]

The division numerator units follow either from the exact coordinates
\(3P=(289/2025,90287/91125)\), \(\psi_3(P)=-45\), or from good reduction and the formal parameter valuations.

Choose \(s_0^2=-2\). At this specialization the twist isomorphism
\((X,Y)\mapsto(-2X,-2s_0Y)\) sends P to Q_0 and transports the chosen complements. Consequently

\[
 m_0=\ell_0/s_0,\quad Z_0'=s_0Z_0,
 \quad\lambda'(Q_0)=h_0+\log_3 2,
 \quad K_0=2h_0.
\]

It also transports 3P to 3Q_0, preserving the parameter valuation 2 and the required unit numerators.

For a satisfying (9), the branch \(s^2=(a+1)/2\) with \(s\equiv s_0\pmod3\) satisfies \(s-s_0\in3^6\mathbf Z_3\): factor \((s-s_0)(s+s_0)=d-d_0\), and use that \(s+s_0\) is a unit. The two elliptic models, their complement coefficients, P, and Q therefore all agree with the specializations to the precision required in (10). It follows that

\[
 \ell-\ell_0,\ m-m_0\in3^5\mathbf Z_3,
 \quad h-h_0,\ \lambda'(Q)-\lambda'(Q_0)\in3^4\mathbf Z_3,
\]

\[
 Z-Z_0,\quad Z'-Z_0'\in\mathbf Z_3.
\]

Hence the claimed logarithm and primitive valuations persist. Writing \(9\alpha=h/(\ell/3)^2\) shows \(9\alpha\equiv2\pmod3\). Also

\[
 K=\lambda'(Q)-\log_3d-2(9\alpha)(m/3)^2
\]

reduces to \(K_0=2h_0\equiv1\pmod3\), while
\(C=2(9\alpha)/d\equiv1\pmod3\). This proves (H) and the proposition. ∎

## 5. An arithmetic parameter-family theorem

**Theorem (full depth-two equality with the exact target-integrality criterion).** Let a be an integer satisfying

\[
 a\equiv-5\pmod{5832},\qquad
 \operatorname{rank}E_a(\mathbf Q)=1.
\]

Suppose that, for every odd prime q dividing a+1 for which \((2/q)=1\),

\[
 v_3\bigl(v_q(a+1)\bigr)<v_3(q^2-1). \tag{12}
\]

No multiplicity restriction is imposed at primes with \((2/q)=-1\). Then, for the Mordell–Weil-restricted, actual-local-image depth-two convention,

\[
 C_a(\mathbf Q_3)_2=C_a(\mathbf Q)
 =\{(0,1),(0,-1),\infty_+,\infty_-\}. \tag{13}
\]

**Proof.** Since \(5832=8\cdot3^6\), the congruence gives both the analytic certificate (H) proved in Section 4 and a ≡ 3 (mod 8). The exact local-target theorem in `../proofs/reciprocal_local_targets.md` gives first actual target \(\Omega=\{0\}\). Its second actual local contributions vanish at 2 and at odd primes not dividing a+1. At an odd q dividing a+1, put m=v_q(a+1) and e=v_3(q²−1). Here q ≠ 3 and

\[
 v_3(\log_3q)=e\ge1.
\]

The possible coefficients of \(\log_3q\) are

\[
 0,\qquad \pm\frac{2k(m-k)}m\quad(1\le k\le\lfloor m/2\rfloor)
\]

in the split case; in the nonsplit case they are 0 for odd m, or \(0,\pm m/2\) for even m. Nonsplit coefficients are always 3-integral. Split coefficients have valuation at least −v_3(m), so (12) makes every local contribution lie in \(3\mathbf Z_3\). The second actual target consequently satisfies \(\Omega'\subseteq3\mathbf Z_3\). Conditions (T1) and (T2) follow, and the rank-one two-height theorem proves (13). ∎

**Precision of the arithmetic hypothesis.** Under the congruence a ≡ −5 (mod 5832), condition (12) is necessary and sufficient for \(\Omega'\subseteq3\mathbf Z_3\), as proved in the cited local-target theorem. Indeed, if 3 divides a split multiplicity m, the attained k=1 coefficient has valuation exactly −v_3(m); if 3 does not divide m, all coefficients are integral and (12) holds automatically. Each local image contains zero, so a failing individual contribution also occurs in the global target. This is an exact criterion for the stated **target containment**, not a necessary criterion for (T2), which also permits targets of negative valuation, and not a necessary criterion for the full depth-two equality itself.

**Easy corollaries.** The theorem applies if

\[
 3\nmid v_q(a+1)\quad\text{for every odd }q\mid a+1.
\]

An easier sufficient condition is that the odd part of a+1 be squarefree. Under the displayed congruence, \(v_2(a+1)=2\), so this means precisely that \(|a+1|/4\) is squarefree. In this special case both actual targets are exactly \(\{0\}\). All these corollaries retain the rank-one hypothesis.

This is a conditional parameter-family theorem with an explicit, proved analytic and local arithmetic part. It does not assert infinitely many rank-one parameters in this progression.

**The refinement is strictly broader than the 3-free-multiplicity corollary.** For

\[
 a=10631731=-5+1823\cdot5832,
 \qquad a+1=4\cdot17^3\cdot541,
\]

the prime 17 is split, m=3, but \(v_3(17^2-1)=2>v_3(3)=1\). The other odd multiplicity is 1, and 541 is prime. Hence the refined criterion holds although the 3-free-multiplicity hypothesis fails. In fact the exact second target is

\[
 \Omega'=\{0,\ \pm(4/3)\log_3 17\}\subset3\mathbf Z_3,
\]

with its nonzero elements of valuation 1. The analytic certificate also holds. No rank-one claim or full-equality claim is made for this parameter without a rank certificate.

### The local-target restriction is genuinely additional

Take

\[
 a=23323=-5+4\cdot5832,
 \qquad a+1=4\cdot7^3\cdot17.
\]

The full analytic certificate (H) holds, and is also checked directly by `../scripts/check_general_prime3.py`. At q=7, however, 2 is a square modulo 7, m=3, and

\[
 v_3(m)=v_3(7^2-1)=1.
\]

In the second model, u=7 is locally realized: its equation has right side of 7-adic valuation 2 and square unit residue 1 modulo 7, so Hensel's lemma supplies v. The exact local-target formula gives

\[
 w_7^*(u,v)=-\frac43\log_3 7,
 \qquad v_3(w_7^*)=0.
\]

Thus the second actual target contains a unit even **inside** the analytic parameter progression. This example shows why 3-adic proximity alone cannot supply the target hypothesis. No rank assertion is made for a=23323, and this local-target obstruction is not claimed to be a counterexample to full depth-two equality.

## 6. A second fully explicit parameter

The parameter

\[
 a=-157469=-5-27\cdot5832
\]

has \(a+1=-4\cdot39367\), where 39367 is prime. The exact two-isogeny descent certificate in `../proofs/rank_one_parameter_157469.md` and `../scripts/check_rank_one_parameter.py` proves \(\operatorname{rank}E_a(\mathbf Q)=1\): the two descent images have size at most 2 and 4, respectively, while the certified nonzero logarithm of P gives rank at least one. Thus all hypotheses of the preceding theorem are verified for this parameter, and (13) holds for it. Both actual targets are zero here. The separate independent review of the rank certificate has passed, including a second implementation that tests every primitive residue pair. The complete reproducible obstruction list is supplied.

## 7. What is actually established, and what remains arithmetic

1. The theorem is a genuine sufficient criterion for exact equality, reduced to finitely many endpoint constants and finite target valuations/residues. The all-orders estimates are proved, rather than inferred from a truncated power series or a sample of points.
2. The analytic conditions hold for every odd a ≡ −5 (mod 729), with no unproved height nonvanishing assumption. This proves h(P) is a 3-adic unit for these parameters with the specified splitting. It also proves P is nontorsion.
3. For any such parameter with rank one and targets satisfying (T1)–(T2), the full restricted depth-two equality follows. Section 5 supplies a concrete congruence and multiplicity criterion ensuring those target conditions; the squarefree-odd-part special case gives both targets {0}.
4. The already verified a=−5 case is a complete example. The new exact rank-one certificate supplies a second complete example, a=−157469, as detailed in Section 6. For contrast, a=5827=−5+8·729 satisfies the analytic and squarefree-odd-part target conditions, but its rank has not been proved to be one here; it is not claimed as another full equality example.
5. No claim is made that infinitely many parameters in the progression have rank one, that rank one forces nonzero heights in general, or that an actual target remains zero merely because a is close to −5 at 3.

Dependencies: the exact base certificate and uniform-series bounds are recorded in `../proofs/prime3_height_certificate.md` and `../proofs/prime3_disk_isolation.md`. The arithmetic family theorem uses `../proofs/reciprocal_local_targets.md`; the new rank certificate is `../proofs/rank_one_parameter_157469.md`, with exact scripts and complete obstruction output. The depth-two upgrade uses `../proofs/endpoint_basepoint_bridge.md` and the general nonmonic containment theorem in the manuscript. The local-height double-integral formula is Balakrishnan–Besser, Theorem 4.1, https://arxiv.org/html/1201.6016#S4 .
