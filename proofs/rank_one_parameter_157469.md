# A second exact rank-one parameter in the analytic neighborhood

Status: independently reviewed exact rank certificate. This note proves the rank condition for a new parameter and applies the separately established exact local-target theorem. The certificate and complete finite obstruction list are supplied for review.

## Parameter and result

Take

\[
 a=-157469=-5-27\cdot(8\cdot3^6).
\]

Then

\[
 A=a-3=-157472=-32\cdot7\cdot19\cdot37,
 \qquad a+1=-157468=-4\cdot39367,
\]

where 39367 is prime. The two elliptic quotients are

\[
 E:Y^2=X^3+AX^2-AX,
 \qquad E':Y^2=X^3-2AX^2+A(A+4)X.
\]

**Proposition.** Both E and E′ have rational rank one. The analytic certificate (H) of `../proofs/general_prime3_criterion.md` holds. Every odd-prime exponent in a+1 is prime to 3, in fact the only one is 1.

## Exact rank upper bound by two-isogeny descent

For an elliptic curve

\[
 F_{A,B}:Y^2=X^3+AX^2+BX
\]

with the rational two-torsion point T=(0,0), define the standard descent map

\[
 \delta(O)=1,\quad\delta(T)=B,
 \quad\delta((X,Y))=X\quad\text{in }\mathbf Q^\times/\mathbf Q^{\times2}.
\]

For its two-isogenous curve \(F'_{A,B}:Y^2=X^3-2AX^2+(A^2-4B)X\), use the corresponding map δ′. The usual elementary two-isogeny descent identity is

\[
 2^{\operatorname{rank} F_{A,B}(\mathbf Q)}
   =\frac{|\delta(F_{A,B}(\mathbf Q))|\,
           |\delta'(F'_{A,B}(\mathbf Q))|}{4}. \tag{1}
\]

This is the standard descent via the isogeny with kernel {O,T}; its kernels are the images of the dual isogenies, whose composites are multiplication by 2. Only an upper bound on the two descent images is needed here.

Every image class has a squarefree integer representative d dividing B, with either sign. Indeed, if q does not divide B, the equation forces v_q(X) to be even: if it is positive, the lowest-valuation term on the right is BX; if negative, it is X³. In either case an odd valuation contradicts that Y² is a square. Write X=d(U/V)² with coprime integers U,V. Substitution gives the homogeneous quartic

\[
 N^2=dU^4+AU^2V^2+(B/d)V^4. \tag{2}
\]

Its rational N is automatically integral because its square is integral. The special classes 1 and B are included in the same squarefree candidate list.

For any prime q and modulus q^k, a rational solution of (2) produces a primitive local pair (U,V), since U,V are coprime. If V is a unit, scale to V=1. Otherwise U is a unit and scale to U=1 with q dividing V. Thus it is enough to test both finite lists

\[
 d t^4+A t^2+B/d \pmod{q^k}\quad(t\in\mathbf Z/q^k),
\]

\[
 d+A t^2+(B/d)t^4 \pmod{q^k}\quad(t\in q\mathbf Z/q^k)
\]

for membership in the complete set of squares modulo q^k. If both lists avoid squares, the candidate d is impossible. The procedure uses only necessary local conditions, so there is no claim that a surviving quartic has a rational point.

The exact script `../scripts/check_rank_one_parameter.py` enumerates every squarefree signed divisor, tests the real place and the finite moduli \(2^8,7^2,19^2,37^2\), and records an obstruction for every discarded class. Its successive survivor counts are

- For E: 16 after the real test, then 8, 4, 2, 2.
- For E′: 64 after the real test, then 24, 12, 6, 4.

The final lists are

\[
 \delta(E(\mathbf Q))\subseteq\{1,9842\},
\]

\[
 \delta'(E'(\mathbf Q))
 \subseteq\{1,-39367,-9842,387450014\}.
\]

All numbers in the lists are squarefree; \(387450014=9842\cdot39367\). The factorization of the second B-coefficient is

\[
 A(A+4)=2^7\cdot7\cdot19\cdot37\cdot39367.
\]

The script gives the complete individual obstruction list in `../verification/rank_one_obstructions.txt`. There is no omitted local-solubility oracle or floating-point arithmetic. Formula (1) now gives \(2^{\operatorname{rank}E}\le(2\cdot4)/4=2\), so the rank is at most one.

## Rank lower bound and analytic constants

Since a ≡ −5 (mod 3^6), the quantitative analytic-neighborhood proposition applies. In particular \(v_3(L(P))=1\) for P=(1,1), so P is nontorsion and the rank is at least one. Alternatively the lower bound follows directly from the exact third multiple: \(v_3(t(3P))=2\), and the formal logarithm is t plus terms of strictly higher valuation on that disk, hence \(v_3(L(P))=2-1=1\).

Consequently \(\operatorname{rank}E(\mathbf Q)=1\), and isogeny invariance gives rank one for E′ as well. The exact-check script independently verifies the residue constants

\[
 \ell/3=h=9\alpha=2\pmod3,
 \qquad K=C=1\pmod3,
\]

and the valuations \(v_3(\zeta(P))=v_3(\zeta'(Q))=-1\), using rational arithmetic in coordinates \(Y=s\overline Y\), \(s^2=(a+1)/2\). The equality notation here means separate equalities of residues, not equalities of the numbers themselves.

## Unconditional depth-two consequence from the established local targets

This parameter has a ≡ −5 (mod 8) and the sole odd valuation v_39367(a+1)=1. The exact local-target theorem in `../proofs/reciprocal_local_targets.md` therefore gives both actual targets exactly {0}: the first target vanishes under the mod-8 congruence, while the second has no nonzero coefficient when its sole odd bad-prime multiplicity is 1. Its 2-contribution also vanishes.

All hypotheses of the arithmetic family theorem in `../proofs/general_prime3_criterion.md` are now verified. Consequently, for the Mordell–Weil-restricted, actual-local-image convention,

\[
 C_{-157469}(\mathbf Q_3)_2=C_{-157469}(\mathbf Q)
 =\{(0,1),(0,-1),\infty_+,\infty_-\}.
\]

This conclusion uses the established endpoint-basepoint bridge and the separately proved exact local targets, rather than assuming either target from the parameter's 3-adic proximity to −5. The newly supplied rank certificate is undergoing independent review; that review status is not an unproved arithmetic hypothesis. No assertion about infinitely many rank-one parameters follows, and nothing has been published.
