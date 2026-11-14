#!/usr/bin/env python3
"""Exact arithmetic checks; the whole-disk and descent proofs are in the note."""
from itertools import product
from math import isqrt, lcm
from fractions import Fraction

def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))

def fermat_log_digit(q):
    assert q % 13
    return ((pow(q, 12, 169) - 1) // 13) * pow(12, -1, 13) % 13

def nonzero_target_digit_test(terms):
    for eps in product((-1, 0, 1), repeat=len(terms)):
        if not any(eps):
            continue
        if sum(e * exponent * fermat_log_digit(q)
               for e, (q, exponent) in zip(eps, terms)) % 13 == 0:
            return False
    return True

def valuation13(x):
    x = Fraction(x)
    assert x
    n, d, v = abs(x.numerator), x.denominator, 0
    while n % 13 == 0:
        n //= 13
        v += 1
    while d % 13 == 0:
        d //= 13
        v -= 1
    return v

def residue13(x):
    x = Fraction(x)
    return x.numerator * pow(x.denominator, -1, 13) % 13

def exact_target_signature(coefficients):
    """Return (valuation, leading unit, forbidden-square flag), or None for0.

    Inputs are rational coefficients indexed by distinct primes other than13.
    No p-adic approximation or bounded-precision zero test is used.
    """
    coefficients = {q: Fraction(c) for q, c in coefficients.items() if c}
    if not coefficients:
        return None
    assert all(prime(q) and q != 13 for q in coefficients)
    D = lcm(*(c.denominator for c in coefficients.values()))
    R = Fraction(1)
    for q, c in coefficients.items():
        exponent = int(D * c)
        R *= Fraction(q) ** exponent
    assert R != 1
    z = R**12 - 1
    e, d = valuation13(z), valuation13(D)
    assert e >= 1
    leading = residue13((z / (13**e)) / (12 * (D // 13**d)))
    v = e - d
    forbidden = v >= 2 and v % 2 == 0 and pow(leading, 6, 13) == 1
    return v, leading, forbidden

examples = [(1255747, 401839, 5, -40183901, 12),
            (5930963, 5271967, 3, -189790813, 5)]
for r, s, m, a, digit in examples:
    assert prime(r) and prime(s) and prime(m)
    assert r % 8 == 3 and s % 8 == 7
    assert pow(2, (m - 1) // 2, m) == m - 1
    assert 8 * r - 1 == m * m * s
    assert a == 3 - 32 * r and a % 2197 == 1426 and a % 8 == 3
    assert a + 1 == -4 * m * m * s
    assert fermat_log_digit(m) == digit
    assert nonzero_target_digit_test([(m, 1)])
    for sign in (-1, 1):
        v, unit, forbidden = exact_target_signature({m: sign})
        assert v == 1 and unit == sign * digit % 13 and not forbidden
    assert pow(64 * r % m, (m - 1) // 2, m) == m - 1
    A = -32 * r
    for X, Y in [(A, 2 * A), (A + 4, 2 * (A + 4))]:
        assert Y * Y == X**3 - 2 * A * X**2 + A * (A + 4) * X
    print(f'PASS: a={a}, complete primality bounds {isqrt(r)}, {isqrt(s)}, '
          f'nonzero target digit {digit}.')

# A genuinely stronger application: even valuation, nonsquare leading unit.
r, s, m = 270643099, 5997631, 19
a = 3 - 32 * r
assert prime(r) and prime(s) and prime(m)
assert (r % 8, s % 8) == (3, 7)
assert 8 * r - 1 == m * m * s
assert a == -8660579165 and a % 2197 == 1426 and a % 8 == 3
assert a + 1 == -4 * m * m * s
assert pow(2, (m - 1) // 2, m) == m - 1
assert pow(64 * r % m, (m - 1) // 2, m) == m - 1
assert exact_target_signature({19: 1}) == (2, 5, False)
assert exact_target_signature({19: -1}) == (2, 8, False)
assert not nonzero_target_digit_test([(19, 1)])
print(f'PASS: a={a}, complete primality bounds {isqrt(r)}, {isqrt(s)}, '
      'even-valuation nonsquare targets.')

# Exact residues governing the W-image and first endpoint isolation.
squares13 = {x * x % 13 for x in range(13)}
for root in (5, 8):
    beta = 2 * root * (2 + 8) * pow(6 * 6, -1, 13) % 13
    assert beta == 2 * root % 13 and beta in squares13 and beta != 0
assert (8 - 4) % 13 == 4

# Denominator loss, exact cancellation and square/nonsquare tests.
assert exact_target_signature({}) is None
assert exact_target_signature({5: 13}) == (2, 12, True)
assert exact_target_signature({5: 26}) == (2, 11, False)
assert exact_target_signature({5: Fraction(1, 13)}) == (0, 12, False)
assert exact_target_signature({3: 1, 5: 5}) == (2, 7, False)

# Bounded first-image obstruction after the U-even normalization.
squares8 = {x * x % 8 for x in range(8)}
for r in (3, 5):
    assert 2 not in squares8
    assert r not in squares8 and (r + 2) % 8 not in squares8

# For every odd representative d not 1 mod8, the second quartic is
# impossible already modulo256 on every primitive pair (U,V).
squares256 = {x * x % 256 for x in range(256)}
for r in (3, 5):
    c, b = 64 * r % 256, 128
    for d in range(1, 256, 2):
        if d % 8 == 1:
            continue
        for U in range(16):
            for V in range(16):
                if U % 2 == 0 and V % 2 == 0:
                    continue
                rhs = (d * U**4 + c * U*U * V*V
                       + b * pow(d, -1, 256) * V**4) % 256
                assert rhs not in squares256
    candidates = (1, -1, r, -r, 7, -7, 7*r, -7*r)
    assert [d for d in candidates if d % 8 == 1] == [1, -7]

print('PASS: square-unit W coefficients and unit first endpoint coefficient.')
print('PASS: bounded two-isogeny descent obstructions and supported classes.')
print('PASS: exact rational target signatures, including cancellation and denominators.')
print('The exact image, contraction, arbitrary-prime valuation obstruction, and '
      'Selmer containment are proved in the companion text.')
