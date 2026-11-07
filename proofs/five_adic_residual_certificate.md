# A certified nonzero residual period for C_{−605} at p=5

Status: complete proof with independent algebraic, analytic and arithmetic verification. The regular-lift construction, reduction bounds, endpoint comparison and both separately written Python implementations have passed independent review and execution checks. The reported values are certified modulo 5⁷.

## 1. Result and precise scope

Let

    C: y²=f(x)=x⁶−605x⁴−605x²+1,
    W₋=(−i,0), W₊=(i,0), i²=−1 in Q₅,
    ν_j=x^j dx/(2y),  j=0,1,2,3,4.

All integrals use the canonical Frobenius-invariant Coleman path and the outer-first word convention. The computation proves

    (1/i) ∫_{W₋}^{W₊}ν₀ν₁ = 21625 + O(5⁷).       (1)

In particular its valuation is exactly three, with leading unit three. Since dx/y=2ν₀ and x dx/y=2ν₁, the holomorphic period is

    I=∫_{W₋}^{W₊}(dx/y)(x dx/y)
      =4i(21625+O(5⁷)) ≠ 0.                       (2)

The independently proved holomorphic residual criterion therefore gives δ₅(W₊)≠0, and δ₅(W₋)=−δ₅(W₊)≠0. For this parameter all actual residual targets over Q vanish: a−3=−32·19, the dyadic theorem applies, and 19 is nonsplit in Q(i). The other odd bad prime151 is potentially multiplicative and contributes zero residual image. The rank-one certificate is recorded in Theorem25 of [PROOF.md](../PROOF.md); non-CM follows from v₁₅₁(j(E))=−1, using j(E)=256a³/(a+1). Under the established non-CM, rank-one restricted Selmer convention, BOTH W₊ and W₋ are excluded from the residual quotient's Chabauty–Kim set and hence from full depth two.

This does NOT prove C(Q₅)₂ equals the four rational endpoints. It excludes these two previously surviving Weierstrass points; no assertion about every other 5-adic point is made.

On the monic odd-degree model of the preceding holomorphic-test note, with A=−608, the equivalent target is

    J₅(−608)=∫_∞^{(−608,0)}(X dX/Y)(dX/Y)
             = 48500+O(5⁷).                       (3)

Indeed I=2iA J and I=4i times (1), so J=2·21625/(−608) modulo 5⁷.

## 2. Inputs and computational provenance

Only the exact polynomial f, the prime 5, twenty binomial terms, and coefficient arithmetic modulo 5³⁰ are used. The implementation is original Python using integer arithmetic and SymPy for a six-by-six rational linear solve. It does not invoke Sage, Magma, PARI, downloaded research software, a remote execution service or any unverified endpoint routine.

Reproduction command:

    python scripts/compute_p5_residual.py 20 30

The script generates chabauty_regular_frobenius_certificate.json, containing the matrix, right-hand side and six answers modulo 78125. Its defaults are exactly twenty terms and coefficient precision thirty; only the residues modulo 5⁷ are displayed as certified. Working with larger cutoffs and larger coefficient precision was used as an additional check, not as the proof of the error bound. The separate standard-library checker scripts/check_p5_residual_certificate.py verifies the recorded linear system, characteristic polynomials, determinant, targets and theoretical precision parameters. That smaller checker does not replace the full Frobenius recomputation or the analytic proof. The committed witness is [verification/p5_residual_certificate.json](../verification/p5_residual_certificate.json); the checker reads it by default and accepts a generated JSON path as an optional argument. A second, independently written standard-library implementation is [scripts/compute_p5_residual_independent.py](../scripts/compute_p5_residual_independent.py).

## 3. A Frobenius lift regular at the Weierstrass endpoints

Work in the finite free Z₅-algebra Z₅[x]/(f⁵). Modulo 5, f=x⁶+1 and f⁵=x³⁰+1. The polynomial H₀=x⁵ satisfies f(H₀)=0 in this algebra modulo 5, and

    f′(H₀)≡x²⁵ modulo (5,f⁵)

is a unit, with inverse −x⁵. Hensel's lemma therefore supplies a unique root H of f in this algebra with H≡x⁵ modulo 5. Choose its polynomial representative of degree at most 29. Then, exactly over Z₅[x],

    f(H)=f⁵ U,   U≡1 modulo 5.                    (4)

Differentiating (4), and using that f′(H) is a unit modulo f⁴, shows f⁴ divides H′. Put

    P=H′/f⁴.

Then deg U≤144, deg P≤4, and P is divisible by 5. Uniqueness and the evenness of f show H is odd, U is even, and P is even.

On an affine dagger neighborhood the formulas

    φ(x)=H(x),   φ(y)=y⁵ U(x)^{1/2}               (5)

define a Frobenius lift. The square root is the binomial series congruent to 1 modulo 5. Since U−1 has coefficients divisible by 5 and bounded polynomial degree, the series is overconvergent on a neighborhood of the affine unit region. No extension to either point at infinity is required.

This lift fixes W₋ and W₊. At x=±i, equation (4) says H(±i) is a root of f, and its reduction agrees with (±i)⁵=±i. The root is simple modulo 5, so Hensel uniqueness gives H(±i)=±i. The y-coordinate in (5) is zero there.

Thus the Frobenius pullbacks and all primitives below are regular at the actual endpoints. There is no ramified boundary-point construction and no call to an implementation restricted to non-Weierstrass points.

## 4. Polynomial Frobenius pullbacks and horizontal reduction

Direct differentiation gives

    φ*ν_j=B_j(x)ν₀,
    B_j=H^j f² P U^{-1/2}.                        (6)

Expand U^{-1/2}=Σ_{n≥0} binom(−1/2,n)(U−1)^n. The n-th polynomial term B_{j,n} has coefficient valuation at least n+1 and degree at most

    D_n=132+144n.                                  (7)

The binomial coefficients are 5-integral, as they equal (−1)^n binom(2n,n)/4^n. The extra factor of 5 in (7) comes from P.

For any polynomial g there is a unique decomposition

    gν₀=d(yK)+rν₀,
    g=2fK′+f′K+r,   deg r≤4.                      (8)

Applying (8) termwise gives

    φ*ν_i=dh_i+Σ_j M_ijν_j,   h_i=yK_i.            (9)

Only horizontal reduction is needed. Each K_i is a polynomial dagger series, hence regular at W₋ and W₊, and

    h_i(W₋)=h_i(W₊)=0.                            (10)

### Horizontal-reduction denominator bound

If g has integral coefficients and degree D, the coefficients of K and r in (8) belong to 5^{−L}Z₅, where

    L=floor(log₅(max(1,D−2))).                     (11)

Here is a proof covering the primitive as well as the cohomology coefficients. At infinity put z=1/x and y=z^{-3}v(z), where

    v(z)=sqrt(1−605z²−605z⁴+z⁶)∈Z₅[[z]]×.

Then ν₀=−z dz/(2v). The high-pole part of an antiderivative of gν₀ has terms q_k z^{-k} for 3≤k≤D−2. Their only integration denominators are k, so their valuations are at least −L. The term rν₀ contributes integrated poles of order at most two, and possibly a logarithm, none of which affects this high-pole part. Multiplying it by z³/v and retaining nonpositive powers of z recovers K without any additional denominator. Finally r=g−2fK′−f′K has the same bound.

This also gives an efficient independent reduction algorithm. If v^{-1}=Σ_l v_l z^l, then

    q_k=(1/(2k)) Σ_{j≥k+2}g_j v_{j−k−2},
    K_d=Σ_{k≥d+3}q_k v_{k−d−3}.                 (12)

Both sums are correlations and can be computed by two polynomial convolutions. Scaling by 5^L makes all divisions integral. The code verifies the complete polynomial identity in (8) modulo the working modulus, not just the final matrix entries.

Exact integer convolution uses Kronecker substitution with a radix strictly larger than every possible convolution coefficient. Thus it involves no floating-point or fixed-width-overflow assumption.

## 5. Single periods, third-kind forms and parity

Every ν_j is odd under the hyperelliptic involution, and its poles, if any, are at infinity, not at W₋ or W₊. Consequently

    ∫_{W₋}^{W₊}ν_j=0,  j=0,…,4.                 (13)

For ν₂ this includes a third-kind differential. The relevant fact is the odd-meromorphic differential lemma, which does not require second kind: fixing a logarithm branch, the hyperelliptic involution fixes both endpoints and negates the integral. See Balakrishnan–Bradshaw–Kedlaya, arXiv:1004.4936v2, Section 3.4, Lemma 1. The desired holomorphic answer is independent of that auxiliary logarithm branch; in the present regular-lift computation no logarithms occur in the correction integrals anyway.

The involution g(x,y)=(-x,y) has sign ε_j=(−1)^{j+1} on ν_j. It commutes with the regular Frobenius lift. Thus M splits into an even-index block M_e on indices (0,2,4) and an odd-index block M_o on (1,3). The code verifies these zero patterns and the corresponding parity of K_i.

Let D_ik=∫_{W₋}^{W₊}ν_iν_k. Path reversal, g-parity and shuffle with (13) imply D_ik=0 for equal parities and D_ki=−D_ik for opposite parities. There are only six unknowns, ordered as

    (0,1), (0,3), (2,1), (2,3), (4,1), (4,3).      (14)

## 6. Exact Frobenius equation and polynomial right-hand side

Because φ fixes both endpoints, expanding the double integral of (9), using (10) and (13), gives

    D_ik=Σ_{l,m}M_il M_km D_lm+C_ik,

    C_ik=∫ h_k dh_i
          +Σ_l M_il∫ h_kν_l−Σ_m M_km∫ h_iν_m.    (15)

There are no endpoint correction terms. Every remaining integrand is polynomial in x. Writing m_i(x)=Σ_j M_ijx^j and h_i=yK_i, equation (8) simplifies (15) to

    C_ik=(1/2)∫_{−i}^{i}[K_k B_i−K_i m_k]dx.     (16)

For an even-index i and odd-index k the bracketed polynomial is even. Define the rational endpoint functional

    T(Σ_n c_nx^n)=Σ_{m≥0} c_{2m}(−1)^m/(2m+1).

Then C_ik/i=T(K_k B_i−K_i m_k). This uses only Q₅ arithmetic: no numerical square root of −1 and no ramified extension are needed.

If c is the vector of these six normalized right-hand sides and z the vector of D_ik/i, then

    (I₆−M_e⊗M_o)z=c.                            (17)

As an independent structural check, the characteristic polynomials are

    char(M_e)=(T−5)(T²+5),   char(M_o)=T²+5.

The factor T−5 is the residue-at-infinity direction of the even-degree affine basis; both elliptic reductions over F₅ have Frobenius trace exactly zero. Hence

    det(I₆−M_e⊗M_o)=(1−25)²(1+125)=72576,

a 5-adic unit. The code also verifies invertibility directly in the computed matrix, so the certificate does not depend solely on this structural check.

## 7. Error bound: twenty terms suffice modulo 5⁷

Write L_n=floor(log₅(130+144n)). By (7) and (11), the matrix and primitive contribution of term n has valuation at least

    n+1−L_n.                                      (18)

For every n≥20 this is at least 17. For example 130+144·20=3010<5⁵, and the left side grows by a factor less than 5 at each subsequent integer, proving 130+144n<5^{n−15}.

For a bilinear term indexed by n,m in (16), put s=n+m. Its degree is at most 259+144s, and the endpoint integration introduces at most floor(log₅(260+144s)) additional denominators. A uniform conservative valuation bound is

    s+2−3 floor(log₅(260+144s)).                   (19)

Every omitted product has s≥20. For s between 20 and 106 the floor in (19) is 5 and the bound is at least 7. At subsequent logarithmic breakpoints the exponential growth of 5^j dominates 3j; explicitly, for j≥6, 5^j≥144(3j+5)+260, so s≥(5^j−260)/144 implies s+2−3j≥7. Therefore the entire omitted right-hand side is O(5⁷). The number of terms of a given total index does not worsen a non-Archimedean valuation bound.

For completeness, the same proof can be sharpened without numerical estimation. Put L_s=floor(log₅(130+144s)), J_s=floor(log₅(260+144s)), and P(s)=(130+144s)²(260+144s). The unweakened bilinear bound is s+2−L_n−L_m−J_s≥s+2−2L_s−J_s. One has P(20)=28,448,714,000<5¹⁵=30,517,578,125 and P(s+1)/P(s)≤(21/20)³<5 for s≥20. Thus P(s)<5^{s−5}, giving 2L_s+J_s≤s−6 and an O(5⁸) right-hand-side tail. We continue to report only seven digits.

For the finite computation, take coefficient precision N=30. The theoretical degree of a truncated B_i is at most 2868, so L=4. Products in (16) have degree at most 5731; polynomial integration loses at most five digits. The scaled horizontal identity is checked coefficientwise modulo 5³⁰. Applying the proved operator bound to its residual error certifies K_i and M_ij to at least 5²². Even the conservative propagation allowing another four digits for multiplication by a primitive and five for endpoint integration leaves finite right-hand-side error O(5¹³), far smaller than the required O(5⁷).

The finite computed M and c are integral; this is explicitly checked after removing their known scaling powers. The computed system determinant is a unit. The true M differs by O(5¹⁷), and the true c by O(5⁷), so both the computed and true system matrices have integral inverses. The identity

    z−z₀=A^{-1}[(c−c₀)−(A−A₀)z₀]

now proves z=z₀+O(5⁷). This is the certification argument. Agreement at larger precision is supplementary, not its substitute.

## 8. Readable arithmetic certificate

All following entries are modulo 78125=5⁷. With rows and columns indexed 0 through 4, the computed Frobenius matrix is

    [22285,     0, 25800,     0,  5080]
    [    0, 22285,     0,  2540,     0]
    [27935,     0, 64880,     0, 23675]
    [    0, 53188,     0, 55840,     0]
    [  369,     0,   225,     0, 69090].

The normalized right-hand side c, in order (14), is

    [43275, 49005, 51500, 18218, 17316, 51249].

Solving (17) gives

    z=[21625, 13695, 57225, 77593, 71316, 65694].

Multiplying the displayed matrix I₆−M_e⊗M_o by this vector verifies the displayed right-hand side modulo 78125. Its determinant is 72576 modulo 78125, hence 1 modulo 5. The first coordinate is

    21625=3·5³+4·5⁴+5⁵+5⁶,

which proves (1) and its exact valuation. The JSON certificate includes the expanded six-by-six matrix as well.

Independent checks: another original implementation, written before reading this script, reproduced all twenty-five Frobenius entries and all six periods. A separate review read and executed both implementations and checked the theoretical bounds with D*=2868, L*=4 and J*=5, rather than the smaller effective degrees after modular trimming. The review also checked the outer-first sign, differential factor two, endpoint fixing, affine fifth differential and parity closure. Runs with twenty and thirty binomial terms and substantially larger coefficient precision agree to the certified modulus and beyond. Neither agreement check is used in place of Section 7.

## 9. Relation to the preceding mathematical results

The connection from this holomorphic integral to δ is established in [the holomorphic residual test](holomorphic_residual_test.md): the relative central class W₋→W₊ is 2δ; its pure holomorphic length-two coordinate has no Hodge correction and annihilates the two Tate center summands. Therefore nonzero (2) detects the genuinely residual Sym² direction.

The global non-CM gluing theorem and the actual local-image computations then give the stated exclusion of W₊ and W₋. The result is not merely nonvanishing of a global twisted class, and is not another scalar-height test. It computes a nonzero crystalline local period.
