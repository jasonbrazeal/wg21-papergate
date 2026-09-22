Verdict: Adequate (6/14)

The paper gives a plausible account of why the current specification has failed to take hold and why practitioners might prefer a different rule, but it leans heavily on a single anecdote about one implementation and does not develop that evidence into a full case for changing the standard. The strongest material concerns alternatives and prior art, where the paper connects its proposal to earlier CWG decisions and competing implementation behavior. The thinnest support is in the areas that would justify standardization specifically—why the standard must change, why a library solution is insufficient, and whether there is meaningful implementation experience behind the proposed direction.

- The paper clearly grounds its proposal in the history of CWG 1395 and identifies concrete changes to the partial ordering rules as the intended alternative.
- It offers a useful, if limited, signal that current practice diverges from the specified rule, citing GCC, MSVC, and Clang behavior.
- The paper does not establish why the standard itself must be amended rather than leaving the situation to implementation discretion or other remedies.
- The most glaring omission is the absence of any demonstrated implementation experience with the proposed rules beyond a single reported source of bug reports.
