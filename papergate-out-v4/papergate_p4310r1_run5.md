Verdict: Strong (10/14)

The paper’s strongest support comes from its survey of production deployments, and that record carries the load across several of the questions a proposal must answer. The case for standardization itself is thinner: the arguments connecting the deployment evidence to a need for a standard response, and explaining why existing C++26 behavior or a library-level approach would not suffice, are asserted more than demonstrated.

- The paper convincingly establishes that every hardened implementation surveyed terminates or traps on a detected core-language violation, with none defaulting to continuation.
- The deployment record also supports the paper’s claim that the affected population is real and that the proposed response has implementation precedent.
- The paper claims, but does not fully establish, why the standard should prescribe this response rather than leaving it to implementations or aligning with the already-adopted C++26 hardening semantics.
- The most glaring omission is the explanation for why a library-level solution cannot deliver the same behavior, beyond a passing note about exception-handling cost.
