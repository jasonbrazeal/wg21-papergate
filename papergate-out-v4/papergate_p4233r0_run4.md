Verdict: Weak (3/14, close to Adequate)

The paper offers a narrowly framed justification for its own standardization, resting almost entirely on continuity with prior hardening work and on sanitizer-based verification that the identified checks correspond to real out-of-bounds accesses. That support is thinnest around the core questions of why this belongs in the standard rather than in an implementation or library extension, and around any evidence of implementer engagement or coordinated adoption.

- The paper does establish why the checks matter by tying them to demonstrated out-of-bounds reads or writes in at least one major implementation.
- Its strongest contextual support is the presentation of this work as a follow-up to P3471 and P3697, though the prior-art discussion remains more assertion than analysis.
- The paper claims, but does not establish, that a library-only solution would be inadequate, offering only the sanitizer evidence as implicit support.
- It provides no substantive account of who is affected, why the standard is the necessary venue, or how the proposal interoperates with existing hardening modes and implementations.
