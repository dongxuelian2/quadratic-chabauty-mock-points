\\ Run from the repository root after mkdir -p build:
\\ gp -q -f scripts/compute_adjoint_ray.gp
\\ ADJOINT_FIELD_ONLY=1 checks only exact fields and the involution.
\\ PARI_ADJOINT_STACK overrides the default two-gigabyte stack cap.
\\ PARI_ADJOINT_C1 optionally changes the initial relation-factor-base bound.
\\ Degree-ten unrestricted ray space only, not a finite Selmer group.
\\ The class-group stage may take a long time. Output remains conditional
\\ until the final certification succeeds; failures abort the script.
default(parisizemax,if(getenv("PARI_ADJOINT_STACK"),eval(getenv("PARI_ADJOINT_STACK")),2000000000));
default(nbthreads,8);
compute_adjoint_ray()={
  my(f=x^5-1574680*x^2+2362020*x+198368738320);
  my(nf5=nfinit(f));
  if(nf5.disc!=2^8*5^5*7^2*19^2*37^2*39367^4,error("quintic discriminant"));
  my(C=polcompositum(f,x^2-5,1)[1], nf=nfinit(C[1]));
  if(nf.disc!=2^16*5^11*7^4*19^4*37^4*39367^8,error("degree-ten discriminant"));
  print("EXACT_FIELD_DISCRIMINANTS=",[nf5.disc,nf.disc]);
  my(aut=lift(C[4]*C[2]-C[3]));
  if(subst(C[1],x,Mod(aut,C[1]))!=0,error("invalid automorphism"));
  if(subst(aut,x,Mod(aut,C[1]))!=Mod(x,C[1]),error("not an involution"));
  print("EXACT_INVOLUTION_VERIFIED");
  if(getenv("ADJOINT_FIELD_ONLY"),return());
  print("START_CLASS_GROUP");
  my(c1=if(getenv("PARI_ADJOINT_C1"),eval(getenv("PARI_ADJOINT_C1")),0));
  if(getenv("PARI_ADJOINT_DEBUG"),setdebug("bnf",1));
  my(bnf=bnfinit(nf,1,[c1,0,0,0,0,8]));
  writebin("build/adjoint_class_group.bin",[bnf,C]);
  print("CLASS_GROUP_CONDITIONAL=",bnf.cyc);
  my(bnr=bnrinit(bnf,5^3*2*7*19*37*39367,1,5));
  print("RAY_QUOTIENT_CONDITIONAL=",bnr.cyc);
  if(vecprod(bnr.cyc)!=5^(#bnr.cyc),error("ray quotient is not elementary"));
  my(G=bnrgaloismatrix(bnr,aut), r=#bnr.cyc);
  if(Mod(G*G-matid(r),5)!=0*G,error("ray action is not an involution"));
  my(d=matsize(matker(Mod(G+matid(r),5)))[2]);
  print("ANTI_DIMENSION_CONDITIONAL=",d);
  writebin("build/adjoint_ray_space.bin",[bnf,bnr,C,G]);
  print("START_UNCONDITIONAL_CERTIFICATION");
  if(bnfcertify(bnf)!=1,error("class group not certified"));
  print("CERTIFIED_UNRESTRICTED_ADJOINT_DIMENSION=",d);
  print("Finite/crystalline local conditions and target comparison remain separate.");
}
iferr(compute_adjoint_ray(), E, print("FAILED: ",E); quit(1));
quit;
