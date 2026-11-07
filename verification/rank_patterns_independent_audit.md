# Independent audit of the checkable rank-one patterns

Status: completed independent audit. This supplements, rather than retroactively enlarges, the earlier general-family audit.

## Result and scope

The two rank theorems in `../proofs/checkable_rank_patterns.md` pass independent review with their stated hypotheses. Their congruence-restricted prime-3 corollaries follow from the previously audited analytic, exact-local-target and endpoint-basepoint results. No infinitude assertion is justified or made.

Audited deliverables:

- `../proofs/checkable_rank_patterns.md`
- `../scripts/check_rank_patterns.py`
- `../verification/rank_patterns_output.txt`

A separate implementation, `../scripts/check_rank_patterns_independent.py`, tests the uniform 2-adic obstructions on every primitive residue pair, rather than using the source script's two projective charts. It also independently checks the ten examples by exhaustive trial division and exact integer arithmetic. All checks pass.

## Common descent setup

The descent support statement, quartic normalization and identity

    2^rank = |delta(E(Q))| |delta'(E'(Q))| / 4

are correctly applied. The proof uses necessary local conditions to bound the actual descent images, and explicit points to match those bounds. It never promotes merely locally soluble coverings to rational points.

The rational points (A,2A) and (A+4,2(A+4)) on E' are correct. Their squareclasses give the required four-element subgroups in both patterns. Together with the first curve's nontrivial torsion squareclass, this proves the rank lower bound as well as the upper bound, without a separate analytic-rank or nontorsion assumption.

## Linear pattern

For primes r and q=8r-1 with r congruent to 3 or 5 modulo 8, and A=-32r:

1. The first candidate support is exactly {±1, ±2, ±r, ±2r}. All negative candidates have a strict real obstruction.
2. For d=2, odd U gives the nonsquare residue 2 modulo 8. For even U and odd V, dividing by 16 gives the nonsquare residues r or r+2 modulo 8. The division is legitimate because the original equation forces 4 to divide N.
3. The torsion squareclass 2r then rules out r by the group property. Thus the first image is exactly {1,2r}.
4. On E', multiplication by the torsion class 2rq permits every candidate class to be represented by an odd signed divisor of rq. The odd-d lemma is correct: odd U directly forces d=1 modulo 8; U divisible by 4 gives residue 128 modulo 256; and U exactly divisible by 2 reduces to the same d=1 modulo 8 condition after dividing by 16.
5. Among ±1, ±r, ±q, ±rq, only 1 and -q are 1 modulo 8. Restoring the torsion multiplier gives precisely {1,-2r,-q,2rq}, all realized by the known points.

This proves rank exactly one. The prime-power extension r^e with e odd and 8r^e-1=q^f is valid too. Its valuation and residue arguments are unchanged. The congruence q^f=7 modulo 8 forces f odd and q=7 modulo 8, and the distinct underlying primes preserve the four-element known subgroup.

## Odd quadratic/composite pattern

The assumption that n is odd is explicitly present and must be retained. For odd n>1 with all prime divisors 3 or 5 modulo 8, exactly one prime r=3 modulo 8 of odd exponent, and D=2n^2-1 prime:

1. The coordinate valuation lemma is correct. For an odd j=v_p(x), the cubic term is uniquely lowest when j<e=v_p(n), and the linear term is uniquely lowest when j>e. Both have odd valuation. Thus j=e must be odd. Cancellation at j=e imposes the precise congruences -8 times a square on E and 32 times a square on E'.
2. Consequently the first image has support only at 2 and the distinguished r. The real place excludes negative classes.
3. The d=r quartic has nonsquare residue r modulo 16 when U is odd: when V is odd, its two coefficients divisible by 8 cancel modulo 16. When U is even and V odd it is 8 modulo 16. This excludes r, and torsion multiplication excludes 2r. The first image is {1,2}.
4. Since (2/p)=-1 at every prime of n, no such prime appears in the second image. Its candidate support is therefore only -1, 2 and D.
5. The known subgroup H={1,-2,-D,2D} has four distinct classes. To exclude the remaining coset it suffices to exclude -1.
6. At the distinguished r, the two possible unique lowest-valuation terms of the d=-1 quartic have unit squareclasses -1 and 32. Both are nonsquares modulo r. The equality case would require 2v_r(U)=v_r(n), impossible because the latter is odd. The U=0 and V=0 endpoint cases are included by this argument or direct reduction.

Thus the second image is exactly H, proving rank one.

The optional extension D=q^f for a single odd prime q is also valid. The congruence D=-1 modulo the distinguished r makes D a nonsquare there, forcing f odd. The same support reduction and obstruction prove the second image is {1,-2,-q,2q}. Since n is odd, D=1 modulo 8 then forces q=1 modulo 8. If this extension is included, its prime-3 target condition is the already proved split-prime inequality v_3(f)<v_3(q^2-1).

## Scope guard: even n

Dropping oddness would produce a false theorem. At n=6, D=71 is prime and the required odd-prime pattern holds, but E with A=-288 has the point (300,1080). Its descent class is 3. Together with torsion class 2 this gives at least four first-image classes; the known points on E' give at least four second-image classes. The descent identity therefore forces rank at least two. This is not a counterexample to the stated theorem.

## Arithmetic and Chabauty corollaries

The linear congruence r=547 modulo 729 gives a+5=8(1-4r), divisible by 8 times 729. The quadratic congruence n=±1 modulo 729 similarly gives a+5=8(1-n^2). In both prime cases, a+1 is -4 times a prime, so both actual targets vanish. The previously audited analytic certificate therefore proves the four-endpoint equality for all parameters meeting these entirely checkable hypotheses.

The independent checker confirms every primality, factorization and congruence claim for the ten displayed examples. Its output is:

    All uniform 2-adic obstructions PASS on every primitive residue pair.
    Ten example factorizations, primality claims, congruences and known points PASS.
    Scope guard PASS: n=6 admits the extra first-image class 3 via (300,1080).

The additional rank-only prime-7 candidate also checks: 63541 and 508327 are prime, 63541 is 5 modulo 8, a=-2033309 is -5 modulo 2744, and a+1=-4 times 508327. The rank theorem gives rank one and the local-target theorem gives zero targets. This audit does not supply a prime-7 analytic isolation theorem.

## Optional even-A nontorsion lemma

The separate observation mentioned during review is valid but is not needed in the rank-family proofs. For every nonsingular even A, P=(1,1) has X(2P)=(A+1)^2/4. The integral change

    x_new=9X+3A, y_new=27Y

gives the short integral equation

    y_new^2=x_new^3-27A(A+3)x_new+27A^2(2A+9).

The new x-coordinate of 2P still has denominator 4. Nagell–Lutz therefore rules out torsion. The exclusions A=0,-4 are necessary for nonsingularity.
