"""Exact arithmetic in the pointwise ordinary certificate; see its proof.

Recompute with compute_p5_parameter_periods.py -157469 and, independently,
compute_p5_residual_independent.py -157469. Analytic errors are proved in
proofs/actual_noncm_five_adic_period.md, not inferred from these checks.
"""
import json
from pathlib import Path
import sympy as s

root = Path(__file__).resolve().parents[1]
d = json.loads((root/'verification/actual_noncm_p5_period.json').read_text())
a, modulus = -157469, 5**7
assert d['parameter_a'] == a and d['p'] == 5 and d['modulus'] == modulus
assert d['term_cutoff'] == 20 and d['coefficient_precision'] == 30
assert d['theoretical_degree_bound'] == 2868
assert 30-3*4-5 == 13 and 13 >= 7
x, t = s.symbols('x t')
f = x**6+a*x**4+a*x*x+1
assert s.Poly(s.gcd(s.Poly(f, x, modulus=5),
                       s.Poly(s.diff(f, x), x, modulus=5)), x).degree() == 0
assert s.rem(s.diff(f, x), x*x+1, x) == -2*(a-3)*x
M = s.Matrix(d['frobenius_matrix'])
assert M.shape == (5, 5)
assert (s.eye(5)-M).det() % 5 == 4
Me, Mo = M.extract([0, 2, 4], [0, 2, 4]), M.extract([1, 3], [1, 3])
assert all(int(c) % modulus == 0 for c in
           s.Poly(Me.charpoly(t).as_expr()-(t-5)*(t*t+2*t+5), t).all_coeffs())
assert all(int(c) % modulus == 0 for c in
           s.Poly(Mo.charpoly(t).as_expr()-(t*t+2*t+5), t).all_coeffs())
A = (s.eye(6)-s.kronecker_product(Me, Mo)) % modulus
assert A == s.Matrix(d['system_matrix'])
assert A.det() % modulus == 69632
assert A.det() % 5 == 2 == d['system_determinant_mod5']
z = s.Matrix([22100, 73695, 38675, 51468, 35041, 50596])
assert list(z) == d['normalized_cross_periods']
assert (A*z-s.Matrix(d['system_rhs'])) % modulus == s.zeros(6, 1)
assert d['normalized_target'] == 22100 and 22100 % 25 == 0 and 22100 % 125 != 0
assert 2*22100*pow(a-3, -1, modulus) % modulus == d['odd_model_target_J'] == 8275
assert 4*22100 % modulus == 10275
print('PASS: ordinary Frobenius certificate; X=22100 mod5^7 has valuation two.')
print('The zero target is excluded; the two nonzero transported targets remain.')
