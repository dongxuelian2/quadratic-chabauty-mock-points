#!/usr/bin/env python3
"""Exact algebra and valuation-table checks; infinitude and rank use Zywina's theorem."""
from fractions import Fraction as F
triples=[(0,0,0),(0,1,0),(-1,1,-1),(0,2,0),(1,0,0),(-1,1,-1),(0,0,1)]
assert [w-v for u,v,w in triples]==[0,-1,-2,-2,0,-2,1]
def j(a2,a4):
 c4=16*(a2*a2-3*a4)
 delta=16*a4*a4*(a2*a2-4*a4)
 return c4**3/delta
n=0
for b in range(2,31):
 for m in range(1,b):
  u=F(m+b); a=F(3*b-5*m,m+b); A=a-3
  assert -1<a<3
  assert A*u*u==-8*m*u
  assert -A*u**4==8*m*u**3
  assert (-2*A)*(u/2)**2==4*m*u
  assert A*(A+4)*(u/2)**4==2*m*u*u*(m-b)
  jf=j(F(4*m)*u,F(2*m)*u*u*(m-b))
  assert jf==F(64*(5*m+3*b)**3,(m-b)**2*(m+b))
  assert j(A,-A)==256*a**3/(a+1)
  n+=1
print("PASS:",n,"exact parameter/isogeny-model/j-identity checks.")
print("PASS: complete source valuation table has positive differences only 1.")
