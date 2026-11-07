"""Check the readable seven-digit certificate using only the Python standard library.
This checks the recorded linear algebra and arithmetic bounds. Recompute the
Frobenius data with scripts/compute_p5_residual.py; the analytic proof
is proofs/five_adic_residual_certificate.md.
"""
import json, sys
from pathlib import Path

q=5**7
path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parents[1]/'verification'/'p5_residual_certificate.json'
c=json.loads(path.read_text())
assert c['parameter_a']==-605 and c['p']==5
assert c['term_cutoff']==20 and c['coefficient_precision']==30
assert c['modulus']==q
M=c['frobenius_matrix'];pairs=[(0,1),(0,3),(2,1),(2,3),(4,1),(4,3)]
assert c['pairs']==[list(t) for t in pairs]
assert len(M)==5 and all(len(r)==5 for r in M)
assert all(M[i][j]%q==0 for i in range(5) for j in range(5) if (i-j)%2)
A=[[(int(r==s)-M[i][l]*M[k][m])%q for s,(l,m) in enumerate(pairs)]
   for r,(i,k) in enumerate(pairs)]
assert A==c['system_matrix']
x=c['normalized_cross_periods'];b=c['system_rhs']
assert all(sum(A[i][j]*x[j] for j in range(6))%q==b[i] for i in range(6))

def det_mod(a):
    a=[r[:] for r in a];d=1
    for j in range(len(a)):
        r=next(r for r in range(j,len(a)) if a[r][j]%5)
        if r!=j:a[r],a[j]=a[j],a[r];d=-d
        pivot=a[j][j]%q;d=d*pivot%q;iv=pow(pivot,-1,q)
        for r in range(j+1,len(a)):
            h=a[r][j]*iv%q
            a[r]=[(u-h*v)%q for u,v in zip(a[r],a[j])]
    return d%q
assert det_mod(A)==72576

def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))%q for j in range(len(b[0]))]for i in range(len(a))]

def characteristic_coefficients_small(a):
    if len(a)==2:
        return [1,-a[0][0]-a[1][1],a[0][0]*a[1][1]-a[0][1]*a[1][0]]
    tr=sum(a[j][j] for j in range(3));a2=mm(a,a)
    e2=(tr*tr-sum(a2[j][j] for j in range(3)))*pow(2,-1,q)%q
    det=(a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
        -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
        +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))
    return [1,-tr,e2,-det]
Me=[[M[i][j] for j in [0,2,4]]for i in [0,2,4]]
Mo=[[M[i][j] for j in [1,3]]for i in [1,3]]
assert all((u-v)%q==0 for u,v in zip(characteristic_coefficients_small(Me),[1,-5,5,-25]))
assert all((u-v)%q==0 for u,v in zip(characteristic_coefficients_small(Mo),[1,0,5]))
assert x==[21625,13695,57225,77593,71316,65694]
assert x[0]%625==375 and x[0]%125==0
assert c['odd_model_target_J']==2*x[0]*pow(-608,-1,q)%q==48500
# Explicit theoretical degree and finite arithmetic bounds, not trimmed degrees.
D=132+144*19;L=4;J=5
assert D==2868 and 5**L<=D-2<5**(L+1)
assert 5**J<=2*D-4<5**(J+1)
assert 30-3*L-J==13>=7
# The proof's matrix-tail base and right-hand-side logarithmic breakpoint checks.
assert 130+144*20<5**5
assert 5**5<=260+144*20<5**6
assert (5**6-260+143)//144==107
assert 5**6>=144*(3*6+5)+260
print('PASS: seven-digit matrix certificate, parity, characteristic polynomials, unit determinant,')
print('all six normalized periods, odd-model target, and theoretical precision parameters.')
print('(Integral nu_0 nu_1)/i = 21625 + O(5^7), of valuation3; J = 48500 + O(5^7).')
