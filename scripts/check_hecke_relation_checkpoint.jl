using Hecke
include("hecke_relation_checkpoint.jl")
include("hecke_large_prime_patch.jl")
K,a=quadratic_field(5); O=maximal_order(K); automorphism_list(K)
c=Hecke.class_group_init(O,13;add_rels=false,use_aut=true,complete=false)
Hecke.class_group_add_relation(c,FacElem(Dict(K(2)=>ZZ(1))))
for b in [K(3),a,4+a]
 Hecke.class_group_add_relation(c,b)
end
write_relation_checkpoint(c,"build/test_relations.txt",13)
d,B=read_relation_checkpoint(O,"build/test_relations.txt")
@assert B==13 && rank(c.M)==rank(d.M)
@assert Hecke.check_index(c.M)==Hecke.check_index(d.M)
install_relation_checkpoints("build/test_relations_hook.txt",13)
Hecke.class_group_get_pivot_info(c)
@assert isfile("build/test_relations_hook.txt")
# Finish a fresh restored class-group calculation; no saved rank/index is trusted.
Hecke.set_attribute!(O,:ClassGrpCtx,d)
Hecke.class_group_via_lll(d)
G,_=class_group(O;do_lll=false,GRH=false)
@assert order(G)==1
println("CHECKPOINT_ROUNDTRIP_AND_UNCONDITIONAL_CLASS_GROUP_OK")
