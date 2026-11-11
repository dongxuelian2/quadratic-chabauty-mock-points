"""Exact local cocycle checks for the adjoint lattice at odd bad primes.

No number-field class group or global Selmer dimension is computed.
The geometric inertia justification is in proofs/adjoint_local_lifting.md.
"""
from itertools import product
from math import gcd
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

A = -157472
delta = 16*A**3*(A+4)
c4 = 16*A*(A+3)
assert s.factorint(abs(A)) == {2: 5, 7: 1, 19: 1, 37: 1}
assert s.factorint(abs(A+4)) == {2: 2, 39367: 1}
for q in (7, 19, 37):
    assert A % q == 0 and A % (q*q) != 0
    # After adjoining pi^4=A and scaling X=pi^2 Z, Y=pi^3 W,
    # the good special fibre is W^2=Z^3-Z, discriminant 64.
    assert 64 % q != 0
assert c4 % 39367 != 0 and delta % 39367 == 0
assert delta % (39367**2) != 0


def adjoint(g, modulus):
    gi = (pow(int(g.det()), -1, modulus)
          * s.Matrix([[g[1, 1], -g[0, 1]], [-g[1, 0], g[0, 0]]])) % modulus
    assert g*gi % modulus == s.eye(2)
    basis = [s.Matrix([[0, 1], [0, 0]]), s.diag(1, -1),
             s.Matrix([[0, 0], [1, 0]])]
    columns = []
    for b in basis:
        z = g*b*gi % modulus
        columns.append(s.Matrix([z[0, 1], z[0, 0], z[1, 0]]))
    return s.Matrix.hstack(*columns)


def power_sum(g, exponent, modulus):
    """Return g**exponent and sum(g**j, j<exponent) by binary recursion."""
    if exponent == 0:
        return s.eye(g.rows), s.zeros(g.rows)
    p, total = power_sum(g, exponent//2, modulus)
    total = (total+p*total) % modulus
    p = p*p % modulus
    if exponent % 2:
        total = (total+p) % modulus
        p = p*g % modulus
    return p, total


def kernel_size(matrix, modulus):
    diagonal = smith_normal_form(matrix, domain=s.ZZ)
    result = modulus**(matrix.cols-min(matrix.shape))
    for i in range(min(matrix.shape)):
        result *= gcd(int(diagonal[i, i]), modulus)
    return result


for q in (7, 19, 37, 39367):
    for n in range(1, 5):
        modulus = 5**n
        if q == 39367:
            inertia = adjoint(s.Matrix([[1, 1], [0, 1]]), modulus)
        else:
            inertia = s.diag(-1, 1, -1) % modulus
        # For quartic inertia only the Frobenius action on its invariant
        # line matters. These matrices realize the required normalizer.
        frobenius = adjoint(s.diag(q, 1) if q % 4 == 1 or q == 39367
                            else s.Matrix([[0, 1], [-q, 0]]), modulus)
        iq, norm = power_sum(inertia, q, modulus)
        assert frobenius*inertia % modulus == iq*frobenius % modulus
        # c(phi)=x, c(tau)=y; phi*tau=tau**q*phi gives this relation.
        relation = s.Matrix.hstack(s.eye(3)-iq, frobenius-norm) % modulus
        coboundary = s.Matrix.vstack(frobenius-s.eye(3), inertia-s.eye(3)) % modulus
        assert relation*coboundary % modulus == s.zeros(3)
        cycles = kernel_size(relation, modulus)
        boundaries = modulus**3//kernel_size(coboundary, modulus)
        order = cycles//boundaries
        expected = 5 if q == 19 else modulus if q == 37 else 1
        assert order == expected
        if q == 19:
            # The inertia h-coordinate is a well-defined class coordinate.
            assert list(coboundary[4, :]) == [0, 0, 0]
            assert list(relation[1, :]) == [0, 0, 0, 0, (-20) % modulus, 0]
            kernel = [z for z in range(modulus) if 20*z % modulus == 0]
            assert len(kernel) == 5
            if n > 1:
                assert {z % (5**(n-1)) for z in kernel} == {0}
        print(f'q={q}, n={n}: #H1={order}')
    if q == 19:
        # Independent exhaustive mod-five quotient: no rank formula.
        modulus = 5
        inertia = s.diag(-1, 1, -1) % modulus
        frobenius = adjoint(s.Matrix([[0, 1], [-q, 0]]), modulus)
        iq, norm = power_sum(inertia, q, modulus)
        rel = s.Matrix.hstack(s.eye(3)-iq, frobenius-norm) % modulus
        cob = s.Matrix.vstack(frobenius-s.eye(3), inertia-s.eye(3)) % modulus
        vectors = list(product(range(5), repeat=3))
        boundaries = {tuple(cob*s.Matrix(z) % 5) for z in vectors}
        representatives = {(0, 0, 0, 0, b, 0) for b in range(5)}
        cycles = {tuple((s.Matrix(r)+s.Matrix(b)) % 5)
                  for r in representatives for b in boundaries}
        brute = {v for v in product(range(5), repeat=6)
                 if all(sum(int(rel[i, j])*v[j] for j in range(6)) % 5 == 0
                        for i in range(3))}
        assert cycles == brute and len(brute) == 5*len(boundaries)

print('PASS: local cohomology orders, exact cocycles, and zero reduction at 19.')
print('No crystalline-at-5 or global target comparison is inferred.')
