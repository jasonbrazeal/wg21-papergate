Verdict: Strong (9/14)

The paper grounds its case solidly in existing practice and the practical consequences of leaving that practice unacknowledged, but it gives almost no attention to why a design change to the core language is the right vehicle, and its evidence about implementation coverage is more suggestive than documented. The strongest support is concentrated in the problem description and the need for standard acknowledgment, while the weakest parts concern alternatives and actual implementation experience.

- The paper establishes clearly that `$` in identifiers is a widely used extension whose pedantic ill-formedness causes real portability and compliance problems.
- It also shows that the standard currently offers no acknowledgment of this practice, which supports the need for some standardized recognition even if not full portability.
- The discussion of prior art and alternatives gestures toward WG14 N3145 and assembler workarounds but does not develop them into a persuasive comparison.
- Most glaringly, the paper never explains why a library-based or non-core-language mechanism could not address the concern.
