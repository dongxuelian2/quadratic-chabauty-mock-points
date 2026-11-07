#!/usr/bin/env python3
"""Exact algebra and graph-position checks for odd primes dividing a-3."""
from fractions import Fraction as F
for pi in [F(1,3),F(2),F(3),F(5,7)]:
 for Z in [F(1),F(2),F(4,3)]:
  A=pi**4; h=pi**2*Z
  assert h**3+A*h*h-A*h==pi**6*(Z**3+pi*pi*Z*Z-Z)
  for W in [F(1),F(2,3)]:
   z=pi*W/Z; t=-Z/W
   assert z*t==-pi
print("PASS: rescaled elliptic equation and exact neck identity.")
def wedge(u,v):
 return {(i,j):u[i]*v[j]-u[j]*v[i] for i in range(4) for j in range(i+1,4)}
plus=wedge([1,0,0,1],[0,1,-1,0])
minus=wedge([1,0,0,-1],[0,1,1,0])
assert plus[(0,1)]==plus[(2,3)]==1
assert plus[(0,3)]==plus[(1,2)]==0
assert plus[(0,2)]==plus[(1,3)]==-1
assert all(plus[k]==-minus[k] for k in [(0,2),(0,3),(1,2),(1,3)])
print("PASS: separating bivector has zero Tate projection and nonzero opposite Sym² parts.")
for n in range(1,65):
 attained={F(0),F(1),F(-1)}
 for h in range(1,n):
  if 2*h<n and h%2==0:
   value=F(2*h,n)
   attained|={value,-value}
 formula={F(0),F(1),F(-1)}
 for k in range(1,n):
  if 4*k<n: formula|={F(4*k,n),-F(4*k,n)}
 assert attained==formula
print("PASS: interior valuation-to-edge coefficients for n=1,...,64.")
