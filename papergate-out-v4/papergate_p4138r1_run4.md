Verdict: Adequate (6/14)

The paper gives a reasonably solid account of existing implementation behavior and the historical origin of the special treatment for unqualified member functions, but it leaves the standardization argument incomplete in some important respects. The support is strongest where the paper documents compiler agreement and divergence, and thinnest where it needs to explain why the core language—rather than guidance, tooling, or library-level work—is the necessary venue for a fix.

- The paper clearly establishes implementation experience by documenting concrete compiler behavior across multiple cases, including Clang’s existing rejection of certain overload pairs.
- The prior-art discussion is convincingly grounded in N1821 and in current wording that shapes how object parameters correspond.
- The claim about who is affected leans entirely on the compiler-agreement examples without demonstrating the practical impact on users or codebases.
- The paper does not establish why standardization is required, nor why the problem cannot be addressed outside the standard through a library or other means.
