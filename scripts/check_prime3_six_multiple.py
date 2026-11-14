#!/usr/bin/env python3
"""Standalone exact-arithmetic audit using 6P rather than just 3P.

Preserves the additional computation performed during the independent audit.
Python standard library only; no import of the author's verification script.

For E: y^2=x^3-8x^2+8x, P=(1,1), and the audited normalized
height lambda=-2 log_3(t)-2 B(t), multiplication first by 2 and then
by 3 gives

  36 h(P) = 2 log_3(2^9 psi_3(2P)/t(6P)) - 2 B(t(6P)).

We compare this with the 3P identity, using exact rational arithmetic.
The analytic normalization is an input from the audited proof; this script
does not independently construct a Coleman-Gross height.

The all-orders truncation estimates, not numerical experimentation, justify
the displayed residues. If v_3(t)=2 and

  v_3(b_{2k}) >= -v_3(2k)-floor(log_3(2k-1)),

then for k>=8 the omitted B terms have valuation at least 2k+2>=18.
Here we use v_3(2k)<=k-1 and floor(log_3(2k-1))<=k-1 for k>=3.
For a logarithm increment of valuation 2, the omitted terms after n=9
have valuation 2n-v_3(n)>=20: check 10<=n<=18 explicitly; for n>=19
use v_3(n)<=n-1. These termwise bounds tend to infinity.
Division by 9 or 36 loses two powers of 3, so both approximations below
are certified modulo 3^16, more than needed for the modulo-3^10 check.
"""

from fractions import Fraction as F


def valuation3(value):
    value = F(value)
    if value == 0:
        return float("inf")
    numerator, denominator = abs(value.numerator), value.denominator
    result = 0
    while numerator % 3 == 0:
        numerator //= 3
        result += 1
    while denominator % 3 == 0:
        denominator //= 3
        result -= 1
    return result


def residue(value, modulus):
    value = F(value)
    assert value.denominator % 3 != 0
    return value.numerator * pow(value.denominator, -1, modulus) % modulus


def on_curve(point):
    if point is None:
        return True
    x, y = point
    return y * y == x**3 - 8*x*x + 8*x


def add(left, right):
    if left is None:
        return right
    if right is None:
        return left
    x1, y1 = left
    x2, y2 = right
    if x1 == x2 and y1 == -y2:
        return None
    if x1 == x2:
        slope = (3*x1*x1 - 16*x1 + 8) / (2*y1)
    else:
        slope = (y2-y1) / (x2-x1)
    x3 = slope*slope + 8 - x1 - x2
    result = (x3, slope*(x1-x3)-y1)
    assert on_curve(result)
    return result


def psi3(point):
    x, _ = point
    return 3*x**4 - 32*x**3 + 48*x*x - 64


def parameter(point):
    x, y = point
    return -x/y


def formal_B_coefficients(count):
    """Return b[k]=[t^(2k)]B(t), by the formal differential equations."""
    # X=t^-2 U(T), T=t^2; U^2-(1+8T)U+8T^2=0.
    u = [F(1)]
    for n in range(1, count+2):
        u.append(8*u[n-1] - sum(u[j]*u[n-j] for j in range(1, n))
                 - (8 if n == 2 else 0))
    # omega=w(t)dt and U*w=U-T*U'.
    w = [F(1)]
    for n in range(1, count+1):
        w.append((1-n)*u[n] - sum(u[j]*w[n-j] for j in range(1, n+1)))
    # -(X-2)w=-t^-2 + sum a[j] t^(2j).
    a = [j*u[j+1] + 2*w[j] for j in range(count)]
    b = [F(0)]
    for k in range(1, count+1):
        b.append((w[k] + sum(a[j]*w[k-j-1]/(2*j+1)
                              for j in range(k))) / (2*k))
    assert b[1:5] == [F(-3), F(14), F(-512, 5), F(31624, 35)]
    return b


def logarithm_approximation(value):
    """Remove the 3-power and sign, then sum log(1+delta) through n=9."""
    value = F(value)
    power = int(valuation3(value))
    value /= F(3)**power
    if residue(value, 3) == 2:
        value = -value
    delta = value-1
    assert valuation3(delta) == 2
    approximation = sum(F((-1)**(n+1), n)*delta**n for n in range(1, 10))
    return approximation, delta


def main():
    point = (F(1), F(1))
    twice = add(point, point)
    triple = add(twice, point)
    sixfold = add(triple, triple)
    # Check the two group-law routes to 6P independently.
    assert sixfold == add(add(twice, twice), twice)
    assert twice == (F(49, 4), F(217, 8))
    assert triple == (F(289, 2025), F(90287, 91125))
    t3, t6 = parameter(triple), parameter(sixfold)
    assert valuation3(t3) == valuation3(t6) == 2
    assert psi3(point) == -45

    b = formal_B_coefficients(7)

    def B_truncation(t):
        return sum(b[k]*t**(2*k) for k in range(1, 8))

    log3, delta3 = logarithm_approximation(psi3(point)/t3)
    log6, delta6 = logarithm_approximation(2**9*psi3(twice)/t6)
    assert delta3 == F(-5328, 17)
    for n in range(10, 19):
        assert 2*n-valuation3(n) >= 20

    h_via3 = (2*log3-2*B_truncation(t3))/9
    h_via6 = (2*log6-2*B_truncation(t6))/36
    assert valuation3(h_via3) == valuation3(h_via6) == 0
    assert residue(h_via3, 3) == residue(h_via6, 3) == 2
    assert residue(h_via3, 3**10) == residue(h_via6, 3**10) == 6935
    assert valuation3(h_via6-h_via3) >= 16

    print("Two rational group-law routes to 6P: PASS")
    print("v3(t(3P)) = v3(t(6P)) = 2")
    print("Both normalized logarithm increments have valuation 2")
    print("6P certificate: h3(P) = 2 modulo 3")
    print("Independent 3P and 6P residues modulo 3^10: 6935")
    print("Both truncations have rigorously bounded error in 3^16 Z_3")
    print("v3(difference of rational truncations) =", valuation3(h_via6-h_via3))


if __name__ == "__main__":
    main()
