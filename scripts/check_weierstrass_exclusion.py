#!/usr/bin/env python3
"""Exact checks supporting, but not proving, the Weierstrass-exclusion theorem."""
from fractions import Fraction as F
def chi(a,q):
 a%=q
 return 0 if not a else (1 if pow(a,(q-1)//2,q)==1 else -1)
count=0
for q in [3,5,7,11,13,17,19,23,31,43]:
 for beta in range(1,q):
  for m in range(1,7):
   criterion=q%4==1 or (m%2==0 and (q!=3 or chi(beta,q)==-1))
   # q=1 mod4 has an exact unit-x point x²=-1,y=0.
   if q%4==1: attained=any(x*x%q==q-1 for x in range(1,q))
   elif m%2: attained=False
   else:
    attained=any(z*z%q==beta*(1+x*x)%q for x in range(1,q) for z in range(q))
   assert criterion==attained
   count+=1
print("PASS:",count,"exact denominator zero-attainment cases.")
for q in [3,7,11,19,23,31,43]:
 for m in range(1,q):
  b=q-m
  assert (3*b-5*m)%q==(-8*m)%q!=0
  a=F(3*b-5*m,b+m)
  assert a.denominator==q
  j=256*a**3/(a+1)
  assert j.denominator% (q*q)==0
print("PASS: distinguished denominator and nonintegral j identities.")
assert (13-3*7)%8==0 and (19-3*9)%8==0
assert chi(1,3)==1
print("PASS: examples 13/7 (odd multiplicity) and 19/9 (q=3 exception).")
