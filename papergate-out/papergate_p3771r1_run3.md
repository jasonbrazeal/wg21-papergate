Verdict: Strong (9/14)

The paper gives a partial but uneven account of why this facility belongs in the standard, with the clearest support concentrated in the motivation and the rejection of a library-only workaround. Its case is thinnest around implementation experience, coordination with other proposals, and any concrete evidence that the standard itself—rather than a library extension—is the necessary vehicle.

- The strongest support is the concrete explanation of why a library-only pattern would be error-prone and harder to test.
- The motivation is grounded in a real difficulty: conditionally avoiding non-`constexpr` types in otherwise `constexpr`-compatible code.
- The paper asserts continuity with prior `constexpr` work but does not show how this proposal coordinates with or depends on that work.
- The most glaring omission is the absence of any implementation experience, despite noting that a completely new implementation approach has been started.
