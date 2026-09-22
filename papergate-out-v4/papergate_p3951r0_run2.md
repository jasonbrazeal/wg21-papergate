Verdict: Strong (8/14)

The paper establishes a meaningful motivation for the feature and demonstrates some real implementation experience, but it leaves several essential parts of the standardization case asserted rather than argued. The thinnest support concerns why the standard, rather than a library or existing machinery, is the right home for the idea.

- The paper’s strongest support is its concrete motivation: as replacement fields multiply, format strings become hard to read and easy to misorder, and the debugging value of exposing all relevant information is clear.
- The discussion of prior art and alternatives is also well grounded, since it compares the proposal against P3294R2, P3412, and P1819 and explains the intended design space.
- Implementation experience is established through the author’s Clang branch, giving the idea at least some practical grounding.
- The most glaring omission is that the paper does not adequately establish who is affected beyond the unsupported claim that string interpolation is widely popular, nor why this needs standardization or why a library cannot suffice.
