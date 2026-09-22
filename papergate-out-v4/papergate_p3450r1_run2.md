Verdict: Weak (2/14)

The paper offers only a thin account of the need for standardization, treating most of the central justifications as assertions rather than demonstrated facts. The thinnest support concerns the standards process itself: the proposal does not establish why the standard is the right venue, how the change would interoperate with existing practice, or what standardization would require beyond what a compiler extension or implementation strategy could provide.

- The strongest support is the author’s report of hitting the same obstacle while working on `constexpr std::format` in both `{fmt}` and libstdc++, which at least gestures toward practical implementation experience.
- The paper claims a runtime/constant-evaluation asymmetry involving `Base` and `Derived` objects, but it does not show why that situation actually occurs in conforming code or why it matters for a broad audience.
- The discussion of prior art and alternatives points to a previous proposal and a possible extension of `std::is_within_lifetime`, but it does not show how those approaches were evaluated or why they were insufficient.
- The most glaring omission is any case for why standardization is necessary at all, since the paper does not explain why a library solution or compiler-specific mechanism could not address the described need.
