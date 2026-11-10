"""Exact elementary checks; no finite Selmer/ray-class computation claimed."""
P=5

def mul(a,b):
 return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b)))%P for j in range(len(b[0]))) for i in range(len(a)))
def add(a,b): return tuple(tuple((x+y)%P for x,y in zip(r,s)) for r,s in zip(a,b))
def eye(n):return tuple(tuple(int(i==j) for j in range(n)) for i in range(n))
def power(a,n):
 r=eye(len(a))
 while n:
  if n&1:r=mul(r,a)
  a=mul(a,a);n//=2
 return r

def rank(a):
 a=[list(row) for row in a];r=0
 for j in range(len(a[0])):
  pivot=next((i for i in range(r,len(a)) if a[i][j]),None)
  if pivot is None:continue
  a[r],a[pivot]=a[pivot],a[r]
  c=pow(a[r][j],-1,P);a[r]=[c*x%P for x in a[r]]
  for i in range(len(a)):
   if i!=r:
    c=a[i][j];a[i]=[(x-c*y)%P for x,y in zip(a[i],a[r])]
  r+=1
 return r

def projective_order(a):
 for n in range(1,121):
  b=power(a,n)
  if b[0][1]==b[1][0]==0 and b[0][0]==b[1][1]!=0:return n
 raise AssertionError('order not found')

a=-157469;A=a-3
assert A==-32*7*19*37
for ell,expected,expected_order in [(3,6,6),(17,16,4)]:
 assert (16*A**3*(A+4))%ell
 pts=[(x,y) for x in range(ell) for y in range(ell) if (y*y-x**3-A*x*x+A*x)%ell==0]
 count=len(pts)+1;trace=ell+1-count
 assert count==expected
 companion=((0,-ell%P),(1,trace%P))
 assert projective_order(companion)==expected_order
 print(f'ell={ell}, #E={count}, trace={trace}, projective order={expected_order}')

# Conjugation by upper unipotent, in the basis e,h,f of sl_2.
U=((1,3,4),(0,1,1),(0,0,1))
N=((0,0,0),)*3
for k in range(5):N=add(N,power(U,k))
assert N==((0,0,0),)*3
UmI=tuple(tuple((U[i][j]-int(i==j))%P for j in range(3)) for i in range(3))
assert rank(UmI)==2
assert rank(power(UmI,2))==1
assert power(UmI,3)==((0,0,0),)*3
D=((2,0,0),(0,1,0),(0,0,3))
Dinv=((3,0,0),(0,1,0),(0,0,2))
assert mul(mul(D,U),Dinv)==power(U,2)
assert 3*3%5==4 # H1 normalizer multiplier
assert 3*2%5==1 # H2 normalizer multiplier
print('Sylow norm=0; rank(u-1)=2; H1 multiplier=4; H2 multiplier=1')
print('PASS. Stable-elements and transgression proofs are separate mathematical arguments.')

# Every projective lift of u modulo25 has the same nontrivial fifth power.
def mm25(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))%25 for j in range(2)) for i in range(2))
def pp25(a,n):
 r=((1,0),(0,1))
 for _ in range(n):r=mm25(r,a)
 return r
u25=((1,1),(0,1))
for aa in range(5):
 for bb in range(5):
  for cc in range(5):
   # representatives modulo scalar: all trace-zero kernel matrices
   kernel=((1+5*aa,5*bb),(5*cc,1-5*aa))
   assert pp25(mm25(kernel,u25),5)==((1,5),(0,1))
print('PASS: all125 projective mod25 kernel lifts have fifth power I+5e.')
