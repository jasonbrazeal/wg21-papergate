Verdict: Excellent (13/14)

The paper gives concrete evidence for implementation experience, prior art, and interoperability, but it offers almost no direct argument for why this belongs in the standard rather than remaining a library. The thinnest part is the “why the standard” section, which asserts the protocol’s foundational role without explaining what standardization would enable that a shipped library cannot already provide.

- The strongest support comes from working implementations in Capy and Corosio, with real use across sockets, timers, TLS, and DNS.
- The paper also grounds its design in measured performance and a relevant SG4 poll, showing awareness of the surrounding ecosystem.
- The most glaring omission is any specific rationale for standardization itself, beyond the claim that the protocol is small and foundational.
