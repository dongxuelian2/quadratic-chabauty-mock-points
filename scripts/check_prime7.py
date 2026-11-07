#!/usr/bin/env python3
"""Exact rational certificates for the prime-7 first-height isolation theorem.
The all-orders estimates and parameter-continuity proof are in the companion
proofs/prime7_isolation.md. No p-adic numerical package is used.
"""
from fractions import Fraction as F


def vp(x, p):
    x = F(x)
    if not x:
        return float('inf')
    n, d, v = abs(x.numerator), x.denominator, 0
    while n % p == 0:
        n //= p
        v += 1
    while d % p == 0:
        d //= p
        v -= 1
    return v


def mod(x, m):
    x = F(x)
    return x.numerator * pow(x.denominator, -1, m) % m


def add(P, Q, A, B):
    if P is None:
        return Q
    if Q is None:
        return P
    x, y = P
    z, v = Q
    if x == z and y == -v:
        return None
    slope = ((v-y)/(z-x) if x != z else
             (3*x*x+2*A*x+B)/(2*y))
    xx = slope*slope-A-x-z
    yy = slope*(x-xx)-y
    assert yy*yy == xx**3+A*xx*xx+B*xx
    return xx, yy


def check_parameter(a):
    p = 7
    A, B = F(a-3), F(3-a)
    P = (F(1), F(1))
    P2 = add(P, P, A, B)
    P4 = add(P2, P2, A, B)
    t = -P4[0]/P4[1]
    H = 1+2*A+5*B-5*B*B-2*A*B*B-B**3
    Hderiv = 6+10*A+20*B-10*B*B-2*A*B*B
    psi4 = 4*H
    Dlogpsi4 = (3+2*A+B)+2*Hderiv/H
    Zprincipal = 1/(4*t)-Dlogpsi4/16
    assert vp(P4[0], p) == -2
    assert vp(t, p) == vp(psi4, p) == 1
    assert vp(Zprincipal, p) >= 0
    assert mod(Zprincipal, p) == 3
    assert mod(t/(4*p), p) == 5
    modulus = p**3
    ratio = mod(psi4/t, modulus)
    e = (pow(ratio, p-1, modulus)-1) % modulus
    logratio = ((e-e*e*pow(2, -1, modulus)) *
                pow(p-1, -1, modulus)) % modulus
    # Complement (X-2)omega: B_2=(A+2)/2=(a-1)/2.
    Bseries = mod(F(a-1, 2)*t*t, modulus)
    h = (2*(logratio-Bseries)*pow(16, -1, modulus)) % modulus
    assert h == 4*p*p
    alpha = (h//(p*p))*pow(mod(t/(4*p), p)**2, -1, p) % p
    assert alpha == 1
    kappa = (1-mod(Zprincipal, p)+alpha) % p
    assert kappa == 6
    points = [(x, y) for x in range(p) for y in range(p)
              if (y*y-x**6-a*x**4-a*x*x-1) % p == 0]
    assert points == [(0, 1), (0, 6), (2, 0), (3, 0), (4, 0), (5, 0)]
    print(f'a={a}: L/7=5, h/49=4, alpha=1, zeta(P)=3, kappa=6 mod7: PASS')
    if a == -5:
        assert psi4 == 868
        assert ratio == 79 and logratio == 49 and Bseries == 196
        print('4P =', P4)
        print('t(4P) =', t)
        print('zeta principal =', Zprincipal)


if __name__ == '__main__':
    for a in (-5, -5+2744, -5-2744, -5+2*2744):
        check_parameter(a)
    assert 10**2 % 49 == 2
    for r in (9, 11, 38, 40):
        assert (r*r+1)*(r**4-6*r*r+1) % 49 == 0
        assert pow(r, 6, 49) in (15, 36)
        assert vp(pow(r, 6, 49)-1, 7) == 1
    print('All four Weierstrass-center logarithms have valuation one: PASS')
    print('Full-series and parameter-neighborhood claims use the companion proof.')
