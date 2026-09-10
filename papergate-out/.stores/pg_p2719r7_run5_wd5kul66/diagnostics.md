# Diagnostics

Verdict: Adequate (7/14, close to Strong)

Criteria addressed: 4 of 7. Points: 7 of 14. Unsupported quotes rejected: 14. Replies missing: 0.

## motivation - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 0/0/2  chunk 2: 2/2/2  chunk 3: 0/0/0  chunk 4: 0/0/0  chunk 5: 0/0/0
quote: Knowledge of the type being [de]allocated in a *new-expression* is necessary in order to achieve certain levels of flexibility when defining a custom allocation function.

## audience - grade 0
votes: chunk 1: 0/0/0  chunk 2: 0/0/0  chunk 3: 0/0/0  chunk 4: 0/0/0  chunk 5: 0/0/0
quote: (none validated)

## prior_art - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 0/0/2  chunk 2: 2/2/2  chunk 3: 2/2/2  chunk 4: 0/0/0  chunk 5: 0/0/0
quote: The new wording for the return type of allocation and deallocation operators should resolve CWG1676 “`auto` return type for allocation and deallocation functions”, as it follows the approach in CWG1669 “`auto` return type for `main`”.

## vehicle - grade 0
votes: chunk 1: 0/0/0  chunk 2: 0/0/0  chunk 3: 0/0/0  chunk 4: 0/0/0  chunk 5: 0/0/0
quote: (none validated)

## coordination - grade 0
votes: chunk 1: 0/0/0  chunk 2: 0/0/0  chunk 3: 0/0/0  chunk 4: 0/0/0  chunk 5: 0/0/0
quote: (none validated)

## insufficiency - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 2/2/2  chunk 2: 0/2/2  chunk 3: 0/0/0  chunk 4: 0/0/0  chunk 5: 0/0/0
quote: Unfortunately, this has a number of problems, the most significant being that it’s not possible to distinguish the newly-introduced type-aware operator from existing template `operator new` and `operator delete` declarations.

## implementation - grade 1
votes: chunk 1: 1/1/1  chunk 2: 0/0/0  chunk 3: 0/0/0  chunk 4: 0/0/0  chunk 5: 0/0/0
quote: This is achieved via the use of an additional `std::type_identity<T>` tag argument that allows the provision of the concrete type to `operator new` and `operator delete`.
