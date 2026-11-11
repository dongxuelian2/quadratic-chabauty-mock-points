# Regression: a=4+sqrt(5) and b=2a share the large prime ideal of norm 11.
# Their quotient contributes the exact principal relation (2).
using Hecke
Qx, x = polynomial_ring(QQ, :x)
K, a = number_field(x^2-5, :a)
O = maximal_order(K)
function context()
    c = Hecke.class_group_init(Hecke.NfFactorBase(O, 7); add_rels=false)
    c.B2 = 100
    return c
end
function feed(c)
    Hecke.class_group_add_relation(c, 4+a)
    Hecke.class_group_add_relation(c, 2*(4+a))
end
c = context()
feed(c)
@assert c.largePrimeCnt == 2
@assert c.largePrime_success == 0 && c.largePrime_no_success == 0
@assert c.rel_cnt == 0
println("REPRODUCED: old cache misses the repeated norm-11 prime ideal")

include("hecke_large_prime_patch.jl")
c = context()
feed(c)
@assert c.largePrimeCnt == 2 && c.largePrime_success == 1
@assert c.rel_cnt == 1
@assert length(c.R_gen) == 1
elt = evaluate(c.R_gen[1])
@assert elt == K(2)
row = c.M.bas_gens[1]
for j in eachindex(c.FB.ideals)
    @assert row[j] == valuation(elt,c.FB.ideals[j])
end
@assert prod(c.FB.ideals[j]^Int(row[j]) for j in eachindex(c.FB.ideals)) == ideal(O,elt)
Hecke.class_group_add_relation(c, 4+a)
@assert evaluate(c.R_rel[end]) == 1
@assert isempty(c.M.rel_gens[nrows(c.M.rel_gens)].pos)
println("PASS: repeated large prime produces the correct exact principal-ideal relation")
