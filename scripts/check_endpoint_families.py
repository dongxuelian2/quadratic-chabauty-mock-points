#!/usr/bin/env python3
"""Exact certificates for proofs/uniform_endpoint_families.md.
Requires SymPy for generic rational identities; numerical checks use exact
integers and fractions. The proof supplies all infinite-series bounds.
"""
from fractions import Fraction as F
from math import isqrt
import sympy as S

def vp(x,p):
    x=F(x)
    if not x: return float("inf")
    n,d,v=abs(x.numerator),x.denominator,0
    while n%p==0: n//=p; v+=1
    while d%p==0: d//=p; v-=1
    return v

def mod(x,m):
    x=F(x); return x.numerator*pow(x.denominator,-1,m)%m

def add(P,Q,A):
    x,y=P;u,v=Q
    m=(v-y)/(u-x) if x!=u else (3*x*x+2*A*x-A)/(2*y)
    z=m*m-A-x-u;w=m*(x-z)-y
    assert w*w==z**3+A*z*z-A*z
    return z,w

def prime(n):
    return n>1 and all(n%d for d in range(2,isqrt(n)+1))

a=S.symbols("a"); A=a-3
x2=(a-2)**2/4
y2=-(a-2)*(a*a-2*a-4)/8
m=(y2-1)/(x2-1)
x3=S.factor(m*m-A-x2-1)
y3=S.factor(m*(1-x3)-1)
psi3=a*(4-a);N=a*a-8;Q=3*a**4-20*a**3+40*a*a-64
assert S.cancel(x3-N*N/psi3**2)==0
assert S.cancel(y3+N*Q/psi3**3)==0
t3=psi3*N/Q;U3=Q/N
assert S.cancel(U3-8-a*a*(3*a-8)*(a-4)/N)==0
assert S.cancel(1/(3*t3)-8/(3*psi3)+a*(3*a-8)/(3*N))==0
assert U3.subs(a,4)==8 and S.diff(U3,a).subs(a,4)==8
m2=(3*x2*x2+2*A*x2-A)/(2*y2)
x4=S.factor(m2*m2-A-2*x2);y4=S.factor(m2*(x2-x4)-y2)
psi4=-4*(a-2)*(a*a-2*a-4)
D=a**4-8*a**3+24*a*a-16*a-32
N4=a**8-8*a**7-8*a**6+224*a**5-672*a**4+640*a**3-512*a+1024
U4=-N4/D
assert S.cancel(-psi4*y4/x4-U4)==0
# psi4=4Y H(X); at P, Dlog psi4=a+2H'(1)/H(1).
X=S.symbols("X")
H=X**6+2*A*X**5-5*A*X**4-5*A*A*X**2-2*A**3*X+A**3
assert S.cancel(4*H.subs(X,1)-psi4)==0
Dlog=a+2*S.diff(H,X).subs(X,1)/H.subs(X,1)
assert S.cancel(-y4/(4*x4)-Dlog/16+(a**3-2*a*a-8)/D)==0
assert U4.subs(a,2)==16 and S.diff(U4,a).subs(a,2)==-16
print("PASS: generic tripling, quadrupling, derivative, unit-ratio and primitive identities.")

for p,base,U in ((7,4,U3),(11,2,U4)):
    for k in range(p):
        v=U.subs(a,base+p*k);u=mod(F(int(v.p),int(v.q)),p*p)
        digit=((pow(u,p-1,p*p)-1)%(p*p))//p
        assert digit==(6*(1+k)%7 if p==7 else (9+k)%11)
print("PASS: all 7 and 11 lifts; omitted classes are 46 mod49 and 24 mod121.")

for p,av in ((7,4),(11,2),(19,0)):
    pts=[(x,y) for x in range(p) for y in range(p)
         if (y*y-x**6-av*x**4-av*x*x-1)%p==0]
    assert pts==[(0,1),(0,p-1)]
    assert ((av+1)*(av-3))%p
print("PASS: exhaustive smooth finite-field counts, four endpoint disks in every case.")

for p,r in ((7,19),(11,571),(19,541)):
    q=8*r-1;av=3-32*r
    assert prime(r) and prime(q) and r%8 in (3,5) and av%8==3
    if p==7: assert av%7==4 and av%49!=46
    if p==11: assert av%11==2 and av%121!=24
    if p==19: assert av%152==19
    print("PASS: prime-pair rank prerequisites",p,av,r,q)
n=659;dd=2*n*n-1
assert prime(n) and prime(dd) and n%8==3 and n%19 in (6,13)
assert 3-8*n*n==-3474245 and (3-8*n*n)%152==19
print("PASS: quadratic rank prerequisites",n,dd,-3474245)

av=-18269;AA=av-3;P=(F(1),F(1))
P2=add(P,P,AA);P4=add(P2,P2,AA)
tt=-P4[0]/P4[1];ps=-4*(av-2)*(av*av-2*av-4)
zz=-F(av**3-2*av*av-8,av**4-8*av**3+24*av*av-16*av-32)
assert tt==F(-2718621001809760145725766425220,12413902554450543099975932989931009)
assert ps==24394919938180 and zz==F(6098062471839,111442095678080129)
assert vp(tt,11)==2 and vp(ps,11)==2 and vp(zz,11)>=0
ee=(pow(mod(F(ps)/tt,121),10,121)-1)%121
hh=F(ee,80)
assert (mod(tt/484,11),mod(hh/11,11),mod(zz,11))==(9,3,5)
assert mod(1331*hh/(tt/4)**2,11)==9
print("PASS: exact p11 example, ell/121=9,h/11=3,Z=5,1331alpha=9 mod11.")

assert pow(8,18,361)==172
for av in (19,-19,57,-17309,-3474245,19**2,-3*19**3,5*19**5):
    AA=av-3;ps=av*(4-av);nn=av*av-8;qq=3*av**4-20*av**3+40*av*av-64
    tt=F(ps*nn,qq);uu=F(qq,nn);zz=F(1,3)/tt-F(8,3)/ps
    ss=vp(av,19)
    assert vp(tt,19)==ss and mod(tt/av,19)==10
    assert mod(uu,361)==8 and vp(zz,19)>=ss
    P3=add(add(P,P,AA),P,AA)
    assert P3==(F(nn*nn,ps*ps),-F(nn*qq,ps**3))
    assert 2*pow(9,-1,19)*10%19==17
    if av==-17309:
        assert tt==F(-89781788228166141,269386870276931839)
        assert uu==F(269386870276931839,299601473)
        assert zz==F(-898942915,898804419)
        assert mod(tt/57,19)==16 and 17*pow(16**2,-1,19)%19==4
print("PASS: exact p19 examples and supplemental valuations 1,2,3,5.")
print("All exact checks pass. Uniform analytic assertions rely on the companion proof.")
