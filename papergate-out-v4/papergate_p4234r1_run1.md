Verdict: Strong (9/14)

The paper’s support for its own standardization is uneven: it convincingly shows that the extension exists and is widely implemented, but it does not adequately establish who is affected at scale, why standardization—rather than continued reliance on extensions—is necessary, or how the change would interact with other parts of the standard and existing practice. The thinnest part is the absence of any discussion of why a library solution would be inadequate, leaving a basic rationale for standardization unaddressed.

- The strongest support is the implementation experience section, which documents support across major compilers and includes an implementation attempt, showing the proposal is grounded in real practice rather than speculation.
- The paper establishes prior art and alternatives by distinguishing C++ from C and comparing several possible approaches, including a preference for the least user-hostile option.
- The case for who is affected is weaker, relying on a single GitHub search and general claims of popularity without evidence about the prevalence of `$` in identifiers across relevant codebases.
- The most glaring omission is the failure to establish why a library will not do, since the paper never discusses whether the desired effect could be achieved through existing language or library mechanisms.
