Verdict: Strong (10/14)

The paper provides meaningful support in key areas, particularly by grounding its motivation in the costs of optionality and by demonstrating existing implementation and interoperability practice. However, the case is uneven: the evidence that the affected audience is genuinely broad is asserted rather than shown, and the paper never explains why the same goal could not be achieved through a library or other non-core mechanism, leaving a significant part of the standardization rationale unaddressed.

- The strongest support comes from implementation experience, where the paper cites concrete assumptions in libstdc++, libc++, and Microsoft STL, as well as compiler support on targets with unusual pointer sizes.
- The paper also clearly establishes prior art and design alternatives, framing the choice among requiring the types, inventing new ones, or doing nothing.
- The discussion of why the standard should act is weaker, leaning on surveyed support without establishing that the affected community extends beyond already-conforming implementations.
- The most glaring omission is the absence of any argument for why a library-based solution would not suffice, leaving a core requirement for standardization unmet.
