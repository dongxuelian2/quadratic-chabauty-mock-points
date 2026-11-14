"""Exact module, modular-resolvent and field-isomorphism checks.

The cohomological and local-conductor arguments are in
proofs/adjoint_quintic_reduction.md. This does not compute a Selmer group.
"""
import sympy as s


def canonical(m):
    first = next(x % 5 for x in m if x % 5)
    return tuple(x * pow(first, -1, 5) % 5 for x in m)


def multiply(a, b):
    return canonical((a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
                      a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3]))


def compose(a, b):
    return tuple(a[b[i]] for i in range(5))


u, v = (1, 1, 0, 1), (0, 1, 3, 0)
generators = [(u, (1, 2, 3, 4, 0)), (v, (1, 0, 2, 3, 4))]
mapping = {(1, 0, 0, 1): tuple(range(5))}
queue = list(mapping)
for a in queue:
    for b, pb in generators:
        ab, pab = multiply(a, b), compose(mapping[a], pb)
        if ab in mapping:
            assert mapping[ab] == pab
        else:
            mapping[ab] = pab
            queue.append(ab)
assert len(mapping) == len(set(mapping.values())) == 120


def adjoint(a):
    m = s.Matrix(2, 2, a)
    inv = m.inv_mod(5)
    columns = []
    for e in [s.Matrix([[0, 1], [0, 0]]), s.diag(1, -1),
              s.Matrix([[0, 0], [1, 0]])]:
        z = m*e*inv
        columns.append(s.Matrix([z[0, 1], z[0, 0], z[1, 0]]) % 5)
    return s.Matrix.hstack(*columns)


def twisted_deleted(perm):
    columns = []
    for i in range(3):
        z = [0]*5
        z[perm[i]] += 1
        z[perm[4]] -= 1
        columns.append(s.Matrix([z[j]-z[3] for j in range(3)]))
    sign = (-1)**sum(perm[i] > perm[j] for i in range(5) for j in range(i+1, 5))
    return sign*s.Matrix.hstack(*columns) % 5


K = s.Matrix([[2, 1, 3], [3, 3, 0], [2, 4, 1]])
assert K.det() % 5 == 1
for a, perm in mapping.items():
    assert (adjoint(a)*K-K*twisted_deleted(perm)) % 5 == s.zeros(3)
    parity = (-1)**sum(perm[i] > perm[j] for i in range(5) for j in range(i+1, 5))
    assert pow((a[0]*a[3]-a[1]*a[2]) % 5, 2, 5) == parity % 5
print("PASS: all 120 projective elements, permutation action, sign and intertwiner.")

x, a = s.symbols("x a")
j = 256*a**3/(a+1)
phi = x**5 + 40*x*x/j - 5*x/j + 1/j
f = x**5 + 10*(a+1)*x*x - 5*a*(a+1)*x + 4*a*a*(a+1)
assert s.cancel((4*a)**5*phi.subs(x, x/(4*a))-f) == 0
disc = 2**4*5**5*a*a*(a+1)**4*(a-3)**2*(2*a+3)**4
assert s.factor(s.discriminant(f, x)-disc) == 0
f = s.Poly(f.subs(a, -157469), x, domain=s.QQ)
g = s.Poly(x**5-1574680*x*x+2362020*x+198368738320, x, domain=s.QQ)
t = s.Poly((4*x**4+2*x**3+x*x-5038975*x+5668848)/2519489, x, domain=s.QQ)
powers = [s.Poly(1, x, domain=s.QQ)]
for _ in range(5):
    powers.append((powers[-1]*t) % g)
assert sum((coeff*powers[k] for (k,), coeff in f.terms()), s.Poly(0,x)) % g == 0
assert s.Matrix([[powers[k].nth(r) for k in range(5)] for r in range(5)]).det() != 0
print("PASS: modular scaling, symbolic discriminant, exact quintic field isomorphism.")

S = {2, 5, 7, 19, 37, 39367}
assert all(s.isprime(q) for q in S)
assert set(s.factorint(2*5*(-157469-3)*(-157469+1))) == S
assert all(q % 5 != 1 for q in S-{5})
# Faithful order-four character occurs in no prime permutation module:
for q in S-{5}:
    order = s.n_order(q, 5)
    assert order > 1 and pow(q, 3, 5) != 1
assert (4/s.pi)**2*s.factorial(4)/4**4*s.sqrt(125) < 2
print("PASS: ramification set, decomposition characters and cyclotomic class-number bound.")
print("No finite/crystalline local conditions or transported target values computed.")
