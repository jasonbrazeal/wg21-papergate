Verdict: Strong (11/14, close to Excellent)

The paper offers a reasonably grounded case for standardization, with concrete references to NB comments, prior art, and standardese that justify the change, though the support is uneven and leans heavily on specification-level reasoning rather than practical evidence. The thinnest area is implementation experience, which is asserted but not substantiated, leaving the reader to take the fragility and surprise claims on faith.

- The strongest support comes from the specific NB comments and the explanation of how the current specification permits scheduler changes that can fail in problematic ways.
- The discussion of prior art and the rationale for tying `affine_on` to the receiver’s environment gives the proposal a clear design anchor in the existing framework.
- The paper does not address who is affected by the change, which weakens the case for urgency or broad relevance.
- Implementation experience is merely asserted, with no examples, code, or reports to back the claim that the existing approach was fragile and surprising.
