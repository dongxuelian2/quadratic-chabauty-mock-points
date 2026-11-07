# An exact certificate at the remaining prime 3

This note closes the prime-3 boundary for the four points with x = ±1 in the Mordell–Weil-restricted depth-two argument. It uses the height normalization and the second-model containment already established in `../PROOF.md`. The proof and its all-orders bounds have received independent review.

## Proposition

Let

\[
 E:Y^2=X^3-8X^2+8X,\qquad P=(1,1),\qquad
 \omega=\frac{dX}{2Y}.
\]

Use the cyclotomic logarithm with \(\log_3(3)=0\), the unit-root splitting, and the normalized local height
\(\lambda_3=-2\log_3(t)+O(t)\), where \(t=-X/Y\).
Then

\[
 \boxed{h_3(P)\in 2+3\mathbf Z_3.} \tag{1}
\]

In particular \(h_3(P)\ne0\). This is a finite-precision certificate with a proven error bound, not an inference from an unbounded numerical approximation.

## 1. Determine the splitting algebraically

Choose \(s\in\mathbf Q_3\) with \(s^2=-2\), which exists by Hensel's lemma. The CM endomorphism already used in the main proof is

\[
 \eta(X,Y)=\left(-\frac{X-8+8/X}{2},
                  -\frac{Y(1-8/X^2)}{2s}\right),
 \qquad \eta^*\omega=s\omega.
\]

Put \(\nu=X\omega\). Direct differentiation on the curve gives

\[
 d(Y/X)=(X-8/X)\omega.
\]

Consequently

\[
 \eta^*\nu=-\frac{s}{2}(X-8+8/X)\omega
          =-s\nu+4s\omega+\frac{s}{2}d(Y/X),
\]

so the complementary CM eigenspace in de Rham cohomology is

\[
 W=\mathbf Q_3[(X-2)\omega]. \tag{2}
\]

The curve has good ordinary reduction at 3: its discriminant is \(2^{15}\), and \(\#E(\mathbf F_3)=6\), so \(a_3=-2\). CM commutes with crystalline Frobenius, so the two CM eigenlines are Frobenius-stable. The Hodge line cannot be the slope-zero line: as a Frobenius-stable subobject its Hodge number is 1, and Newton number 0 would contradict weak admissibility. It is therefore the slope-one line, and the complementary CM eigenline (2) is the unit-root space. Equivalently, the Frobenius roots are \(-1\pm s\), of valuations 0 and 1. Thus (2) is exactly the splitting used in the endpoint-height calculation, not an arbitrary convenient height.

## 2. A directly convergent local-height expansion

Balakrishnan–Besser, Theorem 4.1, describes the local height as a normalized double Coleman integral for any isotropic complement. In the present normalization, the dual second-kind differential is \(-(X-2)\omega\), its leading term being \(-t^{-2}dt\). That theorem applies at 3 and does not assume \(p>3\).

Write

\[
 X(t)=t^{-2}U(t^2),\qquad \omega=w(t)dt,
 \qquad U\in1+t^2\mathbf Z_3[[t^2]],\quad
 w\in1+t^2\mathbf Z_3[[t^2]].
\]

For precision, with \(T=t^2\), the series \(U=U(T)\in1+T\mathbf Z[[T]]\) is the unique formal solution with constant coefficient 1 to

\[
 U^2-(1+8T)U+8T^2=0,
 \qquad w(t)=1-T\frac{U'(T)}{U(T)}. \tag{3}
\]

The assertion needed here is simply \(U\in1+T\mathbf Z[[T]]\); it follows coefficient by coefficient from (3), since its derivative with respect to \(U\) has constant coefficient 1. All coefficients of \(w\) are also integers. In particular,

\[
 X=t^{-2}+8-8t^2+64t^4+\cdots,
 \qquad w=1-8t^2+80t^4+\cdots.
\]

Define odd and even formal series, respectively, by

\[
 Z(t)=\int -(X(t)-2)w(t)dt=\frac1t+2t-8t^3+\cdots,
\]

\[
 B(t)=\int\left(w(t)Z(t)-\frac1t\right)dt
     =-3t^2+14t^4-\frac{512}{5}t^6+\frac{31624}{35}t^8+\cdots. \tag{4}
\]

Both integration constants are zero. The local-height formula and symmetry give

\[
 \lambda_3(t)=-2\log_3(t)-2B(t). \tag{5}
\]

One may regard \(\log_3(t)+B(t)\) as \(\log_3\sigma_3(t)\), but neither existence of an integral sigma series at 3 nor a software implementation of it is needed: (5) follows directly from the double-integral theorem and the convergent series below.

### Proven tail bound

Write

\[
 -(X-2)w=-t^{-2}+\sum_{j\ge0}a_{2j}t^{2j},
 \qquad w=\sum_{j\ge0}w_{2j}t^{2j},
\]

with all \(a_{2j},w_{2j}\in\mathbf Z_3\). If \(B=\sum_{k\ge1}b_{2k}t^{2k}\), then

\[
 b_{2k}=\frac1{2k}\left(w_{2k}+
       \sum_{j=0}^{k-1}\frac{a_{2j}w_{2(k-j-1)}}{2j+1}\right).
\]

It follows for every \(k\ge1\) that

\[
 v_3(b_{2k})\ge-v_3(2k)-\lfloor\log_3(2k-1)\rfloor. \tag{6}
\]

Thus the series converges whenever \(v_3(t)>0\). At \(v_3(t)=2\),

\[
 v_3(b_{2k}t^{2k})\ge
 4k-v_3(2k)-\lfloor\log_3(2k-1)\rfloor.
\]

The right side is at least 7 for every \(k\ge2\): it is 7 at \(k=2\), and for \(k\ge3\) the inequalities
\(v_3(2k)\le k-1\) and \(\lfloor\log_3(2k-1)\rfloor\le k-1\) give the stronger lower bound \(2k+2\ge8\).
Since \(b_2=-3\), this proves

\[
 B(t)=-3t^2+O(3^7)\in3^5\mathbf Z_3
 \quad\text{whenever }v_3(t)=2. \tag{7}
\]

The notation \(O(3^7)\) here means an actual element of \(3^7\mathbf Z_3\), justified for the entire infinite tail by (6).

## 3. Exact rational multiplication and the logarithm certificate

The chord-and-tangent law gives

\[
 3P=Q=\left(\frac{289}{2025},\frac{90287}{91125}\right),
 \qquad t(Q)=-\frac{765}{5311},\qquad v_3(t(Q))=2. \tag{8}
\]

The third division polynomial is

\[
 \psi_3(X)=3X^4-32X^3+48X^2-64,
 \qquad\psi_3(P)=-45.
\]

The normalized local-height multiplication identity is

\[
 \lambda_3(3P)=9\lambda_3(P)-2\log_3(\psi_3(P)).
\]

As established for this model in the main proof, \(P\) is integral and nonsingular at every finite prime and has zero non-3 local heights. Hence \(h_3(P)=\lambda_3(P)\). Substituting (5) and (8), and using \(765=45\cdot17\), gives the exact identity

\[
 9h_3(P)=2\log_3(5311/17)-2B(-765/5311). \tag{9}
\]

Now \(\log_3(-1)=0\), and

\[
 -\frac{5311}{17}=1+\delta,\qquad
 \delta=-\frac{5328}{17}=-9\frac{592}{17},\qquad v_3(\delta)=2.
\]

For every \(n\ge2\),
\(v_3(\delta^n/n)=2n-v_3(n)\ge4\). Therefore the entire logarithm tail has valuation at least 4, giving

\[
 \log_3(5311/17)=\delta+O(3^4),
 \qquad
 \frac{\log_3(5311/17)}9\equiv-\frac{592}{17}\equiv1\pmod3. \tag{10}
\]

Equation (7) says \(B(t(Q))/9\in3^3\mathbf Z_3\). Combining (9) and (10) proves (1).

## 4. Consequence for the four points

The existing second-model calculation, valid at every odd split prime, gives

\[
 \rho_3^*((-1,\pm2\sqrt{-2})^*)=2h_3(P),\qquad
 \rho_3^*((1,\pm2\sqrt{-2})^*)=-2h_3(P).
\]

The actual away-from-3 target is \(\{0\}\), and the nonmonic actual-target containment is valid at 3. Equation (1) makes all four endpoint values nonzero, indeed 3-adic units. Hence all four points are excluded from the full Mordell–Weil-restricted depth-two set at \(p=3\).

Together with the existing \(p\ge5\) proof, the four-point exclusion now holds at every odd prime where the points are locally visible. Together with the eight-point and anti-CM two-point exclusions already proved, all fourteen specified nonrational first-height candidates are excluded at every odd prime where locally visible. No classification of other depth-two points follows from this conclusion.

## Sources and reproducibility

- J. S. Balakrishnan and A. Besser, *Coleman–Gross height pairings and the p-adic sigma function*, Theorem 4.1 and Corollary 4.2, give the normalized local double integral and its sigma interpretation. Theorem 4.1 is the result used above. https://arxiv.org/html/1201.6016#S4
- The local-height division-polynomial identity is the same standard multiplication identity already used in Sections 2 and 6 of the main manuscript.
- `../scripts/check_prime3_height.py` verifies the rational group law, division polynomial, formal coefficients, coefficient bounds, and the residue certificate using only Python's exact rational arithmetic. The proof of the infinite-tail estimate is (6), not a finite test in the script.

