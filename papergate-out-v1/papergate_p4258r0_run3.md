Verdict: Adequate (4/14, close to Weak)

The paper provides only narrow, uneven support for its own standardization, leaning on a few concrete references while leaving most of the case unstated. The strongest material concerns prior art and observed implementation behavior, but the discussion of motivation, affected users, and why a library solution is insufficient is essentially absent.

- The paper grounds its discussion in a specific prior proposal and accepted change, giving readers a concrete standards-history anchor.
- It cites implementation experience from both libstdc++ and libc++, showing that current practice already diverges from the standard’s wording.
- The paper does not explain who is affected by the issue or why the change matters in practical terms.
- It offers no argument for why the standard, rather than a library or coding guideline, is the right place to address the problem.
