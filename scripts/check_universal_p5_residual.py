#!/usr/bin/env python3
"""Standard-library verification of the universal five-adic certificate.

The analytic parameter-degree and monic-remainder arguments are in the
companion proof. This checker verifies the exact arithmetic they reduce to.
"""
import argparse
import json
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path


def vp(n):
    if not n: return float('inf')
    n = abs(n); v = 0
    while n % 5 == 0: n //= 5; v += 1
    return v


def interpolate(values, modulus=125):
    """Exact Newton interpolation, with no modular nonunit division."""
    d = len(values)
    out = [F(0)] * d
    falling = [1]
    differences = values[:]
    for k in range(d):
        coefficient = F(differences[0], factorial(k))
        for j, c in enumerate(falling): out[j] += coefficient*c
        differences = [v-u for u,v in zip(differences,differences[1:])]
        nxt = [0]*(len(falling)+1)
        for j,c in enumerate(falling): nxt[j] -= k*c; nxt[j+1] += c
        falling = nxt
    assert all(c.denominator % 5 for c in out), 'nonintegral interpolant'
    return trim([c.numerator*pow(c.denominator,-1,modulus)%modulus for c in out])


def trim(a):
    while len(a)>1 and a[-1]==0: a.pop()
    return a


def padd(a,b,q=125):
    return trim([((a[j] if j<len(a) else 0)+(b[j] if j<len(b) else 0))%q
                 for j in range(max(len(a),len(b)))])


def pscale(a,c,q=125): return trim([x*c%q for x in a])


def pmul(a,b,q=125):
    r=[0]*(len(a)+len(b)-1)
    for j,c in enumerate(a):
        for k,d in enumerate(b): r[j+k]=(r[j+k]+c*d)%q
    return trim(r)


def psum(ps,q=125):
    out=[0]
    for p in ps: out=padd(out,p,q)
    return out


def peval(p,x,q=125):
    r=0
    for c in p[::-1]: r=(r*x+c)%q
    return r


def check(samples_path,polynomials_path):
    samples=json.loads(Path(samples_path).read_text())
    universal=json.loads(Path(polynomials_path).read_text())
    assert len(samples)==16
    pairs=[(i,k) for i in (0,2,4) for k in (1,3)]
    for b,s in enumerate(samples):
        assert s['b']==b and s['parameter_a']==5*b-5
        assert (s['p'],s['term_cutoff'],s['coefficient_precision'],s['modulus'])==(5,20,30,78125)
        assert s['theoretical_degree_bound']==2868
        assert s['pairs']==[list(p) for p in pairs]
        M=s['frobenius_matrix']; c=s['system_rhs']; z=s['normalized_cross_periods']; q=78125
        A=[[(int(r==t)-M[i][j]*M[k][l])%q
             for t,(j,l) in enumerate(pairs)] for r,(i,k) in enumerate(pairs)]
        assert A==s['system_matrix']
        assert all(sum(A[r][t]*z[t] for t in range(6))%q==c[r] for r in range(6))
        assert z[0]==s['normalized_target']
        assert s['odd_model_target_J']==2*z[0]*pow(s['parameter_a']-3,-1,q)%q
        for i in range(5):
            for j in range(5):
                assert M[i][j]%5 == (3 if (i,j)==(3,1) else 4 if (i,j)==(4,0) else 0)
    M=[[interpolate([s['frobenius_matrix'][i][j] for s in samples])
        for j in range(5)] for i in range(5)]
    c=[interpolate([s['system_rhs'][i] for s in samples]) for i in range(6)]
    assert universal['modulus']==125 and M==universal['M'] and c==universal['C']
    # Interpolation loses at most three digits; seven-digit data leave four.
    assert vp(factorial(15))==3
    assert max(vp(factorial(j)*factorial(15-j)) for j in range(16))==3
    assert 7-3>=3
    # Explicit theoretical bounds used in the proof, never trimmed degrees.
    D=132+144*19
    assert D==2868 and 5**4<=D-2<5**5 and 5**5<=2*D-4<5**6
    assert 30-2*4==22 and 22-4-5==13
    assert 16-4-4-5==3
    assert (130+144*20)**2*(260+144*20)==28448714000<5**15
    assert F(21,20)**3<5
    A=[[padd([int(r==t)],pscale(pmul(M[i][j],M[k][l]),-1))
        for t,(j,l) in enumerate(pairs)] for r,(i,k) in enumerate(pairs)]
    assert A==universal['system_matrix']
    z=universal['solution']
    assert z==[[0,75],[70,75,75],[100,0,25],[43,10],[66,100,100],[94,120,50]]
    assert [psum([pmul(A[r][t],z[t]) for t in range(6)]) for r in range(6)]==c
    # A mod5 = I-K, with only K_50=2, hence K²=0.
    A5=[[trim([x%5 for x in p]) for p in row] for row in A]
    for r in range(6):
        for t in range(6):
            assert A5[r][t]==[(int(r==t)-(2 if (r,t)==(5,0) else 0))%5]
    for b,s in enumerate(samples):
        assert peval(z[0],b)==s['normalized_target']%125
    # Exact CM automorphism polynomial identity, by clearing denominators.
    # (x-1)^6 f((x+1)/(x-1)) = -8 f(x).
    def exact_mul(a,b):
        r=[0]*(len(a)+len(b)-1)
        for j,c0 in enumerate(a):
            for k,d0 in enumerate(b): r[j+k]+=c0*d0
        return r
    def exact_pow(a,n):
        r=[1]
        for _ in range(n): r=exact_mul(r,a)
        return r
    out=[0]*7
    for k,coefficient in [(6,1),(4,-5),(2,-5),(0,1)]:
        term=exact_mul(exact_pow([1,1],k),exact_pow([-1,1],6-k))
        for j,v in enumerate(term): out[j]+=coefficient*v
    assert out==[-8,0,40,0,40,0,-8]
    assert F(-2,4)*(-2)==1  # determinant of the pullback matrix
    def prime(n): return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
    examples=[]
    for r in [19,619,859,1699,2179,3019,4219,5059]:
        assert r%40==19 and prime(r) and prime(8*r-1)
        a=3-32*r
        assert a%5==0 and a%16==3 and r%8==3
        examples.append(a)
    # Positive example a=35: two explicit descent classes on E, and the
    # class3 covering on E' is insoluble modulo9 for every primitive pair.
    assert 24**2==(-4)**3+32*(-4)**2-32*(-4)
    assert 1152==2*24**2 and -32==-2*4**2
    squares9={n*n%9 for n in range(9)}
    for u in range(9):
        for v in range(9):
            if u%3 or v%3:
                assert (3*u**4-64*u*u*v*v+384*v**4)%9 not in squares9
    assert 35%16==3 and 35%5==0 and 35-3==32
    print('PASS: all 16 seven-digit inputs and exact rational interpolation.')
    print('PASS: coefficientwise integral M,C polynomials; all six equations A*z=C mod125.')
    print('PASS: X(5b-5)=75b mod125, nilpotent mod5 reduction, and precision constants.')
    print('PASS: exact CM symmetry and deterministic prime-pattern examples:',examples)
    print('PASS: a=35 explicit descent classes and complete primitive mod9 obstruction.')
    print('Analytic coefficient tails and monic-remainder justification are in the proof.')


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('samples',nargs='?',default=Path(__file__).resolve().parents[1]/'verification/universal_p5_samples.json')
    p.add_argument('polynomials',nargs='?',default=Path(__file__).resolve().parents[1]/'verification/universal_p5_polynomials.json')
    a=p.parse_args()
    check(a.samples,a.polynomials)
