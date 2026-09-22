Verdict: Adequate (7/14, close to Strong)

The paper gives a reasonably solid conceptual case for consteval-only types as a language feature, but much of its support remains asserted rather than demonstrated, particularly around practical impact, implementability, and alternatives to standardization. The strongest footing is in connecting the feature to existing standardization activity and showing why a language rule, rather than a library convention, is needed for sound guarantees.

- The paper best establishes why standardization is necessary by explaining that consteval functions cannot guarantee consteval-only data and that a formal language notion enables reflection and prevents runtime leakage.
- It also clearly grounds the proposal in prior committee work, citing CWG3150, P4101R0, and std::meta::info as relevant context for why consteval-only types belong in the standard.
- The case for who is affected is thinner, relying on general claims about vectors, maps, and diagnostics without concrete evidence that real-world code commonly encounters the problem.
- The most glaring omission is implementation experience, where historical anecdotes and a claim of trivial implementation implications do not show that the feature has been built and validated in a modern compiler at scale.
