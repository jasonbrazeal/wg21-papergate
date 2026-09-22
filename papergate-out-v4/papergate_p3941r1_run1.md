Verdict: Adequate (4/14)

The paper offers support for standardization mainly by documenting prior discussion and a design evolution around `affine_on`, but it does not build much of a case for why the feature belongs in the C++ standard or how it fits with existing practice. The thinnest parts concern the affected users, the need for a standard rather than a library solution, and any evidence from implementation experience.

- The strongest support is the discussion of prior concerns and alternatives, which grounds the proposed change in earlier review of `affine_on`.
- The paper also establishes that a task resuming on its original scheduler motivates a simpler one-parameter design for `affine_on`.
- The most glaring omission is any evidence about who is affected or what implementation experience supports the change, leaving the practical need largely unstated.
