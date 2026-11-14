#!/usr/bin/env python3
"""Exact finite checks for the five-adic six-disk isolation theorem.

Standard-library only. Analytic infinite-tail and Selmer arguments are proved
in proofs/five_adic_disk_isolation.md, not inferred from finite sampling.
"""
from fractions import Fraction as F
from math import isqrt


def add(f, g):
    h = [F(0)] * max(len(f), len(g))
    for j, c in enumerate(f): h[j] += c
    for j, c in enumerate(g): h[j] += c
    while len(h) > 1 and not h[-1]: h.pop()
    return h


def neg(f): return [-c for c in f]


def mul(f, g):
    h = [F(0)] * (len(f) + len(g) - 1)
    for j, c in enumerate(f):
        for k, d in enumerate(g): h[j+k] += c*d
    while len(h) > 1 and not h[-1]: h.pop()
    return h


def scale(c, f): return [c*x for x in f]


def vp(x, p=5):
    x = F(x)
    if not x: return float('inf')
    n, d, v = abs(x.numerator), x.denominator, 0
    while n % p == 0: n //= p; v += 1
    while d % p == 0: d //= p; v -= 1
    return v


def residue(x, exponent=1, p=5):
    x = F(x); modulus = p**exponent
    assert x.denominator % p
    return (x.numerator * pow(x.denominator, -1, modulus)) % modulus


def floorlog(n, p=5):
    k = 0
    while n >= p: n //= p; k += 1
    return k


def ecadd(P, Q, A):
    if P is None: return Q
    if Q is None: return P
    x, y = P; u, v = Q
    if x == u and y == -v: return None
    m = (3*x*x + 2*A*x - A)/(2*y) if P == Q else (v-y)/(u-x)
    z = m*m - A - x - u
    return z, -y + m*(x-z)


# Polynomial identities in the parameter a, checked coefficientwise.
a = [0, 1]
psi = [0, 4, -1]
N = [-8, 0, 1]
Q = [-64, 0, 40, -20, 3]
assert add(Q, neg(scale(8, N))) == mul([0, 0, 1], mul([-8, 3], [-4, 1]))
# 1/(3t3)-8/(3psi)=-a(3a-8)/(3N), with t3=psi*N/Q.
assert add(add(Q, neg(scale(8, N))), mul(mul(a, [-8, 3]), psi)) == [0]

# Independent rational elliptic additions reproduce the displayed tripling.
a0 = -605; A = a0-3
P = (F(1), F(1))
P2 = ecadd(P, P, A); P3 = ecadd(P2, P, A)
psi0 = a0*(4-a0); n0 = a0*a0-8
q0 = 3*a0**4-20*a0**3+40*a0*a0-64
assert P3 == (F(n0*n0, psi0*psi0), F(-n0*q0, psi0**3))
t3 = -P3[0]/P3[1]
U = F(psi0)/t3
Zprincipal = 1/(3*t3)-F(8, 3*psi0)
assert t3 == F(-134857133565, 406366445311)
assert U == F(406366445311, 366017)
assert Zprincipal == F(-1102915, 1098051)
assert vp(t3) == 1 and residue(t3/5) == 2
assert residue(U, 2) == 8
log_over_5 = residue((U**4-1)/20)
assert log_over_5 == 1
ell_over_5 = residue(t3/15)
h_over_5 = residue(F(2, 9)*log_over_5)
five_alpha = h_over_5*pow(ell_over_5**2, -1, 5) % 5
assert (ell_over_5, h_over_5, five_alpha) == (4, 3, 3)
assert vp(Zprincipal) == 1

# The proof supplies the infinite bounds; these are additional checks over
# all small logarithmic breakpoints, not the analytic justification.
for n in range(4, 10000, 2):
    assert n-2-vp(n)-floorlog(n-1) >= 2
for n in range(3, 10000, 2):
    assert n-1-vp(n) >= 2

# Exhaustive smooth reduction: precisely four affine and two infinite points.
affine = [(x,y) for x in range(5) for y in range(5)
          if (y*y-x**6-1) % 5 == 0]
assert affine == [(0,1),(0,4),(2,0),(3,0)]
for x,y in affine:
    assert (2*y) % 5 != 0 or (6*x**5) % 5 != 0
assert (a0-3)*(a0+1) % 5 != 0

# At r²=-1: f'(r)=-2rA, L1/y=-1/A, L2/y=-r/A.
# Thus (-L1²+L2²)/y²=-2/A², a unit. The local-height
# terms are integral by the all-orders proof and cannot cancel alpha.
assert residue(F(-2, A*A)) == 2
assert residue(F(-2, A*A))*five_alpha % 5 == 1

# Arithmetic hypotheses already established by the rank-pattern theorem.
def isprime(n): return n >= 2 and all(n % d for d in range(2,isqrt(n)+1))
assert isprime(19) and isprime(151) and 8*19-1 == 151
assert 19 % 8 == 3 and a0 == 3-32*19
assert a0 % 8 == 3 and vp(a0-3, 2) == 5 and 19 % 4 == 3

print('PASS: tripling identities, endpoint constants, reduction, and W coefficients.')
print('ell/5=4, h/5=3, 5*alpha=3 modulo 5.')
print('Exactly six residue disks; endpoint and W quadratic factors are units.')
print('Infinite-tail bounds and the final Selmer implication are in the proof.')
