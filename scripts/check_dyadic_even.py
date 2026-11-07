#!/usr/bin/env python3
"""Exact checks supporting the even-valuation dyadic proof; requires SymPy."""
import sympy as S
B,c,a,t,z,x=S.symbols("B c a t z x")
psi=lambda x:3*x**4+4*c*x**3-6*B*x**2-B**2
target=3*z**4+(6*a+2*c)*z**3+(3*B+9*t+3*c*a)*z**2+(3*a*t+S.Rational(3,2)*c*a*a)*z+c*a**3/4
def reduce(e):
    e=S.rem(S.Poly(S.expand(e),a),S.Poly(a*a-B-2*t,a)).as_expr()
    return S.rem(S.Poly(S.expand(e),t),S.Poly(3*t*t-B*B,t)).as_expr().expand()
assert reduce(psi(a+2*z)/16-target)==0
d=S.symbols("d")
res=S.Poly(S.expand(target.subs({c:4*d,a:1,t:1,B:1})-(z**4+z+d)),z,d)
assert all(k%2==0 for k in res.coeffs())
u,v=S.symbols("u v")
quartic=S.expand((x-u-v)*(x-u+v)*(x+u-v)*(x+u+v))
assert S.expand(quartic-(x**4-2*(u*u+v*v)*x*x+(u*u-v*v)**2))==0
for n in range(4,41,2):
    if n%4==0:
        k=n//4;twist=0;xs=2*k;ys=3*k;ce=2*k
    else:
        k=(n-2)//4;twist=1;xs=2*k+2;ys=3*k+3;ce=2*k+1
    assert 3*xs==2*ys
    assert n+twist+2*xs-2*ys==ce
    assert n+2*twist+xs-2*ys==0
    assert ce>=2
print("PASS: exact shifted quartic, separable residue polynomial, root polynomial, and even-valuation normalizations.")
print("Squareclass independence and Galois stabilizers are proved algebraically in the companion proof.")
