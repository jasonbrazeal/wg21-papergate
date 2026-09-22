Verdict: Adequate (6/14)

The paper offers a solid conceptual foundation for why class invariants matter and shows meaningful engagement with prior art, but much of the case for standardization remains asserted rather than demonstrated. The thinnest support appears where the paper needs to connect its motivating tension to concrete evidence about affected users, implementation viability, and why a library solution is insufficient.

- The strongest support is the established discussion of prior art, which credibly frames the design space and the need for a principled rule in C++.
- The paper establishes why runtime checking of invariants would be valuable, particularly as an extension to the C++26 Contracts facility.
- The weakest areas are the claims about how many users are affected and what implementation experience actually shows, since these are asserted without the supporting detail needed to carry the standardization argument.
- The most glaring omission is the lack of established evidence for why a library cannot address the problem, despite the paper’s appeal to zero-overhead and ABI concerns.
