Verdict: Excellent (12/14, close to Strong)

The paper provides substantial, concrete support for its standardization case through implementation data, historical context, and clear examples of the problem it addresses, though the rationale for why a standard change is necessary remains underdeveloped. The strongest evidence comes from compiler agreement across most test cases and the demonstration of how current behavior can silently break existing code, while the thinnest support lies in the absence of any discussion about why the standard itself—rather than implementation fixes or guidance—is the right venue.

- The paper grounds its case in concrete implementation evidence, showing that GCC and MSVC already conform while Clang and EDG diverge in specific, reproducible ways.
- The historical tracing of intent back to N1821 and the explanation of how adding a `this D` overload flips well-formed calls provide compelling motivation for addressing the inconsistency.
- The most glaring omission is the lack of any discussion about why standardization is required, leaving the reader to infer whether this is a defect report, a clarification, or a new feature.
