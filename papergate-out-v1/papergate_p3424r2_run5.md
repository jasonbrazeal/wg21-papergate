Verdict: Strong (9/14)

The paper provides concrete implementation evidence and a clear account of current compiler behavior, but it leaves several parts of the standardization case unstated, especially around affected users and why a library-level solution is insufficient. The strongest support is technical and narrow, while the broader justification for a core-language change remains largely asserted rather than argued.

- The paper gives specific compiler observations, including Clang, EDG, and MSVC behavior, which grounds its implementation-experience claims.
- The rationale for changing the standard is asserted in a single sentence without elaboration on why disallowing the construct is the right normative outcome.
- The affected audience is not identified, so the practical impact of the change is unclear.
- The possibility of a library-based alternative is not discussed, leaving a gap in the case for standardization.
