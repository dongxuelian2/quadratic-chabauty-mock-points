"""Parameterized finite Frobenius certificate.
The uniform analytic bounds from the fixed certificate apply; comparisons
between parameter samples alone are not a proof of uniform nonvanishing.
"""
from compute_p5_residual import *
import argparse
from pathlib import Path
def compute(a,cutoff=20,W=30,verbose=False):
    assert a % 5 == 0, "The certified family requires a divisible by 5."
    assert cutoff == 20 and W >= 30, "The published seven-digit certificate uses T=20 and N>=30."
    t0=time.time();q=5**W;f=[1,0,a,0,a,0,1]
    H,U,PP=regular_lift(f,W,q)
    if verbose: print('regular lift verified',len(H)-1,len(U)-1,len(PP)-1,'seconds',time.time()-t0,flush=True)
    E=sub(U,[1],q);Epow=[1];V=[0]
    for n in range(cutoff):
        c=(-1)**n*math.comb(2*n,n)*pow(4,-n,q)%q
        V=add(V,scale(Epow,c,q),q)
        Epow=mul(Epow,E,q)
    base=mul(mul(power(f,2,q),PP,q),V,q)
    B=[];Hpow=[1]
    for j in range(5):
        B.append(mul(Hpow,base,q));Hpow=mul(Hpow,H,q)
    maxD=max(map(len,B))-1
    iv=invsqrt_series([1,0,a,0,a,0,1],maxD+1,q)
    if verbose: print('binomial cutoff',cutoff,'max degree',maxD,'seconds',time.time()-t0,flush=True)
    data=[horizontal(g,f,iv,q,W) for g in B]
    L=max(z[2] for z in data);sc=5**L
    Ks=[scale(K,5**(L-l),q) for K,r,l in data]
    Ms=[scale(r,5**(L-l),q)+[0]*(5-len(r)) for K,r,l in data]
    if verbose: print('horizontal verified','L',L,'min M scaled valuation',min(vp(c) for row in Ms for c in row),'seconds',time.time()-t0,flush=True)
    # g parity and expected cohomological characteristic polynomials.
    for j in range(5):
        assert all(c==0 for n,c in enumerate(Ks[j]) if (-1)**n != (-1)**(j+1))
        assert all(c==0 for k,c in enumerate(Ms[j]) if (j-k)%2)
    ei=[0,2,4];oi=[1,3];pairs=[(i,k) for i in ei for k in oi]
    rhs=[];Js=[]
    for i,k in pairs:
        r=sub(scale(mul(Ks[k],B[i],q),sc,q),mul(Ks[i],Ms[k],q),q)
        c,J=functional_scaled(r,q);rhs.append(c);Js.append(J)
    J=max(Js);rhs=[c*5**(J-j)%q for c,j in zip(rhs,Js)]
    Q=[]
    for row,(i,k) in enumerate(pairs):
        Q.append([((sc*sc if row==col else 0)-Ms[i][l]*Ms[k][m])%q for col,(l,m) in enumerate(pairs)])
    mat=sp.Matrix(Q);rhsM=sp.Matrix(rhs)
    det=mat.det();dval=vp(det)
    if verbose: print('six-by-six determinant valuation',dval,'expected',12*L,'seconds',time.time()-t0,flush=True)
    assert all(c % sc == 0 for row in Ms for c in row)
    assert all(c % (sc*sc*5**J) == 0 for c in rhs)
    amat=mat.applyfunc(lambda x: x//(sc*sc))
    bvec=rhsM.applyfunc(lambda x: x//(sc*sc*5**J))
    assert vp(amat.det())==0
    sol=amat.inv()*bvec
    mod=5**7
    if verbose: print('M mod5^7:',[[int(c//sc)%mod for c in row] for row in Ms],flush=True)
    def rr(x):
        nn,dd=map(int,sp.fraction(x));return nn*pow(dd,-1,mod)%mod
    if verbose: print('All cross values mod5^7:',[rr(x) for x in sol],flush=True)
    certificate={'parameter_a':a,'p':5,'term_cutoff':cutoff,'coefficient_precision':W,
      'theoretical_degree_bound':132+144*(cutoff-1),'effective_degree':maxD,
      'horizontal_scale_exponent':L,'integration_scale_exponent_used':J,
      'pairs':[list(z) for z in pairs],'modulus':mod,
      'frobenius_matrix':[[int(c//sc)%mod for c in row] for row in Ms],
      'system_matrix':[[int(amat[i,j])%mod for j in range(6)] for i in range(6)],
      'system_rhs':[int(z)%mod for z in bvec],
      'normalized_cross_periods':[rr(z) for z in sol],
      'normalized_target':rr(sol[0]),'odd_model_target_J':2*rr(sol[0])*pow(a-3,-1,mod)%mod,
      'system_determinant_mod5':int(amat.det())%5,
      'status':'Finite arithmetic certificate; analytic certification is Section 7 of proofs/five_adic_residual_certificate.md.'}

    if verbose: print('Normalized target modulo5^7:',rr(sol[0]),flush=True)
    if verbose: print('Odd-model target J modulo5^7:',2*rr(sol[0])*pow(a-3,-1,mod)%mod,flush=True)
    Dstar=132+144*(cutoff-1)
    Lstar=log5floor(Dstar-2);Jstar=log5floor(2*Dstar-4)
    if verbose: print('Theoretical bounds:',{'D':Dstar,'L':Lstar,'J':Jstar,'finite_error_exponent':W-3*Lstar-Jstar},flush=True)
    if verbose: print('Analytic tail justification: companion proof, Section7. Seconds=',time.time()-t0,flush=True)
    return certificate

if __name__=='__main__':
    parser=argparse.ArgumentParser(description="Compute certified seven-digit parameter samples; no output file is overwritten unless --output is supplied.")
    parser.add_argument('parameters', nargs='*', type=int, help='Parameters a divisible by 5; default: a=5b-5 for b=0,...,15.')
    parser.add_argument('--output', type=Path, help='Explicit destination for the JSON certificates.')
    args=parser.parse_args()
    values=args.parameters or [5*b-5 for b in range(16)]
    certificates=[]
    for a in values:
        certificate=compute(a)
        certificate['b']=(a+5)//5
        certificates.append(certificate)
        print('a=',a,'b=',certificate['b'],'X mod5^7=',certificate['normalized_target'],flush=True)
    if args.output:
        args.output.write_text(json.dumps(certificates,indent=2)+'\n')
        print('Wrote',args.output)
