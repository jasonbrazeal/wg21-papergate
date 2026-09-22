Verdict: Adequate (6/14)

The paper offers a solid conceptual foundation for why class invariants are a recurring and difficult design problem, and it clearly draws on prior language experience, but it does not adequately demonstrate that the specific facility it envisions belongs in the C++ standard. The reasoning is strongest when situating the problem in the broader history of contracts and language design, and thinnest when it comes to showing demand, implementability, and why existing mechanisms cannot cover the need.

- The discussion of prior art, especially the tensions around redundant checking and D’s limitations, gives real weight to the claim that this is a standardization-shaped problem.
- The paper repeatedly asserts that class invariants are a common request, but it does not supply evidence of who is asking or how widespread that need actually is.
- The absence of any implementation experience in a C++ compiler leaves the practical viability of the proposed rules entirely unproven.
- Most glaringly, the paper never addresses why a library-based or tooling-based solution would be insufficient, which is a fundamental gap in the standardization argument.
