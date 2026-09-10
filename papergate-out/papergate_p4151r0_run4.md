Verdict: Adequate (4/14, close to Weak)

The paper offers only a narrow, name-focused rationale for its proposed change, leaving most of the standardization case unaddressed. The strongest support appears in its discussion of prior art and naming consistency, but the absence of any treatment of affected users, implementation experience, or why a library solution would not suffice leaves the proposal largely unsubstantiated.

- The paper grounds its argument in specific prior art by identifying the existing `std::execution` entities whose names contain “on” and explaining how the proposed change would affect that naming rationale.
- The paper provides a concrete reason for the change by arguing that rendering `affine_on` unary would undermine the meaning of “on” in its name.
- The paper does not identify who would be affected by the change or what the migration or compatibility impact would be.
- The paper offers no implementation experience, no discussion of why the standard rather than a library is the right venue, and no coordination or interoperability analysis.
