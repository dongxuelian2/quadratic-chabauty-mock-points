#!/usr/bin/env python3
"""Exact checks for two proved rank-one patterns; standard library only.

The symbolic rank proofs are in proofs/checkable_rank_patterns.md.
Primality here is certified by exhaustive integer trial division.
No probabilistic primality, analytic-rank oracle or numerical Selmer oracle.
"""
from math import isqrt
from check_general_prime3 import check_parameter


def factor(n):
    n = abs(n)
    out = {}
    while n % 2 == 0:
        out[2] = out.get(2, 0) + 1
        n //= 2
    q = 3
    while q*q <= n:
        while n % q == 0:
            out[q] = out.get(q, 0) + 1
            n //= q
        q += 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def prime(n):
    return n >= 2 and factor(n) == {n: 1}


def sqclass(n):
    answer = -1 if n < 0 else 1
    for p, e in factor(n).items():
        if e % 2:
            answer *= p
    return answer


def multiply_classes(x, y):
    # x,y are signed squarefree integers.
    from math import gcd
    return x*y // gcd(abs(x), abs(y))**2


def residue_possible(d, A, B, modulus):
    """Primitive projective pairs modulo a power of 2, exhaustively."""
    assert B % d == 0
    squares = {x*x % modulus for x in range(modulus)}
    for u in range(modulus):  # V is a unit, scale it to 1.
        if (d*u**4 + A*u*u + B//d) % modulus in squares:
            return True
    for v in range(0, modulus, 2):  # Otherwise U unit; scale it to 1.
        if (d + A*v*v + (B//d)*v**4) % modulus in squares:
            return True
    return False


def check_uniform_two_adic_arguments():
    # E in Theorem 1: coefficients modulo 128 depend only on p mod 8.
    for p in (3, 5):
        assert not residue_possible(2, -32*p, 32*p, 128)

    # E' odd-d lemma: c is 64 times an odd number and B/d is
    # 128 times an odd number. Exhaust all c,d and (B/d) residues
    # relevant modulo 256, independently of the primality pattern.
    for c in (64, 192):
        for d in range(1, 256, 2):
            if d % 8 == 1:
                continue
            assert not residue_possible(d, c, d*128, 256)

    # E in Theorem 2: r=3 or11 mod16, c=-8 mod16,
    # and B/r=8 mod16. This is independent of other factors of n.
    for r in (3, 11):
        assert not residue_possible(r, -8, 8*r, 16)

    print('Uniform 2-adic obstructions: exhaustive residue checks PASS.')


def check_known_points(A):
    Ap, Bp = -2*A, A*(A+4)
    for x in (A, A+4):
        y = 2*x
        assert y*y == x**3 + Ap*x*x + Bp*x
    H = {1, sqclass(A), sqclass(A+4), sqclass(Bp)}
    assert len(H) == 4
    for x in H:
        for y in H:
            assert multiply_classes(x, y) in H
    return H


def check_linear(p):
    q = 8*p - 1
    assert p % 8 in (3, 5)
    assert p % 729 == 547
    assert prime(p) and prime(q)
    A, a = -32*p, 3-32*p
    assert (a+5) % 5832 == 0 and a+1 == -4*q
    assert not residue_possible(2, A, -A, 128)
    odd_candidates = {s*p**i*q**j
                      for s in (-1, 1) for i in (0, 1) for j in (0, 1)}
    assert {d for d in odd_candidates if d % 8 == 1} == {1, -q}
    for d in odd_candidates - {1, -q}:
        assert not residue_possible(d, -2*A, A*(A+4), 256)
    H = check_known_points(A)
    assert H == {1, -2*p, -q, 2*p*q}
    print(f'LINEAR: p={p}, q={q}, a={a}; primes certified by trial division.')
    print(f'  Descent images: [1, {2*p}], {sorted(H)}; rank = 1.')
    check_parameter(a)
    print('  a+1=-4q; both actual targets are {0}; full depth-two equality certified.')


def legendre(a, p):
    value = pow(a % p, (p-1)//2, p)
    return -1 if value == p-1 else value


def check_quadratic(n):
    fac = factor(n)
    assert n > 1 and n % 2 == 1
    assert all(prime(p) and p % 8 in (3, 5) for p in fac)
    distinguished = [p for p, e in fac.items() if p % 8 == 3 and e % 2]
    assert len(distinguished) == 1
    r = distinguished[0]
    D = 2*n*n-1
    assert prime(D)
    assert n % 729 in (1, 728)
    A, a = -8*n*n, 3-8*n*n
    assert (a+5) % 5832 == 0 and a+1 == -4*D
    for p, e in fac.items():
        assert legendre(2, p) == -1
        assert legendre(-2, p) == (1 if p % 8 == 3 else -1)
        if p != r:
            assert e % 2 == 0 or legendre(-2, p) == -1
    assert fac[r] % 2 == 1
    assert legendre(-1, r) == legendre(32, r) == -1
    assert not residue_possible(r, A, -A, 16)
    H = check_known_points(A)
    assert H == {1, -2, -D, 2*D}
    print(f'QUADRATIC: n={n}, factors={fac}, D={D}, a={a}; primes certified.')
    print(f'  Distinguished prime r={r}; descent images [1, 2], {sorted(H)}; rank = 1.')
    check_parameter(a)
    print('  a+1=-4D; both actual targets are {0}; full depth-two equality certified.')


if __name__ == '__main__':
    check_uniform_two_adic_arguments()
    for p in (6379, 12211, 19501, 48661, 159469):
        check_linear(p)
    for n in (2915, 8747, 11663, 29159, 32075):
        check_quadratic(n)
    print('PASS: ten new parameters certified, with no infinitude assertion.')
