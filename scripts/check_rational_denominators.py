#!/usr/bin/env python3
"""Exact finite-field and rational arithmetic checks; not a substitute for the local proof."""
from fractions import Fraction as F
def chi(a,q):
 a%=q
 return 0 if a==0 else (1 if pow(a,(q-1)//2,q)==1 else -1)
checked=0
for q in [3,5,7,11,13,17,19,23,31,43]:
 for beta in range(1,q):
  if q%4==3:
   count=sum(z*z%q==beta*(1+x*x)%q for x in range(1,q) for z in range(q))
   assert count==q-1-2*chi(beta,q)
  for m in range(1,7):
   for k in range(1,8):
    # A value a=beta/q^m is enough to check all leading residues.
    x=F(q**k); a=F(beta,q**m)
    f=x**6+a*x**4+a*x**2+1
    num,den=f.numerator,f.denominator
    val=0
    while num%q==0: num//=q; val+=1
    while den%q==0: den//=q; val-=1
    sq=(val%2==0 and chi(num*pow(den,-1,q),q)==1)
    if 2*k<m:
     assert sq==(m%2==0 and chi(beta,q)==1)
    if 2*k>m: assert sq
    checked+=1
print("PASS: exact residual conic counts and",checked,"interior/saturated square-class checks.")
# Pure arithmetic for the two component-height differences.
for m in range(1,11):
 for k in range(1,11):
  if 2*k<m:
   correction1=-F(m,2)
   i=m-2*k
   correction2=-F(i*(2*m-i),2*m)
   w=-correction1+correction2-2*k
   assert w==-F(2*k*(m-k),m)
print("PASS: component-height difference formula.")
