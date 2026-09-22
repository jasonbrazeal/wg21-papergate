Verdict: Weak (2/14)

The paper offers only a sketch of motivation and a passing reference to prior work, leaving most of the case for standardization unstated. The thinnest areas are the absence of any discussion of who would be affected, why the standard is the right layer for this change, how it coordinates with existing rules, or how the design has fared in practice.

- The strongest support is the paper’s connection of persistent `constexpr` allocations to a recognized gap between compile-time computation and runtime initialization cost.
- The paper points to earlier standardization discussion of the same general idea, though it does not explain how this proposal addresses the concerns that led to that idea being deferred.
- The paper gives no account of implementation experience, which leaves the feasibility and consequences of the approach entirely unsupported.
- Most glaringly, the paper never explains why the standard must change rather than solving the problem through a library or existing language mechanisms.
