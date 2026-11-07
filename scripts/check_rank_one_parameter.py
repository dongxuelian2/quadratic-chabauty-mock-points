#!/usr/bin/env python3
"""Exact 2-isogeny descent upper bound for a=-157469; standard library only.

Every discarded squareclass has an explicit real or finite-modulus obstruction
for its homogeneous descent quartic. Passing classes are not claimed globally
soluble on this basis. The certified bound is combined with the independently
checked nonzero elliptic logarithm of P for exact rank one.
"""
from itertools import product
from math import isqrt, prod
from check_general_prime3 import check_parameter

A_PARAM = -157469
A = A_PARAM - 3
B = -A
AP = -2*A
BP = A*(A+4)
MODULI = ((2, 8), (7, 2), (19, 2), (37, 2))


def factor(n):
    n = abs(n)
    answer = {}
    q = 2
    while q*q <= n:
        while n % q == 0:
            answer[q] = answer.get(q, 0) + 1
            n //= q
        q += 1
    if n > 1:
        answer[n] = answer.get(n, 0) + 1
    return answer


def squarefree_divisors(B):
    ps = tuple(factor(B))
    return sorted(sign*prod(q for q, bit in zip(ps, bits) if bit)
                  for bits in product((0, 1), repeat=len(ps))
                  for sign in (-1, 1))


def real_possible(d, A, B):
    # N^2=d U^4+A U^2 V^2+(B/d)V^4. A necessary real test.
    if d > 0 or B//d > 0:
        return True
    # Both endpoint coefficients are negative. For V!=0 this is a
    # downward quadratic in r=(U/V)^2>=0; its maximum can be >=0
    # only if its vertex is positive and its discriminant is >=0.
    return A > 0 and A*A-4*B >= 0


def residue_witness(d, A, B, p, k):
    """Return one primitive projective residue witness, or None.

    If V is a unit, scale to V=1. Otherwise U is a unit and we scale
    to U=1, with V divisible by p. These are exhaustive over Z/p^k.
    """
    m = p**k
    squares = {n*n % m for n in range(m)}
    for t in range(m):
        if (d*t**4+A*t*t+B//d) % m in squares:
            return (t, 1)
    for t in range(0, m, p):
        if (d+A*t*t+(B//d)*t**4) % m in squares:
            return (1, t)
    return None


def bound_side(label, A, B, expected_counts, expected_final):
    candidates = squarefree_divisors(B)
    discarded = []
    for d in candidates[:]:
        if not real_possible(d, A, B):
            candidates.remove(d)
            discarded.append((d, 'real place'))
    counts = [len(candidates)]
    for p, k in MODULI:
        survivors = []
        for d in candidates:
            if residue_witness(d, A, B, p, k) is None:
                discarded.append((d, f'mod {p}^{k}'))
            else:
                survivors.append(d)
        candidates = survivors
        counts.append(len(candidates))
    assert counts == expected_counts, (label, counts)
    assert candidates == sorted(expected_final), (label, candidates)
    print(f'{label}: candidate counts after real place, 2^8, 7^2, 19^2, 37^2: {counts}')
    print(f'{label}: surviving squareclasses: {candidates}')
    print(f'{label}: complete exclusion list:')
    for d, reason in sorted(discarded):
        print(f'  {d}: {reason}')
    return len(candidates)


if __name__ == '__main__':
    assert A == -32*7*19*37
    assert A_PARAM+1 == -4*39367
    assert factor(39367) == {39367: 1}
    assert factor(B) == {2: 5, 7: 1, 19: 1, 37: 1}
    assert factor(BP) == {2: 7, 7: 1, 19: 1, 37: 1, 39367: 1}
    assert (A_PARAM+5) % (8*3**6) == 0
    n = bound_side('E', A, B, [16, 8, 4, 2, 2], [1, 9842])
    np = bound_side('Eprime', AP, BP, [64, 24, 12, 6, 4],
                    [1, -39367, -9842, 387450014])
    assert n*np == 8
    print('2-isogeny formula: 2^rank <= 2, hence rank <= 1.')
    check_parameter(A_PARAM)
    print('v3(L(P))=1, so P is nontorsion and rank >= 1.')
    print('EXACT CONCLUSION: rank E(Q) = rank Eprime(Q) = 1.')
    print('The odd-prime exponents of a+1 are all 1, hence prime to 3.')
