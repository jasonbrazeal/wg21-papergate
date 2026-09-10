# What the paper offers

## why it matters: supported with specifics
> Knowledge of the type being [de]allocated in a *new-expression* is necessary in order to achieve certain levels of flexibility when defining a custom allocation function.

## who is affected: asserted, with nothing supporting it
> Beyond these issues, a common problem in we see in the wild is codebases overriding the global (and untyped) `operator new` via the usual link-time mechanism and running into problems

## prior art and alternatives: supported with specifics
> [ Drafting note: The new wording for the return type of allocation and deallocation operators should resolve CWG1676 “`auto` return type for allocation and deallocation functions”, as it follows the approach in CWG1669 “`auto` return type for `main`”. ]

## why the standard: not addressed
> Since this adds complexity to the proposal and implementation and doesn’t provide great value, we are not pursuing it as part of this proposal.

## coordination and interoperability: not addressed

## why a library will not do: supported with specifics
> Unfortunately, this has a number of problems, the most significant being that it’s not possible to distinguish the newly-introduced type-aware operator from existing template `operator new` and `operator delete` declarations.

## implementation experience: asserted, with nothing supporting it
> This paper proposes an extension to *new-expressions* and *delete-expressions* to provide the concrete type being [de]allocated to the allocation functions.
