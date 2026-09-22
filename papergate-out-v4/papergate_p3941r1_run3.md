Verdict: Adequate (4/14)

The paper gives a partial account of its standardization case, centered on the difficulties already encountered with `affine_on` and the existence of a prior design that this proposal would supersede. The support is thinnest where the paper should connect that design history to a concrete audience, a need for language or standard-library action specifically, and evidence beyond a brief mention of a fragile approach.

- The paper clearly establishes why the current `affine_on` specification became a problem and points to earlier discussion as the main motivation for revisiting it.
- The prior-art discussion is the strongest part of the case, since it identifies both the original `continues_on` approach and the reduced parameter requirements under the proposed affinity guarantee.
- The paper asserts a coordination constraint involving the receiver’s scheduler, but it does not yet show how that constraint is reconciled with other senders, schedulers, or existing practice.
- The paper does not establish who is affected, why this cannot be handled outside the standard library, or what implementation experience supports the specific design being proposed.
