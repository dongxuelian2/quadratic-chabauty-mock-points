# Exact finite-field scope of the small-disk method

Status: independently reviewed structural supplement. This classifies the reductions with at most eight rational residue disks relevant to the present endpoint and special-center arguments. It does not rule out other Chabauty proofs, more-disk arguments, non-scalar directions, or four-point full depth-two equality at larger primes.

Let a be an odd integer and put

\[
 C_a:y^2=x^6+ax^4+ax^2+1
\]

and let p be an odd good model prime, equivalently \((a+1)(a-3)\not\equiv0\pmod p\). Both elliptic quotients are isomorphic to

\[
 E_a:Y^2=X^3+(a-3)X^2-(a-3)X.
\]

The two quotient maps give \(J(C_a)\sim E_a^2\), so writing \(t_p=p+1-\#E_a(\mathbf F_p)\),

\[
 \#C_a(\mathbf F_p)=p+1-2t_p.
\]

Hasse's bound \(|t_p|\le2\sqrt p\) implies that a reduction with at most eight rational points satisfies

\[
 p+1-4\sqrt p\le8,
 \qquad p\le(2+\sqrt{11})^2=15+4\sqrt{11}<29.
\]

Every rational residue point lifts to a full Q_p residue disk because the model is smooth.

## The scalar obstruction removes p=1 modulo 4

At every good prime p≡1 modulo 4, the two points (±i,0) are Q_p-visible and pass both scalar heights exactly. The first quotient pair agrees at two-torsion, so its height is −log_p(±i)=0. Under the second coordinate u=(x+1)/(x−1), these points have u=∓i and again have zero second height. For odd a, both actual targets contain zero (the first uses the nonsingular rational point above x=0); the second model has rational points u=±1, v=±4 whose local contributions vanish individually.

Consequently the intersection of the two scalar actual-target conditions cannot consist of only the four rational endpoints at such a prime. This is an obstruction to this scalar-intersection conclusion, not an assertion that (±i,0) belong to the full depth-two set.

The primes to inspect for a four-point conclusion by the present at-most-eight-disk scalar method are therefore exactly 3,7,11,19,23.

## Complete finite enumeration

For each of these primes, inspect every a modulo p with (a+1)(a−3) nonzero. The complete list with at most eight rational points is:

| p | a modulo p | number of disks | disks beyond the four rational endpoints |
|---|---|---:|---|
| 3 | 1 | 8 | four above x=±1 |
| 7 | 2 | 8 | four quartic Weierstrass disks, x=±2,±3 |
| 7 | 4 | 4 | none |
| 11 | 1 | 8 | four above x=±1, y=±2 |
| 11 | 2 | 4 | none |
| 11 | 7 | 8 | four above x=±1, y=±4 |
| 19 | 0 | 4 | none |
| 23 | 20 | 8 | four quartic Weierstrass disks, x=±3,±8 |

The supplied exact enumeration script loops over these finite fields, counts every affine (x,y) solution, adds the two points at infinity, verifies the elliptic point-count identity for every eligible parameter, and asserts this entire table. This is a reproducible exhaustive finite computation, not a sample or numerical approximation.

In particular, the **exactly-eight-disk** possibilities are (p,a mod p)=(3,1),(7,2),(11,1),(11,7),(23,20). There are none at p=19. The endpoint-only four-disk layouts at (7,4),(11,2),(19,0) suggest additional simpler analytic criteria, but the table alone certifies neither height isolation nor rank one.

For the two already studied integer parameters:

- a=−5 falls in the p=3, a=1 case and p=7, a=2 case. The prime-7 companion proves first-height isolation for all odd a≡−5 modulo 343, and full restricted equality under rank one and a≡3 modulo 8.
- a=−157469 falls in p=3, a=1 and p=11, a=7. The prime-11 companion proves its exact two-height intersection and full restricted equality. Prime 7 is bad for this parameter because 7 divides a−3.
- At p=5 both parameters have the exact (±i,0) scalar obstruction above.

The Hasse argument only bounds primes for this small-disk layout. It says nothing against successful analysis of more than eight disks at p≥29 or at any other prime.
