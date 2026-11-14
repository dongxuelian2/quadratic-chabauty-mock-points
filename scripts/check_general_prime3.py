#!/usr/bin/env python3
"""Exact finite checks for the general prime-3 criterion (standard library only).

The parameter-neighborhood and all-orders conclusions are proved in the
companion .md file. This script checks rational constants at explicit examples;
it does NOT compute Mordell-Weil ranks or away-from-3 local targets.
"""
from fractions import Fraction as F


def v3(x):
    x = F(x)
    if not x:
        return float('inf')
    n, d, v = abs(x.numerator), x.denominator, 0
    while n % 3 == 0:
        n //= 3
        v += 1
    while d % 3 == 0:
        d //= 3
        v -= 1
    return v


def mod3(x):
    x = F(x)
    assert v3(x) >= 0
    return x.numerator * pow(x.denominator, -1, 3) % 3


def log_unit_delta(x):
    """log(x)=delta+O(3^4) when the returned delta has valuation two."""
    x = F(x)
    assert v3(x) == 0
    delta = (x if mod3(x) == 1 else -x) - 1
    assert v3(delta) == 2
    return delta


def add_scaled(p, q, A, B, d):
    """Group law for y=s*ybar, s^2=d, on y^2=x^3+A*x^2+B*x."""
    if p is None:
        return q
    if q is None:
        return p
    x, ybar = p
    z, vbar = q
    assert d*ybar*ybar == x**3 + A*x*x + B*x
    assert d*vbar*vbar == z**3 + A*z*z + B*z
    if x == z and ybar == -vbar:
        return None
    slopebar = ((vbar-ybar)/(z-x) if x != z else
                (3*x*x + 2*A*x + B)/(2*d*ybar))
    outx = d*slopebar*slopebar-A-x-z
    outy = slopebar*(x-outx)-ybar
    assert d*outy*outy == outx**3+A*outx*outx+B*outx
    return outx, outy


def check_parameter(a):
    assert a % 2 and (a+5) % (3**6) == 0
    A = F(a-3)
    d = F(a+1, 2)
    P = (F(1), F(1))
    P3 = add_scaled(add_scaled(P, P, A, -A, F(1)), P, A, -A, F(1))
    t = -P3[0]/P3[1]
    psi = F(a*(4-a))
    H = A*A + 6*A + 1
    D = 3*A**4 + 16*A**3 + 22*A*A + 24*A - 1
    assert t == psi*H/D
    assert v3(t) == v3(psi) == 2
    assert v3(H) == v3(D) == 0
    ell_over_3 = mod3(t/9)  # formal-log omitted tail has valuation >= 3
    h = mod3(2*log_unit_delta(psi/t)/9)
    alpha9 = h*pow(ell_over_3**2, -1, 3) % 3
    Zprincipal = 1/(3*t) - 24/(9*psi)
    assert Zprincipal == -(A+3)*(3*A+1)/(3*H)
    assert v3(Zprincipal) == -1

    Ap = -2*A
    Bp = A*(A+4)
    Q = (d, d)  # actual point is (d,d*s)
    Q3 = add_scaled(add_scaled(Q, Q, Ap, Bp, d), Q, Ap, Bp, d)
    tbar = -Q3[0]/(d*Q3[1])  # t(3Q)=s*tbar
    psiQ = 3*d**4 + 4*Ap*d**3 + 6*Bp*d*d - Bp*Bp
    assert v3(tbar) == v3(psiQ) == 2
    R = psiQ/(d*tbar)  # psiQ/t(3Q)=s*R
    lamQ = mod3(log_unit_delta(d*R*R)/9)
    m_over_3_squared = mod3(d*(tbar/9)**2)
    K = (lamQ - 2*alpha9*m_over_3_squared) % 3
    C = (2*alpha9*pow(mod3(d), -1, 3)) % 3
    ZQprincipal_over_s = 1/(3*d*tbar) - 8*d**4/(3*psiQ)
    assert v3(ZQprincipal_over_s) == -1
    assert ell_over_3 == h == alpha9 == 2
    assert m_over_3_squared == 1 and K == C == 1
    assert (a-1) % 3 == 0 and (7-a) % 3 == 0
    print(f'a={a}: ell/3=h=9alpha=2, K=C=1 mod3; both zeta valuations=-1: PASS')


if __name__ == '__main__':
    for a in (-5, 5827, 11659, -5837, -157469, 23323, 10631731):
        check_parameter(a)
    # An exact local-target obstruction inside the analytic progression.
    a = 23323
    assert a+1 == 4*7**3*17 and (a+5) % (8*3**6) == 0
    d = (a+1)//2
    value = d*(7**6+1)+(8-d)*(7**4+7**2)
    assert value % 49 == 0 and (value//49) % 7 == 1
    assert 3*3 % 7 == 2
    assert v3(7**2-1) == v3(3) == 1
    print('a=23323: u=7 is Q7-visible and -(4/3)log3(7) is a target unit: PASS')
    a = 10631731
    assert a+1 == 4*17**3*541 and (a+5) % (8*3**6) == 0
    assert all(541 % n for n in range(2, 24))
    assert 6*6 % 17 == 2 and v3(17**2-1) == 2 > v3(3)
    print('a=10631731: refined target criterion passes despite multiplicity 3: PASS')
    print('The analytic checks alone do not certify rank or global target conditions.')
