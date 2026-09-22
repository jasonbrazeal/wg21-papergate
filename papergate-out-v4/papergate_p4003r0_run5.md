Verdict: Strong (9/14)

The paper gives solid grounding on technical motivation, implementation experience, and prior art, especially through its reference implementations and direct use of C++20 coroutine machinery. The case for standardization is thinner where it relies on active-use claims, why a library cannot suffice, and how the proposal coordinates with or improves interoperability across existing async models.

- The strongest support is the demonstrated implementation experience, with multiple libraries built on the protocol and concrete reports of usage in timers, sockets, TLS, DNS, and HTTP.
- The paper firmly establishes why the problem matters by showing that current solutions force frame-allocation concerns into coroutine signatures and duplicate boilerplate.
- It clearly situates the design against prior art and available implementations, including Capy and Corosio, and explains the protocol’s divergence from executor-based approaches.
- The most glaring omission is positive evidence for the decision to standardize rather than continue as a library, since the mimalloc comparison and unique timing argument are only asserted, not yet supported by the paper itself.
