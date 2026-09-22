Verdict: Adequate (5/14)

The paper offers only a narrow foundation for its standardization case: it establishes that runtime indexing of tuples is a real need and that ABI constraints make existing tuple layouts unsuitable, but nearly every other necessary argument is asserted rather than demonstrated. The thinnest support concerns who is actually affected, how the problem is currently solved in practice, and whether any implementation experience backs the claimed benefits.

- The paper’s strongest support is the established point that existing tuples cannot be optimized for runtime indexing without breaking ABI, which gives the proposal a concrete technical motivation.
- The paper claims that switch-based access is not guaranteed to be fastest for many elements, but this remains an assertion without benchmarks or examples.
- The discussion of affected users rests on specializations for reference-supporting variant and optional, yet no evidence ties those users to the proposed tuple type.
- The most glaring omission is implementation experience: the paper allows for efficient techniques but provides no prototype, measurements, or real-world usage to show the design works or is adopted.
