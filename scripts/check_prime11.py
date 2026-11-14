#!/usr/bin/env python3
"""Exact certificates for a=-157469, p=11. Standard library only.
Companion proof: proofs/prime11_isolation.md.
"""
from fractions import Fraction as F
from check_prime7 import vp, mod


def add(P, Q, A, B, d):
    """Coordinates are (X,Ybar) with actual Y=s Ybar and s^2=d."""
    if P is None:
        return Q
    if Q is None:
        return P
    x, y = P
    z, v = Q
    assert d*y*y == x**3+A*x*x+B*x
    if x == z and y == -v:
        return None
    slope = ((v-y)/(z-x) if x != z else
             (3*x*x+2*A*x+B)/(2*d*y))
    xx = d*slope*slope-A-x-z
    yy = slope*(x-xx)-y
    assert d*yy*yy == xx**3+A*xx*xx+B*xx
    return xx, yy


def multiply(P, n, A, B, d):
    Q = None
    for _ in range(n):
        Q = add(Q, P, A, B, d)
    return Q


def division5(x, A, B):
    """Return psi5 and its ordinary X-derivative, using Y^2=g(X)."""
    g = x**3+A*x*x+B*x
    gp = 3*x*x+2*A*x+B
    q = 3*x**4+4*A*x**3+6*B*x*x-B*B
    qp = 12*x**3+12*A*x*x+12*B*x
    H = x**6+2*A*x**5+5*B*x**4-5*B*B*x*x-2*A*B*B*x-B**3
    Hp = 6*x**5+10*A*x**4+20*B*x**3-10*B*B*x-2*A*B*B
    psi = 32*g*g*H-q**3
    deriv = 64*g*gp*H+32*g*g*Hp-3*q*q*qp
    return psi, deriv


def constants5(P, A, B, d):
    Q = multiply(P, 5, A, B, d)
    tbar = -Q[0]/(d*Q[1])  # actual t(5P)=s*tbar
    psi, deriv = division5(P[0], A, B)
    V = psi*psi/(d*tbar*tbar)  # (psi5/t(5P))^2
    assert vp(V, 11) == 0
    # log(V)/11 mod11 from Fermat's quotient; higher log terms are 121-integral.
    vv = mod(V, 121)
    logoverp = ((pow(vv, 10, 121)-1)//11)*pow(10, -1, 11) % 11
    heightoverp = logoverp*pow(25, -1, 11) % 11
    Zbar = 1/(5*d*tbar)-2*P[1]*deriv/(25*psi)
    assert vp(Zbar, 11) >= 0
    return tbar, heightoverp, Zbar, vv


def main():
    a, p = -157469, 11
    A, d = F(a-3), F(a+1, 2)
    P = (F(1), F(1))
    tP, hP, ZP, VP = constants5(P, A, -A, F(1))
    assert vp(tP, p) == 1
    assert mod(tP/(5*p), p) == 1
    assert hP == 8 and mod(ZP, p) == 1
    palpha = hP*pow(mod(tP/(5*p), p)**2, -1, p) % p
    assert palpha == 8

    Q = (d, d)
    tQ, hQ, ZQbar, VQ = constants5(Q, -2*A, A*(A+4), d)
    assert vp(tQ, p) == 2
    assert hQ == 5 and mod(ZQbar, p) == 10
    dd = mod(d, p*p)
    logdoverp = ((pow(dd, p-1, p*p)-1)//p)*pow(p-1, -1, p) % p
    assert logdoverp == 10
    Koverp = (hQ-logdoverp) % p  # 2alpha*m^2 has valuation at least3.
    C = 2*palpha*pow(mod(d, p), -1, p) % p
    assert (Koverp, C) == (6, 4)

    R = (F(2), F(2))  # actual R=(2,2s) on E.
    R2 = add(R, R, A, -A, d)
    tR, _, _, _ = constants5(R2, A, -A, d)  # t(10R)=s*tR
    assert vp(tR, p) == 2
    psi, deriv = division5(R2[0], A, -A)
    Dlogpsi5bar = 2*R2[1]*deriv/psi
    Dlogpsi2bar = (3*R[0]**2+2*A*R[0]-A)/(d*R[1])
    ZRbar = 1/(10*d*tR)-Dlogpsi5bar/50-Dlogpsi2bar/4
    assert mod(ZRbar, p*p) == 109
    Lrscaled = mod(tR/(10*p*p), p)
    assert Lrscaled == 4
    Doverp = -4*((mod(ZRbar, p*p)+1)//p+palpha*Lrscaled) % p
    assert Doverp == 8

    points = [(x, y) for x in range(p) for y in range(p)
              if (y*y-x**6-a*x**4-a*x*x-1) % p == 0]
    assert points == [(0, 1), (0, 10), (1, 4), (1, 7), (10, 4), (10, 7)]
    for t in range(p):
        first = t*(Doverp-C*t*t) % p
        second = (Koverp+C*t*t) % p
        assert first != 0 or second != 0
    print('a=-157469, p=11: PASS')
    print('P: L/11=1, h/11=8, 11alpha=8, zeta(P)=1 mod11; square-ratio mod121:', VP)
    print('Q: v11(L)=2, lambda(Q)/11=5, zeta(Q)/s=10 mod11; square-ratio mod121:', VQ)
    print('log11(d)/11=10, K/11=6, C=4 mod11')
    print('R: zeta(R)/s=109 mod121, L(R)/(121s)=4 mod11, D/11=8 mod11')
    print('rho(11t)/121=t(8-4t^2), rho*(11t)/11=6+4t^2 mod11: no common residue root')


if __name__ == '__main__':
    main()
