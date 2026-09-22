Verdict: Strong (10/14)

The paper builds a reasonably strong case for the core feature, particularly by grounding it in concrete implementation experience and explaining why existing tools like immediately invoked lambdas fall short. The thinnest parts of the argument concern the human and ecosystem dimensions: the paper does not establish who is affected or demonstrate clear coordination with related work beyond assertions of relevance.

- The paper shows the most support through working implementation experience, with links to a clang implementation and a live compiler explorer demonstration.
- The paper clearly establishes the motivation and why a standard language feature is needed, especially where control flow like `return`, `break`, and `continue` cannot be handled by library or lambda-based workarounds.
- The paper treats prior art and alternative spellings seriously, including earlier revisions and rejected forms, which helps situate the proposal.
- The most glaring omission is the failure to establish who is affected or to substantiate the claimed coordination with pattern matching and macro desugaring in concrete design terms.
