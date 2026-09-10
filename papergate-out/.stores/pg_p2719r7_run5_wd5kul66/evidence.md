# What the paper offers

## why it matters: supported with specifics
> Knowledge of the type being [de]allocated in a *new-expression* is necessary in order to achieve certain levels of flexibility when defining a custom allocation function.

## who is affected: not addressed

## prior art and alternatives: supported with specifics
> The new wording for the return type of allocation and deallocation operators should resolve CWG1676 “`auto` return type for allocation and deallocation functions”, as it follows the approach in CWG1669 “`auto` return type for `main`”.

## why the standard: not addressed

## coordination and interoperability: not addressed

## why a library will not do: supported with specifics
> Unfortunately, this has a number of problems, the most significant being that it’s not possible to distinguish the newly-introduced type-aware operator from existing template `operator new` and `operator delete` declarations.

## implementation experience: asserted, with nothing supporting it
> This is achieved via the use of an additional `std::type_identity<T>` tag argument that allows the provision of the concrete type to `operator new` and `operator delete`.
