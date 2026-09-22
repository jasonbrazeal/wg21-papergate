Verdict: Weak (2/14)

The paper offers only a preliminary outline of its problem space, with its central motivation and the existence of affected users asserted rather than demonstrated. The thinnest support appears around the fundamental question of why standardization is required, as well as around alternatives, interoperability, implementability, and the limits of library-only solutions.

- The strongest element is the paper’s acknowledgment of prior work, particularly its reference to P0784R5 and the composability concerns that kept persistent `constexpr` allocations out of C++20.
- The claim that the feature would unlock construction of complex compile-time data structures for runtime use is stated, but not supported with concrete examples or evidence of need.
- The paper does not establish who would be affected beyond citing one earlier proposal.
- It leaves entirely unaddressed why a library cannot achieve the goal, why the standard is the right venue, and whether any implementation experience exists.
