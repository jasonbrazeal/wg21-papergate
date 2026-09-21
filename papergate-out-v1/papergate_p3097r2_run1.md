Verdict: Excellent (12/14, close to Strong)

The paper grounds several of its key claims in concrete examples and prior work, but its support is uneven: the design rationale is well illustrated, while the evidence that the proposed approach has been validated in practice is largely asserted rather than demonstrated. The thinnest support concerns implementation experience and the breadth of affected users, where the paper leans on a single poll result and an unsubstantiated claim about prior implementations.

- The strongest support comes from the use of specific real-world examples, such as the Qt `QIODevice` interface, to illustrate why static substitutability models fail for common C++ patterns.
- The discussion of prior art and alternatives is concrete, clearly distinguishing this design from Eiffel, D, Ada, and earlier C++ proposals.
- The claim that all previous C++ proposals with assertion inheritance, including C++20 Contracts and GCC, failed to handle direct calls correctly is presented without supporting evidence or references.
- The only evidence of community interest is a single EWG poll, with no additional context about the affected developer population or the scale of the problem.
