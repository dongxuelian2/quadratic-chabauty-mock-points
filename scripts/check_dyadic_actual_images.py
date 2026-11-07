#!/usr/bin/env python3
"""Exact finite checks accompanying the actual dyadic image proof.

The source path lemma and transported Galois action are proved in the text;
these elementary checks do not replace them.
"""
from fractions import Fraction as F
from math import factorial,isqrt

def valuation2(x):
    x=F(x)
    if not x:return float('inf')
    n,d,v=abs(x.numerator),x.denominator,0
    while n%2==0:n//=2;v+=1
    while d%2==0:d//=2;v-=1
    return v

def f(a,x):return x**6+a*x**4+a*x*x+1
for a in (3,11):
    for x in range(1,16,2):
        assert f(a,x)%16==8
        assert (a+1)*(x*x+1)%16==8
    for x in (2,6):assert f(a,x)%8==5
assert 8 not in {x*x%16 for x in range(16)}
assert 5 not in {x*x%8 for x in range(8)}

# Exact binomial denominator, and the all-n bound's finite sanity check.
c=F(1)
for n in range(1,101):
    c=c*(F(1,2)-(n-1))/n
    assert valuation2(c)==-n-valuation2(factorial(n))
    assert valuation2(factorial(n))<=n-1
    assert 4*n+valuation2(c)>=2*n+1
for a in (3,11,35,-69,-965):
    for t in range(-3,4):
        assert f(a,4*t)==1+16*a*t*t+256*a*t**4+4096*t**6

# g1 has eigenvalues (+,+,-,-) on V1+V2; h=-I acts + in degree2.
g1=[1,1,-1,-1];h=[-1]*4;g2=[x*y for x,y in zip(g1,h)]
for i in (0,1):
    for j in (2,3):
        assert g1[i]*g1[j]==-1
        assert h[i]*h[j]==1
        assert g2[i]*g2[j]==-1
# At infinity z=y/x³, g2 preserves z, whereas g1 negates it.
assert F(-1,(-1)**3)==1
assert F(1,(-1)**3)==-1

def prime(n):return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
for n,p in [(11,5),(3,13)]:
    a=3-8*n*n;A=a-3
    assert prime(n) and prime(2*n*n-1) and n%8==3
    assert a%8==3 and a%16==11 and valuation2(A)==3 and n%4==3
    if p==5:assert a==-965 and a%5==0
    else:assert a==-69 and a%13==9 and a%169!=74
print('PASS: complete dyadic residue exclusions and square-root coefficient checks.')
print('PASS: center signs and infinity-chart action of the two involutions.')
print('PASS: rank-pattern arithmetic and new valuation-three examples a=-965,-69.')
