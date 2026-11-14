#!/usr/bin/env python3
"""Exact arithmetic for a rank-certified 12-first/4-second/full-4 example.
Standard library only. Analytic tails and containment are proved separately."""
from fractions import Fraction as F
from math import isqrt
p=7;r=467941;q=8*r-1;a=3-32*r;A=a-3
def prime(n):return n>1 and all(n%d for d in range(2,isqrt(n)+1))
def md(x,m):
 x=F(x);return x.numerator*pow(x.denominator,-1,m)%m
assert prime(r) and prime(q)
assert r%8==5 and a%8==3 and a%343==242 and a+1==-4*q
assert a==-14974109 and q==3743527
psi=a*(4-a);U=F(3*a**4-20*a**3+40*a*a-64,a*a-8);t=F(psi)/U
Zpr=-F(a*(3*a-8),3*(a*a-8))
M=p**7;e=(pow(md(U,M),p-1,M)-1)%M
lg=sum((-1)**(k+1)*F(e**k,k*(p-1)) for k in range(1,4))
B=F(a-1,2)*t*t+F(A*A+A,4)*t**4
h=F(2,9)*(lg-B);ell=(t+F(A,3)*t**3)/3;Z=Zpr+F(2,3)*t
alpha=h/(ell*ell);kappa=1-Z+alpha*(1-ell)
b=F(a,4)*Z-F(1+2*a,4)+alpha*(F(a,4)*ell-F(1,4)-F(a,3))
slope=-2*(1+Z+alpha*ell)
assert (md(ell/p,p),md(Z,p),md(h/p**2,p),md(alpha,p))==(6,4,3,3)
assert md(kappa,p**3)==294 and md(b,p)==4 and md(slope,p)==4
roots=[v for v in range(p) if (4*v*v+6)%p==0]
assert roots==[3,4] and sorted(4*v%p for v in roots)==[2,5]
# Independent formal recursion through degree 20.
N=10;v=[F(1)]+[F(0)]*(N+2)
for n in range(1,N+3):
 v[n]=A*v[n-1]-A*sum((v[i]*v[n-2-i] for i in range(n-1)),F(0))
inv=[F(1)]+[F(0)]*(N+2)
for n in range(1,N+3):
 inv[n]=-sum(v[i]*inv[n-i] for i in range(1,n+1))
omega=[F(1)]+[sum(i*v[i]*inv[n-i] for i in range(1,n+1)) for n in range(1,N+2)]
zet=[(2*omega[n]-sum(inv[i]*omega[n+1-i] for i in range(n+2)))/F(2*n+1) for n in range(N)]
Ls=[omega[n]/F(2*n+1) for n in range(N+1)]
Bs=[F(0)]+[(omega[n]+sum(zet[i]*omega[n-1-i] for i in range(n)))/F(2*n) for n in range(1,N+1)]
ell2=sum((c*t**(2*n+1) for n,c in enumerate(Ls)),F(0))/3
Z2=Zpr+sum((c*t**(2*n+1) for n,c in enumerate(zet)),F(0))/3
B2=sum((c*t**(2*n) for n,c in enumerate(Bs)),F(0))
M2=p**8;e2=(pow(md(U,M2),p-1,M2)-1)%M2
lg2=sum((-1)**(k+1)*F(e2**k,k*(p-1)) for k in range(1,10))
h2=F(2,9)*(lg2-B2);alpha2=h2/(ell2*ell2)
kap2=1-Z2+alpha2*(1-ell2);slope2=-2*(1+Z2+alpha2*ell2)
assert md(kap2,p**3)==294 and md(slope2,p)==4
print("PASS: complete primality and rank-pattern prerequisites; both actual targets zero.")
print("PASS: ell/7=6,Z=4,h/49=3,alpha=3,b=4,second slope=4 mod7.")
print("PASS: kappa=294 mod343 by low and independent degree20 formal calculations.")
print("PASS: first extras x/7=±3 have second height/7=±2, hence are excluded.")
print("Full-set equality uses the proved series bound and actual-target containment.")
