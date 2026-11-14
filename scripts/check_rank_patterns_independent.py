#!/usr/bin/env python3
"""Independent all-pair 2-adic tests and primality checks for rank patterns."""
from math import isqrt

def no_primitive_square(d,c,e,M):
    squares={z*z%M for z in range(M)}
    u2=[u*u%M for u in range(M)]
    u4=[s*s%M for s in u2]
    for u in range(M):
        for v in range(M):
            if (u|v)%2==0:continue
            assert (d*u4[u]+c*u2[u]*u2[v]+e*u4[v])%M not in squares,(d,c,e,M,u,v)

for p in (3,5):
    no_primitive_square(2,-32*p,16*p,128)
for c in (64,192):
    for d in range(1,256,2):
        if d%8!=1:no_primitive_square(d,c,128,256)
for r in (3,11):
    no_primitive_square(r,-8,8,16)
print('All uniform 2-adic obstructions PASS on every primitive residue pair.')

def prime(p):
    assert p>=2
    assert all(p%d for d in range(2,isqrt(p)+1)),p

def factors(n):
    ans={}
    p=2
    while p*p<=n:
        while n%p==0:
            ans[p]=ans.get(p,0)+1;n//=p
        p+=1
    if n>1:ans[n]=ans.get(n,0)+1
    return ans

for p in [6379,12211,19501,48661,159469]:
    q=8*p-1;prime(p);prime(q)
    assert p%8 in (3,5) and p%729==547
    A=-32*p
    assert (A+8)%5832==0 and A+4==-4*q
    for x in (A,A+4):assert (2*x)**2==x**3-2*A*x*x+A*(A+4)*x
for n in [2915,8747,11663,29159,32075]:
    fs=factors(n);D=2*n*n-1;prime(D)
    assert n>1 and n%2 and n%729 in (1,728)
    assert all(p%8 in (3,5) for p in fs)
    assert sum(p%8==3 and e%2==1 for p,e in fs.items())==1
    A=-8*n*n
    assert (A+8)%5832==0 and A+4==-4*D
    for x in (A,A+4):assert (2*x)**2==x**3-2*A*x*x+A*(A+4)*x
print('Ten example factorizations, primality claims, congruences and known points PASS.')

# The odd-n assumption cannot be discarded.
A=-288;x=300;y=1080
assert y*y==x*x*x+A*x*x-A*x
assert factors(71)=={71:1}
print('Scope guard PASS: n=6 admits the extra first-image class 3 via (300,1080).')
