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

## 6. Boundary of this result

The exact classification in Theorem 2 concerns Weierstrass points of the specified bielliptic candidate set. Theorem 4 supplies a uniform non-Weierstrass mechanism in a rank-restricted one-parameter family, with a proved rank-two specialization. It neither proves that infinitely many parameters have rank one nor classifies all non-Weierstrass candidates.

The principal remaining arithmetic question is whether these points survive the **full** depth-two Selmer conditions, including independent correspondences. In the reciprocal family the Jacobian is isogenous to a square of an elliptic curve, so additional correspondences are available. Establishing their effect is needed before claiming a solution of ICM Problem 6.4 for the full Chabauty–Kim set.

The exact examples themselves were already detected in [5]. The contribution of the arguments above is an exact algebraic membership test, an all-prime exclusion criterion, and a symmetry proof covering a parameter family. No priority claim is made beyond the literature checked here.

## References

1. J. S. Balakrishnan, *Chabauty and Beyond: Explicit p-adic Methods for Rational Points*, ICM 2026, especially Section 4.5 and Problem 6.4. https://doi.org/10.1137/25M1805011
2. F. Bianchi and O. Padurariu, *Rational points on rank 2 genus 2 bielliptic curves in the LMFDB*, Contemporary Mathematics 796 (2024), 215–242, especially Theorem 2.3 and Proposition 2.6. https://arxiv.org/abs/2212.11635
3. F. Bianchi, *Quadratic Chabauty for (bi)elliptic curves and Kim's conjecture*, Algebra & Number Theory 14 (2020), 2369–2416, especially Sections 2.1.2 and 3.4. https://arxiv.org/abs/1904.04622
4. J. S. Balakrishnan and A. Besser, *Coleman–Gross height pairings and the p-adic sigma function*, Proposition 6.1. https://arxiv.org/abs/1201.6016
5. K. Finnerty, *Quadratic Chabauty Experiments on Genus 2 Bielliptic Modular Curves in the LMFDB*, especially Remark 2.4, Remark 3.4 and Section 3.3. https://arxiv.org/abs/2507.03784
6. J. H. Silverman and J. Tate, *Rational Points on Elliptic Curves*, Undergraduate Texts in Mathematics, Springer, first edition (1992), Chapter III, Section 6, p. 91. https://doi.org/10.1007/978-1-4757-4252-7
