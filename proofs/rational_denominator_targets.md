# Rational parameters: exact denominator-prime local targets

Let a in Q, a != -1,3, A=a-3, and let p be an odd good prime. Use the models, doubled local-height normalization and continuous endpoint extensions of [reciprocal_local_targets.md](reciprocal_local_targets.md). In particular P=(1,1) on E: Y²=X³+AX²-AX. Write L_q=log_p(q). This note concerns actual local images, not a sufficient test for full depth-two membership.

## Theorem

For an odd q != p with v_q(a)=-m<0, put beta=q^m a in Z_q^*, and chi=(beta/q).
Then the second-model function w*_q is identically zero, whereas

    lambda_q(P)=(m/2)L_q.

The exact first-model coefficient image w_q(C_a(Q_q))/L_q is

    {±m/2}
    union {±2k(m-k)/m : 1<=k<m/2, m even, chi=1}
    union Z,

where Z={0} if q=1 modulo 4, or if m is even and (q!=3 or chi=-1); otherwise Z is empty.

In particular the two local targets behave differently at denominator primes. For a=13/7 and q=7 the first image is exactly {±L_7/2}, with no zero, while the second image is {0}.

## Normalized base extension

Set Q=q^m. Over K=Q_q when m is even, or K=Q_q(sqrt(q)) when m is odd, choose s with s²=Q. Extend v_q with v_q(q)=1 and write e for the ramification degree. Scale the elliptic coordinates by

    z=Q X,  w=s³Y.

For the height normalization over K use log_p(q)/e per unit of the integer valuation v_K=e v_q. Local heights then agree with the original heights on Q_q-rational points. The displayed-model height is lambda_min+m L_q. Consequently this correction cancels in paired differences.

## Second model

Put c=(a+1)/2 and gamma=Qc, a unit. The scaled equation is

    w²=z³+(8Q-4gamma)z²+(4gamma²-8Qgamma)z.

Its reduction is z(z-2gamma)², its c4 is a unit, and its normalized discriminant valuation is m. Thus the minimal model has type I_(em) over K. The quotient coordinates are gamma(1+u²) and gamma(1+u^-2).

If k=v_q(u)>0, the first image reduces to z=gamma, a nonsingular point, and the second has z-valuation -2k. Its height is 2k L_q, cancelling 2 log_p|u|_q=-2k L_q. Negative k follows by reciprocity.

Suppose u is a unit. Unless u²=1 in the residue field both images are nonsingular (this includes u²=-1). Otherwise let epsilon=±1 with u congruent to epsilon. The addition law gives, on the unscaled model,

    X(Q1+epsilon Q2)
      =[c(u²-1)²+8u²]/[(u+epsilon)²(u²+1)].

The denominator is a unit and after scaling the numerator becomes gamma(u²-1)²+8Q u², which reduces to zero. Hence Q1+epsilon Q2 reduces to (0,0), a nonsingular point, whereas the node is (2gamma,0). The two component indices are therefore equal up to sign. The multiplicative correction -i(n-i)/n, for n=em, is unchanged by sign; both integral quotient images have equal heights. The addition formula extends by the tangent law at u=epsilon (there X(Q1+epsilon Q2)=1). Continuity handles every coordinate endpoint. This proves w*_q=0, without requiring split multiplicative reduction.

## First model: pointwise values

Write alpha=QA. Its scaled model is

    w²=z³+alpha z²-Q alpha z.

Here alpha is a unit, the discriminant has normalized valuation 2m, and the model has type I_(2em). Apply the nodal duplication lemma in reciprocal_local_targets.md over K, with integer valuations multiplied by e. For an integral point of positive normalized z-valuation h its minimal height divided by L_q is

    -h+h²/(2m) if 0<h<=m,
    -m/2 if h>=m.

The value at the two-torsion point is included by continuity. This use of the duplication lemma does not infer component indices merely from valuations.

For k=v_q(x)>0 the first quotient has z-valuation m. The second has z-valuation m-2k. Thus, after the common correction cancels,

    w_q/L_q=-2k(m-k)/m  if 0<2k<m,
    w_q/L_q=-m/2       if 2k>=m.

At 2k=m the second image is nonsingular; at 2k>m it is nonintegral with height (2k-m)L_q. If x is a unit, both quotient z-valuations are m+v_q(1+x²)>=m, so their heights coincide and w_q=0. Reciprocity supplies negative k.

For P=(1,1), X(2P)=(a-2)²/4 has valuation -2m. Its scaled coordinate has valuation -m, so lambda_min(2P)=m L_q and lambda(2P)=2m L_q. Since 2Y(P)=2 is a unit, the duplication identity gives lambda(P)=m L_q/2.

## Exact attainability

For k>m/2, take x=q^k. The curve's right side lies in 1+qZ_q and is a square, so both saturated values occur by reciprocity.

For 0<2k<m, the right side has valuation 2k-m and leading unit beta times a square. Hence points in this range exist exactly when m is even and chi=1. Conversely those conditions supply every indicated k.

Only unit x can give zero. If q=1 modulo 4, take x²=-1 and y=0. If q=3 modulo 4, then 1+x² is a unit for every unit x. The right side has valuation -m, excluding odd m. For even m, with z=q^(m/2)y/x, the residual equation is

    z²=beta(1+x²),  x!=0.

It has q-1-2chi solutions: the full conic has q-chi solutions and exactly 1+chi have x=0. All remaining solutions have z!=0 and lift by Hensel's lemma. The count is positive for q>=7; at q=3 it is positive exactly when chi=-1. This proves the complete image formula.

## Global consequences and limitations

The integral-parameter local proofs in reciprocal_local_targets.md depend only on local integrality, so they also apply to rational a at primes where a is integral. Thus, if a lies in Z_2 and a=3 modulo 8, the second target is {0} whenever each positive odd v_q(a+1) is 1 (more generally, the previously stated odd nonsplit condition suffices). Negative valuations of a+1 introduce no second-target contribution.

If D is the positive reduced denominator of a, a lies in Z_2 with a=3 modulo 8, and p does not divide D, the global height of P is

    h_p(P)=lambda_p(P)+(1/2)log_p(D).

At locally integral odd primes P is nonsingular because its Y-coordinate is 1, and its local height is zero. The dyadic displayed height is likewise zero under the stated congruence. The denominator-prime theorem accounts for all remaining terms.

Consequently formulas that silently replace h_p(P) by lambda_p(P) cannot be transported from integral parameters to rational parameters. Nor can one assume the first local image contains zero. None of these local calculations by itself determines full depth-two membership.
