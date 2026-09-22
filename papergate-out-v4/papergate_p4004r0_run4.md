Verdict: Adequate (7/14, close to Strong)

The paper offers some concrete motivation and useful context for revisiting CWG 1395, particularly around divergence between the specified rule and widespread implementation behavior. However, much of the supporting evidence is asserted rather than demonstrated, leaving the case for standardization thinner on details about affected users, interoperability, and actual implementation experience.

- The strongest support is the established observation that GCC, Clang, and MSVC do not follow the CWG 1395 resolution and that the current wording fails to resolve the relevant ambiguities.
- The paper also establishes that revisiting the resolution is motivated by a decade of non-adoption and real-world reports from the one implementation that did follow it.
- The thinnest support is the repeated reliance on the same few statements to claim who is affected, why a library cannot help, and what implementation experience exists, without additional evidence or detail.
- A notable omission is any substantive discussion of coordination and interoperability beyond saying existing practice seems reasonable to specify.
