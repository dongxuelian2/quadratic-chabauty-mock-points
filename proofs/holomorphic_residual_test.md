# A correction-free holomorphic double-integral test for the residual discrepancy

Status: independently reviewed proof and computational specification. No numerical value or nonvanishing assertion for the target integral is made.

## 1. The relative class removes the global reference

Retain the reciprocal curve, the good odd split prime p, the residual quotient U_R, and the canonical discrepancy of the residual-gluing theorem. Let W₊=(i,0), W₋=(−i,0), and let

    j_R,b(W₊)=δ*γ_p,   j_R,b(W₋)=−δ*γ_p.

The relative U_R path torsor from W₋ to W₊ has zero abelian cohomology class. Indeed

    div((x−i)/(x+i))=2W₊−2W₋,

so W₊−W₋ is a torsion divisor. Its rationalized abelian Kummer class is zero. Since H⁰(Q_p,H)=0, the trivial abelian torsor has a unique Galois-invariant trivialization. The relative path therefore has a well-defined central class

    ε_p∈H¹(Q_p,R).

Path composition and the free central action on the common abelian fiber give

    ε_p=δ_p(W₊)−δ_p(W₋)=2δ_p(W₊).             (1)

The previously proved crystalline central-difference property gives δ_p(W₊)∈H_f¹(Q_p,R). Equation (1) therefore proves ε_p∈H_f¹(Q_p,R). Ordinary H⁰-vanishing above establishes uniqueness, not crystallinity by itself.

One way to verify that no basepoint term is missing is to choose cocycles for the two b-based path torsors whose abelian cocycles agree. Their quotient is central and represents the difference in (1). Twisting by the W₋ torsor changes the action on the full group by inner automorphisms, but acts trivially on its center R. Thus the relative central class uses the same representation R as the original discrepancy. Neither a rational reference point of the curve with abelian class a₀ nor a de Rham coordinate for γ is required.

## 2. The holomorphic coordinate

Put

    ω₀=dx/y,   ω₁=x dx/y,
    I_p(a)=∫_{W₋}^{W₊} ω₀ω₁,                (2)

using the outer-first iterated-integral convention of Balakrishnan and Beacom. Both forms are globally holomorphic on the proper genus-two curve, including both points at infinity.

The single integrals between the two Weierstrass points vanish. This follows either from the torsion divisor or from the hyperelliptic involution, which fixes both endpoints and negates these forms. Shuffle therefore gives

    ∫ω₁ω₀=−I_p(a),   ∫ω₀ω₀=∫ω₁ω₁=0.        (3)

Hyperelliptic symmetry does NOT force I_p(a)=0: a length-two word of two odd forms is invariant, not anti-invariant. Balakrishnan's Corollary 7.13 and Example 7.14 explicitly distinguish these statements.

**Holomorphic-coordinate lemma.** Under the filtered de Rham comparison for the central class ε_p, there is a nonzero linear functional

    ℓ_hol:D_dR(R)/F⁰→Q_p

whose normalization by the commutator dual to ω₀,ω₁ gives

    ℓ_hol(log_BK ε_p)=I_p(a).                (4)

Reversing the path orientation or word-order convention changes a common sign; all integrals here use the canonical Frobenius-invariant Coleman path. In particular,

    I_p(a)≠0  ⇒  δ_p(W₊)≠0.                (5)

This is a sufficient residual test, not a two-scalar-height equation. A zero value of I_p(a) does not prove δ_p(W₊)=0, since the local residual finite space is two-dimensional and this tests one of its coordinates.

### Proof, including Hodge normalization

Choose a de Rham basis starting with the two holomorphic forms and let A₀,A₁ be their dual generators. The length-two holomorphic block of the logarithm of the de Rham Albanese map is

    ½ Σ_{k,l<2}(∫ω_kω_l)[A_k,A_l].          (6)

By (3), its coefficient at [A₀,A₁] is exactly I_p(a). The logarithmic correction from passing from the group-like signature to its logarithm consists of products of single integrals, which vanish here.

The key Hodge issue is that (6) has NO gauge or Hodge correction involving only holomorphic indices. Beacom, Proposition 5.7, gives (6) unchanged while placing all additional Hodge terms in brackets with at least one nonholomorphic index. Proposition 6.7 proves the same statement for a basepoint at infinity; its proof explicitly makes the holomorphic–holomorphic correction forms zero. The coordinate is therefore not obtained by dropping uncomputed correction terms.

Intrinsic explanation: the bar word built from two globally holomorphic forms is a closed length-two bar element of Hodge filtration F². Its reduced coproduct is the tensor product of the corresponding length-one holomorphic functions. Those functions vanish on F⁰ paths; consequently this coordinate is unchanged by the Hodge trivialization. On the zero-abelian fiber it is linear on the central Lie algebra. Completing the affine curve to the proper curve does not affect the word, because both forms extend globally; the surface relation is annihilated since the cup product of two holomorphic forms is zero.

The coordinate also annihilates the entire algebraic Tate center. The dual of Q_p(1) has Hodge filtration F¹ but F²=0. Strict compatibility of the inclusion Q_p(1)²→Z(U₂) with the filtration therefore makes every F² central functional vanish on the Tate summands. Thus the holomorphic coordinate descends to R. It vanishes on F⁰R and is nonzero on the remaining holomorphic commutator direction, proving the existence of ℓ_hol. This argument does not depend on a unit-root complement or on ordinary reduction.

The good-reduction Frobenius eigenvalues of R are not 1. Thus the Bloch–Kato exponential identifies D_dR(R)/F⁰ with H_f¹(Q_p,R); the central part of the unipotent comparison agrees with this identification. Applying it to the relative class gives (4). Equation (1) then proves (5).

Primary normalization source: J. Beacom, *Computation of the Unipotent Albanese Map on Elliptic and Hyperelliptic Curves*, arXiv:1711.03932v2, Propositions 5.7 and 6.7. https://arxiv.org/html/1711.03932v2 . The cited formulas separate the pure holomorphic block from all mixed correction terms. The intrinsic argument above explains why its projection to the proper residual quotient needs no extra correction.

## 3. A rational monic odd-degree model for the computation

Write A=a−3, and make the change of variables over Q_p

    X=2iA/(x+i),   Y=−4A² y/(x+i)³.         (7)

Then the equation becomes

    D_A: Y²=F_A(X),
    F_A(X)=(X−A)[X⁴−4AX³+(4A²−16A)X²+32A²X−16A³].  (8)

This is a MONIC degree-five polynomial with rational coefficients. The transformation sends W₋ to the single point at infinity and W₊ to (A,0). Both endpoints are consequently rational on D_A, even though the isomorphism (7) uses i.

Let Ω=dX/Y. Direct differentiation gives

    dx/y=−XΩ,
    x dx/y=i(X−2A)Ω.                        (9)

Using functoriality and the diagonal shuffle identity, the target (2) becomes

    I_p(a)=2iA J_p(A),
    J_p(A)=∫_{∞}^{(A,0)}(XΩ)Ω.              (10)

Indeed the other term is −i∫(XΩ)(XΩ)=−i/2(∫XΩ)²=0. Since A≠0, I_p(a) is nonzero exactly when J_p(A) is nonzero.

The forms Ω and XΩ are regular at infinity, so (10) is an ordinary proper-curve integral with an actual Weierstrass endpoint, not an undefined divergent integral. It can be computed via a tangential description if convenient; the pure holomorphic value is independent of that auxiliary tangent. Alternatively, use the ordinary Weierstrass-endpoint routines and endpoint correction formulas.

The polynomial identity and the differential pullbacks have been verified exactly with SymPy. No p-adic numerical calculation is used in this transformation.

## 4. Exact target for a=−605 and p=5

Take A=−608. Then

    F_A(X)=X⁵+3040X⁴+2967040X³+916766720X²
             +10788274176X+2186423566336.     (11)

The reduction modulo 5 is

    F_A(X)≡X⁵+X+1,

whose derivative is 1. Hence (11) is a good monic odd-degree model over Z₅. The target is precisely

    J₅(−608)=∫_{∞}^{(−608,0)} (X dX/Y)(dX/Y).  (12)

In the standard basis ν_j=X^j dX/(2Y), j=0,1,2,3, this is

    J₅(−608)=4∫_{∞}^{(−608,0)}ν₁ν₀.         (13)

The factor four and the word order are part of the specification. Choosing i≡2 modulo 5 fixes the sign in (10), but is unnecessary for deciding nonvanishing of J₅.

The finite endpoint has X≡2 modulo 5. Its derivative is exactly F_A'(A)=A⁴, a 5-adic unit. A convenient local parameter is Y, with

    X=A+Y²/A⁴+O(Y⁴).

At infinity use a standard odd-degree parameter such as t=X²/Y. The two endpoints lie in different residue disks. Therefore an expansion in only one disk, or a tiny double integral without the global Frobenius comparison, is insufficient.

## 5. What remains to calculate and certify

Balakrishnan's *Iterated Coleman integration for hyperelliptic curves* provides the applicable method: Algorithm 7.1 or 7.4 for the global Frobenius linear system, together with the Weierstrass-endpoint procedures of Section 7D (notably Algorithms 7.9 and 7.10) and path-composition corrections. https://msp.org/obs/2013/1-1/obs-v1-n1-p03-s.pdf

A certified computation of (12) needs:

1. The cohomological Frobenius matrix M and exact-reduction primitives h_j for φ*ν_j=dh_j+Σ_k M_jkν_k on (11).
2. The degree-two Frobenius correction constants or equivalent iterated-connection data. Single-integral Frobenius data alone do not determine the double periods.
3. The local expansions and boundary/intermediary endpoint corrections at infinity and (−608,0).
4. A rigorous absolute-error bound through reductions, divisions, the degree-two linear solve, and endpoint evaluation. An output J=c·5^m+O(5^{m+1}), c∈Z₅×, with that bound would prove nonvanishing. Merely increasing numerical precision is a useful check but not a replacement for an error bound.

The current local environment has SymPy but no SageMath, Magma, PARI/GP or an installed double-Coleman implementation. The verified work here supplies the exact model and target, not the missing Frobenius/iterated-reduction computation. No numerical value is asserted.

### Pinned implementation follow-up

The author's actual implementation is https://github.com/jbalakrishnan/AWS , pinned for this task to commit `43636f5725ba085b9f9614e613bbc4f685af3414`. Its README specifies SageMath 9.8 and warns that newer Sage releases can change genus-two Coleman results because the underlying Frobenius/Monsky–Washnitzer code changed. Use an isolated Sage 9.8 session with the repository's runtime patch, recording the exact version and commit. Do not silently substitute a current Sage release.

The verified method is `double_integrals_on_basis(P,Q)`, with row-major output index `4*i+j` in genus two. However its documented inputs are NON-Weierstrass points, and its source directly evaluates Frobenius reduction primitives at the endpoints. A direct call with infinity and (−608,0) is therefore NOT an executable solution of (12). A follow-up must first implement and verify the Weierstrass/boundary corrections from the cited paper, or obtain a separately verified implementation of those corrections. The desired corrected output is four times entry `4*1+0=4`.

There is an additional source-level issue to check before using its infinite-disk branch: that branch calls `tiny_double_integrals_on_basis_in_infinite_disc`, while the inspected file defines only the singular-coordinate method `tiny_double_integral_in_infinite_disc`; no definition of the former was found in the inspected source. The repository does provide ramified-extension and boundary-point helpers for single integration, but this does not establish a complete working double-integral endpoint path. Working on the original even-degree model with two finite boundary points could avoid this particular infinite-disk branch, provided the ramified-field backend and all endpoint corrections are independently verified.

Before evaluating the target, reproduce the author's non-Weierstrass regression example on y²=x³−4x+4 at p=5, endpoints (2,2) and (1,1), comparing the direct Frobenius and Teichmüller methods to the source's displayed residues. Then reproduce a genus-two example from the published paper and a genuine Weierstrass-to-Weierstrass example (such as Example 7.14) to test the newly supplied endpoint treatment. For the target, check shuffle, reversed-path transpose, all vanishing single integrals and agreement at higher working precision, alongside the rigorous error accounting already required above.

This is a concrete implementation-and-certification target, not a claim that stock Sage includes a suitable endpoint routine. No downloaded code has been executed in this work.

If (12) is certified nonzero, then δ₅(W₊)≠0 by (5), so both W₊ and W₋ fail the residual condition for a=−605, because all original actual residual targets are zero. If it is zero, the second residual coordinate still has to be evaluated before drawing any membership conclusion.

## 6. Scope

Established here: the relative class is 2δ; a correction-free holomorphic sufficient test; the exact odd-degree transformation; the exact 5-adic target and its good reduction; and the required computational inputs.

Not established here: a nonzero or zero value for J₅(−608), any general p-local nonvanishing theorem for the twisted global class, or full-depth-two exclusion of W for this example.
