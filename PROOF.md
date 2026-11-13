# Exact mechanisms for bielliptic height candidates

## 1. Scope and conventions

Balakrishnan's ICM survey [1, Problem 6.4] asks for an explanation of mock rational points on genus-two curves of Jacobian rank two. We study the explicitly defined **one-function bielliptic height-candidate set** below. For the standard local targets discussed below, this is a single-correspondence height condition; membership alone does not establish membership in the full depth-two Chabauty–Kim set.

Throughout, depth-two Selmer sets use the Mordell–Weil abelian-image convention specified in Section 13; no unrestricted Bloch–Kato identification is inferred from rank alone.

Let

\[
 C:y^2=f(x)=a_6x^6+a_4x^4+a_2x^2+a_0
\]

have integral coefficients, with \(a_0a_6\ne0\) and \(f\) squarefree. Its elliptic quotients are

\[
\begin{aligned}
 E_1 &:Y^2=g_1(X)=X^3+a_4X^2+a_2a_6X+a_0a_6^2,\\
 E_2 &:Y^2=g_2(X)=X^3+a_2X^2+a_4a_0X+a_6a_0^2,
\end{aligned}
\]

with maps

\[
 \phi_1(x,y)=(a_6x^2,a_6y),\qquad
 \phi_2(x,y)=(a_0/x^2,a_0y/x^3).
\]

Assume both elliptic curves have rational rank one. Fix an odd prime \(p\) of good reduction for this model, in particular \(p\nmid a_0a_6\), and fix the height splittings. Write \(L_i\) for the elliptic logarithm and \(\lambda_{i,p}\) for the local height normalized by

\[
 \lambda_{i,p}(P)=-2\log_p(t(P))+O(t(P)),\qquad t=-X/Y,
\]

near the origin. Use \(\log_p(p)=0\). For any nontorsion \(P_i\in E_i(\mathbb Q)\), put
\(\alpha_i=h_i(P_i)/L_i(P_i)^2\). The Bianchi–Padurariu function [2, Theorem 2.3] is

\[
 \rho_p(z)=\lambda_{1,p}(\phi_1z)-\lambda_{2,p}(\phi_2z)
 -2\log_p x(z)-\alpha_1L_1(\phi_1z)^2+\alpha_2L_2(\phi_2z)^2.
 \tag{1}
\]

It extends across \(x=0,\infty\). We denote the extension by the same symbol.

To specify the target without hiding the local conditions, let \(S\) be a finite set of primes not containing \(p\), and let \(B\subset\mathbb Q^S\) be finite. Define

\[
 \Omega_{p,B}=\left\{\sum_{q\in S}c_q\log_pq:c\in B\right\},\qquad
 A_{p,B}=\{z\in C(\mathbb Q_p):\rho_p(z)\in\Omega_{p,B}\}.
 \tag{2}
\]

The coarse local-height target in [2, Theorem 2.3] has this form. So does the sharper target obtained by taking the actual local images of

\[
 w_q(z)=-\lambda_{1,q}(\phi_1z)+\lambda_{2,q}(\phi_2z)
             +2\log_p|x(z)|_q.
 \tag{3}
\]

Here \(\lambda_{i,q}\) is the local height for the displayed elliptic model; changes to a minimal model require the corresponding height correction. At \(x=0\) and \(x=\infty\), use the continuous extensions of (3). The coefficients of these local images are rational multiples of \(\log_pq\) and independent of the chosen good prime \(p\). Take \(S\) large enough to contain every nonzero contribution. For these two choices of target, rational points belong to \(A_{p,B}\).

## 2. A local height identity at two-torsion

**Lemma 1.** On \(E:Y^2=g(X)\), with the preceding normalization, a nonzero two-torsion point \(T=(e,0)\in E(\mathbb Q_p)\) satisfies

\[
 \lambda_p(T)=\frac12\log_p g'(e).
 \tag{4}
\]

**Proof.** The standard local-height multiplication formula is

\[
 \lambda_p(2P)=4\lambda_p(P)-2\log_p(2Y(P)).
 \tag{5}
\]

This is the \(m=2\) case of the division-polynomial identity in [3, Section 2.1.2]. As \(P\to T\), the doubling formula gives

\[
 X(2P)=\frac{g'(X(P))^2}{4Y(P)^2}-A_2-2X(P),
 \qquad
 \frac{t(2P)}{2Y(P)}\longrightarrow\frac1{g'(e)}.
\]

Substitute the normalized expansion at the origin into (5), cancel the logarithmic singularities, and take the limit. The result is
\(4\lambda_p(T)=2\log_p g'(e)\). This also shows that the value is independent of the height splitting. ∎

The two-torsion evaluation is a standard identity, not a new height formula; compare also Balakrishnan–Besser [4, Proposition 6.1].

## 3. An exact algebraic criterion for every Weierstrass point

**Theorem 2.** Let \(r\in\overline{\mathbb Q}\) satisfy \(f(r)=0\), and fix an embedding \(\mathbb Q(r)\hookrightarrow\mathbb Q_p\). Write \(W=(r,0)\). Then

\[
 \rho_p(W)=\frac12\log_p\left(\frac{a_6}{a_0r^2}\right).
 \tag{6}
\]

Choose a positive integer \(d\) such that \(dc_q\in\mathbb Z\) for every \(c\in B\) and every \(q\in S\). Then \(W\in A_{p,B}\) if and only if, for some \(c\in B\), the algebraic number

\[
 U_c=\left(\frac{a_6}{a_0r^2}\right)^d
                 \prod_{q\in S}q^{-2dc_q}
 \tag{7}
\]

is a root of unity.

**Proof.** Both images of \(W\) are nonzero two-torsion points, so both elliptic logarithms in (1) vanish. Set
\(H=3a_6r^4+2a_4r^2+a_2\). Squarefreeness and \(r\ne0\) give \(H\ne0\). Direct differentiation, using \(f(r)=0\), gives

\[
 g_1'(a_6r^2)=a_6H,\qquad
 g_2'(a_0/r^2)=-\frac{a_0}{r^2}H.
\]

By Lemma 1 their local-height difference is
\(\tfrac12\log_p(-a_6r^2/a_0)\). Subtracting \(2\log_pr\) proves (6), since \(\log_p(-1)=0\).

The root \(r\) is a \(p\)-adic unit: if its valuation were positive, the constant term of \(f(r)\) would be the unique term of smallest valuation; if negative, the leading term would be. Both contradict \(f(r)=0\). Therefore \(U_c\) is a \(p\)-adic unit. By (6), equality with the target indexed by \(c\) is equivalent to \(\log_p U_c=0\). The kernel of \(\log_p\) on \(\mathbb Z_p^\times\) is \(\mu_{p-1}\). An embedding of number fields is injective, so its image is a root of unity if and only if \(U_c\) itself is. This proves both directions. ∎

**Consequences.**

1. For fixed coefficients and fixed \(B\), a Weierstrass point either passes at every eligible prime admitting its field embedding or at none. The prime controls local visibility, not the algebraic test (7).
2. Every Galois conjugate passes the same algebraic test. Among conjugates actually lying in \(\mathbb Q_p\), membership is uniform.
3. Membership can be decided by exact number-field arithmetic: construct (7) for each target vector and test whether it is a root of unity. No finite-precision logarithmic equality is needed.

This uses the logarithmic-kernel strategy already present in Bianchi's elliptic work [3, Theorem 3.18]. The result here is its explicit application to the difference of the two elliptic heights at a genus-two Weierstrass point.

**Corollary 3 (unit obstruction).** If \(a_6=1\) and \(a_0\in\{1,-1\}\), then

\[
 W\in A_{p,B}
 \quad\Longleftrightarrow\quad
 r\text{ is a root of unity and }0\in B.
 \tag{8}
\]

Equivalently, the last condition is \(0\in\Omega_{p,B}\).

**Proof.** Every root of the monic polynomial \(f\), whose constant term is a unit, is an algebraic unit. If (7) is a root of unity, valuations at primes of \(\mathbb Q(r)\) above each \(q\in S\) give \(c_q=0\). Equation (7) then implies that \(r\) is a root of unity. The converse is immediate. Finally, if \(\sum c_q\log_pq=0\), clearing denominators gives a positive rational number, supported on \(S\), in the kernel of \(\log_p\). Its \(p\)-valuation is zero; it must be 1, and unique factorization gives \(c=0\). ∎

## 4. Reciprocal symmetry and non-Weierstrass candidates

Consider the parameter family

\[
 C_a:y^2=x^6+ax^4+ax^2+1,\qquad a\in\mathbb Z\setminus\{-1,3\}.
 \tag{9}
\]

The discriminant of the sextic is \(-64(a-3)^6(a+1)^2\), so these are smooth genus-two curves. Both quotients are the same elliptic curve

\[
 E_a:Y^2=X^3+aX^2+aX+1.
\]

Assume \(\operatorname{rank}E_a(\mathbb Q)=1\), so that \(\operatorname{rank}\operatorname{Jac}(C_a)(\mathbb Q)=2\), and use the same height splitting on the two identical quotients.

**Theorem 4.** For every odd good model prime \(p\):

(a) Every point

\[
 (\pm1,\pm\sqrt{2(a+1)})\in C_a(\mathbb Q_p)
 \tag{10}
\]

has \(\rho_p=0\). If \(2(a+1)\notin\mathbb Q^{\times2}\), these are nonrational, non-Weierstrass points.

(b) With the coarse Bianchi–Padurariu target, \(0\in\Omega\), so every point (10) is a mock candidate. The Weierstrass candidates are precisely those whose \(x\)-coordinates are roots of unity.

(c) If \(a\) is odd, the same statements hold for the sharper target formed from the actual local images (3).

**Proof.** At \(x=1\), the two elliptic images coincide. At \(x=-1\), they are negatives. Local heights are even and squares of elliptic logarithms are unchanged by negation. Since the quotients and splittings are identical, \(\alpha_1=\alpha_2\); also \(\log_p(\pm1)=0\). Thus all terms in (1) cancel in pairs, proving (a).

For (b), the two integral local-height sets \(W_q^{E_a}\) are identical and nonempty, since \((0,1)\in E_a(\mathbb Q)\). As \(a_0=a_6=1\), the coarse target includes \(-W_q^{E_a}+W_q^{E_a}\), hence includes 0 at each prime. Corollary 3 gives the Weierstrass assertion.

For (c), use the rational point \(z_0=(0,1)\in C_a(\mathbb Q)\). The extension of (3) at this point is

\[
 w_q(z_0)=-\lambda_q((0,1)).
\]

The elliptic point \((0,1)\) reduces nonsingularly at every odd prime, because the derivative with respect to \(Y\) is 2. At 2 the derivative with respect to \(X\) is \(-a\), which is odd. Thus \(\lambda_q((0,1))=0\) for every \(q\ne p\), by [2, Proposition 2.2(a)]. Each actual local target contains 0. Corollary 3 applies again. ∎

For this family the root-of-unity test is particularly explicit:

\[
 f_a(x)=(x^2+1)(x^4+(a-1)x^2+1).
\]

If a root \(r\) of the quartic is a root of unity, then \(u=r^2\) is a root of unity and \(u+u^{-1}=1-a\). The right-hand side is an integer in \([-2,2]\), so \(a\in\{-1,0,1,2,3\}\). After excluding the two singular parameters, only \(a=0,1,2\) remain; their quartics are respectively \(\Phi_{12},\Phi_8,\Phi_3\Phi_6\). Thus at every other parameter, exactly \(r=\pm i\) can be Weierstrass candidates. This conclusion is subject to local visibility and the stated rank hypotheses.

There is also an explicit symmetry behind the cancellation: \(\tau(x,y)=(1/x,y/x^3)\) interchanges the elliptic maps and satisfies
\(\rho_p\circ\tau=-\rho_p\). This identifies a reason that a single height equation can retain algebraic points. It does not say that a second independent quadratic Chabauty equation would retain them.

## 5. An unconditional rank-two case

Take

\[
 C:y^2=x^6-5x^4-5x^2+1
   =(x^2+1)(x^2-2x-1)(x^2+2x-1).
 \tag{11}
\]

This is the example in [5, Remark 3.4 and Section 3.3]. The following conclusions are exact and hold at all odd primes, without an ordinary-reduction restriction.

**Corollary 5.** The Jacobian of (11) has rank two. For both targets in Theorem 4:

- The Weierstrass mock candidates are exactly \((i,0),(-i,0)\) when \(p\equiv1\pmod4\); there are no Weierstrass candidates when \(p\equiv3\pmod4\).
- The four points \((\pm1,\pm2\sqrt{-2})\) are non-Weierstrass mock candidates exactly at primes \(p\equiv1,3\pmod8\), the primes at which these points lie in \(C(\mathbb Q_p)\).
- The remaining four Weierstrass points, with \(x=\pm1\pm\sqrt2\), are excluded at every odd prime where they are locally visible.

These statements classify the Weierstrass part and certify the four specified non-Weierstrass points; they do not classify every other point in \(A_{p,B}\).

**Proof of the rank claim.** Substituting \(X_{\mathrm{old}}=X-1\) in the common quotient gives

\[
 E:Y^2=X^3-8X^2+8X.
\]

Its two-isogenous curve is

\[
 E':Y^2=X^3+16X^2+32X.
\]

We use the classical two-isogeny descent: for \(Y^2=X^3+AX^2+BX\), the descent map sends an affine point with \(X\ne0\) to the squareclass of \(X\), the origin to 1, and \((0,0)\) to the squareclass of \(B\). Its image is supported on the prime factors of \(B\); for the two dual curves,

\[
 2^{\operatorname{rank}E(\mathbb Q)}
       =\frac{|\operatorname{im}\delta_E|\,|\operatorname{im}\delta_{E'}|}{4}.
 \tag{12}
\]

For completeness, prime support follows by taking valuations in \(Y^2=X(X^2+AX+B)\): at a prime not dividing \(B\), a negative valuation of \(X\) has even parity because the cubic term dominates, and a positive valuation has even parity because \(B\) is a unit. Formula (12) is the standard two-isogeny descent rank identity [6].

For \(E\), negative \(X\) makes \(X(X^2-8X+8)<0\), so its descent image is contained in \(\{1,2\}\). Both occur: the origin gives 1 and \((0,0)\) gives the class of 8, namely 2. For \(E'\), the possible classes are \(\{1,-1,2,-2\}\); they all occur because \((0,0)\) gives 2 and \((-4,8)\) gives \(-1\), and the image is a group. Equation (12) therefore gives rank one. The two degree-two maps give the standard isogeny \(\operatorname{Jac}(C)\sim E\times E\), proving rank two.

The displayed factorization proves that the only roots of unity among the roots of \(f\) are \(\pm i\): the other four roots are real and are neither 1 nor \(-1\). The model discriminants of \(C\) and \(E\) are powers of 2, so every odd prime is eligible. Theorem 4 and the elementary splitting criteria for \(\mathbb Q(i)\) and \(\mathbb Q(\sqrt{-2})\) finish the proof. ∎

## 6. A complete rational-factor test for Weierstrass candidates

The root-of-unity test can be reduced to rational arithmetic, without constructing a number field. This also gives an obstruction outside the monic-unit case.

Put
\[
 H(T)=a_6T^3+a_4T^2+a_2T+a_0,\qquad A=a_6/a_0.
\]
The hypotheses on \(f\) imply that \(H\) is squarefree and has no zero root.

**Lemma 6 (rational powers in degrees at most three).** Let \(h\in\mathbb Q[T]\) be monic and irreducible, of degree at most three, with nonzero constant term, and let \(t\) be a root. There is an integer \(n>0\) with \(t^n\in\mathbb Q^\times\) if and only if \(h\) is one of the following types. In each listed case the pair \((m,R)\) satisfies \(t^m=R\in\mathbb Q^\times\) for every root of \(h\).

- \(h=T+b\): take \((m,R)=(1,-b)\).
- \(h=T^2+bT+c\), \(b=0\): take \((m,R)=(2,-c)\).
- \(h=T^2+bT+c\), \(b^2=c\): take \((m,R)=(3,bc)\).
- \(h=T^2+bT+c\), \(b^2=2c\): take \((m,R)=(4,-c^2)\).
- \(h=T^2+bT+c\), \(b^2=3c\): take \((m,R)=(6,-c^3)\).
- \(h=T^3+d\): take \((m,R)=(3,-d)\).

In particular, no other irreducible quadratic or cubic has a root with a nonzero rational power.

**Proof.** If \(t^n\) is rational and nonzero, all complex conjugates of \(t\) have the same absolute value.

For a quadratic with two real roots, distinctness and equal absolute values force the roots to be negatives of one another, so \(b=0\). Otherwise its roots \(t,\bar t\) lie in an imaginary quadratic field, and \(\zeta=t/\bar t\) is a root of unity in that field. A root of unity in a quadratic field has order \(1,2,3,4,\) or \(6\), since its cyclotomic degree is at most two. Order 1 would give a repeated root. Moreover
\[
 \frac{b^2}{c}=\frac{(t+\bar t)^2}{t\bar t}
             =2+\zeta+\zeta^{-1}.
\]
The remaining orders give respectively \(0,1,2,3\), exactly the quadratic cases listed. Conversely, reduction modulo \(T^2+bT+c\) gives the displayed identities \(t^m=R\) in each case.

For an irreducible cubic \(T^3+bT^2+cT+d\), three distinct real roots cannot all have the same absolute value. Thus there is one real root \(u\) and a conjugate nonreal pair \(z,\bar z\). Equal absolute values give \(z\bar z=u^2\). Vieta's formulas imply
\[
 b=-(u+z+\bar z),\qquad
 c=u(z+\bar z)+u^2=-bu.
\]
If \(b\ne0\), then \(u=-c/b\) is rational, contrary to irreducibility. Hence \(b=c=0\). The converse and the linear case are immediate. ∎

**Theorem 7 (factorwise target-vector classification).** Retain the hypotheses and target \(B\) of Section 1. Factor \(H\) over \(\mathbb Q\), making each irreducible factor monic. Let \(W=(r,0)\in C(\mathbb Q_p)\), \(t=r^2\), and let \(h\) be the factor containing \(t\).

If \(h\) is not on the list in Lemma 6, then \(W\notin A_{p,B}\), for every finite rational-log target \(B\).

If \(h\) is on the list, choose its displayed pair \((m,R)\) and set
\[
 V_h=\frac{A^m}{R}\in\mathbb Q^\times.
\]
For a rational prime \(\ell\), write \(v_\ell\) for the valuation normalized by \(v_\ell(\ell)=1\). Then
\[
 W\in A_{p,B}
 \quad\Longleftrightarrow\quad
 \begin{cases}
 v_\ell(V_h)=0&\text{for every prime }\ell\notin S,\\
 \bigl(v_q(V_h)/(2m)\bigr)_{q\in S}\in B.
 \end{cases}
 \tag{13}
\]
Thus each irreducible factor is either excluded outright or has exactly one possible target coefficient vector. Local visibility of \(r\), rather than merely of \(t\), is still required.

**Proof.** If \(W\) passes, Theorem 2 says that \((A/t)^d\) times a nonzero rational number is a root of unity. Raising to its finite order shows that a positive power of \(t\) is rational. Lemma 6 proves the exclusion assertion.

For a listed factor, \(t^m=R\), and equation (6) gives
\[
 \rho_p(W)=\frac{1}{2m}\log_p V_h
           =\sum_{\ell\ne p}\frac{v_\ell(V_h)}{2m}\log_p\ell.
 \tag{14}
\]
The sum is finite; the sign of \(V_h\) contributes zero. Also \(v_p(V_h)=0\), because \(A\) and \(t\) are \(p\)-adic units.

The logarithms of distinct rational primes other than \(p\) are linearly independent over \(\mathbb Q\). Indeed, clearing denominators in a putative relation gives a positive rational \(p\)-adic unit in the logarithm kernel. Such a number is a rational root of unity, hence 1; unique factorization makes every coefficient zero. Comparing (14) with a target vector proves (13), in both directions. ∎

**Corollary 8 (irreducible-cubic obstruction).** If \(H\) is irreducible over \(\mathbb Q\) and \((a_4,a_2)\ne(0,0)\), there are no Weierstrass points in \(A_{p,B}\), at any eligible prime and for any finite rational-log target as in (2).

In the exceptional binomial case \(H=a_6T^3+a_0\), whether or not it is irreducible, every locally visible Weierstrass point instead has
\[
 \rho_p(W)=\frac23\log_p(a_6/a_0).
 \tag{15}
\]
Consequently the unique possible target vector is
\(\bigl(\tfrac23v_q(a_6/a_0)\bigr)_{q\in S}\), provided the ratio has no prime support outside \(S\). This follows directly from \(t^3=-a_0/a_6\), which gives \(V=-A^4\). These statements assume the rank hypotheses needed for the chosen height setup; they do not assert that any new family has rank two.

For the specialization (11),
\[
 H(T)=(T+1)(T^2-6T+1).
\]
The linear factor has \(V=-1\) and hence target vector zero. The quadratic has \(b^2/c=36\), so it is excluded for every target, recovering the four excluded Weierstrass points without algebraic-unit computations. More generally, (13) is a complete classification of the Weierstrass part of the specified single-height set using factorization and valuations over \(\mathbb Q\). It gives no additional conclusion about non-Weierstrass points or full depth-two Selmer conditions.

## 7. Simultaneous three-torsion and eight further non-Weierstrass candidates

**Lemma 9.** In the setup of Section 1, let \(z=(x,y)\in C(\mathbb Q_p)\) with \(xy\ne0\). If both \(\phi_1(z)\) and \(\phi_2(z)\) have exact order three, then
\[
 \rho_p(z)=\frac23\log_p(a_6/a_0).
 \tag{16}
\]

**Proof.** For an order-three point \(P=(X,Y)\), \(2P=-P\). Evenness of the local height and the duplication identity (5) give
\[
 3\lambda_p(P)=2\log_p(2Y).
\]
The elliptic logarithms of both images of \(z\) vanish. Their \(Y\)-coordinates have ratio \(a_6x^3/a_0\); hence
\[
 \rho_p(z)=\frac23\log_p(a_6x^3/a_0)-2\log_px
           =\frac23\log_p(a_6/a_0).
\]
No finite-precision equality or limiting calculation is used. ∎

**Theorem 10 (complete simultaneous-three-torsion locus in the reciprocal family).** On the smooth family \(C_a\) of (9), over \(\overline{\mathbb Q}\), the finite points with \(xy\ne0\) whose two elliptic images have exact order three exist precisely when \(a=-5\) or \(a=15\). They are:

- At \(a=-5\), the eight points
\[
 3x^4-2x^2+3=0,\qquad y^2=x^6-5x^4-5x^2+1.
 \tag{17}
\]
- At \(a=15\), the four points \(x=\pm1,\ y=\pm4\sqrt2\).

At every eligible prime where these points are locally visible, \(\rho_p=0\). If the common elliptic quotient has rank one, they pass both targets in Theorem 4. For \(a=-5\) this rank hypothesis is already proved in Corollary 5, so (17) gives eight unconditional algebraic non-Weierstrass candidates, distinct from the four with \(x=\pm1\).

**Proof.** The three-division polynomial of \(E_a\) is
\[
 D_a(T)=3T^4+4aT^3+6aT^2+12T+4a-a^2.
\]
With \(u=x^2\ne0\), simultaneous three-torsion is equivalent to
\(D_a(u)=u^4D_a(1/u)=0\). On a smooth elliptic curve in characteristic zero, the roots of this division polynomial are precisely the \(X\)-coordinates of nonzero three-torsion; none is a two-torsion coordinate.

The exact resultant is
\[
 \operatorname{Res}_T(D_a(T),T^4D_a(1/T))
  =(a-15)(a-3)^{10}(a+1)^3(a+5)^2.
 \tag{18}
\]
The singular parameters \(a=3,-1\) are excluded. At the remaining two parameters the greatest common divisors, up to nonzero rational constants, are
\[
 \gcd(D_{-5}(T),T^4D_{-5}(1/T))=3T^2-2T+3,\qquad
 \gcd(D_{15}(T),T^4D_{15}(1/T))=T-1.
\]
Equation (18) and these gcd identities are exact polynomial identities, also checked in the accompanying script. For (17), the quartic has four distinct nonzero roots; its roots are not \(\pm1\). The corresponding \(y\)-coordinates are nonzero, since the elliptic images have order three rather than two. Thus there are eight distinct non-Weierstrass points. None is rational: \(3x^4-2x^2+3\) is positive for real \(x\). Lemma 9 gives \(\rho_p=0\), and both parameters are odd, so Theorem 4 supplies zero in both targets under its rank hypothesis. ∎

**Local visibility of (17).** At \(p=3\), these points are not defined over \(\mathbb Q_3\): the roots \(u\) of \(3u^2-2u+3\) have valuations \(1\) and \(-1\), so neither can equal \(x^2\) with \(x\in\mathbb Q_3\).

For every odd \(p\ne3\), (17) is locally visible exactly when there is an \(s\in\mathbb F_p\) such that
\[
 3s^4-2s^2+3=0,\qquad s^6-5s^4-5s^2+1
       \text{ is a nonzero square in }\mathbb F_p.
 \tag{19}
\]
Indeed the quartic discriminant is \(2^{14}3^2\), and its resultant with \(x^6-5x^4-5x^2+1\) is \(2^{22}\). Thus its roots and the required \(y\)-coordinates are simple modulo every such prime. Hensel's lemma proves sufficiency; unit coordinates and reduction prove necessity. The transformations \(x\mapsto-x\), \((x,y)\mapsto(1/x,y/x^3)\), and \(y\mapsto-y\) act transitively on the eight points. Therefore either all eight are locally visible or none is.

For a concrete exact witness, \(p=67\) and \((s,y)=(6,20)\) satisfy both equations modulo 67 with nonzero derivatives, so all eight points lift to \(\mathbb Q_{67}\). This is an exact Hensel certificate, not a numerical approximation to a height zero. We make no priority claim for these points or the torsion mechanism.

## 8. What the exclusions imply for depth two

For the **standard coarse target** of Bianchi–Padurariu [2, Theorem 2.3], there is a known containment
\[
 C(\mathbb Q_p)_2\ \subseteq\ A_{p,B_{\rm coarse}}.
 \tag{20}
\]
Here \(C(\mathbb Q_p)_2\) denotes the full depth-two Chabauty–Kim set in the standard setup of that method. The relationship of the successive explicit supersets to this set is explained in [5, Remark 2.4], citing Balakrishnan–Dogra. We use (20) only for that standard target, under its hypotheses, not for an arbitrary finite target \(B\) or an unproved refinement.

**Corollary 11 (genuine depth-two exclusions).** Under the hypotheses of (20):

1. Any Weierstrass point excluded by Theorem 7 with \(B=B_{\rm coarse}\) is absent from \(C(\mathbb Q_p)_2\).
2. If \(H\) is irreducible over \(\mathbb Q\) and \((a_4,a_2)\ne(0,0)\), the full depth-two set has no Weierstrass points at any eligible prime.
3. For the rank-two curve (11), the four Weierstrass points \(x=\pm1\pm\sqrt2\) are not in the full depth-two set at any eligible prime where they are locally visible.

**Proof.** Each statement is the contrapositive of containment (20), applied to Theorem 7, Corollary 8, or Corollary 5 respectively. ∎

This implication is strictly one-way. The six earlier candidates have not been proved here to lie in the full depth-two set. For the eight points (17), Section 11 below resolves another correspondence condition and proves exclusion.

## 9. The coordinate field and density of the eight-point locus

**Theorem 12.** The eight points (17) form a single Galois orbit. The field generated by the two coordinates of any one of them is the same Galois extension \(L/\mathbb Q\), of degree eight and dihedral Galois group \(D_4\) (of order eight). It is unramified outside 2 and 3. For every odd prime \(p\ne3\), the eight points are locally visible exactly when \(p\) splits completely in \(L\). The set of such primes has natural density \(1/8\).

**Proof.** Put
\[
 d=\sqrt{-2},\quad F=\mathbb Q(d),\quad
 u=\frac{1+2d}{3},\quad x^2=u,\quad
 v=\frac{64-160d}{27},\quad y^2=v.
\]
Reduction modulo \(3u^2-2u+3\) gives \(f(x)=v\). Since
\[
 d=\frac{3x^2-1}{2},\qquad
 (x+x^{-1})^2=\frac83,
\]
the field \(\mathbb Q(x)\) contains both \(d\) and \(\sqrt6\). Conversely, one can choose
\(x=(\sqrt6+\sqrt{-3})/3\), with \(\sqrt{-3}=d\sqrt6/2\). Thus
\[
 K=\mathbb Q(x)=\mathbb Q(d,\sqrt6)
\]
is biquadratic. Write \(c=32/9\). Direct calculation gives
\[
 v\bar v=\frac{2048}{27}=6c^2.
 \tag{21}
\]
For an element of \(F\) to be a square in \(F(\sqrt6)\), it must be a square in \(F\) or six times a square in \(F\): expand \((a+b\sqrt6)^2\) and use \(2ab=0\). Both possibilities for \(v\) are ruled out by (21), since its norm to \(\mathbb Q\) is not a rational square, whereas the norm of a square or of six times a square is a rational square. Therefore \(L=K(y)\) has degree eight.

Every \(\mathbb Q\)-embedding of \(K\) takes \(v\) to \(v\) or \(\bar v\), and both square roots of the latter lie in \(L\), since
\[
 \sqrt{\bar v}=\frac{c\sqrt6}{y}.
\]
Consequently \(L/\mathbb Q\) is normal, hence Galois. The automorphisms
\[
 \sigma:(d,\sqrt6,y)\longmapsto(d,-\sqrt6,y),\qquad
 \tau:(d,\sqrt6,y)\longmapsto(-d,\sqrt6,c\sqrt6/y)
\]
are involutions. Their product has order four: its square fixes \(K\) and sends \(y\) to \(-y\). Their images generate \(\operatorname{Gal}(K/\mathbb Q)\), so they generate the full group of order eight, which is \(D_4\). Since \((x,y)\) generates \(L\), its orbit has eight elements, precisely (17); normality shows every point in the orbit has the same coordinate field.

The quadratic fields generating \(K\) are unramified away from 2 and 3. At every prime of \(F\) over a rational prime other than 2 or 3, \(v\) is integral and a unit: its denominator is supported at 3 and its norm is supported at 2 and 3. Adjoining its square root is unramified at odd residue characteristic, since the polynomial \(Z^2-v\) then has unit discriminant \(4v\). This proves the ramification assertion. In particular, a prime dividing a polynomial discriminant for a chosen coordinate generator need not ramify in the field.

For \(p\ne2,3\), a point in (17) lies in \(C(\mathbb Q_p)\) precisely when its coordinate field \(L\) embeds in \(\mathbb Q_p\). As \(L/\mathbb Q\) is Galois and unramified at \(p\), this is equivalent to complete splitting. The Chebotarev density theorem, applied to the identity conjugacy class, gives density \(1/[L:\mathbb Q]=1/8\). ∎

This is an arithmetic classification of the prime visibility of the eight single-height candidates. It is not a density statement about their membership in the full depth-two set.

## 10. An explicit second necessary height test

The remaining correspondence issue can be made concrete for (11), rather than left as an unspecified search.

**Proposition 13.** The rational change of variables
\[
 u=\frac{x+1}{x-1},\qquad v=\frac{4y}{(x-1)^3}
\]
extends to an isomorphism from the smooth projective curve (11) to
\[
 C^\ast:v^2=-2u^6+10u^4+10u^2-2.
 \tag{22}
\]
Both bielliptic quotients of (22) are
\[
 \widetilde E:Y^2=X^3+10X^2-20X-8.
\]
They have rational rank one. Hence the standard coarse Bianchi–Padurariu construction on (22) supplies another necessary height condition for the full depth-two set on (11).

Under this change of variables, the eight points (17) have
\[
 u^4+10u^2+1=0.
 \tag{23}
\]
Neither elliptic image in this new model has order three. Thus the order-three argument of Lemma 9 does not evaluate this second height condition.

**Proof.** Substitution gives
\[
 (u-1)^6 f\!\left(\frac{u+1}{u-1}\right)
       =-8(u^6-5u^4-5u^2+1),
\]
and \(v=y(u-1)^3/2\), proving the model identity. The rational inverse away from the exceptional coordinate charts, and smooth projective completion, give the isomorphism. The quotient formulas in Section 1 give \(\widetilde E\). Substituting \(X=Z+2\) gives
\[
 Y^2=Z^3+16Z^2+32Z,
\]
which is exactly the curve \(E'\) in Corollary 5, two-isogenous to the rank-one curve \(E\). Thus the required ranks are proved. Every odd prime is good for these displayed models.

The standard containment (20), transported through the isomorphism, means that full depth-two points must satisfy both the original coarse height condition and the coarse condition from (22). This assertion requires neither a claim that the two conditions are independent nor a claim that their intersection is the full depth-two set.

Finally,
\[
 (u-1)^4\left(3\left(\frac{u+1}{u-1}\right)^4
 -2\left(\frac{u+1}{u-1}\right)^2+3\right)
 =4(u^4+10u^2+1).
\]
The three-division polynomial of \(\widetilde E\), evaluated at \(X=-2T\), is \(16D_{-5}(T)\). Exact polynomial division gives
\[
 \gcd(T^2+10T+1,D_{-5}(T))=1.
\]
Apply this with \(T=u^2\), and with \(T=u^{-2}\), noting that (23) is reciprocal. Both images therefore fail to be three-torsion. This does not assert that they are nontorsion, nor does it decide the second height value. ∎

The next theorem evaluates this second height exactly: the images have order six, and the additional test excludes the eight-point locus.


## 11. The eight three-torsion candidates fail the second test

**Theorem 14 (all-prime depth-two exclusion of the eight-point locus).** Let \(z\) be any of the eight points (17), locally visible at an odd prime \(p\), and let \(z^\ast=(u,v)\) be its image on (22). Put \(t=u^2\), so \(t^2+10t+1=0\). Both elliptic images of \(z^\ast\) on \(\widetilde E\) have exact order six, and the height function for model (22) satisfies
\[
 \rho^\ast_p(z^\ast)=-\frac13\log_p t.
 \tag{24}
\]
This value belongs to no finite rational-log target of the form (2), with \(p\notin S\). In particular, the eight points (17) are absent from the full depth-two Chabauty–Kim set at every odd prime where they are locally visible.

Thus these eight points pass the first standard coarse height test but fail the second. They provide an exact example of why membership in a single-correspondence height set must not be identified with full depth-two membership.

**Proof.** Write
\[
 G(X)=X^3+10X^2-20X-8,\quad
 h(X)=X^2-20X+4,\quad
 D(X)=3X^4+40X^3-120X^2-96X-720.
\]
Here \(D\) is the three-division polynomial of \(\widetilde E\). For a point \(Q=(X,Y)\) with \(h(X)=0\), ordinary elliptic doubling and reduction modulo \(h\) give
\[
 X(2Q)=X-16,\qquad
 \frac{Y(2Q)}{Y(Q)}=k(X):=10-\frac X2.
 \tag{25}
\]
These expressions have no zero denominators: \(\gcd(G,h)=1\). Moreover
\[
 D(X-16)\equiv0\pmod h,\qquad \gcd(D,h)=1.
\]
Therefore \(2Q\) has exact order three, while \(Q\) does not have order three; it follows that \(Q\) has exact order six.

For \(z^\ast=(u,v)\), the two elliptic images are
\[
 Q_1=(-2t,-2v),\qquad
 Q_2=(-2/t,-2v/u^3).
\]
Both \(X\)-coordinates satisfy \(h=0\), so both images have order six and both elliptic logarithms vanish. Applying duplication and then the order-three formula to \(2Q\) yields
\[
 \lambda_p(Q)=\frac14\bigl(\lambda_p(2Q)+2\log_p(2Y(Q))\bigr)
 =\frac16\log_p(2Y(2Q))+\frac12\log_p(2Y(Q)).
 \tag{26}
\]
This holds for each quotient with its chosen splitting; torsion removes the splitting-dependent logarithm terms.

Since \(Y(Q_1)/Y(Q_2)=u^3\), equations (25)–(26) cancel the \(-2\log_pu\) in the bielliptic height function and give
\[
 \rho^\ast_p(z^\ast)
 =\frac16\log_p\frac{k(-2t)}{k(-2/t)}.
\]
The relation \(t^2+10t+1=0\) implies
\[
 k(-2t)=10+t=-t^{-1},\qquad
 k(-2/t)=10+t^{-1}=-t.
\]
This proves (24).

Finally \(t\) is an algebraic unit, and its two real conjugates are \(-5\pm2\sqrt6\); neither is \(1\) or \(-1\), so \(t\) is not a root of unity. Suppose (24) equals \(\sum_{q\in S}c_q\log_pq\) for rational \(c_q\). Choose a positive integer \(N\) with \(3Nc_q\in\mathbb Z\) for every \(q\). Then
\[
 U=t^N\prod_{q\in S}q^{3Nc_q}
\]
is a \(p\)-adic unit with \(\log_pU=0\), and hence a root of unity. Taking number-field valuations above each \(q\) forces \(c_q=0\), because \(t\) is a global unit. It follows that \(t^N\) is a root of unity, a contradiction. This rules out every such target, including the standard coarse target for (22).

Proposition 13 and containment (20) now exclude the original points from the full depth-two set. Local visibility at \(p=3\) was already ruled out in Section 7; at every other eligible prime the argument applies as stated. ∎

This theorem alone does not settle the full-depth-two membership of the six earlier points \((\pm i,0)\) and \((\pm1,\pm2\sqrt{-2})\), or classify all other points of the depth-two set. It does resolve the extra second-correspondence condition for the entire eight-point locus (17).

## 12. Exact second-height values for the remaining six points

The four points with \(x=\pm1\) require a different argument from the torsion calculation in Section 11. Their second-height values can nevertheless be evaluated exactly in terms of one rational elliptic height.

**Theorem 15.** Let \(p\) be odd and split in \(\mathbb Q(\sqrt{-2})\), put \(s=\sqrt{-2}\in\mathbb Q_p\), and let
\[
 E:Y^2=X^3-8X^2+8X,\qquad P=(1,1).
\]
Use the unit-root (equivalently complementary CM-eigenspace) splitting for its cyclotomic \(p\)-adic height \(h_p\). For the second-model height of (22),
\[
 \rho^\ast_p((-1,\pm2s)^\ast)=2h_p(P),\qquad
 \rho^\ast_p((1,\pm2s)^\ast)=-2h_p(P).
 \tag{27}
\]
Here the superscript \({}^\ast\) means transport through the isomorphism in Proposition 13. At every odd prime where they are visible, the two Weierstrass points instead satisfy
\[
 \rho^\ast_p((\pm i,0)^\ast)=0.
 \tag{28}
\]

**Proof.** Write \(E':Y^2=Z^3+16Z^2+32Z\), identified with \(\widetilde E\) by \(X_{\widetilde E}=Z+2\). Consider the degree-two isogeny and the quadratic-twist isomorphism
\[
 \phi(X,Y)=\left(X-8+\frac8X,\ Y\left(1-\frac8{X^2}\right)\right),
 \qquad
 \psi(X,Y)=(-2X,-2sY).
 \tag{29}
\]
For the invariant differentials \(\omega=dX/(2Y)\) and \(\omega'=dZ/(2Y)\), direct differentiation gives
\(\phi^\ast\omega'=\omega\) and \(\psi^\ast\omega'=\omega/s\).
The endomorphism \(\eta=\psi^{-1}\phi\) therefore has differential multiplier \(s\), and \(\eta^2=[-2]\), since in characteristic zero the differential determines an endomorphism. This realizes CM by \(\mathbb Z[\sqrt{-2}]\). At the split good primes under consideration the curve is ordinary; the eigenspace complementary to the Hodge line is its unit-root complement.

Transport this complement via \(\psi\) to \(E'\). Since the complement is \(\eta\)-stable, both \(\phi\) and \(\psi\) preserve the chosen splittings. Functoriality of compatible global heights for the degree-two polarized isogeny, and functoriality of elliptic logarithms, give, for
\[
 R=\phi(P)=(1,-7),\qquad Q=\psi(P)=(-2,-2s),
\]
the identities
\[
 h'_p(R)=2h_p(P),\qquad L'(R)=L(P),\qquad
 L'(Q)=L(P)/s.
 \tag{30}
\]
The height multiplier is the degree of \(\phi\): pullback of the canonical polarization is twice the canonical polarization. The use of compatible splittings is essential here.

The point \(P\) is nontorsion. For example, direct counting gives
\(\#E(\mathbb F_3)=6\) and \(\#E(\mathbb F_7)=8\); injectivity of prime-to-residue-characteristic rational torsion under good reduction forces the rational torsion order to divide 2. The point \(P\), with nonzero \(Y\), is not two-torsion.

In the original quotient coordinates, \(P\) is \((0,1)\). It is integral and nonsingular at every finite prime: use the \(Y\)-derivative at odd primes and the \(X\)-derivative at 2. Its non-\(p\) local heights are zero, so \(\lambda_p(P)=h_p(P)\). Under the compatible twist isomorphism the formal parameter changes by \(t'=t/s\), whence the normalized local-height transformation is
\[
 \lambda'_p(Q)=\lambda_p(P)+\log_p2.
 \tag{31}
\]
Thus, with \(\alpha'=h'_p(R)/L'(R)^2\), equations (30) give
\(\alpha'L'(Q)^2=-h_p(P)\).

On (22), the continuous extension at \(u=0\), where \(v^2=-2\), is, writing the finite quotient image in \(E'\)-coordinates,
\[
 \rho^\ast_p(0,v)
   =\lambda'_p((-2,-2v))-\log_p(-2)
       -\alpha'L'((-2,-2v))^2.
\]
Indeed the formal parameter of the second quotient is \(-u/v\), so its logarithmic singularity cancels \(-2\log_pu\), leaving \(-\log_p(v^2)\). Equations (30)–(31) now give \(2h_p(P)\). Reciprocal antisymmetry gives \(-2h_p(P)\) at either infinity. Old \(x=-1\) maps to \(u=0\), and old \(x=1\) to infinity, proving (27). The signs of \(y\) do not affect the heights or squared logarithms.

Finally old \(x=\pm i\) maps to \(u=\mp i\). Theorem 2, with \(a_6=a_0=-2\), gives (28). ∎

**Proposition 16 (the exact second local target).** For model (22), the actual local-image functions (3) satisfy
\[
 w^\ast_q\equiv0\quad\text{on }C^\ast(\mathbb Q_q)
 \quad\text{for every }q\ne p.
\]
Consequently the actual local-image target is exactly \(\{0\}\), for every odd good \(p\).

**Proof.** At 2, put \(k=v_2(u)\). If \(k>0\), the valuation of \(-2F(u)\) is 1; if \(k<0\), it is \(1+6k\), where \(F(u)=u^6-5u^4-5u^2+1\). Both are odd and impossible for \(v^2\). Hence \(u\) is a unit. Its square is 1 or 9 modulo 16, giving \(F(u)\equiv8\pmod{16}\), and therefore \(v_2(v)=2\).

Use the integral minimal quotient model
\[
 E'':w^2=z^3+4z^2+2z,\qquad
 X_{\widetilde E}=4z+2,\quad Y_{\widetilde E}=8w.
\]
The two images have respectively
\[
 (z,w)=\left(-\frac{u^2+1}{2},-\frac v4\right),\qquad
 \left(-\frac{u^{-2}+1}{2},-\frac{v}{4u^3}\right).
\]
All coordinates are 2-adic units. The derivative \(3z^2+8z+2\) is odd, so both reduce nonsingularly and have minimal local height zero. Each displayed-model height has the same change-of-model correction \(-2\log_p2\), and these corrections cancel. Also \(|u|_2=1\), proving \(w^\ast_2=0\). There are no \(u=0\) or infinite points over \(\mathbb Q_2\), since their leading or constant coefficient is \(-2\).

At an odd \(q\ne p\), the quotient model has good reduction. If \(k=v_q(u)>0\), the first quotient image has integral coordinates and height zero, while the second has height \(2k\log_pq\), which cancels \(2\log_p|u|_q=-2k\log_pq\). The case \(k<0\) is symmetric; if \(k=0\), all terms vanish. Continuity gives the same result at any \(u=0,\infty\) points. ∎

**Corollary 17 (exclusion from the refined second-height set).** For every \(p\ge5\) split in \(\mathbb Q(\sqrt{-2})\), the four points \((\pm1,\pm2\sqrt{-2})\) fail the second actual local-image height condition. The two locally visible Weierstrass points \((\pm i,0)\) pass both actual local-image height conditions.

**Proof.** Bertrand's nonvanishing theorem for CM elliptic heights, in the form of [7, Appendix A, Theorem A.1 and Lemma A.2], implies \(h_p(P)\ne0\). More explicitly, the one-prime height there is nonzero for a nontorsion point; the anticyclotomic height of rational \(P\) is zero by complex conjugation, so its cyclotomic height cannot be zero. The cyclotomic height agrees with the unit-root height used here up to a nonzero normalization.

We retain the source's assumption \(p>3\). Its CM and functional-equation hypotheses hold: translating \(X=z+3\) identifies \(E\) with LMFDB 256.a1, \(Y^2=z^3+z^2-13z-21\). The local root number at its sole bad prime 2 is \(+1\) [8]; with the archimedean factor \(-1\), its global root number is \(-1\). The CM field \(\mathbb Q(\sqrt{-2})\) has class number one. No numerical approximation to a regulator or analytic rank is being used to infer nonvanishing.

Equations (27) and Proposition 16 exclude the four points from the refined second-height set. Equation (28), Theorem 4, and Proposition 16 prove the assertion about the two Weierstrass points. ∎

The next section proves the nonmonic actual-target containment needed to upgrade Corollary 17. At \(p=3\), equation (27) and Proposition 16 remain valid, but the cited nonvanishing result has not been applied here. Passing both tests at the two Weierstrass points still does not prove full-depth-two membership.

## 13. Actual-target containment without a monic hypothesis

**Selmer convention.** We use the depth-two Selmer set with the Mordell–Weil abelian-image condition of [9, Definition 2.2(3)], as in the correspondence construction below. If instead one drops that condition and allows the entire global Bloch–Kato group in degree one, the same conclusion requires identifying that group with the Mordell–Weil image; rank alone does not establish this identification.

**Theorem 18.** In the setup of Section 1, suppose that \(C\) has a rational basepoint \(b\) away from \(x=0,\infty\), with \(y(b)\ne0\). Let \(p\) be an odd good prime for the curve and its displayed elliptic quotients, with \(p\nmid a_0a_6\). Use compatible symmetric height splittings and invariant-differential tangent normalizations. Then
\[
 C(\mathbb Q_p)_2\subseteq
 \left\{z:\rho_p(z)\in\sum_{q\ne p}w_q(C(\mathbb Q_q))\right\}.
 \tag{32}
\]
The sum uses actual local images, including the continuous endpoint values. No monic-model or rational-infinity hypothesis is needed.

**Proof.** Let \(\iota\) be the hyperelliptic involution, let
\(g_1(x,y)=(-x,y)\), \(g_2(x,y)=(-x,-y)\), and write \(D_0,D_\infty\) for the degree-two divisors above zero and infinity. These divisors are rational even when their individual points are not, and
\(\operatorname{div}(x)=D_0-D_\infty\).
Use the rational correspondence \(Z=\Gamma_{g_2}-\Gamma_{g_1}\).
Its intersection with the diagonal minus the two basepoint fibers is zero: the fixed divisors have degree two and each graph meets each fiber in degree one. Its projected wedge-square class is nonzero. Indeed the involutions are Rosati self-adjoint, and their difference acts by opposite nonzero eigenvalues on the two elliptic summands of \(H^1(C)\). Thus it gives a nonzero trace-zero alternating class, not merely a nonzero tensor class.

The divisor associated to this graph difference is
\[
 D_Z(b,z)=D_\infty-D_0+g_1z-g_2z+g_1b-g_2b.
\]
Put \(P_i=\phi_i(z)\), \(B_i=\phi_i(b)\), and
\(T_i=(-P_i)+(-B_i)-2O_i\). Direct pullback gives the exact identity
\[
 D_Z(b,z)=-\phi_1^*T_1+\phi_2^*T_2+\operatorname{div}(x).
 \tag{33}
\]
For example \(\phi_1^*(-P_1)=\iota z+g_2z\),
\(\phi_2^*(-P_2)=\iota z+g_1z\), and the pullbacks of the origins are \(D_\infty,D_0\). The principal term in (33) must not be omitted.

For the symmetric elliptic divisor pairing, initially at generic points with the necessary disjoint supports,
\[
 h_v(P-B,(-P)+(-B)-2O)
 =-\lambda_v(P)+\lambda_v(B)+\chi_v(Y(P)/Y(B)).
 \tag{34}
\]
Here \(\chi_p=\log_p\), and \(\chi_q=\log_p|\cdot|_q\) otherwise. To check the normalization, expand the pairing: the cross terms cancel by symmetry and inversion. The principal divisor of \(X-X(P)\), with invariant-differential tangents at all support points, gives
\(h_v(P-O,(-P)-O)+h_v(P-O,P-O)=\chi_v(2Y(P))\).
The self-height is \(\lambda_v(P)\); subtract the corresponding identity for \(B\). This proves (34), including its sign.

Apply the projection formula to (33). Since \(Y(P_1)/Y(P_2)=(a_6/a_0)x(z)^3\), the constants cancel against their values at \(b\), and the principal term contributes one copy of \(\chi_v(x(z)/x(b))\). Consequently
\[
 h_v(z-b,D_Z(b,z))=r_v(z)-r_v(b),\qquad
 r_v=\lambda_{1,v}\circ\phi_1-\lambda_{2,v}\circ\phi_2-2\chi_v(x).
 \tag{35}
\]
Globally the principal height is zero. Bilinearity on divisor classes, using \([T_i]=-[P_i]-[B_i]\), gives
\[
 h(z-b,D_Z(b,z))
 =h_1(P_1)-h_1(B_1)-h_2(P_2)+h_2(B_2).
 \tag{36}
\]
This determines the quadratic correction as an identity of forms, not by interpolation on rational curve points. Because each elliptic quotient has rank one, their nonzero elliptic logarithms give the required isomorphism
\(J(\mathbb Q)\otimes\mathbb Q_p\longrightarrow H_f^1(\mathbb Q_p,V_p(J))\).
The expression in (36), on these localizations, is \(F(z)-F(b)\), where
\(F=\alpha_1L_1^2\circ\phi_1-\alpha_2L_2^2\circ\phi_2\).

Now use the full-curve mixed extension \(A_Z(b,z)\) of [9, Proposition 5.5], whose local heights agree with the divisor pairing on its open domain by [9, Theorem 6.3]. These general constructions have no leading-coefficient restriction. They give the necessary condition
\[
 H_p(z)-F(z)+F(b)\in
 \left\{-\sum_{q\ne p}H_q(z_q):z_q\in C(\mathbb Q_q)\right\}.
 \tag{37}
\]
We justify (35) also at the omitted points. Write
\(\lambda_i=-2\log_p(t_i)+A_i(t_i)\), with \(A_i\) analytic at zero.
Near \(x=0\), \(t_2=-x/y\), and
\(r_p=\lambda_1(\phi_1z)-2\log_p y-A_2(-x/y)\).
Near infinity put \(s=1/x,\ v=y s^3\); then
\(r_p=2\log_p v+A_1(-s/v)-\lambda_2(\phi_2z)\).
Both extend analytically, retaining the endpoint constants involving \(a_0,a_6\).
The full-curve mixed-extension height is locally analytic at \(p\), so equality extends by density of the open domain in each local disk. Away from \(p\), the local Kummer map is locally constant [10, Theorem 0.1], and the same cancellation gives continuous extensions of \(r_q\). Thus density again extends (35). Finite image alone is not being used as a continuity argument.

Finally \(r_q=-w_q\) and \(r_p-F=\rho_p\). Equation (37) becomes
\[
 \rho_p(z)-\rho_p(b)\in
 \left\{\sum_{q\ne p}w_q(z_q)-\sum_{q\ne p}w_q(b)\right\}.
\]
The rational basepoint satisfies \(\rho_p(b)=\sum_{q\ne p}w_q(b)\) by the global-height decomposition and product formula. Cancelling proves (32). ∎

**Corollary 19 (four further depth-two exclusions).** For every \(p\ge5\) split in \(\mathbb Q(\sqrt{-2})\), the four points \((\pm1,\pm2\sqrt{-2})\) on (11) are absent from \(C(\mathbb Q_p)_2\).

**Proof.** Apply Theorem 18 to (22) with rational basepoint \(b=(-1,-4)\). All its good-prime and rank hypotheses were verified above. Proposition 16 gives actual target \(\{0\}\), while Theorem 15 and the nonvanishing argument of Corollary 17 give nonzero values \(\pm2h_p(P)\). Transport through the rational curve isomorphism. ∎

The restriction \(p\ge5\) is retained: no new nonvanishing assertion at \(p=3\) is made.

## 14. The remaining central directions

Let \(V=V_p(E)\) for the rational elliptic curve in Section 12, with \(\det V=\mathbb Q_p(1)\). The quotient isogeny gives \(V_p(J)=V\otimes M\), with \(M=\mathbb Q_p^2\) a trivial Galois module. The Cauchy decomposition and the surface relation give
\[
 \operatorname{gr}_2(U)=\bigwedge^2(V\otimes M)/\mathbb Q_p(1)
 \simeq \operatorname{Sym}^2 V\oplus\mathbb Q_p(1)^2.
 \tag{38}
\]
Indeed the wedge square decomposes into
\(\operatorname{Sym}^2V\otimes\bigwedge^2M\) and
\(\det V\otimes\operatorname{Sym}^2M\).
The polarization relation lies in the latter summand: \(\operatorname{End}_{\mathbb Q}(E)\otimes\mathbb Q=\mathbb Q\), so the former has no rational Tate line. Removing one line from its three-dimensional Tate multiplicity space proves (38).

Over a coefficient extension containing \(K=\mathbb Q(\sqrt{-2})\), write
\(V|_{G_K}=\psi\oplus\psi^c\). Then the remaining representation is
\[
 \operatorname{Sym}^2V
 \simeq\operatorname{Ind}_{G_K}^{G_{\mathbb Q}}(\psi^2)
       \oplus\mathbb Q_p(1)\chi_K.
 \tag{39}
\]
For the sign in the last character, an element outside \(G_K\) exchanges the two eigenvectors; on their symmetric product its action is minus its determinant.

The last one-dimensional direction has no global finite-Selmer translation freedom:
\[
 H_f^1(\mathbb Q,\mathbb Q_p(1)\chi_K)=0.
 \tag{40}
\]
By restriction and Kummer theory it is the anti-invariant part of
\(\mathcal O_K^\times\otimes\mathbb Q_p\), which is zero because \(K\) is imaginary quadratic. Allowing ramification at 2 adds only an invariant valuation direction, since 2 has a unique prime in \(K\). The crystalline condition removes valuation directions at \(p\). Locally the finite Selmer space in this direction has dimension one: its de Rham tangent quotient has dimension one and its invariant subspace is zero.

These calculations identify a genuine remaining local comparison, not a membership test already evaluated. Fibers over a fixed nonzero abelian class are torsors. Vanishing (40) does not canonically make the relevant local coordinate zero; a global lift and its localization must still be constructed and compared. In particular, passing the two scalar heights alone does not settle the full depth-two membership of \((\pm i,0)\). The next section supplies the missing global lift and local comparison in the anti-CM direction. Their visible primes \(p\equiv1\pmod4\) include both CM-split primes \(p\equiv1\pmod8\) and CM-inert primes \(p\equiv5\pmod8\).

## 15. An explicit norm-one-torus obstruction excludes the pair

**Theorem 20 (exclusion of the final Weierstrass pair).**

Let

\[
 C:y^2=x^6-5x^4-5x^2+1,
 \qquad b=(0,1),
 \qquad E:Y^2=X^3-8X^2+8X.
\]

For every odd prime \(p\equiv1\pmod4\), neither \((i,0)\) nor \((-i,0)\) belongs to the full depth-two Chabauty–Kim set defined using global classes with abelian projection in \(J(C)(\mathbf Q)\otimes\mathbf Q_p\). An explicit quotient detecting them has center
\(\mathbf Q_p(1)\otimes\chi_{\mathbf Q(\sqrt{-2})}\).

The local obstruction is the Kummer class of a non-torsion norm-one unit. Under a choice \(s=\sqrt{-2}\) and \(i^2=-1\), its scalar representative, up to inversion and multiplication by \(-1\), is
\[
 g(i)=\frac{i+s}{i-s}=-(1+\sqrt2)^2,
 \qquad \sqrt2=s/i.
\]
The proof applies equally when \(p\equiv1\pmod8\) (split CM) and \(p\equiv5\pmod8\) (inert CM). No ordinary splitting or nonvanishing theorem for an elliptic height is needed.

### 1. The exact CM maps and the principal divisor

Put \(K=\mathbf Q(s)\), \(s^2=-2\), and denote its nontrivial automorphism by \(c\). Let \(T=(0,0)\in E[2](\mathbf Q)\) and \(P=(1,1)\in E(\mathbf Q)\). The two quotient maps, in the shifted elliptic coordinates, are
\[
 f_1(x,y)=(x^2+1,y),\qquad
 f_2(x,y)=(1+x^{-2},y/x^3).
\]
They extend to the smooth projective curve, and
\[
 (f_1(b),f_2(b))=(P,O),\qquad
 (f_1(W),f_2(W))=(T,T)
\]
for either \(W=(\pm i,0)\).

The CM endomorphism
\[
 \eta(X,Y)=\left(-\frac{X-8+8/X}{2},
                 -\frac{Y(1-8/X^2)}{2s}\right)
\]
extends across the displayed poles. It satisfies
\(\eta^2=[-2]\), \(c(\eta)=-\eta\), \(\eta(T)=O\), and \(\eta^\dagger=-\eta\) for the Rosati involution. These facts also follow by composing the degree-two isogeny
\((X,Y)\mapsto(X-8+8/X,Y(1-8/X^2))\)
with the inverse of \((X,Y)\mapsto(-2X,-2sY)\). Its invariant-differential multiplier is \(s\).

Define \(f_\pm=f_1\pm\eta f_2:C_K\to E_K\), and put
\[
 A=x^3+\frac{3s}{2}x^2-x-\frac{s}{2},\qquad
 B=x^3-\frac{3s}{2}x^2-x+\frac{s}{2},\qquad g=A/B.
\]
Then
\[
 \operatorname{div}(g)=f_+^*(O)-f_-^*(O). \tag{41}
\]
Here the origin divisors have degree six. To verify (41), the addition-law denominators give
\[
 X(f_1)-X(\eta f_2)
 =\frac{2x^6+5x^4-4x^2+1}{2x^2(x^2+1)}
 =\frac{AB}{x^2(x^2+1)},
\]
while
\[
 \frac{Y(\eta f_2)}{Y(f_1)}
 =\frac{7x^4-2x^2-1}{2s x^3(x^2+1)^2}.
\]
This ratio is \(-1\) modulo \(A\), and \(+1\) modulo \(B\). Consequently the six points above roots of \(A\) are precisely the origin fiber of \(f_+\), and those above roots of \(B\) are the origin fiber of \(f_-\), with multiplicity one in characteristic zero. The exact checks
\[
 \operatorname{disc}(A)=13,\quad
 \operatorname{Res}(A,B)=-8s,\quad
 \operatorname{Res}(A,x^6-5x^4-5x^2+1)=-256,\quad
 \operatorname{Res}(A,x)=s/2,\quad
 \operatorname{Res}(A,x^2+1)=-4
\]
verify the needed disjointness (the same checks apply to \(B\)). At \(x=0\), \(f_\pm\) limit to \((1,\pm1)\); at infinity they limit to \(\pm\eta(1,\pm1)\), whose \(X\)-coordinate is \(-1/2\); at \(x=\pm i\), both limit to \(T\). Thus no exceptional chart adds an origin point. These computations establish the divisor, not merely a relation between its degrees.

Finally,
\[
 g(0)=-1,\qquad c(g)=g^{-1},\qquad
 g(i)=\frac{i+s}{i-s},\qquad g(-i)=g(i)^{-1}. \tag{42}
\]

### 2. A norm-one-torus torsor over the abelian surface

Write \(D=E\times E\), and on \(D_K\) let
\[
 m_\pm(R,S)=R\pm\eta S,
 \qquad
 \mathcal L=m_+^*\mathcal O_E(O)\otimes m_-^*\mathcal O_E(O)^{-1}.
\]
There is a canonical rational section \(\sigma\) of \(\mathcal L\), obtained as the ratio of the pullbacks of the canonical section of \(\mathcal O_E(O)\). Its divisor is \(m_+^*(O)-m_-^*(O)\).

Conjugation exchanges \(m_+\) and \(m_-\), hence canonically identifies \(c^*\mathcal L\) with \(\mathcal L^{-1}\). On nonzero vectors, combine this identification with dual inversion \(v\mapsto v^{-1}\). The resulting semilinear involution squares to the identity. Effective descent gives a variety \(\mathcal X/\mathbf Q\) over \(D\), which is a torsor under
\[
 \mathcal T=\operatorname{Res}^{1}_{K/\mathbf Q}\mathbf G_m.
\]
After base change to \(K\), it is \(\mathcal L^\times\); its torus has Tate module
\(V_p\mathcal T=\mathbf Q_p(1)\chi_K=:W\).

Let \(j=(f_1,f_2):C\to D\). By (41), \(j^*\sigma/g\) is an everywhere nonzero section of \(j^*\mathcal L\). Since conjugation inverts both \(\sigma\) and \(g\), this section descends to a morphism
\[
 \widetilde j:C\longrightarrow\mathcal X
\]
over \(j\). This is an actual morphism on the proper curve, including zeros and poles of \(A/B\), because the divisors in (41) cancel exactly.

Whenever \(m_+(a)=m_-(a)\ne O\), the fiber of \(\mathcal L\) at \(a\) has its canonical ratio trivialization, and \(\sigma(a)=1\). In particular, these trivializations apply at \((P,O)\), \((T,O)\), and \((T,T)\). Thus
\[
 \widetilde j(b)=(P,O,-1),\qquad
 \widetilde j(W)=(T,T,g(W)^{-1}). \tag{43}
\]
The notation for the third coordinate is confined to these canonically trivialized fibers.

### 3. Why this is a depth-two quotient

Let \(U_{\mathcal X}\) be the \(\mathbf Q_p\)-unipotent geometric étale fundamental group of \(\mathcal X\), based at \(\widetilde j(b)\). Then
\[
 1\longrightarrow W\longrightarrow U_{\mathcal X}
 \longrightarrow V_pD\longrightarrow1 \tag{44}
\]
is a central extension, so \(U_{\mathcal X}\) is two-step unipotent.

One direct explanation is to base change to \(\mathbf C\). An abelian variety is a topological \(K(\mathbf Z^{2\dim D},1)\). The nonzero vectors of a line bundle form a \(\mathbf C^\times\)-bundle. Its homotopy exact sequence gives a central extension of \(\mathbf Z^{2\dim D}\) by \(\mathbf Z\), whose commutator is the Chern class of the line bundle. Rational Malcev completion gives (44) over an algebraic closure; étale comparison and the descent just described identify the Galois module of the center as \(W\).

The Chern class is nonzero: relative to the product principal polarization, its associated symmetric homomorphism is
\[
 m_+^\dagger m_+-m_-^\dagger m_-
 =\begin{pmatrix}0&2\eta\\-2\eta&0\end{pmatrix}\ne0.
\]
Also \(j\) induces the known isogeny \(J(C)\to E^2\). Therefore the induced map of unipotent groups factors through the full depth-two quotient \(U_2(C,b)\) and is surjective on its first graded quotient and its central line. In particular, every admissible global depth-two class on \(C\) has an image in (44), with functorial localizations.

This is the non-split-torus version of the geometric quadratic-Chabauty construction. The proof here only uses the explicit torsor, rather than any assertion that a rational-point height equation automatically gives a Selmer condition.

### 4. An explicit admissible global lift

Let
\[
 q=(T,T,-1)\in\mathcal X(\mathbf Q).
\]
Its existence is literal: in the fiber at \((T,T)\), the two line factors are the same, their ratio is canonically one-dimensional, and \(-1\) has norm one.

The global path torsor from \(\widetilde j(b)\) to \(q\) provides a reference lift \(\gamma\). Its abelian projection is the Kummer class of
\[
 (T-P,T)\in D(\mathbf Q),
\]
which becomes \((-P,0)\) after tensoring with \(\mathbf Q_p\).

Its required local properties can be proved without a general theorem about nonproper crystalline path torsors. The bundle \(\mathcal L\) is canonically trivial on \(E\times\{O\}\), since there \(m_+=m_-\). It is also canonically trivial on \(\{T\}\times E\): because \(T=-T\),
\[
 m_-(T,S)=-m_+(T,S),
\]
and the canonical symmetric linearization of \(\mathcal O_E(O)\) identifies the two pullbacks, preserving its canonical section. Both trivializations descend to \(\mathbf Q\); the constant \(-1\) sections give proper copies of \(E\) in \(\mathcal X\). They meet at \((T,O,-1)\), and their trivializations there agree. They connect
\[
 (P,O,-1)\longrightarrow(T,O,-1)\longrightarrow(T,T,-1).
\]
Concatenate the images of the two elliptic path torsors. Proper smooth good reduction of \(E\) at every odd prime shows that \(\gamma\) is crystalline at \(p\), and unramified at primes outside \(\{2,p\}\). No local-image condition at 2 is asserted or needed for this reference class.

### 5. Uniqueness in the global central fiber

The rank computation already established for this curve gives \(E(\mathbf Q)\otimes\mathbf Q_p=\mathbf Q_p P\), with \(P\) nontorsion. The elliptic logarithm of \(P\) is nonzero at every prime of good reduction: its kernel on \(E(\mathbf Q_p)\) is torsion. Consequently
\[
 D(\mathbf Q)\otimes\mathbf Q_p\longrightarrow H_f^1(\mathbf Q_p,V_pD)
\]
is injective. The same is true for \(J(C)\) through its isogeny with \(D\).

If \(W_0=(\pm i,0)\) were in the depth-two set, its global class would therefore have exactly the same global abelian projection as \(\gamma\), namely \((-P,0)\). This uses the Mordell–Weil projection clause of the Selmer definition.

For the central representation \(W=\mathbf Q_p(1)\chi_K\),
\[
 H^1_{f,\{2\}}(\mathbf Q,W)=0. \tag{45}
\]
Here the subscript permits arbitrary ramification at 2, requires the usual unramified conditions elsewhere away from \(p\), and requires the crystalline condition at \(p\). Indeed restriction to \(K\) and the eigenspace decomposition identify this group with the anti-invariant part of
\(\mathcal O_K[1/2]^\times\otimes\mathbf Q_p\). Class groups contribute only torsion. The unit group of the imaginary quadratic field \(K\) is finite, and there is a single prime over 2. Its valuation direction is invariant under \(c\). Thus the anti-invariant part is zero. Crystallinity excludes valuation directions at the primes above \(p\).

The usual cohomology sequence for a central extension says that two lifts of the same abelian class differ by an element of \(H^1(\mathbf Q,W)\), modulo the action of the abelian invariants. Here \(H^0(\mathbf Q,V_pD)=0\), and also \(H^0(\mathbf Q_p,V_pD)=0\), so the action in the relevant nonempty fibers is free. The imposed unramified/crystalline conditions put the difference of the two admissible lifts in the group (45). Thus their global classes, and hence their localizations, must agree.

For completeness, the crystalline-fiber assertion needs more than the vanishing of ordinary invariants. The group \(U_{\mathcal X}\) is a crystalline quotient of \(U_2(C)\), because \(C\) has good reduction at \(p\). Twisting by the crystalline reference torsor \(\gamma\) preserves crystallinity. Apply exactness of \(D_{\mathrm{cris}}\) to
\[
 0\longrightarrow\operatorname{Lie}W
 \longrightarrow\operatorname{Lie}(U_{\mathcal X}^{\gamma})
 \longrightarrow V_pD\longrightarrow0.
\]
It gives surjectivity on \(B_{\mathrm{cris}}\)-valued Galois invariants, using exponential coordinates. Thus the connecting boundary from \(V_pD(B_{\mathrm{cris}})^{G_{\mathbb Q_p}}\) vanishes. A central difference between two crystalline lifts is therefore in \(H_f^1(\mathbb Q_p,W)\). Ordinary \(H^0(\mathbb Q_p,V_pD)=0\) separately gives freeness. Compare the finite-Selmer exact sequence in [11, proof of Proposition 2.2]. At a prime \(q\ne2,p\), good reduction and the absence of Frobenius eigenvalue 1 give the analogous unramified conclusion.

### 6. The local difference is nonzero

By (43), the points \(q\) and \(\widetilde j(W_0)\) lie above the same point \((T,T)\). Their ratio in that torus fiber is
\[
 t_{W_0}=-g(W_0)^{-1}\in\mathcal T(\mathbf Q_p).
\]
The difference of the corresponding local path classes in (44) is exactly the image of its torus Kummer class
\[
 \kappa_{\mathcal T}(t_{W_0})\in H_f^1(\mathbf Q_p,W). \tag{46}
\]
The inclusion into the central fiber is injective because \(H^0(\mathbf Q_p,V_pD)=0\).

To see that (46) is nonzero, put \(F=K\otimes\mathbf Q_p\). In the split case \(F=\mathbf Q_p\times\mathbf Q_p\), the two coordinates of \(g(W_0)\) are inverse units. In the inert case \(F\) is the unramified quadratic extension, and \(c(g(W_0))=g(W_0)^{-1}\). In either case ordinary Kummer theory after restriction to a splitting field identifies the finite torus Kummer class with the appropriate norm-zero component of the logarithm of this unit.

For \(W_0=(i,0)\), equation (42) gives
\[
 g(W_0)=-(1+r)^2,\qquad r=s/i,\qquad r^2=2.
\]
This is an algebraic unit and is not a root of unity: under a real embedding its absolute value is \((1+\sqrt2)^2>1\). The kernel of the \(p\)-adic logarithm on the units of a finite extension of \(\mathbf Q_p\) consists of roots of unity. Therefore its logarithm is nonzero. Restriction to a finite splitting field is injective on \(\mathbf Q_p\)-cohomology, by restriction–corestriction; hence (46) itself is nonzero. Replacing \(i\) by \(-i\) inverts \(g\) and gives the same conclusion.

This contradicts the equality of localizations forced by (45), proving the statement.

The structural central extension (44) is also described in [12, Section 3, equation (3.0.1)]. Its norm-one descent, explicit curve lift, and admissible reference path have been constructed above, so no sufficiency claim based merely on the two earlier scalar heights is used. ∎

## 16. A complete depth-two calculation at p=3

**Theorem 21.** For the smooth projective curve (11), using the Mordell–Weil abelian-image and actual-local-image Selmer convention of Section 13,
\[
 C(\mathbf Q_3)_2=C(\mathbf Q)
 =\{(0,1),(0,-1),\infty_+,\infty_-\}.
\]
Moreover, the four points with x=±1 are excluded from the full depth-two set at p=3. Together with the preceding results, all fourteen specified nonrational first-height candidates are excluded at every odd prime where locally visible.

**Proof.** Complete details, including every infinite-tail estimate and the endpoint-basepoint comparison, are supplied in the following three companion proofs:

1. [Exact prime-3 height certificate](proofs/prime3_height_certificate.md): identify the CM unit-root complement, use the normalized double integral, and prove h₃(P) ≡ 2 mod 3 with a rigorous infinite-tail bound. Also L(P)/3 ≡ 2 mod 3 and 3ζ(P) ≡ 1 mod 3.
2. [Uniform isolation on all eight residue disks](proofs/prime3_disk_isolation.md): on the four disks around the rational points, the first height has no other zero. On the remaining four disks, the second height reduces to h₃(P)(2−(u/L(P))²) modulo 3, which cannot vanish. Both actual targets are {0}. Thus the intersection of the two height conditions is exactly the four displayed points.
3. [Endpoint-basepoint containment](proofs/endpoint_basepoint_bridge.md): a double twist of a fixed truncated path module gives joint regularity in the basepoint and endpoint. The cycle comparison over the generic function field extends the adjacent extensions across the endpoint basepoint and retains its necessary linear height correction. This extends Theorem 18 to that basepoint and proves that both scalar conditions contain the full restricted depth-two set.

Every displayed point is rational and hence satisfies the global Selmer conditions. The necessary conditions from steps 2 and 3 give the reverse inclusion. This proves the full equality, not just a candidate-set calculation. The four-point p=3 exclusion also follows directly from the second-model endpoint values ±2h₃(P). ∎

Independent audits are included in [verification/prime3_independent_audit.md](verification/prime3_independent_audit.md) and [verification/endpoint_basepoint_independent_audit.md](verification/endpoint_basepoint_independent_audit.md). Exact standard-library verification scripts are `scripts/check_prime3_height.py` and `scripts/check_prime3_six_multiple.py`; the latter independently reproduces the height residue through 6P. Finite checks corroborate, and do not replace, the proved all-orders bounds.

## 17. A reciprocal-family theorem and another complete example

**Theorem 22 (sufficient family criterion).** Let
\[
 C_a:y^2=x^6+a x^4+a x^2+1,\qquad a\equiv-5\pmod{5832},
\]
and put E_a:Y²=X³+(a−3)X²−(a−3)X. Assume E_a(Q) has rank one. For each odd prime q dividing a+1 at which 2 is a quadratic residue, put m_q=v_q(a+1), and assume
\[
 v_3(m_q)<v_3(q^2-1).
\]
Then, in the stated Mordell–Weil-restricted, actual-local-image convention,
\[
 C_a(\mathbf Q_3)_2=C_a(\mathbf Q)
 =\{(0,1),(0,-1),\infty_+,\infty_-\}.
\]
A simpler sufficient arithmetic condition is that none of the odd-prime multiplicities in a+1 is divisible by 3. In particular, a squarefree odd part of |a+1| suffices. Rank one remains a separate hypothesis; no infinitude of rank-one parameters is asserted.

**Proof.** [The general analytic criterion](proofs/general_prime3_criterion.md) proves all eight disk estimates uniformly for a≡−5 modulo 3⁶, using compatible integral complements and quantitative formal-series bounds. [The exact local-target calculation](proofs/reciprocal_local_targets.md) proves that the first actual target is {0} and, under the displayed prime-factor test, the second target is contained in 3Z₃. The first height isolates the four rational endpoints, while the second height is a unit on the other four residue disks. The endpoint-basepoint containment proved in Section 16 supplies the full-depth-two inclusion. Rational-point containment supplies the reverse inclusion. ∎

The local-target result is broader than this sufficient equality theorem. At an odd q dividing a+1, with m=v_q(a+1), its second coefficient image is exactly:

- If 2 is a square modulo q: {0} together with ±2k(m−k)/m for 1≤k≤floor(m/2).
- If 2 is a nonsquare and m is odd: {0}.
- If 2 is a nonsquare and m is even: {0,±m/2}.

Each coefficient multiplies logₚ(q). The displayed prime-factor condition is necessary and sufficient for the stronger target containment Ω′⊆3Z₃ in this progression; it is not asserted necessary for full-depth-two equality. For example a=23323 lies in the analytic progression but has the target unit −(4/3)log₃7. This is an obstruction to that target-containment test, not a counterexample to full-depth-two equality.

**Corollary 23 (a second fully certified curve).** The theorem applies unconditionally to a=−157469. Its elliptic quotient has rank one by exact two-isogeny descent: the two descent images have cardinality at most 2 and 4, and the nonzero formal logarithm proves rank at least one. Also a+1=−4·39367, with 39367 prime, so both actual targets are zero. Thus
\[
 C_{-157469}(\mathbf Q_3)_2=C_{-157469}(\mathbf Q)
 =\{(0,1),(0,-1),\infty_+,\infty_-\}.
\]
The Jacobian has rational rank two. Full [rank proof](proofs/rank_one_parameter_157469.md), [finite obstruction list](verification/rank_one_obstructions.txt), and [independent audit](verification/general_family_independent_audit.md) are supplied. The independent checker re-tests all primitive residue pairs rather than reusing the original two-chart enumeration.

This is a conditional family theorem with two fully verified members, not a classification of every curve or prime. Exact checks are `scripts/check_general_prime3.py`, `scripts/check_rank_one_parameter.py`, and `scripts/check_rank_one_independent.py`.

## 18. Checkable rank patterns and further good primes

The following results separate rank certification from local analytic isolation. All depth-two equalities retain the Mordell–Weil-restricted, actual-local-image convention.

**Theorem 24 (arithmetic rank criteria).** Each of the following conditions proves rank E_a(Q)=1 by elementary two-isogeny descent:

1. a=3−32r, where r and 8r−1 are primes and r≡3 or5 modulo8.
2. a=3−8n², where n>1 is odd, every prime dividing n is 3 or5 modulo8, exactly one prime congruent to3 modulo8 occurs to odd exponent, and 2n²−1 is prime.

The [complete proof](proofs/checkable_rank_patterns.md) also states the precise prime-power extensions. The descent images are determined exactly, not inferred from local solubility. In case1 the extra condition r≡547 modulo729, and in case2 n≡±1 modulo729, place the curve in Theorem22 with zero actual targets. Ten explicit examples, including a=−204125 and a=−67977797, have exact certificates. These are checkable implications, not assertions of infinitely many prime patterns or rank-one parameters. Oddness of n is essential: dropping it permits n=6, where a rational point forces rank at least two.

**Theorem 25 (two prime-7 neighborhoods).** The first scalar height alone has exactly four rational endpoint zeros for every odd integer a in either progression
\[
 a\equiv-5\pmod{343},\qquad\text{or}\qquad a\equiv-605\pmod{49}.
\]
If additionally a≡3 modulo8 and E_a(Q) has rank one, this gives
\[
 C_a(\mathbf Q_7)_2=C_a(\mathbf Q)
 =\{(0,1),(0,-1),\infty_+,\infty_-\}.
\]
The combined progressions are respectively −5 modulo2744 and −605 modulo392. No restriction on the prime multiplicities in a+1 is needed. The unconditional examples a=−5, a=−2033309 and a=−605 have certified rank one.

The [eight-disk proof](proofs/prime7_isolation.md) controls four rational endpoint disks and four Weierstrass disks uniformly, with an independent 4P/8P height check. It uses a fixed height complement, not an ordinary or unit-root assumption; E_{−5} is supersingular at7. The [four-disk proof](proofs/prime7_four_disk_family.md) treats a second residue pattern using a dominating quadratic coefficient. Both include infinite-tail and parameter-continuity bounds.

**Theorem 26 (the second certified curve at11).** For a=−157469,
\[
 C_a(\mathbf Q_{11})_2=C_a(\mathbf Q)
 =\{(0,1),(0,-1),\infty_+,\infty_-\}.
\]
Its first height has exactly eight zeros: the four rational endpoints and the four x=±1 centers. The second height excludes the latter. The [complete proof](proofs/prime11_isolation.md) reduces the nonrational residue disks to the two polynomials T(8−4T²) and 6+4T² over F_11, which have no common root, and proves bounds for every remaining series term. The existing exact rank and zero-target certificates apply at11.

Finally, the [small-disk classification](proofs/small_disk_classification.md) uses Hasse's bound and exhaustive finite-field enumeration to identify every relevant reduction with at most eight rational disks for odd a. After the scalar obstruction at p≡1 modulo4 is removed, only p=3,7,11,19,23 remain for this particular layout. At p≡1 modulo4 both scalar heights retain (±i,0), so their intersection cannot be just the four endpoints. This never proves full-depth-two membership of those points and does not preclude non-scalar obstructions or successful larger-disk methods.

Independent audit reports and exact scripts accompany every statement in `verification/` and `scripts/`. General classification across all parameters and primes remains open.

## 19. Uniform endpoint-only families at 7, 11 and 19

**Theorem 27.** Let a be odd and use the reciprocal family, fixed integral complement, and scalar normalization specified in [the full proof](proofs/uniform_endpoint_families.md). The first scalar height has exactly the four rational endpoint zeros in each locus:
- p=7, a≡4 mod7 and a not≡46 mod49;
- p=11, a≡2 mod11 and a not≡24 mod121;
- p=19, a≡0 mod19.

If additionally a≡3 mod8 and rank E_a(Q)=1, the full Mordell–Weil-restricted, actual-local-image depth-two set equals those four rational points. The omitted residue lifts are unresolved by this leading-digit argument, not counterexamples. At 19 the combined progression is a≡19 mod152, still conditional on rank one.

The proof factors the endpoint identity by alpha, permitting arbitrary negative v_p(alpha), rather than only −1. Exact tripling and quadrupling formulas establish the needed valuations for every parameter, including arbitrarily large v7(a−4), v11(a−2), and v19(a). Entire-series denominator bounds control all omitted terms. The four residue disks exhaust each reduction.

The previously proved rank patterns certify a=−18269 at 11 and a=−17309, −3474245 at 19; a=−605 at 7 is retained. These arithmetic certificates do not establish infinitude. The complete proof, review and standalone exact script are in proofs/uniform_endpoint_families.md, verification/endpoint_families_review.md and scripts/check_endpoint_families.py. The general classification remains open.

## 20. Unconditional infinitude for rational parameters

**Theorem 28.** There are infinitely many a∈Q∩(−1,3) for which E_a(Q) has rank one and Jac(C_a)(Q) has rank two. The resulting genus-two curves include infinitely many geometric isomorphism classes.

This is an explicit transfer of Zywina's existing infinitude theorem, not an infinitude assertion about the earlier simultaneous-prime patterns. With t∈(0,1), set A=−8t/(t+1), a=A+3 and s=(t+1)/2. Scaling the two-isogenous curve E'_A by (u,v)=(s²X,s³Y) gives exactly the family used in Zywina, arXiv:2505.16960v1, Theorem 1.5 and Section 4. Rank is preserved under isogeny. The two independent elliptic quotient differentials give Jac(C_a) isogenous to E_a².

The [complete proof](proofs/rational_rank_infinitude.md) verifies the source specialization statement, inverse parameter, smoothness and infinitely many curve isomorphism classes. An exact script and independent review accompany it. This does not establish infinitely many integral parameters or infinitely many full depth-two endpoint equalities; denominator primes require separate local analysis.

## 21. Exact four-versus-twelve scalar classification

**Theorem 29.** For odd a and (p,a mod p)=(7,4) or (11,2), use the constants of Theorem 27 and set κ=1−Z+alpha(1−ell). The first scalar height has exactly twelve distinct zeros if 0≠κ∈p²Z_p and −κ is a square in Q_p. Otherwise it has exactly four zeros, the rational endpoints. If κ=0 the endpoints have multiplicity four, not extra distinct zeros.

The twelve-zero alternative can occur only at a≡242 mod343 for p=7 or a≡508 mod1331 for p=11. These necessary congruences alone are not sufficient. The [full proof](proofs/endpoint_bifurcation.md) derives the exact quartic coefficient, shows it is a square unit in the critical cases, and controls the entire higher tail by a contraction argument. It supplies the complete squareclass criterion rather than an unexplained finite-precision test.

Together with the prime-19 result, this classifies every scalar case whose smooth reduction has exactly four rational points: precisely (p,a mod p)=(7,4),(11,2),(19,0). It does not classify all other disk layouts.

Exact examples with twelve scalar zeros are a=12487 and a=656691 at 11, and a=17735 at 7. The extra points are called nonendpoint, not necessarily nonrational; no rank-one certificate is asserted for these examples. Under the separate rank-one and a≡3 mod8 hypotheses, four scalar zeros give full restricted depth-two equality, while twelve give only an upper bound of twelve. Additional scalar zeros are not thereby proved to belong to the full depth-two set.

## 22. The second height removes all eight bifurcating extras

**Theorem 30.** In the omitted endpoint lifts a≡46 mod49 at p=7 and a≡24 mod121 at p=11, the second scalar has exactly the four rational endpoint zeros. Its local slope is −2(1+Z+alpha ell), a unit; a full-series estimate proves rho*(x)/x lies in that slope+p²Z_p throughout each noncentral endpoint disk.

If a≡3 mod8, E_a(Q) has rank one and the actual second target is {0}, the full restricted depth-two set is exactly the four endpoints. Combining with Theorem27 gives this conclusion for every a≡4 mod7 or a≡2 mod11 under these arithmetic hypotheses, with no omitted-lift exception. Squarefree odd part of a+1 is sufficient for the second target; the exact weaker criterion is stated in the [complete proof](proofs/second_height_endpoint_exclusion.md).

For a=−14974109 at7, r=467941 and q=3743527=8r−1 are prime, proving rank one through the existing descent theorem, while a+1=−4q gives zero actual targets. Exact calculations show twelve first-scalar zeros but four second-scalar zeros. Consequently C_a(Q_7)₂=C_a(Q) is the four rational endpoints. All eight additional first-height zeros are excluded from the full restricted depth-two set.

The second model's basepoint (u,v)=(−1,−4) satisfies Theorem18 directly, so the new omitted-lift upper inclusion needs no endpoint-basepoint continuation. The proof and independent review include exact compatible primitive identities, full-series bounds, correct reciprocity symmetry, and an independent degree20 certificate. Necessary valuation and residue tests for nonzero second targets are also supplied; they are not sufficiency claims.

## 23. A second scalar-invisible pair excluded by a torus quotient

**Theorem 31.** For C_15:y²=x⁶+15x⁴+15x²+1, the Jacobian has rational rank two. At every prime p≡1 mod4, neither (i,0) nor (−i,0) belongs to the full depth-two set under the stated Mordell–Weil abelian-image convention.

The [complete proof](proofs/cm15_torus_exclusion.md) supplies an elementary rank-one certificate for E:Y²=X³+12X²−12X and a degree-three CM map over Q(sqrt(−3)). Its norm-one-torus quotient detects the local Kummer class of −7+4sqrt(3), or its inverse, a non-torsion algebraic unit. This applies at both split and inert CM primes, without an ordinary-height assumption.

Here the degree-eight origin fibers share all six Weierstrass points. The proof checks that complete divisor, evaluates the necessary 0/0 section ratio by derivatives, and uses the correct proper reference endpoint (T,T,+1). These details differ essentially from the earlier a=−5 construction. The anti-invariant S-unit group vanishes for S={2,3}, and the nonzero local torus class contradicts global central-fiber uniqueness.

The pair has zero in both earlier scalar expressions, so this is a genuine additional central obstruction. It does not classify all points of C_15(Q_p)₂ or provide a general non-CM criterion. Exact map identities, descent obstructions and fiber values are verified by scripts/check_cm15_torus.py, with independent review and passing output.

## 24. Rational denominator primes: the two targets differ

**Theorem 32 (exact denominator-prime targets).** Let a be rational, a != -1,3, and let q != p be odd with v_q(a)=-m<0. Set beta=q^m a and chi=(beta/q). The second-model local target is {0}, and lambda_q(1,1)=(m/2)log_p(q). The exact first-model coefficient image is

    {±m/2}
    union {±2k(m-k)/m : 1<=k<m/2, m even, chi=1}
    union Z,

where Z={0} exactly when q=1 modulo 4, or m is even and (q!=3 or chi=-1); otherwise Z is empty. In particular a=13/7, q=7 gives the nonzero first image {±log_p(7)/2}.

The complete proof, including normalized ramified base extension, actual-image attainability and the exceptional q=3 case, is in [rational_denominator_targets.md](proofs/rational_denominator_targets.md). Independent review and exact checks are in [the review](verification/rational_denominator_review.md) and [the script](scripts/check_rational_denominators.py).

For rational a in Z_2 with a=3 modulo 8 and positive reduced denominator D prime to p, the global point height is h_p(P)=lambda_p(P)+(1/2)log_p(D). Therefore an integral-parameter proof cannot be extended simply by retaining the old alpha coefficient or assuming its first target is {0}. The second target remains {0} when every positive odd valuation of a+1 is one. These are exact local and global-height statements, not a general full-depth-two classification.

## 25. An infinite rank-one family with zero second target

**Theorem 33 (unconditional rational infinitude with a local condition).** There are infinitely many rational a in (-1,3), yielding infinitely many geometric genus-two isomorphism classes, with rank E_a(Q)=1, rank J_a(Q)=2, a=3 modulo 8 in Z_2, and every positive odd valuation of a+1 equal to one. For every good odd p their entire second actual local target is therefore Omega*={0}. For any fixed odd p and N>=1 the construction can additionally impose v_p(a+5)>=N, with good reduction at p.

The proof combines the fully audited local valuation conditions in Zywina's construction with Theorem 32. See [complete proof](proofs/infinite_zero_second_target.md), [independent source audit](verification/infinite_second_target_review.md), and [exact algebra checks](scripts/check_infinite_second_target.py).

This is an unconditional infinite family satisfying rank and the second-target condition, not an infinite family of proved full-depth-two equalities. Denominator contributions to the first target and global height remain; merely imposing the displayed p-adic neighborhood does not establish the older analytic hypotheses for rational parameters. No infinitude of integral parameters is asserted.

## 26. General non-CM residual lifting and exact full gluing

**Theorem 34 (residual Selmer localization and joint criterion).** Suppose E_a is geometrically non-CM of rank one, p is good and 1 modulo 4, and R=Sym²(V_pE_a). Newton–Thorne's proved adjoint vanishing and Selmer duality imply H_f^1(Q,R)=0. For a finite set S containing all bad primes and excluding p, localization is an isomorphism

    H_f,S^1(Q,R) -> direct-sum_(q in S) H^1(Q_q,R).

The involution x -> -x provides a canonical reference lift for the common abelian class of W_±=(±i,0). Its two local discrepancies delta_p(W_±) lie in the two-dimensional H_f^1(Q_p,R) and are negatives of one another. The residual quotient criterion is exactly membership in the finite target obtained by transporting all actual bad-prime residual images through the inverse localization map.

Only 2 and odd primes with v_q(a-3)>0 can contribute nonzero ACTUAL residual targets. Multiplicative primes and odd denominator primes have zero local H^1(R); good primes have zero actual image but can have nonzero full H^1(R).

Furthermore U2 is the fiber product of its Tate and residual quotients, in both ordinary and crystalline cohomology here. Full membership is equivalent to one compatible global Tate lift together with joint bad-local pairs arising from the SAME local point, whose residual coordinates transport to delta_p(W). Neither separate scalar target membership nor replacing joint images by products is sufficient without another proof.

See [complete proof and exact quantified criterion](proofs/noncm_residual_gluing.md) and [independent audit](verification/noncm_residual_gluing_review.md). The proof evaluates neither delta_p(i,0), the surviving joint local images, nor the global Tate lift. It therefore does not settle general non-CM membership or establish any new general exclusion.

## 27. Actual exclusions in an infinite non-CM family

**Theorem 35 (denominator obstruction and infinite exclusions).** For rational a=M/D in lowest terms, D>0, the first-height actual-target containment extends by clearing denominators and using the true global height. Call an odd prime eligible when it does not divide D(M-3D)(M+D).

Assume a=3 modulo 8 in Z_2 and rank E_a(Q)=1. The visible points (±i,0) pass the first-height test exactly when every odd denominator prime q satisfies the zero-attainment test of Theorem 32. In particular, a prime q=3 modulo 4 with odd denominator multiplicity excludes both points from full depth two. The same obstruction excludes every visible point (±1,±sqrt(2(a+1))), since its first scalar also vanishes. Cancellation between different primes cannot rescue these points: prime logarithms are Q-linearly independent.

For any nonintegral rational a in (-1,3), the four remaining quartic Weierstrass points fail every actual first-height target whenever visible. Indeed their squared x-coordinates have complex absolute value one; a candidate logarithmic relation would make their trace 1-a a rational algebraic integer.

Taking Zywina's construction with source quadratic extension Q(i) gives infinitely many geometrically different rational parameters in (-1,3), with rank E_a=1 and rank J_a=2, whose distinguished denominator prime is 3 modulo 4 with multiplicity one. Its negative j-valuation also proves geometric non-CM. At EVERY eligible odd prime, all locally visible points in the ten-point geometric packet (six Weierstrass points and the four x=±1 points) are absent from the full restricted depth-two set.

See [complete proof](proofs/infinite_weierstrass_exclusion.md), [independent review](verification/weierstrass_exclusion_review.md), and [exact checks](scripts/check_weierstrass_exclusion.py). This is an actual infinite-family exclusion theorem, not an evaluation of the Sym² discrepancy or a full classification of non-Weierstrass members. No endpoint-only equality for an infinite family is claimed.

## 28. Exact odd bad-prime residual and joint images

**Theorem 36 (odd residual local images).** Let q be odd, q!=p, and n=v_q(a-3)>0. Use the basepoint (0,1) and the central coordinates T=Q_p(1)^2 and R=Sym²V from Theorem34. If q=3 modulo4, the actual residual image Delta_q and the same-point joint image Xi_q are both zero. If q=1 modulo4, choose i in Q_q and put e_q=r_q(i,0). Then e_q is NONZERO and

    Delta_q={0,±e_q} union {±(4k/n)e_q : integers 1<=k<n/4},
    Xi_q={(0,delta):delta in Delta_q}.

Every listed value is attained. The proof constructs the two-elliptic-component stable fiber, verifies its edge length n/2 and midpoint basepoint, identifies the separating class as nonzero and entirely in R, and applies the published Betts–Dogra graph Kummer formula. The exact same-point Tate projection vanishes, rather than merely satisfying two separate numerical tests.

For a=-157469, the only possible odd residual contribution is at37, where Delta_37={0,±e_37}; the images at7 and19 vanish. The dyadic image, global transport Theta_p and local discrepancy delta_p remain separate problems.

The same stable model proves that an odd prime q is good for C_a exactly when a is q-integral and a modq is neither -1 nor3. Consequently the explicit eligible primes in Theorem35 are ALL odd good-reduction primes of the abstract curve. Its infinite-family exclusions therefore hold at every odd good prime, whenever the points are visible.

See [complete proof](proofs/odd_bad_residual_images.md), [independent audit](verification/odd_bad_residual_review.md), and [exact checks](scripts/check_odd_bad_residual.py). No dyadic calculation or general full-set equality is asserted.

## 29. The compatible Tate lift is uniquely determined

**Theorem 37 (residual sufficiency for the integral family).** Suppose a is integral, a=3 modulo8, E_a is geometrically non-CM of rank one, and p is an odd good prime congruent1 modulo4. There is a unique global crystalline U_T lift of the common abelian class of W_±=(±i,0) whose local classes at every bad prime are neutral. Its p-localization equals BOTH j_T,p(W_+) and j_T,p(W_-).

The proof first removes the global central obstruction by Brauer localization, then uses Kummer S-units to construct and uniquely normalize the lift. The two correspondence functionals span the full Tate center. Their arbitrary-torsor height comparison, with the endpoint-basepoint correction retained, proves equality with the local point classes. No scalar sufficiency is assumed.

Every actual residual local value can be represented with neutral Tate coordinate, including at2 by the two independent zero local-height functions. Theorem34's same-point gluing therefore gives the exact equivalence

    W_± in C_a(Q_p)_2 iff delta_p(W_±) in Omega_R,p.

This discharges the previously unresolved Tate-lift existence and joint-compatibility quantifier in THIS integral family. It does not compute the dyadic residual image, global transport Theta_p, or the discrepancy delta_p itself. The exact odd factors of Omega_R,p are supplied by Theorem36.

See [complete proof](proofs/integral_tate_lift.md) and [independent audit](verification/integral_tate_lift_review.md).

## 30. Dyadic residual vanishing in an infinite congruence subfamily

**Theorem 38 (dyadic residual cohomology).** Let a be integral, a=3 modulo8, and suppose n=v_2(a-3) is odd and at least5. For every odd coefficient prime p, including3,

    H^1(Q_2,Sym² V_p(E_a))=0.

No rank or non-CM hypothesis is required for this local assertion. The two already established independent zero Tate-height coordinates consequently give the exact same-point local image Xi_2={(0,0)}.

The proof scales, and when necessary quadratically twists, E_a to y²=x³+c x²-2B x with B odd and c divisible by8. An exact Newton polygon for its third division polynomial forces wild inertia Q_8. The common good special fiber transports its faithful, absolutely irreducible representation to every odd-p Tate module. The residual representation has no wild-inertia invariants; inflation-restriction gives the claimed cohomology vanishing.

Under the additional global hypotheses of Theorem37, the full membership criterion for W_±=(±i,0) now has only the explicit odd factors from Theorem36: those at primes q=1 modulo4 dividing a-3. If no such prime occurs, it is exactly

    W_± in C_a(Q_p)_2 iff delta_p(W_±)=0.

For a=-605 and a=-1373 all residual local targets are zero; use the full equivalence only when the rank-one global hypotheses hold. For the certified example a=-157469, the global target is {0,±Theta_p(e_37)}, with at most three values; no injectivity of Theta_p is asserted. In particular this theorem does NOT evaluate delta_p(W), show it is nonzero, or by itself exclude W.

The cases n=3 and even n are not covered. See [complete proof](proofs/dyadic_residual_vanishing.md), [exact checks](scripts/check_dyadic_residual.py), and [independent audit](verification/dyadic_residual_review.md).

## 31. The dyadic theorem extends to every valuation at least four

**Theorem 39 (even dyadic valuations).** In the integral reciprocal family, for every n=v_2(a-3)>=4 and every odd coefficient prime p,

    H^1(Q_2,Sym² V_p(E_a))=0,    Xi_2={(0,0)}.

The odd n cases are Theorem38. For even n, scaling and, if necessary, quadratic twisting reduces to y²=x³+c x²-Bx with B odd and c divisible by4. Its third division polynomial has a biquadratic splitting field over Q_2^nr. An exact Hensel deformation preserves the absence of root stabilizers, forcing wild inertia Q_8 and the same cohomology vanishing.

Thus the result covers the entire integral congruence subfamily a=3 modulo16, excluding a=3. Neither rank nor non-CM is needed for local cohomology vanishing; global conclusions retain Theorem37's hypotheses. The remaining integral a=3 modulo8 case is n=3, which is not covered.

See [proof](proofs/dyadic_even_valuation.md), [exact checker](scripts/check_dyadic_even.py), and [independent audit](verification/dyadic_even_review.md).

## 32. A nonzero global quadratic-twisted discrepancy class

**Theorem 40 (twisted descent and its localization boundary).** Fix K=Q(i), its quadratic character chi, and a good odd p=1 modulo4. The central difference between the K-rational point W_+=(i,0) and the canonical global reference descends uniquely to a class

    eta_p in H^1(Q,Sym² V_p(E_a) tensor chi),
    loc_p(eta_p)=delta_p(W_+).

Arithmetic conjugation and the geometric involution x->-x both exchange W_+ and W_-, but only the latter acts as -1 on the residual center; comparing them proves the required anti-invariance. The p-local class is crystalline.

For every odd q with v_q(a-3)>0, the restriction to Q_q(i) is a nonzero ramified endpoint class. In particular, for a=-605 it is nonzero at19, so eta_p is globally nonzero, including at coefficient prime p=5. This is NOT a proof that delta_p(W_+) is nonzero: the latter is a different localization.

For a=-605, Theorem37 and the zero actual residual targets give the exact full-membership criterion

    W_± in C_a(Q_p)_2 iff loc_p(eta_p)=0.

A dimension formula further shows that, when a-3 has at least two distinct odd prime divisors of positive valuation and E is non-CM, the relaxed twisted Selmer source has dimension at least3, whereas its crystalline p-local target has dimension2. Blanket localization injectivity is then impossible. This does not decide localization on the distinguished line generated by eta_p.

See [complete proof](proofs/twisted_discrepancy_descent.md) and [independent audit](verification/twisted_discrepancy_review.md). No value of delta_p or Theta_p and no new full-set equality are asserted.

## 33. Complete rational-CM Weierstrass subcase

**Theorem (complete rational-CM subcase).** For the reciprocal family C_a, the rational parameters with geometrically CM elliptic quotient are exactly 0, −3/2, −15/16, −5, 15, −33 and 255. The parameter 0 has elliptic rank zero. Each of the other six has elliptic rank one and Jacobian rank two. At every odd good prime, every locally visible Weierstrass point on each of these six curves is excluded from the full depth-two set in the stated Mordell–Weil abelian-image and actual-local-image convention.

The [complete proof](proofs/rational_cm_weierstrass_classification.md) supplies the finite CM-parameter classification, elementary two-isogeny rank certificates, four new explicit torus quotients, complete origin-fiber divisors and reference-path normalizations. For a=−33 the origin-fiber comparison requires a third-order divided by first-order limit, producing relative torus value 1/9; for a=−3/2 the corresponding value is 1/3. The Q(√−7) values at a=−15/16 and 255 are respectively (431−160√7)/81 and (364961−137920√7)/6561.

The Q(√−7) cases retain the potentially nonzero global S-unit space. Betts's rationality theorem for actual local Néron metrics forces rational coefficients through the injective valuation map on imaginary-quadratic norm-one S-units. Clearing denominators then gives an exact algebraic logarithm comparison; complex absolute values exclude every allowed combination. The argument does not substitute a vanishing assumption for these nonzero targets. The remaining Weierstrass points follow from the existing root-power criterion, except the four additional points at a=−3/2, whose new torus values are (−1±2√−2)/3.

The exact checks are in [scripts/check_rational_cm_packet.py](scripts/check_rational_cm_packet.py). This theorem closes the entire rational-CM Weierstrass subclass, not the non-Weierstrass or general non-CM classification. In particular the non-CM comparison with {0,±Theta_5(e_37)} for a=−157469 is still open.

## 34. Uniform periods and the complete actual dyadic image

The [actual dyadic-image theorem](proofs/dyadic_actual_images.md) proves
Xi₂={(0,0)} for every a∈Z₂ with a≡3 modulo8 and a≠3, at every odd
coefficient prime. This includes v₂(a−3)=3, which was left open by
Theorems38–39. The conclusion concerns point images; it does not assert
vanishing of the entire local cohomology group in that remaining valuation.

The [uniform five-adic period theorem](proofs/universal_five_adic_residual.md)
proves X_a=5(a+5)U((a+5)/5), with U∈Z₅⟨b⟩ and U≡3 modulo5. Its
only zero for a∈5Z₅ is a=−5. In particular the [regular Frobenius
certificate](proofs/five_adic_residual_certificate.md) evaluates the
previously unevaluated localization for a=−605: its normalized holomorphic
coordinate is21625 modulo5⁷, of valuation3. This excludes W± there,
under the established rank-one global hypotheses and zero actual residual
targets. The CM case a=−5 is handled by its separate torus obstruction.

Combined with the [six-disk and gluing arguments](proofs/five_adic_selmer_dichotomy.md),
every integral a≡3 modulo8 with 5|a and rank E_a(Q)=1 has exactly the
four rational endpoints. Its full restricted depth-two set is either
those four or those four together with W±. The latter alternative can
only occur through a nonzero odd residual target; the dyadic target is
zero throughout. If every odd prime dividing a−3 is3 modulo4, the full
set is exactly the four endpoints.

The [prime-thirteen period theorem](proofs/universal_thirteen_adic_residual.md),
[critical-lift continuation](proofs/prime13_critical_lift.md), and
[nonzero second-scalar-target theorem](proofs/prime13_nonzero_second_targets.md)
give further full equalities with their stated residue, rank and actual
target hypotheses. A nonzero second scalar target in these theorems must
not be confused with an evaluated nonzero transported Sym² target.

## 35. Quintic reduction of the actual mod-five adjoint calculation

For a=−157469 set M=ad⁰(E_a[5]) and S={2,5,7,19,37,39367,∞}.
The [quintic-reduction theorem](proofs/adjoint_quintic_reduction.md) gives

    H¹(G_{Q,S},M) ≅ Hom(Cl_m(F(√5))/5,F₅)⁻,

where F is the quintic field defined by
t⁵−1574680t²−123981642460t−15618612205226992 and
m=(5³·2·7·19·37·39367)O_{F(√5)}. The involution fixes F.
The proof identifies M with the sign-twisted deleted five-point module,
proves H¹ and H² vanish for the auxiliary quadratic character over Q
with this S, and applies the resulting exact sequences, Shapiro and
class field theory. It uses the published Fernández–Lario modular
resolvent to identify the quintic field.

This replaces a degree-120 splitting-field calculation by a degree-ten
unrestricted ray-class calculation. The [exact checker](scripts/check_adjoint_quintic.py)
verifies the representation on all120 elements and the field identities.
No class-group dimension or propagated finite/crystalline local condition
is inferred from that checker. The comparison with {0,±Θ₅(e₃₇)} and the
general classification remain open.

### 35.1 Local lifting obstruction and conductor reduction

For the same actual curve let T=ad⁰(T₅E), M_n=T/5ⁿT. The
[local lifting theorem](proofs/adjoint_local_lifting.md) proves, for all n>=1,

    H¹(Q₇,M_n)=H¹(Q₃₉₃₆₇,M_n)=0,
    H¹(Q₁₉,M_n)≅Z/5Z,
    H¹(Q₃₇,M_n)≅Z/5ⁿZ (unramified).

Every map H¹(Q₁₉,M_(n+1))->H¹(Q₁₉,M_n) induced by coefficient
reduction is zero. Thus a global mod-five class that lifts even to
M_2 must have zero localization at 19. The proof identifies the local
group with ker(20:Z/5ⁿZ->Z/5ⁿZ); it does not infer lifting from its order.

Exact prime-ideal decompositions and the local logarithm reduce the
unrestricted ray modulus to P5^13 Q19 tau(Q19), where P5 is the unique
prime above 5 and the two Q19 primes have (e,f)=(2,2). Under Section 35's
global isomorphism, ker(loc_19) is exactly the anti-invariant character
space for modulus P5^13. This is a necessary condition for integral
lifts, not a complete finite/crystalline Selmer computation. No dimension
drop on the global space or value of the transported target is proved.

The exact finite-module checker and the bounded Hecke ideal-decomposition
checker both pass. The two long class-group computations have been
stopped without a class-group or ray-dimension result; the saved
smaller-base relations remain recoverable locally. The new modulus has
not been used to restart a long computation.

### 35.2 The residual quintic module has no lift on the same group

The [same-group lifting obstruction](proofs/adjoint_same_group_lifting.md)
proves that no free rank-three Z/25Z representation of S₅ reduces to
ad⁰(E[5]). In the displayed Sylow-five basis, every lift U+5B has
fifth-power entries (1,2)=15 and (2,3)=5 modulo25, so it cannot satisfy
the order-five relation. This excludes every such coefficient lift,
including ones unrelated to the deleted-permutation formula.

For the actual curve the projective mod-25 image is PGL₂(Z/25Z), of
order15,000. The existing nonzero fifth-power witness generates the
whole three-dimensional congruence kernel under conjugation. This is
an elementary specialization of the usual congruence lifting phenomenon.

Thus simply replacing F₅ by Z/25Z on the same S₅ quotient cannot extend
the degree-ten residual construction to integral precision. A further
algorithm must include the nontrivial congruence-kernel action. This
does not decide whether individual cohomology classes lift or evaluate
the original transported target. The new matrix checker passes, and
the finite-group argument was independently reviewed.

### 35.3 A nonzero discrepancy for the actual target at five

For a=-157469 the [pointwise ordinary certificate](proofs/actual_noncm_five_adic_period.md)
proves

    (1/i) integral_(W₋)^(W₊) nu₀ nu₁ = 22100+O(5⁷),

of valuation two. The earlier holomorphic-coordinate lemma therefore
gives delta₅(W)!=0. This removes zero from the actual target grid;
comparison with the two values ±Theta₅(e₃₇) remains open.

The two independent implementations agree in every displayed matrix
entry and all six cross periods. This parameter has ordinary reduction
and requires a new polynomial inverse in the regular Frobenius lift;
the supersingular inverse cannot be reused. The existing reduction
and tail bounds apply because this f is integral, monic and squarefree
modulo5. The true six-dimensional system has unit determinant, with
residue69632 modulo5⁷. The proof checks these hypotheses directly,
without extending the previous uniform parameter-family interpolation.

## 36. Boundary of this result

The exact classification in Theorem 2 concerns Weierstrass points of the specified bielliptic candidate set. Theorem 4 supplies a uniform non-Weierstrass mechanism in a rank-restricted one-parameter family, with a proved rank-two specialization. Theorem 4 itself neither proves rank infinitude nor classifies all non-Weierstrass candidates. Theorem 28 separately proves rational-parameter rank infinitude by transfer from Zywina's theorem.

Sections 8, 11, and 13 transfer exclusions to the full depth-two set in the stated Selmer convention: all eight points (17) are excluded, and so are the four points with x=±1 at their visible primes p≥5. Section 15 also excludes the pair \(\pm i,0\) at every odd prime where it is visible. Thus, for \(p\ge5\), all fourteen specified nonrational points that survive the first height test (the pair, the four points with x=±1, and the eight three-torsion candidates) are excluded from the full depth-two set whenever locally visible. This does not classify all other points of the full set or solve ICM Problem 6.4 in general. Section 16 closes the p=3 boundary and gives a complete full-depth-two calculation for this curve at p=3. Sections 17–18 supply explicit sufficient reciprocal-family criteria, arithmetic rank patterns, further certified members, and results at primes7 and11. These integral-family criteria do not classify the full set at all primes or for general curves, and do not prove infinitude within their integer parameter loci. Theorem 28 supplies an unconditional infinitude statement for rational rank-one parameters, without a full-depth-two conclusion. Theorem 29 completes the first scalar zero classification in all four-residue-disk cases. Theorem 30 then excludes its eight extras when the actual second target is zero, and certifies a twelve-versus-four full-depth-two example. Theorem 31 extends the non-scalar torus obstruction to a second CM curve. The full general classification remains open.

The exact examples themselves were already detected in [5]. The contribution of the arguments above is an exact algebraic membership test, an all-prime exclusion criterion, and a symmetry proof covering a parameter family. No priority claim is made beyond the literature checked here.

## References

1. J. S. Balakrishnan, *Chabauty and Beyond: Explicit p-adic Methods for Rational Points*, ICM 2026, especially Section 4.5 and Problem 6.4. https://doi.org/10.1137/25M1805011
2. F. Bianchi and O. Padurariu, *Rational points on rank 2 genus 2 bielliptic curves in the LMFDB*, Contemporary Mathematics 796 (2024), 215–242, especially Theorem 2.3 and Proposition 2.6. https://arxiv.org/abs/2212.11635
3. F. Bianchi, *Quadratic Chabauty for (bi)elliptic curves and Kim's conjecture*, Algebra & Number Theory 14 (2020), 2369–2416, especially Sections 2.1.2 and 3.4. https://arxiv.org/abs/1904.04622
4. J. S. Balakrishnan and A. Besser, *Coleman–Gross height pairings and the p-adic sigma function*, Proposition 6.1. https://arxiv.org/abs/1201.6016
5. K. Finnerty, *Quadratic Chabauty Experiments on Genus 2 Bielliptic Modular Curves in the LMFDB*, especially Remark 2.4, Remark 3.4 and Section 3.3. https://arxiv.org/abs/2507.03784
6. J. H. Silverman and J. Tate, *Rational Points on Elliptic Curves*, Undergraduate Texts in Mathematics, Springer, first edition (1992), Chapter III, Section 6, p. 91. https://doi.org/10.1007/978-1-4757-4252-7

7. A. Agboola and B. Howard, *Anticyclotomic Iwasawa theory of CM elliptic curves*, with Appendix A by K. Rubin, especially Theorem A.1 and Lemma A.2 (Bertrand's nonvanishing theorem). https://web.math.ucsb.edu/~agboola/papers/cm1-final.pdf
8. LMFDB, elliptic curve 256.a1, minimal equation and local root-number data. https://www.lmfdb.org/EllipticCurve/Q/256/a/1

9. J. S. Balakrishnan and N. Dogra, *Quadratic Chabauty and rational points I: p-adic heights*, especially Definition 2.2, Proposition 5.5, Theorem 6.3, and Lemma 7.5. https://arxiv.org/abs/1601.00388
10. M. Kim and A. Tamagawa, *The l-component of the unipotent Albanese map*, Math. Ann. 340 (2008), 223–235, Theorem 0.1; also restated in L. A. Betts, *Local constancy of pro-unipotent Kummer maps*, introduction. https://arxiv.org/abs/2203.03701

11. J. S. Balakrishnan and N. Dogra, *Quadratic Chabauty and Rational Points II: Generalised Height Functions on Selmer Varieties*, especially Section 2 and the proof of Proposition 2.2. https://arxiv.org/abs/1705.00401
12. L. Alexander Betts, *The motivic anabelian geometry of local heights on abelian varieties*, Section 3, equation (3.0.1). https://arxiv.org/abs/1706.04850




13. D. Zywina, *Rank one elliptic curves and rank stability*, arXiv:2505.16960v1 (2025), Section 1.1, Theorem 1.5 and Section 4. https://arxiv.org/abs/2505.16960
