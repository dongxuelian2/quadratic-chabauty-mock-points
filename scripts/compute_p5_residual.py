"""Original Python regular-Frobenius certificate computation.
No external research code is executed. The default T=20, N=30 calculation,
together with the explicit bounds in chabauty_five_adic_residual_certificate.md,
certifies the displayed residues modulo 5^7. No finer digits are asserted.
"""
import math, time, sys, json
import sympy as sp
P=5

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
    # Start in the actual residue algebra, including ordinary reductions.
    x=sp.symbols('x')
    poly=lambda a: sp.Poly.from_list(list(reversed(a)),x,modulus=5)
    inverse=sp.invert(poly(D),poly(g))
    r=[int(inverse.nth(i))%q for i in range(inverse.degree()+1)]
    assert rem(mmul(D,r,g,5),g,5)==[1]
    n=1
    while n<W:
        r=mmul(r,sub([2],mmul(D,r,g,q),q),g,q);n*=2
    assert rem(mmul(D,r,g,q),g,q)==[1]
    return r

def vp(n):
    n=int(n)
    if n==0:return 10**9
    v=0
    while n%5==0:n//=5;v+=1
    return v

def log5floor(n):
    k=0
    while 5**(k+1)<=max(1,n):k+=1
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
    g=power(f,5,q);H=[0]*5+[1];prec=1
    fp=[j*f[j] for j in range(1,len(f))]
    while prec<W:
        F=eval_mod(f,H,g,q);D=eval_mod(fp,H,g,q)
        H=sub(H,mmul(F,inv_mod(D,g,q,W),g,q),q);prec*=2
    assert eval_mod(f,H,g,q)==[0]
    FH=[0]
    for c in reversed(f):FH=add(mul(FH,H,q),[c%q],q)
    U,r=divmonic(FH,g,q);assert r==[0]
    Hd=[(j*H[j])%q for j in range(1,len(H))]
    PP,r=divmonic(Hd,power(f,4,q),q);assert r==[0]
    assert all(x%5==0 for x in PP)
    assert U[0]%5==1 and all(x%5==0 for x in U[1:])
    return H,U,PP

def horizontal(g,f,iv,q,W):
    D=len(g)-1;L=log5floor(max(1,D-2));s=5**L
    if D<=4:return [0],scale(g,s,q),L
    corr=mul(list(reversed(g)),iv,q,limit=D-4)
    qs=[0]*(D-1)
    for k in range(3,D-1):
        den=2*k;v=vp(den);unit=den//5**v
        idx=D-k-2
        qs[k]=(corr[idx] if idx<len(corr) else 0)*5**(L-v)*pow(unit,-1,q)%q
    corr2=mul(list(reversed(qs)),iv,q,limit=D-4)
    K=[corr2[D-j-5] if D-j-5<len(corr2) else 0 for j in range(D-4)]
    dK=[j*K[j] for j in range(1,len(K))]
    fp=[j*f[j] for j in range(1,len(f))]
    LK=add(scale(mul(f,dK,q),2,q),mul(fp,K,q),q)
    r=sub(scale(g,s,q),LK,q)
    assert len(r)<=5,('horizontal failed',D,len(r),L)
    return trim(K),r,L

def functional_scaled(r,q):
    # 5^J times sum r_(2m)*(-1)^m/(2m+1).
    J=log5floor(len(r));total=0
    for n in range(0,len(r),2):
        den=n+1;v=vp(den);unit=den//5**v
        total=(total+(-1 if n//2%2 else 1)*r[n]*5**(J-v)*pow(unit,-1,q))%q
    return total,J

def rational_padic(x,prec=12):
    num,den=map(int,sp.fraction(x));v=vp(num)-vp(den)
    if num==0:return '0 (finite computation)'
    nu=num//5**vp(num);du=den//5**vp(den)
    unit=nu*pow(du,-1,5**prec)%(5**prec)
    return {'valuation':v,'unit_mod_5power':unit,'unit_digits':prec}

def run(cutoff,W):
    t0=time.time();q=5**W;a=-605;f=[1,0,a,0,a,0,1]
    H,U,PP=regular_lift(f,W,q)
    print('regular lift verified',len(H)-1,len(U)-1,len(PP)-1,'seconds',time.time()-t0,flush=True)
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
    print('binomial cutoff',cutoff,'max degree',maxD,'seconds',time.time()-t0,flush=True)
    data=[horizontal(g,f,iv,q,W) for g in B]
    L=max(z[2] for z in data);sc=5**L
    Ks=[scale(K,5**(L-l),q) for K,r,l in data]
    Ms=[scale(r,5**(L-l),q)+[0]*(5-len(r)) for K,r,l in data]
    print('horizontal verified','L',L,'min M scaled valuation',min(vp(c) for row in Ms for c in row),'seconds',time.time()-t0,flush=True)
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
    print('six-by-six determinant valuation',dval,'expected',12*L,'seconds',time.time()-t0,flush=True)
    assert all(c % sc == 0 for row in Ms for c in row)
    assert all(c % (sc*sc*5**J) == 0 for c in rhs)
    amat=mat.applyfunc(lambda x: x//(sc*sc))
    bvec=rhsM.applyfunc(lambda x: x//(sc*sc*5**J))
    assert vp(amat.det())==0
    sol=amat.inv()*bvec
    mod=5**7
    print('M mod5^7:',[[int(c//sc)%mod for c in row] for row in Ms],flush=True)
    def rr(x):
        nn,dd=map(int,sp.fraction(x));return nn*pow(dd,-1,mod)%mod
    print('All cross values mod5^7:',[rr(x) for x in sol],flush=True)
    certificate={'parameter_a':a,'p':5,'term_cutoff':cutoff,'coefficient_precision':W,
      'theoretical_degree_bound':132+144*(cutoff-1),'effective_degree':maxD,
      'horizontal_scale_exponent':L,'integration_scale_exponent_used':J,
      'pairs':[list(z) for z in pairs],'modulus':mod,
      'frobenius_matrix':[[int(c//sc)%mod for c in row] for row in Ms],
      'system_matrix':[[int(amat[i,j])%mod for j in range(6)] for i in range(6)],
      'system_rhs':[int(z)%mod for z in bvec],
      'normalized_cross_periods':[rr(z) for z in sol],
      'normalized_target':rr(sol[0]),'odd_model_target_J':2*rr(sol[0])*pow(-608,-1,mod)%mod,
      'system_determinant_mod5':int(amat.det())%5,
      'status':'Finite arithmetic certificate; analytic certification is Section 7 of chabauty_five_adic_residual_certificate.md.'}
    with open('chabauty_regular_frobenius_certificate.json','w') as out:
        json.dump(certificate,out,indent=2)

    print('Normalized target modulo5^7:',rr(sol[0]),flush=True)
    print('Odd-model target J modulo5^7:',2*rr(sol[0])*pow(-608,-1,mod)%mod,flush=True)
    Dstar=132+144*(cutoff-1)
    Lstar=log5floor(Dstar-2);Jstar=log5floor(2*Dstar-4)
    print('Theoretical bounds:',{'D':Dstar,'L':Lstar,'J':Jstar,'finite_error_exponent':W-3*Lstar-Jstar},flush=True)
    if cutoff==20 and W>=30:
        assert [rr(x) for x in sol]==[21625,13695,57225,77593,71316,65694]
        assert W-3*Lstar-Jstar>=7
        print('Seven-digit certificate agrees with the companion proof; valuation of the first period is3.',flush=True)
    print('Analytic tail justification: companion proof, Section7. Seconds=',time.time()-t0,flush=True)
    return sol
if __name__=='__main__':
    n=int(sys.argv[1]) if len(sys.argv)>1 else 20
    w=int(sys.argv[2]) if len(sys.argv)>2 else 30
    run(n,w)
