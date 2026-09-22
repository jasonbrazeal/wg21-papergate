Verdict: Strong (9/14)

The paper offers solid grounding in existing practice and prior art, and it makes a credible conceptual case that the proposal completes the lambda model rather than inventing a new one. The thinnest support is the social and practical argument: it asserts broad relevance and interoperability benefits without showing failures in real code or library ecosystems, and its coordination story rests on the same unproven claims.

- The strongest support is implementation experience, with a publicly available GCC proof-of-concept and a credible report that the change required only modest work.
- The paper also establishes prior art well by showing how recent standard callable types have already moved toward respecting call-signature constness.
- The reasoning for why the standard is the right place is asserted mainly through the desugaring analogy, but the paper does not show that this framing is shared or sufficient in committee terms.
- The most glaring omission is evidence of who is affected: no real-world code, library, or user experience is cited to demonstrate that the absence of these captures is a practical problem rather than a widely felt inconvenience.
