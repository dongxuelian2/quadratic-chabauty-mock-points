#!/usr/bin/env python3
"""Exact scalar-bifurcation certificates. Requires SymPy.
The companion proof supplies the all-orders convergence and contraction."""
from fractions import Fraction as F
from math import gcd
import sympy as S
a,Z,ell,alpha=S.symbols("a Z ell alpha")
q1=-a/2;q2=3*a*a/8-a/2;r0=q1-1;r1=(q2-q1)/3
c1=q1-Z-r0+alpha*(1-ell)
c2=(q2-Z*q1-S.Rational(1,2)-r1-r0*q1)/2
c2+=alpha*(2*q1/3-ell*q1/2-S.Rational(1,4))
assert S.expand(c1-(1-Z+alpha*(1-ell)))==0
assert S.expand(c2-((a*Z-1-2*a)/4+alpha*(a*ell/4-S.Rational(1,4)-a/3)))==0
print("PASS: symbolic endpoint coefficients kappa and b.")

def vp(q,p):
 q=F(q)
 if not q:return float("inf")
 n,d,v=abs(q.numerator),q.denominator,0
 while n%p==0:n//=p;v+=1
 while d%p==0:d//=p;v-=1
 return v
def mod(q,M):
 q=F(q);assert gcd(q.denominator,M)==1
 return q.numerator*pow(q.denominator,-1,M)%M
def add(P,Q,A):
 x,y=P;u,v=Q
 slope=(v-y)/(u-x) if x!=u else (3*x*x+2*A*x-A)/(2*y)
 xx=slope*slope-A-x-u;yy=slope*(x-xx)-y
 assert yy*yy==xx**3+A*xx**2-A*xx
 return xx,yy
def constants(p,a):
 A=a-3;P=(F(1),F(1));P2=add(P,P,A)
 if p==7:
  m=3;Pm=add(P2,P,A);psi=a*(4-a)
  Uf=F(3*a**4-20*a**3+40*a*a-64,a*a-8)
  Z0=-F(a*(3*a-8),3*(a*a-8))
 else:
  assert p==11
  m=4;Pm=add(P2,P2,A);psi=-4*(a-2)*(a*a-2*a-4)
  D=a**4-8*a**3+24*a*a-16*a-32
  N=a**8-8*a**7-8*a**6+224*a**5-672*a**4+640*a**3-512*a+1024
  Uf=-F(N,D);Z0=-F(a**3-2*a*a-8,D)
 t=-Pm[0]/Pm[1];U=F(psi)/t
 assert U==Uf and vp(t,p)==1
 return A,m,t,U,Z0

def formal(A,N=8):
 # Independently generate from u=t²v(t²), v=1+A*w*v-A*w²*v².
 v=[F(1)]+[F(0)]*(N+2)
 for n in range(1,N+3):
  v[n]=A*v[n-1]-A*sum((v[i]*v[n-2-i] for i in range(n-1)),F(0))
 inv=[F(1)]+[F(0)]*(N+2)
 for n in range(1,N+3):
  inv[n]=-sum(v[i]*inv[n-i] for i in range(1,n+1))
 omega=[F(1)]+[sum(i*v[i]*inv[n-i] for i in range(1,n+1)) for n in range(1,N+2)]
 zeta=[(2*omega[n]-sum(inv[i]*omega[n+1-i] for i in range(n+2)))/F(2*n+1) for n in range(N)]
 L=[omega[n]/F(2*n+1) for n in range(N+1)]
 B=[F(0)]+[(omega[n]+sum(zeta[i]*omega[n-1-i] for i in range(n)))/F(2*n) for n in range(1,N+1)]
 assert L[1]==F(A,3)
 assert zeta[0]==2 and zeta[1]==A
 assert B[1]==F(A+2,2) and B[2]==F(A*A+A,4)
 return L,zeta,B

def invariants(p,a,high=False):
 A,m,t,U,Z0=constants(p,a)
 precision=7 if high else 5;M=p**precision
 e=F((pow(mod(U,M),p-1,M)-1)%M)
 assert vp(e,p)>=2
 terms=8 if high else 2
 logU=sum(((-1)**(k+1)*e**k/F((p-1)*k) for k in range(1,terms+1)),F(0))
 if high:
  Ls,Zs,Bs=formal(A)
  ep=sum((c*t**(2*n+1) for n,c in enumerate(Ls)),F(0))/m
  zz=Z0+sum((c*t**(2*n+1) for n,c in enumerate(Zs)),F(0))/m
  bb=sum((c*t**(2*n) for n,c in enumerate(Bs)),F(0))
 else:
  ep=(t+F(A,3)*t**3)/m;zz=Z0+2*t/m
  bb=F(A+2,2)*t*t+F(A*A+A,4)*t**4
 hh=F(2,m*m)*(logU-bb);al=hh/(ep*ep)
 kap=1-zz+al*(1-ep)
 bc=(a*zz-1-2*a)/4+al*(F(a,4)*ep-F(1,4)-F(a,3))
 assert vp(ep,p)==1 and vp(hh,p)>=2 and vp(al,p)>=0
 vals=tuple(mod(q,p**n) for q,n in ((ep/p,1),(zz,1),(hh/p**2,1),(al,1),(kap,3),(bc,1)))
 return vals,vp(hh,p)

for p,base in ((7,46),(11,24)):
 for j in range(p):
  vals,_=invariants(p,base+p*p*j)
  ep,zz,hh,al,kap,bb=vals
  assert ep==6
  if p==7:
   assert (zz,hh,al,kap%p)==(4,(j+6)%p,(j+6)%p,(j+3)%p)
  else:
   assert (zz,hh,al,kap%p)==(5,(4*j+7)%p,(5*j+6)%p,(5*j+2)%p)
  if kap%p==0:assert bb==4
 print("PASS: all omitted-lift residues at",p)
for p,a,target in ((11,12487,726),(11,656691,726),(7,17735,294)):
 low=invariants(p,a);high=invariants(p,a,True)
 assert low==high,(p,a,low,high)
 vals,vh=low;ep,zz,hh,al,kap,bb=vals
 assert kap==target and bb==4 and vh==2
 assert kap%(p*p)==0 and (kap//(p*p))%p!=0
 assert pow((-(kap//(p*p)))%p,(p-1)//2,p)==1
 print("PASS: 12 scalar zeros:",p,a,"kappa mod p^3 =",kap,"b mod p =",bb)
found=[]
for p in (3,5,7,11,13,17,19):
 for a in range(p):
  if (a+1)*(a-3)%p==0:continue
  count=2+sum((y*y-x**6-a*x**4-a*x*x-1)%p==0 for x in range(p) for y in range(p))
  if count==4:found.append((p,a))
assert found==[(7,4),(11,2),(19,0)]
print("PASS: complete finite-field list",found)
print("Analytic completeness and infinite tails are proved in the companion text.")
