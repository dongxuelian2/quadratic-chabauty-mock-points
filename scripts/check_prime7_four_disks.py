from fractions import Fraction as F
from math import isqrt

def vp(x,p=7):
 x=F(x);n,d=abs(x.numerator),x.denominator;v=0
 if not n:return float('inf')
 while n%p==0:n//=p;v+=1
 while d%p==0:d//=p;v-=1
 return v

def residue(x,m=7):
 x=F(x);return x.numerator*pow(x.denominator,-1,m)%m

def add(P,Q,A):
 x,y=P;u,v=Q
 t=(v-y)/(u-x) if x!=u else (3*x*x+2*A*x-A)/(2*y)
 z=t*t-A-x-u
 return z,t*(x-z)-y

a=-605;A=a-3;P=(F(1),F(1));R=add(add(P,P,A),P,A)
assert R==(F(133968444289,135751718025),F(148737027213396287,50017041747721125))
t=-R[0]/R[1];psi=F((1-A)*(A+3));U=psi/t
assert t==F(-134857133565,406366445311) and psi==-368445
assert vp(t)==vp(psi)==1 and residue(U,49)==36
assert vp(U**6-1)==1 and residue((U**6-1)/7)==2
ell=t/3;h=(U**6-1)/27;Z=1/(3*t)-F(8,3)/psi
assert Z==F(-1102915,1098051)
assert (residue(ell/7),residue(h/7),residue(Z),residue(7*h/ell**2))==(4,5,4,6)
pts=[(x,y) for x in range(7) for y in range(7) if (y*y-(x**6+a*x**4+a*x*x+1))%7==0]
assert pts==[(0,1),(0,6)]
assert all(all(q%d for d in range(2,isqrt(q)+1)) for q in [19,151])
assert A==-32*19 and 151==8*19-1 and 19%8==3 and a%8==3
print('PASS: exact 3P, height/logarithm/primitive residues, four disks, rank-pattern prerequisites.')
print('Formal tails and parameter persistence are proved in the companion note.')
