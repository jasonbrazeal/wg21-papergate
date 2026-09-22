Verdict: Strong (10/14)

The paper offers substantial support in the areas that matter most for a language feature: it establishes why virtual function contract support is needed, shows credible prior art and alternatives, and provides implementation experience through a complete GCC implementation. The support is thinnest where the paper relies on broad claims about affected users, interoperability across components, and the necessity of standardization rather than a library solution, which are asserted but not demonstrated with concrete evidence.

- The strongest support is the implementation experience, with wording rebased on the current working draft and a complete implementation available in GCC.
- The paper also clearly establishes why the feature matters, particularly the current impossibility of using `pre` and `post` on virtual functions and the impracticality of manual repetition.
- Prior art and alternatives are well covered, including a critique of earlier C++ proposals and comparisons with Eiffel, D, and Ada.
- The most glaring omission is the lack of established evidence for who is affected, since the cited EWG poll and the general statement about billions of lines of code do not by themselves demonstrate the scale or urgency of real-world need.
