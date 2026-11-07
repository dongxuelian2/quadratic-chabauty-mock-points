# Exact mechanisms for bielliptic height candidates

## 1. Scope and conventions

Balakrishnan's ICM survey [1, Problem 6.4] asks for an explanation of mock rational points on genus-two curves of Jacobian rank two. We study the explicitly defined **one-function bielliptic height-candidate set** below. For the standard local targets discussed below, this is a single-correspondence height condition; membership alone does not establish membership in the full depth-two Chabauty–Kim set.

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

This does not settle the full-depth-two membership of the six earlier points \((\pm i,0)\) and \((\pm1,\pm2\sqrt{-2})\), or classify all other points of the depth-two set. It does resolve the extra second-correspondence condition for the entire eight-point locus (17).

## 12. Boundary of this result

The exact classification in Theorem 2 concerns Weierstrass points of the specified bielliptic candidate set. Theorem 4 supplies a uniform non-Weierstrass mechanism in a rank-restricted one-parameter family, with a proved rank-two specialization. It neither proves that infinitely many parameters have rank one nor classifies all non-Weierstrass candidates.

Sections 8 and 11 transfer exclusions to the full depth-two set; Section 11 in particular excludes all eight points (17). The principal remaining arithmetic question is whether the surviving candidates satisfy the **full** depth-two Selmer conditions, including independent correspondences. In the reciprocal family the Jacobian is isogenous to a square of an elliptic curve, so additional correspondences are available. Establishing their effect is needed before claiming a solution of ICM Problem 6.4 for the full Chabauty–Kim set.

The exact examples themselves were already detected in [5]. The contribution of the arguments above is an exact algebraic membership test, an all-prime exclusion criterion, and a symmetry proof covering a parameter family. No priority claim is made beyond the literature checked here.

## References

1. J. S. Balakrishnan, *Chabauty and Beyond: Explicit p-adic Methods for Rational Points*, ICM 2026, especially Section 4.5 and Problem 6.4. https://doi.org/10.1137/25M1805011
2. F. Bianchi and O. Padurariu, *Rational points on rank 2 genus 2 bielliptic curves in the LMFDB*, Contemporary Mathematics 796 (2024), 215–242, especially Theorem 2.3 and Proposition 2.6. https://arxiv.org/abs/2212.11635
3. F. Bianchi, *Quadratic Chabauty for (bi)elliptic curves and Kim's conjecture*, Algebra & Number Theory 14 (2020), 2369–2416, especially Sections 2.1.2 and 3.4. https://arxiv.org/abs/1904.04622
4. J. S. Balakrishnan and A. Besser, *Coleman–Gross height pairings and the p-adic sigma function*, Proposition 6.1. https://arxiv.org/abs/1201.6016
5. K. Finnerty, *Quadratic Chabauty Experiments on Genus 2 Bielliptic Modular Curves in the LMFDB*, especially Remark 2.4, Remark 3.4 and Section 3.3. https://arxiv.org/abs/2507.03784
6. J. H. Silverman and J. Tate, *Rational Points on Elliptic Curves*, Undergraduate Texts in Mathematics, Springer, first edition (1992), Chapter III, Section 6, p. 91. https://doi.org/10.1007/978-1-4757-4252-7
