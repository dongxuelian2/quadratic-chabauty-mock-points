import sympy as s
X,x,A=s.symbols('X x A'); i=s.I; k=2*i*A
F=(X-A)*(X**4-4*A*X**3+(4*A*A-16*A)*X*X+32*A*A*X-16*A**3)
f=x**6+(A+3)*x**4+(A+3)*x*x+1
assert s.cancel(F.subs(X,k/(x+i))-k**4*f/(x+i)**6)==0
# Differential multiplier (dX/Y)/(dx/y).
Om=s.cancel(s.diff(k/(x+i),x)*(x+i)**3/k**2)
assert s.simplify(Om+(x+i)/k)==0
assert s.simplify(-k/(x+i)*Om-1)==0
assert s.simplify(i*(k/(x+i)-2*A)*Om-x)==0
assert s.expand(s.diff(F,X).subs(X,A)-A**4)==0
F605=s.expand(F.subs(A,-608))
expected=X**5+3040*X**4+2967040*X**3+916766720*X**2+10788274176*X+2186423566336
assert s.expand(F605-expected)==0
assert s.Poly(F605,X,modulus=5)==s.Poly(X**5+X+1,X,modulus=5)
assert s.gcd(s.Poly(F605,X,modulus=5),s.Poly(s.diff(F605,X),X,modulus=5)).degree()==0
print('Odd model, both differential pullbacks, endpoint derivative, and p=5 good reduction: PASS')
print('No numerical Coleman integral or nonvanishing conclusion is computed by this script.')
