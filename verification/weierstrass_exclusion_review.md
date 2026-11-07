# Independent audit: infinite non-CM Weierstrass exclusions

The following steps were independently verified before publication:

1. Clearing rational denominators by y'=Dy gives the integral sextic (D²,MD,MD,D²). Common elliptic model scaling cancels in the height difference; compatible differential scaling preserves the quadratic correction. The existing endpoint-basepoint bridge therefore supplies the full-depth-two necessary condition. The true global height, not its p-local term alone, is retained.
2. Prime logarithms are Q-linearly independent by the logarithmic kernel and unique factorization. No Q_p-linear independence claim is made.
3. The precise denominator zero-attainment test includes the q=3, even multiplicity, square-unit exception.
4. At (±i,0) and all four x=±1 points the first scalar is zero, so a local target omitting zero excludes them from the full restricted depth-two set.
5. For nonintegral a in (-1,3), the quartic roots squared have complex absolute value one. Clearing a candidate logarithmic equality forces a root of unity; its rational trace would make a integral. Thus the four quartic Weierstrass points cannot pass.
6. Zywina v1 Theorem 1.5 allows source twist -1. Lemma 3.8 makes q2 inert in Q(i), and the distinct prime-ideal condition gives v_q2(a)=-1. Thus it supplies the required obstruction for infinitely many geometric curve classes.
7. v_q2(j(E))=-2 proves geometric non-CM directly, since CM j-invariants are integral.

The theorem retains the explicit eligible-prime condition p not dividing D(M-3D)(M+D). It does not rely on an unreviewed assertion about all alternative minimal good-reduction models.

Executed check_weierstrass_exclusion.py:
    PASS: 972 exact denominator zero-attainment cases.
    PASS: distinguished denominator and nonintegral j identities.
    PASS: examples 13/7 (odd multiplicity) and 19/9 (q=3 exception).

These checks do not certify ranks of the two illustrative parameters. Infinitude and rank use Zywina's theorem. The result excludes a ten-point geometric packet when locally visible; it neither classifies all non-Weierstrass points nor evaluates the residual Sym² discrepancy.
