# A second CM norm-one-torus exclusion

## Theorem and convention

Let C:y²=x⁶+15x⁴+15x²+1 and b=(0,1). Its Jacobian has rational rank two. For every prime p≡1 mod4, neither (i,0) nor (−i,0) lies in the full depth-two set under the Mordell–Weil abelian-image convention of PROOF.md Section13.

The detecting central line is Q_p(1)χ_K for K=Q(s), s²=−3. The local obstruction is the nonzero torus Kummer class of −7+4sqrt(3), or its inverse. Both split and inert CM primes are covered. This is an additional unconditional curve beyond a=−5, not a classification of the whole depth-two set of C.

## 1. Elementary rank certificate

The common quotient is E:Y²=X³+12X²−12X, with two-isogenous E':Y²=X³−24X²+192X. Classical two-isogeny descent gives
2^rank E(Q)=|im δ_E| |im δ_E'|/4.

The image for E lies in {±1,±2,±3,±6}. The two-torsion point T=(0,0) gives −3, and (−2,8) gives −2, generating H={1,−3,−2,6}. Class2 would require a primitive integral solution
N²=2(U⁴+6U²V²−3V⁴).
If exactly one of U,V is odd, the right side has valuation1 at2. If both are odd, the bracket is4 mod8, giving valuation3. Both are impossible. Since the image is a group containing H, this excludes the entire other coset 2H. Thus its size is4.

For E', X³−24X²+192X=X((X−12)²+48), so nonzero rational X-coordinates are positive. The image lies in {1,2,3,6}, and T supplies3. Class2 would require
N²=2(U⁴−12U²V²+48V⁴).
For odd U the right side is2 mod8. Otherwise V is odd; put U=2k to obtain
N²=32(k⁴−3k²V²+3V⁴),
whose bracket is odd. Its valuation5 is impossible. Thus im δ_E'={1,3}, and rank E(Q)=1.

The point P=(1,1) is nontorsion. Its doubled X-coordinate is169/4; on the integral short model with z=X+4,
Y²=z³−60z+176,
the coordinate is185/4, incompatible with Nagell–Lutz for a torsion point. Therefore E(Q)⊗Q_p=Q_p P. The two independent elliptic quotient maps give J(C) isogenous to E² and hence rank two.

## 2. Exact CM endomorphism

Over K define
η_X=−X(X+6)²/[3(X−2)²],
η_Y=−Y(X+6)(X²−12X−12)/[3s(X−2)³].
These formulas preserve E and extend to an endomorphism of degree3. If η_Y=v(X)Y and η_X=u(X), direct calculation gives u'=s v, so η*ω=sω for ω=dX/(2Y). The map fixes T, satisfies η²=[−3], c(η)=−η and η†=−η. The square identity also follows from faithfulness of the characteristic-zero differential representation, after establishing that the map is an endomorphism.

The discriminants are Δ(E)=2^14·3³ and disc(C)=−2^26·3⁶. Thus all primes p≥5 are good.

## 3. Complete principal-divisor calculation

Set f1=(x²+1,y), f2=(1+x^(-2),y/x³) and f±=f1±η f2. Then
f±*ω=(x∓s)dx/y.
At b the pair is (P,O); at W=(±i,0) it is (T,T).

Writing F=x⁶+15x⁴+15x²+1, direct calculation gives
X(f1)−X(η f2)=(x²+1)(3x²+1)(x⁴+14x²+1)/[3x²(x²−1)²],
Y(η f2)/Y(f1)=−(7x²+1)(23x⁴+10x²−1)/[3s x³(x²−1)³].

All six Weierstrass points occur in BOTH origin fibers: f1 and η f2 are there the same nonzero two-torsion point. Each occurs simply since dx/y is nonzero and F(±s)=64.

The residual origin points of f+ are x=−s/3,y=±8s/9; those of f− are x=s/3,y=±8s/9. Indeed F(±s/3)=−64/27 and the Y-ratio is −1 or +1, respectively. They too are simple by the differential formula.

The exceptional charts add no origins: at x=0 the images are (1,±1); at infinity their X-coordinate is−49/3; at x=±1, η f2=O while f1≠O. Hence each origin divisor has exactly degree8: the six common Weierstrass points and its two stated residual points.

Consequently
g=(3x+s)/(3x−s),
div(g)=f+*(O)−f−*(O), g(0)=−1, c(g)=g^(-1).
The common six-point divisor is explicitly accounted for, rather than discarded from a denominator calculation.

## 4. Torus descent and the essential origin-fiber limit

Let D=E×E, M=O_E(O), m±(R,S)=R±ηS and
L=m+*M⊗m−*M^(-1).
Let σ be the ratio of the pullbacks of the canonical section of M. Conjugation exchanges the factors. Its identification c*L≅L^(-1), followed by inversion on nonzero vectors, descends L^× to a torsor X over D under T=Res^1_(K/Q) G_m.

For j=(f1,f2), the section j*σ/g is everywhere nonzero by the divisor identity, and descends to a morphism jtilde:C→X. At b the equal-fiber coordinate is
jtilde(b)=(P,O,−1).

At W=(i,0), both m+ and m− equal O. One MUST NOT substitute σ=1. Choose the same local parameter t=−X/Y and frame t^(-1) of M at O. The frame ratio equals1 in the identical-fiber identification. The section coefficient along C is t(f+)/t(f−). Its limit is
(j*σ)(W)=(i−s)/(i+s),
by the nonzero differential values above.

Put r=s/i, r²=3. Then g(i)=(3+r)/(3−r)=2+r and (i−s)/(i+s)=r−2. Therefore
jtilde(W)=(T,T,−(2−r)²)=(T,T,−7+4r).
Replacing i by−i inverts this coordinate.

## 5. Proper reference path and its sign

On E×{O}, the identical-factor trivialization of L has unit section e1. On {T}×E, m−=−m+; use the canonical symmetric linearization [−1]*M→M preserving the canonical section to obtain a unit section e2. These sections descend to Q: conjugation takes their trivializations to their inverses.

At (T,O), the common image is T≠O, and e1=e2=1 in the identical-fiber coordinate. At (T,T), the common image is O, where the symmetric linearization acts by−1 on M_O. This sign is forced by the odd local parameter t and its frame t^(-1). Thus e2 has coordinate−1 there.

Accordingly the proper sections −e1 and −e2 connect
(P,O,−1) → (T,O,−1) → q=(T,T,+1).
The reference endpoint is +1, not−1. Concatenating the two proper elliptic path torsors gives a rational global reference γ, crystalline at every p≥5 and unramified outside {2,3,p}. Its abelian projection is the Kummer class of (T−P,T), or (−P,0) after tensoring with Q_p.

## 6. A detecting depth-two quotient

The unipotent fundamental group of X has a central extension
1→W_T→U_X→V_pD→1, W_T=Q_p(1)χ_K.
As in PROOF.md Section15, this follows from the fundamental group of a torus bundle over an abelian variety and its nonzero Chern class. Relative to the product polarization, that class is represented by
m+†m+−m−†m−=[[0,2η],[−2η,0]]≠0.
The map j induces the isogeny J(C)→E², so the map from C factors through its full depth-two quotient and is surjective on the abelian graded quotient and this central line. The principal pullback divisor makes the required curve lift literal.

## 7. Global uniqueness in the central fiber

Rank one and nonzero local logarithm of P give injectivity of localization on D(Q)⊗Q_p, hence on the Mordell–Weil image of J(C). A hypothetical global class for W must thus have the same abelian projection as γ.

But
H^1_(f,{2,3})(Q,Q_p(1)χ_K)=0.
Restriction identifies this with the anti-invariant part of O_K[1/6]^×⊗Q_p. Ordinary units in the imaginary quadratic K are finite. The prime2 is inert and3 ramified, so each gives a single conjugation-invariant valuation direction. Crystallinity removes valuation directions above p; class groups contribute only torsion. Hence the anti-invariant group vanishes.

Retain the crystalline-fiber justification from Section15: U_X is a crystalline quotient of U2(C); twisting by the crystalline γ preserves this. Exactness of D_cris for the twisted Lie extension makes the connecting boundary from the abelian B_cris invariants vanish. A central difference between crystalline lifts therefore lies in H_f^1(Q_p,W_T). Ordinary H^0(Q_p,V_pD)=0 separately supplies freeness; it does not alone prove the crystalline assertion. At good primes away from p, absence of Frobenius eigenvalue1 gives the analogous unramified result.

Thus the hypothetical global class and γ must have identical localizations.

## 8. Nonzero local discrepancy

In the fiber over (T,T), the actual endpoint divided by q is
t_W=−7+4r, r²=3.
It has norm1, inverse−7−4r, and is a non-root-of-unity algebraic unit, as seen from a real embedding.

For p≡1 mod4, i∈Q_p. The CM algebra splits when p≡1 mod12 and is the unramified quadratic extension when p≡5 mod12. In either case restriction to a splitting field identifies the finite torus Kummer class with the norm-zero logarithm of this unit. A unit in a finite p-adic extension has zero logarithm only if it is a root of unity. The local class is therefore nonzero; restriction is injective on Q_p-cohomology by restriction–corestriction.

Since H^0(Q_p,V_pD)=0, this nonzero central class acts freely in the local fiber. It contradicts the global uniqueness just proved. The inverse class treats −i identically.

This argument uses neither sufficiency of scalar heights nor an ordinary-height nonvanishing assumption. The origin-fiber limit and the corrected reference sign are indispensable.
