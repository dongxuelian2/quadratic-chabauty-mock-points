# Opt-in workaround for Hecke 0.41.1's single-large-prime cache mismatch.
# Rel_add.jl looks up (prime, polynomial), but inserts only polynomial into
# a polynomial-keyed Dict. Keep a separate correctly typed per-context cache.
# The factored quotient must also combine exponents when its two bases agree.
# No installed package file is modified; every resulting relation still goes
# through Hecke's ordinary exact factorization and relation insertion.
using Hecke

function install_large_prime_workaround()
    pkgversion(Hecke) == v"0.41.1" || error("Workaround audited only for Hecke 0.41.1")
    isdefined(Hecke, :_qc_large_prime_cache) && return
    path = joinpath(pkgdir(Hecke), "src", "NumFieldOrd", "NfOrd", "Clgp", "Rel_add.jl")
    source = read(path, String)
    start = findfirst("function class_group_add_relation(clg::ClassGrpCtx{T}, a::AbsSimpleNumFieldElem, n::QQFieldElem", source)
    stop = findnext("function class_group_add_relation(clg::ClassGrpCtx{<:SMat", source, last(start)+1)
    body = source[first(start):prevind(source,first(stop))]
    @assert occursin("haskey(clg.largePrime, (r, i))", body)
    @assert occursin("clg.largePrime[i] = (a, n*nI)", body)
    @assert occursin("b = FacElem(Dict([(a,1), (lp[1],-1)]))", body)
    body = replace(body, "b = FacElem(Dict([(a,1), (lp[1],-1)]))" => "b = FacElem([a, lp[1]], ZZRingElem[1, -1])")
    body = replace(body, "clg.largePrime[" => "cache[")
    body = replace(body, "haskey(clg.largePrime," => "haskey(cache,")
    body = replace(body, "cache[i] = (a, n*nI)" => "cache[(deepcopy(r), deepcopy(i))] = (a, n*nI)")
    body = replace(body, "  if !fl\n" => "  cache = get!(() -> Dict{Tuple{ZZRingElem,ZZPolyRingElem},Tuple{AbsSimpleNumFieldElem,QQFieldElem}}(), _qc_large_prime_cache, clg)\n  if !fl\n"; count=1)
    Core.eval(Hecke, :(const _qc_large_prime_cache = IdDict()))
    Base.include_string(Hecke, body, "QC_Hecke_0.41.1_large_prime_workaround")
    println("HECKE_SINGLE_LARGE_PRIME_WORKAROUND_ENABLED")
end

install_large_prime_workaround()
