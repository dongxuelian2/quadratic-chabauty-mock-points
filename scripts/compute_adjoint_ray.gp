\\ Run from the repository root after mkdir -p build:
\\ gp -q -f scripts/compute_adjoint_ray.gp
\\ ADJOINT_FIELD_ONLY=1 checks only exact fields and the involution.
\\ PARI_ADJOINT_STACK overrides the default two-gigabyte stack cap.
\\ PARI_ADJOINT_C1 optionally changes the initial relation-factor-base bound.
\\ PARI_ADJOINT_NRPID=-1 selects random relations instead of small norms.
\\ PARI_ADJOINT_IDEX and PARI_ADJOINT_MAX_FACT tune small-norm enumeration.
\\ PARI_ADJOINT_THREADS and PARI_ADJOINT_WORKER_STACK control parallelism.
\\ ADJOINT_RESUME_CLASS resumes a completed v2 class checkpoint.
\\ Degree-ten unrestricted ray space only, not a finite Selmer group.
\\ The class-group stage may take a long time. Output remains conditional
\\ until the final certification succeeds; failures abort the script.
default(parisizemax,if(getenv("PARI_ADJOINT_STACK"),eval(getenv("PARI_ADJOINT_STACK")),2000000000));
default(threadsizemax,if(getenv("PARI_ADJOINT_WORKER_STACK"),eval(getenv("PARI_ADJOINT_WORKER_STACK")),256000000));
default(nbthreads,if(getenv("PARI_ADJOINT_THREADS"),eval(getenv("PARI_ADJOINT_THREADS")),8));
\\ writebin appends; read returns either one record or a vector of records.
load_adjoint_checkpoint(path)={
  my(saved=read(path));
  if(type(saved)!="t_VEC" || #saved==0,error("invalid checkpoint"));
  if(type(saved[1])=="t_VEC",saved=saved[#saved]);
  if(#saved!=3 || saved[1]!="adjoint-ray-v2",error("invalid checkpoint version"));
  saved;
}
compute_adjoint_ray()={
  my(f=x^5-1574680*x^2+2362020*x+198368738320);
  my(nf5=nfinit(f));
  if(nf5.disc!=2^8*5^5*7^2*19^2*37^2*39367^4,error("quintic discriminant"));
  my(C=polcompositum(f,x^2-5,1)[1], R=polredbest(C[1],1));
  my(oldroot=R[2], newroot=modreverse(oldroot), nf=nfinit(R[1]));
  if(nf.disc!=2^16*5^11*7^4*19^4*37^4*39367^8,error("degree-ten discriminant"));
  print("EXACT_FIELD_DISCRIMINANTS=",[nf5.disc,nf.disc]);
  if(subst(C[1],x,oldroot)!=0,error("invalid reduced-field embedding"));
  if(subst(lift(newroot),x,oldroot)!=Mod(x,R[1]),error("invalid inverse embedding"));
  my(oldaut=C[4]*C[2]-C[3]);
  my(aut=lift(subst(lift(subst(lift(newroot),x,oldaut)),x,oldroot)));
  if(subst(R[1],x,Mod(aut,R[1]))!=0,error("invalid automorphism"));
  if(subst(aut,x,Mod(aut,R[1]))!=Mod(x,R[1]),error("not an involution"));
  my(sqrt5=subst(lift(C[3]),x,oldroot), quintic=subst(lift(C[2]),x,oldroot));
  if(subst(lift(sqrt5),x,Mod(aut,R[1]))!=-sqrt5,error("quadratic action"));
  if(subst(lift(quintic),x,Mod(aut,R[1]))!=quintic,error("quintic action"));
  print("EXACT_INVOLUTION_VERIFIED");
  if(getenv("ADJOINT_FIELD_ONLY"),return());
  my(bnf);
  my(c1=if(getenv("PARI_ADJOINT_C1"),eval(getenv("PARI_ADJOINT_C1")),0));
  my(nrpid=if(getenv("PARI_ADJOINT_NRPID"),eval(getenv("PARI_ADJOINT_NRPID")),0));
  my(idex=if(getenv("PARI_ADJOINT_IDEX"),eval(getenv("PARI_ADJOINT_IDEX")),0));
  my(maxfact=if(getenv("PARI_ADJOINT_MAX_FACT"),eval(getenv("PARI_ADJOINT_MAX_FACT")),0));
  if(getenv("PARI_ADJOINT_DEBUG"),setdebug("bnf",1));
  if(getenv("ADJOINT_RESUME_CLASS"),
    my(saved=load_adjoint_checkpoint(getenv("ADJOINT_RESUME_CLASS")));
    if(saved[1]!="adjoint-ray-v2" || saved[2].pol!=R[1] || saved[3]!=aut,error("incompatible checkpoint"));
    bnf=saved[2]; print("RESUMED_CLASS_GROUP"),
    print("START_CLASS_GROUP nrpid=",nrpid," threads=",default(nbthreads));
    bnf=bnfinit(nf,1,[c1,0,nrpid,maxfact,idex,default(nbthreads)]);
    writebin("build/adjoint_class_group_v2.bin",["adjoint-ray-v2",bnf,aut]);
  );
  print("CLASS_GROUP_CONDITIONAL=",bnf.cyc);
  my(bnr=bnrinit(bnf,5^3*2*7*19*37*39367,1,5));
  print("RAY_QUOTIENT_CONDITIONAL=",bnr.cyc);
  if(vecprod(bnr.cyc)!=5^(#bnr.cyc),error("ray quotient is not elementary"));
  my(G=bnrgaloismatrix(bnr,aut), r=#bnr.cyc);
  if(Mod(G*G-matid(r),5)!=0*G,error("ray action is not an involution"));
  my(d=matsize(matker(Mod(G+matid(r),5)))[2]);
  print("ANTI_DIMENSION_CONDITIONAL=",d);
  writebin("build/adjoint_ray_space_v2.bin",["adjoint-ray-v2",bnf,bnr,aut,G]);
  print("START_UNCONDITIONAL_CERTIFICATION");
  if(bnfcertify(bnf)!=1,error("class group not certified"));
  print("CERTIFIED_UNRESTRICTED_ADJOINT_DIMENSION=",d);
  print("Finite/crystalline local conditions and target comparison remain separate.");
}
iferr(compute_adjoint_ray(), E, print("FAILED: ",E); quit(1));
quit;
