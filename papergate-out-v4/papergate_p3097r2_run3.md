Verdict: Strong (9/14)

The paper offers a reasonably strong case for treating virtual-function contracts as independent per-function assertions, with good grounding in prior art and the history of earlier C++ attempts. Its support is thinnest where it moves from technical motivation to the practical case for standardization, especially around affected users, interoperability, and implementation experience, which are asserted more than demonstrated.

- The strongest support is the paper’s engagement with prior C++ proposals and other languages, showing both the recurrence of the problem and why earlier inheritance-based designs failed.
- The paper clearly establishes why the limitation matters for virtual functions, explaining the expressible subset today and the mismatch with common real-world patterns.
- The paper only claims rather than establishes who is affected, relying on a single EWG poll and generic statements about C++’s scale rather than concrete evidence of demand.
- The most glaring omission is the lack of substantiated implementation or deployment experience beyond a passing reference to a GCC implementation, with no details on completeness or lessons learned.
