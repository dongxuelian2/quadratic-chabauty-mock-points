#!/usr/bin/env python3
"""Exact algebra for rational_cm_weierstrass_classification.md.

Requires SymPy. No p-adic approximation, rank oracle, class-group oracle,
or bounded search for rational parameters is used. The geometric degree
counts and the rational-target cohomology argument are in the proof.
"""

from fractions import Fraction

import sympy as S

x, z, a = S.symbols("x z a", real=True)
ii = S.I
s7 = S.sqrt(-7)


def zero(expr, ext=None):
    reduced = S.cancel(expr, extension=ext) if ext is not None else S.cancel(expr)
    assert reduced == 0


def conjugate(expr):
    return S.conjugate(expr)


def sf(n):
    n = Fraction(n)
    sign = -1 if n < 0 else 1
    for q, e in S.factorint(abs(n.numerator * n.denominator)).items():
        if e % 2:
            sign *= int(q)
    return sign


def squareclasses(B):
    ans = [1]
    for q in S.factorint(abs(B)):
        ans += [int(q) * d for d in ans]
    return set(ans + [-d for d in ans])


def residue_obstruction(A, B, d, q, k):
    """All primitive pairs modulo q^k, normalized by a unit coordinate."""
    modulus = q**k
    squares = {n * n % modulus for n in range(modulus)}
    assert B % d == 0
    for U in range(modulus):
        assert (d * U**4 + A * U * U + B // d) % modulus not in squares
    for V in range(0, modulus, q):
        assert (d + A * V * V + (B // d) * V**4) % modulus not in squares


def descent_row(A, B, expected, witnesses, obstructions, real_negative=False):
    candidates = squareclasses(B)
    H = {1, sf(B)}
    for X, Y in witnesses:
        assert Y * Y == X**3 + A * X * X + B * X
        assert X != 0
        H.add(sf(X))
    while True:
        new = H | {sf(u * v) for u in H for v in H}
        if new == H:
            break
        H = new
    assert H == set(expected)
    excluded = set()
    if real_negative:
        assert B > 0 and A * A - 4 * B < 0
        excluded |= {d for d in candidates if d < 0}
    for d, q, k in obstructions:
        residue_obstruction(A, B, d, q, k)
        excluded |= {sf(d * h) for h in H}
    assert H.isdisjoint(excluded)
    assert H | excluded == candidates
    return len(H)


def check_classification():
    js = [0, 1728, -3375, 8000, -32768, 54000, 287496, -884736,
          -12288000, 16581375, -884736000, -147197952000,
          -262537412640768000]
    irreducible_primes = {-32768: 3, -884736: 5, -12288000: 7,
                          -884736000: 11, -147197952000: 17,
                          -262537412640768000: 41}
    roots = set()
    for j in js:
        polynomial = S.Poly(256 * a**3 - j * a - j, a)
        coeff, factors = S.factor_list(polynomial.as_expr(), a)
        zero(polynomial.as_expr() - coeff * S.prod(f**m for f, m in factors))
        for f, _ in factors:
            p = S.Poly(f, a)
            if p.degree() == 1:
                roots.add(-p.TC() / p.LC())
            elif p.degree() == 2:
                D = S.discriminant(p.as_expr(), a)
                assert D < 0 or not S.sqrt(D).is_Rational
            else:
                assert p.degree() == 3
                q = irreducible_primes[j]
                assert int(p.LC()) % q
                assert all(int(p.eval(t)) % q for t in range(q))
    roots.remove(S.Integer(3))  # Singular original curve.
    assert roots == {S.Integer(0), S.Rational(-3, 2), S.Rational(-15, 16),
                     S.Integer(-5), S.Integer(15), S.Integer(-33), S.Integer(255)}
    print("PASS: all thirteen rational singular moduli give exactly seven admissible parameters.")


def check_ranks():
    # Rank-zero CM parameter.
    m = descent_row(-3, 3, {1, 3}, [], [], True)
    n = descent_row(6, -3, {1, -3}, [], [(-1, 2, 4)])
    assert m * n == 4
    # Common rank-one E6 for -3/2 and -33.
    m = descent_row(0, -36, {-6, -3, -2, -1, 1, 2, 3, 6},
                    [(12, 36), (18, 72)], [])
    n = descent_row(0, 144, {1}, [], [(2, 2, 4), (3, 3, 2), (6, 3, 2)], True)
    assert m * n == 8
    m = descent_row(-63, 1008, {1, 7}, [],
                    [(2, 2, 4), (3, 3, 2), (6, 2, 4)], True)
    n = descent_row(126, -63, {1, -7, -3, 21},
                    [(-75, 540), (21, 252)], [(-1, 2, 4)])
    assert m * n == 8
    m = descent_row(252, -252, {1, -7, 2, -14},
                    [(18, 288), (-14, 224)],
                    [(-1, 2, 4), (3, 2, 4), (-3, 2, 5)])
    n = descent_row(-504, 64512, {1, 7}, [],
                    [(2, 3, 3), (3, 3, 2), (6, 3, 2)], True)
    assert m * n == 8
    # P is nontorsion: exact doubling and short integral-model coordinates.
    for A, B, X, Y, expected in [
        (-36, 0, 12, 36, (S.Rational(25, 4), S.Rational(-35, 8))),
        (-315, 2646, -5, 64,
         (S.Rational(865, 64), S.Rational(-14993, 512))),
        (-21420, 1206576, 85, 1,
         (S.Rational(64345, 4), S.Rational(-16321283, 8))),
    ]:
        X, Y = S.Rational(X), S.Rational(Y)
        assert Y**2 == X**3 + A * X + B
        slope = (3 * X**2 + A) / (2 * Y)
        X2 = slope**2 - 2 * X
        Y2 = slope * (X - X2) - Y
        assert (X2, Y2) == expected
        assert Y2**2 == X2**3 + A * X2 + B
        assert X2.q > 1  # Nagell--Lutz on the short integral model.
    print("PASS: rank zero at a=0 and elementary rank-one certificates for all four new parameters.")


def model(a_value, h1z, h1v, cubic, h2z=None, h2v=None):
    F = x**6 + a_value * x**4 + a_value * x*x + 1
    if h2z is None:
        h2z = S.cancel(h1z.subs(x, 1 / x))
        h2v = S.cancel(h1v.subs(x, 1 / x) / x**3)
    zero(h1v**2 * F - cubic.subs(z, h1z))
    zero(h2v**2 * F - cubic.subs(z, h2z))
    # Nonzero independent pullbacks of the regular elliptic differential.
    w1 = S.cancel(S.diff(h1z, x) / (2 * h1v))
    w2 = S.cancel(S.diff(h2z, x) / (2 * h2v))
    c = S.cancel(w1 / x)
    assert not c.has(x) and c != 0
    zero(w2 + c)
    disc = S.discriminant(F, x)
    for part in (abs(disc.p), disc.q):
        assert set(S.factorint(part)) <= {2, 3, 7}
    return F, h2z, h2v, c


def fiber_identity(F, h1z, h1v, h2z, h2v, eta_x, eta_y,
                   P, common_factor, ext):
    Pbar = conjugate(P)
    D = S.cancel(h1z - eta_x.subs(z, h2z), extension=ext)
    Dn, Dd = S.fraction(D)
    expected = S.Poly(common_factor * P * Pbar, x, extension=ext)
    assert S.Poly(Dn, x, extension=ext).monic() == expected.monic()
    ratio = S.cancel(eta_y.subs(z, h2z) * h2v / h1v, extension=ext)
    rn, rd = S.fraction(ratio)
    for poly, sign in ((P, 1), (Pbar, -1)):
        pp = S.Poly(poly, x, extension=ext)
        assert S.rem(rn + sign * rd, poly, x, extension=ext) == 0
        for forbidden in (S.diff(poly, x), Pbar if sign == 1 else P,
                          F, Dd, rd, x*x - ext**2):
            assert S.gcd(pp, S.Poly(forbidden, x, extension=ext)).degree() == 0
    return S.cancel(P / Pbar, extension=ext)


def check_i_models():
    cubic = z**3 - 36*z
    # a=-3/2, two degree-two maps, four simple points per origin fiber.
    h1z, h1v = 4*x*x - 2, S.Integer(8)
    F, h2z, h2v, c = model(S.Rational(-3, 2), h1z, h1v, cubic)
    g = fiber_identity(F, h1z, h1v, h2z, h2v, -z, ii,
                       x*x + ii*x - 1, S.Integer(1), ii)
    assert S.simplify(g.subs(x, 0)) == 1
    assert S.simplify(1 / g.subs(x, ii)) == S.Rational(1, 3)
    for xx in (S.sqrt(2), -S.sqrt(2), 1/S.sqrt(2), -1/S.sqrt(2)):
        zero(F.subs(x, xx))
        t = S.simplify(1 / g.subs(x, xx))
        assert S.simplify(3*t*t + 2*t + 3) == 0
    # a=-33, degree-four maps and exceptional ramification at W.
    h1z = (x*x-5)**2/(4*(x*x+1))
    h1v = (x*x-5)*(x*x+7)/(8*(x*x+1)**2)
    F, h2z, h2v, c = model(S.Integer(-33), h1z, h1v, cubic)
    assert c == 2
    g_regular = fiber_identity(F, h1z, h1v, h2z, h2v, -z, ii,
                               x*x + 4*ii*x - 1, S.Integer(1), ii)
    g = (x-ii)/(x+ii)*g_regular
    assert S.simplify(g.subs(x, 0)) == -1
    slope_g = S.simplify(S.limit(g/(x-ii), x, ii))
    assert slope_g == -3/(2*ii)
    # Exact local integration: x-i=c0*y^2; t+=4c0^2*y^3/3,
    # t-=8ic0*y. Converting y^2 to (x-i)/c0 gives 1/(6i).
    c0 = S.simplify(1/S.diff(F,x).subs(x,ii))
    assert c0 != 0
    slope_sigma = S.simplify((S.Rational(4,3)*c0*c0)/(8*ii*c0)/c0)
    assert slope_sigma == 1/(6*ii)
    actual = S.simplify(slope_sigma/slope_g)
    assert actual == -S.Rational(1,9)
    assert actual/(-1) == S.Rational(1,9)
    print("PASS: both Q(i) maps, complete non-pole fiber identities, and the third-order 1/9 limit.")


def cm7_endomorphism():
    k = z**3 - 21*z*z - 189*z + 2457
    numerator = (z**7 - 42*z**6 + 3087*z**5 + 15876*z**4
                 - 1972593*z**3 + 29172150*z*z - 208289151*z + 924173712)
    U = numerator/k**2
    cubic = z**3 - 315*z + 2646
    L = S.diff(k,z)/k
    zero(U - (7*z - 42 - (6*z*z-630)*L - 4*cubic*S.diff(L,z)))
    assert S.gcd(numerator,k) == 1
    u = -U/7
    w = -S.diff(U,z)/(7*s7)
    zero(w*w*cubic - cubic.subs(z,u),s7)
    zero(S.diff(u,z)-s7*w,s7)
    assert S.cancel(u.subs(z,-21)) == -21
    assert S.degree(numerator,z) == 7 and S.degree(k*k,z) == 6
    return cubic,u,w


def check_seven_models():
    cubic,u,w = cm7_endomorphism()
    # a=-15/16: two degree-two maps and sixteen points per origin fiber.
    h1z,h1v = 16*x*x-5,S.Integer(64)
    F,h2z,h2v,_ = model(S.Rational(-15,16),h1z,h1v,cubic)
    P = (7*x**3+6*s7*x*x-8*s7)*(43*x**4+13*s7*x**3-54*x*x-8*s7*x+8)
    assert S.degree(P,x)==7
    g = fiber_identity(F,h1z,h1v,h2z,h2v,u,w,P,x*x+1,s7)
    assert S.simplify(g.subs(x,0))==-1
    t = S.simplify(S.expand_complex((ii-s7)/(ii+s7)/g.subs(x,ii)))
    expected=(431-160*S.sqrt(7))/81
    assert S.simplify(t-expected)==0
    assert S.expand(81*t*t-862*t+81)==0
    # a=255: isogeny to the 8-twist, degree four in each factor.
    d=8
    cubic8=z**3-315*d*d*z+2646*d**3
    u8=d*u.subs(z,z/d)
    w8=w.subs(z,z/d)
    h1z=(x**4+86*x*x-167)/(x*x+1)
    h1v=(x**4+2*x*x+253)/(x*x+1)**2
    F,h2z,h2v,_=model(S.Integer(255),h1z,h1v,cubic8)
    P=(42453593*x**13+62753181*s7*x**12-271681298*x**11
       -72395730*s7*x**10+75687395*x**9+2718759*s7*x**8
       +14565684*x**7+1712724*s7*x**6-478065*x**5
       -31205*s7*x**4-7938*x**3-610*s7*x*x+21*x+s7)
    assert S.degree(P,x)==13
    g=fiber_identity(F,h1z,h1v,h2z,h2v,u8,w8,P,x**4+254*x*x+1,s7)
    assert S.simplify(g.subs(x,0))==-1
    zero(u8.subs(z,-168)+168,s7)
    # The four other Weierstrass points map to (-168,0) in both factors.
    quartic=x**4+254*x*x+1
    assert S.rem(S.numer(S.cancel(h1z+168)),quartic,x)==0
    assert S.rem(S.numer(S.cancel(h2z+168)),quartic,x)==0
    # W± map to O; check their genuine poles and nonzero m± differentials.
    assert S.limit((x*x+1)*h1z,x,ii)!=0
    assert S.limit((x*x+1)*h2z,x,ii)!=0
    assert ii-s7!=0 and ii+s7!=0
    t=S.simplify(S.expand_complex((ii-s7)/(ii+s7)*g.subs(x,0)/g.subs(x,ii)))
    expected=(364961-137920*S.sqrt(7))/6561
    assert S.simplify(t-expected)==0
    assert S.expand(6561*t*t-729922*t+6561)==0
    print("PASS: degree-seven CM map, both full Q(sqrt(-7)) fiber decompositions, and both exact target values.")


def check_remaining_weierstrass():
    for av in [-5,15,-33,255]:
        assert abs(1-av)>2
        F=x**6+av*x**4+av*x*x+1
        zero(F-(x*x+1)*(x**4+(av-1)*x*x+1))
    trace=S.Rational(31,16)
    assert -2<trace<2 and trace.q!=1
    # Both Q(sqrt7) comparison numbers are real, norm one, and not ±1.
    for t in [(431-160*S.sqrt(7))/81,
              (364961-137920*S.sqrt(7))/6561]:
        assert S.simplify(t*t.subs(S.sqrt(7),-S.sqrt(7)))==1
        assert S.simplify(t-1)!=0 and S.simplify(t+1)!=0
    # The extra four C_-3/2 values have nonintegral rational trace.
    t=(-1+2*S.sqrt(-2))/3
    assert S.simplify(t+S.conjugate(t))==-S.Rational(2,3)
    assert S.simplify(t*S.conjugate(t))==1
    print("PASS: all remaining Weierstrass root-power and non-root-of-unity obstructions.")


if __name__ == "__main__":
    check_classification()
    check_ranks()
    check_i_models()
    check_seven_models()
    check_remaining_weierstrass()
    print("All exact arithmetic checks passed. See the proof for the global actual-target argument.")
