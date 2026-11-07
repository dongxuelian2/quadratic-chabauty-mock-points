#!/usr/bin/env python3
"""Exact checks for the dyadic quaternion-inertia proof; no numerical 2-adic roots."""
from fractions import Fraction as F
def v2(x):
 x=F(x)
 if x==0:return 10**9
 n,d=abs(x.numerator),x.denominator
 v=0
 while n%2==0:n//=2;v+=1
 while d%2==0:d//=2;v-=1
 return v
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def mul(x,y,B):return (x[0]*y[0]+2*B*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def pmul(a,b,B):
 o=[(F(0),F(0)) for _ in range(len(a)+len(b)-1)]
 for i,x in enumerate(a):
  for j,y in enumerate(b):o[i+j]=add(o[i+j],mul(x,y,B))
 return o
cases=0
for B in range(-31,32,2):
 for C in range(-8,9):
  c=8*C
  x=[(F(2*B),F(1)),(F(2*B),F(0))]
  pows=[[(F(1),F(0))]]
  for n in range(4):pows.append(pmul(pows[-1],x,B))
  out=[(F(0),F(0)) for _ in range(5)]
  for deg,coef in [(4,3),(3,4*c),(2,-12*B),(0,-4*B*B)]:
   for j,(u,v) in enumerate(pows[deg]):
    out[j]=add(out[j],(coef*u/(16*B*B),coef*v/(16*B*B)))
  exact=[
   (F(-1+6*B+3*B*B+3*c+2*B*c),6*F(B)+F(c*(1+6*B),2*B)),
   (F(12*B*(1+B)+3*c*(1+2*B)),F(6*(3*B+c))),
   (F(6*B*(1+3*B+c)),F(3*(6*B+c))),
   (F(12*B*B+2*B*c),F(6*B)),
   (F(3*B*B),F(0))]
  assert out==exact
  assert v2(out[4][0])==0 and out[4][1]==0
  for u,v in out[:4]:
   assert v2(u)>=2 and v2(v)==1
   assert min(F(v2(u)),F(v2(v))+F(1,2))==F(3,2)
  cases+=1
print("PASS:",cases,"exact quartic expansions and uniform Newton valuations.")
I=(1,0,0,1)
def mm(a,b):
 return ((a[0]*b[0]+a[1]*b[2])%3,(a[0]*b[1]+a[1]*b[3])%3,
         (a[2]*b[0]+a[3]*b[2])%3,(a[2]*b[1]+a[3]*b[3])%3)
G={(a,b,c,d) for a in range(3) for b in range(3) for c in range(3) for d in range(3) if (a*d-b*c)%3==1}
minusI=(2,0,0,2)
Q={I,minusI}|{g for g in G if mm(g,g)==minusI}
assert len(G)==24 and len(Q)==8
def closure(gens):
 s={I}; todo=[I]
 while todo:
  x=todo.pop()
  for g in gens:
   z=mm(x,g)
   if z not in s:s.add(z);todo.append(z)
 return frozenset(s)
subs={frozenset([I])}; todo=list(subs)
while todo:
 H=todo.pop()
 for g in G-H:
  K=closure(list(H)+[g])
  if K not in subs:subs.add(K);todo.append(K)
def line(v):
 a,b=v
 if a:return (1,b*pow(a,-1,3)%3)
 return (0,1)
for H in subs:
 orbit={line((g[0],g[2])) for g in H}
 if len(orbit)==4:assert Q<=H
print("PASS: every transitive projective subgroup of SL2(F3) contains Q8.")
for n in range(5,40,2):
 for B in [-7,-3,1,5]:
  A=2**n*B
  if n%4==1:
   k=(n-1)//4;c=F(A,2**(2*k));d=F(-A,2**(4*k))
  else:
   k=(n-3)//4+1;c=F(2*A,2**(2*k));d=F(-4*A,2**(4*k))
  assert v2(c)>=3 and d==-2*B
print("PASS: scaling/twist reduction for every odd n from5 through39.")
