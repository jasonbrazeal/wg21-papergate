Verdict: Adequate (7/14, close to Strong)

The paper gives a clear but narrow rationale for relaxing the restriction, grounded mainly in consistency with existing practice and the precedent of a closely related defect fix. Its strongest material concerns the motivation and prior-art context, while the sections on user impact, implementation experience, and the need for a standard change rely on assertions that are not fully supported. The thinnest area by far is the absence of any argument for why a library solution would be insufficient.

- The paper’s most solid support is its explanation that the original restriction was adopted for simplicity rather than any demonstrated technical need, and that a recent related fix was deliberately minimal.
- The claim that users are likely already depending on the behavior because implementations accept it is plausible but not backed by concrete evidence or reported usage.
- The assertion that most or all implementations accept the change is vague and partly inconsistent, weakening the implementation-experience case.
- The proposal does not address whether a library-level approach could serve the same purpose, leaving a significant gap in the standardization argument.
