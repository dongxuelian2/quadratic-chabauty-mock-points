#!/usr/bin/env python3
"""Independent full-pair recheck of the recorded local rank obstructions."""
from fractions import Fraction as F
from itertools import product
from math import isqrt, prod
from pathlib import Path
import re

A=-157472
sides={'E':(A,-A,[2,7,19,37],{1,9842}),
       'Eprime':(-2*A,A*(A+4),[2,7,19,37,39367],{1,-39367,-9842,387450014})}
assert all(39367%d for d in range(2,isqrt(39367)+1))
source=(Path(__file__).resolve().parents[1] / 'verification' / 'rank_one_obstructions.txt').read_text()
for label,(aa,bb,primes,remain) in sides.items():
    section=source.split(label+': complete exclusion list:\n',1)[1]
    if label=='E': section=section.split('Eprime:',1)[0]
    else: section=section.split('2-isogeny formula:',1)[0]
    exclusions=[]
    for line in section.splitlines():
        mt=re.fullmatch(r'  (-?\d+): (real place|mod (\d+)\^(\d+))',line)
        if mt: exclusions.append((int(mt[1]),mt[2],int(mt[3] or 0),int(mt[4] or 0)))
    allclasses={sgn*prod(q for bit,q in zip(bits,primes) if bit)
                for bits in product([0,1],repeat=len(primes)) for sgn in [-1,1]}
    assert len(exclusions)==len(allclasses)-len(remain)
    assert {d for d,*_ in exclusions}==allclasses-remain
    for d,reason,p,k in exclusions:
        assert bb%d==0
        if reason=='real place':
            assert d<0 and aa<0 and bb//d<0
            continue
        mod=p**k
        sq={z*z%mod for z in range(mod)}
        square=[u*u%mod for u in range(mod)]
        fourth=[z*z%mod for z in square]
        # Unlike the generating certificate, test all primitive pairs, not charts.
        for u in range(mod):
            for v in range(mod):
                if u%p==0 and v%p==0: continue
                f=(d*fourth[u]+aa*square[u]*square[v]+(bb//d)*fourth[v])%mod
                assert f not in sq,(label,d,p,k,u,v)
    print(label+': every recorded obstruction independently verified on all primitive residue pairs.')

# Direct rational group law, independently of the analytic-check implementation.
def plus(P,Q):
    if P is None:return Q
    if Q is None:return P
    x,y=P;z,w=Q
    if x==z and y==-w:return None
    slope=(w-y)/(z-x) if x!=z else (3*x*x+2*A*x-A)/(2*y)
    xx=slope*slope-A-x-z
    yy=slope*(x-xx)-y
    assert yy*yy==xx**3+A*xx*xx-A*xx
    return xx,yy
P=(F(1),F(1)); T=plus(plus(P,P),P)
t=-T[0]/T[1]
def valuation(r):
    n,d=abs(r.numerator),r.denominator;v=0
    while n%3==0:n//=3;v+=1
    while d%3==0:d//=3;v-=1
    return v
assert valuation(t)==2
assert t.numerator*pow(t.denominator,-1,3**5)%(3**5)%27==18
print('Direct group law: v3(t(3P))=2 and t(3P)/9=2 mod3, proving nonzero formal logarithm.')
print('INDEPENDENT RANK CHECK PASS: rank upper bound 1 and rank lower bound 1.')
