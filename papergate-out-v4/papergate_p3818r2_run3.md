Verdict: Strong (8/14)

The paper makes a solid case for the existence and mechanics of the problem, but its supporting evidence becomes noticeably thinner when it moves from describing the breakage to justifying who is actually hurt and why a library-side or educational workaround cannot suffice. The strongest material concerns implementability and the narrow standardese change needed to avoid silent behavior change.

- The proposal clearly establishes that the interaction with potentially-constant initialization creates surprising silent breakage, and that the fix requires a standard change to make evaluation fail when these two functions are reached.
- The implementation experience is concrete and linked, showing the change has been prototyped and exercised in a compiler.
- The paper only claims, rather than demonstrates, that a meaningful population of users is affected by the trend of running tests in the constant evaluator.
- The most glaring omission is evidence for why a library will not do: the document asserts that non-`constexpr` functions make storing and reusing exceptions impossible and that workarounds would be unacceptable, but it does not establish that claim with examples or user experience.
