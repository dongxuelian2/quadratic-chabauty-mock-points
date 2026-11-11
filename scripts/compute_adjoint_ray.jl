# Hecke/Nemo alternative to the PARI class-group calculation.
# julia --project=<environment containing Hecke> scripts/compute_adjoint_ray.jl
# ADJOINT_FIELD_ONLY=1 stops after exact field and involution checks.
# ADJOINT_CONDITIONAL_ONLY=1 stops before unconditional certification.
# ADJOINT_FACTOR_BOUND overrides Hecke's default factor-base bound.
using Hecke

function adjoint_field()
    Qx, x = polynomial_ring(QQ, :x)
    g = x^5 - 1574680*x^2 + 2362020*x + 198368738320
    # g(sqrt(5)-x) = A(x) + B(x)*sqrt(5).
    A = -x^5 - 50*x^3 - 1574680*x^2 - 2362145*x + 198360864920
    B = 5*x^4 + 50*x^2 + 3149360*x + 2362045
    K, a = number_field(A^2 - 5*B^2, :a)
    gamma = -evaluate(A, a) / evaluate(B, a)
    beta = gamma-a
    @assert gamma^2 == 5 && evaluate(g, beta) == 0
    sigma = hom(K, K, a-2*gamma)
    @assert sigma(gamma) == -gamma && sigma(beta) == beta
    @assert sigma(sigma(a)) == a && sigma(a) != a
    O = maximal_order(K)
    expected = ZZ(2)^16 * ZZ(5)^11 * ZZ(7)^4 * ZZ(19)^4 * ZZ(37)^4 * ZZ(39367)^8
    @assert discriminant(O) == expected
    println("EXACT_FIELD_DISCRIMINANT=", discriminant(O))
    println("EXACT_QUINTIC_SUBFIELD_AND_INVOLUTION_VERIFIED")
    flush(stdout)
    return K, O, sigma
end

function ray_dimension(O, sigma; grh=true)
    modulus = ideal(O, ZZ(5)^3 * 2 * 7 * 19 * 37 * 39367)
    R, mR = ray_class_group(modulus; n_quo=5, GRH=grh)
    @assert all(5*r == zero(R) for r in gens(R))
    tau = Hecke.induce_action(mR, [sigma])[1]
    @assert all(tau(tau(r)) == r for r in gens(R))
    # The kernel of tau+1 on an elementary 5-group is the minus space.
    minus, _ = kernel(tau + id_hom(R))
    n = order(minus)
    d = 0
    while n > 1
        @assert is_divisible_by(n, 5)
        n = divexact(n, 5)
        d += 1
    end
    println(grh ? "RAY_GROUP_CONDITIONAL=" : "RAY_GROUP_CERTIFIED=", R)
    println(grh ? "RAY_ORDER_CONDITIONAL=" : "RAY_ORDER_CERTIFIED=", order(R))
    println(grh ? "ANTI_DIMENSION_CONDITIONAL=" : "CERTIFIED_UNRESTRICTED_ADJOINT_DIMENSION=", d)
    flush(stdout)
    return d
end

function main()
    println("HECKE_VERSION=", pkgversion(Hecke))
    K, O, sigma = adjoint_field()
    haskey(ENV, "ADJOINT_FIELD_ONLY") && return
    set_verbosity_level(:ClassGroup, 1)
    set_verbosity_level(:UnitGroup, 1)
    # Expose the known order-two symmetry to Hecke's relation collector.
    auts = automorphism_list(K)
    @assert length(auts) == 2 && any(t(a) == sigma(a) for t in auts for a in [gen(K)])
    println("START_CLASS_GROUP_WITH_AUTOMORPHISMS")
    flush(stdout)
    bound = parse(Int, get(ENV, "ADJOINT_FACTOR_BOUND", "-1"))
    @assert bound == -1 || bound > 0
    println("FACTOR_BOUND=", bound == -1 ? "Hecke default" : string(bound))
    flush(stdout)
    C, _ = class_group(O; GRH=true, use_aut=true, bound=bound)
    println("CLASS_GROUP_CONDITIONAL=", C)
    println("CLASS_NUMBER_CONDITIONAL=", order(C))
    flush(stdout)
    d = ray_dimension(O, sigma; grh=true)
    haskey(ENV, "ADJOINT_CONDITIONAL_ONLY") && return
    println("START_UNCONDITIONAL_CLASS_AND_UNIT_CERTIFICATION")
    flush(stdout)
    # ray_class_group(GRH=false) certifies both class group and units,
    # then recomputes the quotient; no cached conditional dimension is promoted.
    certified_d = ray_dimension(O, sigma; grh=false)
    @assert d == certified_d
    println("Finite/crystalline local conditions and target comparison remain separate.")
end

if abspath(PROGRAM_FILE) == abspath(@__FILE__)
    main()
end
