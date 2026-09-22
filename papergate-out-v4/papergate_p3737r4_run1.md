Verdict: Strong (8/14)

The paper offers a solid grounding in existing implementation practice, particularly through its comparison of major standard libraries and its acknowledgment of MSVC’s nonconformance, but it leaves several justifications asserted rather than demonstrated. The thinnest support appears where the paper relies on general appeals to existing practice or WG21 habits without connecting them concretely to the proposed wording’s portability, coordination, or necessity.

- The strongest support comes from concrete implementation details, especially the table showing libstdc++ and libc++ already matching the proposal and the explicit note that nonzero-length arrays comply everywhere.
- The paper also clearly establishes why the zero-length case matters by tying it to observable divergence in size, alignment, and missing guarantees like trivial copyability.
- Prior art is credibly covered through the recognition that MSVC’s zero-length implementation is broken and ABI-locked, which frames the standardization target as the common denominator of the other two libraries.
- The most glaring omission is the failure to show that a library-level solution cannot address the problem, since the paper only mentions a bit_cast use case without demonstrating why non-standard guarantees or a different facility would be inadequate.
