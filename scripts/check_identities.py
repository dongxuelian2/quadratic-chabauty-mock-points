#!/usr/bin/env python3
"""Exact polynomial checks accompanying PROOF.md; no p-adic approximations."""
import sympy as s

x, u, a, a0, a2, a4, a6 = s.symbols('x u a a0 a2 a4 a6')
f = a6*x**6 + a4*x**4 + a2*x**2 + a0
g1 = u**3 + a4*u**2 + a2*a6*u + a0*a6**2
g2 = u**3 + a2*u**2 + a4*a0*u + a6*a0**2
h = 3*a6*x**4 + 2*a4*x**2 + a2
assert s.expand(s.diff(g1,u).subs(u,a6*x**2) - a6*h) == 0
# Multiply away denominators; the residual is exactly 3*a0*f.
residual = s.expand(x**4*s.diff(g2,u).subs(u,a0/x**2) + a0*x**2*h)
assert s.expand(residual - 3*a0*f) == 0

fa = x**6 + a*x**4 + a*x**2 + 1
ea = u**3 + a*u**2 + a*u + 1
assert s.factor(s.discriminant(fa,x)) == -64*(a-3)**6*(a+1)**2
assert s.factor(s.discriminant(ea,u)) == (a-3)**3*(a+1)
assert s.expand(x**6*fa.subs(x,1/x) - fa) == 0
assert s.expand(ea.subs(u,x**2) - fa) == 0
assert s.simplify(ea.subs(u,1/x**2) - fa/x**6) == 0
assert s.expand(fa.subs(x,1)) == 2*(a+1)

fm = fa.subs(a,-5)
assert s.expand(fm-(x*x+1)*(x*x-2*x-1)*(x*x+2*x-1)) == 0
assert s.expand(ea.subs(a,-5).subs(u,u-1)) == u**3-8*u**2+8*u
A,B=-8,8
assert (-2*A,A*A-4*B) == (16,32)
assert (-4)**3+16*(-4)**2+32*(-4) == 8**2
assert s.discriminant(fm,x) == -2**28
assert 16*B**2*(A**2-4*B) == 2**15
print('PASS: quotient derivatives, reciprocal symmetry, discriminants, factorization, and descent witness.')
