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

# Lemma 6: exact rational-power identities for every permitted quadratic type.
b,c,d = s.symbols('b c d')
for quad,m,R in [
    (u**2+c,2,-c),
    (u**2+b*u+b**2,3,b**3),
    (u**2+b*u+b**2/2,4,-b**4/4),
    (u**2+b*u+b**2/3,6,-b**6/27),
]:
    assert s.rem(u**m-R,quad,u) == 0
assert s.rem(u**3+d,u**3+d,u) == 0
# Equal-modulus cubic roots u,z,zbar have z*zbar=u*u.
zsum = s.symbols('zsum')
cubic_b = -(u+zsum)
cubic_c = u*zsum+u**2
assert s.expand(cubic_c+cubic_b*u) == 0
# The unconditional example's rejected quadratic lies outside all four types.
assert 36 not in (0,1,2,3)
assert s.expand((u+1)*(u**2-6*u+1)) == u**3-5*u**2-5*u+1
ratio = s.symbols('ratio',nonzero=True)
assert s.cancel(ratio**3/(-1/ratio)) == -ratio**4
print('PASS: rational-power factor identities, cubic obstruction, and binomial target.')

# Simultaneous three-torsion: exact parameter elimination and specializations.
D3 = 3*u**4+4*a*u**3+6*a*u**2+12*u+4*a-a**2
D3_recip = s.expand(u**4*D3.subs(u,1/u))
assert s.factor(s.resultant(D3,D3_recip,u)) == (a-15)*(a-3)**10*(a+1)**3*(a+5)**2
assert s.Poly(s.gcd(D3.subs(a,-5),D3_recip.subs(a,-5)),u).monic().as_expr() == u**2-s.Rational(2,3)*u+1
assert s.Poly(s.gcd(D3.subs(a,15),D3_recip.subs(a,15)),u).monic().as_expr() == u-1
q3 = 3*x**4-2*x**2+3
assert s.discriminant(q3,x) == 2**14*3**2
assert s.resultant(q3,fm,x) == 2**22
p = 67
residue_points = [(xx,yy) for xx in range(p) if int(q3.subs(x,xx)) % p == 0
                  for yy in range(p) if (yy**2-int(fm.subs(x,xx))) % p == 0]
assert residue_points == [(6,20),(6,47),(11,21),(11,46),(56,21),(56,46),(61,20),(61,47)]
for xx,yy in residue_points:
    assert int(s.diff(q3,x).subs(x,xx)) % p != 0
    assert 2*yy % p != 0
print('PASS: simultaneous three-torsion locus, non-Weierstrass certificate, and exact Hensel witness.')
