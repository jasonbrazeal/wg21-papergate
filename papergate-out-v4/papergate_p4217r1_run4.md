Verdict: Adequate (4/14)

The paper offers only scattered, anecdotal support for its case, leaving most of its core claims asserted rather than substantiated. The thinnest areas are the fundamental justifications that cannot be supplied by implementation experience alone: why the standard itself must change, and why a library-level solution would be inadequate.

- The most concrete support is a reported implementation of the coalescing approach against NVIDIA’s reference implementation, though the paper does not show how that experience validates the proposed direction.
- Feedback from Ben Deane suggests at least one external codebase already treats an empty `when_all()` as well-formed and synchronous, lending some real-world corroboration to the affected-user claim.
- The paper asserts that the current restriction creates special cases and hanging behavior in generic algorithms, but it does not demonstrate those consequences with examples or analysis.
- The paper provides no argument for why the change belongs in the standard rather than in a library, and no coordination or interoperability evidence beyond a single maintainer’s comment.
