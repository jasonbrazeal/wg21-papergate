Verdict: Strong (10/14)

The paper provides a reasonably specific case for standardizing `affine_on`, particularly through its discussion of scheduler affinity, prior art, and the limits of library-only implementations, but it leaves notable gaps around who would be affected and whether the design has been validated in practice. The strongest support comes from the concrete explanation of how the proposal interacts with existing scheduler queries and the standard’s current error-handling permissions. The thinnest areas are the absence of implementation experience and any discussion of the affected user base, which weakens confidence that the feature is ready for standardization.

- The paper grounds its motivation in a concrete coroutine behavior and connects it to the earlier `task` design, showing a clear lineage for the problem being solved.
- It explains why a library-only solution is insufficient by pointing to the standard’s allowance for throwing synchronization primitives, which gives a standards-level rationale.
- The coordination and interoperability section is specific about how `affine_on` would need to match the scheduler from `get_scheduler`, clarifying a key integration constraint.
- The paper does not address who is affected by the proposal, making it hard to judge the breadth or urgency of the need.
- There is no implementation experience cited, leaving the practical viability and performance implications of the design unexamined.
