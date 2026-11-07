#!/usr/bin/env python3
"""Exact polynomial and parity checks for the dyadic residual-vanishing proof.
SymPy is used only for rational polynomial arithmetic; no p-adic approximations.
"""
import sympy as s
B,c,r,w,x,u,v=s.symbols('B c r w x u v')
psi=3*x**4+4*c*x**3-12*B*x*x-4*B*B
P=s.cancel(s.rem(s.Poly(psi.subs(x,r+2*B+2*B*w),r),
                   s.Poly(r*r-2*B,r)).as_expr()/(16*B*B))
expected=[3*B*B+2*B*c+6*B*r+6*B+3*c*r+3*c-1+c*r/(2*B),
          12*B*B+6*B*c+18*B*r+12*B+6*c*r+3*c,
          18*B*B+6*B*c+18*B*r+6*B+3*c*r,
          12*B*B+2*B*c+6*B*r,3*B*B]
for j,e in enumerate(expected):
    assert s.cancel(s.expand(P).coeff(w,j)-e)==0
    if j<4:
        # Multiply by B to remove the only unit denominator, preserving valuation.
        intpart=s.expand((B*e).subs(r,0))
        rpart=s.expand(B*s.diff(e,r))
        # For B odd and c divisible by8, integer part has valuation>=2,
        # while the coefficient of r has valuation exactly1.
        ii=s.Poly(s.expand(intpart.subs({B:2*u+1,c:8*v})),u,v)
        rr=s.Poly(s.expand(rpart.subs({B:2*u+1,c:8*v})),u,v)
        assert all(int(k)%4==0 for k in ii.coeffs())
        assert all(int(k)%2==0 for k in rr.coeffs())
        rr2=s.Poly(s.expand(rr.as_expr()/2),u,v)
        assert int(rr2.coeff_monomial(1))%2==1
        assert all(int(coeff)%2==0 for mon,coeff in rr2.terms() if mon!=(0,0))
P5=s.expand(P.subs(c,8*B))
P5expected=(3*B*B*w**4+(28*B*B+6*B*r)*w**3+
             (66*B*B+42*B*r+6*B)*w*w+
             (60*B*B+66*B*r+36*B)*w+
             19*B*B+30*B*r+30*B+4*r-1)
assert s.expand(P5-P5expected)==0
for a in [-605,-1373,-157469]:
    A=a-3;n=0
    while A%2==0:A//=2;n+=1
    assert n==5 and A%2 and a%8==3
    print('a=',a,'v2(a-3)=',n,'B=',A)
print('General division-polynomial identity and all four coefficient valuations: PASS')
print('n=5 specialized polynomial identity: PASS')
print('Newton polygon has endpoints (0,3/2),(4,0); all middle coefficients have valuation3/2.')
print('The inertia and cohomology conclusions are proved in the companion note, not inferred numerically.')
