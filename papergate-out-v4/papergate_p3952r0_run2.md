Verdict: Strong (8/14)

The paper’s strongest backing comes from concrete implementation experience, including a description of an existing Clang prototype and prior art in Boost and LLVM that maps directly onto the proposed name. Beyond that, the document leans heavily on assertions rather than demonstrated need: its claims about widespread use, type-safety risks, reliance on unspecified behavior in standard library components, and the inadequacy of a non-standard library solution are asserted but not substantiated with evidence or analysis. The thinnest support is in the most fundamental areas—why this needs to be standardized at all, and why a library cannot address the problem.

- The proposal clearly establishes prior art and implementation experience, including an existing Clang prototype and named functions in Boost and libc++.
- The paper links the proposed name to existing practice, which gives the naming choice some grounding in precedent.
- The case for who is affected rests on a list of projects but does not establish the scope or significance of the problem they face.
- The most glaring omission is a substantiated argument for why standardization is necessary rather than leaving this to existing libraries or unspecified implementation techniques.
