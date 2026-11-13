# A certified nonzero period for the actual non-CM target at 5

Put a=-157469, A=a-3=-157472 and

    C: y²=f(x)=x⁶+a x⁴+a x²+1,
    W₋=(-i,0), W₊=(i,0), i²=-1 in Q₅,
    ν_j=x^j dx/(2y), 0<=j<=4.

Use the canonical Frobenius-invariant Coleman path and the outer-first
word convention of the [fixed-parameter certificate](five_adic_residual_certificate.md).
The actual finite computation, with the error bounds justified below, gives

    X=(1/i) integral_(W₋)^(W₊) ν₀ν₁
      =22100+O(5⁷).                                 (1)

Thus v₅(X)=2, since 22100/25=884 is a unit. The holomorphic period is

    I=integral_(W₋)^(W₊) (dx/y)(x dx/y)=4iX != 0.

By the [holomorphic-coordinate lemma](holomorphic_residual_test.md), the
relative central class is twice the discrepancy and its holomorphic
coordinate equals I. Consequently δ₅(W₊) and δ₅(W₋) are nonzero.
On the monic odd-degree model defined in that note, the equivalent period is

    J₅(A)=integral_∞^((A,0)) (X dX/Y)(dX/Y)
         =2X/A=8275+O(5⁷).                          (2)

The actual residual target grid is `{0,±Theta₅(e₃₇)}`. Equation (1)
excludes its zero entry. It does not compare δ₅(W₊) with the two nonzero
entries, so it does not settle full depth-two membership of either W.

## 1. The regular lift at this parameter

Unlike the preceding a=-605 certificate, this parameter is 1 modulo 5.
Its polynomial satisfies

    f mod5=(x²+1)(x²-2)(x²+2),  gcd(f,f')=1 mod5.

Thus C has good reduction at 5. In the finite free algebra
`Z₅[x]/(f⁵)`, the initial H₀=x⁵ satisfies `f(H₀)=0 mod5`, because
`f(x⁵)=f(x)⁵ mod5`. Also `f'(x⁵)=f'(x)⁵ mod5` is a unit there.
Its inverse is computed by polynomial extended Euclid modulo `(5,f⁵)`
and lifted by Newton iteration. The inverse `-x⁵` used for a=-605
must not be reused at this parameter.

Hensel uniqueness now gives H congruent to x⁵ modulo 5, represented
by a polynomial of degree at most 29, such that

    f(H)=f⁵ U,  U=1 mod5,
    H'=f⁴ P,   P=0 mod5,
    deg U<=144, deg P<=4.                            (3)

These statements follow exactly as in Sections 3–4 of the preceding
certificate: differentiate the first identity and use that f'(H) is a
unit modulo f⁴. The quotient f⁴ is monic, so P remains integral.
Evenness of f and uniqueness make H odd, U and P even. The regular
Frobenius lift is `phi(x)=H(x)`, `phi(y)=y⁵ U(x)^(1/2)`.

At x=±i one has `f'(±i)=-2A(±i)`, a 5-adic unit. Since
`H(±i)=±i mod5` and `f(H(±i))=0`, uniqueness of the simple lifted
root proves H(±i)=±i exactly. Thus phi fixes both Weierstrass endpoints.

Write `phi*ν_i=d(yK_i)+sum_j M_ij ν_j` by horizontal reduction.
Every primitive yK_i is regular and zero at these endpoints. The vector
of single periods therefore satisfies `v=Mv`. The characteristic
polynomials, computed modulo 5⁷, are

    char(M_e)=(t-5)(t²+2t+5),
    char(M_o)=t²+2t+5,                              (4)

on indices (0,2,4) and (1,3), respectively. In particular
`det(I-M)=4 mod5`; the true matrix has the same reduction by the error
bound below. Therefore I-M is invertible and all five single periods
are zero. This also removes the single-period products in shuffle and
path composition; no uncomputed endpoint correction is discarded.

## 2. Seven-digit arithmetic certificate

All entries in this section are modulo 78125=5⁷. The Frobenius matrix is

    [21175,     0, 22195,     0, 36815]
    [    0, 21175,     0, 57470,     0]
    [16500,     0, 41315,     0, 56395]
    [    0, 66641,     0, 56948,     0]
    [51008,     0, 41999,     0, 15638].

In cross-word order `(0,1),(0,3),(2,1),(2,3),(4,1),(4,3)`, the system
`(I₆-M_e tensor M_o)z=c` has

    c=[15725,65180,24125,53778,10216,37248],
    z=[22100,73695,38675,51468,35041,50596].          (5)

The expanded system and reproduction inputs are recorded in
[`verification/actual_noncm_p5_period.json`](../verification/actual_noncm_p5_period.json).
Multiplication verifies (5) modulo 78125. From (4), the tensor-system
determinant is congruent to

    (1-5)² ((1+5)²-(-2)²) (1-5*(-2)+25*5)
      =69632 mod78125,

which is 2 modulo 5. The supersingular value 72576 from the earlier
certificate is not used. Both M and c are integral after removing
their explicitly recorded reduction scales.

## 3. Why the existing analytic error bounds apply

This is a direct certification for the displayed polynomial, not an
interpolation claim about other parameter residues. The proof of
[Section 7 of the preceding certificate](five_adic_residual_certificate.md#7-error-bound-twenty-terms-suffice-modulo-5⁷)
uses only (3), integral coefficients of f and the unit final determinant.
All hold here, with the following unchanged estimates.

The n-th term of the binomial expansion of U^(-1/2) contributes a
polynomial pullback of degree at most `132+144n` and valuation at least
`n+1`. Horizontal reduction loses at most
`L_n=floor(log₅(130+144n))` digits. At infinity, the required inverse
square-root series of `1+a z²+a z⁴+z⁶` is integral: its binomial
denominators are powers of 2. Thus the proof of this reduction bound
is independent of the residue or size of a in Z₅.

For a bilinear term with total index s, endpoint polynomial integration
loses at most `floor(log₅(260+144s))` additional digits. Evaluation at
±i introduces no loss, since i is a unit. Consequently its valuation
is at least

    s+2-3 floor(log₅(260+144s)).

For all omitted terms s>=20 this is at least seven, by the same
explicit logarithmic-breakpoint inequality proved in that section.
The single-pullback tail is O(5¹⁷). Hence twenty binomial terms give
right-hand-side tail O(5⁷) and matrix tail O(5¹⁷).

For finite arithmetic modulo 5³⁰, use the theoretical degree bound
2868, horizontal loss at most four and endpoint integration loss at
most five, even though modular trimming gives smaller effective
degrees. Coefficientwise verification of the scaled horizontal identity
certifies M and the primitives to at least 5²². Conservative bilinear
propagation leaves finite right-hand-side error O(5¹³). The final
system matrix and right-hand side are integral and its determinant is
a unit. Applying

    z-z₀=A_true^(-1)((c_true-c₀)-(A_true-A₀)z₀)

therefore proves (5) with error O(5⁷). Agreement of implementations is
an arithmetic check, while these estimates supply the error guarantee.

The parameterized regular-lift implementation and a separately adapted
version of the original independent horizontal-reduction implementation
reproduced all twenty-five matrix entries and all six periods in (5).
The latter used a separately computed polynomial inverse modulo 5,
then its original Newton and reduction code. The audit checked the
squarefree reduction, endpoint fixing, single-period vanishing, the
ordinary characteristic polynomials and unit determinant, and each
parameter-independent hypothesis of the preceding error proof.

Reproduce the pointwise certificate and its independent calculation:

    python scripts/compute_p5_parameter_periods.py -157469
    python scripts/compute_p5_residual_independent.py -157469
    python scripts/check_actual_noncm_five_adic_period.py

No ray-group dimension, global lifting criterion, or value of
Theta₅(e₃₇) follows from this calculation.
