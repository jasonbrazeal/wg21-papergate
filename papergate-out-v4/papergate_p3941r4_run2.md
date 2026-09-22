Verdict: Weak (3/14, close to Adequate)

The paper offers only a partial account of its standardization case, strongest when it connects the current design to prior proposals and discussions, but thin almost everywhere else. Most of the material that would show a real need for standardization—affected users, implementation experience, why a library solution is insufficient, and interoperability—is simply missing, and the paper’s motivating claims about the importance of the change are asserted rather than demonstrated.

- The clearest support comes from the documented history of concerns with `affine_on` and the connection to prior work such as P3718R0 and the earlier `continues_on` approach.
- The paper claims that taking newly revealed aspects into account points toward a better design, but it does not establish why that design improvement matters enough to justify standardization.
- The paper does not establish who is affected by the problem or how the proposed change would improve their code in practice.
- The most glaring omission is the absence of any implementation experience, interoperability analysis, or explanation of why a library-level solution cannot achieve the same result.
