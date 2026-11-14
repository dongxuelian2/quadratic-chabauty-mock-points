#!/usr/bin/env python3
"""Exact standard-library checks for the uniform thirteen-adic theorem."""
import json
import argparse
from fractions import Fraction as F
from math import factorial,isqrt
from pathlib import Path

P=13;Q=P**3
def trim(a):
    while len(a)>1 and not a[-1]:a.pop()
    return a
def add(a,b,q=None):
    c=[(a[j] if j<len(a) else 0)+(b[j] if j<len(b) else 0) for j in range(max(len(a),len(b)))]
    return trim([x%q for x in c] if q else c)
def scale(a,k,q=None):return trim([x*k%q if q else x*k for x in a])
def mul(a,b,q=None):
    c=[0]*(len(a)+len(b)-1)
    for j,x in enumerate(a):
        for k,y in enumerate(b):c[j+k]+=x*y
    return trim([x%q for x in c] if q else c)
def power(a,n,q=None):
    r=[1]
    for _ in range(n):r=mul(r,a,q)
    return r
def evaluate(a,x):
    r=0
    for c in a[::-1]:r=r*x+c
    return r
def derivative(a):return [j*a[j] for j in range(1,len(a))]
def vp(n,p=P):
    n=F(n)
    if not n:return float('inf')
    a,b,v=abs(n.numerator),n.denominator,0
    while a%p==0:a//=p;v+=1
    while b%p==0:b//=p;v-=1
    return v
def residue(x,q=Q):
    x=F(x);return x.numerator*pow(x.denominator,-1,q)%q
def interp(values):
    n=len(values);out=[F(0)]*n;fall=[1]
    for k in range(n):
        c=F(values[0],factorial(k))
        for j,v in enumerate(fall):out[j]+=c*v
        values=[v-u for u,v in zip(values,values[1:])]
        fall=mul(fall,[-k,1])
    assert all(c.denominator%P for c in out)
    return trim([residue(c) for c in out])
def determinant_mod(A,p):
    A=[r[:] for r in A];d=1
    for j in range(len(A)):
        k=next(k for k in range(j,len(A)) if A[k][j]%p)
        if k!=j:A[k],A[j]=A[j],A[k];d=-d
        t=A[j][j]%p;d=d*t%p
        for k in range(j+1,len(A)):
            c=A[k][j]*pow(t,-1,p)%p
            A[k]=[(x-c*y)%p for x,y in zip(A[k],A[j])]
    return d%p

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('samples',nargs='?',type=Path,default=Path(__file__).resolve().parents[1]/'verification/universal_p13_samples.json')
parser.add_argument('polynomials',nargs='?',type=Path,default=Path(__file__).resolve().parents[1]/'verification/universal_p13_polynomials.json')
args=parser.parse_args()
samples=json.loads(args.samples.read_text())
universal=json.loads(args.polynomials.read_text())
assert len(samples)==12
pairs=[(i,k) for i in (0,2,4) for k in (1,3)]
for b,s in enumerate(samples):
    assert s['b']==b and s['parameter_a']==9+13*b
    assert (s['p'],s['term_cutoff'],s['coefficient_precision'],s['modulus'])==(13,12,24,13**5)
    M=s['frobenius_matrix'];c=s['system_rhs'];z=s['normalized_cross_periods'];q=13**5
    A=[[(int(r==t)-M[i][j]*M[k][l])%q for t,(j,l) in enumerate(pairs)] for r,(i,k) in enumerate(pairs)]
    assert A==s['system_matrix']
    assert all(sum(A[r][t]*z[t] for t in range(6))%q==c[r] for r in range(6))
    assert determinant_mod(A,13)==11
M=[[interp([s['frobenius_matrix'][i][j] for s in samples]) for j in range(5)] for i in range(5)]
c=[interp([s['system_rhs'][i] for s in samples]) for i in range(6)]
assert M==universal['M'] and c==universal['C']
A=[[add([int(r==t)],scale(mul(M[i][j],M[k][l],Q),-1,Q),Q)
    for t,(j,l) in enumerate(pairs)] for r,(i,k) in enumerate(pairs)]
assert A==universal['system_matrix']
z=universal['solution']
for r in range(6):
    out=[0]
    for t in range(6):out=add(out,mul(A[r][t],z[t],Q),Q)
    assert out==c[r]
assert z[0]==[1521,1690,845]==[169*x for x in [9,10,5]]
M0=[[1976%13,0,442%13,0,1807%13],[0,1976%13,0,2002%13,0],
    [1534%13,0,1378%13,0,1768%13],[0,1900%13,0,225%13,0],
    [638%13,0,304%13,0,1057%13]]
for i in range(5):
    for j in range(5):assert trim([v%13 for v in M[i][j]])==[M0[i][j]]
assert determinant_mod([[p[0]%13 for p in row] for row in A],13)==11
assert (-2)%13 not in {x*x%13 for x in range(13)}
assert all((9+10*b+5*b*b)%13 for b in range(13))
assert factorial(11)%13
assert 348+384*11==4572 and 13**3<=4570<13**4 and 13**3<=9140<13**4
assert 24-2*3==18 and 18-3-3==12 and 12-3-3-3==3
assert (346+384*12)**2*(692+384*12)==130073214800<13**10
assert F(13,12)**3<13
assert 12**2*180*2146==55624320 and 55624320%13==11

# Exact polynomial quintuple identities. Rational functions are pairs of
# integer polynomials; cross multiplication avoids any numerical algebra.
class RF:
    def __init__(self,n,d=None):
        self.n=[n] if isinstance(n,int) else n
        self.d=[1] if d is None else ([d] if isinstance(d,int) else d)
    def __add__(self,o):
        if not isinstance(o,RF):o=RF(o)
        return RF(add(mul(self.n,o.d),mul(o.n,self.d)),mul(self.d,o.d))
    __radd__=__add__
    def __neg__(self):return RF(scale(self.n,-1),self.d)
    def __sub__(self,o):return self+-o if isinstance(o,RF) else self+(-o)
    def __rsub__(self,o):return -self+o
    def __mul__(self,o):
        if not isinstance(o,RF):o=RF(o)
        return RF(mul(self.n,o.n),mul(self.d,o.d))
    __rmul__=__mul__
    def __truediv__(self,o):
        if not isinstance(o,RF):o=RF(o)
        return RF(mul(self.n,o.d),mul(self.d,o.n))
    def __pow__(self,n):return RF(power(self.n,n),power(self.d,n))
    def equals(self,o):return add(mul(self.n,o.d),scale(mul(o.n,self.d),-1))==[0]
a=RF([0,1]);Aell=a-3
ps3=a*(4-a);N3=a*a-8;Q3=3*a**4-20*a**3+40*a*a-64
x2=(a-2)**2/4;y2=-(a-2)*(a*a-2*a-4)/8
x3=N3**2/ps3**2;y3=-N3*Q3/ps3**3
slope=(y3-y2)/(x3-x2);x5=slope*slope-Aell-x2-x3;y5=-y2+slope*(x2-x5)
psi=[-256,0,128,-96,48,-12,1]
N=[256,-256,-192,224,-56,0,1]
Q5=[65536,65536,-49152,-98304,47104,56320,-47104,4864,7296,-3776,856,-100,5]
R=[-256,0,-64,-32,96,-40,5]
assert (-x5/y5).equals(RF(scale(mul(psi,N),-1),Q5))
ps4=-4*(a-2)*(a*a-2*a-4)
assert (8*ps4-ps3**3).equals(RF(psi))
Dpsi=[0,-1280,-640,960,-200]
# Dpsi=-40a(5a³-24a²+16a+32).
assert add(scale(Q5,5),mul(Dpsi,N))==scale(mul(psi,R),5)
for r in range(3):assert evaluate(psi,r)%3==2
U9=F(-evaluate(Q5,9),evaluate(N,9))
Up9=F(-evaluate(derivative(Q5),9)*evaluate(N,9)+evaluate(Q5,9)*evaluate(derivative(N),9),evaluate(N,9)**2)
assert residue(U9,169)==56 and residue(Up9,13)==4
assert residue((U9**12-1)/156,13)==8
assert residue(F(-evaluate(R,9),5*evaluate(N,9)),13)==5
for b in range(13):
    av=9+13*b;U=F(-evaluate(Q5,av),evaluate(N,av))
    assert residue(U,169)==(56+52*b)%169
    assert residue(F(2,25)*(U**12-1)/156,13)==(10-2*b)%13
assert [(x,y) for x in range(13) for y in range(13)
        if (y*y-x**6-9*x**4-9*x*x-1)%13==0]==[(0,1),(0,12),(5,0),(8,0)]
def prime(n):return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
assert prime(571) and prime(4567) and 8*571-1==4567 and 571%8==3
for av in [35,-18269]:
    assert av%13==9 and av%169!=74 and av%16==3
print('PASS: all twelve certificates, exact integral interpolation and six polynomial equations.')
print('PASS: X/13² = 9+10b+5b² modulo13; nonsquare discriminant; pointwise valuation two.')
print('PASS: all theoretical precision constants, exact quintuple identities and scalar residues.')
print('PASS: exhaustive six-point reduction and arithmetic conditions for a=35,−18269.')
