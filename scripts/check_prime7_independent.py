#!/usr/bin/env python3
"""Independent standard-library-only prime-7 audit.

Uses successive doubling and the composite division-function identity,
rather than importing the submitted checker or its fourth-division polynomial.
It compares 4P and 8P certificates modulo 7^6. The all-orders error bounds are
recorded in verification/prime7_independent_audit.md.
"""
from fractions import Fraction as F


def valuation(value, p=7):
    value = F(value)
    if not value:
        return float('inf')
    n, d, result = abs(value.numerator), value.denominator, 0
    while n % p == 0:
        n //= p
        result += 1
    while d % p == 0:
        d //= p
        result -= 1
    return result


def residue(value, modulus):
    value = F(value)
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def double(point, A):
    x, y = point
    slope = (3*x*x + 2*A*x - A)/(2*y)
    xx = slope*slope - A - 2*x
    yy = slope*(x-xx)-y
    assert yy*yy == xx**3+A*xx*xx-A*xx
    return xx, yy


def formal_coefficients(A, count=6):
    # U^2-(1-A*T)U-A*T^2=0; w*U=U-T*U'.
    u = [F(1)]
    for n in range(1, count+2):
        u.append(-A*u[n-1] - sum(u[j]*u[n-j] for j in range(1, n))
                 + (A if n == 2 else 0))
    w = [F(1)]
    for n in range(1, count+1):
        w.append((1-n)*u[n] - sum(u[j]*w[n-j] for j in range(1, n+1)))
    # -(X-2)w=-t^-2+sum a[j]*t^(2j).
    inner = [j*u[j+1]+2*w[j] for j in range(count)]
    b = [F(0)]
    for k in range(1, count+1):
        b.append((w[k]+sum(inner[j]*w[k-j-1]/(2*j+1)
                           for j in range(k)))/(2*k))
    assert b[1] == F(A+2, 2)
    return w, inner, b


def log_unit_approximation(value):
    # Units have log(value)=log(value^6)/6; no Teichmuller computation.
    assert valuation(value) == 0
    e = value**6-1
    assert valuation(e) >= 1
    return sum(F((-1)**(n+1), 6*n)*e**n for n in range(1, 9))


def certify(a):
    A = F(a-3)
    point = (F(1), F(1))
    n, division, derivative = 1, F(1), F(0)
    data = {}
    w, inner, b = formal_coefficients(A)
    while n < 8:
        x, y = point
        # psi_(2n)(P) = 2Y(nP)*psi_n(P)^4.
        # D_P log(2Y(nP)) = n*g'(X(nP))/Y(nP).
        derivative = n*(3*x*x+2*A*x-A)/y+4*derivative
        division = 2*y*division**4
        point = double(point, A)
        n *= 2
        if n < 4:
            continue
        t = -point[0]/point[1]
        assert valuation(t) == valuation(division) == 1
        L = sum(w[k]*t**(2*k+1)/F(2*k+1) for k in range(len(w))) / n
        zeta = (1/t+sum(inner[j]*t**(2*j+1)/F(2*j+1)
                       for j in range(len(inner))))/n-derivative/F(n*n)
        B = sum(b[k]*t**(2*k) for k in range(1, len(b)))
        height = 2*(log_unit_approximation(division/t)-B)/F(n*n)
        assert valuation(L) == 1 and residue(L/7, 7) == 5
        assert valuation(height) == 2 and residue(height/49, 7) == 4
        assert residue(zeta, 7) == 3
        assert residue(height/(L*L), 7) == 1
        data[n] = (L, height, zeta)
    assert all(valuation(x-y) >= 6 for x, y in zip(data[4], data[8]))
    print(f'a={a}: independent 4P and 8P constants agree modulo 7^6: PASS')
    if a == -5:
        print('residues (ell, h, Z) modulo 7^6 =',
              tuple(residue(x, 7**6) for x in data[4]))


if __name__ == '__main__':
    # Exercise every next 7-adic parameter digit while preserving oddness.
    for k in range(7):
        certify(-5+686*k)
    points = [(x, y) for x in range(7) for y in range(7)
              if (y*y-x**6+5*x**4+5*x*x-1) % 7 == 0]
    assert points == [(0, 1), (0, 6), (2, 0), (3, 0), (4, 0), (5, 0)]
    roots = [r for r in range(49) if (r**4-6*r*r+1) % 49 == 0]
    assert roots == [9, 11, 38, 40]
    assert [pow(r, 6, 49) for r in roots] == [36, 15, 15, 36]
    print('Residue disks and all four center logarithm valuations: PASS')
