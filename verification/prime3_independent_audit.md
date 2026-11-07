# Independent audit of the prime-3 height certificate and disk isolation

Reviewed on 2026-11-07. Scope: `../proofs/prime3_height_certificate.md`, `../proofs/prime3_disk_isolation.md`, and `../scripts/check_prime3_height.py`, with the definitions and second-model identities in `../PROOF.md`.

Publication note: this analytic audit preceded the separate [endpoint-bridge audit](endpoint_basepoint_independent_audit.md), which subsequently passed. Its requested explanatory improvements have been incorporated. The conditional language below records the dependency at that review stage; the combined result is now proved.

## Verdict

**The arithmetic certificate and the uniform two-height intersection proof pass this audit.** In the stated normalization, the conclusions are

\[
h_3((1,1))\equiv2\pmod3,
\qquad
\{\rho_3=0\}\cap\{\rho_3^*=0\}
=\{(0,\pm1),\infty_\pm\}.
\]

No false coefficient, sign, valuation estimate, missing residue disk, or target correction was found. The infinite-tail arguments are genuine coefficient bounds, not extrapolations from the executable checks. The executable checks pass.

This verdict does **not** independently establish the endpoint-basepoint bridge for the full depth-two set. That bridge is a separate premise; the disk note correctly preserves its conditional status. The four-point exclusion using the second model does not need that bridge.

Subsequent review: the separate bridge was completed and passed the audit recorded in `../verification/endpoint_basepoint_independent_audit.md`. The full restricted depth-two conclusion is now supported by that additional argument, not by the analytic estimates alone.

## 1. Height normalization and the CM complement

The identity

\[
d(Y/X)=(X-8/X)\omega
\]

is correct. Thus the displayed CM action sends \([X\omega]\) to \(-s[X\omega]+4s[\omega]\), and \([(X-2)\omega]\) has eigenvalue \(-s\). It complements the holomorphic eigenline, whose eigenvalue is \(s\).

The identification with the unit-root line is correct, though one extra explanatory sentence would improve the certificate. CM commutes with crystalline Frobenius. For good ordinary split CM reduction, the two one-dimensional CM eigenspaces are Frobenius stable. The holomorphic line cannot be the slope-zero line: as a filtered Frobenius-stable subobject that would violate weak admissibility. It is the slope-one line, and its complementary CM line is therefore slope zero. Equivalently, the Frobenius eigenvalues are \(-1\pm s\), one of valuation one and one of valuation zero, since their product is 3.

The elliptic discriminant is \(32768=2^{15}\), and direct point counting gives six points over \(\mathbf F_3\). There is no exceptional reduction issue at 3.

I checked Balakrishnan–Besser, Theorem 4.1 and the discussion immediately following it: the normalized self-height is the symmetric double integral with inner differential representing the cup-product dual of \(\omega\). Its leading term is \(-t^{-2}dt\). Therefore the choice \(-(X-2)\omega\), the factor \(-2\), and the zero constant terms used in the certificate agree with that normalization. The theorem used here does not impose \(p>3\). No integral sigma-function theorem at 3 is required.

Source: <https://arxiv.org/html/1201.6016#S4>.

## 2. Formal series and all tails

Substitution of \(Y=-X/t\) in the curve equation gives exactly

\[
U^2-(1+8T)U+8T^2=0,
\qquad w=1-TU'/U.
\]

Its formal implicit derivative at \((U,T)=(1,0)\) is one, so the integral coefficient claim is justified. I independently obtained the coefficients of the inner differential and of \(B\), including

\[
B=-3t^2+14t^4-\frac{512}{5}t^6+\frac{31624}{35}t^8+\cdots.
\]

The denominator bound on \(b_{2k}\) accounts for both integrations: the outer denominator is \(2k\), and the inner denominators are the odd integers at most \(2k-1\). Their maximum possible 3-adic valuation is bounded by \(\lfloor\log_3(2k-1)\rfloor\). The nonarchimedean triangle inequality therefore proves the stated bound on every coefficient.

At \(v_3(t)=2\), the quadratic term has valuation five and every subsequent term has valuation at least seven. At \(v_3(t)\ge1\), division by \(t^2\) leaves all terms in \(3\mathbf Z_3\). The elementary bounds used for the first few indices are valid, and the general bounds tend to infinity. Hence the conclusions concern the entire convergent series.

For the second elliptic model I independently repeated the formal calculation. With its coefficients \(A=16,B=32\), the equation is \(U^2-(1-16T)U+32T^2=0\), and the second-kind differential is \(-(X+4)\omega'\). The resulting series begins

\[
B_{E'}=6t^2+56t^4+\frac{4096}{5}t^6
+\frac{505984}{35}t^8+\cdots.
\]

In particular the crucial quadratic coefficient 6, which the submitted script does not separately compute, is correct. The same all-orders denominator argument applies.

The bounds for the regular single and nested integrals also pass. In the nested case the denominator of an individual summand is \((2n)(2j+2)\) with \(2j+2\le2n-2\), which gives the claimed coefficient bound. After dividing by \(z^2\), its value is in \(9\mathbf Z_3\), uniformly for every \(z\in3\mathbf Z_3\). The logarithm-of-an-even-unit bound follows termwise from \(\log(1+z^2r)\); division by \(z^2\) introduces no nonintegral values on this disk.

## 3. Exact height, logarithm, and primitive constants

The group law and division polynomial calculations are correct:

\[
3P=(289/2025,90287/91125),\quad t(3P)=-765/5311,
\quad \psi_3(P)=-45.
\]

The multiplication identity consequently gives

\[
9h=2\log_3(5311/17)-2B(-765/5311).
\]

The sign is correct. Replacing \(5311/17\) by its negative does not change its logarithm, and the resulting increment is \(-9\cdot592/17\). The full logarithm tail has valuation at least four. The logarithm contribution divided by nine is 1 modulo 3, whereas the \(B/9\) contribution is divisible by 27. This proves \(h\equiv2\pmod3\) exactly.

As a separate computational cross-check, I used \(6P=2(3P)=3(2P)\) and the composite multiplication identity

\[
36h=2\log_3\!\left(2^9\psi_3(2P)/t(6P)\right)-2B(t(6P)).
\]

It again gives 2 modulo 3, and gives the same residue 6935 modulo \(3^{10}\) as the submitted calculation. This corroboration is not needed for the all-orders proof.

Differentiating the multiplication identity yields the stated minus sign in

\[
\zeta(P)=\zeta(3P)/3-(D\log\psi_3)(P)/9.
\]

I independently evaluated \((D\log\psi_3)(P)=-8/15\). The principal terms combine to \(-115/51\); the remaining inner-integral terms are in \(3\mathbf Z_3\). Hence \(v_3(\zeta(P))=-1\) and \(3\zeta(P)\equiv1\pmod3\). The logarithm estimate similarly gives \(v_3(\ell)=1\) and \(\ell/3\equiv2\pmod3\).

## 4. Uniform disk argument

The first finite-point map pulls back both differentials to \(x\) times an even integral series. Its local height variation divided by \(x^2\) is therefore in \(3^{-1}\mathbf Z_3\). All nonleading terms in \(\rho/x^2\), including the logarithmic singularity cancellation, have this same lower bound or a stronger one. The surviving term \(\alpha(J/x)^2\) has valuation \(-2\) and is \(\alpha\) times a unit congruent to one. It cannot cancel. This proves isolation throughout both disks above \(x=0\), not merely near their centers. Reciprocity handles the two infinity disks.

The second-model differential scaling is \(\psi^*\omega'=\omega/s\), the height shift is \(\log_3(2)\), and the primitive scaling is \(s\). These give \(\alpha'=2h/\ell^2\), not \(-2h/\ell^2\). The minus sign instead comes from \(s^{-2}=-1/2\). Consequently the second-disk reduction is exactly

\[
\rho^*(u)\equiv h\left(2-(u/\ell)^2\right)\pmod3.
\]

Every omitted finite-height variation, cross term, and regularized singular term is in \(3\mathbf Z_3\), including when \(v_3(u)=1\). Since the only squares in \(\mathbf F_3\) are 0 and 1, the reduction never vanishes. This excludes the whole two disks above \(u=0\), and reciprocity excludes the two above infinity.

For completeness, inclusion of the four rational endpoints in the intersection can be seen directly, without invoking any depth-two bridge: \(\rho\) vanishes at the original endpoints; their second coordinates have \(u=\pm1\), where the two elliptic images agree or differ by negation, so every term of \(\rho^*\) cancels.

## 5. Targets and complete coverage

The first actual target is zero. At 2 a unit \(x\) gives the nonsquare residue 8 modulo 16. When \(v_2(x)>0\), the first elliptic image is integral and smooth, and the second image's formal-group contribution cancels the explicit local logarithm. Reciprocity covers negative valuation and continuous extension covers endpoints. At every other away-from-3 prime both quotients have good reduction, and the same integral/nonintegral argument applies.

The second target calculation in Proposition 16 is consistent with the model change: the two displayed-model height corrections at 2 are equal and cancel. There is no uncancelled \(\log_3(2)\) contribution to either target.

Modulo 3, the polynomial is \(x^6+x^4+x^2+1\), whose gcd with its derivative \(x^3-x\) is one. It has two points over each of \(x=0,1,-1\), and two smooth infinity points. Thus there are exactly eight rational residue disks, and the good proper model ensures they exhaust \(C(\mathbf Q_3)\). The second change of coordinate has unit determinant at 3, maps the \(x=-1\) disks to \(u=0\), and maps the \(x=1\) disks to \(u=\infty\). No disks are omitted or counted incorrectly.

## Publication boundary

No original proof or repository was changed in this audit. The natural improvements are explanatory rather than corrective: expand the CM/unit-root sentence, include the second-model quadratic coefficient in the reproducibility script, and explicitly note the direct cancellation at \(u=\pm1\). The full depth-two classification should remain conditional until the separately proposed endpoint-basepoint mixed-extension comparison is verified.
