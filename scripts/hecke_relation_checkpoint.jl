# Exact relation export before costly HNF/index calculations. This is NOT a
# certified class group: a restored context must finish all ordinary checks.
using Hecke

function write_relation_checkpoint(c, path, bound)
    K = Hecke.nf(c)
    n = degree(K)
    relations = vcat(c.R_gen, c.R_rel)
    putcoeff(io, values) = println(io, join((string(numerator(v), " ", denominator(v)) for v in values), " "))
    mkpath(dirname(abspath(path)))
    open(path*".tmp", "w") do io
        println(io, "QC_RELATIONS_V1")
        println(io, n)
        putcoeff(io, [coeff(defining_polynomial(K),i) for i in 0:n])
        println(io, discriminant(Hecke.order(c)))
        println(io, bound)
        println(io, length(relations))
        for a in relations
            factors = a isa FacElem ? collect(a.fac) : [a => ZZ(1)]
            println(io, length(factors))
            for (b,e) in factors
                println(io, e)
                putcoeff(io, [coeff(b,i) for i in 0:n-1])
            end
        end
    end
    mv(path*".tmp",path;force=true)
    println("EXACT_RELATION_CHECKPOINT=",path," COUNT=",length(relations)," RANK=",rank(c.M))
    flush(stdout)
end

function read_relation_checkpoint(O, path)
    K = Hecke.nf(O)
    open(path) do io
        @assert readline(io) == "QC_RELATIONS_V1"
        n = parse(Int,readline(io))
        @assert n == degree(K)
        function getcoeff(count)
            v = split(readline(io))
            @assert length(v) == 2*count
            return [QQ(parse(ZZRingElem,v[2*i-1]),parse(ZZRingElem,v[2*i])) for i in 1:count]
        end
        @assert getcoeff(n+1) == [coeff(defining_polynomial(K),i) for i in 0:n]
        @assert parse(ZZRingElem,readline(io)) == discriminant(O)
        bound = parse(Int,readline(io))
        count = parse(Int,readline(io))
        c = Hecke.class_group_init(O,bound;add_rels=false,use_aut=true,complete=false)
        c.B2 = 1000*bound
        for _ in 1:count
            a = one(K)
            for _ in 1:parse(Int,readline(io))
                e = parse(Int,readline(io))
                a *= K(getcoeff(n))^e
            end
            # Re-factor the exact element, including all ideal valuations.
            # Duplicated or orbit-generated relations may already be present.
            Hecke.class_group_add_relation(c,a;integral=false)
        end
        @assert eof(io)
        c.expect = Hecke.class_group_expected(c,100)
        c.GRH = true
        println("RESTORED_UNCERTIFIED_RELATIONS=",count," RANK=",rank(c.M))
        return c,bound
    end
end

function install_relation_checkpoints(path, bound)
    @assert pkgversion(Hecke) == v"0.41.1"
    seen = IdDict()
    hook = function(c)
        count = length(c.R_gen)+length(c.R_rel)
        full = rank(c.M) == length(c.FB.ideals)
        oldcount,oldfull = get(seen,c,(-256,false))
        if count >= oldcount+256 || (full && !oldfull)
            write_relation_checkpoint(c,path,bound)
            seen[c] = (count,full)
        end
    end
    Core.eval(Hecke, :(_qc_checkpoint_hook = $hook))
    src = read(joinpath(pkgdir(Hecke),"src","NumFieldOrd","NfOrd","Clgp","Main_enum.jl"),String)
    start = findfirst("function class_group_get_pivot_info(clg::ClassGrpCtx)",src)
    stop = findnext("\nend",src,last(start)+1)
    body = src[first(start):last(stop)]
    body = replace(body,"  # Extract information" => "  _qc_checkpoint_hook(clg)\n  # Extract information";count=1)
    Base.include_string(Hecke,body,"QC_relation_checkpoint_before_index")
end
