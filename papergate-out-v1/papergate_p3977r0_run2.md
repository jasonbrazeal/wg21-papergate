Verdict: Strong (8/14, close to Adequate)

The paper provides a reasonably concrete rationale for why existing contract terminology is insufficient and why the distinction it draws has observable consequences for ABI and compiler behavior, but it leaves several standardization-facing questions largely unexamined. The strongest support is concentrated in the technical motivation and interoperability discussion, while the case for why this belongs in the standard rather than in guidance or a library is notably thin.

- The paper gives specific, technically grounded reasons why the proposed distinction matters, including its implications for ABI stability and caller-side check elision.
- It engages with prior art and existing terminology in enough detail to show where current language falls short.
- It does not address who is affected by the proposal or what implementation experience exists, leaving the practical demand unclear.
- The absence of any discussion of why the standard is the right venue is the most glaring omission, since the paper’s core contribution could plausibly be framed as terminology or guidance rather than normative wording.
