#!/usr/bin/env python3
"""Exact transfer identities. Requires SymPy; rank/infinitude use Zywina
arXiv:2505.16960v1, Theorem 1.5 and Section 4, not numerical sampling."""
import sympy as s
t,a,A,x,X=s.symbols("t a A x X")
def zero(f): assert s.cancel(f)==0,s.factor(f)
def E(z):return z**3+A*z*z-A*z
def Ep(z):return z**3-2*A*z*z+A*(A+4)*z
zero(E(X)*(X*X+A)**2/X**4-Ep(E(X)/X**2))
zero(16*s.discriminant(E(X),X)-16*A**3*(A+4))
zero(16*s.discriminant(Ep(X),X)+256*A**3*(A+4)**2)
At=-8*t/(t+1);at=(3-5*t)/(t+1);scale=(t+1)/2
zero(at-At-3)
zero(scale**2*(-2*At)-4*t*(t+1))
zero(scale**4*At*(At+4)-2*t*(t+1)**2*(t-1))
inverse=(3-a)/(a+5)
zero(inverse.subs(a,at)-t);zero(at.subs(t,inverse)-a)
zero(s.diff(at,t)+8/(t+1)**2)
assert at.subs(t,0)==3 and at.subs(t,1)==-1
F=X**3+4*t*(t+1)*X*X+2*t*(t+1)**2*(t-1)*X
zero(16*s.discriminant(F,X)-2**9*t**3*(t+1)**7*(t-1)**2)
f=x**6+a*x**4+a*x*x+1
zero(s.discriminant(f,x)+64*(a-3)**6*(a+1)**2)
rhs=E(X).subs(A,a-3)
zero(rhs.subs(X,x*x+1)-f)
zero(rhs.subs(X,x**(-2)+1)-f/x**6)
zero(s.diff(x*x+1,x)/2-x)
zero(s.diff(x**(-2)+1,x)*x**3/2+1)
c4=16*A*(A+3);delta=16*A**3*(A+4)
zero(c4**3/delta-256*(A+3)**3/(A+4))
zero((c4**3/delta).subs(A,a-3)-256*a**3/(a+1))
print("PASS: isogeny, scaling, inverse, discriminants, quotient maps, differentials and j.")
print("Infinitude/rank one are supplied by Zywina's cited theorem and proof.")
