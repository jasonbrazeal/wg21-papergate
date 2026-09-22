Verdict: Strong (9/14)

The paper gives solid support for the existence of a widely deployed extension and for the practical shape of the mechanism it proposes, but it is much thinner when it comes to showing that the situation cannot be handled adequately through existing practice or non-standard means. The strongest parts of the case rest on concrete implementation evidence and a clear account of prior art; the weakest parts are the unelaborated claims about compliance pressure, the limits of compiler extensions in real environments, and why standardization itself is the necessary remedy.

- The paper clearly establishes implementation experience by pointing to a concrete Clang PR and naming numerous major compilers with longstanding support.
- The prior-art discussion is well grounded, including the contrast with C’s approach and the specific trade-offs among listed alternatives.
- The claim that compiler extensions create a compliance issue is asserted rather than developed, with no substantive explanation of the environments or requirements that make standardizing the extension necessary.
- The argument for why a library or existing asm-label workaround will not suffice is barely sketched, leaving the core “why the standard” question largely unsupported.
