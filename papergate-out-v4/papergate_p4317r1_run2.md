Verdict: Strong (9/14)

The paper offers substantial support for the need to standardize its profile, especially through demonstrable implementation experience and a clear account of the affected populations and prior art. The thinnest parts are the arguments that this belongs in the standard rather than in a library and that the proposed machinery coordinates cleanly with existing standards and deployment paths.

- The strongest support is the live prototype and the evidence that production hardening and sanitizers already implement much of the same enforcement model.
- The paper clearly establishes that the relevant user base includes both mainstream hardening deployments and gaps reported by prototype compiler studies.
- It also situates the design well against prior art, showing how existing sanitizers, library assertions, and Contracts differ in routing or coverage.
- The most glaring omission is the absence of a developed case for why a library cannot provide the same capability outside the standard.
