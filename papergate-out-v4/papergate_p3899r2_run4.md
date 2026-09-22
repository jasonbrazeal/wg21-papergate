Verdict: Strong (8/14)

The paper offers a credible but uneven case for standardization, resting most heavily on compiler behavior and the observation that the current wording is unclear. The support is thinnest around why a library solution would be inadequate and around the broader rationale for a core-language change beyond consistency with one implementation.

- The strongest support is the concrete implementation experience, since GCC 15 is reported to implement exactly the behavior being proposed.
- The paper also establishes that this is a matter of core-language and library coordination, aided by a survey of how major compilers treat constant-expression floating-point cases.
- The motivation for changing the core language is asserted more than demonstrated, with the main argument being a preference against divergence from the library.
- The most glaring omission is any real explanation of why a library-only approach cannot address the problem.
