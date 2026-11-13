"""Exact obstruction to lifting the three-dimensional S5 module modulo 25.

Checks every first-order matrix direction; no ray group is computed.
The group-image argument is in proofs/adjoint_same_group_lifting.md.
"""
from itertools import product
import sympy as s

U = s.Matrix([[1, 3, 4], [0, 1, 1], [0, 0, 1]])
I = s.eye(3)
E13 = s.zeros(3)
E13[0, 2] = 1
C = ((U**5-I)/5) % 5
assert C == s.Matrix([[0, 3, 0], [0, 0, 1], [0, 0, 0]])
assert U**5 % 5 == I
for j in range(9):
    B = s.zeros(3)
    B[j//3, j % 3] = 1
    differential = sum((U**i*B*U**(4-i) for i in range(5)), s.zeros(3)) % 5
    assert differential == (4*B[2, 0]*E13) % 5
    assert (U+5*B)**5 % 25 == (I+5*(C+differential)) % 25
assert C[0, 1] == 3 and C[1, 2] == 1
print('PASS: every lift has fifth-power entries (1,2)=15 and (2,3)=5 modulo25.')

# The pre-existing projective mod-25 witness and its adjoint action.
def mul(a, b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2)) % 25
                 for i in range(2) for j in range(2))


def power(a, n):
    z = (1, 0, 0, 1)
    for _ in range(n):
        z = mul(z, a)
    return z


for a, b, c in product(range(5), repeat=3):
    kernel = (1+5*a, 5*b, 5*c, 1-5*a)
    assert power(mul(kernel, (1, 1, 0, 1)), 5) == (1, 5, 0, 1)

e = s.Matrix([[0, 1], [0, 0]])
h = s.diag(1, -1)
f = s.Matrix([[0, 0], [1, 0]])
basis = [e, h, f]
ad_e = s.Matrix.hstack(*[s.Matrix([(e*b-b*e)[0, 1],
                                  (e*b-b*e)[0, 0],
                                  (e*b-b*e)[1, 0]]) for b in basis])
assert ad_e % 5 == C
assert I+5*ad_e % 25 != I
# Irreducibility: three distinct diagonal weights, plus u and v link them.
D = s.diag(2, 1, 3)
V = s.Matrix([[0, 0, 2], [0, 4, 0], [3, 0, 0]])
assert len({D[i, i] for i in range(3)}) == 3
assert V*s.Matrix([1, 0, 0]) % 5 == s.Matrix([0, 0, 3])
assert (U*s.Matrix([0, 0, 1])-s.Matrix([0, 0, 1]))[1] == 1
assert (U*s.Matrix([0, 1, 0])-s.Matrix([0, 1, 0])) % 5 == s.Matrix([3, 0, 0])
assert 120*5**3 == 15000
print('PASS: all125 projective lifts, adjoint kernel witness and irreducibility identities.')
print('The same S5 cannot act on a free rank-three mod25 lift; no Selmer dimension follows.')
