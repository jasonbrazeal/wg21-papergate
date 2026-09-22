Verdict: Strong (10/14)

The paper gives a clear account of why `$` in identifiers matters for C++ and has solid evidence that implementations already support the extension, but its broader case for standardization rests heavily on assertions that are not backed up with concrete detail. The thinnest support appears where the paper needs to show who is affected, why the standard itself must change, and that other approaches would not suffice.

- The strongest support is the implementation experience, with multiple named compilers and a measurable body of existing code using the extension.
- The paper also clearly establishes the prior art, especially the C committee’s treatment of `$` in identifiers and existing compiler-specific workarounds.
- The claim that this is a widespread and important compatibility issue is repeated, but the paper does not show much evidence about the affected communities or the practical consequences for them.
- The most glaring omission is the argument for why the standard must change rather than leaving the behavior as a common extension, particularly when alternatives and library-like workarounds are mentioned but not convincingly dismissed.
