Verdict: Adequate (5/14)

The paper offers meaningful but incomplete support for its own standardization. Its strongest moments connect the proposal to existing precedent and to a recognized safety gap, but large parts of the standardization case—especially who is affected, why a library solution is insufficient, and whether anyone has implemented the idea—are left unaddressed.

- The paper establishes why the problem matters by pointing to the lack of bounds checking in view classes and the resulting safety concerns.
- The paper establishes credible prior art by referencing `span` and `string_view`’s existing `at()` methods and P2278’s `cbegin()`/`cend()` approach.
- The paper claims but does not establish that extending `at()` to generic views requires standardization rather than a library solution.
- The paper offers no evidence about who is affected, implementation experience, or coordination with existing practice.
