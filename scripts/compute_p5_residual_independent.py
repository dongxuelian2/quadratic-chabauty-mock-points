from math import comb
p=5;N=30;q=p**N
def trim(a):
 while a and a[-1]==0:a.pop()
 return a or [0]
def add(a,b):
 c=[0]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]+=x
 for i,x in enumerate(b):c[i]+=x
 return trim([x%q for x in c])
def neg(a):return [(-x)%q for x in a]
def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):
    if y:c[i+j]=(c[i+j]+x*y)%q
 return trim(c)
def power(a,n):
 z=[1]
 while n:
  if n&1:z=mul(z,a)
  a=mul(a,a);n//=2
 return z
f=[1,0,-605,0,-605,0,1];f=[x%q for x in f]
F=power(f,5)
def divmodpoly(a,b):
 a=a[:];out=[0]*max(1,len(a)-len(b)+1)
 bi=pow(b[-1],-1,q)
 while len(a)>=len(b) and any(a):
  k=len(a)-len(b);v=a[-1]*bi%q;out[k]=v
  for j,t in enumerate(b):a[k+j]=(a[k+j]-v*t)%q
  a=trim(a)
 return trim(out),trim(a)
def red(a):return divmodpoly(a,F)[1]
def rmul(a,b):return red(mul(a,b))
def comp(a,h):
 out=[0]
 for c in a[::-1]:out=add(rmul(out,h),[c])
 return out
def inverse(a):
 z=[0]*6;z[5]=-1%q
 for k in range(5):z=rmul(z,add([2],neg(rmul(a,z))))
 assert rmul(a,z)==[1]
 return z
H=[0]*6;H[5]=1
fp=[(i*f[i])%q for i in range(1,len(f))]
for k in range(5):
 D=comp(fp,H);inv=inverse(D);H=add(H,neg(rmul(comp(f,H),inv)))
assert comp(f,H)==[0]
# Ordinary polynomial composition.
fh=[0]
for c in f[::-1]:fh=add(mul(fh,H),[c])
U,rem=divmodpoly(fh,F);assert rem==[0]
der=[(j*H[j])%q for j in range(1,len(H))]
P,rem=divmodpoly(der,power(f,4));assert rem==[0]
assert all(x%5==0 for x in P)
assert U[0]%5==1 and all(x%5==0 for x in U[1:])
assert all((H[j]-(1 if j==5 else 0))%5==0 for j in range(len(H)))
print('PASS regular endpoint lift modulo 5^'+str(N), 'degrees',len(H)-1,len(U)-1,len(P)-1)
print('P mod125',[v%125 for v in P])
print('H mod125',[v%125 for v in H])


from time import time
start=time()
def mul(a,b):
 if len(a)*len(b)<2500:
  c=[0]*(len(a)+len(b)-1)
  for i,x in enumerate(a):
   if x:
    for j,y in enumerate(b):
     if y:c[i+j]=(c[i+j]+x*y)%q
  return trim(c)
 width=( (min(len(a),len(b))*(q-1)**2).bit_length()+7)//8
 aa=int.from_bytes(b''.join((x%q).to_bytes(width,'little') for x in a),'little')
 bb=int.from_bytes(b''.join((x%q).to_bytes(width,'little') for x in b),'little')
 n=len(a)+len(b)-1;buf=(aa*bb).to_bytes(n*width,'little')
 return trim([int.from_bytes(buf[j*width:(j+1)*width],'little')%q for j in range(n)])
def scale(a,c):return trim([v*c%q for v in a])
T=20
v=add(U,[-1]);powers=[1];series=[1]
for n in range(1,T):
 powers=mul(powers,v)
 c=(-1)**n*comb(2*n,n)*pow(4**n,-1,q)%q
 series=add(series,scale(powers,c))
baseB=mul(mul(power(f,2),P),series)
Bs=[];Hp=[1]
for j in range(5):
 Bs.append(mul(Hp,baseB));Hp=mul(Hp,H)
Dmax=max(len(b)-1 for b in Bs);L=0
while 5**(L+1)<=Dmax-2:L+=1
S=5**L
w=[1];vs=[1]; inv4=pow(4,-1,q);invpow=1
for n in range(1,Dmax//2+1):
 val=-sum([-605,-605,1][k-1]*(2*n-k)*4**k*w[n-k] for k in range(1,min(3,n)+1))
 assert val%(2*n)==0;w.append(val//(2*n));invpow=invpow*inv4%q
 vs.append(w[-1]%q*invpow%q)
vv=[0]*(Dmax+1)
for j,vj in enumerate(vs):vv[2*j]=vj
def scaled_div(c,k,loss):
 v=0
 while k%5==0:k//=5;v+=1
 assert loss>=v
 return c*5**(loss-v)*pow(k,-1,q)%q
def reducehorizontal(g):
 D=len(g)-1;cv=mul(g[::-1],vv[:D+1]);h=[0]*(D-1)
 for k in range(3,D-1):h[k]=scaled_div(cv[D-k-2],2*k,L)
 kk=mul(h[::-1],vv[:D+1])
 K=[kk[D-j-5] for j in range(D-4)]
 rr=scale(g,S)
 rr+= [0]*(D+1-len(rr))
 for j,c in enumerate(K):
  if c:
   for k,ff in enumerate(f):
    if ff and j+k:
     ix=j+k-1;rr[ix]=(rr[ix]-(2*j+k)*ff*c)%q
 assert all(z==0 for z in rr[5:]),'bad reduction'
 return trim(K),rr[:5]
Ks=[];ms=[]
for g in Bs:
 k,m=reducehorizontal(g);Ks.append(k);ms.append(m)
assert all(z%S==0 for r in ms for z in r),'nonintegral M'
M=[[z//S for z in r] for r in ms]
assert all(M[i][j]==0 for i in range(5) for j in range(5) if (i-j)%2),'parity'
print('Reduction done seconds',round(time()-start,2),'D,L',Dmax,L,flush=True)
print('M mod15625',[[z%(5**6) for z in r] for r in M],flush=True)
pairs=[(i,k) for i in [0,2,4] for k in [1,3]]
D2=max(len(Ks[k])+len(Bs[i])-2 for i,k in pairs)
L2=0
while 5**(L2+1)<=D2+1:L2+=1
cs=[]
for i,k in pairs:
 d=add(scale(mul(Ks[k],Bs[i]),S),neg(mul(Ks[i],ms[k])))
 assert all(d[j]==0 for j in range(1,len(d),2))
 c=sum(scaled_div(v*((-1)**(j//2)),j+1,L2) for j,v in enumerate(d) if not j%2)%q
 cs.append(c)
AA=[[((1 if r==s else 0)-M[i][j]*M[k][l])%q for s,(j,l) in enumerate(pairs)] for r,(i,k) in enumerate(pairs)]
aug=[r+[b] for r,b in zip(AA,cs)]
for j in range(6):
 pivot=next(k for k in range(j,6) if aug[k][j]%5)
 aug[j],aug[pivot]=aug[pivot],aug[j]
 inv=pow(aug[j][j],-1,q);aug[j]=[z*inv%q for z in aug[j]]
 for k in range(6):
  if k!=j:
   c=aug[k][j];aug[k]=[(x-c*y)%q for x,y in zip(aug[k],aug[j])]
sol=[row[-1] for row in aug];exponent=2*L+L2;den=5**exponent
def val5(x):
 if not x:return N
 v=0
 while x%5==0:x//=5;v+=1
 return v
print('WORK N,T,L,L2',N,T,L,L2,flush=True)
print('scaled solution valuations',[val5(z) for z in sol],'scale exponent',exponent,flush=True)
if all(z%den==0 for z in sol):
 print('I_eo/i mod5^6',[z//den%(5**6) for z in sol],flush=True)
 print('original holomorphic I/i mod5^6',4*(sol[0]//den)%(5**6),flush=True)
print('seconds',round(time()-start,2),flush=True)
