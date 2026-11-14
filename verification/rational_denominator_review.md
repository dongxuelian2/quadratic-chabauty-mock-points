# Rational denominator review

The local theorem and exact attainability were independently derived and reviewed before publication. The reviewer checked the ramified base extension normalization (type I_(em) in the second model, not I_m), the addition-law argument at u=±1, the common model correction, and the rational point height m log_p(q)/2.

For the first model the published nodal duplication lemma yields the pointwise formula over the normalized extension. Independently, factoring the scaled cubic as z(z-r)(z-R), with v(r)=m and R a unit, and taking a square root of z-R after an unramified extension gives nodal coordinates U=z-r/2+w/sqrt(z-R), V=z-r/2-w/sqrt(z-R), with UV=r²/4. Their valuations recover the same component corrections.

Exact-image review includes the exceptional q=3, even m, square beta case: the residual unit-x conic has no solutions. Its count is q-1-2(beta/q), not merely a coarse lower bound. The saturated values are always attained.

Executed check_rational_denominators.py with Python standard-library exact arithmetic:

    PASS: exact residual conic counts and 6804 interior/saturated square-class checks.
    PASS: component-height difference formula.

Finite checks supplement the all-prime proof; they do not prove height identities or full Selmer membership. Rational parameters require the global height correction +(1/2)log_p(D), and their first local targets need not contain zero.
