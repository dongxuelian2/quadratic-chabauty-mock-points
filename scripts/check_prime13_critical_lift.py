#!/usr/bin/env python3
"""Exact arithmetic checks for the critical prime-13 two-height proof."""
from fractions import Fraction as F
from math import isqrt

N=[256,-256,-192,224,-56,0,1]
Q=[65536,65536,-49152,-98304,47104,56320,-47104,4864,7296,-3776,856,-100,5]
psi=[-256,0,128,-96,48,-12,1]
R=[-256,0,-64,-32,96,-40,5]
def evaluate(f,a):return sum(c*a**k for k,c in enumerate(f))
def derivative(f):return [k*f[k] for k in range(1,len(f))]
def residue(x,m=13):
    x=F(x);return x.numerator*pow(x.denominator,-1,m)%m
def val13(x):
    x=F(x)
    if not x:return float('inf')
    n,d,v=abs(x.numerator),x.denominator,0
    while n%13==0:n//=13;v+=1
    while d%13==0:d//=13;v-=1
    return v
def floorlog13(n):
    k=0
    while n>=13:n//=13;k+=1
    return k

table=[]
for c in range(13):
    a=74+169*c;n=evaluate(N,a);q=evaluate(Q,a);ps=evaluate(psi,a)
    t=F(-ps*n,q);U=F(-q,n)
    assert residue(F(ps,13))==12 and residue(n)==9 and residue(q)==3
    assert val13(t)==1 and residue(t/13)==3 and residue(t/65)==11
    assert residue(F(-evaluate(R,a),5*n))==5
    e=U**12-1
    assert val13(e)>=2
    log_trunc=e/12
    B=F(a-1,2)*t*t
    assert residue(log_trunc/169)==(12+c)%13
    assert residue(B/169)==10
    h=F(2,25)*(log_trunc-B);ell=t/5
    alpha=residue(h/(ell*ell))
    assert alpha==(12+6*c)%13
    table.append(alpha)
assert table==[12,5,11,4,10,3,9,2,8,1,7,0,6]
assert (74+169*3,74+169*8)==(581,1426)
U=F(-evaluate(Q,74),evaluate(N,74))
Up=F(-evaluate(derivative(Q),74)*evaluate(N,74)+evaluate(Q,74)*evaluate(derivative(N),74),evaluate(N,74)**2)
assert residue(Up/U)==1

# Exhaust all possible integral alpha residues and both branch roots.
# The first and second quadratic numerators cannot vanish together.
for alpha in range(13):
    endpoint=(alpha-4)%13
    slope=-2*(1+5)%13
    assert slope==1
    for r in (5,8):
        assert r*r%13==12
        first=-(10+2*alpha)%13
        second=2*r*(2+alpha)%13
        assert first or second
        assert (first==0)==(alpha==8)
    assert (endpoint==0)==(alpha==4)

# Exact quadratic computation in Q[r]/(r²+1), after clearing A-denominators.
def add(z,w):return z[0]+w[0],z[1]+w[1]
def scale(z,c):return z[0]*c,z[1]*c
def mul(z,w):return z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]
first1=(-1,0);first2=(0,-1)
assert add(mul(first1,first1),scale(mul(first2,first2),-1))==(2,0)
second1=(1,-1);second2=(-1,-1)
assert scale(add(mul(second1,second1),scale(mul(second2,second2),-1)),F(1,4))==(0,-1)
for n in range(3,10000,2):assert n-1-2*floorlog13(n)>=2
for n in range(4,10000,2):assert n-2-2*floorlog13(n)>=2

def prime(n):return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
def factor(n):
    n=abs(n);out={};d=2
    while d*d<=n:
        while n%d==0:out[d]=out.get(d,0)+1;n//=d
        d+=1
    if n>1:out[n]=out.get(n,0)+1
    return out
def second_zero(a):
    for q,m in factor(a+1).items():
        if q==2:continue
        if not (m==1 or (m%2==1 and pow(2,(q-1)//2,q)==q-1)):return False
    return True
for r,q,target in [(326923,2615383,581),(95731,765847,1426)]:
    assert prime(r) and prime(q) and q==8*r-1 and r%8==3
    a=3-32*r
    assert a%2197==target and a%16==3 and factor(a+1)=={2:2,q:1}
    assert second_zero(a)
assert prime(47059) and prime(376471) and 376471==8*47059-1
assert (3-32*47059)%2197==1257
assert factor(4299-3)=={2:3,3:1,179:1}
assert factor(4299+1)=={2:2,5:2,43:1}
assert 4299%169==74 and 4299%8==3 and not second_zero(4299)
assert factor(-1373+1)=={2:2,7:3} and pow(2,3,7)==1 and not second_zero(-1373)
print('PASS: all thirteen alpha residues, primitive constants, endpoint slope and fine lifts.')
print('PASS: both exact W quadratic numerators and every mod13 unit alternative.')
print('PASS: complete trial-division examples in both fine lifts and exact target counterchecks.')
print('The whole-series inequalities and Selmer containments are proved in the companion text.')
