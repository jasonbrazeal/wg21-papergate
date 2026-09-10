Verdict: Adequate (7/14, close to Strong)

The paper gives a narrow but concrete rationale for removing these constructors, leaning on mailing-list sentiment and a small illustrative example, but it does not build a complete standardization case. The thinnest areas are the absence of implementation experience, any discussion of why a library-level solution would be insufficient, and coordination with affected specifications or implementations.

- The strongest support comes from the concrete example showing that exposing the constructors provides no observable value to users.
- The paper also cites SG9 discussion indicating expected breakage would be minimal and likely reveal already-questionable code.
- The argument for why this belongs in the standard is largely asserted rather than demonstrated, with no supporting evidence beyond the author’s belief.
- The paper does not address implementation experience, library alternatives, or coordination and interoperability concerns.
