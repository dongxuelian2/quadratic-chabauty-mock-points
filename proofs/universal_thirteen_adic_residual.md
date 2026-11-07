# A uniform residual obstruction at 13 and a six-disk classification

Status: complete and independently reviewed. All twelve period computations were reproduced with a separately written implementation, and the uniform precision and parameter-degree bounds, polynomial interpolation, scalar disk isolation, and full-depth-two consequences passed independent review.

## 1. Local period theorem

Let a∈9+13Z₁₃ and b=(a−9)/13. On

    C_a: y²=x⁶+a x⁴+a x²+1

put W±=(±i,0), i²=−1, and ν_j=x^j dx/(2y), 0≤j≤4. Use the canonical Frobenius-invariant Coleman path and the outer-first word convention. Define

    X_a=(1/i)∫_(W₋)^(W₊) ν₀ν₁.

**Uniform local theorem.** As an identity of restricted analytic functions in b,

    X_(9+13b)≡13²(9+10b+5b²) modulo13³             (1)

coefficientwise. Consequently

    v₁₃(X_a)=2  for every a∈9+13Z₁₃.              (2)

Indeed 9+10b+5b²=5(b+1)²+4 has discriminant −80≡−2 modulo13, and −2 is a nonsquare in F₁₃. Thus the polynomial is nonzero at every b∈Z₁₃. It is not asserted to be a unit of the full Tate algebra: its reduction has roots over a quadratic extension. The conclusion (2) is about Q₁₃-valued parameters.

No rationality, rank, or global Selmer hypothesis is needed for this local theorem.

## 2. General odd-prime regular Frobenius formulas

For an odd prime p and a monic degree-six polynomial f∈Z_p[x] whose reduction is squarefree, the finite free quotient Z_p[x]/(f^p) has a unique H lifting x^p with f(H)=0. The derivative f′(x^p) is a unit modulo (p,f^p), because f is squarefree modulo p. Unlike the special prime-five model, the initial inverse is obtained by a general polynomial Euclidean inverse; the shortcut −x⁵ is not used.

Choose deg H≤6p−1. Exact monic division and differentiation give

    f(H)=f^p V,  V≡1 modulo p,
    H′=f^(p−1)P,  deg P≤4,  P≡0 modulo p,
    deg V≤30p−6.

The last divisibility uses invertibility of f′(H) modulo f^(p−1). The lift

    φ(x)=H,  φ(y)=y^p sqrt(V)

is regular at finite Weierstrass points. At p=13 it fixes W± exactly, because i^13=i and the two simple branch roots have unique lifts in their disks. Its pullbacks are

    φ*ν_j=B_jν₀,
    B_j=H^j f^((p−1)/2)P V^(−1/2).

The n-th binomial term has coefficient valuation at least n+1 and degree at most

    D_n=27p−3+(30p−6)n.                             (3)

Horizontal reduction g=2fK′+f′K+m, deg m≤4, loses at most floor(log_p(max(1,deg g−2))) in both K and m. The proof is the same high-pole principal-part integration at infinity as in the [five-adic certificate](five_adic_residual_certificate.md): the only denominators are integers at most deg g−2, and multiplying by the integral inverse square-root series introduces no additional loss.

All five affine differentials, including the puncture direction, are retained. Their single periods between W± vanish by hyperelliptic oddness. Parity and shuffle reduce the double integrals to six pairs

    (0,1),(0,3),(2,1),(2,3),(4,1),(4,3).

Writing m_j=Σ_k M_jk x^k and letting M_e,M_o be the even- and odd-index blocks, the normalized vector z satisfies exactly

    (I₆−M_e⊗M_o)z=c,
    c_jk=T(K_kB_j−K_jm_k),
    T(Σ g_2r x^(2r))=Σ g_2r(−1)^r/(2r+1).          (4)

All primitive endpoint terms vanish because their primitives are yK_j. These are polynomial correction integrals; no missing Weierstrass boundary routine is assumed.

## 3. Certified precision at 13

Here D_n=348+384n. Put

    L_n=floor(log₁₃(346+384n)),
    J_s=floor(log₁₃(692+384s)).

Use twelve binomial terms n=0,…,11 and coefficients modulo13²⁴. Retain the theoretical bounds

    D*=4572,  L*=3,  J*=3,

even when modular trimming leaves a smaller effective degree or loss. The complete scaled horizontal polynomial congruence is checked. The operator bound therefore certifies finite K,M to 24−2L*=18 digits. In the quadratic correction, allowing one further primitive loss and the integration loss leaves finite error at least18−3−3=12 digits.

For n≥12 the matrix and primitive tails have valuation at least n+1−L_n≥10. To prove the correction tail uniformly, for s=n+m≥12 set

    P(s)=(346+384s)²(692+384s).

One has

    P(12)=130073214800<13¹⁰=137858491849,
    P(s+1)/P(s)≤(13/12)³<13.

Thus P(s)<13^(s−2), giving 2L_s+J_s≤s−3. Every correction term has valuation at least

    s+2−L_n−L_m−J_s≥s+2−2L_s−J_s≥5.

The infinite tails therefore contribute errors of at least ten digits to M and five to c. These are entire-series bounds, not precision-stabilization tests. The finite computation explicitly checks integrality and invertibility of the six-variable system. Its solution is certified modulo13⁵.

As a structural check, the special fiber has six points and the elliptic trace is4. The cross-system determinant is

    (p−1)²((p+1)²−t²)(1−pt+p³)
      =12²·180·2146=55624320≡11 modulo13.

The polynomial matrix computation below also checks invertibility over the parameter Tate algebra directly.

## 4. Parameter-degree control and twelve-node interpolation

Work first over Z₁₃[[v]], v=a−9, starting at the exact Hensel solution for a=9. The derivative matrix of the equation for H is integral and invertible at v=0. Thus H,V,P have integral formal v-coefficients. Substituting v=13b gives a gain of at least d in valuation for each b-degree-d coefficient. The independent divisibilities P,V−1∈13Z₁₃⟨b⟩ give

    v₁₃([b^d]B_(j,n))≥max(d,n+1).

The same degree gain holds for the integral inverse-square-root factors in horizontal reduction. Consequently

    v₁₃([b^d]K_(j,n)),v₁₃([b^d]m_(j,n))
       ≥max(d,n+1)−L_n,

    v₁₃([b^d]c_(n,m))
       ≥max(d,n+m+2)−L_n−L_m−J_(n+m).              (5)

The Gauss estimates from Section3 show convergence in Q₁₃⟨b⟩. For s=n+m<12 use L_n,L_m,J_s≤3. Every coefficient of b-degree at least twelve in M and c then lies in13³; the infinite tail already lies in13⁵. Thus M,c modulo13³ have degree at most eleven coefficientwise.

For Q(b)=∏_(j=0)^11(b−j), monic remainder is Gauss-norm nonincreasing and extends continuously to restricted analytic series. Therefore the high-degree13³-integral tail has a13³-integral remainder. Interpolating the entire functions at b=0,…,11 computes their low coefficients modulo13³. All interpolation denominators j!(11−j)! are13-adic units, so the five-digit sampled precision loses no digits.

The sample matrices and correction vectors are in [universal_p13_samples.json](../verification/universal_p13_samples.json). Exact rational interpolation has integral coefficients, proving M,c∈Z₁₃⟨b⟩ together with the high-degree bound. Their coefficientwise residues and the polynomial system are recorded in [universal_p13_polynomials.json](../verification/universal_p13_polynomials.json).

Modulo13, M is the constant matrix

    [0,0,0,0,0]
    [0,0,0,0,0]
    [0,0,0,0,0]
    [0,2,0,4,0]
    [1,0,5,0,4].

The resulting constant cross-system determinant is11 modulo13, a unit. Hence the inverse exists over the Tate algebra, by a geometric series around a constant matrix inverse.

Direct polynomial multiplication modulo2197=13³ verifies (4) with solution

    z=[1521+1690b+845b²,
       819+312b+1859b²,
       1859+1521b+676b²,
       2126+2080b+169b²,
       1381+1001b+1183b²,
       1696+2158b+845b²].                            (6)

The first entry is exactly13²(9+10b+5b²). This proves (1) coefficientwise, and the nonsquare discriminant proves (2).

For a=35, the independently reproducible five-digit value is X_35=56615+O(13⁵), with X_35/13²≡10 modulo13. The uniform statement does not rely on this one value.

## 5. Six scalar centers on a large integral residue family

Let a be an odd integer with

    a≡9 modulo13,  a not≡74 modulo169.              (7)

Put A=a−3 and E_a:Y²=X³+AX²−AX, P=(1,1). Use the fixed integral complement (X−2)dX/(2Y), the compatible primitive ζ and height λ, and

    ell=L(P), h=λ(P), Z=ζ(P), alpha=h/ell².

The first scalar rho has the same normalization as the earlier [six-disk theorem](five_adic_disk_isolation.md):

    f₁=(1+x²,y), f₂=(1+x⁻²,y/x³),
    rho=λ(f₁)−λ(f₂)−2log₁₃(x)−alpha L(f₁)²+alpha L(f₂)²,

with continuous extensions at the rational endpoints. For odd integral parameters h is also the global point height.

Here are exact quintuple identities proving the needed constants. Define

    ψ=(a³−8a²+8a+16)(a³−4a²+8a−16),
    N=a⁶−56a⁴+224a³−192a²−256a+256,
    Q=5a¹²−100a¹¹+856a¹⁰−3776a⁹+7296a⁸+4864a⁷
       −47104a⁶+56320a⁵+47104a⁴−98304a³−49152a²
       +65536a+65536,
    R=5a⁶−40a⁵+96a⁴−32a³−64a²−256.

Then

    ψ₅(P)=ψ,  t₅=t(5P)=−ψN/Q,
    U=ψ₅(P)/t₅=−Q/N,
    ell=L(t₅)/5,
    h=(2/25)(log₁₃(U)−B(t₅)),
    Z=ζ(t₅)/5−Dlogψ₅(P)/25,
    1/(5t₅)−Dlogψ₅(P)/25=−R/(5N).                 (8)

Here D=d/ω and Dψ₅(P)=−40a(5a³−24a²+16a+32). All identities follow by exact addition or division polynomials and are independently checkable by polynomial arithmetic.

For a=9+13b, N and Q are units modulo13. The expanded polynomial ψ=a⁶−12a⁵+48a⁴−96a³+128a²−256 is identically2 modulo3 as a function on the three integer residue classes. Thus ψ≠0 for every integer parameter under consideration, and s=v₁₃(t₅)=v₁₃(ψ)≥1 is finite. The formal bounds give L(t₅)−t₅∈13^(3s), B(t₅)∈13^(2s), and ζ(t₅)−1/t₅∈13^s.

Exact rational reduction gives

    U(9)≡56 modulo169,  U′(9)≡4 modulo13,
    U≡56+52b modulo169,
    log₁₃(U)/13≡8+b modulo13,
    h/13≡10−2b modulo13,
    Z≡5 modulo13.                                  (9)

Condition (7) is exactly b≠5 modulo13, so h has valuation one. Therefore ell is nonzero, v₁₃(ell)=s≥1, Z is integral, and v₁₃(alpha)=1−2s<0.

The already established all-orders endpoint argument applies at13: on either punctured finite endpoint disk,

    rho/(alpha x²)∈1+13Z₁₃.

Reciprocity handles infinity. On each Weierstrass disk with parameter y,

    rho/(alpha y²)≡−2/A² modulo13,

also a unit. These use the entire integral single- and double-primitive bounds, including all integration denominators; they are not finite Taylor tests.

An exhaustive reduction gives precisely (0,±1),(±5,0),∞± for a≡9 modulo13. These six disks exhaust C_a(Q₁₃). Thus the first scalar has exactly the four endpoint zeros and W± for every parameter satisfying (7). The omitted lift a≡74 modulo169 is not asserted to be a counterexample; this leading-height argument simply does not address it.

## 6. Full depth-two and rational-point consequences

Suppose (7) holds, and additionally

- a≡3 modulo16;
- E_a(Q) has rank one;
- every odd prime dividing a−3 is congruent to3 modulo4.

Non-CM is automatic: v₂(a+1)=2, an odd divisor of a+1 gives negative j-valuation, and the alternatives a=3,−5 do not satisfy these simultaneous conditions. The actual residual target is zero by the dyadic and odd bad-prime theorems. The first actual scalar target is zero, so the scalar containment and Section5 leave only six centers. The nonzero period (2) excludes W± by the holomorphic residual criterion and exact joint gluing. The rational endpoints give the reverse inclusion. Hence, under the established Mordell–Weil-abelian-image and actual-local-image convention,

    C_a(Q₁₃)₂=C_a(Q)
      ={(0,1),(0,−1),∞₊,∞₋}.                       (10)

The unconditional positive example a=35 satisfies every hypothesis. Its rank-one proof by the exact two-isogeny images of sizes4 and2 was supplied in the [uniform five-adic theorem](universal_five_adic_residual.md), and a−3=32 has no odd prime divisors. It also has a=9+13·2, so the omitted lift does not occur. Thus the same curve has complete four-point full-depth-two classifications at both5 and13.

Another already rank-certified example is a=−18269, where a−3=−32·571, 571≡3 modulo4, and 8·571−1=4567 is prime. Here a≡152 modulo169, not74. No infinitude of certified rank-one parameters is inferred.

For rational points alone, the weaker congruence a≡3 modulo8 suffices, with rank one and (7): the first scalar target is zero, and W± are not rational over Q. Thus C_a(Q) consists of the four endpoints even if some residual target is nonzero. The Q-automorphism (x,y)↦(−x,y) fixes the basepoint and preserves the Selmer conditions, so the full depth-two set is then exactly either these four points or these four together with both W±. Choosing between the two alternatives requires the residual target condition; full membership is not inferred from scalar membership.

## 7. Reproduction

From the repository root, regenerate all twelve five-digit certificates with:

    python scripts/compute_p13_parameter_periods.py --output verification/universal_p13_samples.json

The certified interface is restricted to p=13, a≡9 modulo13, twelve binomial terms, and coefficient precision at least24. It makes no certification claim for arbitrary primes or other residue classes. SymPy is used only for exact finite polynomial inversion and a six-by-six rational solve. No external research code is executed.

Run the standalone standard-library arithmetic and scalar checker with:

    python scripts/check_universal_p13_residual.py

This verifies the complete twelve-point interpolation certificate, all six polynomial equations, the nonsquare discriminant, theoretical precision constants, exact rational-function quintuple identities, every scalar leading residue, and the exhaustive reduction. The analytic tail and parameter bounds are proved in Sections3–4, not inferred from finite sampling.
