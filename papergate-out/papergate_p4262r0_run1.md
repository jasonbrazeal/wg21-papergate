Verdict: Excellent (12/14, close to Strong)

The paper provides substantial support for its standardization by grounding its motivation in concrete bug categories, prior art, and implementation experience, though it leaves a notable gap around the core standards-level rationale. The strongest material concerns comparisons with other languages and empirical compiler behavior, while the thinnest support is the absence of a principled rule for when invariants should hold within C++’s model.

- The paper convincingly documents real reentrancy bugs and ties them to a specific, recurring callback scenario.
- Prior art and alternatives are examined in detail, including Ada’s parameter checking and D’s restriction on public calls inside invariants.
- Implementation experience is backed by direct testing with DMD 2.112, lending credibility to the claims about compiler behavior.
- The most glaring omission is the lack of a standard-level justification explaining how the proposed rule fits C++’s compilation and access-control model.
