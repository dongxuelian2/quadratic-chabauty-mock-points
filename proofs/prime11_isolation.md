# Two complementary residue polynomials at 11

Status: unpublished exact research proof. The standard-library certificate is `../scripts/check_prime11.py`. This supplies a second good prime for the rank-certified parameter a=−157469, without relying on a numerical search for height zeros.

## 1. A two-polynomial isolation criterion

Let p≥5 be a good odd prime for

\[
 C_a:y^2=x^6+ax^4+ax^2+1,\quad
 E:Y^2=X^3+AX^2-AX,\quad A=a-3.
\]

Put d=(a+1)/2 and suppose d is a p-adic unit square, with s²=d. Use the fixed compatible complements

\[
 W=\mathbf Q_p[(X-2)\omega],\qquad
 W'=\mathbf Q_p[(Z-a-1)\omega']
\]

on E and its 2-isogenous curve

\[
 E':Y^2=Z^3-2AZ^2+A(A+4)Z.
\]

The two genus-two models and their identical quotient pairs are those in the established reciprocal-family construction. Write

\[
 P=(1,1)\in E,\quad Q=(d,ds)\in E',\quad R=(2,2s)\in E,
\]

\[
 \ell=L(P),\quad h=\lambda(P),\quad \alpha=h/\ell^2,
 \quad m=L'(Q),\quad r=L(R).
\]

Here λ(P) is the global height because all away-from-p contributions at P vanish. The second global coefficient is α'=2α. Let ζ and ζ' denote the odd normalized primitives for the chosen complements. Define

\[
 K=\lambda'(Q)-\log_p d-2\alpha m^2,
\]

\[
 D=-4\left(\zeta(R)/s+1+\alpha r/s\right),\qquad
 C=2p\alpha/d. \tag{1}
\]

Suppose:

1. The entire rational reduction consists of the four endpoint disks and the four disks above x=±1.
2. \(v_p(\ell)=v_p(h)=1\), and \(\zeta(P),\zeta'(Q)\in\mathbf Z_p\).
3. \(v_p(m)\ge2\), \(v_p(r)\ge2\), and \(\zeta(R)/s+1\in p\mathbf Z_p\).
4. \(K\in p\mathbf Z_p\), and the two polynomials
   \[
   F(T)=T(\overline{D/p}-\overline C T^2),\qquad
   G(T)=\overline{K/p}+\overline C T^2 \tag{2}
   \]
   have no common zero in \(\mathbf F_p\).

The bars mean reduction modulo p. The assumptions make all quantities in (2) integral, and C is a unit.

**Proposition.** Under these hypotheses, the intersection of the two height-zero sets is precisely the four rational endpoints.

**Proof at the endpoints.** The formal coefficients need not individually be integral. The double-integration bound gives B(t)/t² ∈ Z_p for t∈pZ_p; the corresponding single- and nested-integral bounds give the same evaluated estimate for the finite-point and logarithmic-unit terms.

 Since \(v_p(\alpha)=-1\), while the primitive at P is integral and the regularized local-height variation divided by the squared disk coordinate is integral after evaluation on the whole residue disk, the same all-orders endpoint calculation as in the prime-3 argument gives

\[
 \rho(x)/(\alpha x^2)\in1+p\mathbf Z_p
 \qquad(0\ne x\in p\mathbf Z_p).
\]

The only zero in each endpoint disk is its center. Reciprocal symmetry handles infinity.

**Proof on the other disks.** Use

\[
 u=(x+1)/(x-1),\quad
 v=4y/(x-1)^3,
\]

and, on a u=0 disk, choose

\[
 v(u)=s\sqrt{1+bu^2+bu^4+u^6},\qquad b=(15-a)/(a+1).
\]

The opposite branch gives the same heights. Put

\[
 J(u)=\int_0^u dt/v(t),\qquad I(u)=\int_0^u t\,dt/v(t).
\]

The first-model quotient logarithms are exactly

\[
 L(f_1)=-r-J-I,\qquad L(f_2)=r-J+I,
\]

because the original x and y are

\[
 x=-(1+u)/(1-u),\qquad y=-2v/(1-u)^3,
\]

and the pullback differentials are \(-(1+u)du/v\) and \(-(1-u)du/v\). Thus the quadratic correction in the first height is exactly

\[
 \alpha(L(f_2)^2-L(f_1)^2)=-4\alpha J(r+I). \tag{3}
\]

The remaining local-height/logarithm expression is odd in u. Its derivative at zero is

\[
 -4(\zeta(R)/s+1).
\]

All its higher terms, evaluated at u in \(p\mathbf Z_p\), contribute in \(p^3\mathbf Z_p\): its oddness removes the quadratic term, and its differential primitives have integral numerators with only single- or double-integration denominators. Explicitly, the n-th coefficient valuation is bounded below by

\[
 -v_p(n)-\lfloor\log_p(n-1)\rfloor
\]

for the double-integral part, and by −v_p(n) for single integrals. For every n≥3 and p≥5, the resulting evaluated valuation is at least three, and tends to infinity. Its primitive constant is integral by assumption. This is a bound for the whole series.

The same denominator estimates give

\[
 J=u/s+O(p^3),\qquad I=u^2/(2s)+O(p^4)
\]

uniformly for u in \(p\mathbf Z_p\). Since r has valuation at least two, equation (3), combined with the linear local-height term, gives

\[
 \rho(u)=D u-(2\alpha/d)u^3+O(p^3).
\]

Here D is divisible by p. For u=pT this is the uniform congruence

\[
 \boxed{\rho(pT)/p^2\equiv T(D/p-CT^2)\pmod p.} \tag{4}
\]

For the second height, the finite-point local-height variation is in \(u^2\mathbf Z_p\), as is the variation of the singular regularized height, whose constant is −log_p d. The second logarithms are m+I and −J. Since m has valuation at least two and α has valuation −1, the terms involving 2mI and I² lie in \(p^3\mathbf Z_p\). The only contribution modulo p² besides the constant K is \(2\alpha J^2\equiv(2\alpha/d)u^2\). Hence

\[
 \boxed{\rho^*(pT)/p\equiv K/p+CT^2\pmod p.} \tag{5}
\]

The absence of a common residue zero in (2) excludes every point in these disks. The reciprocal involution on the u-model carries its zero and infinity disks to one another; it negates ρ* and preserves ρ, so all four disks are covered. The four rational endpoints themselves pass both heights. ∎

A convenient sufficient finite condition in item 4 is

\[
 \overline{K/p}\ne0,\qquad
 \overline{D/p}+\overline{K/p}\ne0. \tag{6}
\]

Indeed \(F+TG=(\overline{D/p}+\overline{K/p})T\). This criterion works even if G alone has residue roots. More precisely, if K/p is nonzero, common roots exist exactly when D/p+K/p is zero and −(K/p)/C is a square modulo p.

## 2. Explicit application: a=−157469 and p=11

Set

\[
 a=-157469,\quad A=-157472,\quad d=-78734.
\]

These curves have good reduction at 11, and d≡4 modulo 11. Their rational reduction consists precisely of

\[
 (0,\pm1),(1,\pm4),(-1,\pm4),\infty_+,\infty_-.
\]

Thus hypothesis 1 holds. The following constants are certified exactly:

\[
 \ell/11\equiv1,\quad h/11\equiv8,\quad
 11\alpha\equiv8,\quad \zeta(P)\equiv1\pmod{11}; \tag{7}
\]

\[
 v_{11}(m)=2,\quad \lambda'(Q)/11\equiv5,\quad
 \zeta'(Q)/s\equiv10,\quad \log_{11}d/11\equiv10\pmod{11}; \tag{8}
\]

\[
 v_{11}(r)=2,\quad r/(121s)\equiv4\pmod{11},\qquad
 \zeta(R)/s\equiv109\pmod{121}. \tag{9}
\]

It follows that

\[
 K/11\equiv6,\qquad C\equiv4,\qquad D/11\equiv8\pmod{11}.
\]

For D, the two contributions after division by 11 are

\[
 (\zeta(R)/s+1)/11\equiv10,\qquad
 \alpha r/(11s)\equiv(11\alpha)\,r/(121s)\equiv8\cdot4.
\]

Thus D/11≡−4(10+8·4)≡8. The criterion gives the exact pair

\[
 F(T)=T(8-4T^2),\qquad G(T)=6+4T^2
 \quad\text{over }\mathbf F_{11}. \tag{10}
\]

These have no common zero, since F+TG=3T and G(0)=6. Notice that G by itself has the two residue zeros T=±2: the second-height no-root method used at 3 would fail here. The first height removes precisely the possible residue locations left by the second. This is a genuine simultaneous two-polynomial certificate.

The proposition therefore proves

\[
 \{z\in C_{-157469}(\mathbf Q_{11}):\rho(z)=\rho^*(z)=0\}
  =\{(0,\pm1),\infty_+,\infty_-\}. \tag{11}
\]

### Sharper first-height classification at this prime

In this explicit case the first height already has exactly eight zeros: the four rational endpoints and the four centers x=±1, y=±2s. To check all smaller subdisks, use the factorized version of the uniform expansion rather than only (4). The same coefficient bounds show

\[
 \frac{\rho(u)}{u}
   =D-\frac{2\alpha}{d}u^2
     +u^2\mathbf Z_{11}
     +\alpha u^4\mathbf Z_{11}
     +\alpha r u^2\mathbf Z_{11}.
\]

This notation asserts membership for every nonzero u in 11 Z_11, with the quotient extending analytically at zero. Division by 11 therefore gives, uniformly,

\[
 \frac{\rho(u)}{11u}
       \equiv8-4(u/11)^2\pmod{11}.
\]

The residue 2 is not a square in F_11, so the right side is always nonzero. Thus u=0 is the unique first-height zero in either u=0 disk; reciprocal symmetry gives the two infinity centers. Their second-height values are ±K with v_11(K)=1, so the second height removes precisely these four additional zeros. This sharper statement is compatible with, and independently strengthens, the simultaneous-polynomial certificate (10).

## 3. Reproducibility of the constant certificate

No unit-root calculation or numerical p-adic height library is used. For an integral model \(Y^2=g(X)=X^3+A_2X^2+A_4X\), define

\[
 H_4=X^6+2A_2X^5+5A_4X^4-5A_4^2X^2
                  -2A_2A_4^2X-A_4^3,
\]

\[
 \psi_3=3X^4+4A_2X^3+6A_4X^2-A_4^2,
 \qquad \psi_5=32g^2H_4-\psi_3^3.
\]

The derivative of ψ_5 is obtained by ordinary polynomial differentiation. All group operations are exact rational operations in coordinates (X,Ybar) with Y=sYbar, s²=d.

For any such point T whose 5-multiple is formal, write \(t(5T)=s\tau\). The multiplication identities give

\[
 L(T)=L(5T)/5,
\]

\[
 \lambda(T)=\frac{2}{25}
       \left(\log_p\frac{\psi_5(T)}{t(5T)}-B(t(5T))\right),
\]

\[
 \zeta(T)/s=
 \frac{1}{5d\tau}-\frac{2\overline Y\,\psi_5'(X)}{25\psi_5(X)}
       +O(p^{v_p(\tau)}). \tag{12}
\]

For P use d=1. For Q use E' and d=−78734. The rational units

\[
 V_T=\frac{\psi_5(T)^2}{d\tau^2}
\]

are the squares of the units inside the logarithms. Exact computation gives

\[
 V_P\equiv23,\qquad V_Q\equiv45\pmod{121}.
\]

For a unit V,

\[
 \log_{11}V/11\equiv\frac{V^{10}-1}{110}\pmod{11}.
\]

The formal B-term has valuation at least two, so it contributes nothing to λ(T)/11 modulo 11. This proves the height residues in (7)–(8). The formal logarithm remainder is at least cubic; the primitive remainder in (12) has valuation at least v_p(τ). These bounds follow from the integral differential expansions and their exact integration denominators.

To obtain (9), calculate 2R and then 5(2R)=10R, whose formal parameter is \(s\tau_R\) with valuation two. Twice applying the derivative multiplication identity gives

\[
 \zeta(R)/s\equiv
 \frac1{10d\tau_R}
 -\frac{(D\log\psi_5)(2R)/s}{50}
 -\frac{(D\log\psi_2)(R)/s}{4}
 \pmod{121}. \tag{13}
\]

The rational right side reduces to 109. Also \(L(R)/(121s)\equiv\tau_R/(10\cdot121)\equiv4\pmod{11}\). The first omitted formal primitive term in (13) has valuation two, so reduction modulo 121 is rigorously justified. The supplied script evaluates all these exact rational expressions, checks the required valuations, enumerates all eight rational residue disks, and verifies the two finite-field polynomials have no common root.

## 4. Full restricted depth-two consequence

The existing exact descent certificate establishes rank E_a(Q)=1 for a=−157469. Also

\[
 a\equiv3\pmod8,\qquad a+1=-4\cdot39367,
\]

where 39367 is prime. The established local-target theorem therefore makes both actual away-from-11 targets exactly {0}. The endpoint-basepoint bridge and both actual-target containments put the full restricted depth-two set inside (11). Rational Kummer classes give the reverse inclusion. Thus

\[
 \boxed{C_{-157469}(\mathbf Q_{11})_2=C_{-157469}(\mathbf Q)
       =\{(0,\pm1),\infty_+,\infty_-\}.}
\]

This proves equality at a second prime for the new parameter, in addition to its existing prime-3 equality. It is not a claim about the unrestricted abelian Bloch–Kato convention or about all good primes.
