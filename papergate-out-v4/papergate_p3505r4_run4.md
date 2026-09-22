Verdict: Strong (9/14)

The paper offers solid grounding for the proposal through established implementation experience and a credible account of the problem’s significance, but its case for standardization is thinner where it must show why a standard library change is indispensable and how the work coordinates with existing practice. The strongest support is concrete and practical; the weakest areas rely on assertion or implication rather than demonstrated necessity.

- The paper clearly establishes why the current behavior is a meaningful problem by tying it to user surprise, performance regression, and inconsistency with widely used implementations.
- Implementation experience is well supported through references to the existing FMT implementation, its long availability, and described benchmark results.
- Prior art and the availability of alternative implementations are established, though the paper only claims rather than demonstrates that a library-level solution cannot suffice.
- The most glaring omission is the lack of established evidence for why standardization itself is required, since the paper does not show what would remain broken or impossible without a standard change.
