#!/usr/bin/env python3
"""Exact algebra and descent-obstruction checks for cm15_torus_exclusion.md.
Requires SymPy. The geometric descent and Selmer argument are in the proof."""
import sympy as S
X,x=S.symbols("X x");s=S.sqrt(-3)
f=lambda z:z**3+12*z*z-12*z
u=-X*(X+6)**2/(3*(X-2)**2)
v=-(X+6)*(X*X-12*X-12)/(3*s*(X-2)**3)
def zero(q):assert S.cancel(q,extension=s)==0
zero(v*v*f(X)-f(u))
zero(S.diff(u,X)-s*v)
assert u.subs(X,0)==0
# Independent rational addition gives tripling; compare both coordinates.
xp2=S.cancel(S.diff(f(X),X)**2/(4*f(X))-12-2*X)
yp2factor=S.cancel(S.diff(f(X),X)*(X-xp2)/(2*f(X))-1)
slopefactor=S.cancel((yp2factor-1)/(xp2-X))
xp3=S.cancel(f(X)*slopefactor**2-12-X-xp2)
yp3factor=S.cancel(slopefactor*(X-xp3)-1)
zero(u.subs(X,u)-xp3)
zero(v.subs(X,u)*v+yp3factor)
print("PASS: CM map preserves E, differential multiplier sqrt(-3), eta²=[-3].")
F=x**6+15*x**4+15*x*x+1
X1=x*x+1;X2=1+x**-2
dx=S.factor(X1-u.subs(X,X2))
expected=(x*x+1)*(3*x*x+1)*(x**4+14*x*x+1)/(3*x*x*(x*x-1)**2)
zero(dx-expected)
ratio=S.cancel(v.subs(X,X2)/x**3)
expected_ratio=-(7*x*x+1)*(23*x**4+10*x*x-1)/(3*s*x**3*(x*x-1)**3)
zero(ratio-expected_ratio)
zero(ratio.subs(x,-s/3)+1);zero(ratio.subs(x,s/3)-1)
assert S.expand(F.subs(x,s))==64 and S.expand(F.subs(x,-s))==64
assert S.expand(F.subs(x,s/3))==-S.Rational(64,27)
assert S.expand((8*s/9)**2)==-S.Rational(64,27)
assert u.subs(X,1)==-S.Rational(49,3)
assert S.factor(F)==(x*x+1)*(x**4+14*x*x+1)
print("PASS: complete-fiber algebra, residual signs and exceptional finite values.")
g=(3*x+s)/(3*x-s)
assert g.subs(x,0)==-1
zero(g*S.conjugate(g).subs(S.conjugate(x),x)-1)
# Exact origin-fiber ratio and local unit.
r=S.sqrt(3);ii=S.I
zero(g.subs(x,ii)-(2+r))
zero((ii-s)/(ii+s)-(r-2))
unit=S.simplify(((ii-s)/(ii+s))/g.subs(x,ii))
assert S.simplify(unit-(-7+4*r))==0
assert S.expand((-7+4*r)*(-7-4*r))==1
print("PASS: derivative fiber ratio gives local unit -7+4sqrt(3), of norm one.")
assert 16*S.discriminant(f(X),X)==2**14*3**3
assert S.discriminant(F,x)==-2**26*3**6
assert S.expand((X+4)**3-60*(X+4)+176-f(X))==0
assert xp2.subs(X,1)==S.Rational(169,4)
assert f(-2)==64 and f(1)==1
# Exhaust primitive pairs modulo8; squares modulo64.
squares={n*n%64 for n in range(64)}
for U in range(8):
 for V in range(8):
  if U%2==0 and V%2==0:continue
  rhs=2*(U**4+6*U*U*V*V-3*V**4)
  rhs2=2*(U**4-12*U*U*V*V+48*V**4)
  assert rhs%64 not in squares and rhs2%64 not in squares
print("PASS: both primitive d=2 descent obstructions, rank witnesses and corrected short model.")
print("The proof separately establishes fiber multiplicities, proper reference signs and the global obstruction.")
