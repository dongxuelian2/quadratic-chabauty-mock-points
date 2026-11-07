# A four-residue-disk family at 7

Status: independently reviewed proof. This supplements the separately reviewed eight-disk family; it does not assert any infinite rank-one family.

Let C_a:y²=x⁶+a x⁴+a x²+1 and E_a:Y²=X³+AX²−AX, A=a−3, with P=(1,1). Use the fixed complement (X−2)ω and the normalization of the prime-7 companion. Write ell=L(P), h=lambda(P), Z=zeta(P), alpha=h/ell². For odd a, h is the global height because all other local heights of P vanish.

## The theorem

For every odd integer a≡−605 modulo 49, the first scalar height has exactly the four zeros (0,±1),infinity_± in C_a(Q_7).

If also a≡3 modulo 8 and E_a(Q) has rank one, the full Mordell–Weil-restricted, actual-local-image depth-two set equals these four rational points. Thus a≡−605 modulo 392 is a sufficient combined progression, subject to rank one.

At a=−605 every hypothesis is independently arithmetic: A=−32·19, and 19 and 8·19−1=151 are primes with 19≡3 modulo 8. The reviewed prime-pair rank theorem therefore gives rank one. Consequently C_{−605}(Q_7)_2=C_{−605}(Q) is exactly the four endpoints.

## Exact base constants

At A=−608 the exact group law gives

    3P=(133968444289/135751718025,
        148737027213396287/50017041747721125),
    t_3=−134857133565/406366445311,
    psi_3(P)=−368445.

Both t_3 and psi_3 have valuation one. The exact derivative identity is Dpsi_3(P)=24, where D=d/omega. The normalized multiplication identities are

    ell=L(t_3)/3,
    h=(2/9)(log_7(psi_3/t_3)−B(t_3)),
    Z=zeta(t_3)/3−8/(3psi_3).

For t∈7Z_7 the proven formal bounds give L(t)−t∈7³Z_7, B(t)∈7²Z_7, and zeta(t)−1/t∈7Z_7. The last statement uses the fixed integral complement. The residue U=psi_3/t_3 is 36 modulo 49, and (U⁶−1)/7 is 2 modulo 7. Since log_7(U)=(1/6)log(1+(U⁶−1)), its omitted terms are in 49Z_7. Exact reduction yields

    ell/7 ≡4, h/7 ≡5, Z≡4, 7alpha≡6 modulo 7.

For the primitive, the rational principal part is

    1/(3t_3)−8/(3psi_3)=−1102915/1098051.

Thus v_7(ell)=v_7(h)=1, Z is integral, and v_7(alpha)=−1. These are finite residue certificates with the all-orders bounds explicitly stated; the accompanying script uses rational arithmetic only.

## Uniform parameter and disk bounds

If a≡−605 modulo 7^M, M≥2, the third-division numerators Phi_3 and Omega_3 remain units and psi_3 remains of valuation one. Hence

    Delta t_3 ∈7^M Z_7,
    Delta(psi_3/t_3)=Delta(−Omega_3/Phi_3)∈7^M Z_7.

The integral formal numerators and single-/double-integration denominator bounds give Delta ell and Delta h in 7^M Z_7, and Delta Z in 7^(M−2) Z_7. The possible two-power loss is from 1/t_3 and the derivative quotient Dpsi_3/psi_3; division by 3 or 9 loses no 7-adic precision. The bounds apply to every term of the convergent series, as in the prime-7 companion's parameter-continuity proof. For M=2 they preserve v_7(ell)=v_7(h)=1 and Z∈Z_7, hence alpha has valuation −1.

On either endpoint disk x∈7Z_7, coefficientwise integration and the formal bound

    v_7([t^(2k)]B) ≥ −v_7(2k)−floor(log_7(2k−1))

show that the finite-height variation and the regularized singular variation, divided by x², are integral after evaluation. The coefficients themselves need not be integral. The logarithms have the form ±ell+I and −J, with I/x² integral and J/x∈±1+7Z_7. Thus

    rho_a(x)/x² ∈ Z_7 + alpha(1+7Z_7),
    rho_a(x)/(alpha x²)∈1+7Z_7       for x≠0.

Here the cross term alpha·ell·I/x² is integral, and alpha·I²/x² has positive valuation. The displayed expression never vanishes. At x=0 the height is zero by h=alpha ell². Reciprocity proves the same isolation at infinity.

Every parameter in this family is 4 modulo 7. Direct enumeration gives only the affine residue points (0,1),(0,−1), together with the two infinity points. The model is smooth because a+1 and a−3 are units modulo 7. These four disks exhaust C_a(Q_7), proving the scalar equality.

Finally a≡3 modulo 8 gives first actual target {0} by the exact local-target theorem, without any restriction on a+1 multiplicities. Under rank one the established endpoint-basepoint containment supplies the full-depth-two inclusion; rational points give the reverse inclusion.

Dependencies: ../proofs/prime7_isolation.md for the uniform formal bounds, ../proofs/reciprocal_local_targets.md for the first target, ../proofs/endpoint_basepoint_bridge.md for containment, and ../proofs/checkable_rank_patterns.md for the concrete rank certificate. The proof has received independent review.
