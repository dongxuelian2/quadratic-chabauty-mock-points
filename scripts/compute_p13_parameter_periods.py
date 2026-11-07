"""Certified prime-13 parameter periods using original regular-Frobenius arithmetic."""
import math, time, sys, json
import argparse
from pathlib import Path
import sympy as sp
P=13
INVERSE_SEED=None

def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def add(a,b,q):
    c=[0]*max(len(a),len(b))
    for j in range(len(c)):c[j]=((a[j] if j<len(a) else 0)+(b[j] if j<len(b) else 0))%q
    return trim(c)

def sub(a,b,q):return add(a,[(-x)%q for x in b],q)

def scale(a,c,q):return trim([(x*c)%q for x in a])

def mul(a,b,q,limit=None):
    if not a or not b:return [0]
    size=len(a)+len(b)-1
    if min(len(a),len(b))<12 or len(a)*len(b)<5000:
        c=[0]*size
        for i,x in enumerate(a):
            if x:
                for j,y in enumerate(b):
                    if limit is not None and i+j>=limit:break
                    c[i+j]+=x*y
        if limit is not None:c=c[:limit]
        return trim([x%q for x in c])
    # Exact Kronecker substitution, with a radix exceeding every convolution sum.
    bits=2*q.bit_length()+min(len(a),len(b)).bit_length()+1
    width=(bits+7)//8
    aa=int.from_bytes(b''.join(int(x%q).to_bytes(width,'little') for x in a),'little')
    bb=int.from_bytes(b''.join(int(x%q).to_bytes(width,'little') for x in b),'little')
    raw=(aa*bb).to_bytes(size*width,'little')
    if limit is not None:size=min(size,limit)
    return trim([int.from_bytes(raw[j*width:(j+1)*width],'little')%q for j in range(size)])

def power(a,n,q,limit=None):
    r=[1]
    while n:
        if n&1:r=mul(r,a,q,limit)
        n//=2
        if n:a=mul(a,a,q,limit)
    return r

def divmonic(a,b,q):
    a=list(a); d=len(b)-1
    if len(a)<=d:return [0],trim(a)
    out=[0]*(len(a)-d)
    for k in range(len(a)-1,d-1,-1):
        c=a[k]%q;out[k-d]=c
        if c:
            for j in range(d+1):a[k-d+j]=(a[k-d+j]-c*b[j])%q
    return trim(out),trim(a[:d] or [0])

def rem(a,g,q):return divmonic(a,g,q)[1]
def mmul(a,b,g,q):return rem(mul(a,b,q),g,q)
def mpow(a,n,g,q):
    r=[1]
    while n:
        if n&1:r=mmul(r,a,g,q)
        n//=2
        if n:a=mmul(a,a,g,q)
    return r

def eval_mod(coeff,H,g,q):
    r=[0]
    for c in reversed(coeff):r=add(mmul(r,H,g,q),[c%q],q)
    return r

def inv_mod(D,g,q,W):
    global INVERSE_SEED
    if INVERSE_SEED is None:
        x=sp.Symbol('x')
        dd=sp.Poly.from_list(list(reversed(D)),gens=x,modulus=P)
        gg=sp.Poly.from_list(list(reversed(g)),gens=x,modulus=P)
        ii=sp.invert(dd,gg)
        INVERSE_SEED=[int(ii.nth(j))%q for j in range(ii.degree()+1)]
    r=list(INVERSE_SEED); n=1
    while n<W:
        r=mmul(r,sub([2],mmul(D,r,g,q),q),g,q);n*=2
    assert rem(mmul(D,r,g,q),g,q)==[1]
    return r

def vp(n):
    n=int(n)
    if n==0:return 10**9
    v=0
    while n%P==0:n//=P;v+=1
    return v

def logpfloor(n):
    k=0
    while P**(k+1)<=max(1,n):k+=1
    return k

def invsqrt_series(F,n,q):
    r=[1];m=1;half=pow(2,-1,q)
    while m<n:
        m=min(2*m,n)
        r=scale(mul(r,sub([3],mul(F,mul(r,r,q,m),q,m),q),q,m),half,q)
    chk=mul(F,mul(r,r,q,n),q,n)
    assert chk==[1]
    return r

def regular_lift(f,W,q):
    g=power(f,P,q);H=[0]*P+[1];prec=1
    fp=[j*f[j] for j in range(1,len(f))]
    while prec<W:
        F=eval_mod(f,H,g,q);D=eval_mod(fp,H,g,q)
        H=sub(H,mmul(F,inv_mod(D,g,q,W),g,q),q);prec*=2
    assert eval_mod(f,H,g,q)==[0]
    FH=[0]
    for c in reversed(f):FH=add(mul(FH,H,q),[c%q],q)
    U,r=divmonic(FH,g,q);assert r==[0]
    Hd=[(j*H[j])%q for j in range(1,len(H))]
    PP,r=divmonic(Hd,power(f,P-1,q),q);assert r==[0]
    assert all(x%P==0 for x in PP)
    assert U[0]%P==1 and all(x%P==0 for x in U[1:])
    return H,U,PP

def horizontal(g,f,iv,q,W):
    D=len(g)-1;L=logpfloor(max(1,D-2));s=P**L
    if D<=4:return [0],scale(g,s,q),L
    corr=mul(list(reversed(g)),iv,q,limit=D-4)
    qs=[0]*(D-1)
    for k in range(3,D-1):
        den=2*k;v=vp(den);unit=den//P**v
        idx=D-k-2
        qs[k]=(corr[idx] if idx<len(corr) else 0)*P**(L-v)*pow(unit,-1,q)%q
    corr2=mul(list(reversed(qs)),iv,q,limit=D-4)
    K=[corr2[D-j-5] if D-j-5<len(corr2) else 0 for j in range(D-4)]
    dK=[j*K[j] for j in range(1,len(K))]
    fp=[j*f[j] for j in range(1,len(f))]
    LK=add(scale(mul(f,dK,q),2,q),mul(fp,K,q),q)
    r=sub(scale(g,s,q),LK,q)
    assert len(r)<=5,('horizontal failed',D,len(r),L)
    return trim(K),r,L

def functional_scaled(r,q):
    # P^J times sum r_(2m)*(-1)^m/(2m+1).
    J=logpfloor(len(r));total=0
    for n in range(0,len(r),2):
        den=n+1;v=vp(den);unit=den//P**v
        total=(total+(-1 if n//2%2 else 1)*r[n]*P**(J-v)*pow(unit,-1,q))%q
    return total,J

def rational_padic(x,prec=12):
    num,den=map(int,sp.fraction(x));v=vp(num)-vp(den)
    if num==0:return '0 (finite computation)'
    nu=num//P**vp(num);du=den//P**vp(den)
    unit=nu*pow(du,-1,P**prec)%(P**prec)
    return {'valuation':v,'unit_mod_ppower':unit,'unit_digits':prec}


def compute(a,prime=13,cutoff=12,W=24,verbose=False):
    assert prime == 13 and a % 13 == 9, "Certified mode requires p=13 and a=9 modulo13."
    assert cutoff == 12 and W >= 24, "Certified mode requires T=12 and N>=24."
    global P,INVERSE_SEED
    P=prime;INVERSE_SEED=None
    t0=time.time();q=P**W;f=[1,0,a,0,a,0,1]
    H,U,PP=regular_lift(f,W,q)
    if verbose: print('regular lift verified',len(H)-1,len(U)-1,len(PP)-1,'seconds',time.time()-t0,flush=True)
    E=sub(U,[1],q);Epow=[1];V=[0]
    for n in range(cutoff):
        c=(-1)**n*math.comb(2*n,n)*pow(4,-n,q)%q
        V=add(V,scale(Epow,c,q),q)
        Epow=mul(Epow,E,q)
    base=mul(mul(power(f,(P-1)//2,q),PP,q),V,q)
    B=[];Hpow=[1]
    for j in range(5):
        B.append(mul(Hpow,base,q));Hpow=mul(Hpow,H,q)
    maxD=max(map(len,B))-1
    iv=invsqrt_series([1,0,a,0,a,0,1],maxD+1,q)
    if verbose: print('binomial cutoff',cutoff,'max degree',maxD,'seconds',time.time()-t0,flush=True)
    data=[horizontal(g,f,iv,q,W) for g in B]
    L=max(z[2] for z in data);sc=P**L
    Ks=[scale(K,P**(L-l),q) for K,r,l in data]
    Ms=[scale(r,P**(L-l),q)+[0]*(5-len(r)) for K,r,l in data]
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
    J=max(Js);rhs=[c*P**(J-j)%q for c,j in zip(rhs,Js)]
    Q=[]
    for row,(i,k) in enumerate(pairs):
        Q.append([((sc*sc if row==col else 0)-Ms[i][l]*Ms[k][m])%q for col,(l,m) in enumerate(pairs)])
    mat=sp.Matrix(Q);rhsM=sp.Matrix(rhs)
    det=mat.det();dval=vp(det)
    if verbose: print('six-by-six determinant valuation',dval,'expected',12*L,'seconds',time.time()-t0,flush=True)
    assert all(c % sc == 0 for row in Ms for c in row)
    assert all(c % (sc*sc*P**J) == 0 for c in rhs)
    amat=mat.applyfunc(lambda x: x//(sc*sc))
    bvec=rhsM.applyfunc(lambda x: x//(sc*sc*P**J))
    assert vp(amat.det())==0
    sol=amat.inv()*bvec
    mod=P**5
    if verbose: print(f'M mod{P}^5:',[[int(c//sc)%mod for c in row] for row in Ms],flush=True)
    def rr(x):
        nn,dd=map(int,sp.fraction(x));return nn*pow(dd,-1,mod)%mod
    if verbose: print(f'All cross values mod{P}^5:',[rr(x) for x in sol],flush=True)
    certificate={'parameter_a':a,'p':P,'term_cutoff':cutoff,'coefficient_precision':W,
      'theoretical_degree_bound':27*P-3+(30*P-6)*(cutoff-1),'effective_degree':maxD,
      'horizontal_scale_exponent':L,'integration_scale_exponent_used':J,
      'pairs':[list(z) for z in pairs],'modulus':mod,
      'frobenius_matrix':[[int(c//sc)%mod for c in row] for row in Ms],
      'system_matrix':[[int(amat[i,j])%mod for j in range(6)] for i in range(6)],
      'system_rhs':[int(z)%mod for z in bvec],
      'normalized_cross_periods':[rr(z) for z in sol],
      'normalized_target':rr(sol[0]),'odd_model_target_J':2*rr(sol[0])*pow(a-3,-1,mod)%mod,
      'system_determinant_modp':int(amat.det())%P,
      'status':'Finite arithmetic certificate; analytic bounds are proved in proofs/universal_thirteen_adic_residual.md.'}

    if verbose: print(f'Normalized target modulo{P}^5:',rr(sol[0]),flush=True)
    if verbose: print(f'Odd-model target J modulo{P}^5:',2*rr(sol[0])*pow(a-3,-1,mod)%mod,flush=True)
    Dstar=27*P-3+(30*P-6)*(cutoff-1)
    Lstar=logpfloor(Dstar-2);Jstar=logpfloor(2*Dstar-4)
    if verbose: print('Theoretical bounds:',{'D':Dstar,'L':Lstar,'J':Jstar,'finite_error_exponent':W-3*Lstar-Jstar},flush=True)
    if verbose: print('Analytic tail justification: companion proof, Section7. Seconds=',time.time()-t0,flush=True)
    return certificate


if __name__=='__main__':
    parser=argparse.ArgumentParser(description="Compute certified five-digit prime-13 parameter samples.")
    parser.add_argument('parameters',nargs='*',type=int,help='Parameters a=9 modulo13; default: a=9+13b for b=0,...,11.')
    parser.add_argument('--output',type=Path,help='Explicit destination for JSON certificates; no file is written unless supplied.')
    args=parser.parse_args()
    samples=[]
    for a in args.parameters or [9+13*b for b in range(12)]:
        sample=compute(a);sample['b']=(a-9)//13;samples.append(sample)
        print('a=',a,'b=',sample['b'],'X mod13^5=',sample['normalized_target'],flush=True)
    if args.output:
        args.output.write_text(json.dumps(samples,indent=2)+'\n')
        print('Wrote',args.output)
