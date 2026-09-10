# Diagnostics

Verdict: Strong (8/14, close to Adequate)

Criteria addressed: 4 of 7. Points: 8 of 14. Unsupported quotes rejected: 11. Replies missing: 0.

## motivation - grade 2
votes: chunk 1: 2/2/2  chunk 2: 2/2/2  chunk 3: 0/0/0  chunk 4: 0/0/0  chunk 5: 0/0/0
quote: Knowledge of the type being [de]allocated in a *new-expression* is necessary in order to achieve certain levels of flexibility when defining a custom allocation function.

## audience - grade 0
votes: chunk 1: 0/0/0  chunk 2: 0/0/0  chunk 3: 0/0/0  chunk 4: 0/0/0  chunk 5: 0/0/0
quote: (none validated)

## prior_art - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 0/1/1  chunk 2: 2/2/2  chunk 3: 2/2/2  chunk 4: 0/0/0  chunk 5: 0/0/0
quote: [ Drafting note: The new wording for the return type of allocation and deallocation operators should resolve CWG1676 “`auto` return type for allocation and deallocation functions”, as it follows the approach in CWG1669 “`auto` return type for `main`”. ]

## vehicle - grade 0 (UNSTABLE: votes cross zero)
votes: chunk 1: 0/0/0  chunk 2: 0/0/2  chunk 3: 0/0/0  chunk 4: 0/0/0  chunk 5: 0/0/0
quote: Since this adds complexity to the proposal and implementation and doesn’t provide great value, we are not pursuing it as part of this proposal.

## coordination - grade 0
votes: chunk 1: 0/0/0  chunk 2: 0/0/0  chunk 3: 0/0/0  chunk 4: 0/0/0  chunk 5: 0/0/0
quote: (none validated)

## insufficiency - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 2/2/2  chunk 2: 0/2/2  chunk 3: 0/0/0  chunk 4: 0/0/0  chunk 5: 0/0/0
quote: However, even when defining `T::operator new` in-class, the only information available to the implementation is the type declaring the operator, not the type being allocated.

## implementation - grade 2
votes: chunk 1: 2/2/2  chunk 2: 0/0/0  chunk 3: 0/0/0  chunk 4: 0/0/0  chunk 5: 0/0/0
quote: Based on implementation experience
