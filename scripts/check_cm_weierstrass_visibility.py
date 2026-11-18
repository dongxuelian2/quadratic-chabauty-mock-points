#!/usr/bin/env python3
"""Exact arithmetic for rational_cm_all_good_primes.md; standard library."""
from fractions import Fraction as F
from math import comb


def valuation_two(q):
    q = F(q)
    assert q
    n, d, v = q.numerator, q.denominator, 0
    while n % 2 == 0:
        n //= 2
        v += 1
    while d % 2 == 0:
        d //= 2
        v -= 1
    return v, n * pow(d, -1, 8) % 8


def square_two(q):
    if not q:
        return True
    v, unit = valuation_two(q)
    return v % 2 == 0 and unit == 1


def transform(a):
    return (15-a)/(a+1)


packet = [F(0), F(-3, 2), F(-15, 16), F(-5), F(15), F(-33), F(255)]
obstructions = [-a-1 if a != -5 else 3-a for a in packet]
expected = [(0, 7), (-1, 1), (-4, 7), (3, 1), (4, 7), (5, 1), (8, 7)]
assert not square_two(-1)
for a, obstruction, signature in zip(packet, obstructions, expected):
    assert valuation_two(obstruction) == signature
    assert not square_two(obstruction)
    assert not (square_two(-a-1) and square_two(3-a))
    assert transform(a) in packet
    assert transform(transform(a)) == a
print('PASS: no Q2 Weierstrass points for all seven rational-CM parameters.')

# Coefficientwise identity (4), separately for the constant and linear
# coefficient in a. No evaluation/interpolation assumption is used.
for degree in range(7):
    constant = comb(6, degree)*((-1)**(6-degree)+1)
    linear = 0
    for left, right in [(4, 2), (2, 4)]:
        for j in range(left+1):
            k = degree-j
            if 0 <= k <= right:
                linear += comb(left, j)*(-1)**(left-j)*comb(right, k)
    assert constant == {0: 2, 2: 30, 4: 30, 6: 2}.get(degree, 0)
    assert linear == {0: 2, 2: -2, 4: -2, 6: 2}.get(degree, 0)
print('PASS: exact Mobius identity including its essential twist multiplier.')

for p in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
    squares = {x*x % p for x in range(p)}
    for a in range(p):
        if a in [(-1) % p, 3 % p]:
            continue
        actual = sum((x**6+a*x**4+a*x*x+1) % p == 0 for x in range(p))
        predicted = 2*((-1) % p in squares) + 4*((-a-1) % p in squares and (3-a) % p in squares)
        assert actual == predicted, (p, a, actual, predicted)
print('PASS: fieldwise visibility formula on every smooth parameter over ten odd prime fields.')
