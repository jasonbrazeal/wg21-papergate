# Diagnostics

Verdict: Strong (8/14, close to Adequate)

Criteria addressed: 5 of 7. Points: 8 of 14. Unsupported quotes rejected: 7. Replies missing: 0.

## motivation - grade 2
votes: chunk 1: 2/2/2  chunk 2: 2/2/2  chunk 3: 0/0/0  chunk 4: 0/0/0  chunk 5: 0/0/0
quote: Knowledge of the type being [de]allocated in a *new-expression* is necessary in order to achieve certain levels of flexibility when defining a custom allocation function.

## audience - grade 1 (UNSTABLE: votes cross zero)
votes: chunk 1: 0/1/1  chunk 2: 0/0/0  chunk 3: 0/0/0  chunk 4: 0/0/0  chunk 5: 0/0/0
quote: Beyond these issues, a common problem in we see in the wild is codebases overriding the global (and untyped) `operator new` via the usual link-time mechanism and running into problems

## prior_art - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 0/1/2  chunk 2: 2/2/2  chunk 3: 2/2/2  chunk 4: 0/0/0  chunk 5: 0/0/0
quote: [ Drafting note: The new wording for the return type of allocation and deallocation operators should resolve CWG1676 “`auto` return type for allocation and deallocation functions”, as it follows the approach in CWG1669 “`auto` return type for `main`”. ]

## vehicle - grade 0 (UNSTABLE: votes cross zero)
votes: chunk 1: 0/0/0  chunk 2: 0/0/1  chunk 3: 0/0/0  chunk 4: 0/0/0  chunk 5: 0/0/0
quote: Since this adds complexity to the proposal and implementation and doesn’t provide great value, we are not pursuing it as part of this proposal.

## coordination - grade 0
votes: chunk 1: 0/0/0  chunk 2: 0/0/0  chunk 3: 0/0/0  chunk 4: 0/0/0  chunk 5: 0/0/0
quote: (none validated)

## insufficiency - grade 2
votes: chunk 1: 1/1/2  chunk 2: 2/2/2  chunk 3: 0/0/0  chunk 4: 0/0/0  chunk 5: 0/0/0
quote: Unfortunately, this has a number of problems, the most significant being that it’s not possible to distinguish the newly-introduced type-aware operator from existing template `operator new` and `operator delete` declarations.

## implementation - grade 1
votes: chunk 1: 1/1/1  chunk 2: 0/0/0  chunk 3: 0/0/0  chunk 4: 0/0/0  chunk 5: 0/0/0
quote: This paper proposes an extension to *new-expressions* and *delete-expressions* to provide the concrete type being [de]allocated to the allocation functions.
