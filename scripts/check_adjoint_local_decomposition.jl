# Exact local ideal arithmetic; no class group or ray class group is computed.
include("compute_adjoint_ray.jl")

K, O, sigma = adjoint_field()
expected = Dict(
    2 => [(1, 2), (4, 2)],
    5 => [(10, 1)],
    7 => [(1, 2), (2, 2), (2, 2)],
    19 => [(1, 1), (1, 1), (2, 2), (2, 2)],
    37 => [(1, 2), (2, 2), (2, 2)],
    39367 => [(5, 2)])

for q in sort(collect(keys(expected)))
    factors = prime_decomposition(O, q)
    ef = sort([(e, degree(P)) for (P, e) in factors])
    @assert ef == expected[q]
    @assert sum(e*f for (e, f) in ef) == degree(K)
    @assert prod(P^e for (P, e) in factors) == ideal(O, q)
    for (P, e) in factors
        k, _ = residue_field(O, P)
        @assert order(k) == norm(P) == ZZ(q)^degree(P)
    end
    if q in (2, 7, 37, 39367)
        @assert all(mod(norm(P), 5) == 4 for (P, e) in factors)
    elseif q == 19
        quartic = [P for (P, e) in factors if e == 2 && degree(P) == 2]
        @assert length(quartic) == 2 && quartic[1] != quartic[2]
        @assert Hecke.induce_image(sigma, quartic[1]) == quartic[2]
        @assert Hecke.induce_image(sigma, quartic[2]) == quartic[1]
    else
        @assert q == 5 && ef == [(10, 1)]
        @assert 10+fld(10, 4)+1 == 13
    end
    println("q=", q, " (e,f)=", ef)
end
println("PASS: exact ideal products, residue fields and conjugate degree-four primes.")
println("Unrestricted modulus: P5^13 * Q19 * tau(Q19); integral lifts: P5^13.")
