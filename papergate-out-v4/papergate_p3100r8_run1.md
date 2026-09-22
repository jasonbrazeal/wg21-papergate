Verdict: Strong (9/14)

The paper offers solid grounding for the general problem it addresses and for the existence of prior work, but its case thins considerably when it moves from motivation to evidence about who is concretely affected and why the feature belongs in the standard rather than in a library. The strongest material concerns the scope and tractability of undefined behavior and the surrounding ecosystem of tools and proposals; the weakest concerns actual implementation experience and the specificity of affected users.

- The paper convincingly establishes that reducing undefined behavior matters and that a large share of UB cases are in principle checkable at runtime, with prior art and alternatives well documented.
- The discussion of affected users remains more asserted than demonstrated, since the paper reports aggregate counts but does not show the practical impact on particular codebases or developers.
- The case for standardization over a library solution is thin, relying on general integration difficulties and a few sanitizer callback examples rather than showing why a standard core-language facility is required.
- Implementation experience is only gestured at through references to a companion paper and existing compiler flags, without enough detail here to establish that the proposed design has been meaningfully exercised.
