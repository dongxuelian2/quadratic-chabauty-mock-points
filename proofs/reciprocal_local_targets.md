# Exact away-from-p targets in the reciprocal family

## Scope and notation

Let a be an odd integer, a != -1,3, put A=a-3, and let p be an odd good prime. Write L_q=log_p(q), and normalize the away-from-p local height so that it is zero at integral nonsingular points of an integral minimal Weierstrass model and equals -v_q(X)L_q when v_q(X)<0. Its duplication identity is

    lambda(2P)=4 lambda(P)-2 log_p|2Y(P)|_q.

Under X=q^(2r) X_min, Y=q^(3r)Y_min, the displayed-model height is lambda_min-2r L_q. Thus a common model correction cancels in the differences below. The formulas for height coefficients are rational and make sense independently of p.

The first model and its identical elliptic quotients are

    C_a: y²=x⁶+a x⁴+a x²+1,
    E: Y²=X³+A X²-A X,
    P1=(1+x²,y), P2=(1+x⁻²,y/x³),
    w_q=-lambda(P1)+lambda(P2)+2 log_p|x|_q.

The second model is

    c=(a+1)/2=(A+4)/2, d=(15-a)/2=8-c,
    C*: v²=c(u⁶+1)+d(u⁴+u²),
    E': Y²=Z³-2A Z²+A(A+4)Z,
    Q1=(c(1+u²),cv), Q2=(c(1+u⁻²),cv/u³),
    w*_q=-lambda(Q1)+lambda(Q2)+2 log_p|u|_q.

All functions are extended continuously at coordinate endpoints. Reciprocity sends w_q and w*_q to their negatives.

## The conclusions

1. For every odd q != p, w_q is identically zero, with no additional hypothesis on a.
2. If a is 3 modulo 8, w_2 is also identically zero.
3. For the second model, w*_q is zero at every odd q not dividing a+1, including all odd q dividing a-3.
4. Suppose q is odd and m=v_q(a+1)>0. The exact coefficient image w*_q(C*(Q_q))/L_q is:
   - If 2 is a square modulo q: {0} union { plus or minus 2k(m-k)/m : 1<=k<=floor(m/2) }.
   - If 2 is not a square modulo q and m is odd: {0}.
   - If 2 is not a square modulo q and m is even: {0, plus or minus m/2}.
5. If a is 3 modulo 8, w*_2 is identically zero.

In particular, both global actual targets are {0} if a is 3 modulo 8 and the odd part of a+1 is squarefree. Still assuming a is 3 modulo 8, the exact weaker second-target-zero condition is that every odd prime divisor q of a+1 has either valuation 1, or odd valuation and (2/q)=-1. No unrestricted classification of the prime-2 contribution is asserted.

For p=3 with good reduction, every second-target coefficient is 3-integral if 3 does not divide v_q(a+1) for every odd q dividing a+1. Since log_3(q) lies in 3 Z_3 for q !=3, and the 2-contribution is zero under the congruence hypothesis, this gives Omega* subset 3 Z_3. This sufficient integrality condition is not necessary: some displayed fractions simplify, and nonsplit odd multiplicities contribute zero.

## Exact criterion for the second target to lie in 3 Z_3

Assume a is 1 modulo 3 and 3 modulo 8, and let Omega* be the usual actual-local-image target, the Minkowski sum of the separate away-from-3 local images. Then

    Omega* subset 3 Z_3

if and only if, for every odd prime q dividing a+1 with (2/q)=1,

    v_3(v_q(a+1)) < v_3(q²-1).

There is no restriction on the multiplicities at primes with (2/q)=-1.

Proof. Set m=v_q(a+1) and e=v_3(q²-1). The hypothesis a=1 modulo 3 excludes q=3, so e>=1. Since q² lies in 1+3 Z_3,

    v_3(log_3 q)=v_3(log_3(q²))=e.

At a nonsplit prime the exact coefficient image is either {0} or {0, plus or minus m/2}; every coefficient is 3-integral. Its entire contribution therefore lies in 3 Z_3, regardless of m. At a split prime with 3 not dividing m, all coefficients 2k(m-k)/m are likewise 3-integral, and the displayed strict inequality holds automatically. If 3 divides m, then m>=3 and k=1 is among the attained coefficients. Every coefficient has valuation at least -v_3(m), while 2(m-1)/m has exactly that valuation. Thus the minimum valuation of a nonzero local contribution is exactly e-v_3(m), and the whole local image lies in 3 Z_3 exactly when e>v_3(m). The case m=1 has only the zero image and also satisfies the inequality automatically.

All remaining odd-prime images vanish, and the prime-2 image vanishes under the stated congruence. Each local image contains zero, witnessed by the rational points u=1, v=plus or minus 4. Consequently the global Minkowski sum lies in 3 Z_3 exactly when every individual local image does: each individual image occurs in the sum with zero chosen at all other primes. This proves both directions.

This sharpens, without replacing, the simpler sufficient condition that all odd-prime multiplicities in a+1 are prime to 3.

## Conditional family corollary

Let a be an integer satisfying

    a = -5 modulo (8*3^6),
    3 does not divide v_q(a+1) for every odd prime q dividing a+1.

Then at p=3 the exact first actual local-image target is Omega={0}, and the second satisfies Omega* subset 3 Z_3. These local-target conclusions do not require a rank hypothesis.

If, in addition, E_a(Q) has rank one, the analytic theorem and explicit congruence certificate in `../proofs/general_prime3_criterion.md`, together with its stated actual-target containment and endpoint-basepoint bridge, give

    C_a(Q_3)_2 = C_a(Q) = {(0,1),(0,-1),infinity_+,infinity_-}.

Here the depth-two set uses exactly the Mordell-Weil-restricted, actual-local-image convention of that companion. Indeed the congruence supplies its analytic hypothesis (H), Omega={0} supplies (T1), and Omega* subset 3 Z_3 supplies (T2). This is a conditional family theorem: no assertion is made that every parameter in the progression, or infinitely many such parameters, has rank one.

## First model: odd primes

The discriminant is Delta(E)=16 A³(A+4). If k=v_q(x)>0, P1 is integral and nonsingular because its Y-coordinate is a unit, while v_q(X(P2))=-2k. The heights and explicit logarithm cancel. Negative k follows by reciprocity. It remains to consider unit x. At good primes both images are integral, so the result is immediate.

### Primes dividing A

Let n=v_q(A), r=floor(n/4), and j=n-4r. Apply the common scaling X=q^(2r)X_min, Y=q^(3r)Y_min. The scaled coefficients have

    v(a2_min)=2r+j,  v(a4_min)=j,  v(Delta_min)=3j.

If j=0 the model is good. If j=1,2,3 its Kodaira type is respectively III, I0*, III*. These conclusions follow directly from Tate's algorithm over every odd residue characteristic, including 3: for j=1 the b8 test gives III; for j=2 the auxiliary cubic is T(T²+unit) and is separable; for j=3 the b8 test gives III*. Minimality also follows from the discriminant valuation being less than 12.

For these types the correction for any nonidentity component met by a rational point is respectively 1/2, 1, 3/2, in the doubled-height normalization used here. Thus an integral point has height 0 if it reduces nonsingularly and minus this constant times L_q otherwise. These are the standard component-intersection local-height corrections; importantly, for I0* all three possible nonidentity outer components have the same correction.

The two scaled X-coordinates differ by the unit x^-2 and the two scaled Y-coordinates by the unit x^-3. If either X-coordinate is nonintegral, both have the same valuation and hence height. Otherwise both are integral, and either both or neither reduce to the unique singular point (0,0). The preceding component corrections therefore prove equality of heights. This argument uses the actual component-height table, not equality of valuations by itself.

### Primes dividing A+4

Here A is a unit, the displayed model is minimal, and the reduction is multiplicative of type I_m, m=v_q(A+4), with equation

    Y²=X(X-2)² modulo q.

If x² is not 1 modulo q, both quotient images are nonsingular. Otherwise write s=1+x². Direct addition on E gives

    X(P1+P2)=(s²+A x²)/((x+1)² s),
    X(P1-P2)=(s²+A x²)/((x-1)² s),

where the applicable formula extends through a removable coincidence by the tangent law. If x is 1 modulo q use the first formula; if x is -1 modulo q use the second. Its denominator is a unit, while its numerator is 0 modulo q. Thus P1+P2 or P1-P2 reduces to (0,0), a nonsingular point of this nodal cubic. Therefore the component classes of P1 and P2 are equal up to sign.

For type I_m the height of an integral point in component i is -i(m-i)/m times L_q. This is unchanged by i -> -i. The two heights are consequently equal. No claim about component indices is inferred merely from equal valuations.

## First model: the prime 2

Assume a is 3 modulo 8. For unit x, x² is 1 or 9 modulo 16, and

    x⁶+a x⁴+a x²+1 = (a+1)(x²+1) = 8 modulo 16.

Thus there are no unit-x points. For v_2(x)>0, P1 has odd X and Y, and the X-derivative 3X²+2AX-A is odd. It is nonsingular on the displayed integral model and has displayed height zero. P2 has X-valuation -2v_2(x), giving the required cancellation. Reciprocity and continuity finish the proof. A possibly nonminimal displayed equation causes no issue: applying the model correction to the nonintegral image on a minimal model gives the same displayed height zero at a nonsingular displayed point.

## A duplication lemma at a nodal cubic

Let q be odd and consider

    E_b,D: Y²=X³+bX²+DX,
    v_q(b)=0, v_q(D)=m>0.

Assume v_q(b²-4D)=0, as is automatic here. The discriminant valuation is 2m and the equation is minimal. For an integral point with h=v_q(X)>0, write lambda(P)=H(P)L_q. Then

    H(P)=-h+h²/(2m)          if 0<h<=m,
    H(P)=-m/2               if h>=m.

Here h=infinity includes the rational two-torsion point (0,0) by continuity.

Proof. First suppose Y(P) is nonzero; nonzero two-torsion points follow by continuity. Duplication gives

    X(2P)=(X²-D)²/(4Y²).

If h>m, the curve equation gives 2v(Y)=m+h, while v(X²-D)=m. Hence v(X(2P))=m-h<0, so the height duplication identity gives H(P)=-m/2. If h=m, put t=v(Y)>=m. Again v(X²-D)=m. If t>m the doubled X-coordinate is nonintegral; if t=m it is a unit and nonsingular. In either case H(2P)=2(t-m), and duplication again gives H(P)=-m/2.

For 0<h<m, the curve equation gives v(Y)=h. Unless 2h=m, the doubled X-valuation is

    h_next=2 min(h,m-h).

If 2h=m, write v(X²-D)=m+e with e>=0. Then v(X(2P))=m+2e>=m. If X²=D exactly, 2P is the two-torsion point (0,0). These cases were already handled above. The doubled point cannot be O in this range: v(Y)=h is finite, and a nonzero two-torsion point with nonzero X has X-valuation 0 or m, not a valuation strictly between them. The proposed function G(h)=-h+h²/(2m) satisfies

    G(h_next)=4G(h)+2h.

Thus the discrepancy H(P)-G(h) is multiplied by 4 at every doubling that remains in 0<h<m. If an iterate reaches h>=m, the discrepancy vanishes by the preceding calculation. Otherwise all iterates remain in the compact set of points reducing to the node, which is disjoint from O. An away-from-p local height is locally constant on E(Q_q) minus O, so it has a finite image on this compact set. The integer h also has only the values 1,...,m-1, so the discrepancy has finite image. If its initial value were nonzero, its successive values 4^n times that value would be pairwise distinct in characteristic zero. This contradiction proves the formula. This finite-image argument does not appeal to p-adic growth of 4^n (which would be false for odd p).

This is also a self-contained derivation of the needed multiplicative component-height formula in this particular coordinate model.

## Second model: odd primes not dividing A+4

Its discriminant is

    Delta(E')=-256 A³(A+4)².

At q dividing A, c is a unit. Exactly the same scaling, types III/I0*/III*, and component-height argument as above applies, since v_q(-2A)=v_q(A(A+4))=v_q(A). Unit-u paired coordinates differ by units; nonunit-u coordinates give the nonsingular/formal cancellation. At the remaining odd primes the curve has good reduction and c is a unit, so the same elementary cancellation applies.

## Second model: complete calculation at q dividing A+4

Put m=v_q(c)=v_q(a+1)>0. The nodal lemma applies to E' with b=-2A and D=A(A+4). Here the node is (0,0), and the reduction is split exactly when 8, equivalently 2, is a square modulo q.

First let u be a unit. Both Q1 and Q2 are integral and have the same positive X-valuation h=m+v_q(1+u²)>=m. The lemma gives height -m/2 times L_q for each. Thus w*_q=0. This also covers u²=-1 by continuity.

Now let k=v_q(u)>0. The first quotient has X-valuation m, so its height is -m/2 times L_q. The second has X-valuation m-2k. Consequently:

- If 2k<m, the lemma gives H(Q2)=-(m-2k)+(m-2k)²/(2m), hence w*_q/L_q=-2k(m-k)/m.
- If 2k=m, Q2 has unit X-coordinate, so is nonsingular and has height zero. The value is -m/2.
- If 2k>m, Q2 is nonintegral, with height (2k-m)L_q. The value is again -m/2.

These formulas also give the endpoint value -m/2 when a Q_q-point exists at u=0. Negative k and infinity give the opposite values.

It remains to prove exactly which valuation ranges occur. The second curve equation is

    v²=c(u⁶+1)+d(u⁴+u²),    d=8-c.

If 0<2k<m, its leading term is d u², with d=8 modulo q. Thus such points exist if and only if (2/q)=1; in that case every positive integer k<m/2 occurs, by Hensel lifting a unit square.

If 2k>m, the valuation of the right side is m. Thus m must be even, and in fact sufficiently small u exist precisely when c is a square in Q_q. All such points already give the same saturated value -m/2.

If m is even, k=m/2 always occurs, whether or not c is a square. Write u=q^(m/2)r and v=q^(m/2)z. Modulo q the resulting equation is the nonsingular conic

    z²-8r²=c/q^m,    r !=0.

The number of affine solutions is q-(2/q), while at most two have r=0. This leaves a solution with r!=0 for every odd q: for q>=5 the count is at least four, and for q=3 it is exactly four. The derivative with respect to r is -16r, a unit, so a solution lifts to the full equation with r a unit. Therefore the saturated value always occurs for even m.

If m is odd and (2/q)=-1, none of the positive-valuation cases is possible. This proves every asserted image, including its surjectivity, rather than just an upper bound.

## Second model: the prime 2

Assume a is 3 modulo 8. Then v_2(A)>=3 and v_2(c)=1. If u has positive or negative valuation, the constant or leading term in the curve equation has odd valuation, so no such point exists. Hence u is a unit.

Put s=1+u², so v_2(s)=1. The equation factors as

    v²=s(c s²-2A u²).

The two terms in parentheses have valuations 3 and at least 4, respectively. Therefore v_2(v)=2. Scale Z=4z, Y=8w, obtaining the integral equation

    w²=z³-(A/2)z²+[A(A+4)/16]z.

Both images now have unit z and w. The derivative

    3z²-Az+A(A+4)/16

is odd, so both are nonsingular with height zero on this integral equation. Their common change-of-model correction cancels, and log|u|_2=0. Endpoints do not occur because c has odd valuation. Thus w*_2=0.

## Explicit counterexamples to an unrestricted second-target-zero claim

Take a=1699 and q=5. Then a is 3 modulo 8 and 1 modulo 3, c=850=25*34, and 34 is a 5-adic square. At u=0 choose v=sqrt(c). The finite quotient is Q=(c,c sqrt(c)), and

    X(2Q)=(c-2A)²/(4c),    v_5(X(2Q))=-2.

Hence lambda(2Q)=2 L_5. Since v_5(2Y(Q))=3, duplication gives lambda(Q)=-L_5. The singular quotient and explicit logarithm leave -v_5(c)L_5=-2L_5, so

    w*_5(u=0)=-L_5,   not zero.

The same value occurs at positive finite u of sufficiently large 5-adic valuation, so this is not an endpoint artifact.

A denominator-3 example inside the explicit analytic neighborhood is a=23323=-5+4*(8*3^6), q=7, u=7. Here p=3 is good, a is 3 modulo 8, c=11662=2*17*7³, and m=3. The right side of the second curve equation has valuation 2 and square unit residue 1 modulo 7, so v exists in Q_7. The exact formula gives

    w*_7=-(4/3)log_p(7).

For p=3 this is a 3-adic unit, since v_3(log_3(7))=1. Thus second targets need not even lie in 3 Z_3 without an additional arithmetic condition, even within the explicit parameter neighborhood where the analytic companion certifies (H). No rank assertion or counterexample to full depth-two equality is claimed for this parameter.

These are arithmetic local-height statements only. They assert neither Mordell-Weil rank hypotheses nor a full depth-two containment theorem. The statements and scope distinctions above have received independent review.
