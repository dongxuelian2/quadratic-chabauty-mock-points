#!/usr/bin/env python3
"""Exact arithmetic checks for the prime-3 height nonvanishing certificate.

Only Python's standard library is required. The all-orders analytic estimate
is proved in the companion note, not inferred from these finite checks.
"""
from fractions import Fraction as F


def v3(x):
    x = F(x)
    if not x:
        return float("inf")
    n, d, value = abs(x.numerator), x.denominator, 0
    while n % 3 == 0:
        n //= 3
        value += 1
    while d % 3 == 0:
        d //= 3
        value -= 1
    return value


def floor_log3(n):
    assert n >= 1
    result = 0
    while n >= 3:
        n //= 3
        result += 1
    return result


def residue(x, modulus):
    x = F(x)
    return (x.numerator * pow(x.denominator, -1, modulus)) % modulus


def on_curve(point):
    if point is None:
        return True
    x, y = point
    return y * y == x**3 - 8 * x**2 + 8 * x


def add(p, q):
    if p is None:
        return q
    if q is None:
        return p
    x, y = p
    u, v = q
    if x == u and y == -v:
        return None
    slope = ((v - y) / (u - x) if x != u
             else (3 * x**2 - 16 * x + 8) / (2 * y))
    z = slope**2 + 8 - x - u
    answer = (z, slope * (x - z) - y)
    assert on_curve(answer)
    return answer


P = (F(1), F(1))
Q = add(add(P, P), P)
assert Q == (F(289, 2025), F(90287, 91125))
t = -Q[0] / Q[1]
assert t == F(-765, 5311) and v3(t) == 2
psi3 = 3 * P[0]**4 - 32 * P[0]**3 + 48 * P[0]**2 - 64
assert psi3 == -45
assert t / psi3 == F(17, 5311)

# With T=t^2, U^2-(1+8T)U+8T^2=0, X=t^-2 U.
N = 80
u = [1]
for n in range(1, N + 2):
    u.append(8 * u[n - 1] - sum(u[i] * u[n-i] for i in range(1, n))
             - (8 if n == 2 else 0))
assert u[:5] == [1, 8, -8, 64, -576]

# w=1-T U'/U, calculated from U*w=U-T U'.
w = [1]
for n in range(1, N + 1):
    w.append((1 - n) * u[n] - sum(u[i] * w[n-i] for i in range(1, n + 1)))
assert w[:4] == [1, -8, 80, -896]

# -(X-2)w = -t^-2 + sum a[k]*t^(2k).
a = [k * u[k + 1] + 2 * w[k] for k in range(N)]
b = [F(0)]
for k in range(1, N + 1):
    b.append((F(w[k]) + sum(F(a[j] * w[k-j-1], 2*j+1)
                                for j in range(k))) / (2*k))
assert b[1:5] == [F(-3), F(14), F(-512, 5), F(31624, 35)]
for k in range(1, N + 1):
    bound = -v3(2*k) - floor_log3(2*k-1)
    assert v3(b[k]) >= bound
    if k >= 2:
        assert 4*k + bound >= 7

# Independently generate the second model's series. For
# y^2=x^3+A*x^2+B*x, U^2-(1-A*T)U+B*T^2=0.
# The complementary differential for E' is (x+4)*omega'.
u_prime = [1]
for n in range(1, N + 2):
    u_prime.append(-16 * u_prime[n - 1]
                   - sum(u_prime[i] * u_prime[n-i] for i in range(1, n))
                   - (32 if n == 2 else 0))
w_prime = [1]
for n in range(1, N + 1):
    w_prime.append((1 - n) * u_prime[n]
                   - sum(u_prime[i] * w_prime[n-i] for i in range(1, n + 1)))
a_prime = [k * u_prime[k + 1] - 4 * w_prime[k] for k in range(N)]
b_prime = [F(0)]
for k in range(1, N + 1):
    b_prime.append((F(w_prime[k])
                    + sum(F(a_prime[j] * w_prime[k-j-1], 2*j+1)
                          for j in range(k))) / (2*k))
assert b_prime[1:5] == [F(6), F(56), F(4096, 5), F(505984, 35)]
for k in range(1, N + 1):
    assert v3(b_prime[k]) >= -v3(2*k) - floor_log3(2*k-1)

delta = F(-5328, 17)
assert 1 + delta == F(-5311, 17)
assert v3(delta) == 2
assert residue(delta / 9, 3) == 1
assert residue(2 * delta / 9, 3) == 2

# Additional finite exact check, with separate analytic tail estimates:
# log(1+delta) through n=12 is correct mod 3^24 because
# 2n-v3(n)>=24 for every n>=13; B through k=7 is correct mod 3^26.
log_approx = sum((-1)**(n+1) * delta**n / n for n in range(1, 13))
B_approx = sum(b[k] * t**(2*k) for k in range(1, 8))
h_approx = (2 * log_approx - 2 * B_approx) / 9
assert v3(log_approx) == 2
assert v3(B_approx) == 5
assert v3(h_approx) == 0
assert residue(h_approx, 3) == 2

# Constants needed for uniform residue-disk isolation.
LQ = sum(F(w[k], 2*k+1) * t**(2*k+1) for k in range(8))
L = LQ / 3
ZQ = 1/t + sum(F(a[k], 2*k+1) * t**(2*k+1) for k in range(8))
Z = ZQ / 3 + F(8, 135)
assert v3(L) == 1 and residue(L / 3, 3) == 2
assert v3(Z) == -1 and residue(3 * Z, 3) == 1
assert F(1, 3) / t + F(8, 135) == F(-115, 51)
for k in range(1, 1000):
    assert 2*k - 2 - v3(2*k) >= 0
    assert 2*k - v3(2*k+1) >= 1
    if k >= 2:
        assert 2*k - 2 - v3(2*k) - floor_log3(2*k-1) >= 1
        assert 2*k - 2 - v3(2*k) - floor_log3(2*k-2) >= 2
assert {r*r % 3 for r in range(3)} == {0, 1}
assert all((2 - r*r) % 3 for r in range(3))
assert all((x**6 - 5*x**4 - 5*x*x + 1) % 16 == 8
           for x in range(1, 16, 2))
affine_f3 = [(x, y) for x in range(3) for y in range(3)
             if (y*y - (x**6 - 5*x**4 - 5*x*x + 1)) % 3 == 0]
assert len(affine_f3) == 6
assert all(y in (1, 2) for x, y in affine_f3)

print("Exact rational group law: PASS")
print("Third division polynomial: PASS")
print("Formal integral coefficients through degree", 2*N, ": PASS")
print("Second-model formal coefficients, including quadratic coefficient 6: PASS")
print("All checked coefficients satisfy the proven valuation bound: PASS")
print("v3(t(3P)) =", v3(t))
print("v3(log(5311/17)) = 2; v3(B(t(3P))) = 5")
print("h3(P) = 2 mod 3; in particular h3(P) is nonzero")
print("Extra residue check modulo 3^10:", residue(h_approx, 3**10))
print("Logarithm and zeta constants for residue-disk isolation: PASS")
print("Integral coefficient bound checks, F3 disks, and F2 obstruction: PASS")
