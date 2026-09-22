Verdict: Strong (8/14)

The paper makes a real case that enumerating and categorizing core-language undefined behavior is a worthwhile exercise, but its support for actually standardizing the proposed mechanisms is much thinner. The strongest material concerns the problem framing and available prior work; the weakest concerns the specific need for a standard, interoperability story, and evidence that the suggested semantics are implementable and sufficient in practice.

- The paper effectively establishes why reducing undefined behavior matters for C++ and shows familiarity with existing tools and proposals in this space.
- The paper claims a standard contract-violation-handling API could unify existing sanitizer callbacks, but it does not establish that such coordination is achievable or that relevant implementations would adopt it.
- The paper points to widely deployed runtime checks and compiler options, but it does not demonstrate implementation experience with the particular standard mechanism being proposed.
- The paper repeatedly asserts that standardization has benefits, but it does not establish what those benefits are concretely or why a library-level approach could not deliver enough of them.
