Verdict: Strong (9/14)

The paper provides some concrete implementation evidence and a clear reading of the current standard, but it leaves several important parts of the standardization case unaddressed, particularly around who is affected and why a library-level solution would not suffice. The strongest support comes from compiler behavior and the standard’s own language about undefined behavior, while the rationale for changing the standard itself is largely asserted rather than argued.

- The paper gives specific compiler evidence, noting that Clang trunk and EDG follow the standard while MSVC diverges, which grounds the discussion in real implementation behavior.
- It clearly identifies the standard’s position that leaving a deallocation function via an exception leads directly to undefined behavior.
- The argument that the standard should be changed rests on the assertion that the only effect is to permit undefined behavior, with no supporting reasoning or examples beyond that claim.
- The paper does not discuss who is affected by the current rule or the proposed change, nor does it explain why a library-based approach could not address the concern.
