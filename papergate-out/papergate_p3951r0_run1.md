Verdict: Excellent (13/14)

The paper grounds its standardization case in concrete implementation experience, prior-art comparisons, and a clear rationale for why a language feature is preferable to a library approach. The support is thinnest when it comes to demonstrating who is actually affected or why the feature’s popularity translates into a C++ need, since that claim is asserted rather than evidenced.

- The strongest support comes from the author’s working Clang implementation, which shows the feature is small enough to build and evaluate in practice.
- The discussion of prior WG21 papers and the rejection of token sequence injection gives the proposal a realistic, bounded scope within the committee’s trajectory.
- The explanation of why a library solution falls short is specific about laziness, opacity, dangling references, and limited usage.
- The most glaring omission is any substantiation of the claim that string interpolation is “wildly popular” or that C++ users are meaningfully affected by its absence.
