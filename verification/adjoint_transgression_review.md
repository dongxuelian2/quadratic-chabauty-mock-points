# Independent review

Reviewed `adjoint_transgression.md` and `check_adjoint_transgression.py` on 2026-11-10. Ran the local standard-library checker; every assertion passed, including all 125 projective mod-25 lifts. No downloaded research code was executed.

## Verified conclusions

- For a = −157469, the point counts at 3 and 17 are 6 and 16. Both primes are good. The resulting projective Frobenius orders are 6 and 4; the stated subgroup argument correctly forces the projective mod-5 image to be PGL₂(F₅) ≅ S₅.
- The Sylow action is one Jordan block of size 3, with zero norm. Normalizer multipliers on H¹ and H² are respectively 4 and 1. The stable-elements argument therefore gives H¹(G,M) = 0 and H²(G,M) ≅ F₅.
- Restricted transgression is represented by ±F(σ⁵). Restriction to the Sylow subgroup is injective; consequently descent is equivalent to F(σ⁵) = 0. Changing the lift alters this value by the zero norm. This is one linear equation, potentially zero on a particular restricted subspace.
- Restricting the projective E[25] representation gives an equivariant map F₀ to the trace-zero congruence kernel. Kernel identification is understood relative to compatible torsion bases. Every lift has fifth power I + 5e, so F₀ has nonzero transgression. Thus the unrestricted transgression is surjective.
- The ordinary reduction at 5 is correct: independent enumeration gives #E(F₅) = 8 and trace −2. This differs from the supersingular a ≡ 0 mod 5 examples.

## Scope and limitations

The opening residual-target grid and rank certificate are external premises, not re-certified by this review and not needed for the finite-group proof. Neither the note nor the checker claims a finite Selmer dimension, membership of F₀ in a prescribed ray-class or local-condition subspace, or completion of the depth-two classification. Implementing the descent equation and propagated finite local conditions remains necessary.

The reviewed files do not contain the excluded denominator theorem, the −485 quartic calculation, or a PROOF index. Ordinary uses of the words “proof” and “proofs” concern the present argument only.

The newly reported sextic and construction of its normal closure are outside this completed review. Nothing was uploaded or published.
