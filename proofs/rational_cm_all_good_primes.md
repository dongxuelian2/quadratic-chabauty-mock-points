# Exact Weierstrass visibility and the prime-two boundary

Let `C_a: y²=x⁶+a x⁴+a x²+1`, with `a≠−1,3`. The smooth
projective model has no Weierstrass point at infinity. This note removes
the restriction “odd” from the good-prime conclusion of
[the rational-CM classification](rational_cm_weierstrass_classification.md),
without using a two-adic comparison theorem.

## 1. An exact fieldwise criterion

For any field `k` of characteristic different from two, the number of
`k`-rational Weierstrass points is

    2·1{−1∈k×²} + 4·1{−a−1∈k×² and 3−a∈k×²}.       (1)

Here all three tested elements are nonzero by the smoothness assumptions.
Indeed,

    x⁶+a x⁴+a x²+1=(x²+1)(x⁴+(a−1)x²+1).

The first factor gives the first summand. For a root of the second,
`x≠0` and

    (x−x⁻¹)²=−a−1,       (x+x⁻¹)²=3−a.              (2)

Conversely, choose `t²=−a−1`, `r²=3−a` in `k`. Since
`r²−t²=4`, the elements `(r+t)/2` and `(r−t)/2` are nonzero
and reciprocal. Their positives and negatives give precisely the four
distinct roots. Neither vanishing square root nor overlap with `x²+1`
is possible when `a≠−1,3`. This proves (1), including both necessity
and sufficiency; no splitting-field search is involved.

For example, for `a∈Z₂\{−1,3}`, the second summand is present exactly
when `−a−1` is a nonzero square of valuation at least six. Necessity
follows from `x` being a unit and
`v₂(x−x⁻¹)=v₂(x²−1)≥3`. Conversely, if `t²=−a−1` and
`v₂(t)≥3`, then `3−a=4(1+t²/4)` is a square because its unit
factor is one modulo eight. This is an exact criterion on the entire
two-adic integral parameter space, not just on the seven CM parameters.

## 2. No two-adic Weierstrass points in the rational-CM packet

A nonzero rational number `q=2^n u`, `u∈Z₂×`, is a square in `Q₂`
exactly when `n` is even and `u≡1 modulo8`. The necessity follows
from odd squares modulo eight; sufficiency follows by lifting odd square
roots (equivalently, the usual two-adic square criterion).

The following table gives an obstruction for every parameter in the
complete packet. The entries in the last column are the valuation and
odd unit residue of the element in the middle column.

| a | tested nonsquare from (1) | `(n,u mod8)` |
|---|---|---|
| 0 | −a−1=−1 | `(0,7)` |
| −3/2 | −a−1=1/2 | `(−1,1)` |
| −15/16 | −a−1=−1/16 | `(−4,7)` |
| −5 | 3−a=8 | `(3,1)` |
| 15 | −a−1=−16 | `(4,7)` |
| −33 | −a−1=32 | `(5,1)` |
| 255 | −a−1=−256 | `(8,7)` |

Also `−1` is not a two-adic square. Formula (1) therefore proves

    {W∈C_a(Q₂): W is Weierstrass}=∅                 (3)

for all seven parameters. This statement is independent of the chosen
integral equation and of whether the curve has good reduction at two.
In particular an even discriminant of the displayed equation is not
being used as an intrinsic bad-reduction certificate.

**All-good-prime corollary.** For each

    a∈{−3/2,−15/16,−5,15,−33,255},

every locally visible Weierstrass point is excluded from the full
restricted depth-two set at **every prime of good reduction**. The
Selmer convention is precisely the Mordell–Weil abelian-image and
actual-local-image convention of the existing rational-CM theorem.

**Proof.** Apply that theorem for odd primes; at two there is no point
to test, by (3). This proof asserts nothing about crystalline fibers,
height normalizations or logarithm kernels at coefficient prime two. ∎

## 3. The reciprocal parameter involution and its exact twist

There is a useful equation-level identity, valid for every `a≠−1`:

    (u+1)⁶ f_a((u−1)/(u+1))
      =2(a+1)[u⁶+T(a)u⁴+T(a)u²+1],
    T(a)=(15−a)/(a+1),       T(T(a))=a.             (4)

Thus `x=(u−1)/(u+1)`, `v=(u+1)³y` gives a rational
isomorphism from `C_a` to the smooth projective curve

    v²=2(a+1) f_(T(a))(u).                         (5)

The rational inverse on the affine overlap is `u=(1+x)/(1−x)`,
`y=v/(u+1)³`; hence the isomorphism extends to smooth projective
models. In particular it maps the Weierstrass divisors bijectively.
The seven parameters break into

    {0,15}, {−3/2,−33}, {−15/16,255}, {−5}.

The multiplier `2(a+1)` is essential. For `a=0,−3/2,−15/16,−5`
its squareclass is respectively `2,−1,2,−2`. These are not rational
isomorphisms between the corresponding *untwisted* reciprocal curves.
Equation (5) transports the existing full-depth-two statements only to
the actually isomorphic model, with the basepoint, global
Mordell–Weil condition and every local condition transported as well.
It supplies no rank or Selmer conclusion for arbitrary quadratic twists.

On the other hand, multiplying the sextic by any nonzero scalar does
not change its Weierstrass x-coordinates, so (1) and (3) apply to those
twists as visibility statements, without any rank assumption.

The checker `scripts/check_cm_weierstrass_visibility.py` verifies the
square obstructions, all coefficients of (4), the packet involution and
the exact count (1) over small odd finite fields. The proof above,
rather than those finite-field checks, establishes the uniform statements.
