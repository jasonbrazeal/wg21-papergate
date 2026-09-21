Verdict: Adequate (7/14, close to Strong)

The paper provides uneven support for its own standardization, with concrete reasoning in some areas but little more than assertion in others. The thinnest support appears where the proposal relies on claims about code rarity, rewrite ease, and the impossibility of library solutions without offering evidence or experience.

- The strongest support comes from the discussion of prior art and alternatives, where the paper ties its approach to P3446R0 and gives a specific rule about `[[may_invalidate]]`.
- The rationale for why the feature matters is also grounded in concrete goals, namely provable safety and reducing false positives.
- The claim that the problematic code patterns are rare and easy to rewrite is asserted without examples or data.
- The paper does not address implementation experience or coordination with other proposals, leaving the practical path to standardization unclear.
