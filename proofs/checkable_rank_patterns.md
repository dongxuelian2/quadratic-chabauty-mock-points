# Two elementary, checkable rank-one families

Status: independently reviewed research proof, with an exact standalone verification script. No assertion of infinitely many parameters is made. The rank theorems below are unconditional for every parameter meeting their stated prime-factor conditions. The depth-two corollaries use the already established analytic, actual-local-target, and endpoint-basepoint results in the companion notes.

## 1. The curves and the descent identity

Write

\[
 E_A:y^2=x^3+Ax^2-Ax,\qquad
 E'_A:y^2=x^3-2Ax^2+A(A+4)x,
 \qquad a=A+3.
\]

The curves are nonsingular for \(A\ne0,-4\), and are two-isogenous. For
\(F:y^2=x^3+cx^2+bx\), the standard two-isogeny descent map is

\[
 \delta_F(O)=1,\quad \delta_F((0,0))=b,
 \quad\delta_F((x,y))=x
 \quad\text{in }\mathbf Q^\times/\mathbf Q^{\times2}.
\]

It is a group homomorphism. Its image is represented by squarefree signed divisors \(d\) of \(b\), and every image class has a solution of

\[
 N^2=dU^4+cU^2V^2+(b/d)V^4,\qquad
 U,V,N\in\mathbf Z,\quad\gcd(U,V)=1. \tag{1}
\]

Here and below the exceptional points \(O,(0,0)\) are included directly by the definition of the map. The support statement follows because, outside the prime divisors of \(b\), an odd valuation of \(x\) gives an odd valuation of the unique lowest-valuation term of the cubic. Substituting \(x=d(U/V)^2\) gives (1).

The elementary two-isogeny identity is

\[
 2^{\operatorname{rank}E_A(\mathbf Q)}
 =\frac{|\delta(E_A(\mathbf Q))|\,
         |\delta'(E'_A(\mathbf Q))|}{4}. \tag{2}
\]

In particular, these are actual descent images, not sets of merely locally soluble coverings. We only use local obstructions to give upper bounds, and explicit points to give the matching lower bounds.

Two useful rational points on the second curve exist for every \(A\):

\[
 R=(A,2A),\qquad S=(A+4,2(A+4)). \tag{3}
\]

Indeed, substitution gives \(4A^2\) and \(4(A+4)^2\), respectively. Thus the image of \(\delta'\) contains the classes \([A]\), \([A+4]\), and their product \([A(A+4)]\).

## 2. A linear prime-pattern theorem

**Theorem 1.** Let \(p\) and \(q=8p-1\) be primes, with

\[
 p\equiv3\text{ or }5\pmod8.
\]

Set \(A=-32p\), equivalently \(a=3-32p\). Then

\[
 \delta(E_A(\mathbf Q))=\{1,2p\},\qquad
 \delta'(E'_A(\mathbf Q))=\{1,-2p,-q,2pq\}, \tag{4}
\]

and both elliptic curves have rank exactly one.

### Proof for the first descent image

The coefficients of the first curve are \(c=-32p,b=32p\), so the signed squareclass candidates are \(\pm1,\pm2,\pm p,\pm2p\). Every negative candidate is impossible at the real place: all three coefficients of its quartic (1) are negative.

To exclude \(d=2\), suppose

\[
 N^2=2U^4-32pU^2V^2+16pV^4. \tag{5}
\]

If \(U\) is odd, its right side is \(2\pmod8\). Otherwise \(V\) is odd, and putting \(U=2u\) and dividing by 16 gives

\[
 (N/4)^2=2u^4-8pu^2V^2+pV^4
 \equiv p+2u^4\pmod8.
\]

Its possible residues are \(\{3,5\}\) when \(p\equiv3\pmod8\), and \(\{5,7\}\) when \(p\equiv5\pmod8\). None is a square modulo 8. Thus \(2\) is absent from the image.

The torsion point has image \([32p]=[2p]\). Since the image is a group, the presence of \(p\) would imply the presence of \(2\). Thus \(p\) is absent too, proving the first equality in (4).

### Proof for the second descent image

The second coefficients are

\[
 c'=64p,\qquad b'=128pq.
\]

Its torsion class is \([2pq]\). Multiplying any even squarefree candidate by this class produces an odd squarefree representative. Consequently it is enough to consider

\[
 d\in\{\pm1,\pm p,\pm q,\pm pq\}. \tag{6}
\]

We claim that a locally soluble quartic for an odd \(d\) in (6) necessarily satisfies

\[
 d\equiv1\pmod8. \tag{7}
\]

If \(U\) is odd this follows directly by reducing (1) modulo 8. If \(U\) is even, \(V\) is odd. If \(4\mid U\), the right side of (1) is \(128\pmod{256}\), not a square. In the remaining case put \(U=2u\) with \(u\) odd. Dividing by 16 gives

\[
 (N/4)^2=d u^4+16p u^2V^2+(8pq/d)V^4
 \equiv d\pmod8,
\]

which proves (7). This argument is a uniformly bounded obstruction, using no modulus beyond 256.

Now \(q\equiv7\pmod8\). If \(p\equiv3\) or \(5\pmod8\), the only members of (6) congruent to 1 modulo 8 are \(1\) and \(-q\). Restoring multiplication by the torsion class gives

\[
 \delta'(E'_A(\mathbf Q))\subseteq\{1,-q,2pq,-2p\}.
\]

Both nontrivial generators are realized by (3): \([A]=[-2p]\), \([A+4]=[-q]\). These generate four distinct squareclasses, proving the second equality in (4). Formula (2) gives \(2^{\operatorname{rank}}=2\). The isogenous curve has the same rank. ∎

**Prime-power extension.** The identical proof applies if

\[
 m=p^e,\quad e\text{ odd},\quad p\equiv3\text{ or }5\pmod8,
 \qquad 8m-1=q^f
\]

for primes \(p,q\), with \(A=-32m\). Necessarily \(f\) is odd and \(q\equiv7\pmod8\). The descent images are again (4), with \(p,q\) denoting the underlying primes. The first congruence proof uses \(m\equiv3\) or \(5\pmod8\); the second uses \(v_2(c')=6,v_2(b')=7\). The odd-support list is unchanged. This is not an assertion that infinitely many such prime powers exist.

## 3. A quadratic family with a composite-parameter criterion

The following result also supplies a genuine Legendre-symbol criterion on a composite parameter, not just a one-prime example.

**Theorem 2.** Let \(n>1\) be odd. Suppose:

1. Every prime divisor of \(n\) is congruent to 3 or 5 modulo 8, equivalently \((2/p)=-1\) at every \(p\mid n\).
2. Exactly one prime \(r\equiv3\pmod8\) has odd exponent in \(n\).
3. \(D=2n^2-1\) is prime.

Set \(A=-8n^2\), equivalently \(a=3-8n^2\). Then

\[
 \delta(E_A(\mathbf Q))=\{1,2\},\qquad
 \delta'(E'_A(\mathbf Q))=\{1,-2,-D,2D\}. \tag{8}
\]

Both elliptic curves have rank one. In particular the theorem applies whenever \(n\equiv3\pmod8\) and both \(n\) and \(2n^2-1\) are prime.

### A valuation lemma

At an odd prime \(p\mid n\), let \(e=v_p(n)\), \(m=n/p^e\). For a nonzero coordinate \(x\) on either curve, suppose \(j=v_p(x)\) is odd. A negative \(j\) is impossible because the cubic term uniquely has lowest valuation \(3j\). For positive \(j\), the three valuations are

\[
 3j,\qquad 2e+2j,\qquad 2e+j.
\]

If \(j<e\) the first is uniquely lowest and odd. If \(j>e\) the third is uniquely lowest and odd. Therefore \(j=e\), and in particular \(e\) is odd. Writing \(x=p^e u\), cancellation of the first and third terms further requires

\[
 u^2\equiv -8m^2\pmod p\quad\text{on }E_A,
 \qquad
 u^2\equiv32m^2\pmod p\quad\text{on }E'_A. \tag{9}
\]

For the second congruence use \(D\equiv-1\pmod p\). Thus a prime \(p\mid n\) can appear in a first descent squareclass only if \(e\) is odd and \((-2/p)=1\). It can appear in a second descent squareclass only if \(e\) is odd and \((2/p)=1\).

### First image

The coefficient \(b=8n^2\) is positive and \(c=-8n^2\) is negative, so all negative candidates are impossible at the real place. For \(p\equiv5\pmod8\), \((-2/p)=-1\); for \(p\equiv3\pmod8\), \((-2/p)=1\). The valuation lemma and assumptions leave only

\[
 \delta(E_A(\mathbf Q))\subseteq\{1,2,r,2r\}.
\]

The quartic for \(d=r\) is

\[
 N^2=rU^4-8n^2U^2V^2+(8n^2/r)V^4. \tag{10}
\]

If \(U\) is odd, its right side is \(r\pmod{16}\), whether \(V\) is even or odd. This is 3 or 11 modulo 16, neither a square. If \(U\) is even, \(V\) is odd and the right side is 8 modulo 16, again impossible. Thus \(r\) is absent. The torsion class \([8n^2]=2\) excludes \(2r\) by multiplication and proves the first equality in (8).

### Second image

Here \(c'=16n^2\) and \(b'=32n^2D\). Assumption 1 and (9) exclude every prime of \(n\) from the second image. Hence

\[
 \delta'(E'_A(\mathbf Q))\subseteq
 \{\pm1,\pm2,\pm D,\pm2D\}. \tag{11}
\]

The points (3) give the subgroup

\[
 H=\{1,-2,-D,2D\}.
\]

It remains to exclude the other coset \(-H\), for which it is enough to exclude \(-1\).

Let \(r\) be the distinguished prime from assumption 2 and \(e=v_r(n)\), which is odd. The \(d=-1\) quartic is

\[
 N^2=-U^4+16n^2U^2V^2-32n^2D V^4. \tag{12}
\]

If \(r\mid V\), then \(U\) is a unit and reduction modulo \(r\) forces \(-1\) to be a square, impossible for \(r\equiv3\pmod4\). Suppose \(V\) is a unit and put \(h=v_r(U)\), allowing \(h=+\infty\) if \(U=0\). Equality \(2h=e\) is impossible because \(e\) is odd.

- If \(2h<e\), the first term uniquely has lowest valuation \(4h\); after division by \(r^{4h}\) its unit squareclass is \(-1\), impossible.
- If \(2h>e\), the last term uniquely has lowest valuation \(2e\). Since \(D\equiv-1\pmod r\), its unit squareclass is \(32\), impossible because \((2/r)=-1\).

Thus \(-1\) is locally impossible. Because the actual descent image is a group containing \(H\), no element of \(-H\) can occur. This proves (8); (2) gives rank one. ∎

## 4. Consequences for the reciprocal genus-two family

Retain the actual-local-image, Mordell–Weil-restricted depth-two convention of `../proofs/general_prime3_criterion.md`. Let

\[
 C_a:y^2=x^6+ax^4+ax^2+1.
\]

**Corollary 1.** If the primes in Theorem 1 also satisfy

\[
 p\equiv547\pmod{729},
\]

then, for \(a=3-32p\),

\[
 C_a(\mathbf Q_3)_2=C_a(\mathbf Q)
 =\{(0,1),(0,-1),\infty_+,\infty_-\}. \tag{13}
\]

Indeed, \(4\cdot547\equiv1\pmod{729}\), so \(a+5=8(1-4p)\) is divisible by \(5832=8\cdot729\). Theorem 1 verifies the rank hypothesis. Moreover \(a+1=-4q\), with \(q\) prime, so the odd part of \(a+1\) is squarefree and both exact local targets are \(\{0\}\). All hypotheses of the established arithmetic family theorem are verified by elementary congruence and primality tests.

For the prime-power extension, replace the congruence by \(p^e\equiv547\pmod{729}\). Rank one is still unconditional. The full depth-two conclusion follows if \(v_3(f)<v_3(q^2-1)\), in particular if \(3\nmid f\). Zero targets are asserted here only for \(f=1\).

**Corollary 2.** If \(n\) meets the three conditions of Theorem 2 and

\[
 n\equiv1\text{ or }-1\pmod{729},
\]

then (13) holds for \(a=3-8n^2\).

Here \(a+5=8(1-n^2)\) is divisible by 5832, Theorem 2 proves rank one, and \(a+1=-4D\) has squarefree odd part. Again both exact local targets are zero.

### Explicit new examples

The following entries are certified by the accompanying standard-library script, including primality by complete trial division and the exact analytic constant checks from the earlier companion script.

Linear family:

| p | q=8p−1 | a=3−32p |
|---:|---:|---:|
| 6379 | 51031 | −204125 |
| 12211 | 97687 | −390749 |
| 19501 | 156007 | −624029 |
| 48661 | 389287 | −1557149 |
| 159469 | 1275751 | −5103005 |

Quadratic/composite family:

| n | factorization of n | D=2n²−1 | a=3−8n² |
|---:|:---|---:|---:|
| 2915 | 5·11·53 | 16994449 | −67977797 |
| 8747 | 8747 | 153020017 | −612080069 |
| 11663 | 107·109 | 272051137 | −1088204549 |
| 29159 | 13·2243 | 1700494561 | −6801978245 |
| 32075 | 5²·1283 | 2057611249 | −8230444997 |

The script additionally checks the bounded 2-adic obstruction arguments over all parameter residues needed for them, and checks (3) by exact substitution at each displayed parameter. These checks supplement the symbolic proofs; no rank database, analytic-rank oracle, unproved Selmer solubility assumption, or floating-point computation is used.

## 5. Scope

These results remove the unspecified rank hypothesis from two explicit arithmetic patterns. For any proposed parameter in either pattern, only factorization, primality, and stated congruence tests remain. Theorems 1 and 2 themselves are unconditional implications and do not depend on the analytic Chabauty theorem.

The prime conditions may hold infinitely often, but this is not established here. In particular, simultaneous primality of \(p\) and \(8p-1\) in specified congruence classes is not being claimed, and neither is infinitude for \(2n^2-1\) in the quadratic pattern. The finitely displayed examples are individually unconditional.

## Necessity of retaining the odd-n hypothesis

The oddness condition in Theorem 2 cannot simply be removed. For n=6, the integer D=2n²−1=71 is prime, but the curve with A=−288 has the rational point (300,1080). Its descent class is 3, while the rational two-torsion point has class 2. Thus the first descent image has at least four classes. The two rational points on the isogenous curve supplied by X=A and X=A+4 have independent classes −2 and −71, so its descent image also has at least four classes. The rank formula gives rank at least two. This is not a counterexample to Theorem 2, whose statement explicitly requires n odd.

## A rank-certified parameter for the prime-7 progression

The primes r=63541 and 8r−1=508327 satisfy r≡5 modulo 8. Theorem 1 therefore proves rank one for a=3−32r=−2033309. Moreover a≡−5 modulo 2744. This verifies the arithmetic prerequisites for the separately stated prime-7 isolation theorem; the analytic conclusion follows by applying that independently reviewed theorem, rather than from the rank argument alone.
